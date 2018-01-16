#This program takes in an array and sorts it using a bubble sort

def bubble(listToSort):
    listLen=len(listToSort)
    #check if list is empty
    if listLen==0:
        return listToSort
    else:

        for i in range(0,listLen):
            j=1
            while j<(listLen-i):
                if listToSort[j-1]>listToSort[j]:
                    temp=listToSort[j]
                    listToSort[j]=listToSort[j-1]
                    listToSort[j-1]=temp;
                j+=1

    return listToSort


#this script takes in a list of integers and outputs a sorted list using the quicksort algorithm

def partition(ListToSort, p, r):
    
    pivot_num=ListToSort[p]
    left=p
    pivot=left
    right=r

    while (left<right):
        while ListToSort[left]<=pivot_num:
            left+=1
        while ListToSort[right]>pivot_num:
            right-=1
        if left<right:
            #print(ListToSort[left],ListToSort[right])
            ListToSort[left],ListToSort[right]=ListToSort[right],ListToSort[left]
            #print(ListToSort[left],ListToSort[right])
    
    ListToSort[p]=ListToSort[right]
    ListToSort[right]=pivot_num
    #print('return',right)
    return right

    

def quickSort(ListToSort,p,right):
    if right>p:
        pivot=partition(ListToSort,p,right)
        #print(pivot)
        quickSort(ListToSort,p,pivot-1)
        quickSort(ListToSort,pivot+1,right)
    return ListToSort


