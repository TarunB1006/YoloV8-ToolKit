import cv2

# Load the image
image_path = r"path_to_image"
image = cv2.imread(image_path)

# Initialize lists to store coordinates
coordinates = []
sets_of_coordinates = []

# Resize the image for uniformity
#image = cv2.resize(re_image, (new_width, new_height)) assign values to new width and height

# Function to capture mouse click events
def click_event(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        # Add the clicked coordinates to the list
        coordinates.append((x, y))
        
        # Display the coordinates on the image
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(image, str((x, y)), (x, y), font, 0.5, (255, 0, 0), 2)
        cv2.imshow('image', image)
        
        # Check if 4 points have been captured
        if len(coordinates) == 4:                    # Made for a box , can change according to requirement of the shape
            print("Captured Coordinates:", coordinates)
            sets_of_coordinates.append(coordinates.copy())
            # Clear the list for the next set of coordinates
            coordinates.clear()

# Display the image and set the mouse callback function
cv2.imshow('image', image)
cv2.setMouseCallback('image', click_event)

# Wait indefinitely until any key is pressed
cv2.waitKey(0)

# Destroy all OpenCV windows
cv2.destroyAllWindows()

# Print all sets of captured coordinates
print("\nAll sets of captured coordinates:")
for i, coord_set in enumerate(sets_of_coordinates, 1):
    print(f"'J{i}': {coord_set},")
