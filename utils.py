from pylibdmtx.pylibdmtx import encode
from PIL import Image
import os

def save_datamatrix(data: str, filename: str) -> str:
    """Generate a DataMatrix image and save it as PNG."""
    encoded = encode(data.encode("utf-8"))
    path = os.path.join("outputs", filename)

    # Write raw image bytes
    with open(path, "wb") as f:
        f.write(encoded)  # ✅ fix here (was: encoded.png)

    return path

def ip_to_hex(ip: str) -> str:
    parts = ip.strip().split(".")
    if len(parts) != 4:
        raise ValueError("Invalid IP format")
    return ''.join(f"{int(p):02X}" for p in parts)
