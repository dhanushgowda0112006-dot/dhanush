import streamlit as st
import pandas as pd
from analysis import (
    basic_info,
    numerical_analysis,
    categorical_analysis,
    correlation_analysis
)

st.set_page_config(
    page_title="Finance Data Analyzer",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Finance Data Analysis Dashboard")

uploaded_file = st.file_uploader(
    "Upload CSV File",
    type=["csv"]
)

if uploaded_file is not None:

    df = pd.read_csv(uploaded_file)

    st.success("File Uploaded Successfully")

    st.subheader("Dataset Preview")
    st.dataframe(df.head())

    st.subheader("Dataset Shape")
    st.write(f"Rows: {df.shape[0]}")
    st.write(f"Columns: {df.shape[1]}")

    tab1, tab2, tab3, tab4 = st.tabs(
        [
            "Basic Info",
            "Numerical Analysis",
            "Categorical Analysis",
            "Correlation"
        ]
    )

    with tab1:
        basic_info(df)

    with tab2:
        numerical_analysis(df)

    with tab3:
        categorical_analysis(df)

    with tab4:
        correlation_analysis(df)
