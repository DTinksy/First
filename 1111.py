import cv2
img = cv2.imread('1920x1080-px-artwork-digital-art-fantasy-art-house-ladders-leaves-ropes-science-fiction-trees-1254663.jpg')
print(img)

cv2.imshow('window', img)
cv2.waitKey(2000)
