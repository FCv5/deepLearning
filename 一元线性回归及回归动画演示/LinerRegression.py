import myTool
import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt('ex1data1.txt', delimiter=',')
# print(type(data))
x = data[:, 0]
y = data[:, 1]
# print(x)
# print(y)
plt.scatter(x, y, marker='x')
plt.show()

'''                       成本计算测试代码
test_x = np.array([0, 1, 2])
test_y = np.array([3, 4, 5])
print(myTool.computer_cost(test_x, test_y, 2, 1))
'''

'''
cost = myTool.computer_cost(x, y, 0, 0)
print(cost)
'''

'''
test_x = np.array([3, 7])
test_y = np.array([8, 10])
w = 3
b = 1
dw, db = myTool.gradDec(test_x, test_y, w, b)
print('dw:' + str(dw))
print('db:' + str(db))
'''

alpha = 0.01
iters = 1500

w, b, cost_list, w_history, b_history = myTool.model(x, y, alpha, iters)
print('w: ' + str(w))
print('b: ' + str(b))

# 回归动画代码开始
'''
fig = plt.figure()  # 获取matplotlib的绘图figure对象
plt.scatter(x, y, label='train datas', color='r', s=50, marker='x')
ax = plt.axes()
line, = ax.plot([], [], lw=2)  # 取得plot对象,updatefig函数会调用此对象实现绘图.


def f(x, w_his, b_his):  # 函数定义,求出给定的w,b下期望值
    return w_his*x+b_his

# im = plt.imshow(f(x, w,b), animated=True)  # 调用imshow实现绘图.这里参数animated=True很重要

i = 0

def updatefig(*args):  # FuncAnimation会将updatefig中的数据传递给绘图句柄,从而更新绘图
    global i
    if i == iters // 100:
        #print(i)
        i = 0    
    w_his = w_history[i]
    b_his = b_history[i]
    i = i+1
    #print(i)
    line.set_data(x, f(x, w_his, b_his))
    return line,  # 这里的,很重要.


ani = animation.FuncAnimation(fig, updatefig, interval=50, blit=True)
plt.show()
'''
frames=iters // 100 #计算帧数
myTool.liner_reg_animation(x,y,w_history,b_history,frames)
# 回归动画代码结束

plt.scatter(x, y, label='train datas', color='r', s=50, marker='x')
plt.plot(x, w * x + b, 'b-', label='predictions', linewidth=2)
plt.xlabel('numbers')
plt.ylabel('pay')
plt.legend()
plt.show()
