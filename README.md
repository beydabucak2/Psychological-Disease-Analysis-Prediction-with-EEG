# 🧠 EEG-Based Health Prediction Web App

![EEG Banner](https://upload.wikimedia.org/wikipedia/commons/thumb/5/53/21_electrode_placement_EEG.svg/2560px-21_electrode_placement_EEG.svg.png)

## 📌 About the Project

This project aims to predict an individual's neurological health status based on EEG (Electroencephalography) recordings, specifically analyzing **Delta** and **Theta** brainwaves. Using statistical analysis with **Jamovi**, these two signals were found to have **significant differences** between healthy and unhealthy groups. A machine learning model then utilizes this insight to classify new input.

---

## 🎯 Purpose

- To provide a health prediction system using **EEG wave features**
- To demonstrate the effectiveness of **Delta** and **Theta** waves in classification
- To offer a clean, neuroscience-themed **user interface** for quick use

---

## 🧪 Tools & Technologies Used

| Tool | Description |
|------|-------------|
| `Jamovi` | Statistical analysis (t-tests for significance) |
| `Python` | Data preprocessing, modeling, and server logic |
| `Scikit-learn` | Machine Learning (Gradient Boosting Classifier) |
| `Flask` | Backend web server |
| `HTML/CSS` | Frontend design |
| `Chart.js` | Visualization of prediction results (pie chart) |

---

## 📊 Statistical Preprocessing

Using **Jamovi**, statistical analysis confirmed that:

- **Delta** and **Theta** waves differed **significantly** between groups (`p < 0.05`)
- These features were used to train a classifier
- Target labels: `1 = Healthy`, `2 = Unhealthy`

---

## 🚀 How It Works

1. User inputs Delta and Theta wave values from EEG analysis.
2. Data is scaled using `StandardScaler`.
3. The trained **GradientBoostingClassifier** processes the inputs.
4. The system returns the health prediction and shows results visually.

---

## 💻 How to Run the Project

```bash
# 1. Install required packages
pip install flask scikit-learn matplotlib seaborn

# 2. Run the Flask server
python app.py

# 3. Open the app in your browser
http://127.0.0.1:5000



🖼️ UI Features
Modern neuroscience-themed background

Centered input and prediction form

Dynamic pie chart showing health prediction:

Healthy:
"With a probability of 57.2%, your EEG data indicates a healthy state. No significant neurological abnormality detected."

Unhealthy:
"With a probability of 73.5%, the result suggests a potential disorder. This is not a definitive diagnosis. Please consult your doctor."



☁️ Deployment
Local development: Flask development server

For production: Can be deployed using gunicorn or hosted on platforms like Render, Railway, or Heroku


📁 File Structure
cpp
Copy
Edit
EEG/
├── app.py
├── model.pkl
├── static/
│   └── style.css
├── templates/
│   └── index.html
└── README.md
🙋 Feedback & Contributions
Feel free to open issues, fork the repo, or submit pull requests. Contributions are always welcome!

⚠️ Disclaimer
⚠️ This tool is for educational and research purposes only. It is not intended for medical diagnosis. Always consult a healthcare professional for clinical decisions.

📜 License
MIT License – You are free to use, modify, and distribute this project as you wish.
