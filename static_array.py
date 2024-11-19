arr = [1, 2, 3]
length = 3

def insertAtEnd(arr, n, length, capacity):
    if length < capacity:
        arr.append(n)
        length += 1
        print(f"Updated array: {arr}, Length: {length}")
    else:
        print("Array is full.")
        
def removeFromEnd(arr, length):
    if length <= 0:
        print("No data available in array")
    else:
        arr.pop()
        length -= 1
        print(f"Updated array: {arr}, Length: {length}")
    return length  # Return the updated length


def insertMiddle(arr, n):
    length = len(arr)
    middle_index = length//2
    new_arr = arr[:middle_index] + [n] + arr[middle_index:]
    print(f"Updated array: {new_arr}, Length: {length}")
    
def removeFromMiddle(arr):
    length = len(arr)
    middle_index = length//2
    new_arr = arr[:middle_index]+arr[middle_index:]
    print(f"Updated array: {new_arr}, Length: {length}")
    

insertAtEnd(arr, 4, 3, 10)
removeFromEnd(arr, length)
insertMiddle(arr, 78)
removeFromMiddle(arr)


