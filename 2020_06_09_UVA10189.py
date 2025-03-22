count=1
first=True
while True:
	index=input().split()
	if index == ['0','0']:
		break
	else:
		if first==False:
			print()
		first=False
		print(f"Field #{count}:")
		count+=1
		M,N=int(index[0]),int(index[1])
		arr=[[0 for j in range(N+2)]for i in range(M+2)]
		bomb=[]
		for k in range(M):
			bomb.append(input().split())
		position=[]	
		for i in range(1,M+1):
			for j in range(1,N+1):
				if bomb[i-1][0][j-1]=="*":
					position.append([i-1,j-1])
					arr[i-1][j-1]+=1
					arr[i-1][j]+=1
					arr[i-1][j+1]+=1
					arr[i][j-1]+=1
					arr[i][j+1]+=1
					arr[i+1][j-1]+=1
					arr[i+1][j]+=1
					arr[i+1][j+1]+=1
		for i in range(1,M+1):
			ans_str=""
			for j in range(1,N+1):
				if [i-1,j-1] in position:
					ans_str+="*"
				else:
					ans_str+=str(arr[i][j])
			print(ans_str)
		
			