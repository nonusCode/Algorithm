# Counting Sort : 원소들의 순서를 결정하기 위해 집합에 각 항목이 몇 개씩 있는지 세는 작업을 하여 임의의 배열에 넣어 정렬하는 방식
# 시간 복잡도 : O(n)

def countingSort(arr):
    # count 배열에 arr 배열내 원소의 빈도수 체크
    for i in arr:
        count[i] += 1
    # count 배열을 순회하면서 앞 쪽의 값을 더함
    for i in range(1, len(count)):
        count[i] += count[i-1]
    # arr 배열의 뒤쪽부터 순회하면서 count 배열을 참조하여 index를 찾고 res 배열에 넣음
    for i in range(len(arr)-1, -1, -1):
        res[count[arr[i]] - 1] = arr[i]
        count[arr[i]] -= 1

    return res

count = [0] * (max(arr)+1)   # count = arr 배열의 가장 큰 값 + 1만큼의 크기 배열
res = [0] * len(arr)