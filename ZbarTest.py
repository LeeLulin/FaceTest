import cv2
import pyzbar.pyzbar as pyzbar


def decodeDisplay(image):
    barcodes = pyzbar.decode(image)

    for barcode in barcodes:
        (x, y, w, h) = barcode.rect
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)
        barcodeData = barcode.data.decode('utf-8')
        text = "{}".format(barcodeData)
        cv2.putText(image, text, (x, y - 10), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 2)
        print("barcode: {}".format(barcodeData))

    return image


def detect():
    camera = cv2.VideoCapture(0)

    while True:
        ret, frame = camera.read()
        im = decodeDisplay(frame)
        cv2.namedWindow('camera')
        cv2.imshow('camera', im)
        if cv2.waitKey(5) & 0xFF == ord('q'):
            break

    camera.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    detect()
