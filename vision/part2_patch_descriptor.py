#!/usr/bin/python3

import numpy as np


def compute_normalized_patch_descriptors(
    image_bw: np.ndarray, X: np.ndarray, Y: np.ndarray, feature_width: int
) -> np.ndarray:
    """Create local features using normalized patches.

    Normalize image intensities in a local window centered at keypoint to a
    feature vector with unit norm. This local feature is simple to code and
    works OK.

    Choose the top-left option of the 4 possible choices for center of a square
    window.

    Args:
        image_bw: array of shape (M,N) representing grayscale image
        X: array of shape (K,) representing x-coordinate of keypoints
        Y: array of shape (K,) representing y-coordinate of keypoints
        feature_width: size of the square window

    Returns:
        fvs: array of shape (K,D) representing feature descriptors
    """

    ###########################################################################
    # TODO: YOUR CODE HERE                                                    #
    ###########################################################################
    fvs = []
    if feature_width%2 == 1:
      low = (feature_width+1)//2
      high = (feature_width+1)//2 + 1
    else:
      low = (feature_width)//2 - 1
      high = (feature_width)//2 + 1
    padded_image = np.pad(image_bw, (low, high))
    padded_X = X + low
    padded_Y = Y + low
    for i in range(X.shape[0]):
      window = padded_image[int(padded_Y[i]-low):int(padded_Y[i]+high),int(padded_X[i]-low):int(padded_X[i]+high)]
      window = window/np.linalg.norm(window)
      window = window.reshape([feature_width**2])
      fvs.append(window)
    fvs = np.array(fvs)

    


    # raise NotImplementedError('`compute_normalized_patch_descriptors` ' +
    #     'function in`part2_patch_descriptor.py` needs to be implemented')

    ###########################################################################
    #                             END OF YOUR CODE                            #
    ###########################################################################

    return fvs
