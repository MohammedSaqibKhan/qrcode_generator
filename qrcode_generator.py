import qrcode
import image
qr = qrcode.QRCode(
    version=15,
    box_size=10,
    border=5    
)

link = "https://youtu.be/HEvJGmaiGQc"
qr.add_data(link)
qr.make(fit=True)
img = qr.make_image(fill = 'black',back_color = 'white')
img.save('test.png')