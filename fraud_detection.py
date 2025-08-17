import streamlit as st
import pandas as pd
import joblib

model = joblib.load("fraud_detection_pipeline.pkl")

st.title("Fraud Detection Prediction App")


st.markdown("Please enter the transaction details and use the predict button")


st.divider()


transaction_type = st.selectbox("Transaction Type", ["PAYMENT", "TRANSFER", "CASH_OUT", "DEBIT", "CASH_IN"])
amount = st.number_input("Amount", min_value=0.0, value=1000.0)
oldbalanceOrg = st.number_input("Old Balance (Origin)", min_value=0.0, value=10000.0)
oldbalanceOrg = st.number_input("Old Balance (Sender)", min_value=0.0, value=10000.0, help="Enter the sender's balance before the transaction")
newbalanceOrig = st.number_input("New Balance (Sender)", min_value=0.0, value=9000.0, help="Enter the sender's balance after the transaction")
oldbalanceDest = st.number_input("Old Balance (Receiver)", min_value=0.0, value=5000.0, help="Enter the receiver's balance before the transaction")
newbalanceDest = st.number_input("New Balance (Receiver)", min_value=0.0, value=6000.0, help="Enter the receiver's balance after the transaction")


# Create a button to trigger the prediction
if st.button("Predict"):
    # Create a DataFrame from the user's input

    input_data = pd.DataFrame({
        "type": [transaction_type],
        "amount": [amount],
        "oldbalanceOrg": [oldbalanceOrg],
        "newbalanceOrig": [newbalanceOrig],
        "oldbalanceDest": [oldbalanceDest],
        "newbalanceDest": [newbalanceDest]
    })

    # Use the loaded model to make a prediction
    prediction = model.predict(input_data)             # model.predict → predicts 0 (Not Fraud) or 1 (Fraud)
    prediction_proba = model.predict_proba(input_data) # model.predict_proba → gives the probabilities of each class: [prob_not_fraud, prob_fraud]

    # Display the prediction result
    st.subheader("Prediction Result")
    if prediction[0] == 1:
        st.error("This transaction is predicted to be FRAUDULENT.")        # red alert for fraud.
        st.write(f"Confidence: {prediction_proba[0][1]*100:.2f}%")    
    else:
        st.success("This transaction is predicted to be NOT FRAUDULENT.")  # green message for safe transactions.
        st.write(f"Confidence: {prediction_proba[0][0]*100:.2f}%")

    st.write("---")
    st.write("Prediction Probabilities:")                                  # Gives detailed prediction probabilities.
    st.write(f"Probability of Not Fraud: {prediction_proba[0][0]:.4f}")
    st.write(f"Probability of Fraud: {prediction_proba[0][1]:.4f}")

