import cv2

# 导入分类器
face_cascade=cv2.CascadeClassifier("D:/OpenCV/opencv/build/etc/haarcascades/haarcascade_frontalface_default.xml")

# 导入图片
image=cv2.imread("face.jpeg")

# 转灰度图
image_gray=cv2.cvtColor(image,cv2.COLOR_RGB2GRAY)

faces=face_cascade.detectMultiScale(image_gray,scaleFactor=1.1,minNeighbors=5,minSize=(30,30))

for (x,y,w,h) in faces:
    cv2.rectangle(image,(x,y),(x+w,y+h),(255,0,0),2)

# 展示图片
cv2.imshow("Display image",image)
cv2.imwrite("face-new.jpeg",image)
cv2.waitKey(0)
cv2.destroyAllWindows()
