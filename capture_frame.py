import cv2
def capture_frame():
# Initialize the camera
    cam = cv2.VideoCapture(0)
# Read input from the camera
    result, image = cam.read()

# return the image
    if result:
        return image
    else:
        print("No image detected. Please try again.")
        return None

# Driver Code
res = capture_frame()
# Show the image
cv2.imshow("Captured Frame", res)
# Save the image - Optional
cv2.imwrite("captured_frame.png", res)
# Wait for any key to be pressed
cv2.waitKey(0)
# Destroy the window
cv2.destroyWindow("Webcam Image")

