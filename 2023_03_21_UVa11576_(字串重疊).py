n=int(input())
for i in range(n):
    # 字串長度為 k
    # 有 m 組輸入
	k,m=map(int,input().split())
	str_list=[input() for j in range(m)] # 讀數輸入的字串
	total=k #目前重組字串長度
	for p in range(1,m):
		rep=0 # 用來計算第 n 與 n-1 個字串有多少字重疊,eg: CAT、TED => T 重疊 => CATEFD
        # 最多只會有 k 個字母重疊,所以從 k 慢慢檢查到沒有重疊的情況
		for length in range(k,0,-1): 
			if str_list[p][0:length]==str_list[p-1][k-length:]:
				rep=length
				break
		total+=(k-rep)
	print(total)
	