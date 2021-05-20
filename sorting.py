from typing import List
from timeit import default_timer as timer
import random
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


def quick_sort(numbers: List[int], low: int, high: int) -> None:
    if low < high:
        i = low
        pivot = numbers[high-1]
        for j in range(low, high):
            if numbers[j] < pivot:
                numbers[j], numbers[i] = numbers[i], numbers[j]
                i += 1
        numbers[i], numbers[high-1] = numbers[high-1], numbers[i]

        # recursive call
        quick_sort(numbers,low, i)
        quick_sort(numbers, i + 1, high)




# We need an easy way to make large lists of integers, for testing our sorting algorithms
# This function helps us create such lists easily
def create_random_integers(lower: int, upper: int, no_of_ints) -> List[int]:
    arr = []
    for _ in range(no_of_ints):
        arr.append(random.randint(lower, upper))
    return arr



if __name__=='__main__':

    # Due to how Python works, we must make copies of the lists we create
    # With the copy method
    test_numbers = create_random_integers(0,50,1000)
    test_numbers_copy = test_numbers.copy()
    
    # Test algorithms
    s = timer()
    quick_sort(test_numbers, 0, len(test_numbers))
    e = timer()
    difference1 = e - s
    #print(test_numbers)

    s = timer()

    insertion_sort(test_numbers_copy)
    e = timer()
    difference2 = e - s
    #print(test_numbers)
    print(f'quick_sort time: {difference1}, insertion_sort time = {difference2}')
    