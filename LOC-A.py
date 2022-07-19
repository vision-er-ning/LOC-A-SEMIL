from cProfile import label
from scipy import signal
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pylab import *
from pandas import DataFrame,Series
#file = open('C:/Users/Administrator/Desktop/语义定位手稿/gyr_synthetic_tran-2.txt')
x_deepnavi=[0,0.5,1,1.5,2,2.5,3]
y_deepnavi=[0,0.556,0.756,0.847,0.91,0.946,0.972]
x_SVL=[0,0.5,1,1.5,2,2.5,3]
y_SVL= [0,0.682,0.906,0.936,0.963,0.98,0.985]
x_L_SVL=[0,0.5,1,1.5,2,2.5,3]
y_L_SVL= [0,0.64,0.87,0.914,0.948,0.969,0.976]
x_VMag=[0,0.5,1,1.5,2,2.5,3]
y_VMag=[0,0.61,0.853,0.926,0.951,0.972,0.983]
x_SEMIL=[0,0.5,1,1.5,2,2.5,3]
y_SEMIL = [0,0.652,0.896,0.946,0.961,0.975,0.986]
# for line in file:
#     if line != "\n":
#         data.append(line)
# print(len(data))
#data = file.readlines()
#画图
#figure(figsize=(16,8),dpi=200)

rcParams['font.sans-serif']=['SimHei'] #显示中文字符
rcParams['axes.unicode_minus'] = False

config = {
    "font.family":'Time New',  # 设置字体类型
    #"font.size": ,
#     "mathtext.fontset":'stix',
}
rcParams.update(config)

plt.xlabel('Localization Error (m)',size = 18)#横坐标命名
plt.ylabel('CDF',size = 18)
# x=np.arange(0.2,3)
plt.axis([0.2,3,0,1])





#plt.plot(data0_1000,'b',label='Gyroscope data')
#plt.plot(data1007_2025,'b',label='Gyroscope data')
plt.plot(x_deepnavi,y_deepnavi,'b',label='DeepNavi',linestyle='-.',marker='o')
plt.plot(x_SVL,y_SVL,'y',label='SVL',linestyle='--',Marker='^')
plt.plot(x_L_SVL,y_L_SVL,'purple',label='L-SVL',linestyle='-',Marker='s')
plt.plot(x_VMag,y_VMag,'green',label='VMag',linestyle=':',Marker='v')
plt.plot(x_SEMIL,y_SEMIL,'r',label='VISEL',Marker='*')

#plt.gcf().set_facecolor(np.ones(3)*240/255)   #生成画布网格大小
plt.grid()  #生成网格
plt.legend(loc='lower right',fontsize=16)#标签显示位置和大小   upper, lower
plt.subplots_adjust(top=0.986, bottom=0.106, right=0.983, left=0.096, hspace=0, wspace=0)
plt.savefig("localization_A.eps", dpi = 500)
plt.show()

# markeredgecolor 或 mec 标记边缘颜色
# markeredgewidth 或 mew 标记边缘宽度
# markerfacecolor 或 mfc 标记面颜色
# markerfacecoloralt 或 mfcalt
# markersize 或 ms 标记大小