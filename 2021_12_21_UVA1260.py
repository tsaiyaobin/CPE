# 題目在問第 n 天的時候前 n-1 天中有幾天 <= 當天 的營業額

num=int(input())
for i in range(num):
	test=int(input())
	listA=input().split()
	arr=[int(listA[0])]
	count=0
	for j in range(1,len(listA)):
		for k in range(len(arr)):
			if int(listA[j]) >= arr[k]:
				count+=1
		arr.append(int(listA[j]))
	print(count)	