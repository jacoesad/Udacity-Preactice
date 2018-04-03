"""
下面的文件将会从csv文件中读取读取短信与电话记录，
你将在以后的课程中了解更多有关读取文件的知识。
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
任务3:
(080)是班加罗尔的固定电话区号。
固定电话号码包含括号，
所以班加罗尔地区的电话号码的格式为(080)xxxxxxx。

第一部分: 找出被班加罗尔地区的固定电话所拨打的所有电话的区号和移动前缀（代号）。
 - 固定电话以括号内的区号开始。区号的长度不定，但总是以 0 打头。
 - 移动电话没有括号，但数字中间添加了
   一个空格，以增加可读性。一个移动电话的移动前缀指的是他的前四个
   数字，并且以7,8或9开头。
 - 电话促销员的号码没有括号或空格 , 但以140开头。

输出信息:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
代号不能重复，每行打印一条，按字典顺序排序后输出。

第二部分: 由班加罗尔固话打往班加罗尔的电话所占比例是多少？
换句话说，所有由（080）开头的号码拨出的通话中，
打往由（080）开头的号码所占的比例是多少？

输出信息:
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
注意：百分比应包含2位小数。
"""

#Part 1
#生成不重复的区号集合
set_of_codes = set()

for call in calls:
	if call[0][:5] == "(080)":
		#固定电话
		if call[1][0] == "(":
			set_of_codes.add(call[1][1:call[1].find(')')])
		#电话促销员
		elif call[1][:3] == "140":
			continue
		#移动电话
		else:
			set_of_codes.add(call[1][:4])

#排序并保存为列表
list_of_codes=[]

while min(set_of_codes, default=0):
	list_of_codes.append(min(set_of_codes))
	set_of_codes.remove(min(set_of_codes))

#输出结果
print("The numbers called by people in Bangalore have codes:")
for code in list_of_codes:
	print(code)

#Part 2
#所有由080的打出的电话的集合
dict_of_calls = []
#同时目的也是080的数量
local_count = 0

#生成数据
for call in calls:
	if call[0][:5] == "(080)":
		dict_of_calls.append(call)
		if call[1][:5] == "(080)":
			local_count += 1

#计算百分比
percentage = '%.2f'%(local_count/len(dict_of_calls)*100)

#输出结果
print("{} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.".format(percentage))