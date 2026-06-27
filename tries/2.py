numbers = []


while True:
	print("\033[32m输入0关闭\n输入999查看统计\033[0m")
	num = input("请输入一个数字")

	num = int(num)
	if num == 999:
		if len(numbers) == 0:
			print("数字总量为空，无法统计")
		else:
			print("下面展示统计结果")
			total = sum(numbers)
			averge = total/len(numbers)
			print("总数：",total)
			print("平均数：",averge)			
	elif num == 0:
		print("再见")
	elif num > 10:
		print("这个数字很大")
		numbers.append(num)
	elif num < 10:
		print("这个数字很小")
		numbers.append(num)
	else:
		print("这个数字为10")
		numbers.append(num)