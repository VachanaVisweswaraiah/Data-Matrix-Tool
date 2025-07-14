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
