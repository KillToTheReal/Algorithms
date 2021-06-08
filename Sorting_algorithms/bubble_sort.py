'''
С пузырьковой сортировкой думаю всё понятно
'''
def bubble_sort(arr):
    cnt = 0
    for i in range(len(arr) - 1):
        for j in range(i+1, len(arr)):
            cnt = cnt+1
            print("Шаг номер:",cnt, arr)
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
    return arr

arr=[]
a = input("Введите кол-во эл-тов массива: ")
for i in range(int(a)):
    n = input()
    arr.append(int(n))
    
print(bubble_sort(arr));
