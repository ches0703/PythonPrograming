# 2022-2 컴사파 Exam1A
# 21912070 최은성
from MyList import *

# Main Part--------------------------------------
if __name__ == "__main__":
    print("2022-2 컴사파Exam1A 학번: 21912070, 성명: 최은성")
    L_float = get_float_List()
    print("list of input data : ", L_float)
    L_len, L_min, L_max, L_avg, L_var, L_std = get_statistics(L_float)
    print("L_len = {}, L_min = {}, L_max = {}, L_avg = {:.2f}, L_var = {:.2f}, L_std = {:.2f}"
          .format(L_len, L_min, L_max, L_avg, L_var, L_std))
    L_sorted = sort_list(L_float)
    print("sorted list : ", L_sorted)
