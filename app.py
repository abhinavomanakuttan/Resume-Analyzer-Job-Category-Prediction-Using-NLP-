import streamlit as st
import pickle
import docx
import PyPDF2
import re

# Load saved objects

svc_model = pickle.load(open("clf.pkl", "rb"))
tfidf = pickle.load(open("tfidf.pkl", "rb"))
le = pickle.load(open("encoder.pkl", "rb"))

# ---------------------------

# Text Cleaning Function

# ---------------------------

def cleanResume(txt):

    txt = str(txt)

    txt = re.sub(r'http\S+|www\S+|https\S+', ' ', txt)
    txt = re.sub(r'RT|cc', ' ', txt)
    txt = re.sub(r'#\S+', ' ', txt)
    txt = re.sub(r'@\S+', ' ', txt)

    txt = re.sub(
        r'[%s]' % re.escape("""!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""),
        ' ',
        txt
    )

    txt = re.sub(r'[^\x00-\x7f]', ' ', txt)
    txt = re.sub(r'\s+', ' ', txt)

    return txt.lower().strip()
    

# ---------------------------

# PDF Extraction

# ---------------------------

def extract_text_from_pdf(file):

    
    pdf_reader = PyPDF2.PdfReader(file)

    text = ""

    for page in pdf_reader.pages:
        page_text = page.extract_text()

        if page_text:
            text += page_text

    return text


# ---------------------------

# DOCX Extraction

# ---------------------------

def extract_text_from_docx(file):


    doc = docx.Document(file)

    text = ""

    for paragraph in doc.paragraphs:
        text += paragraph.text + "\n"

    return text


# ---------------------------

# TXT Extraction

# ---------------------------

def extract_text_from_txt(file):


    try:
        return file.read().decode("utf-8")

    except UnicodeDecodeError:
        return file.read().decode("latin-1")


# ---------------------------

# Handle Upload

# ---------------------------

def handle_file_upload(uploaded_file):


    extension = uploaded_file.name.split(".")[-1].lower()

    if extension == "pdf":
        return extract_text_from_pdf(uploaded_file)

    elif extension == "docx":
        return extract_text_from_docx(uploaded_file)

    elif extension == "txt":
        return extract_text_from_txt(uploaded_file)

    else:
        raise ValueError(
            "Unsupported file format. Upload PDF, DOCX, or TXT."
        )


# ---------------------------

# Prediction Function

# ---------------------------

def predict_category(resume_text):


    # Check if document is a resume
    if not is_resume(resume_text):
        return "Not Resume"

    # Clean text
    cleaned_text = cleanResume(resume_text)

    # TF-IDF Vectorization
    vectorized_text = tfidf.transform([cleaned_text])

    # Predict
    prediction = svc_model.predict(vectorized_text)

    # Convert numeric label to category name
    category = le.inverse_transform(prediction)

    return category[0]





def is_resume(text):

    text = text.lower()

    resume_keywords = [
        "education",
        "skills",
        "experience",
        "projects",
        "certifications",
        "internship",
        "work experience",
        "technical skills",
        "achievements",
        "phone",
        "email"
    ]

    score = 0

    for keyword in resume_keywords:
        if keyword in text:
            score += 1

    return score >= 3



# ---------------------------

# Streamlit UI

# ---------------------------



def main():
    
    st.set_page_config(
        page_title="Resume Analyzer",
        page_icon="📄",
        layout="wide"
    )

    st.title("📄 Resume Category Prediction")
    st.markdown(
        "Upload a Resume (PDF, DOCX, TXT) and predict its category."
    )

    uploaded_file = st.file_uploader(
        "Upload Resume",
        type=["pdf", "docx", "txt"]
    )

    if uploaded_file is not None:

        try:

            resume_text = handle_file_upload(uploaded_file)

            st.success("Resume uploaded successfully!")

            with st.expander("View Extracted Resume Text"):
                st.text_area(
                    "Resume Content",
                    resume_text,
                    height=300
                )

            if st.button("Predict Category"):

                result = predict_category(resume_text)

                if result == "Not Resume":

                    st.error(
                        "This document does not appear to be a resume."
                    )

                else:

                    st.subheader("Prediction Result")

                    st.success(
                        f"Predicted Resume Category: {result}"
                    )

        except Exception as e:

            st.error(f"Error: {str(e)}")


if __name__ == "__main__":
    main()
