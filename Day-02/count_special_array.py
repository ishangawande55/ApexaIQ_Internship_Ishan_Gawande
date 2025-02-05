from collections import defaultdict

def count_special_subarrays(n, arr):
    prefix_sum = 0
    prefix_xor = 0
    count = 0
    freq = defaultdict(int)

    # Initial condition
    freq[0] = 1  

    for i in range(n):
        prefix_sum += arr[i]
        prefix_xor ^= arr[i]
        
        # Check how many times (prefix_sum - prefix_xor) has appeared before
        count += freq[prefix_sum - prefix_xor]
        
        # frequency map
        freq[prefix_sum - prefix_xor] += 1
    
    return count

def main():
    T = int(input()) 
    for _ in range(T):
        N = int(input()) 
        A = list(map(int, input().split())) 
        print(count_special_subarrays(N, A))


main()