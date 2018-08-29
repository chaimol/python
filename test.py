#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# name = input('Please input your name and I will output your name:')
# s1 = input('input youer last year score')
# s2 = input('input your score of this year')
# s1=float(s1)
# s2=float(s2)
# t=(s2-s1)/s1*100
# print(t)
# if t>0:
# 	print('祝贺呀%s,%1s%%'%(name,t))
# else:
# 	print('hello,%s同学成绩降低了%1s%%'%(name,t))

# tx = ('name','sex','age',['show','hiddden'])
# tx[3][0]='hide'
# tx[3][1]='show'
# print(tx)



# for line in open("sequence/11037.fa"):
# 	print(line)


aDict = {}
for line in open('sequence/11037.fa'):
	if line[0] == '>':
		key = line.strip() #strip移除行首尾的指定字符，默认是空格。

		print(key)
		aDict[key] = []
	else:
		aDict[key].append(line.strip())

#-----------------------------------------
#for key,valueL in aDict.items():
	#print(key)
	#print ".join(valueL)"

	
	
	
	
###	读取excel文件
# import xlrd
# from datetime import date,datetime
# def read_excel():
# #文件位置
# ExcelFile=xlrd.open_workbook(r'E:\gene\gene_id.xlsx')
# #获取目标excel文件sheet名
# print ExcelFile.sheet_names()


# #指定读取某个sheet表，例如读取sheet2
# #sheet2_name=ExcelFile.sheet_names()[1]


# #获取sheet内容【1根据sheet索引 2根据sheet名称】
# sheet=ExcelFile.sheet_by_index(1)
# #sheet=ExcelFile.sheet_by_name('需要做荧光定量的基因')
# #打印sheet的名称。行数，列数
# print sheet.name,sheet.narrows,sheet.ncols

# -*- coding: utf-8 -*-
#导入xlwt模块
import xlwt
# 创建一个Workbook对象，这就相当于创建了一个Excel文件
book = xlwt.Workbook(encoding='utf-8', style_compression=0)
'''
Workbook类初始化时有encoding和style_compression参数
encoding:设置字符编码，一般要这样设置：w = Workbook(encoding='utf-8')，就可以在excel中输出中文了。
默认是ascii。当然要记得在文件头部添加：
#!/usr/bin/env python
# -*- coding: utf-8 -*-
style_compression:表示是否压缩，不常用。
'''
#创建一个sheet对象，一个sheet对象对应Excel文件中的一张表格。
# 在电脑桌面右键新建一个Excel文件，其中就包含sheet1，sheet2，sheet3三张表
sheet = book.add_sheet('test', cell_overwrite_ok=True)
# 其中的test是这张表的名字,cell_overwrite_ok，表示是否可以覆盖单元格，其实是Worksheet实例化的一个参数，默认值是False
# 向表test中添加数据
sheet.write(0, 0, 'EnglishName')  # 其中的'0-行, 0-列'指定表中的单元，'EnglishName'是向该单元写入的内容
sheet.write(1, 0, 'Marcovaldo')
txt1 = '中文名字'
sheet.write(0, 1)  # 此处需要将中文字符串解码成unicode码，否则会报错txt1.decode('utf-8')
txt2 = '马可瓦多'
sheet.write(1, 1)  #, txt2.decode('utf-8')
 
# 最后，将以上操作保存到指定的Excel文件中
book.save(r'E:\test1.xls')  # 在字符串前加r，声明为raw字符串，这样就不会处理其中的转义了。否则，可能会报错















