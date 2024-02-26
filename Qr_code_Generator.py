import qrcode

def generate_qr_code(url, fname):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save(fname)
    img.show()

if __name__ == "__main__":
    url = "https://github.com/chaithrabc"
    fname = "new_qr.png"
    generate_qr_code(url, fname)
    print(f"QR code generated for {url} and saved as {fname}")
