import cv2

Source="Lily.jpg"
Destination="New_imag.jpg"
scale_percent=50 #percent by which image is resized

img=cv2.imread(Source,cv2.IMREAD_UNCHANGED)

if img is None:
    print("Error: Image not loaded properly. Please check the file path.")
else:
    """
    # Display the image
    cv2.imshow("Lily", img) # show image
    """
    
    # Calculate the 50 percent of original dimensions
    new_width=int(scale_percent * img.shape[1] / 100)
    new_height=int(scale_percent * img.shape[0] / 100)

    new_img=cv2.resize(img, (new_width,new_height))

    cv2.imwrite(Destination,new_img)
    
    # cv2.waitKey(0)

    # cv2.destroyAllWindows() # Destroys the window showing image
