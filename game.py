# 作业
#
# 每个操作封装成一个函数
#
# 创建英雄：当前游戏中，创建英雄角色，定义好对应英雄的血量及其攻击力。
# 查看英雄信息：查看当前游戏中所有的英雄信息。
# 修改英雄信息：修改英雄的血量。
# 删除英雄：英雄太弱，不需要，删除掉。
# 退出系统：结束程序

# 创建英雄
def create_hero():
    name = input("请输入英雄的姓名：")
    volume = input("请输入英雄的血量：")
    power = input("请输入英雄的攻击力：")
    hero_data = {"name": name, "volume": volume, "power": power}

    return hero_data

# 查看英雄
def find_hero(hero_list):
    print(f"当前游戏所有英雄的信息：{hero_list}")


# 修改英雄
def alter_hero(hero_list):
    hname = input("请输入要修改的英雄姓名：")
    n = 0
    for i in hero_list:
        if hname == i["name"]:
            volume = input("请输入要修改英雄的血量：")
            hero_list[n]["volume"] = volume # 修改血量
            print(f"修改后的英雄信息：{hero_list[n]}")
            return hero_list
        n += 1
    print("没有找到英雄！")
    return hero_list

# 删除英雄
def delete_hero(hero_list):
    hname = input("请输入需要删除的英雄：")
    for i in hero_list:
        if hname == i["name"]:
            print(f"要删除的英雄信息：{i}")
            hero_list.remove(i)
            return hero_list
    print("没有找到要删除的英雄！")
    return hero_list


def console():
    print('''
        1. **创建英雄**
        2. **查看英雄信息**
        3. **修改英雄信息**
        4. **删除英雄**
        5. **退出系统**
        ''')

    hero_list = [] # 英雄列表
    while True:

        result = input("请输入数字，选择要完成的操作：")

        if result == "1":
            hero = create_hero() # 创建英雄
            hero_list.append(hero) # 将英雄加入列表
        elif result == "2":
            find_hero(hero_list) # 查看英雄
        elif result == "3":
            alter_hero(hero_list) # 修改英雄血量
        elif result == "4":
            delete_hero(hero_list) # 删除英雄
        elif result == "5":
            break

if __name__ == '__main__':
    console()
