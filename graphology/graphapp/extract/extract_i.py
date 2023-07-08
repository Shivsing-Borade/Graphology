import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pickle
import os
import glob
import cv2
import math

# Slant of the handwritten image
# Input: BGR Image
# Output: Slant angle of the image


def slant_angle(img):
    img = cv2.bilateralFilter(img, 5, 700, 700)
    

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    centroids = []
    # Apply image preprocessing techniques
    # Example: Adaptive thresholding
    _, thresholded = cv2.threshold(
        gray, 0, 255, cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
    contours, _ = cv2.findContours(
        thresholded, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    for contour in contours:
        # Calculate the moments of the contour
        moments = cv2.moments(contour)
        a = []
    # Calculate the centroid coordinates
        try:
            cx = int(moments['m10'] / moments['m00'])
            cy = int(moments['m01'] / moments['m00'])
        except Exception:
            continue
        a.append(cx)
        a.append(cy)
        centroids.append(a)

    stem = centroids[0]

    stem_contour = contours[0]
    # min_y = centroids[0][1]
    for i in range(len(centroids)):
        if centroids[i][1] > stem[1]:
            stem = centroids[i]
            stem_contour = contours[i]

    # print(stem_contour)
    if True:
        # Fit a line through the contour using linear regression
        [vx, vy, x, y] = cv2.fitLine(stem_contour, cv2.DIST_L2, 0, 0.01, 0.01)

    # Calculate the inclination angle of the line
        angle = np.arctan2(vy, vx) * 180 / np.pi

        if angle < 0:
            angle += 180

        return 180 - angle[0]


# Position of the dot in the handwritten image with respect to stem
# Input: BGR Image
# Output: Position ['left','right','balanced']
def pos_of_dot(image):
    b_f_img = cv2.bilateralFilter(image, 5, 700, 700)
    angle = slant_angle(image)
    gray = cv2.cvtColor(b_f_img, cv2.COLOR_BGR2GRAY)
    _, thresholded = cv2.threshold(
        gray, 0, 255, cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
    contours, _ = cv2.findContours(
        thresholded, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    centroids = []
    for contour in contours:
        # Calculate the moments of the contour
        moments = cv2.moments(contour)
        a = []
    # Calculate the centroid coordinates
        try:
            cx = int(moments['m10'] / moments['m00'])
            cy = int(moments['m01'] / moments['m00'])
        except Exception:
            continue
        a.append(cx)
        a.append(cy)
        centroids.append(a)

        dot = centroids[0]
        stem = centroids[0]

        dot_contour = contours[0]
        stem_contour = contours[0]
    # min_y = centroids[0][1]
        for i in range(len(centroids)):
            if centroids[i][1] < dot[1]:
                dot = centroids[i]
                dot_contour = contours[i]
        for i in range(len(centroids)):
            if centroids[i][1] > stem[1]:
                stem = centroids[i]
                stem_contour = contours[i]
    dot[1] = thresholded.shape[1]-dot[1]
    stem[1] = thresholded.shape[1]-stem[1]

    slope = (dot[1] - stem[1]) / (dot[0] - stem[0])
    angle_rad = math.atan(slope)
    angle_dot = math.degrees(angle_rad)
    if angle_dot < 0:
        angle_dot += 180

    if angle_dot < angle-10:
        return "right"
    elif angle_dot >= angle-10 and angle_dot <= angle+10:
        return "Balanced"
    else:
        return "Left"


# Height of the dot in the handwritten image with respect to stem
# Input: BGR Image
# Output: Height of the dot (Euclidean distance between dot and top of stem)
def height_of_dot(image):
    image = cv2.resize(image, (228, 228))
    b_f_img = cv2.bilateralFilter(image, 5, 700, 700)
    angle = slant_angle(image)
    gray = cv2.cvtColor(b_f_img, cv2.COLOR_BGR2GRAY)
    _, thresholded = cv2.threshold(
        gray, 0, 255, cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
    contours, _ = cv2.findContours(
        thresholded, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    centroids = []
    for contour in contours:
        # Calculate the moments of the contour
        moments = cv2.moments(contour)
        a = []
    # Calculate the centroid coordinates
        try:
            cx = int(moments['m10'] / moments['m00'])
            cy = int(moments['m01'] / moments['m00'])
        except Exception:
            continue
        a.append(cx)
        a.append(cy)
        centroids.append(a)

        dot = centroids[0]
        stem = centroids[0]

        dot_contour = contours[0]
        stem_contour = contours[0]
    # min_y = centroids[0][1]
        for i in range(len(centroids)):
            if centroids[i][1] < dot[1]:
                dot_contour = contours[i]
        for i in range(len(centroids)):
            if centroids[i][1] > stem[1]:
                stem_contour = contours[i]

    top_point = tuple(stem_contour[stem_contour[:, :, 1].argmin()][0])
    centroid = cv2.moments(dot_contour)["m10"] / cv2.moments(dot_contour)[
        "m00"], cv2.moments(dot_contour)["m01"] / cv2.moments(dot_contour)["m00"]
    return math.sqrt((centroid[0] - top_point[0]) ** 2 + (centroid[1] - top_point[1]) ** 2)
