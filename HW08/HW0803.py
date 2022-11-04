# HW0803.py
"""
Project : Data Analysis with Pandas & Excel
Author: Eun-seong Choi
Date of last update: 2022 / 11 / 04
Update list:
    - v1.1 : 10 / 18
        Get data part : Get data frame from input excel
        Print part : Plane student data frame, Avgs's data frame,
                     Student data frame with avg data added
        Calc part : Each student avg without st_id,
                    Sorting student data frame by Avg
                    each class's avg
        Save part : Save student data frame to Excel
"""
import pandas as pd

# File Relative Path
input_file_path = "InputExcel.xlsx"
output_file_path = "processed_scores.xlsx"

# Get data frame from input excel
student_data_frame = pd.read_excel(input_file_path)

# Print Plane student data frame
print(student_data_frame)
print()

# To calc each student avg without st_id
# Select col to be Calc
temp_df = student_data_frame[["Kor", "Eng", "Math", "Sci"]]
avg_per_student = temp_df.mean(axis=1, numeric_only="None")  # Calc Avg
student_data_frame["Avg"] = avg_per_student  # Add from Studant data frame

# Sorting student data frame by Avg
student_data_frame = student_data_frame.sort_values(by="Avg", ascending=False)

# Calc each class's avg : Total Avg
avgs_per_class = student_data_frame.mean(
    axis=0, numeric_only="None")  # Calc Avg
del avgs_per_class["st_id"]  # Remove Useless data
student_data_frame.loc[len(student_data_frame)] = avgs_per_class
student_data_frame.loc[len(student_data_frame) - 1, "st_name"] = "Total Avg"  # Add Studant data frame

# Print Avgs's data frame
print("Avgs per class :")
print(avgs_per_class)
print()

# Print student data frame with avg data added
print(student_data_frame)
print()

# Save student data frame to Excel
with pd.ExcelWriter(output_file_path) as excel_writer:
    student_data_frame.to_excel(excel_writer, sheet_name="Student Records")
