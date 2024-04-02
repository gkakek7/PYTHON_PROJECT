import numpy as np
arr= list(range(9));
arr_n=np.array(arr)
arr_n2=np.reshape(arr_n,(3,3))

arr_n3=np.float16(arr_n2)

print(arr_n)
print(arr_n2)
print(arr_n3)
print(arr_n.shape)
print(arr_n2.shape)
