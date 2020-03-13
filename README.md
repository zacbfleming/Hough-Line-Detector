# Hough-Line-Detector
The Hough line detector finds lines in an image using opencv. The app converts the image using a Canny edge detector then processes the image pixel by pixel. The app first finds the edges produced by the Canny detector then creates second 2D matrix with an x axis for theta (angles 0 - 180 deg) and a y axis for rho (distance from the origin). Each white pixel in the Canny image produces a theta (angle) and a rho (distance) information that is translated to the 2nd 2D matrix in the form of a vote. For example a white pixel with a rho of 30 (30 pixels from origin) and adjacent white pixels at 45 deg would increment the 2D matrix location at x=30 and y=45 by one. As the line detector runs through all pixels in the image the 'voting bins' (location of votes in the 2D matrix) with the most votes map the lines detected in the image. 

-h will provide help 
-v allows user to adhust the threshold for votes
-i allows a user defines image
-t allows the user to enter the step size for theta (angles)

Install/Configuration
Copy all files in the manifest to the same folder

python requires

-opencv 4.0.1
-numpy 1.18
 
