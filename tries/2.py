while True:
	num = input("请输入一个数字")
	num = int(num)
	if num == 0:
		print("再见")
	elif num > 10:
		print("这个数字很大")
	elif num < 10:
		print("这个数字很小")
	else:
		print("这个数字为10")
	