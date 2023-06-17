import cv2
import os
import time
# kz
path = 'C:/Users/MSI/Desktop/khalil/OpenCV/Data/img'
cameraNo = 0
cameraBrightness = 500
frq = 8
minBlur = 450
grayImg = False
saveData = True
showImg = True
imgWidth = 180
imgHeight = 120
##########################################
global countFolder

cap = cv2.VideoCapture(cameraNo)
cap.set(3, 640)
cap.set(4, 480)
cap.set(10, cameraBrightness)
count = 0
countsave = 0


def saveDatafunction():
    global countFolder
    countFolder = 0
    while os.path.exists(path+str(countFolder)):
        countFolder = countFolder + 1
    os.makedirs(path+str(countFolder))


if saveData:
    saveDatafunction()
while True:

    sucess, img = cap.read()
    img = cv2.resize(img, (imgWidth, imgHeight))
    if grayImg:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    if saveData:
        blur = cv2.Laplacian(img, cv2.CV_64F).var()
        if count % frq == 0 and blur > minBlur:
            nowtime = time.time()
            cv2.imwrite(path+str(countFolder)+'/'+str(countsave) +
                        " " + str(int(blur)) + " " + str(nowtime) + ".png", img)
            countsave += 1
            print("succ")
        count += 1
    if showImg:
        cv2.imshow("image", img)
    if cv2.waitKey(1) & 0xFF == ord('s'):
        break

cap.release()
