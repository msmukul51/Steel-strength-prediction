import streamlit as st
import pickle
import numpy as np
import matplotlib.pyplot as plt

# Load the saved model pipeline
pipe = pickle.load(open('pipe.pkl', 'rb'))

# Title of the app
st.title("🔩 Steel Fatigue Strength Prediction App 💪")

# Sidebar for input parameters
st.sidebar.header("⚙️ Input Parameters")

# Define input fields using sliders in columns
def user_input_features():
    col1, col2 = st.columns(2)

    with col1:
        NT = st.slider("Normalizing Temperature (°C)", 600, 1200, 850)
        THT = st.slider("Through Hardening Temperature (°C)", 600, 1200, 850)
        THt = st.slider("Through Hardening Time (sec)", 0, 5000, 2000)
        THQCr = st.slider("Through Hardening Quenching Cooling Rate (°C/sec)", 0, 200, 50)
        CT = st.slider("Cooling Temperature (°C)", 0, 1000, 500)
        Ct = st.slider("Cooling Time (sec)", 0, 10000, 3000)
        DT = st.slider("Double Tempering Temperature (°C)", 200, 700, 500)
        Dt = st.slider("Double Tempering Time (sec)", 0, 5000, 2000)
        QmT = st.slider("Quenching Medium Temperature (°C)", 0, 500, 100)
        TT = st.slider("Tempering Temperature (°C)", 200, 700, 450)
        Tt = st.slider("Tempering Time (sec)", 0, 5000, 1800)
        TCr = st.slider("Tempering Cooling Rate (°C/sec)", 0, 100, 20)

    with col2:
        C = st.slider("Carbon (%)", 0.0, 2.0, 0.5)
        Si = st.slider("Silicon (%)", 0.0, 5.0, 1.5)
        Mn = st.slider("Manganese (%)", 0.0, 5.0, 1.2)
        P = st.slider("Phosphorus (%)", 0.0, 1.0, 0.05)
        S = st.slider("Sulfur (%)", 0.0, 1.0, 0.05)
        Ni = st.slider("Nickel (%)", 0.0, 5.0, 1.0)
        Cr = st.slider("Chromium (%)", 0.0, 5.0, 1.5)
        Cu = st.slider("Copper (%)", 0.0, 5.0, 1.0)
        Mo = st.slider("Molybdenum (%)", 0.0, 2.0, 0.5)
        RedRatio = st.slider("Reduction Ratio", 1.0, 10.0, 5.0)
        dA = st.slider("Diameter A (mm)", 0.0, 500.0, 250.0)
        dB = st.slider("Diameter B (mm)", 0.0, 500.0, 250.0)
        dC = st.slider("Diameter C (mm)", 0.0, 500.0, 250.0)

    # Store all features in a NumPy array
    features = np.array([[NT, THT, THt, THQCr, CT, Ct, DT, Dt, QmT, TT, Tt, TCr,
                          C, Si, Mn, P, S, Ni, Cr, Cu, Mo, RedRatio, dA, dB, dC]])
    return features

# Get user input
X_input = user_input_features()

# Prediction button
if st.button("🔮 Predict Steel Strength"):
    prediction = pipe.predict(X_input)  # Predict using the loaded model

    # Display results in a styled box
    st.markdown(f"""
    <div style="padding:10px; border-radius:10px; background:#e3f2fd; color:black; font-size:20px; text-align:center;">
        🔥 <b>Predicted Steel Strength:</b> {prediction[0]:.2f} MPa
    </div>
    """, unsafe_allow_html=True)

    # Visualization: Bar Chart for Prediction
    fig, ax = plt.subplots()
    ax.bar(["Predicted Strength"], [prediction[0]], color="steelblue")
    ax.set_ylabel("MPa")
    ax.set_title("Steel Strength Prediction")

    st.pyplot(fig)  # Display the plot in Streamlit
