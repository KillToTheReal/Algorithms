'''
This is  MergeSort
Делим массив пополам до тех пор пока не останутся лишь единичные массивы. 
Затем начинаем объединять получившиеся массивы путем поэлементного сравнения, меньший элемент всегда помещаем влево
'''
#Функция для сортировки
def merge_sort(my_array=[]):
    
  if len(my_array) > 1:
    # делим массив пополам
    print(my_array)
    mid_index = len(my_array) // 2

    # формируем левый и правый массив
    left_array = my_array[:mid_index]
    right_array = my_array[mid_index:]

    left_array = merge_sort(left_array)
    right_array = merge_sort(right_array)

    i = j = k = 0
 
    while i < len(left_array) and j < len(right_array):
      # поочередно добавляем в исходный массив
      # либо из левого либо из правого, в зависимости
      # от того чей элемент меньше
      if left_array[i] < right_array[j]:
          my_array[k] = left_array[i]
          i += 1
      else:
          my_array[k] = right_array[j]
          j += 1
      k += 1

    # просто копируем массивы,
    # но так как мы не знаем в каком осталось больше
    # то мы запускаем 2 цикла, какой-то из них просто не 
    # запустится
    while i < len(left_array):
      my_array[k] = left_array[i]
      i += 1
      k += 1

    while j < len(right_array):
      my_array[k] = right_array[j]
      j += 1
      k += 1

  return my_array

arr=[]
a = input("Введите кол-во эл-тов массива: ")

for i in range(int(a)):
    n = input()
    arr.append(int(n))
    
arr = merge_sort(arr)

print("sorted:", arr)
