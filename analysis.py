import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


def basic_info(df):

    st.subheader("Column Information")

    info_df = pd.DataFrame({
        "Column": df.columns,
        "Data Type": df.dtypes.astype(str),
        "Missing Values": df.isnull().sum()
    })

    st.dataframe(info_df)

    st.subheader("Statistical Summary")
    st.dataframe(df.describe(include="all"))


def numerical_analysis(df):

    numeric_cols = df.select_dtypes(include="number").columns

    if len(numeric_cols) == 0:
        st.warning("No numerical columns found")
        return

    column = st.selectbox(
        "Select Numerical Column",
        numeric_cols
    )

    st.write(df[column].describe())

    fig, ax = plt.subplots()
    ax.hist(df[column], bins=10)
    ax.set_title(column)

    st.pyplot(fig)


def categorical_analysis(df):

    cat_cols = df.select_dtypes(include="object").columns

    if len(cat_cols) == 0:
        st.warning("No categorical columns found")
        return

    column = st.selectbox(
        "Select Categorical Column",
        cat_cols
    )

    counts = df[column].value_counts()

    st.dataframe(counts)

    fig, ax = plt.subplots()

    counts.plot(
        kind="bar",
        ax=ax
    )

    ax.set_title(column)

    st.pyplot(fig)


def correlation_analysis(df):

    numeric_df = df.select_dtypes(include="number")

    if numeric_df.shape[1] < 2:
        st.warning("Not enough numerical columns")
        return

    corr = numeric_df.corr()

    st.dataframe(corr)

    fig, ax = plt.subplots(figsize=(8, 6))

    im = ax.imshow(corr)

    ax.set_xticks(range(len(corr.columns)))
    ax.set_xticklabels(
        corr.columns,
        rotation=90
    )

    ax.set_yticks(range(len(corr.columns)))
    ax.set_yticklabels(corr.columns)

    plt.colorbar(im)

    st.pyplot(fig)
