'''
Functions from Rene's MicroPy-toolbox for Data-analysis and processing. 
'''

# %% 
import numpy as np 

# %% Sharpness-measure

# from my MicroPy-Package
def diff_tenengrad(im):
    '''
    Calculates Tenengrad-Sharpness Metric.
    '''
    impix = 1.0 / np.prod(im.shape)
    return impix * np.sum(diff_sobel_horizontal(im)**2 + diff_sobel_vertical(im)**2, axis=(-2, -1))


def diff_sobel_horizontal(im):
    '''
    Calculates the horizontal sobel-filter.
    Filter-shape: [[-1 0 1],[ -2 0 2],[-1 0 1]] -> separabel:  np.outer(np.transpose([1,2,1]),[-1,0,1])
    '''
    # use separability
    trlist = transpose_arbitrary(im, idx_startpos=[-2, -1], idx_endpos=[1, 0])
    im = np.transpose(im, trlist)
    x_res = im[:, 2:] - im[:, :-2]  # only acts on x
    xy_res = x_res[:-2] + 2*x_res[1:-1] + x_res[2:]  # only uses the y-coords
    return np.transpose(xy_res, trlist)


def diff_sobel_vertical(im):
    '''
    Calculates the vertical sobel-filter.
    Filter-shape: [[-1,-2,-1],[0,0,0],[1,2,1]] -> separabel:  np.outer(np.transpose([-1,0,1]),[1,2,1])
    '''
    # use separability
    trlist = transpose_arbitrary(im, idx_startpos=[-2, -1], idx_endpos=[1, 0])
    im = np.transpose(im, trlist)
    x_res = im[:, :-2] + 2*im[:, 1:-1] + im[:, 2:]  # only x coords
    xy_res = x_res[2:] - x_res[:-2]  # further on y coords
    return np.transpose(xy_res)

def transpose_arbitrary(imstack, idx_startpos=[-2, -1], idx_endpos=[0, 1]):
    '''
    creates the forward- and backward transpose-list to change stride-order for easy access on elements at particular positions.

    TODO: add security/safety checks
    '''
    # some sanity
    if type(idx_startpos) == int:
        idx_startpos = [idx_startpos, ]
    if type(idx_endpos) == int:
        idx_endpos = [idx_endpos, ]
    # create transpose list
    trlist = list(range(imstack.ndim))
    for m in range(len(idx_startpos)):
        idxh = trlist[idx_startpos[m]]
        trlist[idx_startpos[m]] = trlist[idx_endpos[m]]
        trlist[idx_endpos[m]] = idxh
    return trlist