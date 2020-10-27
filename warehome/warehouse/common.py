import qrcode


def generateQRcode(id):
    filename = str(id) + '_itemQR.png'
    image = qrcode.make(f'http://192.168.1.107:8000/warehouse/itemPage/{id}/')
    path = 'C:\\Users\\uzer\PycharmProjects\warehome\warehome\static\images\qrcodes\\'
    image.save(path + filename)

    return path
