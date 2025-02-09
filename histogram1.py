import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread('lena.jpg')
cv.imshow('Original', img)

plt.figure()
plt.title('BGR Color Histogram')
plt.xlabel('Bins')
plt.ylabel('# of pixels')
colors= ('b', 'g', 'r')
for i,col in enumerate (colors):
    hist = cv.calcHist([img], [i], None, [256], [0,256])
    plt.plot(hist, color=col)
    plt.xlim ([0,256])
plt.show()

cv.waitKey(0)
cv.destroyAllWindows()