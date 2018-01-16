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

listToSort=[-3,1,4,-1,2,20,32,7,10]
print(listToSort)

FinalList=quickSort(listToSort,0,len(listToSort)-1)

#print('done')
print(FinalList)
