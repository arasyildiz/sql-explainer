import anthropic
import streamlit as st
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("ANTHROPIC_API_KEY")
api = anthropic.Anthropic(api_key=api_key)

if "gecmis" not in st.session_state:
    st.session_state["gecmis"] = []

request = st.text_area("SQL girin")

buton = st.button("Açıkla")

if buton and request:
    with st.spinner("Açıklanıyor..."):
        r = api.messages.create(model="claude-haiku-4-5", max_tokens=2000, system="SQL sorgusunun ne işe yaradığını türkçe bir şekilde açıkla",messages=[{"role":"user","content": request}])   
    ai_response = r.content[0].text
    st.write(ai_response)
    st.session_state["gecmis"].append({"sorgu": request, "cevap": ai_response})
    
elif not request and buton:
    st.warning("boş veri göndermeyiniz.")


for item in st.session_state["gecmis"]:
    sorgu = item["sorgu"]
    with st.expander(sorgu):
        st.write(item["cevap"])