import numpy as np
import cv2
import time
import pymysql

import os
os.chdir(os.path.dirname(os.path.abspath( __file__ )))

prevPath=''
while 1:
    conn = pymysql.connect(host='localhost', user='root', password='1234', db='mymydb', charset='utf8') 
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM data")
    res = cursor.fetchall()
    res='../../../HiSpeaker'+res[0][1][1:-4]+'.gif'
    conn.commit()
    conn.close()

    gif = cv2.VideoCapture(res)
    ret, frame = gif.read()
    width = 32
    height = 16
    dim = (width, height)

    if res!=prevPath:
        f = open("../../array_data","w")
        f.write('1 ')
        while ret:
            try:
                ret, frame = gif.read()
                frame = cv2.resize(frame, dim, interpolation=cv2.INTER_AREA)
                img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

                for i in range(0,16):
                    for j in range(0,32):
                        for k in range(0,3):
                            f.write(str(img[i][j][k])+' ')
            except:
                pass
        f.close()
    prevPath=res
    
# for n in range(0,count):
#     for i in range()
# closing all open windows
# cv2.destroyAllWindows()