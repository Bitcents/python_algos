from typing import List
from timeit import default_timer as timer

# the simplest of sorting algorithms
# these implementations were inspired by psuedocode found in wikipedia
# for explanations, head to the corresponding wikipedia page
def selection_sort(numbers: List[int]) -> None:
    for i in range(len(numbers)):
        for j in range(i, len(numbers)):
            if numbers[j] < numbers[i]:
                numbers[i], numbers[j] = numbers[j], numbers[i]
            

def insertion_sort(numbers: List[int]) -> None:
    i = 1
    n = len(numbers)
    
    while (i < n):
        j = i
        while j > 0 and numbers[j-1] > numbers[j]:
            numbers[j-1], numbers[j] = numbers[j], numbers[j-1]
            j -= 1
        i += 1
        
    

def bubble_sort(numbers: List[int]) -> None:
    n = len(numbers)
    flag = True
    while(flag):
        newn = 0
        for i in range(1, n):
            if numbers[i-1] > numbers[i]:
                numbers[i - 1], numbers[i] = numbers[i], numbers[i-1]
                newn = i
        n = newn
        flag = not newn <= 1




if __name__=='__main__':
    test_numbers = [23,65,2,6,4,1,1,2,10,7,12,13,18,21,24,17,29,42,51]
    
    s = timer()
    bubble_sort(test_numbers)
    e = timer()
    difference1 = e - s
    print(test_numbers)

    test_numbers = [23,65,2,6,4,1,1,2,10,7,12,13,18,21,24,17,29,42,51]

    s = timer()
    insertion_sort(test_numbers)
    e = timer()
    difference2 = e - s
    print(test_numbers)
    print(f'bubble_sort time: {difference1}, insertion_sort time = {difference2}')
    