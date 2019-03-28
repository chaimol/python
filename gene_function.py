#!/bin/bash

#此脚本是实现玉米V4版本基因的功能注释
#gene_function.txt是对应的注释库文件
#out.csv是需要添加注释的文件
#输出文件为
#@author:chaimol@163.com

import pandas as pd
df1=pd.read_csv('gene_function.csv',encoding='utf-8)
df2=pd.read_csv('out.csv',encoding='utf-8')


#匹配相同内容的行，匹配到之后返回匹配到的行，未匹配到则不返回
index=df1['geneid'].isin(df2['geneid'])
outfile=df1[index]
outfile.to_csv('outfile.csv',index=False,encoding='utf-8')



#匹配相同内容的行，匹配到之后添加内容到右侧文件。为匹配到返回的是NA。
outer=pd.merge(df1,df2,how='right')
outer.to_csv('outer_function.csv',index=False,encoding='utf-8')