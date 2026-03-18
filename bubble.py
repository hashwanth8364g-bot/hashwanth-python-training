def bubble_assc(n,arr):

    swaps = 0
    for i in range(n):
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
                swaps+=1

    return arr , swaps

def bubble_desc(n,arr):

    swaps = 0
    for i in range(n):
        for j in range(n-i-1):
            if arr[j] < arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
                swaps+=1

    return arr , swaps

n = int(input("Enter No.of.elements:"))
arr=[]
for i in range(n):
    a = int(input(f"Element {i}:"))
    arr.append(a)

x , y = bubble_assc(n,arr)
print("Sorted Array ascending:",x)
print("No.of.Swaps:",y)

x , y = bubble_desc(n,arr)
print("Sorted Array desending:",x)
print("No.of.Swaps:",y)

