import pyaudio
import time
import numpy as np
import wave
import threading

import os
os.chdir(os.path.dirname(os.path.abspath( __file__ )))

mic=pyaudio.PyAudio()
CHUNK=1024
FORMAT=pyaudio.paInt16
CHANNELS=1 #마이크가 연결된 디바이스 번호
RATE=44100

stream= mic.open(format=FORMAT, channels=CHANNELS,rate=RATE,input=True, frames_per_buffer=CHUNK)

def Trans(Min,Max,min,max,value):
    if value<Min: value=Min
    if value>Max: value=Max

    rv=(value-Min)/(Max-Min)
    rv*=max-min
    return rv+min

def gotoxy(x,y):
    print ("%c[%d;%df" % (0x1B, y, x), end='')

def draw(matrix):
    gotoxy(0,0)
    for i in range(16):
        for j in range(32):
            if matrix[i][j]:
                print('*',end='')
            else:
                print(' ',end='')
            # print(matrix[i][j], end=' ')
        print()
    print()

while True:
    data=stream.read(CHUNK)
    data_int=np.array(wave.struct.unpack(str(2*CHUNK)+'B',data),dtype='b')

    matrix = [[0 for x in range(32)] for x in range(16)]

    for i in range(0,32):
        size=int(Trans(0,255,0,16,data_int[i]))
        for j in range(0,size):
            matrix[15-j][i]=1

    f = open("../../array_data","w")
    f.write('0 ')
    for i in range(16):
        for j in range(32):
            if matrix[i][j]:
                f.write('255 255 255 ')
            else:
                f.write('0 0 0 ')
    f.close()
    # break

    draw(matrix)
    time.sleep(0.1)