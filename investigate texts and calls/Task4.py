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
任务4:
电话公司希望辨认出可能正在用于进行电话推销的电话号码。
找出所有可能的电话推销员:
这样的电话总是向其他人拨出电话，
但从来不发短信、接收短信或是收到来电


请输出如下内容
"These numbers could be telemarketers: "
<list of numbers>
电话号码不能重复，每行打印一条，按字典顺序排序后输出。
"""

#text_numbers
text_numbers = set()
for text in texts:
	text_numbers.add(text[0])
	text_numbers.add(text[1])

#caller_numbers and called_numbers
caller_numbers = set()
called_numbers = set()
for call in calls:
	caller_numbers.add(call[0])
	called_numbers.add(call[1])

#check market_numbers
market_numbers = set()
for number in caller_numbers:
	if (number not in text_numbers) and (number not in called_numbers):
		market_numbers.add(number)

#creart the list of market numbers
list_of_numbers =[]
while min(market_numbers, default=0):
	list_of_numbers.append(min(market_numbers))
	market_numbers.remove(min(market_numbers))

#print result
print("These numbers could be telemarketers: ")
for number in list_of_numbers:
	print(number)
