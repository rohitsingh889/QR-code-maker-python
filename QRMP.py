import qrcode as qr
from PIL import Image


url = input("Enter the URL or text to generate QR Code: ")
fill_color = input("Enter the foreground color (e.g., black, red, orange): ")
back_color = input("Enter the background color (e.g., white, yellow, blue): ")

qr1 = qr.QRCode(
    version=1,
    error_correction=qr.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4
)


qr1.add_data(url)
qr1.make(fit=True)


img = qr1.make_image(fill_color=fill_color, back_color=back_color)


file_name = "custom_qrcode.png"
img.save(file_name)

print(f"✅ QR code generated with colors {fill_color} on {back_color} and saved as '{file_name}'")
