#
#

# links/urls:
# https://meet.google.com/mhu-wczm-bbg
# https://www.youtube.com/

#### importar as bibliotecas  ####
# pip install pyqrcode
# pip3 install pypng
import pyqrcode
import png

# instalação do OpenCV
# pip install opencv-python
import cv2
##### fim da importação ####  #


# 1
# criar um objeto pyqrcode
url1 = pyqrcode.create("https://meet.google.com/mhu-wczm-bbg")
nomeArquivo1 = "qRSalaAula"
url1.png(nomeArquivo1 + ".png")
url1.show()


# 2
# criar um objeto pyqrcode
url2 = pyqrcode.create("https://www.youtube.com/")
nomeArquivo2 = "qRyoutube"
url2.png(nomeArquivo2 + ".png", scale=10)
url2.show()


# ler qrCode
# 3
# criar um objeto cv2
imagem1 = cv2.imread(nomeArquivo1 + ".png")
imagem2 = cv2.imread(nomeArquivo2 + ".png")
# 4
# criar um objeto cv2
cv2.imshow("qrCode1", imagem1)
cv2.imshow("qrCode2", imagem2)
# 5
# criar um objeto cv2
cv2.waitKey(0)
cv2.destroyAllWindows()
# 6
# criar um objeto cv2
cv2.imwrite("qrCode1.png", imagem1)
cv2.imwrite("qrCode2.png", imagem2)

# decodificar qrCode
# 7
# criar um objeto cv2
decodificar1 = pyqrcode.decode(imagem1)
decodificar2 = pyqrcode.decode(imagem2)
# 8
print(decodificar1)


