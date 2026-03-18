def insertion(n,arr):
    if n <= 1:
        return arr

    # Traverse from second element
    for i in range(1, n):
        
        # Store current element to be inserted
        key = arr[i] 
        
        # Compare with previous elements        
        j = i - 1
        
        # Shift elements greater than key
        while j >= 0 and key[0] < arr[j][0]: 
            arr[j + 1] = arr[j]
            j -= 1
            
        # insert key at correct position
        arr[j + 1] = key 

    return arr

n=int(input("Enter No:"))
arr=[]
for i in range(n):
    a = input(f"Enter Element {i}:")
    arr.append(a)

print(insertion(n,arr))

print("The Sorted array without duplicate:")

u_arr=[]
for item in arr:
    if item not in u_arr:
        u_arr.append(item)

print(u_arr)

