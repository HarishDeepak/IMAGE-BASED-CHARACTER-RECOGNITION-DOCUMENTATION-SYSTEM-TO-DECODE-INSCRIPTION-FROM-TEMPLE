import cv2
import numpy as np

# border removal by inpainting
def border_removal(box_bw,top,bottom,right,left):    
    box_bw[0:top,:]=255   # first "top"  number of rows
    box_bw[-bottom:,]=255 # last "bottom" number of rows
    box_bw[:,0:left]=255  # first "left" number of columns
    box_bw[:,-right:]=255 # last "right" number of columns
    # last two rows a[-2:,]
    return box_bw

def preprocess_image(image_path, save_path):
    remove_border_size = 20;
    # Read the image
    image = cv2.imread(image_path)

    

    # Resize the image to a reasonable size
    resized_image = cv2.resize(image, (800, 600))  # Adjust the size as needed

    # Convert to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply adaptive thresholding to binarize the image
    #binary = cv2.adaptiveThreshold(gray, 255,cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY,  91,10)
    #binary = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 91, 17)
    windowSize = 91
    windowConstant =17
    # Apply the threshold:
    binary = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, windowSize, windowConstant)

   

    # Remove noise using a median blur
    denoised = cv2.medianBlur(binary, 5)

    # Enhance contrast using histogram equalization
    equalized = cv2.equalizeHist(denoised)

    # Apply bilateral filter for smoothing while preserving edges
    smoothed = cv2.bilateralFilter(equalized, 3, 75, 75)

    # Apply morphological operations to further remove small noise
    kernel = np.ones((3, 3), np.uint8)
    morph_open = cv2.morphologyEx(smoothed, cv2.MORPH_OPEN, kernel, iterations=2)

    # Sharpen the image using the unsharp masking technique
    alpha = 1.5  # Adjust the alpha value based on your preference
    beta = -0.5  # Adjust the beta value based on your preference
    sharpened = cv2.addWeighted(morph_open, alpha, smoothed, beta, 0)

    struc_element = cv2.getStructuringElement(cv2.MORPH_RECT,(5,5))
    Output=cv2.erode(sharpened,struc_element)

    # Save the preprocessed image
    cv2.imwrite(save_path, smoothed)

# Replace 'your_image_path.jpg' with the actual path to your image
image_path = 'data/atam.anc.exp0.jpg'
output_path = 'data/atam.anc.exp0.jpg'

preprocess_image(image_path, output_path)
