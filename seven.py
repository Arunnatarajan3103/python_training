import qrcode
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers.pil import VerticalBarsDrawer

# Create QR Code
qr = qrcode.QRCode(
    version=5,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4
)
qr.add_data("https://www.linkedin.com/in/arun-natarajan-")
qr.make(fit=True)

# Generate QR code with circular dots
img = qr.make_image(
    fill_color="blue",
    back_color="black",
    image_factory=StyledPilImage,
    module_drawer=VerticalBarsDrawer()
)

# Save and Show QR Code
img.save("gapped_qr.png")
img.show()
