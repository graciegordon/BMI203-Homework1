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

vect=[3,-2,5,19]
finalSort=bubble(vect)
print finalSort

