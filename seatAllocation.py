# -*- coding: utf-8 -*-
"""
Created on Sun Jan  5 19:30:39 2020

@author: RamKrishan 

"""
"""
IN this Program I have taken 4 uses cases each have different if else statement

"""
    
def check_middle_postion_of_row(row,arr):
    n = 0
    for i in range(2,6):
        if arr[row][i] ==0:
            n +=1
                    
    if n==4:
        return 1
    else:
        return 0        
    
    
def seatAllocation(n,arr):
    """
    If number of seat request is 4
    """
    if(n==4):
        for k in range(3):
            val = check_middle_postion_of_row(k,arr)
            if val:
                for j in range(2,6):
                    arr[k][j] = 1
                break
        if(val==0):
            for k in range(3):
                arr[k][0] = 1
                arr[k][1] = 1
                arr[k][4] = 1
                arr[k][5] = 1
                break
             
        return arr     
         
    elif(n==3):
        for k in range(3):
            val = check_middle_postion_of_row(k,arr)
            if(val):
                for j in range(2,5):
                    arr[k][j] = 1
                break
        return arr
    
    elif(n==2):
        for k in range(3):
            if(arr[k][0]==0 and arr[k][1]==0):
                arr[0][0] =1
                arr[0][1] =1
            else:
                arr[k][6] =1
                arr[k][7] =1
            break
        return arr
        
    elif(n==1):
        for k in range(3):
            for j in range(8):
                if(arr[k][j]==0):
                    arr[k][j] = 1
                    break
            break    
                    
        return arr
    else:
        return 
    

arr = [[0 for i in range(8)] for j in range(3)]     
arr1 = [['1-a','1-b','1-c','1-d','1-e','1-f','1-g','1-h'],
       ['2-a','2-b','2-c','2-d','2-e','2-f','2-g','2-h'],
       ['3-a','3-b','3-c','3-d','3-e','3-f','3-g','2-h']]

arr2=seatAllocation(1,arr)
arr2=seatAllocation(4,arr)

l = []

for i in range(3):
    for j in range(8):
        if(arr2[i][j]==1):
            print(arr1[i][j])


