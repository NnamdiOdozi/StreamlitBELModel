#!/usr/bin/env python
# coding: utf-8

import streamlit as st
import pandas as pd
import copy
from project8 import CashFlowModel

import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))  # Default to 8080 if PORT is not set
    os.system(f"streamlit run main.py --server.port {port} --server.address 0.0.0.0")




# App Title
st.title("Nnamdi's Streamlit App for Cash Flow Modeling")

# Display a screenshot of the expected data format
st.write("### Expected Data Format")
st.image("data_format_example.png", caption="Expected format of the data file.")

# File uploader
st.write("### Upload Your Excel File")
uploaded_file = st.file_uploader("Upload your Excel file (optional)", type=["xlsx"])

# Load default data if no file is uploaded
if uploaded_file:
    data = pd.read_excel(uploaded_file)
    st.write("Uploaded Data:")
else:
    st.write("No file uploaded. Using the default data.xlsx.")
    data = pd.read_excel("data.xlsx")

# Display the loaded data
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
    model.original_data = copy.deepcopy(model.data)

# Calculate Present Value
present_value = model.calculate_present_value()
st.write("Present Value of Cash Flows:")
st.write(f"£{present_value:,.2f}")

# Sensitivity Testing
st.write("### Sensitivity Testing")
interest_rate_factor = st.slider(
    "Interest Rate Adjustment Factor", min_value=0.5, max_value=1.5, value=1.0, step=0.1
)
cash_flow_factor = st.slider(
    "Cash Flow Adjustment Factor", min_value=0.5, max_value=1.5, value=1.0, step=0.1
)
new_present_value = model.sensitivity_test(interest_rate_factor, cash_flow_factor)
st.write(f"Adjusted Present Value: £{new_present_value:,.2f}")
