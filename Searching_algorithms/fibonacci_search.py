from functools import lru_cache

def Fibonacci_Search():
  
  @lru_cache(maxsize=100)
  def FibonacciGenerator(n):
    if n < 1:
        return 0
    elif n == 1:
        return 1
    else:
        return FibonacciGenerator(n - 1) + FibonacciGenerator(n - 2)

  print("Fibonacci number 8:",FibonacciGenerator(8))

  def FibonacciSearch(arr, x):
    max_len = 0 
    # достигаем максимальной длины массива  
    while FibonacciGenerator(max_len) < len(arr): # 
        max_len = max_len + 1
    offset = -1
    print("Maximum length of array in fibonacci: ", max_len)

    # пока разбиение массива больше чем 1
    while (FibonacciGenerator(max_len) > 1):
        pos = min( offset + FibonacciGenerator(max_len - 2) , len(arr) - 1)
        print('Current Element : ', arr[pos], " fibbonacci number: ", FibonacciGenerator(max_len - 2), " length -",len(arr))

        if x > arr[pos]:
            max_len = max_len - 1
            offset = pos
        elif x < arr[pos]:
            max_len = max_len - 2
        else:
            return pos    
    """
    если в бинарном поиске мы увеличивали или уменьшали индекс
    вдвое, то тут мы идем в фибоначчи-виде
    """
    if FibonacciGenerator(max_len - 1) and arr[offset + 1] == x:
        return offset + 1
    return -1

  FibonacciSearch([10,12,13,14,15,16,17,18,20,21,23,46,54,55,57,60,61,63,65], 65)

Fibonacci_Search()
