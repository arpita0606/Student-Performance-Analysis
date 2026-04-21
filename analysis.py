import pandas as pd

print("Program Started\n")

# 1. Load dataset
df = pd.read_csv("students.csv")

# 2. Create average_marks column
df['average_marks'] = df[['math','science','programming']].mean(axis=1)

# 3. Identify top-performing student
top_student = df.loc[df['average_marks'].idxmax()]

# 4. Group by department
grouped = df.groupby('department')

# 5. Department-wise average
dept_avg = grouped['average_marks'].mean()

# 6. Attendance vs marks relationship
correlation = df['attendance'].corr(df['average_marks'])

# OUTPUTS
print("===== FULL DATA =====")
print(df)

print("\n===== TOP STUDENT =====")
print(top_student)

print("\n===== DEPARTMENT AVERAGE =====")
print(dept_avg)

print("\n===== ATTENDANCE vs MARKS =====")
print("Correlation:", correlation)