

def selectionSort(array):
    n = len(array)
    for i in range(n):
        min = i
        for j in range(i+1,n):
            if(array[j]<array[min]):
                min = j
        temp = array[i]
        array[i]=array[min]
        array[min] = temp
    return array

array = []
n = int(input("Enter number of elements : "))
for i in range(0, n):
    element = int(input())
 
    array.append(element)
     
print(selectionSort(array))


#OUTPUT
#Python 3.9.6 (tags/v3.9.6:db3ff76, Jun 28 2021, 15:26:21) [MSC v.1929 64 bit (AMD64)] on win32
#Type "help", "copyright", "credits" or "license()" for more information.
#>>> 
#== RESTART: D:/Users/bipali/Desktop/BE/Third year BE/Sem 6/AI/selectionsort.py =
#Enter number of elements : 15
#54
#56
#48
#52
#45
#41
#87
#56
#20
#10
#45
#98
#23
#54
#75
#[10, 20, 23, 41, 45, 45, 48, 52, 54, 54, 56, 56, 75, 87, 98]
