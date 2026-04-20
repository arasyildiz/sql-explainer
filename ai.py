import anthropic
import streamlit as st
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("ANTHROPIC_API_KEY")

api = anthropic.Anthropic(api_key=api_key)

request = st.text_area("SQL girin")

if st.button("Açıkla"):
    r = api.messages.create(model="claude-haiku-4-5", max_tokens=2000, system="SQL sorgusunun ne işe yaradığını türkçe bir şekilde açıkla",messages=[{"role":"user","content": request}])
    ai_response = r.content[0].text
    st.write(ai_response)
