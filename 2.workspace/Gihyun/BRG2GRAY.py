import cv2 

for i in range(1,29):
    imagePath = "/Users/seogihyun/Desktop/train_image/" + str(i) + ".jpg"
    img = cv2.imread(imagePath)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imwrite('/Users/seogihyun/Desktop/train_image/gray.'+ str(i) + '.jpg', gray)