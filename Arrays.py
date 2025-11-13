# 1.Reverse array
def reverseArray(a):
    return a[::-1]

# 2.hourglass
def hourglassSum(arr):
    max1=-math.inf
    for row in range(len(arr)-2):
        for coloum in range(len(arr)-2):
            a=arr[row][coloum]+arr[row][coloum+1]+arr[row][coloum+2]+arr[row+1][coloum+1]+arr[row+2][coloum]+arr[row+2][coloum+1]+arr[row+2][coloum+2]
            if a>=max1:
                max1=a
    return max1
        
# 3.Electronics shop
def getMoneySpent(keyboards, drives, b):
    max1=-1
    for i in keyboards:
        for j in drives:
            if i+j<=b and i+j>max1:
                max1=i+j
    return max1
