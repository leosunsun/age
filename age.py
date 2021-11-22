driving = input ('请问你有没有开过车')
if driving != '有' and driving != '没有': 
	print ('只能输入 有/没有')
	raise SystemExit

age = input ('请问你的年龄？')
age = int (age)
if driving == '有': 
	if age >= 18:
		print ('你通过了！')
	else:
		print ('你不可能吧…')
elif driving == '没有': 
	if age >= 18: 
		print ('去考驾照吧')
	else: 
		print ('别着急，再等几年就可以考驾照咯')