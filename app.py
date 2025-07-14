import streamlit as st
from utils import save_datamatrix, ip_to_hex, decode_datamatrix
import os

os.makedirs("outputs", exist_ok=True)
st.set_page_config(page_title="DataMatrix Generator", layout="wide")

st.sidebar.title(" DataMatrix Tools")
selection = st.sidebar.radio("Choose an option:", ["Project Info", "Long String → DataMatrix", "IP Address → DataMatrix"])

if selection == "Project Info":
    st.title(" Project Overview")
    st.markdown("""
    This tool converts:
    - Long strings to DataMatrix codes
    - IP addresses to DataMatrix codes (hex)
    
    Built with: `pylibdmtx`, `Pillow`, and `Streamlit`

    Encoding and Decoding of DataMatrix is supported.
    """)

elif selection == "Long String → DataMatrix":
    st.title(" Convert Long String to DataMatrix")
    user_input = st.text_input("Enter the string:")

    if st.button("Generate DataMatrix") and user_input:
        filename = f"string_{user_input}.png".replace(" ", "_")
        path = save_datamatrix(user_input, filename)
        st.image(path, caption="DataMatrix Code")
        decoded = decode_datamatrix(path)
        st.code(f"Decoded content: {decoded}", language="text")

        with open(path, "rb") as f:
            st.download_button("Download PNG", f, file_name=filename)

elif selection == "IP Address → DataMatrix":
    st.title(" Convert IP Address to DataMatrix")
    ip_input = st.text_input("Enter IP Address (e.g. 192.168.0.1):")

    if st.button("Convert IP to DataMatrix") and ip_input:
        try:
            hex_string = ip_to_hex(ip_input)
            filename = f"ip_{ip_input.replace('.', '_')}.png"
            path = save_datamatrix(hex_string, filename)
            st.success(f"Hex representation: `{hex_string}`")
            st.image(path, caption="DataMatrix Code")
            decoded = decode_datamatrix(path)
            st.code(f"Decoded content: {decoded}", language="text")

            with open(path, "rb") as f:
                st.download_button("Download PNG", f, file_name=filename)
        except Exception as e:
            st.error(f"Error: {e}")
