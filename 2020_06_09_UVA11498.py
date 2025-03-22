while True:
	num=int(input())
	if num==0:
		break
	else:
		division_point=input().split()
		N,M=int(division_point[0]),int(division_point[1])
		for i in range(num):
			position=input().split()
			x,y=int(position[0]),int(position[1])
			if x-N==0 or y-M==0:
				print("divisa")	
			elif  x-N>0 and y-M>0:
				print("NE")
			elif  x-N<0 and y-M>0:
				print("NO")
			elif  x-N<0 and y-M<0:
				print("SO")
			elif  x-N>0 and y-M<0:
				print("SE")