from flask import Flask, request, send_file, render_template
import io
import qrcode

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
  return render_template('index.html')
  
@app.route('/generate_qr_code', methods=['GET'])
def generate_qr_code():
    text = request.args.get('text')

    if not text:
        return 'Text parameter is missing', 400

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(text)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")

    # Convert the image to bytes and return as a file response
    img_bytes = io.BytesIO()
    img.save(img_bytes)
    img_bytes.seek(0)

    return send_file(img_bytes, mimetype="image/png")

if __name__ == '__main__':
    app.run(debug=True)
