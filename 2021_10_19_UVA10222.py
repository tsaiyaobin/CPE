# 使用到的技巧
# str.lower(): 將字串中所有字元轉換成小寫字母。
# str.upper(): 將字串中所有字元轉換成大寫字母。
# 這一題的 decode 不是用 ascii 碼，要看鍵盤。
dict_={'e':'q','r':'w','t':'e','y':'r','u':'t','i':'y','o':'u','p':'i','[':'o',']':'p'
,'d':'a','f':'s','g':'d','h':'f','j':'g','k':'h','l':'j',';':'k',"'":'l','c':'z'
,'v':'x','b':'c','n':'v','m':'b',',':'n','.':'m'}

num=int(input())
for i in range(num):
	str_=input()
	decode=""
	for j in str_.lower():
		if j in dict_:
			decode+=dict_[j]
		else:
			decode+=j
	print(decode)