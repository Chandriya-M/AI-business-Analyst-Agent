import streamlit as st
import pandas as pd
from openai import OpenAI
import os


OPENAI_API_KEY = st.secrets["OPENAI_API_KEY"]

client = OpenAI(api_key=OPENAI_API_KEY)

st.set_page_config(page_title="AI Business Analyst — Agent CR", page_icon="🤖", layout="wide")

st.markdown("""
<div style="background: linear-gradient(90deg, #4B79A1, #283E51); padding: 22px; border-radius: 10px; text-align: center;">
    <h1 style="color:White;">🤖 AI Business Analyst — Agent <strong>CR</strong></h1>
    <p style="color:#e8e8e8; font-size:18px;">Your smart AI companion for data understanding, insights, and quick analysis</p>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div style="margin-top: 20px; padding: 15px; border-radius: 12px; background: Black; border-left: 5px solid #4B79A1;">
    <h3>🤝 Meet Your AI Analyst: <strong>Agent CR</strong></h3>
    <p>Designed to help you explore your datasets, extract insights, detect patterns, and answer analytical questions with clarity.</p>
    <p style="font-style: italic;">✨ Crafted with care by <strong>Chandriya</strong></p>
</div>
""", unsafe_allow_html=True)

st.write("")

uploaded = st.file_uploader("📁 Upload your CSV file", type="csv")

if uploaded:
    df = pd.read_csv(uploaded)

    st.subheader("📊 Data Preview")
    st.dataframe(df.head())

    st.subheader("💬 Ask Agent CR About Your Data")
    question = st.text_input("Enter your question:")

    if st.button("Analyze Data"):
        with st.spinner("Agent CR is thinking...🧠"):

            prompt = f"""
You are Agent CR — an expert AI Business Analyst created by Chandriya.
Analyze the dataset shown below.

Dataset Preview (first rows):
{df.head(300).to_markdown()}

User question:
{question}

Provide:
1. A clear explanation (5–10 lines)
2. Key patterns, trends, correlations
3. A bullet-point summary
4. Friendly closing compliment like "Great question!", "Nice exploring!", "You're doing awesome!"
"""

            try:
                response = client.chat.completions.create(
                    model="gpt-4o-mini",
                    messages=[{"role": "user", "content": prompt}]
                )

                answer = response.choices[0].message.content

                st.markdown("""
                <div style="margin-top: 20px; padding: 20px; border-radius: 12px; background: Black; border: 1px solid #ddd;">
                    <h3>📌 Agent CR's Analysis</h3>
                </div>
                """, unsafe_allow_html=True)

                st.write(answer)

            except Exception as e:
                st.error(f"Error: {e}")

else:
    st.info("Please upload a CSV to start.")
