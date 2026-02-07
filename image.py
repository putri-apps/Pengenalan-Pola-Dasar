import matplotlib.pyplot as plt
import cv2

five = cv2.imread("5.png")
plt.figure()
plt.imshow(cv2.cvtColor(five, cv2.COLOR_BGR2RGB))
print(five.shape)
print(five.size)
plt.title("five")
plt.axis("off")
plt.show()

babon = cv2.imread("logo_ipb-2.png")
babon_gray = cv2.cvtColor(babon, cv2.COLOR_BGR2GRAY)

plt.figure()
plt.imshow(cv2.cvtColor(babon, cv2.COLOR_BGR2RGB))
plt.title("babon")
plt.axis("off")
plt.show()

plt.figure()
plt.imshow(babon_gray, cmap="gray")
plt.title("babon_gray")
plt.axis("off")
plt.show()


pixels = five[100,100]
print(pixels)