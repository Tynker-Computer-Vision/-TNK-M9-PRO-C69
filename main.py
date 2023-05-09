# import required libraries
import cv2
from cvzone.HandTrackingModule import HandDetector

# Capture the camera feed and set the resolution
cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)

# Creating object to detect hand
detector = HandDetector(detectionCon=0.8)


# Loop to display video
while True:

    try:
        # Get a single capture from the camera
        success, cameraFeedImg = cap.read()
        cameraFeedImg = cv2.flip(cameraFeedImg, 1)

        # Detect hand in cameraFeedImg
        hands, cameraFeedImg = detector.findHands(
            cameraFeedImg, flipType=False)

        if hands:
            # Hand 1
            hand1 = hands[0]
            lmList1 = hand1["lmList"]  # List of 21 Landmark points
            bbox1 = hand1["bbox"]  # Bounding box info x,y,w,h
            centerPoint1 = hand1['center']  # center of the hand cx,cy
            handType1 = hand1["type"]  # Handtype Left or Right
            fingers1 = detector.fingersUp(hand1)
            indexFingerTop = lmList1[8]
            indexFingerBottom = lmList1[6]

            print(fingers1)

    except Exception as e:
        print(e)

    # Show final image
    cv2.imshow("Image", cameraFeedImg)
    cv2.waitKey(1)
