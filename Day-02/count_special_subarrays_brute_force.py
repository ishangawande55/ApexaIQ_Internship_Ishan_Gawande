def count_special_subarrays_brute_force(n, arr):
    count = 0  # Count of special subarrays
    
    # Iterate over all possible starting points
    for i in range(n):
        subarray_sum = 0
        subarray_xor = 0
        
        # Iterate over all possible ending points
        for j in range(i, n):
            subarray_sum += arr[j]  # Compute sum
            subarray_xor ^= arr[j]  # Compute XOR
            
            # Check if this subarray is special
            if subarray_sum == subarray_xor:
                count += 1  # Increment count
                
    return count

count_special_subarrays_brute_force(2, [4,5])