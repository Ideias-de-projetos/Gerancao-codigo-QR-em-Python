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
nomeArquivo = "qRSalaAula"
url1.png(nomeArquivo + ".png")
url1.show()


# 2
# criar um objeto pyqrcode
url2 = pyqrcode.create("https://www.youtube.com/")
nomeArquivo = "qRyoutube"
url2.png(nomeArquivo + ".png", scale=10)
url2.show()


