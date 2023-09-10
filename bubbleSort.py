def bolha_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]


Vetor = [7, 3, 6, 2, 4, 5, 1]
bolha_sort(Vetor)
print("Vetor:", Vetor)