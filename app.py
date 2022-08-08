import streamlit as st
from bbquote917.quotes import get_quote

st.title("Inspirational Quotes ⭐")

if st.button("Inspire me!"):
  st.markdown(f"### {get_quote()}")
