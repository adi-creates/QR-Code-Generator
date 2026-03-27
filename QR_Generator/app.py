from __future__ import annotations

import base64
from io import BytesIO
from urllib.parse import urlparse

from flask import Flask, render_template, request
import qrcode


app = Flask(__name__)


def normalize_url(raw_url: str) -> str:
    """Normalize user input into a valid URL with a scheme."""
    candidate = raw_url.strip()
    if not candidate:
        return ""

    if not urlparse(candidate).scheme:
        candidate = f"https://{candidate}"

    parsed = urlparse(candidate)
    if parsed.scheme not in {"http", "https"} or not parsed.netloc:
        return ""

    return candidate


def generate_qr_data_uri(url: str) -> str:
    """Generate a QR image and return it as a base64 data URI."""
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_M,
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)

    image = qr.make_image(fill_color="black", back_color="white")
    buffer = BytesIO()
    image.save(buffer, format="PNG")
    encoded = base64.b64encode(buffer.getvalue()).decode("utf-8")
    return f"data:image/png;base64,{encoded}"


@app.route("/", methods=["GET", "POST"])
def index() -> str:
    submitted_url = ""
    normalized_url = ""
    qr_data_uri = ""
    error = ""

    if request.method == "POST":
        submitted_url = request.form.get("url", "")
        normalized_url = normalize_url(submitted_url)

        if not normalized_url:
            error = "Please enter a valid URL (for example: https://example.com)."
        else:
            qr_data_uri = generate_qr_data_uri(normalized_url)

    return render_template(
        "index.html",
        submitted_url=submitted_url,
        normalized_url=normalized_url,
        qr_data_uri=qr_data_uri,
        error=error,
    )


if __name__ == "__main__":
    app.run(debug=True)
