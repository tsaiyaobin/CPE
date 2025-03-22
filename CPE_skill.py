N=int(input())
for i in range(N):
    # 利用 map 將 str 轉 int 再轉 list
    num=list(map(int,input().split()))
    
    num_sort=sorted(num)

    # 直接解包並輸出，預設用空格分隔
    # eg:[1,2,3,4]-->1 2 3 4
    print(*num_sort)