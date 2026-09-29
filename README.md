# Renk Tabanlı Nesne Tespiti

OpenCV ile bir görüntüde belirli renkteki nesneyi tespit edip işaretleyen bir araç.

## Ne Yapıyor?
- Görüntüyü HSV renk uzayına çevirir
- Belirlenen renk aralığında maske oluşturur (cv2.inRange)
- Morfolojik işlemlerle maskeyi temizler (gürültü/delik)
- Konturları bulup nesnelerin etrafına kutu çizer ve sayar

## Kullanılan Teknolojiler
- Python, OpenCV, NumPy

## Nasıl Çalıştırılır?
```
python tespit.py
```