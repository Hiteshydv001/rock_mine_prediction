import streamlit as st
import numpy as np
import joblib

# Load the saved logistic regression model
model = joblib.load('rock_mine_model.pkl')

# Streamlit app title
st.title('Rock or Mine Prediction System')

# Subtitle or description
st.write("""
    This app predicts whether the object is a rock or a mine based on sonar signal returns.
    Please provide the 60 feature values for prediction, or select an example from the dropdown.
""")

# Sidebar for model information
st.sidebar.title("Model Information")
st.sidebar.write("This logistic regression model was trained using a sonar dataset to classify objects as rocks or mines.")

# Define some example inputs
example_data = {
    "Example 1 (Rock)": [0.009, 0.0062, 0.0253, 0.0489, 0.1197, 0.1589, 0.1392, 0.0987, 0.0955, 0.1895, 0.1896, 0.2547, 
                         0.4073, 0.2988, 0.2901, 0.5326, 0.4022, 0.1571, 0.3024, 0.3907, 0.3542, 0.4438, 0.6414, 0.4601, 
                         0.6009, 0.869, 0.8345, 0.7669, 0.5081, 0.462, 0.538, 0.5375, 0.3844, 0.3601, 0.7402, 0.7761, 
                         0.3858, 0.0667, 0.3684, 0.6114, 0.351, 0.2312, 0.2195, 0.3051, 0.1937, 0.157, 0.0479, 0.0538, 
                         0.0146, 0.0068, 0.0187, 0.0059, 0.0095, 0.0194, 0.008, 0.0152, 0.0158, 0.0053, 0.0189, 0.0102],
    
    "Example 2 (Mine)": [0.0453, 0.0523, 0.0843, 0.0689, 0.1183, 0.2083, 0.3517, 0.5026, 0.6844, 0.7640, 0.8523, 0.8521, 
                         0.8519, 0.8540, 0.8555, 0.8507, 0.8310, 0.8080, 0.7584, 0.6921, 0.5843, 0.4810, 0.3636, 0.2754, 
                         0.2283, 0.1803, 0.1509, 0.1205, 0.0852, 0.0807, 0.0766, 0.0885, 0.1278, 0.2146, 0.3355, 0.3687, 
                         0.4336, 0.5049, 0.5898, 0.6533, 0.7145, 0.7697, 0.8099, 0.8384, 0.8712, 0.9051, 0.9161, 0.9306, 
                         0.9342, 0.9357, 0.9373, 0.9394, 0.9407, 0.9422, 0.9436, 0.9453, 0.9464, 0.9478, 0.9494, 0.9507]
}

# Dropdown for example selection
example_choice = st.selectbox("Or select an example to auto-fill the inputs:", options=["None", "Example 1 (Rock)", "Example 2 (Mine)"])

# Create input fields for user to input 60 features or use selected example
input_data = []
if example_choice != "None":
    input_data = example_data[example_choice]
    st.write(f"Example '{example_choice}' loaded successfully.")
else:
    for i in range(60):
        input_val = st.number_input(f"Input feature {i+1}", value=0.0, format="%.4f")
        input_data.append(input_val)

# Button to trigger prediction
if st.button('Predict'):
    if len(input_data) == 60:
        # Check if the input is valid (i.e., not all zeroes)
        if np.all(np.array(input_data) == 0):
            st.error("All input features are zero. Please enter valid values for prediction.")
        else:
            # Convert input data to numpy array and reshape
            input_data_as_numpy_array = np.asarray(input_data).reshape(1, -1)
            
            # Make the prediction using the model
            prediction = model.predict(input_data_as_numpy_array)
            
            # Display the prediction result
            if prediction[0] == 'R':
                st.success('The object is a Rock')
            else:
                st.success('The object is a Mine')
    else:
        st.error('Please provide all 60 input features for prediction.')
