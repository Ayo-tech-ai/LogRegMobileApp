# 🛒 Purchase Predictor — ML-Powered Web & Mobile App

A complete end-to-end machine learning project that predicts whether a user will purchase a product based on their **Age** and **Estimated Salary**. The same trained model powers both a **Streamlit web app** and a **native Android mobile app**.

---

## 📌 Project Overview

This project demonstrates a full ML deployment pipeline:

```
Train Model (Google Colab)
       ↓
Convert to TensorFlow Lite (.tflite)
       ↓
Deploy on Streamlit Cloud (web)
       ↓
Deploy on Android (mobile, on-device inference)
```

The logistic regression model is trained in Python, converted to TFLite, and deployed across two platforms — with the normalization layer baked directly into the model so no manual scaling is needed at inference time.

---

## 📊 Dataset

| Feature | Description | Range |
|---|---|---|
| Age | User's age | 18 – 60 |
| EstimatedSalary | User's estimated income | $15,000 – $150,000 |
| Purchased | Whether the user purchased (0 or 1) | 0 / 1 |

- **400 rows**, no missing values
- **Class distribution:** 64.25% did not purchase, 35.75% purchased

---

## 🤖 Model

- **Type:** Logistic Regression (Keras)
- **Architecture:** Normalization layer → Dense(1, sigmoid)
- **Test Accuracy:** 92.50%
- **Model size (TFLite):** 1,724 bytes
- **Key design choice:** The `Normalization` layer is baked inside the model, so both the web app and mobile app can pass raw input values directly without any preprocessing code

---

## 🌐 Streamlit Web App

The web app loads the `.tflite` model and runs predictions directly in the browser.

### Features
- Two input fields: Age and Estimated Salary
- Predict button → shows probability and Will Purchase / Will Not Purchase
- Clean, minimal UI

### Run Locally

```bash
pip install streamlit tensorflow numpy
streamlit run app.py
```

### Deploy on Streamlit Cloud

1. Push `app.py`, `purchase_model.tflite`, `requirements.txt`, and `.python-version` to GitHub
2. Go to [streamlit.io](https://streamlit.io) and connect your repo
3. Deploy

> **Important:** Include a `.python-version` file containing `3.11` — TensorFlow requires Python 3.11 on Streamlit Cloud.

---

## 📱 Android Mobile App

The Android app runs the same `.tflite` model entirely on-device using the TensorFlow Lite Android library. No internet connection is required for predictions.

### Built With

- **Language:** Kotlin
- **UI Framework:** Jetpack Compose
- **ML Runtime:** TensorFlow Lite 2.17.0
- **Minimum SDK:** API 24 (Android 7.0)

### Features

- Two input fields: Age and Estimated Salary
- Predict button → shows probability and result in green (Will Purchase) or red (Will Not Purchase)
- Reset button → clears inputs and result for a fresh prediction
- Fully on-device inference — no internet needed

### Project Structure

```
app/
  src/
    main/
      assets/
        purchase_model.tflite    ← TFLite model
      java/com/example/purchasepredictor/
        MainActivity.kt          ← UI + prediction logic
```

### Key Dependency

```kotlin
implementation("org.tensorflow:tensorflow-lite:2.17.0")
```

### Build & Run

1. Open the project in Android Studio
2. Connect your Android phone with USB debugging enabled
3. Press **Ctrl + F9** to build
4. Click the green **Run** button ▶️

---

## 📁 Repository Structure

```
├── app.py                          # Streamlit web app
├── purchase_model.tflite           # TFLite model (shared by both apps)
├── purchase_model.keras            # Keras saved model
├── requirements.txt                # Streamlit dependencies
├── .python-version                 # Python 3.11 for Streamlit Cloud
├── training/
│   └── logistic_regression.ipynb  # Google Colab training notebook
└── android/
    └── PurchasePredictor/          # Android Studio project
```

---

## 🧪 Sample Predictions

| Age | Salary | Prediction | Probability |
|---|---|---|---|
| 45 | $120,000 | ✅ Will Purchase | 81.8% |
| 30 | $50,000 | ❌ Will Not Purchase | ~20% |
| 19 | $19,000 | ❌ Will Not Purchase | low |

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| Model Training | Python, TensorFlow/Keras, scikit-learn |
| Model Format | TensorFlow Lite (.tflite) |
| Web App | Streamlit, Python 3.11 |
| Mobile App | Android Studio, Kotlin, Jetpack Compose |
| Deployment | Streamlit Cloud, GitHub |

---

## 👤 Author

Built by **Ayoola Ayodele** — AI educator, tutor, and consultant.

This project is part of a series exploring end-to-end ML deployment across web and mobile platforms, combining machine learning with real-world application development.

---

## 📄 License

MIT License
