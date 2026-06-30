import os

任务文件 = "待办事项.txt"

任务列表 = []

def 加载数据():
	try:
		with open(任务文件, "r", encoding="utf-8") as f:
	
		return [line.strip() for line in f.readlines()]
	except FileNotFoundError:
		return []

def 保存数据():
	with open(任务文件, "w", encoding="utf-8") as f:
		for 任务 in 任务列表:
		f.write(任务 + "\n")

def 显示任务():
	if len(任务列表) == 0:
		print("\n📭 暂无待办事项")
	else:
		print("\n📋 你的待办清单：")
		for i, 任务 in enumerate(任务列表, 1):
		print(f"  {i}. {任务}")

	
任务列表 = 加载数据()

print("\n📝 待办事项清单 1.0\n输入 1 添加任务\n输入 2 删除任务\n输入 3 查看任务\n输入 0 退出")

while True:
	命令 = input("\n请输入命令：").strip().lower()
    
	if 命令 == "1":
		新任务 = input("请输入新任务：")
		if 新任务:
			任务列表.append(新任务)
			保存数据()
			print("✅ 已添加任务")
		else:
			print("⚠️ 任务内容不能为空")
    
	elif 命令 == "3":
		显示任务()
    
	elif 命令 == "2":
		显示任务()
		if len(任务列表) == 0:
			print("还未发现未完成的任务！")
			continue
		try:
			编号 = int(input("请输入要删除的任务编号："))
			if 1 <= 编号 <= len(任务列表):
				已完成 = 任务列表.pop(编号 - 1)
				保存数据()
				print(f"✅ 已删除任务：{已完成}")
			else:
				print("❌ 编号无效")
		except ValueError:
				print("❌ 请输入有效数字")
	elif 命令 == "0":
        保存数据()
        input("按回车键结束...")
        break
    
    else:
        print("❌ 未知命令，请输入 add / done / list / exit")