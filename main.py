import cv2 as cv
import numpy as np
import os
from dotenv import load_dotenv
import firebase_admin
from firebase_admin import credentials, db
import time

# Load the QRCode Detector
detector = cv.QRCodeDetector()

# Initialize the previous QR Code to avoid multiple updates for the same QR code
previousQRCode = ""

# Load the Firebase credentials and initialize the Firebase app
load_dotenv()
cred = credentials.Certificate("credentials.json")
firebase_admin.initialize_app(cred, {
    "databaseURL": os.getenv("FIREBASE_DB_URL"),
})

# Get the reference to the Firebase database node
ref = db.reference("/scanData/qrCode")

# Open the camera
cv.namedWindow("QR Scanner", cv.WINDOW_NORMAL)
cv.setWindowProperty("QR Scanner", cv.WND_PROP_FULLSCREEN, cv.WINDOW_FULLSCREEN)
vc = cv.VideoCapture(0)

# Check if the camera is opened or not
if vc.isOpened():
    rval, frame = vc.read()
else:
    rval = False
    print("Failed to open camera")

# Start the loop to read the QR code
while rval:
    rval, frame = vc.read()
    data, bbox, _ = detector.detectAndDecode(frame)
    if data:
        cv.polylines(frame, [np.int32(bbox)], True, (0, 255, 0), 5)
        ref.set(data)
        time.sleep(5)
    cv.imshow("QR Scanner", frame)
    key = cv.waitKey(20)
    if key == 27: # exit on ESC
        break

# Release the camera and destroy the window
vc.release()
cv.destroyWindow("QR Scanner")