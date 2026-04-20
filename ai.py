import anthropic
import streamlit as st
from dotenv import load_dotenv
import os

def hataBas():
    st.warning("boş veri göndermeyiniz.")

def logla(istek, cevap):
    st.session_state["gecmis"].append({"sorgu": istek, "cevap": cevap})

def yaz(cevap):
    st.write(cevap)

def apiGonder(system, request):
    response = api.messages.create(model="claude-haiku-4-5", max_tokens=2000, system= system ,messages=[{"role":"user","content": request}])   
    return response.content[0].text

def islem(buton, promt, request):
    if request and buton:
        with st.spinner("Düşünüyor..."):
            response = apiGonder(promt, request)
        yaz(response)
        logla(request,response)
    elif not request and buton:
        hataBas() 

load_dotenv()
api_key = os.getenv("ANTHROPIC_API_KEY")
api = anthropic.Anthropic(api_key=api_key)

if "gecmis" not in st.session_state:
    st.session_state["gecmis"] = []

request = st.text_area("SQL girin")

buton = st.button("Açıkla")
optimizeButon = st.button("Sorguyu optimize et")
hataButon = st.button("Hata Tespit")

islem(buton, "SQL sorgusunun ne işe yaradığını türkçe bir şekilde açıkla", request)
islem(optimizeButon, "SQL sorgusunun optimize et", request)
islem(hataButon, "Verilen SQL sorgusunda hata var mı kontrol et. Hata varsa nerede olduğunu ve nasıl düzeltileceğini Türkçe açıkla. Hata yoksa 'Sorguda hata bulunamadı.' de.", request)
  
for item in st.session_state["gecmis"]:
    sorgu = item["sorgu"]
    with st.expander(sorgu):
        yaz(item["cevap"])