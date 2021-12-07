driving = input('請問你有沒有開過車?y/n')
if driving != 'y' and driving !='n':
	print('只能輸入y/n')
	raise SystemExit

age = input("請問你的年齡?")
age = int(age)
if driving == 'y':
	if age >= 18:
		print('你通過測驗了')
	else:
		print("奇怪 你怎麼有開過車") 
elif driving == 'n':
	if age >=18:
		print('你可以考駕照了，還不去')
    else:
		print('很好 再過幾年就可以考了')