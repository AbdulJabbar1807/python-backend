def rotate_right(nums,k):
    nums = nums[-k:]+nums[:-k]
    return nums

def make_identity_grid(n):
    grid = [[0] * n for _ in range(n)]
    for i in range(n):
        grid[i][n-1-i] = 9
    return grid

def main():
    # 1
    nums = [1,2,3,4,5]
    k = 2
    
    rotated = rotate_right(nums,k)
    print(rotated)
    
    # 2
    latencies = [45, 120, 85, 310, 250, 90]
    slow_requests = [latency/1000 for latency in latencies if latency > 100]
    print(slow_requests)
    
    # 3
    n = 3
    print(make_identity_grid(n))
    
if __name__ == "__main__":
    main()
