import qrcode

# Generación básica
img = qrcode.make("https://ejemplo.com")
img.save("codigo_qr.png")

# Generación avanzada con personalización
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data("Texto o URL a codificar")
qr.make(fit=True)
img = qr.make_image(fill_color="blue", back_color="red")
img.save("qr_personalizado.png")   