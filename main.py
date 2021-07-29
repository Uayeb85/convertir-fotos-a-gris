import cv2

imagen = cv2.imread('gato.jpg')

imagen_gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
invertir = cv2.bitwise_not(imagen_gris)
blur = cv2.GaussianBlur(invertir, (21,21),0)

inverted_blur = cv2.bitwise_not(blur)
final = cv2.divide(imagen_gris, inverted_blur, scale=256.0)

cv2.imwrite('gato.png', final)
