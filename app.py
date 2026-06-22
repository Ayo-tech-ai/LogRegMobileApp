import streamlit as st
import numpy as np
import tensorflow as tf

# --- Load the TFLite model ---
@st.cache_resource
def load_model():
    interpreter = tf.lite.Interpreter(model_path='purchase_model.tflite')
    interpreter.resize_tensor_input(0, [1, 2])
    interpreter.allocate_tensors()
    return interpreter

interpreter = load_model()
input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()

# --- App UI ---
st.title("🛒 Purchase Predictor")
st.write("Enter a user's details below to predict whether they will purchase.")

age = st.number_input("Age", min_value=18, max_value=60, value=30)
salary = st.number_input("Estimated Salary ($)", min_value=15000, max_value=150000, value=50000, step=1000)

if st.button("Predict"):
    # Prepare input
    test_input = np.array([[age, salary]], dtype=np.float32)

    # Run prediction
    interpreter.set_tensor(input_details[0]['index'], test_input)
    interpreter.invoke()
    output = interpreter.get_tensor(output_details[0]['index'])

    probability = output[0][0]
    prediction = 1 if probability >= 0.5 else 0

    # Display result
    st.markdown("---")
    if prediction == 1:
        st.success(f"✅ Will Purchase — Probability: {probability * 100:.1f}%")
    else:
        st.error(f"❌ Will Not Purchase — Probability: {probability * 100:.1f}%")
