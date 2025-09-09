import qrcode
import streamlit as st

st.set_page_config(
    page_title="QR Code Generator",
    page_icon="🔳",
    layout="wide"
)

st.title("QR Code Generator")
st.markdown("Gere um QrCode de qualquer coisa!")

data = st.text_input("Insira o conteúdo do qrcode aqui: ")

if data:
    img = qrcode.make(data)
    img.save("qrcode.png")
    st.image("qrcode.png")
    st.success("QR code salvo como qrcode.png")