def find_pair_with_sum(arr, target):
    seen = {}  
    for num in arr:
        complement = target - num
        if complement in seen:
            return num, complement
        seen[num] = True  
    return None  

arr = [3, 1, 5, 2, 4]
target_sum = 9
result = find_pair_with_sum(arr, target_sum)

if result:
    print(f"Pair found: {result}")
else:
    print("No pair found")