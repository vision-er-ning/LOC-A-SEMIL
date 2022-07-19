
#python 画柱状图折线图
#-*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.ticker as mtick
from matplotlib import rcParams
from matplotlib.font_manager import FontProperties
from pandas import DataFrame,Series
from cProfile import label
from scipy import signal
import matplotlib.pyplot as plt
#font = FontProperties(fname=r"c:\windows\fonts\simsun.ttc", size=14)
#a=[1228.3,3.38,63.8,0.07,0.16,6.74,1896.18]  #数据
#b=[0.12,-12.44,1.82,16.67,6.67,-6.52,4.04]

y_SEMIL = (1.15, 0.62, 0.44, 0.432, 0.427, 0.428)

y_compute = (0.12, 0.21, 0.26, 0.35, 0.72, 0.89)


rcParams['font.sans-serif']=['SimHei'] #显示中文字符
rcParams['axes.unicode_minus'] = False
config = {
    "font.family":'Time New',  # 设置字体类型
    #"font.size": ,
#     "mathtext.fontset":'stix',
}
rcParams.update(config)

l=[i for i in range(6)]

plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签

#fmt='%.2f%%'
#yticks = mtick.FormatStrFormatter(fmt)  #设置百分比形式的坐标轴
lx=[u'100',u'300',u'500',u'1000',u'5000',u'10000',]

fig = plt.figure()  
ax1 = fig.add_subplot(111)  
ax1.plot(l, y_compute,alpha=0.8,color= 'darkblue',label=u'Computational cost', linestyle='-.',marker='o')#折线图
plt.bar(l,y_SEMIL,width=0.4,alpha=0.8,color='maroon',label=u'Mean localization error(m)') #柱状图

#ax1.yaxis.set_major_formatter(yticks)

#for i,(_x,_y) in enumerate(zip(l,y_compute)):
#    plt.text(_x,_y,y_compute[i],color='black',fontsize=10,)  #将数值显示在图形上

ax1.legend(loc=1)
ax1.set_ylim([0, 1.3]);
ax1.set_ylabel('CDF',size = 18);
ax1.set_xlabel('Particle Number',size = 18);
#plt.legend(prop={'family':'SimHei','size':8})  #设置中文
#ax2 = ax1.twinx() # this is the important function
#plt.bar(l,y_SEMIL,alpha=0.3,color='blue',label=u'Mean localication error')
#ax2.legend(loc=2)
#ax2.set_ylim([0, 2500])  #设置右侧y轴取值范围
#plt.legend(prop={'family':'SimHei','size':16},loc="upper right")
#plt.grid()  #生成网格
plt.legend(loc='upper center',fontsize=12)
plt.xticks(l,lx)
plt.subplots_adjust(top=0.986, bottom=0.106, right=0.983, left=0.096, hspace=0, wspace=0)
plt.savefig("particle_number.png", dpi = 500)

plt.show()
