import cv2
import matplotlib.pyplot as plt
#@codicaly
print("---Python Cartoonizer---")
path = input("Enter the path to image : ")

img = cv2.imread(path)
img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
gray = cv2.medianBlur(gray,5)

edges = cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,9,2)

color = cv2.bilateralFilter(img,9,9,7)
cartoon = cv2.bitwise_and(color,color,mask=edges)
plt.figure(figsize=(10,10))
plt.imshow(cartoon,cmap="gray")
plt.axis("off")
plt.title("Cartoon Image")
plt.show()