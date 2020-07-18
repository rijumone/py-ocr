# PyOCR
Simple OCR web app put together using Python's Flask and the [pytesseract](https://pypi.org/project/pytesseract/) library for the heavy lifting.

## Dependencies
### System
```bash
sudo apt install tesseract-ocr -y
```
### Python
```bash
pip install --upgrade pip wheel setuptools
pip install -r requirements.txt
```

## Usage
```bash
export FLASK_PYOCR_SECRET_KEY='super-secret-key'
export FLASK_PYOCR_DEBUG='false'
python server.py
```

## Demo
[http://riju.onthewifi.com:5000](http://riju.onthewifi.com:5000)