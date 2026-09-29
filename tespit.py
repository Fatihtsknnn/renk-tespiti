import cv2
import numpy as np

img = cv2.imread("yaprak.jpg")
if img is None:
    print("HATA: Resim okunamadi")
    exit()

hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

alt_yesil = np.array([30,40,40])
ust_yesil = np.array([90,255,255])

maske = cv2.inRange(hsv,alt_yesil,ust_yesil)

cv2.imshow("Orijinal",img)
cv2.imshow("Yesil maske",maske)
cv2.waitKey(0)
kernel = np.ones((5,5),np.uint8)
maske = cv2.morphologyEx(maske,cv2.MORPH_OPEN,kernel)
maske = cv2.morphologyEx(maske,cv2.MORPH_CLOSE,kernel)

konturlar, _ = cv2.findContours(maske,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
sonuc = img.copy()
nesne_sayisi = 0
for kontur in konturlar:
    alan = cv2.contourArea(kontur)
    if alan > 500:
        x,y,w,h = cv2.boundingRect(kontur)
        cv2.rectangle(sonuc,(x,y),(x+w,y+h),(0,0,255),2)
        nesne_sayisi = nesne_sayisi + 1
        print("Tespit edilen nesne sayisi:",nesne_sayisi)

cv2.imshow("Tespit sonucu:",sonuc)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite("tespit_sonucu.jpg",sonuc)
print("Sonuç kaydedildi!")
