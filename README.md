# 📧 Phishing Email Detector (Machine Learning + Streamlit)

A simple demo-friendly **phishing email classifier** built using:
- Python
- Scikit-Learn
- TF-IDF vectorization
- Logistic Regression
- Streamlit web app

This project identifies whether an email text is **PHISHING** or **SAFE** using a lightweight machine-learning model trained on a small sample dataset.

> ⚠️ This is a **demo version**. Accuracy is limited.  
> Can be upgraded anytime using a real dataset.

---

## 🚀 Features

- Detect phishing emails using ML
- Streamlit-based web UI
- Command-line classifier
- Simple and beginner-friendly
- Easy to upgrade with real datasets

---

## 📂 Project Structure

phishing-email-detector/
│
├── app_streamlit.py # Streamlit web UI
├── classify_email.py # CLI classifier
├── train_phishing.py # Model training script (demo dataset)
├── phishing_model.joblib # Saved ML model
├── README.md # Documentation
└── requirements.txt # Dependencies


---

## ⚙️ Installation

### 1. Clone the repository


git clone https://github.com/SaiSrinadh0549/phishing-email-detector.git

cd phishing-email-detector


### 2. Create & activate a virtual environment


python -m venv venv
venv\Scripts\activate # Windows

OR

source venv/bin/activate # Mac/Linux


### 3. Install dependencies


pip install -r requirements.txt


If you don’t have a requirements file:


pip install scikit-learn pandas joblib streamlit


---

## 🧠 Train the Model (optional)

To retrain the demo model:


python train_phishing.py


This generates:


phishing_model.joblib


---

## 🖥️ Run the Web App (Streamlit)



streamlit run app_streamlit.py


Open the URL shown in terminal:


http://localhost:8501


Paste email text → Press **Analyze** → Get prediction.

---

## 🧪 Run via Command Line



python classify_email.py -t "Your account has been suspended. Click here to verify."


---

## 📈 Demo Model Accuracy

Since this version uses a small sample dataset:
- Approx accuracy: **66%**
- Best used for **learning, demo, and project expo**
- Can be upgraded for real-world use

---

## 🛠️ Future Improvements

- Train with real Kaggle phishing dataset  
- Add URL/domain reputation scoring  
- Add email header checks (SPF/DKIM)  
- Deploy online (Streamlit Cloud / Render)  
- Build Chrome extension  
- Add highlighting of suspicious words  

---

## 📜 License

This project is open-source under the **MIT License**.

---

## 🙌 Author

**Sai Srinadh**  
GitHub: https://github.com/SaiSrinadh0549


