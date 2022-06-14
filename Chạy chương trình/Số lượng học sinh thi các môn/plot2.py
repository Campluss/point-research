import csv
file = open("clearDT1.csv" ,encoding ='utf8', mode ="r")

data = file.read().split("\n")

header = data[0]
students = data[1:]

students.pop()

total_student = len(students)

header = header.split(",")
subject =header[5:]

for i in range(len(students)):
	students[i] = students[i].split(",")


#number of students who took
num_of_exam_taken = [0,0,0,0,0,0,0,0,0,0,]

for s in students:
	count = 0;
	for i in range(9):
		if s[i+5] != "-1":
			count += 1

	num_of_exam_taken[count] += 1


# import matplotlib.pyplot as plt

# # Pie chart, where the slices will be ordered and plotted counter-clockwise:
# labels = '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'
# sizes = [0, 80, 122, 2605, 4496, 2879, 64261, 0, 0, 1]
# #explode = (0, 0.1, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs') phồng to ở môn học đó

# fig1, ax1 = plt.subplots()
# ax1.pie(sizes, labels=labels, autopct='%1.1f%%', startangle = 90)#autopct(thêm kí hiệu %) #startangle=90(bắt đầu chạy ở góc 90 độ hay ở 12 giờ) #shadow=True(tạo bóng ở dưới)
# ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

# plt.show()
import numpy as np
import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(6, 3), subplot_kw=dict(aspect="equal"))

recipe = ["0", "1", "2", "3", "4", "5", "6","7", "8", "9"]

data = [float(x.split()[0]) for x in recipe]
ingredients = [x.split()[-1] for x in recipe]


def func(pct, allvals):
    absolute = int(pct/100.*np.sum(allvals))
    return "{:.1f}%\n({:d} môn)".format(pct, absolute)



wedges, texts, autotexts = ax.pie(data, autopct=lambda pct: func(pct, data),
                                  textprops=dict(color="w"))

ax.legend(wedges, ingredients,
          title="Ingredients",
          loc="center left",
          bbox_to_anchor=(1, 0, 0.5, 1))

plt.setp(autotexts, size=8, weight="bold")

ax.set_title("Số lượng học sinh thi các môn")

plt.show()