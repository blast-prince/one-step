import os

# 文件名
TODO_FILE = "todo_list.txt"

# ---------- 功能函数 ----------
def load_todos():
    """从文件读取待办事项"""
    if not os.path.exists(TODO_FILE):
        return []
    with open(TODO_FILE, "r", encoding="utf-8") as f:
        return [line.strip() for line in f.readlines()]

def save_todos(todos):
    """保存待办事项到文件"""
    with open(TODO_FILE, "w", encoding="utf-8") as f:
        for item in todos:
            f.write(item + "\n")

def show_todos(todos):
    """显示所有待办事项"""
    if not todos:
        print("📭 当前没有待办事项")
    else:
        print("\n📋 你的待办清单：")
        for i, item in enumerate(todos, 1):
            print(f"  {i}. {item}")
        print()

# ---------- 主程序 ----------
def main():
    todos = load_todos()
    
    while True:
        show_todos(todos)
        print("请选择操作：")
        print("  [1] 添加事项")
        print("  [2] 删除事项")
        print("  [3] 退出")
        
        choice = input("输入数字选择：")
        
        if choice == "1":
            new_item = input("请输入待办事项：")
            todos.append(new_item)
            save_todos(todos)
            print("✅ 已添加！")
            
        elif choice == "2":
            if not todos:
                print("⚠️ 没有事项可删除")
                continue
            try:
                num = int(input("请输入要删除的编号："))
                if 1 <= num <= len(todos):
                    removed = todos.pop(num - 1)
                    save_todos(todos)
                    print(f"✅ 已删除：{removed}")
                else:
                    print("❌ 编号无效")
            except ValueError:
                print("❌ 请输入有效数字")
                
        elif choice == "3":
            print("👋 再见！")
            break
            
        else:
            print("❌ 无效选择，请重新输入")
        
        input("\n按回车键继续...")

if __name__ == "__main__":
    main()
