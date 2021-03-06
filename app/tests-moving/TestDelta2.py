from __future__ import division

from app.other.Helper import *
import cv2
import app.Settings as Settings


def opticalFlowOverlay1(image_pv, image):
    image_pv = cv2.convertScaleAbs(
        image_pv, alpha=1.5, beta=60)
    image = cv2.convertScaleAbs(
        image, alpha=1.5, beta=60)

    new = np.subtract(
        image.astype(np.int16),
        image_pv.astype(np.int16),
    )
    new = np.absolute(new)
    new = new.astype(np.uint8)

    cv2.imshow('frame1', new)
    cv2.waitKey(0)


def testOpenCVOpticalMoving():
    def format_image(img):
        img = cv2.resize(
            img[250:-160, 150:-150], (0, 0), fx=2, fy=2)
        return img

    for _ in range(2000, 20400, 10):

        for i in range(_, _ + 10):
            image_pv = cv2.imread(
                Settings.TEST_FRAMES + '/'
                + str(i) + '.jpg', cv2.IMREAD_GRAYSCALE)
            image_pv = format_image(image_pv)

            image = cv2.imread(
                Settings.TEST_FRAMES + '/'
                + str(i + 1) + '.jpg', cv2.IMREAD_GRAYSCALE)
            image = format_image(image)

            opticalFlowOverlay1(image_pv, image)


testOpenCVOpticalMoving()
