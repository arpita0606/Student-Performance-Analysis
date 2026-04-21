# Student-Performance-Analysis
Student Performance Analysis
📌 Project Overview
This project analyzes student academic performance using SQL, Python, and Excel.
The goal is to extract meaningful insights from student data to help improve learning outcomes and teaching strategies.

🎯 Objectives
Identify top-performing students
Compare performance across departments
Detect students at risk (low marks)
Analyze the impact of attendance on performance

📁 Dataset
The dataset contains the following fields:
student_id – Unique ID of student
name – Student name
department – Department (CS / IT)
math – Marks in Mathematics
science – Marks in Science
programming – Marks in Programming
attendance – Attendance percentage

Tools & Technologies
Python (Pandas) – Data analysis
SQL (MySQL/Oracle) – Data querying
Excel – Data visualization and pivot tables
🔍 Analysis Performed
Python
Loaded dataset using Pandas
Created average_marks column
Identified top-performing student
Calculated department-wise averages
Analyzed relationship between attendance and marks
SQL
Displayed all student records
Calculated average marks
Identified top-performing student
Computed department-wise performance
Detected students scoring below 60
Calculated overall class average
Excel
Created Average Marks column
Sorted students by performance
Applied conditional formatting (marks < 60)
Created Pivot Table (Department vs Average Marks)
Generated charts:
Bar chart → Student performance
Column chart → Department comparison
Scatter plot → Attendance vs marks

Key Insights
Pooja is the top-performing student
IT department performs better than CS
Students with higher attendance generally score higher
Rahul is at risk due to low marks

📂 Files Included
students.csv – Dataset
analysis.py – Python code
Excel file – Analysis and charts
SQL queries – Database analysis
Project Report – Documentation
How to Run
Install required library:
pip install pandas
Run Python file:
python analysis.py

🔮 Future Improvements
Use larger datasets
Add more subjects
Build interactive dashboards (Power BI/Tableau)
Apply machine learning for prediction

Conclusion
This project demonstrates how student data can be analyzed to identify trends, improve academic performance, and support better decision-making in educational institutions.
