import numpy as np
import time
import numpy as np


class ROI_Selection_Class:
    def timeit(func):
        def wrapper(*args, **kwargs):
            start = time.perf_counter()
            result = func(*args, **kwargs)
            end = time.perf_counter()
            elapsed = end - start
            print(f'Time taken: {elapsed:.6f} seconds')
            return result
        return wrapper
    
    @timeit
    def f3D_Circle_Mask_Generator(image_ds,center,radius):
        """creates a circular mask on image_ds based on the given center (x,y) coordinate and radius

        Args:
            image_ds MxNxZ array: image dataset a mask will be generated
            center 1x2 integer array: (x,y) coordinate for a central location for ROI
            radius integer: radius for determining size of circular array

        Returns:
            mask MxNxZ array: binary circular mask based on specified center location and radius 
        """
        [h,w] = np.shape(image_ds)[1:]
        #todo test error handling!!!
        assert center[0]+radius < h, "X Center Position + R is greater than image bounds"
        assert center[1]+radius < w, "Y Center Position + R is greater than image bounds"
        assert center[0]-radius > 0, "X Center Position - R is Less than image bounds"
        assert center[1]-radius > 0, "Y Center Position - R is Less than image bounds"
        mask = image_ds.copy()
        for i in range(0,h):
            for j in range(0,w):
                dist_from_center = np.sqrt((i-center[1])**2 + (j-center[0])**2)
                if dist_from_center <= radius:
                    mask[:,i,j] = 1
                else:
                    mask[:,i,j] = 0
        return mask
    
    @timeit
    def f2D_Circle_Mask_Generator(image_ds,center,radius):
        """creates a circular mask on image_ds based on the given center (x,y) coordinate and radius

        Args:
            image_ds MxNxZ array: image dataset a mask will be generated
            center 1x2 integer array: (x,y) coordinate for a central location for ROI
            radius integer: radius for determining size of circular array

        Returns:
            mask MxNxZ array: binary circular mask based on specified center location and radius 
        """
        [h,w] = np.shape(image_ds)
        #todo test error handling!!!
        assert center[0]+radius < h, "X Center Position + R is greater than image bounds"
        assert center[1]+radius < w, "Y Center Position + R is greater than image bounds"
        assert center[0]-radius > 0, "X Center Position - R is Less than image bounds"
        assert center[1]-radius > 0, "Y Center Position - R is Less than image bounds"
        mask = image_ds.copy()
        for i in range(0,h):
            for j in range(0,w):
                dist_from_center = np.sqrt((i-center[1])**2 + (j-center[0])**2)
                if dist_from_center <= radius:
                    mask[i,j] = 1
                else:
                    mask[i,j] = 0
        return mask

    @timeit
    def fImage_Mask_Mean(image_ds,mask):
        """find mean of image dataset for a given mask

        Args:
            image_ds MxNxZ array: image dataset that has non binary pixel values
            mask MxNxZ array:  binary mask that has the same shape as image_ds
        """
        # 
        return round(np.mean(image_ds[np.where(mask==1)]),2)

    @timeit
    def fImage_Mask_Std(image_ds,mask):
        """find std of image dataset for a given mask

        Args:
            image_ds MxNxZ array: image dataset that has non binary pixel values
            mask MxNxZ array:  binary mask that has the same shape as image_ds
        """
        # find std of given mask excluding zeros
        return round(np.std(image_ds[np.where(mask==1)]),2)