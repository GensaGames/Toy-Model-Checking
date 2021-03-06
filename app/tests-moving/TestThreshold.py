from __future__ import division

import cv2
import app.Settings as Settings


def opticalFlowOverlay1(image_pv, image):
    image = cv2.convertScaleAbs(
        image, alpha=1.5, beta=50)

    new = cv2.adaptiveThreshold(
        image, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
        cv2.THRESH_BINARY, 11, 2
    )
    cv2.imshow('frame1', new)
    cv2.waitKey(0)


def testOpenCVOpticalMoving():
    def format_image(img):
        img = cv2.resize(
            img[250:-160, 100:-100], (0, 0), fx=2, fy=2)
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
