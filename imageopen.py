#how to show imange
# import cv2
# image=cv2.imread("download.jpeg")
# cv2.imshow("person",image)

# cv2.waitKey(0)
# cv2.destroyAllWindow()

import cv2
import cv2.data
import os
print(os.listdir(cv2.data.haarcascades))
# image=cv2.imread("group.jpg")
# filename="haarcascade_frontalface_default.xml"
# path=cv2.data.haarcascades+filename
# model=cv2.CascadeClassifier(path)
# faces=model.detectMultiScale(image,1.3,5)
# for face in faces:
    # x1=face[0]
    # y1=face[1]
    # x2=x1+face[2]
    # y2=y1+face[3]
# 
    # cv2.rectangle(image,(x1,y1),(x2,y2),[255,255,255],1)
# cv2.imshow("person",image)
# cv2.waitKey(0)
#cv2.destroyAllWindow()
