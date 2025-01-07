#!/usr/bin/env python
# coding: utf-8


import streamlit as st
import pandas as pd
import copy
from project8 import CashFlowModel

# App Title
st.title("Nnamdi's Streamlit App for Cash Flow Modeling")

# File uploader
uploaded_file = st.file_uploader("Upload your Excel file", type=["xlsx"])

if uploaded_file:
    # Read the uploaded Excel file into a Pandas DataFrame
    data = pd.read_excel(uploaded_file)
    st.write("Uploaded Data:")
    st.dataframe(data)

    # Instantiate the CashFlowModel
    model = CashFlowModel()

    # Load the data into the model
    for index, row in data.iterrows():
        model.add_entry(
            year=row["Year"],
            interest_rate=row["Interest Rate"],
            cash_flow=row["Cash Flow"],
        )
    # Save the original data
    model.original_data = copy.deepcopy(model.data)

    # Display the original present value
    original_present_value = model.calculate_present_value()
    st.write("Present Value of Cash Flows:")
    st.write(f"£{original_present_value:,.2f}")

    # Sensitivity Testing
    st.write("Sensitivity Testing:")
    interest_rate_factor = st.slider(
        "Interest Rate Adjustment Factor", min_value=0.5, max_value=1.5, value=1.0, step=0.1
    )
    cash_flow_factor = st.slider(
        "Cash Flow Adjustment Factor", min_value=0.5, max_value=1.5, value=1.0, step=0.1
    )

    # Reset data to original state before applying sensitivity adjustments
    model.reset_data()

    # Apply sensitivity testing and calculate adjusted present value
    adjusted_present_value = model.sensitivity_test(interest_rate_factor, cash_flow_factor)
    st.write("Adjusted Present Value:")
    st.write(f"£{adjusted_present_value:,.2f}")

else:
    st.write("Please upload a file to continue.")
