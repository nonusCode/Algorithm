# Bubble Sort : 인접한 두 개의 원소를 비교하여 자리를 교환하는 정렬 방식
# 시간 복잡도 : O(n^2)

def bubbleSort(arr):
    for i in range(len(arr)-1):
        for j in range(len(arr)-1-i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    
    return arr