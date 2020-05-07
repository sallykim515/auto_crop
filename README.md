# auto-crop
A python program that auto-crops a .png file with white background around one main non-white image.

# Overview
Created initially to remove white background margin around a fingerprint and potential "smudges" (partial fingerprints produced from accidental fumbling), the program crops around one main non-white image. 

# Getting Started
First, open the terminal and `cd` into the directory where you would like to download this program.
Then, clone the auto-crop repository
```
git clone https://github.com/sallykim515/auto-crop.git
```
Put .png file to crop inside the auto-crop folder. Note the filename.
Use the following command to run the program:
```
python sample.py
```
When prompted, enter the input filename noted from above. 
That's it! :)

# Example
The below is a screenshot of the terminal for auto-cropping fingerprint.png file:
<img width="840" alt="auto_crop_screenshot" src="https://user-images.githubusercontent.com/39283556/80664248-2075e900-8a4b-11ea-8541-5f72ad35054c.png">

Input file:  
<img width="607" alt="example_bordered" src="https://user-images.githubusercontent.com/39283556/80664260-253a9d00-8a4b-11ea-8220-2fe5ce9adbfd.png">

Output file:  
<img width="230" alt="example_cropped_bordered" src="https://user-images.githubusercontent.com/39283556/80664261-266bca00-8a4b-11ea-9c98-508434afe4d0.png">

(*Note, the borders were added for illustration purpose*)

# Behind the Scene
Libraries used: `numpy`, `cv2`, `sys`

## Algorithm
1. Compute averages of intensity values across rows and columns of an input image.
2. Only keep rows and columns with averages less than 253. This crops the white backgrounds around the main image and the smudge.
3. Identify "jumps" in the image from step 2, defined by a change in intensity value being greater than 10 in consecutive pixels.
4. Remove the jumps and onward, away from the main image - e.g. if the jumps are on the right half of the image, take the minimum column index of the strips and remove everything right of that idex.
5. Add a small padding (`default_padding=0.012`) all around to the image from step 4 before saving the image.

Note, an average approach is used since fingerprint itself contains white spaces and the program cannot distinguish a smudge from a main image in the beginning. Further what appears to be white background to naked eyes may not have the perfect 255 intensity value. Hence the program uses average values and treats 253+ as white background to be cropped.


## Potential Enhancements
* handling of multiple smudges
* ability to crop an image with non-white background

# Credits
The input `fingerprint.png` file was created using a clipart fingerprint from [Clipart Library](http://clipart-library.com/clipart/8i65bnx5T.htm) by Phillip Martin.
