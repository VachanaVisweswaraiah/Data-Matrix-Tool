from pylibdmtx.pylibdmtx import encode, decode
from PIL import Image
import ipaddress
import os

def save_datamatrix(data: str, filename: str) -> str:
    encoded = encode(data.encode("utf-8"))
    with open(filename, "wb") as f:
        f.write(encoded.data)
    return filename

def ip_to_hex(ip_str: str) -> str:
    ip = ipaddress.IPv4Address(ip_str)
    return format(int(ip), '08X')

def decode_datamatrix(uploaded_file) -> str:
    img = Image.open(uploaded_file)
    result = decode(img)
    if result:
        return result[0].data.decode("utf-8")
    return ""
