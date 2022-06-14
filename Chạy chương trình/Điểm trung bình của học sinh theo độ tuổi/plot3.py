with open("clearDT1.csv", encoding = 'utf8', mode = 'r') as file:
	data = file.read().split("\n")

header = data[0]
students = data[1:]

students.pop()

total_student = len(students)

header = header.split(",")
subject =header[5:]

for i in range(len(students)):
	students[i] = students[i].split(",") 

#lay so hoc sinh theo do tuoi
num_of_student_age_gr = [0,0,0,0,0,0,0,0,0,0,0]
num_age = [0,0,0,0,0,0,0,0,0,0,'>=27']
average_of_student_age_gr = [0,0,0,0,0,0,0,0,0,0,0]

for s in students:
	age = 2020 -int(s[4])
	if(age >= 27):
		age = 27
	num_of_student_age_gr[age - 17] += 1

	sum_score = 0
	cout_socre = 0
	for i in range(9):
		if s[i+5] != "-1":
			cout_socre +=1
			sum_score += float(s[i+5])

	average = sum_score/cout_socre
	average_of_student_age_gr[age - 17] += average



for i in range(10):
	num_age[i] = i + 17

print(num_of_student_age_gr)
print(average_of_student_age_gr)

average_of_tb = [0,0,0,0,0,0,0,0,0,0,0]
for i in range(11):
	average_of_tb[i] = round(average_of_student_age_gr[i]/num_of_student_age_gr[i],2)

print(average_of_tb)
for i in range(11):
	average_of_tb[i] = average_of_tb[i] * 8000

print(average_of_tb)

import matplotlib.pyplot as plt

import numpy as np

figure, axis = plt.subplots()

#list from 0-11
x_pos = np.arange(len(num_of_student_age_gr))
y_pos = np.arange(len(num_of_student_age_gr))

#plot the barchar using 2 list
plt.bar(x_pos, num_of_student_age_gr, align='center') #alpha=0.5 do trong suot hon
plt.plot(x_pos, average_of_tb, color = "red", marker ='o')
plt.xticks(x_pos,num_age)

axis.set_ylim(0, 80000)
plt.ylabel('Số học sinh')

ax2 = axis.twinx()
ax2.set_ylim(0, 10)
ax2.tick_params('y', colors = 'red')
plt.ylabel('So diem TB')

plt.title('Điểm trung bình của học sinh thi theo độ tuổi')

#make some lables
rects = axis.patches
for rect, num_of_student_age_gr in zip(rects, num_of_student_age_gr):
    height = rect.get_height()
    axis.text(rect.get_x() + rect.get_width() / 2, height + 5, num_of_student_age_gr, ha="center", va="bottom" )


plt.show()