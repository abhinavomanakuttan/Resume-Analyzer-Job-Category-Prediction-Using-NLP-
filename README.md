# 📄 Resume Analyzer & Job Category Prediction

An NLP-powered Resume Analyzer built with **Python, Scikit-Learn, and Streamlit** that extracts text from resumes, validates uploaded documents, and predicts job categories using Machine Learning.

## 🚀 Features

* Upload resumes in PDF, DOCX, and TXT formats
* Automatic text extraction and preprocessing
* Resume validation to identify non-resume documents
* TF-IDF based feature extraction
* Job category prediction using LinearSVC
* Interactive Streamlit web interface

## 📂 Predicted Categories

The model classifies resumes into 25 professional domains including:

* Data Science
* Python Developer
* Java Developer
* DevOps Engineer
* Business Analyst
* HR
* Testing
* Network Security Engineer
* SAP Developer
* Web Designing
* And more...

## 🏗️ System Architecture

```text
Resume Upload
      │
      ▼
Text Extraction
      │
      ▼
Text Preprocessing
      │
      ▼
Resume Validation
      │
 ┌────┴────┐
 │         │
 ▼         ▼
Resume   Not Resume
 │
 ▼
TF-IDF Vectorization
 │
 ▼
LinearSVC Classifier
 │
 ▼
Predicted Job Category
```

## 🛠️ Tech Stack

### Languages & Libraries

* Python
* Pandas
* NumPy
* Scikit-Learn

### NLP

* TF-IDF Vectorization
* Text Cleaning
* Regular Expressions

### Model

* LinearSVC
* LabelEncoder

### Deployment

* Streamlit

### Document Processing

* PyPDF2
* python-docx

## 📁 Project Structure

```text
Resume-Analyzer/
│
├── app.py
├── clf.pkl
├── tfidf.pkl
├── encoder.pkl
├── requirements.txt
├── README.md
│
└── dataset/
    └── resume_dataset.csv
```

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/abhinavomanakuttan/Resume-Analyzer-Job-Category-Prediction-Using-NLP-.git
cd resume-analyzer
```

### Create Environment

```bash
conda create -n resume_analyzer python=3.10
conda activate resume_analyzer
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

## ▶️ Run the Application

```bash
streamlit run app.py
```

Open:

```text
http://localhost:8501
```

## 📊 Machine Learning Pipeline

### Preprocessing

* URL removal
* Special character removal
* Text normalization
* Lowercasing
* Whitespace cleanup

### Feature Extraction

```python
TfidfVectorizer()
```

### Classification Model

```python
LinearSVC()
```

### Label Encoding

```python
LabelEncoder()
```

## 🎯 Future Enhancements

* ATS Resume Scoring
* Skill Extraction
* Resume Ranking
* Job Recommendation Engine
* Named Entity Recognition (NER)
* Deep Learning-Based Resume Classification
* Resume Parsing and Analytics Dashboard

## 👨‍💻 Author

**Abhinav Omanakuttan**

B.Tech Artificial Intelligence & Data Science

Machine Learning | Data Science | NLP | MLOps

GitHub: https://github.com/abhinavomanakuttan

## ⭐ Support

If you found this project useful, consider giving it a star on GitHub.
