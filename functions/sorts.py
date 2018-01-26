#sorts

def bubble(listToSort):
    assignment=0
    conditional=0
    listLen=len(listToSort)
    assignment+=1
    #check if list is empty

    for i in range(0,listLen):
        j=1
        assignment+=2
        while j<(listLen-i):
            conditional+=1
            if listToSort[j-1]>listToSort[j]:
                temp=listToSort[j]
                listToSort[j]=listToSort[j-1]
                listToSort[j-1]=temp;
                assignment+=3
            j+=1
            conditional+=1
            assignment+=1
        conditional+=1
    return listToSort,conditional, assignment

#this script takes in a list of integers and outputs a sorted list using the quicksort algorithm

def partition(ListToSort, p, r):
    assignment=0
    conditional=0    
    pivot_num=ListToSort[p]
    left=p
    pivot=left
    right=r
    assignment+=4
    while (left<right):
        conditional+=1
        while ListToSort[left]<=pivot_num:
            conditional+=1
            left+=1
            assignment+=1
        while ListToSort[right]>pivot_num:
            conditional+=1
            right-=1
            assignment+=1
        conditional+=1
        if left<right:
            ListToSort[left],ListToSort[right]=ListToSort[right],ListToSort[left]
            assignment+=1
        conditional+=1
    conditional+=1
    ListToSort[p]=ListToSort[right]
    ListToSort[right]=pivot_num
    #print('return',right)
    assignment+=2
    return right, conditional, assignment

    

def quickSort(ListToSort,p,right,conditional,assignment):
    conditional+=1
    if right>p:
        pivot,conditionals2,assignments2=partition(ListToSort,p,right)
        conditional+=conditionals2
        assignment+=assignments2
        #print(pivot)
        quickSort(ListToSort,p,pivot-1,conditional,assignment)
        quickSort(ListToSort,pivot+1,right,conditional,assignment)
    return ListToSort, conditional, assignment


