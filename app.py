import streamlit as st
from utils import save_datamatrix, ip_to_hex, decode_datamatrix
import os

# Ensure output folder exists
os.makedirs("outputs", exist_ok=True)
st.set_page_config(page_title="DataMatrix Generator", layout="wide")

# Sidebar options
st.sidebar.title("DataMatrix Tools")
selection = st.sidebar.radio("Choose an option:", [
    "Tool Info",
    "Long String → DataMatrix",
    "IP Address → DataMatrix",
    "Upload & Decode DataMatrix"
])

# 1. Project Info
if selection == "Tool Info":
    st.title("Data Matrix Generator Tool")
    st.markdown("""
    This tool lets you generate and decode **DataMatrix codes** for different use cases:
    
    - Convert a **long string** into a DataMatrix code.
    - Convert an **IP address** into a DataMatrix code using its hex format.
    - Upload and **verify** an existing DataMatrix image.

    """)

# 2. Long String to DataMatrix
elif selection == "Long String → DataMatrix":
    st.title("Convert Long String to DataMatrix")
    user_input = st.text_input("Enter the string (e.g. 251070196104002003):")

    if st.button("Generate DataMatrix") and user_input:
        filename = f"string_{user_input}.png".replace(" ", "_")
        path = save_datamatrix(user_input, filename)
        st.image(path, caption="DataMatrix Code")
        decoded = decode_datamatrix(path)
        st.code(f"Decoded content: {decoded}", language="text")

        with open(path, "rb") as f:
            st.download_button("Download PNG", f, file_name=filename)

# 3. IP Address to DataMatrix
elif selection == "IP Address → DataMatrix":
    st.title("Convert IP Address to DataMatrix")
    ip_input = st.text_input("Enter IP Address (e.g. 192.168.0.1):")

    if st.button("Convert IP to DataMatrix") and ip_input:
        try:
            hex_string = ip_to_hex(ip_input)
            filename = f"ip_{ip_input.replace('.', '_')}.png"
            path = save_datamatrix(hex_string, filename)
            st.success(f"Hex representation: {hex_string}")
            st.image(path, caption="DataMatrix Code")
            decoded = decode_datamatrix(path)
            st.code(f"Decoded content: {decoded}", language="text")

            with open(path, "rb") as f:
                st.download_button("Download PNG", f, file_name=filename)
        except Exception as e:
            st.error(f"Error: {e}")

# 4. Upload and Decode
elif selection == "Upload & Decode DataMatrix":
    st.title("Upload and Decode DataMatrix Code")
    st.markdown("Upload a PNG image that contains a DataMatrix code. The tool will decode and display the embedded content.")

    uploaded_file = st.file_uploader("Upload a PNG image", type=["png"])

    if uploaded_file is not None:
        st.image(uploaded_file, caption="Uploaded Image", use_container_width=300)
        try:
            temp_path = "outputs/temp_uploaded.png"
            with open(temp_path, "wb") as f:
                f.write(uploaded_file.read())

            decoded = decode_datamatrix(temp_path)
            st.success("Decoding successful")
            st.code(f"{decoded}", language="text")
        except Exception as e:
            st.error(f"Could not decode the image: {e}")
    else:
        st.info("Please upload a PNG image containing a valid DataMatrix code.")
