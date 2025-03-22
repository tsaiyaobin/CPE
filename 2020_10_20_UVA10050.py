total=int(input()) #一共有幾筆data

for i in range(total):
	days=int(input()) # 天數範圍，假如是14，就是在14內放假的天數
	party_num=int(input()) # 有幾個人
	
	holiday=[]
	for i in range(party_num):
		party=int(input()) # 每隔幾天放一次假
		party_old=party
		while party<=days:
			# 禮拜五六本來就放假，所以不用算計去
			if party%7!=0 and party%7!=6 and party not in holiday:
				holiday.append(party)
			party+=party_old
			
				
	print(len(holiday))