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
url1 = pyqrcode.create("https://meet.google.com/mhu-wczm-bbg")  # criar o qrcode
nomeArquivo1 = "qRSalaAula"
url1.png(nomeArquivo1 + ".png") # salvar o qrcode em um arquivo png
url1.show() # mostrar o qrcode na tela do computador


# 2
# criar um objeto pyqrcode
url2 = pyqrcode.create("https://www.youtube.com/")
nomeArquivo2 = "qRyoutube"
url2.png(nomeArquivo2 + ".png", scale=10) # salvar o qrcode em um arquivo png com escala de 10
url2.show()


# ler qrCode
# 3
# criar um objeto cv2
imagem1 = cv2.imread(nomeArquivo1 + ".png") # ler o arquivo png criado
imagem2 = cv2.imread(nomeArquivo2 + ".png")
# 4
# criar um objeto cv2
cv2.imshow("qrCode1", imagem1) # mostrar a imagem na tela do computador com o nome qrCode1
cv2.imshow("qrCode2", imagem2)
# 5
# criar um objeto cv2
cv2.waitKey(0) # esperar a tecla 0 para sair da imagem
cv2.destroyAllWindows() # fechar todas as janelas abertas
# 6
# criar um objeto cv2
cv2.imwrite("qrCode1.png", imagem1) # salvar a imagem na pasta do computador com o nome qrCode1.png
cv2.imwrite("qrCode2.png", imagem2)





