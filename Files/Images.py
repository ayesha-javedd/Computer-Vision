import cv2
IMAGE_PATHS = [
    "../Images/20160211_084607.jpg",
    "../Images/20160211_084835.jpg",
]

for path in IMAGE_PATHS:
    # Load the image from disk
    image = cv2.imread(path)

    if image is None:
        print(f"Error: could not load image at '{path}'")
        continue

    print(f"Loaded '{path}' successfully! Shape: {image.shape}")

    cv2.imshow(path, image)

# Wait for a key press, then close all windows
cv2.waitKey(0)
cv2.destroyAllWindows()
