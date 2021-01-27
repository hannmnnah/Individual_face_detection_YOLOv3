import cv2
import os
import time

def video_cap(videoFile, imgpath, time_skips):
    start = time.time()
    cap = cv2.VideoCapture(videoFile)
    count = 0
    while(cap.isOpened()):
        ret, frame = cap.read()
        if ret :
            cv2.imwrite(imgpath+"/frame%d.jpg" % count, frame)
            print('%d.jpg done' % count)
            cap.set(cv2.CAP_PROP_POS_MSEC,(count*time_skips))
            count += 1
        
        else:
            break
        
    cap.release()

    runtime = 'runtime : {}'.format(time.time()-start)
    return runtime
