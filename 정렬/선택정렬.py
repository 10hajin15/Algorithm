#선택정렬
#처리되지 않은 데이터 중에서 가장 작은 데이터를 선택해 맨 앞에 있는 데이터와 바꾸는 것을 반복

array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(len(array)):
    min_index = i   #가장 작은 원소의 인덱스
    for j in range(i+1, len(array)):
        if array[min_index] > array[j]:
            min_index = j
    array[i], array[min_index] = array[min_index], array[i] #스와프

print(array)

#선택정렬의 시간 복잡도
#구현 방식에 따라서 사소한 오차는 있을 수 있지만, 전체 연산 횟수는
#N + (N - 1) + (N - 2) + ... + 2
#이는 (N^2 + N - 2)/2, 빅오 표기법에 따라 O(N^2)