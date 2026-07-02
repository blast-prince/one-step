import json
import os

数据文件="生成数据包/数据.json"
scores = {}
data = input("请输入数据或导入文件地址")

def 显示菜单():
	print("\n📊 数据分析系统")
	print("1. 添加数据")
	print("2. 查看所有数据")
	print("3. 查看统计信息")
	print("4. 数据分布分析")
	print("5. 删除项")
	print("0. 退出")

def 添加数据():


def 查看数据():

def 统计数据():

def 分布数据():

def 删除数据():


while True:
	显示菜单()
	命令 = input("\n请输入命令编号：").strip()
	if 命令 == "0"
		print("👋 再见！")
		break
	elif: 命令=="1"
		添加数据()
	elif: 命令=="2"
		查看数据()
	elif: 命令=="3"
		统计数据()
	elif: 命令=="4"
		分布数据()
	elif: 命令=="5"
		删除数据()
	else:
		print("⚠️请输入正确指令")
input('输入回车键关闭')