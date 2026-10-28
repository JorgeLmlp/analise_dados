import streamlit as st
import pandas as pd

nome = "jorge"
idade = 18


df = pd.DataFrame({
  'first column': ["PORTUGUES", "MATEMATICA", "PYTHON", "FRAMEWORK"],
  'second column': [5, 9, 7, 10]
}) 

st.header("Meu primeiro dash")
st.subheader("Jorge")
df
