#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author:Frank

age = input("age(year)")
sex = input("性别：男/女")
height = input("height(m)")
weight = input("weight(kg)")
age = int(age)
height = float(height)
weight = float(weight)
bmi = weight/(height * height)
if bmi < 18.5:
	info = '你已经瘦成闪电，需要补充蛋白质'
elif bmi < 25:
	info = '祝贺你，体重正常'
elif bmi < 28:
	info = '稍微注意保持体形，减点肥就行。过重'
elif bmi < 32:
	info = '体重比较重，注意要减肥了。肥胖'
elif bmi >= 32:
	info = '对不起，你已经胖成球了。严重肥胖'
else:
	info = '你是外星人，你输入的数据不对。'
if age < 18:
	info = '少年' + info
elif age > 40:
	if sex == '男':
		info = '中年油腻大叔'+ info
	else:
		info = '大妈'+ info
else:
	if sex == '女':
		info = '啦啦啦，美少女.'+ info
	else:
		info = '小伙子。'+ info
print(bmi)
print(info)
