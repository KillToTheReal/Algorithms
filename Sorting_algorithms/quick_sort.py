'''
В переданном массиве из n элементов берем опорный элемент(примерно посередине) и создаем два массива с числами больше и меньше опорного, вызываем эту функцию рекурсивно

для n+1 Выполняются такие же правила

'''
def quicksort(array):
  if len(array) < 2:
    return array
  else:
    pivot = array[0]
    less = [i for i in array[1:] if i <= pivot]
    greater = [i for i in array[1:] if i > pivot]
    print("pivot:",pivot,"less",less,"greater",greater)
    return quicksort(less) + [pivot] + quicksort(greater)



arr=[]
a = input("Введите кол-во эл-тов массива: ")

for i in range(int(a)):
    n = input()
    arr.append(int(n))
    
arr = quicksort(arr)

print(arr)
