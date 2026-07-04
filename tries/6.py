import json
import os

数据文件="生成数据包/数据.json"
scores = {}

def 显示菜单():
	print("\n📊 数据分析系统")
	print("1. 添加数据")
	print("2. 查看所有数据")
	print("3. 查看统计信息")
	print("4. 数据分布分析")
	print("5. 删除项")
	print("6. 导入TXT数据")
	print("0. 退出")

def 添加数据():
    name = input("请输入数据项名称（如：一月、A组）：")
    if name in scores:
        print(f"⚠️ 数据项 '{name}' 已存在，数值为 {scores[name]}")
        return
    try:
        value = float(input("请输入数值："))
    except ValueError:
        print("⚠️ 请输入有效的数字")
        return
    scores[name] = value
    print(f"✅ 已添加 {name}: {value}")
    
def 查看数据():
    if not scores:
        print("📭 暂无数据")
        return
    print("\n📋 数据列表：")
    for name, value in scores.items():
        print(f"  {name}: {value}")
        
def 统计数据():
    if not scores:
        print("📭 暂无数据可统计")
        return
    total = len(scores)
    max_val = max(scores.values())
    min_val = min(scores.values())
    avg_val = sum(scores.values()) / total
    print("\n📊 统计信息：")
    print(f"  数据条数: {total}")
    print(f"  最大值: {max_val}")
    print(f"  最小值: {min_val}")
    print(f"  平均值: {avg_val:.2f}")
    
def 分布数据():
    if not scores:
        print("📭 暂无数据可分析")
        return
    try:
        print("请输入分组区间（以逗号分隔，如：10,20,30）：")
        bins_input = input("区间示例: 10,20,30 表示 <10, 10-20, 20-30, >30\n请输入: ")
        bins = [float(b.strip()) for b in bins_input.split(',') if b.strip()]
        if not bins:
            print("⚠️ 未输入有效区间")
            return
    except ValueError:
        print("⚠️ 请输入有效数字区间")
        return
    bins = sorted(bins)
    groups = {f"< {bins[0]}": 0}
    for i in range(len(bins)-1):
        groups[f"{bins[i]} - {bins[i+1]}"] = 0
    groups[f"> {bins[-1]}"] = 0
    for value in scores.values():
        if value < bins[0]:
            groups[f"< {bins[0]}"] += 1
        elif value > bins[-1]:
            groups[f"> {bins[-1]}"] += 1
        else:
            for i in range(len(bins)-1):
                if bins[i] <= value <= bins[i+1]:
                    groups[f"{bins[i]} - {bins[i+1]}"] += 1
                    break
    print("\n📊 数据分布：")
    for range_name, count in groups.items():
        print(f"  {range_name}: {count} 项")
        
def 删除数据():
    if not scores:
        print("📭 暂无数据可删除")
        return
    name = input("请输入要删除的数据项名称：")
    if name in scores:
        del scores[name]
        print(f"✅ 已删除数据项 {name}")
    else:
        print(f"⚠️ 未找到数据项 {name}")
        
def 保存数据():
    try:
        with open(数据文件, 'w', encoding='utf-8') as f:
            json.dump(scores, f, ensure_ascii=False, indent=4)
        print(f"✅ 数据已保存到 {数据文件}")
    except Exception as e:
        print(f"❌ 保存失败: {e}")

def 导入数据():
    file_path = input("请输入TXT文件的完整路径：")
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        
        成功计数 = 0
        跳过计数 = 0
        for line in lines:
            line = line.strip()
            if not line:
                continue
            
            parts = line.split(',')
            if len(parts) != 2:
                parts = line.split('\t')
            
            if len(parts) != 2:
                print(f"⚠️ 跳过格式错误行: {line}")
                跳过计数 += 1
                continue
            
            name = parts[0].strip()
            try:
                value = float(parts[1].strip())
            except ValueError:
                print(f"⚠️ 跳过 {name}，数值 '{parts[1].strip()}' 不是有效数字")
                跳过计数 += 1
                continue
            
            if name in scores:
                print(f"⚠️ 跳过已存在项: {name}，当前数值 {scores[name]}")
                跳过计数 += 1
                continue
            
            scores[name] = value
            成功计数 += 1
        
        print(f"✅ 导入完成！成功导入 {成功计数} 条，跳过 {跳过计数} 条记录。")
        保存数据()
    except FileNotFoundError:
        print(f"❌ 错误：找不到文件 '{file_path}'")
    except Exception as e:
        print(f"❌ 读取文件时发生错误: {e}")





if os.path.exists(数据文件):
    try:
        with open(数据文件, 'r', encoding='utf-8') as f:
            scores = json.load(f)
        print(f"✅ 已从 {数据文件} 加载数据")
    except Exception as e:
        print(f"❌ 加载数据失败: {e}")
        scores = {}
else:
    scores = {}
    print("📭 暂无历史数据，已创建新的数据文件")
while True:
    显示菜单()
    命令 = input("\n请输入命令编号：").strip()
    
    if 命令 == "0":
        print("👋 再见！")
        break
    elif 命令 == "1":
        添加数据()
        保存数据()
    elif 命令 == "2":
        查看数据()
        保存数据()
    elif 命令 == "3":
        统计数据()
        保存数据()
    elif 命令 == "4":
        分布数据()
        保存数据()
    elif 命令 == "5":
        删除数据()
        保存数据()
    elif 命令 == "6":
        导入数据()
        保存数据()        
    else:
        print("⚠️ 请输入正确指令")

input('输入回车键关闭')