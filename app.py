from pylibdmtx.pylibdmtx import encode, decode
from PIL import Image
import os

def save_datamatrix(data: str, filename: str) -> str:
    """Generate and save a DataMatrix code as PNG."""
    encoded = encode(data.encode("utf-8"))
    img = Image.frombytes('RGB', (encoded.width, encoded.height), encoded.pixels)
    path = os.path.join("outputs", filename)
    img.save(path, format="PNG")
    return path

def decode_datamatrix(image_path: str) -> str:
    """Decode a DataMatrix image and return the content."""
    img = Image.open(image_path)
    decoded = decode(img)
    if decoded:
        return decoded[0].data.decode("utf-8")
    return "Could not decode DataMatrix."

def ip_to_hex(ip: str) -> str:
    parts = ip.strip().split(".")
    if len(parts) != 4:
        raise ValueError("Invalid IP format")
    return ''.join(f"{int(p):02X}" for p in parts)

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
    This tool lets you generate and decode DataMatrix codes for different use cases:

    - Convert a long string into a DataMatrix code.
    - Convert an IP address into multiple DataMatrix codes using its hex characters.
    - Upload and verify an existing DataMatrix image.
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

# 3. IP Address to DataMatrix (Updated: one code per hex character)
elif selection == "IP Address → DataMatrix":
    st.title("Convert IP Address to DataMatrix (one code per hex character)")
    ip_input = st.text_input("Enter IP Address (e.g. 192.168.0.1):")

    if st.button("Convert IP to DataMatrix") and ip_input:
        try:
            hex_string = ip_to_hex(ip_input)
            st.success(f"Hex representation: {hex_string}")

            for i, char in enumerate(hex_string):
                filename = f"ip_{ip_input.replace('.', '_')}_{i}_{char}.png"
                path = save_datamatrix(char, filename)
                st.image(path, caption=f"Character: {char}")

                with open(path, "rb") as f:
                    st.download_button(f"Download {char}.png", f, file_name=filename)
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
