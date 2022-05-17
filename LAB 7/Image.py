import cv2
import numpy as np

if __name__ == '__main__':
    src = cv2.imread('Images/PythonTestImage.jpg')

    b, g, r = cv2.split(src)
    cv2.imshow('Blue', b)
    cv2.imshow('Green', g)
    cv2.imshow('Red', r)
    cv2.waitKey(0)
    print(b)
    b[:, :] = 20
    print(b)
    mrgImg = cv2.merge([b, g, r])
    cv2.imshow('Merged', mrgImg)
    cv2.waitKey(0)
