import cv2 as c
from datetime import datetime

wc = c.VideoCapture(0)
data_hora = datetime.now()
data_horaSTR = data_hora.strftime('_%d_%m_%Y---%H_%M_%S')
nomeFoto = 'imgPessoaAcessou' + data_horaSTR + '.png'

if wc.isOpened():
    funfando, fr = wc.read()
    while funfando:
        funfanfo, fr = wc.read()
        c.imshow('---', fr)
        break

    c.imwrite('./img/'+nomeFoto, fr)

wc.release()
c.destroyAllWindows()
