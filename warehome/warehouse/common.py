import qrcode


def generateQRcode(id):
    filename = str(id) + '_itemQR.png'
    image = qrcode.make(f'http://192.168.1.107:8000/warehouse/itemPage/{id}/')
    path = 'C:\\Users\\uzer\PycharmProjects\warehome\warehome\static\images\qrcodes\\'
    image.save(path + filename)

    relativePath = (path + filename).split('\\')

    return ('/' + relativePath[6] + '/' + relativePath[7] + '/' + relativePath[8] + '/' + relativePath[9])

print(generateQRcode(2))
