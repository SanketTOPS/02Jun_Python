import qrcode

#url="https://www.tops-int.com/"

url="Hi, Hello Students! This is Secret"

qr=qrcode.make(url)
qr.save("secrect.png")