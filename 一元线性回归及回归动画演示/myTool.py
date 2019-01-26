import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def computer_cost(x, y, w, b):
    m = len(x)
    cost = 0
    h_x = w * x + b
    cha = h_x - y
    fangcha = cha ** 2
    fangchahe = np.sum(fangcha)
    cost = 1 / (2 * m) * fangchahe
    return cost

def gradDec(x, y, w, b):
    m = len(y)
    h_x = w * x + b
    dw = (h_x - y) * x
    dw = np.sum(dw)/m
    db = h_x - y
    db = np.sum(db)/m
    return dw, db

def updata_param(w, b, dw, db, alpha):
    w = w - alpha * dw
    b = b - alpha * db
    return w, b

def model(x, y, alpha, iters):
    cost_list = []
    w = 0
    b = 0
    w_history=[]
    b_history=[]

    for i in range(iters):
        dw, db = gradDec(x, y, w, b)
        w, b = updata_param(w, b, dw, db, alpha)
        if i % 100 == 0:
            cost = computer_cost(x, y, w, b)
            cost_list.append(cost)
            w_history.append(w)
            b_history.append(b)
            print("第" + str(i) + "次梯度更新后的成本为：" + str(cost))

    return w, b, cost_list,w_history,b_history

def liner_reg_animation(x,y,w_history,b_history,frames,interval=50):
        '''
        功能:实现线性回归过程动画
        x:样本特征值
        y:样本标签值
        w_history:w历史数据
        b_history:b历史数据
        frames:动画帧数
        interval:动画间隔
        '''
        def f(x, w_his, b_his):  # 函数定义,求出给定的w,b下期望值
                return w_his*x+b_his

        i=0
        def updatefig(*args):  # FuncAnimation会将updatefig中的数据传递给绘图句柄,从而更新绘图
                nonlocal i #为了引用外部函数非容器型变量,加上nonlocal关键字
                if i == frames:
                        #print(i)
                        i = 0    
                w_his = w_history[i]
                b_his = b_history[i]
                i = i+1
                #print(i)
                line.set_data(x, f(x, w_his, b_his))
                return line,  # 这里的,很重要.

        fig = plt.figure()  # 获取matplotlib的绘图figure对象
        plt.scatter(x, y, label='train datas', color='r', s=50, marker='x')
        ax = plt.axes()
        line, = ax.plot([], [], lw=2)  # 取得plot对象,updatefig函数会调用此对象实现绘图.

        # im = plt.imshow(f(x, w,b), animated=True)  # 调用imshow实现绘图.这里参数animated=True很重要
        
        ani = animation.FuncAnimation(fig, updatefig, interval=50, blit=True)
        plt.show()