import qrcode
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers.pil import RoundedModuleDrawer

qr = qrcode.QRCode(
    version=4,  
    error_correction=qrcode.constants.ERROR_CORRECT_H,  
    box_size=10,  
    border=4  
)
qr.add_data("https://www.linkedin.com/in/arun-natarajan-")
qr.make(fit=True)

# Generate QR code with rounded edges
img = qr.make_image(
    fill_color="black",
    back_color="red",
    image_factory=StyledPilImage,  
    module_drawer=RoundedModuleDrawer()  
)

img.save("rounded_frame_qr.png")
