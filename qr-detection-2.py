import cv2
from pyzbar.pyzbar import decode


def detectQR():
    # Capture video from the webcam
    cam = cv2.VideoCapture(0)  

# Read input from the camera
    result, image = cam.read()

# Create a variable to store the QR code coordinates
    qr_code_coordinates = None
    qr_code_detected = False


# Convert to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Detect QR codes
    decoded_objects = decode(gray)

# Initialize a flag to check if a QR code is detected
    qr_code_detected = False

    for obj in decoded_objects:
        # Extract the coordinates of the QR code bounding box
        points = obj.polygon
        if len(points) == 4:
            qr_code_coordinates = [tuple(points[0]), tuple(
                points[1]), tuple(points[2]), tuple(points[3])]

        # Draw the bounding box around the QR code
        for j in range(4):
            cv2.line(image, qr_code_coordinates[j], qr_code_coordinates[(
                j+1) % 4], (0, 255, 0), 3)
        # Set the flag to True as a QR code is detected
        qr_code_detected = True

    # Display the image with bounding boxes (optional)
    cv2.imshow('QR Code Detection', image)
    cv2.waitKey(0)
    # Release the webcam
    cam.release()
    cv2.destroyAllWindows()

    # Check if a QR code is detected and return True or False
    return qr_code_detected


res = detectQR()
print(res)