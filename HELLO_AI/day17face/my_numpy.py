import numpy as np

arr=[1,2,3]
arr_n = np.array(arr)

print(np.concatenate([arr_n, arr_n  ], 0))

