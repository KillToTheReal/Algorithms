def radix_sort(arr, decimal_places=2):
  counts = [0] * 10
  len_arr = len(arr)
  # sort loop
  for step in range(decimal_places):
     temp_arr = [0] * len_arr
     print("Step",step)
     for item in arr:
       last_num = check_number(item, step)
       counts[last_num] += 1
    # compute prefix sum
     for i in range(1, 10):
       counts[i] += counts[i-1]

     for i in range(len_arr - 1, -1, -1):
        item = arr[i]
        last_num = check_number(item, step)
        index_num = counts[last_num] - 1
        counts[last_num] -= 1
        temp_arr[index_num] = item

     arr = temp_arr
     counts = [0] * 10
     del temp_arr
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
    
b = input("Введите максимальную степень десяти встречающуюся в массиве(10^n):")
  
print("Sorted array", radix_sort(arr,int(b)))
