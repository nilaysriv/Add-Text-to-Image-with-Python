import cv2

def mouse_callback(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(f"Coordinates: ({x}, {y})")

def get_coordinates():
    #Image path
    image_path = input("Enter the path to the image: ")

    #Image
    image = cv2.imread(image_path)

    if image is None:
        print("Error: Unable to read the image. Please check the file path.")
        return

    # Create a window to display the image
    cv2.namedWindow("Image")

    # Set the mouse callback function
    cv2.setMouseCallback("Image", mouse_callback)

    # Display the image
    cv2.imshow("Image", image)

    # Wait until a key is pressed
    cv2.waitKey(0)

    # Destroy all OpenCV windows
    cv2.destroyAllWindows()

if __name__ == "__main__":
    get_coordinates()
