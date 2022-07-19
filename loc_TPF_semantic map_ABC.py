from cProfile import label
from scipy import signal
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pylab import *
from matplotlib import rcParams

from pandas import DataFrame,Series
#file = open('C:/Users/Administrator/Desktop/语义定位手稿/gyr_synthetic_tran-2.txt')
# x_SEMIL=[0,0.5,1,1.5,2]
# y_SEMIL = [0,0.6786,0.896,0.9296,0.9575]
# y_SEMIL_TPF= [0,0.629,0.816,0.878,0.927]
# y_SEMIL_without_semantic_map =[0,0.652,0.7986,0.862,0.936]
#
#
# # for line in file:
# #     if line != "\n":
# #         data.append(line)
# # print(len(data))
# #data = file.readlines()
# #画图
# #figure(figsize=(16,8),dpi=200)
# rcParams['font.sans-serif']=['SimHei'] #显示中文字符
# rcParams['axes.unicode_minus'] = False
#
# x = list(range(len(x_SEMIL))) #数据在X轴的位置
# width =0.1 #定义柱状图的宽度
#
# plt.xlabel('Localization Error (m)',size = 18)#横坐标命名
# plt.ylabel('CDF',size = 18)
# # x=np.arange(0.2,3)
#
# #plt.axis([0.3,2.5,0,1])
# #plt.locator_params(axis='x',nbins = 5) #定义X轴刻度的个数
#
#
#
# plt.bar(x_SEMIL,y_SEMIL_TPF,width=width,color='blue',label='SEMIL_TPF') #第一个柱状图
#
# #定义第二个柱状图的偏移一个柱的宽度
# for i in range(len(x)):
#     x_SEMIL = x_SEMIL + width
#     #x[i] = x[i]+width
#
#
#
# plt.bar(x_SEMIL,y_SEMIL_without_semantic_map,width=width,color='green',label='SEMIL_Floor Map')
#
# plt.bar(x_SEMIL,y_SEMIL,width=width,color='r',label='SEMIL')

n_groups = 4

y_SEMIL_TPF = (0.629, 0.816, 0.878, 0.927) #sa

y_SEMIL_without_semantic_map = (0.652, 0.7986, 0.862, 0.936)  #ffd

y_SEMIL = (0.6786, 0.896, 0.9296, 0.9575)  #sabf

fig, ax = plt.subplots()

index = np.arange(n_groups)
bar_width = 0.15

opacity = 0.4
error_config = {'ecolor': '0.3'}

rects1 = ax.bar(index, y_SEMIL_TPF, bar_width,alpha=0.8,
                color='darkblue',
                error_kw=error_config,
                label='VISEL_TPF')

rects2 = ax.bar(index + bar_width, y_SEMIL_without_semantic_map, bar_width,alpha=0.8,
                color='darkgreen',
                error_kw=error_config,
                label='VISEL_Floor Map')

rects3 = ax.bar(index + bar_width + bar_width, y_SEMIL, bar_width,alpha=0.8,
                color='maroon',
                error_kw=error_config,
                label='VISEL')

#plt.axis([0.2,2,0,1])
ax.set_xticks(index + 3 * bar_width / 3)
ax.set_xticklabels(('0.5', '1', '1.5', '2'))  #X轴横坐标
ax.legend()


plt.xlabel('Localization Error (m)',size = 18)#横坐标命名
plt.ylabel('CDF',size = 18)







#plt.gcf().set_facecolor(np.ones(3)*240/255)   #生成画布网格大小
#plt.grid()  #生成网格
plt.legend(loc='upper left',fontsize=10.5)#标签显示位置和大小   upper, lower
plt.subplots_adjust(top=0.991, bottom=0.11, right=0.996, left=0.096, hspace=0, wspace=0)
plt.savefig("localization_TPF_semantic map.png", dpi = 500)
plt.show()

# markeredgecolor 或 mec 标记边缘颜色
# markeredgewidth 或 mew 标记边缘宽度
# markerfacecolor 或 mfc 标记面颜色
# markerfacecoloralt 或 mfcalt
# markersize 或 ms 标记大小