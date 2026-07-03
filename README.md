# Disease-Prediction
Disease Prediction
Demo Link: https://disease--prediction.streamlit.app/

# 🩺 Disease Prediction System using Machine Learning

A web-based Machine Learning application that predicts the likelihood of three major diseases—**Diabetes**, **Heart Disease**, and **Parkinson's Disease**—using trained classification models. The application is built with **Python**, **Streamlit**, and **Scikit-learn**, providing an intuitive interface for users to input medical parameters and receive instant predictions.

---

## 🚀 Features

- 🩸 **Diabetes Prediction**
- ❤️ **Heart Disease Prediction**
- 🧠 **Parkinson's Disease Prediction**
- 📊 Interactive and user-friendly Streamlit interface
- 🤖 Machine Learning-based disease prediction
- ⚡ Instant prediction results
- 📱 Responsive web application

---

## 🛠️ Technologies Used

- Python
- Streamlit
- Scikit-learn
- Pandas
- NumPy
- Pickle
- Streamlit Option Menu

---

## 📂 Project Structure

```
Disease-Prediction-System/
│
├── web.py                     # Main Streamlit application
├── diabetes.ipynb             # Diabetes model training
├── heart.ipynb                # Heart disease model training
├── parkinsons.ipynb           # Parkinson's model training
│
├── diabetes.csv               # Diabetes dataset
├── heart.csv                  # Heart disease dataset
├── parkinsons.csv             # Parkinson's dataset
│
├── training_models/
│   ├── diabetes_model.sav
│   ├── heart_model.sav
│   └── parkinsons_model.sav
│
├── requirements.txt
└── README.md
```

---

## 🎯 Disease Prediction Modules

### 🩸 Diabetes Prediction

Predicts whether a person is likely to have diabetes based on medical parameters such as:

- Number of Pregnancies
- Glucose Level
- Blood Pressure
- Skin Thickness
- Insulin Level
- BMI
- Diabetes Pedigree Function
- Age

---

### ❤️ Heart Disease Prediction

Predicts the possibility of heart disease using features including:

- Age
- Sex
- Chest Pain Type
- Resting Blood Pressure
- Cholesterol Level
- Fasting Blood Sugar
- ECG Results
- Maximum Heart Rate
- Exercise Induced Angina
- ST Depression
- Slope
- Major Vessels
- Thalassemia

---

### 🧠 Parkinson's Disease Prediction

Predicts Parkinson's disease using biomedical voice measurement features such as:

- MDVP Frequency Features
- Jitter
- Shimmer
- NHR
- HNR
- RPDE
- DFA
- Spread1
- Spread2
- D2
- PPE

---

## 🤖 Machine Learning

The application uses trained Machine Learning classification models saved as **.sav** files using **Pickle**.

Models Included:

- Diabetes Prediction Model
- Heart Disease Prediction Model
- Parkinson's Disease Prediction Model

---

## 🚀 Installation

### Clone the Repository

```bash
git clone https://github.com/your-username/Disease-Prediction-System.git
```

```bash
cd Disease-Prediction-System
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run the Application

```bash
streamlit run web.py
```

---

## 💻 How to Use

1. Launch the Streamlit application.
2. Select the disease prediction module from the sidebar.
3. Enter the required medical parameters.
4. Click the **Prediction** button.
5. View the prediction result instantly.

---

## 📸 Screenshots

Add screenshots of your application here.

Example:

```
screenshots/
│
├── home.png
├── diabetes_prediction.png
├── heart_prediction.png
└── parkinsons_prediction.png
```

---

## 📊 Datasets

This project uses publicly available healthcare datasets for training the Machine Learning models.

Datasets included:

- diabetes.csv
- heart.csv
- parkinsons.csv

---

## 🔮 Future Enhancements

- User Authentication
- Prediction History
- PDF Report Generation
- Doctor Recommendation System
- Disease Risk Score
- Cloud Deployment
- Additional Disease Prediction Modules
- Data Visualization Dashboard

---

## 🤝 Contributing

Contributions are welcome!

1. Fork the repository
2. Create a new feature branch

```bash
git checkout -b feature-name
```

3. Commit your changes

```bash
git commit -m "Add new feature"
```

4. Push to GitHub

```bash
git push origin feature-name
```

5. Open a Pull Request

---

## 👨‍💻 Author

**Utkarsh Verma**

B.Tech Computer Science and Engineering  
VIT-AP University

---

## ⭐ Support

If you found this project helpful, please give it a ⭐ on GitHub!

---

## 📧 Contact

Feel free to connect with me on **LinkedIn** or reach out for collaboration on Machine Learning and AI projects.
