import cv2
from pyzbar.pyzbar import decode

# Capture video from the webcam
cap = cv2.VideoCapture(0)  # 0 for default camera

# Create a variable to store the QR code coordinates
qr_code_coordinates = None

while True:
    ret, frame = cap.read()

    if not ret:
        break

    # Convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect QR codes in the frame
    decoded_objects = decode(gray)

    for obj in decoded_objects:
        # Extract the coordinates of the QR code bounding box
        points = obj.polygon
        if len(points) == 4:
            qr_code_coordinates = [tuple(points[0]), tuple(
                points[1]), tuple(points[2]), tuple(points[3])]

        # Draw the bounding box around the QR code
        for j in range(4):
            cv2.line(frame, qr_code_coordinates[j], qr_code_coordinates[(
                j+1) % 4], (0, 255, 0), 3)

    # Display the frame with the detected QR code bounding box
    cv2.imshow('QR Code Detection', frame)

    # Break the loop if a QR code is detected
    if qr_code_coordinates:
        cv2.putText(frame, "QR Code Detected", (10, 30),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        cv2.imshow('QR Code Detection', frame)
# Print the coordinates of the QR code bounding box
        print(f"QR Code Coordinates: {qr_code_coordinates}")

    # Exit the loop when 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam (optional)
cap.release()

# Keep the window open until a key is pressed
cv2.waitKey(0)

# Close all OpenCV windows
cv2.destroyAllWindows()

