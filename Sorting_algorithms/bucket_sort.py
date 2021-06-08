'''

Пытается исправить недостаток counting_sort, а именно выделение памяти под счет встречаемых чисел. 
Теперь мы берем все самое лучшее от нее и в тоже время пытаемся экономить память.
Система исчисления десятичная, значит нам нужно 10 ячеек памяти для промежуточного хранения данных. 
А далее мы начинаем поэтапно сортировать наш массив по разрядам. Сначала по нулевому, потом по десятичному и тд.
Количество циклов размещения зависит только от самого высокого разряда. К примеру если максимум встретится число до 100, то надо всего 2 цикла размещения и тд.

Важно упомянуть что эта сортировка подходит только для положительных чисел. 
Для отрицательных возможно стоит завести отдельный массив и добавлять в buckets в реверсивном порядке.

Также эта сортировка может выполнять много лишних операций в почти отсортированным массиве.

Недостаток этой сортировки в том, что операции с linked list очень медленные и в перспективе нам необходимо много раз выделять и очищать память под них, что не очень эффективно.

'''
def bucket_sort(arr, decimal_places=2):
  # в с++ можно было бы создать linked list 
  buckets = [[] for _ in range(10)]
  buckets_len = len(buckets)
  # sort loop
  for step in range(decimal_places):
    print("Step",step)
    for item in arr:
      last_num = check_number(item, step)
      buckets[last_num].append(item)
    print(buckets)

    array_step = 0
    for i in range(buckets_len):
      bucket_len = len(buckets[i])
      if bucket_len > 0:
        for j in range(bucket_len):
          arr[array_step] = buckets[i].pop(0)
          array_step += 1

    print(arr)

  return arr


def check_number(num, pos=0):
  if num < pos * 10:
    return 0
  res = 0
  for _ in range(pos+1):
    res = num % 10
    num = num // 10
  return res
  
arr=[]
a = input("Введите кол-во эл-тов массива: ")
for i in range(int(a)):
    n = input()
    arr.append(int(n))

print("Sorted array:",bucket_sort(arr))
