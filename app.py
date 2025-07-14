import streamlit as st
from utils import save_datamatrix, ip_to_hex, decode_datamatrix
from PIL import Image
import os

st.set_page_config(page_title="DataMatrix Generation Tool", layout="wide")

st.sidebar.title("Data Matrix Tool")
tool = st.sidebar.radio(
    "Choose an option:",
    ("Project Info", "Long String → DataMatrix", "IP Address → DataMatrix", "Upload & Decode DataMatrix")
)

if tool == "Project Info":
    st.title("DataMatrix Generator & Decoder Tool")
    st.markdown(
        """
        This tool helps convert identifiers such as product strings or IP addresses 
        into [DataMatrix](https://en.wikipedia.org/wiki/Data_Matrix) codes and back.
        
        **Features:**
        - Generate DataMatrix from a long string (e.g., serial numbers)
        - Encode IP addresses as compact DataMatrix hex
        - Upload & decode existing DataMatrix PNGs
        """
    )

elif tool == "Long String → DataMatrix":
    st.title("Convert Long String to DataMatrix")
    user_input = st.text_input("Enter the string (e.g. 251070196104002003):")
    if st.button("Generate DataMatrix"):
        filename = f"dm_string_{user_input}.png"
        path = save_datamatrix(user_input, filename)
        st.image(path, caption="DataMatrix Code", use_container_width=True)
        with open(path, "rb") as f:
            st.download_button("Download PNG", f, file_name=filename)

elif tool == "IP Address → DataMatrix":
    st.title("Convert IP Address to DataMatrix")
    ip_input = st.text_input("Enter IP Address (e.g. 192.168.0.1):")
    if st.button("Convert IP to DataMatrix"):
        try:
            hex_value = ip_to_hex(ip_input)
            st.markdown(f"**Hex representation:** `{hex_value}`")
            filename = f"ip_{ip_input.replace('.', '_')}.png"
            path = save_datamatrix(hex_value, filename)
            st.image(path, caption="DataMatrix Code", use_container_width=True)
            with open(path, "rb") as f:
                st.download_button("Download PNG", f, file_name=filename)
        except Exception as e:
            st.error(f"Invalid IP address: {e}")

elif tool == "Upload & Decode DataMatrix":
    st.title("Upload and Decode a DataMatrix Code")
    uploaded = st.file_uploader("Upload a DataMatrix PNG", type=["png"])
    if uploaded:
        st.image(uploaded, caption=uploaded.name, use_container_width=300)
        try:
            result = decode_datamatrix(uploaded)
            if result:
                st.success(f"Decoded content: `{result}`")
            else:
                st.warning("No DataMatrix code found or unreadable.")
        except Exception as e:
            st.error(f"Error decoding image: {e}")
