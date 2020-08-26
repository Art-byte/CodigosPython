import qrcode
data = 'Lic. Karla Lizbeth Martínez Olguín\nEmail: karlamolguin17@gmail.com\nTel: 55 4386 8901'
fileName = "KarlaQR.png"
image = qrcode.make(data)
image.save(fileName)
print('Se ha generado el siguiente dato:\n',data)



