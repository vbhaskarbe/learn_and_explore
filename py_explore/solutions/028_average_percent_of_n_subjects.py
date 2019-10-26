#
## 28. Total average and Percentage of ’N’ Subjects
#

subjects      = int( input("Enter number of subjects: "))
subjects_marks = []
subjects_total = 0
for subject in range(0, subjects):
    subjects_marks.append(int( input("Enter marks for Subject %d: " % (subject + 1))))

for index, marks in enumerate( subjects_marks):
    subjects_total += marks

print("Total subject count is         :", subjects)
print("The marks in those subjects are:", subjects_marks)
print("The sum of the all marks is    :", subjects_total)
print("The average of the marks is    :", subjects_total / subjects)
print("The percentage of the marks is :",( ((subjects_total / (subjects * 100)) * 100)))


