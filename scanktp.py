import cv2
import pytesseract
from pytesseract import Output

img = cv2.imread('images/train4.png')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
retval, threshold = cv2.threshold(img, 100, 255, cv2.THRESH_BINARY)


def scan(img,):
    h, w, c = img.shape
    boxes = pytesseract.image_to_boxes(img)
    for b in boxes.splitlines():
        b = b.split(' ')
        img = cv2.rectangle(
            img, (int(b[1]), h - int(b[2]), (int(b[3]),
                                             h - (int(b[4]))), (0, 255, 0), 2))

        custom_config = r'--oem 3 --psm 6'
        result_scan = pytesseract.image_to_string(img, config=custom_config)
        if result_scan:
            print(result_scan)
            file = open("recognition.txt", "w+")
            file.write(result_scan)
            file.close
            break


file = open("recognition.txt", "w+")
file.write(" ")
file.close()
scan(img)
