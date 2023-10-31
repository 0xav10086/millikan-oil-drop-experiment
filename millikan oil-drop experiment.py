# 导入numpy模块
import numpy as np
# 导入math模块
import math
import matplotlib.pyplot as plt

# 定义一个常量e，表示电子的电荷
e = 1.602 * 10 ** (-19)

# 定义一个空列表，用来存储每组数据的q的值
q_list = []
# 定义一个空列表，用来存储每组数据的n的值
n_list = []

# 定义一个函数，接受四个数作为参数，返回它们的和乘以0.25
def average_four_numbers(a, b, c, d):
    return (a + b + c + d) * 0.25


# 定义一个空列表，用来存储每组数据的elementary charge的值
elementary_charge_list = []

# 用一个循环来重复执行代码，共5次
for i in range(5):
    # 打印提示信息，显示当前是第几组数据
    print("这是第", i + 1, "组数据")
    # 用input函数获取用户输入的四个整数，用逗号分隔
    integers = input("请输入四个整数，用逗号分隔：")
    # 用split方法将字符串分割成列表，用map方法将列表中的元素转换成整数，用*号解包成四个参数
    int_result = average_four_numbers(*map(int, integers.split(",")))
    # 打印结果
    print("四个整数的平均值是：", int_result)

    # 用input函数获取用户输入的四个浮点数，用逗号分隔
    floats = input("请输入四个浮点数，用逗号分隔：")
    # 用split方法将字符串分割成列表，用map方法将列表中的元素转换成浮点数，用*号解包成四个参数
    float_result = average_four_numbers(*map(float, floats.split(",")))
    # 打印结果
    # 打印结果，用round函数对浮点数进行四舍五入，保留两位小数
    print("四个浮点数的平均值是：", round(float_result, 2))

    # 计算q的值，用math.sqrt函数计算平方根，用**号计算幂
    # 用int函数将字符串转换为整数
    q = 9.283 * 10 ** (-15) / (float_result * (1 + 0.02264 * math.sqrt(float_result))) ** (3 / 2) * int(int_result)
    # 打印q的值，不保留小数，直接转换为字符串
    print("q的值是：", str(q))
    # 将每次计算出来的q的值添加到列表中
    q_list.append(q)
    # 计算n'的值，用q除以e
    n_prime = q / e
    # 打印n'的值
    print("n'的值是：", n_prime)
    # 计算n的值，用round函数对n'进行四舍五入，用int函数将结果转换为整数
    n = int(round(n_prime))
    # 将每次计算出来的n的值添加到列表中
    n_list.append(n)
    # 打印n的值
    print("n的值是：", n)

    # 计算elementary charge的值，用q除以n
    elementary_charge = q / n
    # 打印elementary charge的值，不保留小数，直接转换为字符串
    print("elementary charge的值是：", str(elementary_charge))

    # 将每次计算出来的elementary charge的值添加到列表中
    elementary_charge_list.append(elementary_charge)

# 计算e的值，由各组的elementary charge的和再乘以0.2求得
e = sum(elementary_charge_list) * 0.2
# 打印e的值，不保留小数，直接转换为字符串
print("e的值是：", str(e))

# 计算elementary charge的平均值
elementary_charge_mean = np.mean(elementary_charge_list)
# 计算de的值，由根号下各组的elementary charge减去elementary charge的平均值的差的平方的和再乘以0.05求得
de = math.sqrt(sum((x - elementary_charge_mean) ** 2 for x in elementary_charge_list)) * 0.05
# 打印de的值，不保留小数，直接转换为字符串
print("de的值是：", str(de))

# 定义一个常量e0，表示电子的电荷的标准值
e0 = 1.60217662 * 10 ** (-19)
# 计算error的值，由e0减去e的差除以e0再乘以100%求得，用abs函数取绝对值
error = abs(e0 - e) / e0 * 100
# 打印error的值，用str函数转换为字符串并添加百分号
print("error的值是：", str(error) + "%")

# 绘制q-n图像，用scatter函数绘制散点图，用plot函数绘制拟合曲线
plt.scatter(n_list, q_list, color='blue', label='data points') # 绘制散点图，设置颜色为蓝色，标签为"data points"
plt.plot(np.unique(n_list), np.poly1d(np.polyfit(n_list, q_list, 1))(np.unique(n_list)), color='red', label='fitted line') # 绘制拟合曲线，设置颜色为红色，标签为"fitted line"，使用numpy模块中的polyfit函数和poly1d函数进行线性拟合

# 设置图像的标题和坐标轴标签
plt.title('q-n plot') # 设置标题为"q-n plot"
plt.xlabel('n') # 设置x轴标签为"n"
plt.ylabel('q') # 设置y轴标签为"q"

# 显示图例
plt.legend()

# 显示图像
plt.show()