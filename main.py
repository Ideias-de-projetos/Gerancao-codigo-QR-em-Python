#
#

# links/urls:
# https://meet.google.com/mhu-wczm-bbg
# https://www.youtube.com/

#### importar as bibliotecas  ####
import pyqrcode
import png

# instalação do OpenCV
# pip install opencv-python
import cv2
##### fim da importação #####


# 1
# criar um objeto qrcode
url1 = qrcode.make("https://meet.google.com/mhu-wczm-bbg")
url1.save('qRsalaAula.png')



