# Rock or Mine Prediction System

# Deployment Link: [Demo at Streamlit](https://rock-mine-prediction.streamlit.app/)

![Python](https://img.shields.io/badge/python-v3.8+-blue.svg)
![scikit-learn](https://img.shields.io/badge/scikit--learn-v1.2.2-yellow.svg)
![Streamlit](https://img.shields.io/badge/streamlit-v1.10.0-red.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

Welcome to the **Rock or Mine Prediction System**! This project uses a Logistic Regression model to predict whether an object detected by sonar is a rock or a mine, based on sonar signal returns.

## Table of Contents
- [About the Project](#about-the-project)
- [Technologies Used](#technologies-used)
- [Model Training](#model-training)
- [Streamlit Web App](#streamlit-web-app)
- [Installation](#installation)
- [Usage](#usage)
- [Example Inputs](#example-inputs)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

---

## About the Project

This project utilizes sonar sensor data with 60 features per observation to classify an object as a **rock** or **mine**. The classification is achieved using a **Logistic Regression** model, which is built using Python and scikit-learn, and deployed via a **Streamlit** web application for user interaction.

The objective is to give users a simple, web-based interface where they can input sonar signal values and obtain a prediction.

---

## Technologies Used

- **Python**: Core programming language used for building the model.
- **scikit-learn**: For model training, testing, and accuracy evaluation.
- **Streamlit**: For creating an interactive web-based interface.
- **NumPy**: For numerical operations and data handling.
- **Pandas**: For data manipulation.
- **Joblib**: For saving and loading the trained model.

---

## Model Training

The Logistic Regression model is trained using the **Sonar Dataset**, where each sample is described by 60 attributes representing the energy of sonar returns. The target is to classify whether the object is a **Rock (R)** or a **Mine (M)**.

### Steps:
1. Data Preprocessing (Cleaning, Feature Scaling)
2. Train-Test Split
3. Model Training using **LogisticRegression** from scikit-learn
4. Model Evaluation using **accuracy_score**
5. Saving the trained model using **joblib**

---

## Streamlit Web App

The app provides a simple and user-friendly interface to predict the object type. Users input 60 features (which are sonar readings), and the system predicts whether the object is a **Rock** or **Mine**.

---

## Installation

To get started with this project locally, follow these steps:

### Prerequisites

Ensure you have Python installed (version 3.8 or later).

1. Clone this repository:
    ```bash
    git clone https://github.com/your-username/rock-mine-prediction.git
    cd rock-mine-prediction
    ```

2. Install required packages:
    ```bash
    pip install -r requirements.txt
    ```

3. Launch the Streamlit app:
    ```bash
    streamlit run app.py
    ```

---

## Usage

Once the web app is running, enter values for all 60 features into the provided input fields and click the **Predict** button. The app will display whether the object is a **Rock** or **Mine** based on the entered values.

---

## Example Inputs

You can directly try the following input examples in the Streamlit app:

- **Example 1 (Rock)**:
[0.0519, 0.0548, 0.0842, 0.0319, 0.1158, 0.0922, 0.1027, 0.0613, 0.1465, 0.2838, 0.2802, 0.3086, 0.2657, 0.3801, 0.5626, 0.4376, 0.2617, 0.1199, 0.6676, 0.9402, 0.7832, 0.5352, 0.6809, 0.9174, 0.7613, 0.8220, 0.8872, 0.6091, 0.2967, 0.1103, 0.1318, 0.0624, 0.0990, 0.4006, 0.3666, 0.1050, 0.1915, 0.3930, 0.4288, 0.2546, 0.1151, 0.2196, 0.1879, 0.1437, 0.2146, 0.2360, 0.1125, 0.0254, 0.0285, 0.0178, 0.0052, 0.0081, 0.0120, 0.0045, 0.0121, 0.0097, 0.0085, 0.0047, 0.0048, 0.0053]


- **Example 2 (Mine)**:
[0.009, 0.0062, 0.0253, 0.0489, 0.1197, 0.1589, 0.1392, 0.0987, 0.0955, 0.1895, 0.1896, 0.2547, 0.4073, 0.2988, 0.2901, 0.5326, 0.4022, 0.1571, 0.3024, 0.3907, 0.3542, 0.4438, 0.6414, 0.4601, 0.6009, 0.8690, 0.8345, 0.7669, 0.5081, 0.4620, 0.5380, 0.5375, 0.3844, 0.3601, 0.7402, 0.7761, 0.3858, 0.0667, 0.3684, 0.6114, 0.3510, 0.2312, 0.2195, 0.3051, 0.1937, 0.1570, 0.0479, 0.0538, 0.0146, 0.0068, 0.0187, 0.0059, 0.0095, 0.0194, 0.0080, 0.0152, 0.0158, 0.0053, 0.0189, 0.0102]


---


## Contact

If you have any questions or suggestions, feel free to contact the project maintainer:

- **Name**: Hitesh Kumar
- **Email**: hiteshofficial0001@gmail.com
- **Location**: Gurgoan, Haryana, India
