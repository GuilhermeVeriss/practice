# Solution for day 11 

if __name__ == '__main__':

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))
    
    max_sum = 0
    
    for r in range(4):
        for c in range(4):
            hsum = 0 
            for i in range(3):
                hsum += arr[r][c+i]
                hsum += arr[r+2][c+i]
            hsum += arr[r+1][c+1]
            
            if r + c == 0:
                max_sum = hsum
            elif hsum > max_sum:
                max_sum = hsum
    
    print(max_sum)
