def muteCut(arr):
    fi = 0
    fe = len(arr)-1
    
    while True:
        if arr[fi]>2:
            break
        else:
            fi+=1
            
    while True:
        if arr[fe]>2:
            break
        else:
            fe -=1
    
    return arr[fi-1:fe+2]

arr = [0,0,0,0,0,0,0,0,0,5,7,8,5,4,0,0,0]
arr_cut=muteCut(arr)
print(arr_cut)