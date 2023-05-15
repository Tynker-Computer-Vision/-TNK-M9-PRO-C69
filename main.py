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
        readVideo = cap.read()
        check = readVideo[0]
        cameraFeedImg= readVideo[1]

        cameraFeedImg = cv2.flip(cameraFeedImg, 1)

        # Detect hand in cameraFeedImg
        handsDetector = detector.findHands(cameraFeedImg, flipType=False)
        hands = handsDetector[0]
        cameraFeedImg = handsDetector[1]

        if hands:
            # Hand 1
            hand1 = hands[0]
            lmList1 = hand1["lmList"]  # List of 21 Landmark points
            handType1 = hand1["type"]  # Handtype Left or Right
            fingers1 = detector.fingersUp(hand1)

            currentFingerUp = ""
        
            if fingers1[0]== 1:
                currentFingerUp="Thumb"
            elif fingers1[1] == 1:
                currentFingerUp = "Index Finger"
            elif fingers1[2] == 1:
                currentFingerUp = "Middle Finger"
            elif fingers1[3] == 1:
                currentFingerUp = "Ring Finger"
            elif fingers1[4] == 1:
                currentFingerUp = "Little Finger"
            else:
                currentFingerUp = ""

     
            cv2.putText(cameraFeedImg, handType1 + " : " + currentFingerUp , (75, 90),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)


    except Exception as e:
        print(e)

    # Show final image
    cv2.imshow("Image", cameraFeedImg)
    cv2.waitKey(1)
