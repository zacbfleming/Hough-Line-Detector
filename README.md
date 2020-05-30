# Hough-Line-Detector
The Hough line detector finds lines in an image using opencv. The app converts the image using a Canny edge detector then processes the image pixel by pixel. The app first finds the edges produced by the Canny detector then creates second 2D matrix with an x axis for theta (angles 0 - 180 deg) and a y axis for rho (distance from the origin). Each white pixel in the Canny image produces a theta (angle) and a rho (distance) information that is translated to the 2nd 2D matrix in the form of a vote. For example (a white pixel with a rho of 30 (30 pixels from origin) and the angle in degrees of the line from the origin to the white pixel relative to the x axis (i.e. 25 degrees) would increment the 2nd 2D matrix vector [30,25] by one. As the line detector processes all the white pixels in the image for rho and theta, the 'voting bins' (locations in the 2nd 2D matrix) with the most votes map the lines detected in the image. 

Once the app is executed the original image is shown (<spacebar> to progress to next image). Then the Canny image is displayed (<spacebar>). Finally the most prominent lines are colored green. To adjust the threshold for acceptable lines lower the number of acceptable votes (-v). The user can also change the resolution of the angles the app detects. A -t 1 will detect theta (angle of the line that connects the pixel to the origin relative to x) for all angles 1 to 180. Changing -t 10 will include a vote for all angles 1-10 in the same 'voting bin.'

-h will provide help 
-v allows user to adhust the threshold for votes
-i allows a user defined image
-t allows the user to enter the step size for theta (angles in degrees)

Install/Configuration

Clone all files in the manifest to the same folder

python requires...

-opencv 4.0.1
-numpy 1.18

Execution

python3 hough.py
 
