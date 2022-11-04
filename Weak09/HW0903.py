import pandas as pd

input_file_path = "Weak09/InputExcel.xlsx"
output_file_path = "Weak09/processed_scores.xlsx"

student_data_frame = pd.read_excel(input_file_path)

# To calc avg without st_id 
temp_df = student_data_frame[["Kor", "Eng", "Math", "Sci"]]
avg_per_student = temp_df.mean(axis=1, numeric_only="None")
student_data_frame["Avg"] = avg_per_student

avgs_per_class = student_data_frame.mean(axis=0, numeric_only="None")
del avgs_per_class["st_id"]
print("Avgs per class :")
print(avgs_per_class)
print()

student_data_frame = student_data_frame.sort_values(by="Avg", ascending=False)

student_data_frame.loc[len(student_data_frame)] = avgs_per_class
student_data_frame.loc[len(student_data_frame) - 1, "st_name"] = "Total Avg"
print(student_data_frame)
print()

with pd.ExcelWriter(output_file_path) as excel_writer:
    student_data_frame.to_excel(excel_writer, sheet_name="Student Records")
