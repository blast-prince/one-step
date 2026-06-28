import os

DATA = "生成数据包/data.txt"

def 加载数据():
	try:
		with open(DATA,"r") as f:
			return [int(line.strip()) for line in f.readlines()]
	except FileNotFoundError:
		return[]

numbers = 加载数据()

def 保存数据():
	with open(DATA,"w") as f:
		for num in numbers:
			f.write(str(num) + "\n")


def 显示统计():
	if len(numbers) == 0:
		print("数字总量为空，无法统计")
	else:
		print("下面展示统计结果")
		total = sum(numbers)
		averge = total/len(numbers)
		print("总数：",total)
		print("平均数：",averge)

def 数字处理(num):
	if num > 10:
		print("这个数字很大")
		numbers.append(num)
	elif num < 10:
		print("这个数字很小")
		numbers.append(num)
	else:
		print("这个数字为10")
		numbers.append(num)

def 获取用户输入():
	while True:
		try:
			return int(input("请输入一个数字"))
		except ValueError:
			print("\033[31m❌ 请输入有效的数字！\033[0m")

def 显示历史记录():
		if len(numbers)==0:
			print("\033[33m📭 暂无历史记录\033[0m")
		else:
			print("\033[36m📜 历史记录：\033[0m")
			for i,num in enumerate(numbers,1):
				print(f"{i}、{num}")
			print(f"共{len(numbers)}条记录")
print("\033[32m输入0关闭\n输入999查看统计\n输入888查看历史记录\033[0m")
while True:
	num = 获取用户输入()
	if num == 999:
		显示统计()	
	elif num==888:
		显示历史记录()
	elif num == 0:
		保存数据()
		print("再见")
		break
	else:
		数字处理(num)