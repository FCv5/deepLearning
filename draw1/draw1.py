import numpy as np
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
font_fang = FontProperties(fname='C:/Windows/Fonts/simfang.ttf',size=28)

n=3
x1 = np.arange(-3,0,0.1) 
y1=1 / np.power(x1,n)
x2=np.arange(0.1,3,0.1) 
y2=1 / np.power(x2,n)


plt.figure()
plt.title(u'y1=20*sqrt(x)和y=5*x+20',fontproperties=font_fang,color='blue') #设置字体颜色
plt.xlabel(u'这是x轴',fontproperties='SimHei',fontsize=14)
plt.ylabel(u'这是y轴',fontproperties='SimHei',fontsize=14)
plt.plot(x1,y1)
plt.plot(x2,y2)
#plt.plot(x,y2)
#plt.plot([4],[40],'ro')

plt.show()