import pandas as pd
import matplotlib.pyplot as plt
import os

os.makedirs("images", exist_ok=True)

df = pd.DataFrame({
    "student": ["A", "B", "C", "D", "E", "F", "G", "H"],
    "class": ["Class 1", "Class 1", "Class 1", "Class 2", "Class 2", "Class 2", "Class 3", "Class 3"],
    "math": [90, 75, 60, 85, 70, 95, 55, 80],
    "english": [85, 80, 65, 90, 75, 88, 60, 78],
    "science": [92, 70, 68, 88, 72, 94, 58, 82]
})
score_cols = ['math', 'english', 'science']

df['avg_score'] = df[score_cols].mean(axis=1).round(2)
top_students = df.nlargest(3, 'avg_score')[['student', 'class', 'avg_score']] 
class_score_avg = df.groupby('class')['avg_score'].mean().round(2)
subject_score_avg = df[score_cols].mean().round(2)

print('\nAverage score by subject')
print(subject_score_avg)

print('\nAverage score by class')
print(class_score_avg)

print('\nTop 3 students')
print(top_students)

plt.figure()
plt.bar(subject_score_avg.index, subject_score_avg.values, width = 0.5)
plt.ylim(70, 80)
plt.title('Average by Subject')
plt.xlabel('Subject')
plt.ylabel('Average')
plt.savefig('images/subject_average.png', bbox_inches='tight')
plt.close()

plt.figure()
plt.bar(class_score_avg.index, class_score_avg.values, width = 0.5)
plt.ylim(60, 90)
plt.title('Average by Class')
plt.xlabel('Class')
plt.ylabel('Average')
plt.savefig('images/class_average.png', bbox_inches='tight')
plt.close()