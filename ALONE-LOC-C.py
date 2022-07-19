from cProfile import label
from scipy import signal
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pylab import *
from pandas import DataFrame,Series
#file = open('C:/Users/Administrator/Desktop/语义定位手稿/gyr_synthetic_tran-2.txt')
x_image=[0,0.5,1,1.5,2,2.5,3]
y_image=[0,0.526,0.712,0.776,0.869,0.928,0.962]
x_magnetic=[0,0.5,1,1.5,2,2.5,3]
y_magnetic= [0,0.32,0.48,0.646,0.73,0.82,0.87]
x_SEMIL=[0,0.5,1,1.5,2,2.5,3]
y_SEMIL = [0,0.712,0.875,0.901,0.936,0.965,0.982]

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
#plt.axis([0.2,3,0,1])
plt.xlim([0.3,3])
plt.ylim([0,1])

#plt.plot(data0_1000,'b',label='Gyroscope data')
#plt.plot(data1007_2025,'b',label='Gyroscope data')
plt.plot(x_image,y_image,'b',label='VISEL_Image',linestyle='-.',marker='o')
plt.plot(x_magnetic,y_magnetic,'y',label='VISEL_Magnetic',linestyle='--',Marker='^')
# plt.plot(x_L_SVL,y_L_SVL,'purple',label='L-SVL',linestyle='-',Marker='s')
# plt.plot(x_VMag,y_VMag,'green',label='VMag',linestyle=':',Marker='v')
plt.plot(x_SEMIL,y_SEMIL,'r',label='VISEL',Marker='*')

#plt.gcf().set_facecolor(np.ones(3)*240/255)   #生成画布网格大小
plt.grid()  #生成网格
plt.legend(loc='lower right',fontsize=16)#标签显示位置和大小   upper, lower
plt.subplots_adjust(top=0.986, bottom=0.106, right=0.985, left=0.096, hspace=0, wspace=0)
plt.savefig("localization_C_alone.png", dpi = 500)
plt.show()

# markeredgecolor 或 mec 标记边缘颜色
# markeredgewidth 或 mew 标记边缘宽度
# markerfacecolor 或 mfc 标记面颜色
# markerfacecoloralt 或 mfcalt
# markersize 或 ms 标记大小