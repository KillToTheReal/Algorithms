'''
В начале строим max_heap дерево, чтобы максимальный элемент оказался в самом начале массива. 
Затем перемещаем максимум в конец и повторяем ту же операцию для n-1 массива.
'''

def heapify(arr, n, i):
  # print(arr)
  largest = i # Initialize largest as root
  left = 2 * i + 1     
  right = 2 * i + 2

  # See if left child of root exists and is
  # greater than root
  if left < n and arr[largest] < arr[left]:
    largest = left

  # See if right child of root exists and is
  # greater than root
  if right < n and arr[largest] < arr[right]:
    largest = right

  # Change root, if needed
  if largest != i:
    arr[i], arr[largest] = arr[largest], arr[i] # swap

    # Heapify the root.
    heapify(arr, n, largest)

# The main function to sort an array of given size


def heapSort(arr):
  n = len(arr)
  # print(arr)
  # строим maxheap для того чтобы начать алгоритм
  for i in range(n - 1, -1, -1):
    heapify(arr, n, i)
  print(arr)
  cnt = 0
    # One by one extract elements
  for i in range(n-1, 0, -1):
    # swap
    arr[i], arr[0] = arr[0], arr[i]
    heapify(arr, i, 0)
    cnt = cnt+1
    if i==n-2:
        print("Для 2го шага сумма первого и предпоследнего эл-тa: ",arr[0]+arr[len(arr)-2])
    print(cnt," шаг:",arr)


# Driver code
arr=[]
a = input("Введите кол-во эл-тов массива: ")

for i in range(int(a)):
    n = input()
    arr.append(int(n))
    
    
heapSort(arr)
n = len(arr)
print("Sorted array: ", arr)
