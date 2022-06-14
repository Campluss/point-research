#read file
with open("clearDT.csv", encoding ="utf8") as file:
	data = file.read().split("\n")
#lam so hoc sinh khong tham gia thi
header = data[0]
students = data[1:]

#remove last student (empty student)
students.pop()

total_student = len(students)

#split header
header = header.split(",")
subject = header[5:]

#split each student in list
for i in range(len(students)):
	students[i] = students[i].split(",")

#sbd
# print(students[0][0])

note_take_exam = [0,0,0,0,0,0,0,0,0,0,0] #11 mon hoc

#loop through all students : loc qua cac hoc sinh
for s in students:
	#iterate through all subject : loc qua cac mon hoc
	for i in range(5,16):
		if s[i] == "-1":
			note_take_exam[i-5] += 1

#percentage :phan tram
note_take_exam_percentage = [0,0,0,0,0,0,0,0,0,0,0]

for i in range(0,11):
	note_take_exam_percentage[i] = round(note_take_exam[i]*100/total_student,2)#round la lay bao nhieu so thap phan

print(note_take_exam_percentage)
print(subject)
print(note_take_exam)

import matplotlib.pyplot as plt

import numpy as np

figure, axis = plt.subplots()

#list from 0-11
y_pos = np.arange(len(subject))

#plot the barchar using 2 list
plt.bar(y_pos, note_take_exam_percentage, align='center') #alpha=0.5 do trong suot hon
plt.xticks(y_pos,subject)

axis.set_ylim(0, 100)
plt.ylabel('Percentage')
plt.title('Số học sinh bỏ thi hoặc không đăng kí thi')

#make some lables
rects = axis.patches
for rect, note_take_exam in zip(rects, note_take_exam):
    height = rect.get_height()
    axis.text(rect.get_x() + rect.get_width() / 2, height + 5, note_take_exam, ha="center", va="bottom" )


plt.show()
