#code
no = int(input())
size = list()
arr = list()
for i in range(no):
    size = input().split()
    arr = input().split()

arr = [int(i) for i in arr]
size = [int(j) for j in size]

def subarray(arr):
    sum=0
    j=1
    for k in range(2):
        for i in range(len(arr)):
            sum = 0
            sum+=arr[i]
            for j in range(i+1,len(arr)):
                sum+=arr[j]
               
                if sum == size[1]:
                    
                    print("{} {}".format(i+1,j+1))
                    break 
            if sum ==size[1]:
                break
        
subarray(arr)
      