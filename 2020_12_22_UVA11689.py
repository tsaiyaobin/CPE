num=int(input()) # 讀進有幾筆資料
for i in range(num):
    soda=0 # 存放今天可以換幾罐蘇打水
    # a是今天有的空瓶數量,b是今天撿到的空瓶數量,c是要多少空瓶才能換一瓶
    a,b,c=map(int,input().split()) 
    empty_bottles=a+b
    while empty_bottles>=c:
        soda+=empty_bottles//c
        empty_bottles=empty_bottles//c + empty_bottles%c
    print(soda)