# utils.py
import segno
from PIL import Image
import os

def save_datamatrix(data: str, filename: str) -> str:
    """Generate and save a DataMatrix code as PNG"""
    dm = segno.make(data, micro=False)
    path = os.path.join("outputs", filename)
    dm.save(path, scale=5)
    return path

def ip_to_hex(ip: str) -> str:
    """Convert IP address to 8-char uppercase hex string"""
    parts = ip.strip().split(".")
    if len(parts) != 4:
        raise ValueError("Invalid IP format")
    hex_parts = [f"{int(p):02X}" for p in parts]
    return ''.join(hex_parts)
