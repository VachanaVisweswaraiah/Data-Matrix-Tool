Data Matrix Tool
================

This is a simple internal tool developed for **HORIBA FuelCon** to generate **Data Matrix Codes** from long strings or IP addresses. It streamlines encoding processes relevant to production and equipment labeling.

🌐 Live Demo
------------

[https://data-matrix-tool.onrender.com/](https://data-matrix-tool.onrender.com/)

🧩 Use Case
-----------

Designed to support internal workflows at HORIBA FuelCon, this tool helps encode:

*   Equipment identifiers
    
*   Network device IPs
    
*   Serial numbers and configuration strings into **Data Matrix codes** that can be scanned and printed using standard barcode readers like **PowerScan PM9600**.
    

📦 Features
-----------

*   Convert any long string into a scannable Data Matrix code
    
*   Convert IP addresses (IPv4) into compact hex-encoded Data Matrix
    
*   Instant barcode preview
    
*   One-click download as PNG
    
*   Built using **Streamlit** with Docker-based deployment
    

🗂 Project Structure
--------------------

```bash
├── app.py              # Streamlit frontend logic
├── utils.py            # Encode/decode utility functions
├── requirements.txt    # All dependencies
├── Dockerfile          # Containerization
├── .dockerignore
├── .gitignore
├── README.md
└── outputs/            # Saved barcode images
```

🚀 Run Locally
--------------

1.  Clone the repo:git clone [https://github.com/VachanaVisweswaraiah/Data-Matrix-Tool.git](https://github.com/VachanaVisweswaraiah/Data-Matrix-Tool.git)
    
2.  Navigate:cd Data-Matrix-Tool
    
3.  (Optional) Create virtual environment:python -m venv .venvsource .venv/bin/activate
    
4.  Install dependencies:pip install -r requirements.txt
    
5.  Run the app:streamlit run app.py
    
6.  Open:[http://localhost:8501/](http://localhost:8501/)
    

🐳 Docker Deployment
--------------------

Build and run with Docker:

1.  Build:docker build -t data-matrix-tool .
    
2.  Run:docker run -p 8000:8000 data-matrix-tool
    
3.  Access via:[http://localhost:8000/](http://localhost:8000/)
    

🏭 About HORIBA FuelCon
-----------------------

This tool was developed as part of internal tool support at **HORIBA FuelCon**, a leading provider of test systems for fuel cells, batteries, and hydrogen technologies. The tool simplifies code generation for labeling and tracking infrastructure assets.

👩‍💻 Author
------------

Built by [Vachana Visweswaraiah](https://github.com/VachanaVisweswaraiah) 
