import matplotlib.pyplot as plt
import numpy as np
import csv

plt.figure(figsize=(8,8))
plt.title("Amount of Time Studied Compared to Grade on Exam")
plt.xlabel("Grade")
plt.ylabel("Time Studied")


with open(r'C:\Users\Joe\OneDrive\Desktop\PythonPrograms\Homework3\testscore.csv') as file_obj: 
    # Skips the heading 
    heading = next(file_obj) 
      
    reader_obj = csv.reader(file_obj) 
      
    gradeX = [] 
    hoursY = [] 

    for row in reader_obj: 
        #The dataset CSV file I used was very bad, so this is necessary
        format = row[0].split("                ")
        hoursY.append(format[0])
        gradeX.append(format[1])
    
    # If gradeX or hoursY contain strings, convert them to float
    gradeX = np.array(gradeX, dtype=float)
    hoursY = np.array(hoursY, dtype=float)

# Calculate the best-fit line
z = np.polyfit(gradeX, hoursY, 1)
p = np.poly1d(z)

plt.scatter(gradeX, hoursY, c="blue")
plt.plot(gradeX, p(gradeX), "b--")



plt.show()