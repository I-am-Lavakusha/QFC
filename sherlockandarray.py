def balancedSums(arr):
    for i in range(len(arr)):
        total=sum(arr)
        right_sum=0
        left_sum=0
        for i in range(len(arr)):
            right_sum=total-left_sum-arr[i]
            if right_sum==left_sum:
                return "YES"
            
            left_sum+=arr[i]
            
        return "NO"
