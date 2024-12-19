import matplotlib.pyplot as plt
import time

class Figure_Generation_Class:
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
    def fCircle_Draw_Figure(image_ds,center,radius,level,window):
        fig,ax = plt.subplots()
        ax.imshow(image_ds,cmap='gray',vmax=level+float(window/2),vmin=level-float(window/2))
        circle = plt.Circle((center[0],center[1]),radius, color='tab:blue',fill=False)
        ax.add_patch(circle)
        plt.show()