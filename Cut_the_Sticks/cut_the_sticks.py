#!/bin/python3

import sys

def cutTheSticks(arr, result=[]):
    # Complete this function
    
    minLength = min(arr)
    for i in range (0, len(arr)):
        arr[i] -= minLength
    
    result.append(len(arr))
    #print(result)
    #print(arr)
    
    while True:
        if(0 not in arr):
            break
        arr.remove(0)
    
    #print(arr)
    #print(result)
    
    if ( len(arr) > 0):
        cutTheSticks(arr, result)
        return result
    else:
        #print("Cows")
        #print(result)
        return result
    
    
    
    
    
    
    
    

if __name__ == "__main__":
    n = int(input().strip())
    arr = list(map(int, input().strip().split(' ')))
    result = cutTheSticks(arr)
    #print(result)
    print ("\n".join(map(str, result)))
