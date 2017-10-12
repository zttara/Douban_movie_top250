#-*-coding:utf-8-*- 
import sys  
reload(sys)  
sys.setdefaultencoding('utf8') 

import numpy as np
import pandas as pd
from pandas import DataFrame,Series

from bs4 import BeautifulSoup
from urllib2 import urlopen

import re

#正则表达式分割字符串
def func_split(string,pattern):  
    return re.split(pattern,string)

def trans_list(main_list,sub_list):
    index = main_list.index(sub_list)
    sub_list.reverse()  #反转list的排列
    for ele in sub_list:
        main_list.insert(index,ele)  #后一元素插入在前一元素之前
    main_list.pop(main_list.index(sub_list))
    return main_list

def extract_info(li_tag):
    info = []
    for string in li_tag.stripped_strings:
        info.append(string) 

    if '[可播放]' in info:
        index = info.index('[可播放]')
        info.pop(index)  #pop() 函数用于移除列表中的一个元素（默认最后一个元素），并且返回该元素的值
    class_hd = li_tag.find('div',{'class':'hd'})
    if len(class_hd.a.find_all('span')) == 2:
        if '  /  ' in info[2]:
            info.insert(2,np.NaN)  #缺失则插入NaN
            info[3] = info[3][2:]
        else:
            info[2] = info[2][2:]
            info.insert(3,np.NaN)
    else:       
        info[2] = info[2][2:]  #电影中文名,\xa0表示16进制下A0的一个数，为一个字符
        info[3] = info[3][2:]  #电影外文名
    Dir_and_Act = func_split(info[4],r':|\xa0\xa0\xa0')  #分割字符串：导演、主演
        
    if len(Dir_and_Act) == 3:#分割后列表里不含‘主演名字’的情况
        Dir_and_Act.append('NaN')
    elif len(Dir_and_Act) == 2:#分割后列表里只含‘导演’和‘导演名字’的情况
        Dir_and_Act.append('NaN')
        Dir_and_Act.append('NaN')
    Yea_Cou_Gen = func_split(info[5],r'\xa0/\xa0')
    info[4] = Dir_and_Act
    info[5] = Yea_Cou_Gen
    info = trans_list(info,Dir_and_Act)
    info = trans_list(info,Yea_Cou_Gen)
    info.pop(4)  #删除列表中的‘导演’项
    info.pop(5)  #删除列表中的'演员'项
    
    return info  #返回一行movie的数据，list的形式

def collecting_data(url,database):

    soup = BeautifulSoup(urlopen(url),'lxml')
    movie_grid = soup.find_all('ol',{'class':'grid_view'})  #找到电影表单
    movie = movie_grid[0].find_all('li')
    for li in movie:
        database.append(extract_info(li))  #data为list前提下，DataFrame([data])为行排列，DataFrame(data)为列排列
    return database  #database=[[],[],[],....]



def collect_all(url):
    database=[]
    collecting_data(url,database)
    data=pd.DataFrame(database)
    return data  #返回一行数据

def main():
    page = []
    for sequence in list(range(0,250,25)):
        url = r'https://movie.douban.com/top250?start=%d&filter=' %sequence  #所有的网页地址
        page.append(collect_all(url))  #添加爬取的相关数据

    GeneralData = pd.DataFrame()
    for i in range(len(page)):
        GeneralData = pd.concat([GeneralData,page[i]],ignore_index = True)  #pd.concat:[]内要为DataFrame形式

    #保存数据为csv
    #GeneralData = GeneralData.drop(0,axis=1) 
    column = ['排名','电影中文名','电影外文名','电影别名','导演','演员','年份','地区','类别','评分','评分人数','电影概况']
    GeneralData.columns = column
    #GeneralData.to_csv('MovieTop250.csv',encoding='utf-8')  #此函数默认解码方式为utf-8，但是在保存时不加encoding的话，读取会产生错误
    GeneralData.to_csv('E:/Movie.csv')

if __name__ == '__main__':
    main()