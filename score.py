#-*-coding:utf-8-*- 
import pandas as pd
import matplotlib.pyplot as plt
from pylab import mpl

mpl.rcParams['font.sans-serif'] = ['SimHei']

df = pd.read_csv('E:/project/spider/Movie.csv',encoding = 'utf8')
data = df[u'评分']
bins = [8.0,8.5,9.0,9.5,10]  #分区(0,8],(8,8.5]....
sub_reg = pd.cut(data,bins=bins)
sub_cnt = sub_reg.value_counts()  #统计区间个数
sub_pct = sub_cnt/sub_cnt.sum()*100  #计算百分比
#rat_arr_pct = np.array(rat_pct)#将series格式转成array，为了避免pie中出现name
plt.figure(figsize=(5,5))
plt.title(u'电影评分分布情况',fontsize=16)
plt.pie(sub_pct,labels = sub_pct.index,colors = ['fuchsia','orange','limegreen','cornflowerblue'],autopct = '%.2f%%',startangle = 90,explode = [0.05]*4)  #autopct属性显示百分比的值
plt.show()