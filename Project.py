import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="Data Analytics Dashboard", layout="wide")

st.title("📊 Data Analytics Dashboard")

# File uploader
uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.write("### Dataset Preview")
    st.dataframe(df.head())

    # Basic stats
    st.write("### Summary Statistics")
    st.write(df.describe())
    
    # Data visualization
    st.write("### Data Visualizations")
    selected_column = st.selectbox("Select a column for distribution plot", df.select_dtypes(include=['number']).columns)
    
    fig, ax = plt.subplots()
    sns.histplot(df[selected_column], kde=True, ax=ax)
    st.pyplot(fig)
    
    st.write("### Correlation Heatmap")
    fig, ax = plt.subplots(figsize=(8, 6))
    sns.heatmap(df.corr(), annot=True, cmap="coolwarm", fmt=".2f", ax=ax)
    st.pyplot(fig)

