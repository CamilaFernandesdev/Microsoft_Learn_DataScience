import pandas as pd

# Define an array of study hours
study_hours = [10.0,11.5,9.0,16.0,9.25,1.0,11.5,9.0,8.5,14.5,15.5,
               13.75,9.0,8.0,15.5,8.0,9.0,6.0,10.0,12.0,12.5,12.0]

# Create a 2D array (an array of arrays)
student_data = np.array([study_hours, grades])

# display the array
student_data

# Get the mean value of each sub-array
avg_study = student_data[0].mean()
avg_grade = student_data[1].mean()

#print('Average study hours: {:.2f}\nAverage grade: {:.2f}'.format(avg_study, avg_grade))

df_students = pd.DataFrame({'Name': ['Dan', 'Joann', 'Pedro', 'Rosie', 'Ethan', 'Vicky', 'Frederic', 'Jimmie', 
                                     'Rhonda', 'Giovanni', 'Francesca', 'Rajab', 'Naiyana', 'Kian', 'Jenny',
                                     'Jakeem','Helena','Ismat','Anila','Skye','Daniel','Aisha'],
                            'StudyHours':student_data[0],
                            'Grade':student_data[1]})

#----------------------------------------------------------------------------------------------------------------
#Missing datas
df_students.isnull()
df_students.isnull().sum()
df_students[df_students.isnull().any(axis=1)]
df_students.StudyHours = df_students.StudyHours.fillna(df_students.StudyHours.mean())

#----------------------------------------------------------------------------------------------------------------
#drop rows or columns that contains null values by using the dropna method
df_students = df_students.dropna(axis=0, how='any')

#----------------------------------------------------------------------------------------------------------------
#Exploring datas in DataFrame
# Get the mean study hours using to column name as an index
mean_study = df_students['StudyHours'].mean()

# Get the mean grade using the column name as a property (just to make the point!)
mean_grade = df_students.Grade.mean()

# Print the mean study hours and mean grade
print('Average weekly study hours: {:.2f}\nAverage grade: {:.2f}'.format(mean_study, mean_grade))

# Get students who studied for the mean or more hours
df_students[df_students.StudyHours > mean_study]

# What was their mean grade?
df_students[df_students.StudyHours > mean_study].Grade.mean()

aproved_students  = pd.Series(df_students['Grade'] >= 60)
df_students = pd.concat([df_students, aproved_students.rename("Pass")], axis=1)

#----------------------------------------------------------------------------------------------------------------
print(df_students.groupby(df_students.Pass).Name.count())
print(df_students.groupby(df_students.Pass)['StudyHours', 'Grade'].mean())
#----------------------------------------------------------------------------------------------------------------

# Create a DataFrame with the data sorted by Grade (descending)
df_students = df_students.sort_values('Grade', ascending=False)
