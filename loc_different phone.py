from cProfile import label
from scipy import signal
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pylab import *
from pandas import DataFrame,Series
from matplotlib import rcParams

#file = open('C:/Users/Administrator/Desktop/语义定位手稿/gyr_synthetic_tran-2.txt')
x_SEMIL=[0.2,0.5, 1, 1.5, 2, 2.5, 3]

y_Xiaomi_6 = [0.43,0.672, 0.899, 0.932, 0.956, 0.979, 0.993]
y_Pixel_2 =  [0.41,0.665, 0.881, 0.926,  0.959, 0.9742,0.9856]
y_Pixel_3 =  [0.45,0.682, 0.908, 0.938, 0.965, 0.9771,0.9898]
y_Huawei_P30 = [0.426,0.681, 0.906, 0.945, 0.969, 0.985, 0.995]

# y_SEMIL = [0.6786, 0.896, 0.9296, 0.9575]
# y_SEMIL_TPF= [0.629, 0.816, 0.878, 0.927]
# y_SEMIL_without_semantic_map =[0.652, 0.7986, 0.862, 0.936]


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
plt.axis([0.3,3,0.6,1])
plt.locator_params(axis='x',nbins = 6) #定义X轴刻度的个数
plt.tick_params(labelsize=12)


#plt.plot(data0_1000,'b',label='Gyroscope data')
#plt.plot(data1007_2025,'b',label='Gyroscope data')

plt.plot(x_SEMIL,y_Xiaomi_6,'b',label='Xiaomi 6',linestyle='-.',linewidth=2.2, Marker = 'p',markerfacecolor='none', markersize= 10)
plt.plot(x_SEMIL,y_Pixel_2,'green',label='Pixel 2',linestyle='--',linewidth=2.2, Marker = 's',markerfacecolor='none',markersize= 10)
plt.plot(x_SEMIL,y_Pixel_3,'r',label='Pixel 3',linewidth=2.2,Marker='*',markerfacecolor='none',markersize= 10)
plt.plot(x_SEMIL,y_Huawei_P30,'y',label='Huawei P30',linewidth=2.2,Marker='^',markerfacecolor='none',markersize= 10)


# plt.plot(x_deepnavi,y_deepnavi,'b',label='DeepNavi',linestyle='-.',marker='o')
# plt.plot(x_SVL,y_SVL,'y',label='SVL',linestyle='--',Marker='^')
# plt.plot(x_L_SVL,y_L_SVL,'purple',label='L-SVL',linestyle='-',Marker='s')
# plt.plot(x_VMag,y_VMag,'green',label='VMag',linestyle=':',Marker='v')
# plt.plot(x_SEMIL,y_SEMIL,'r',label='SEMIL',Marker='*')

#plt.gcf().set_facecolor(np.ones(3)*240/255)   #生成画布网格大小
plt.grid()  #生成网格
plt.legend(loc='lower right',fontsize=16)#标签显示位置和大小   upper, lower
plt.subplots_adjust(top=0.986, bottom=0.106, right=0.978, left=0.121, hspace=0, wspace=0)
plt.savefig("localization_different phone.eps", dpi = 500)
plt.show()

# markeredgecolor 或 mec 标记边缘颜色
# markeredgewidth 或 mew 标记边缘宽度
# markerfacecolor 或 mfc 标记面颜色
# markerfacecoloralt 或 mfcalt
# markersize 或 ms 标记大小