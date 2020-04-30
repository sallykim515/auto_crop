# auto_crop
A python program that auto-crops a .png file with white background around one main non-white image.

# Overview
Created initially to remove white background margin around a fingerprint and potential "smudges" (partial fingerprints produced from accidental fumbling), the program crops around one main non-white image. 

# Getting Started
First, open the terminal and `cd` into the directory where you would like to download this program.
Then, clone the auto_crop repository
```
git clone https://github.com/sallykim515/auto_crop.git
```
Put .png file to crop inside the auto_crop folder. Note the filename.
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

# Credits
The input `fingerprint.png` file was created using a clipart fingerprint from [Clipart Library](http://clipart-library.com/clipart/8i65bnx5T.htm) by Phillip Martin.