import cv2
import numpy as np

input_file = "fingerprint_1"
output_file = input_file + "_cropped"


def find_keeps(non_empty):
    """
    Takes ndarray of increasing index.
    A jump in these indices suggests a location of smudge.
    Returns cleaned up ndarray to keep only by excluding the location of smudges.
    """
    idx_left = []
    idx_right = []

    # one way to spot a smudge is if consecutive indices "jump"
    for i in range(len(non_empty) - 1):
        if non_empty[i + 1] - non_empty[i] > 10:
            # save separately depending on the first or last half of the indices
            if i <= len(non_empty) / 2:
                idx_left.append(i)
            else:
                idx_right.append(i)
    # if on the first half the indices, its max is where valid index starts
    if idx_left:
        ml = non_empty[max(idx_left)]
    else:
        ml = min(non_empty)

    if idx_right:
        mr = non_empty[min(idx_right)]
    else:
        mr = max(non_empty)

    return ml, mr


def crop_im(im, padding=0.012):
    """
    Takes cv2 image, im, and padding % as a float, padding,
    and returns cropped image.
    """

    bw = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    rows, cols = bw.shape

    row_padding = int(rows * padding)
    col_padding = int(cols * padding)

    # use mean to gauge the amount of "whiteness" (the closer the mean to 255, the more white spaces it has)
    non_empty_columns = np.where(bw.mean(axis=0) < 253)[0]
    non_empty_rows = np.where(bw.mean(axis=1) < 253)[0]

    ml, mr = find_keeps(non_empty_columns)
    mt, mb = find_keeps(non_empty_rows)

    # crop the original image, applying appropriate paddings
    cropped = im[max(mt-row_padding, 0):min(mb+row_padding, rows),
              max(ml-col_padding, 0):min(mr+col_padding, cols),:]

    return cropped


im = cv2.imread(input_file+'.png')
cropped = crop_im(im)
cv2.imwrite(output_file+'.png', cropped)
print(f"Successfully created {output_file}")
