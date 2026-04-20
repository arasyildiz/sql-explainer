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

load_dotenv()
api_key = os.getenv("ANTHROPIC_API_KEY")
api = anthropic.Anthropic(api_key=api_key)

if "gecmis" not in st.session_state:
    st.session_state["gecmis"] = []

request = st.text_area("SQL girin")

buton = st.button("Açıkla")
optimizeButon = st.button("Sorguyu optimize et")
hataButon = st.button("Hata Tespit")

if buton and request:
    with st.spinner("Açıklanıyor..."):
        ai_response = apiGonder("SQL sorgusunun ne işe yaradığını türkçe bir şekilde açıkla", request)
    yaz(ai_response)
    logla(request,ai_response)
elif not request and buton:
    hataBas()

if request and optimizeButon:
    with st.spinner("Optimize ediliyor..."):
        optimizeResponse = apiGonder("SQL sorgusunun optimize et", request)
    yaz(optimizeResponse)
    logla(request,optimizeResponse)
elif not request and optimizeButon:
    hataBas()

if request and hataButon:
    with st.spinner("Hata tespit ediliyor..."):
        hataResponse = apiGonder("Verilen SQL sorgusunda hata var mı kontrol et. Hata varsa nerede olduğunu ve nasıl düzeltileceğini Türkçe açıkla. Hata yoksa 'Sorguda hata bulunamadı.' de.", request)
    yaz(hataResponse)
    logla(request,hataResponse)
elif not request and hataButon:
    hataBas()      

for item in st.session_state["gecmis"]:
    sorgu = item["sorgu"]
    with st.expander(sorgu):
        yaz(item["cevap"])