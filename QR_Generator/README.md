# QR Generator - Flask QR Code Generator

A simple Flask web app that takes a user-provided URL and generates a QR code instantly.

## Features

- URL input form
- URL normalization (adds https:// when missing)
- URL validation for http/https links
- Instant QR code generation in PNG format
- Responsive Bootstrap-based UI
- Side-by-side input/output layout on larger screens

## Tech Stack

- Python 3
- Flask
- qrcode
- Pillow
- Bootstrap 5

## Project Structure

```text
QR_Generator/
  app.py
  requirements.txt
  README.md
  templates/
    index.html
  static/
    style.css
```

## Setup

### 1) Create and activate a virtual environment

Windows PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

Git Bash:

```bash
python -m venv .venv
source .venv/Scripts/activate
```

### 2) Install dependencies

```bash
pip install -r requirements.txt
```

## Run the App

```bash
python app.py
```

Open in your browser:

- http://127.0.0.1:5000

## How to Use

1. Enter a URL in the input field (for example, example.com or https://example.com).
2. Click Generate QR.
3. The QR code appears in the output panel.

## Notes

- This uses Flask development server (debug mode) and is not for production deployment.
- For production, run behind a WSGI server like Gunicorn or Waitress.

## License

This project is for learning/demo purposes. Add a license file if you plan to distribute it.
