import qrcode
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers.pil import CircleModuleDrawer

# Create QR Code
qr = qrcode.QRCode(
    version=8,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=15,
    border=5
)
qr.add_data("https://www.linkedin.com/in/arun-natarajan-")
qr.make(fit=True)

# Generate QR code with circular dots
img = qr.make_image(
    fill_color="red",
    back_color="black",
    image_factory=StyledPilImage,
    module_drawer=CircleModuleDrawer()
)

# Save and Show QR Code
img.save("circle_qr.png")
img.show()
