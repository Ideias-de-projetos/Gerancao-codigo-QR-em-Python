#
#
#
# links
# https://meet.google.com/mhu-wczm-bbg
# https://www.youtube.com/

# importar as bibliotecas
import qrcode
# instalação do OpenCV
# pip install opencv-python
import cv2

# 1
# criar um objeto qrcode
image1 = qrcode.make("https://meet.google.com/mhu-wczm-bbg")
image1.save('qRsalaAula.png')



