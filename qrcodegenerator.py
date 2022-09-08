import qrcode
import image
qr = qrcode.QRCode(
    version= 15, #Higer the version complex and bigger the qr will be
    box_size=10, #Size of the qr code box 
    border=5 #Border for the qr code
)

data = "https://www.google.com/" #Link for which you want to generate qrcode

qr.add_data(data)
qr.make(fit=True)
img = qr.make_image(fill = "black",back_color="white")
img.save("Google.png")