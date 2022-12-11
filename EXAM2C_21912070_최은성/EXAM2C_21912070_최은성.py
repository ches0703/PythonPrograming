# EXAM2C_21912070_최은성.py
"""
Project : EXAM2C 
Author: Eun-seong Choi
Date of last update: 2022 / 12 / 11
Update list:
    - v1.1 : 12 / 11
        Make file read part 
        Make print list : acording dimen
        Make array : A, B
            Add calc part : det_A, Inv_A, X
            Use the matmul() : B1, X1
"""
import numpy as np

def printArray(arr):

    if np.ndim(arr) == 1:   # Case : 1 dimensional array
        for i in range(len(arr)):
            print(arr[i], end="")
        print()

    elif np.ndim(arr) == 2:
        shpae = np.shape(arr)  # Case : 2 dimensional array
        row = shpae[0]
        col = shpae[1]
        for i in range(row):
            for j in range(col):
                print(arr[i][j], end="")
            print()
    
    else :  # Else Case
        print(arr)



def fgetArray(fin_name):
    fin = open(fin_name, "r")
    row, col = map(int, fin.readline().split())
    Mtrx_array = []
    if row == 1:    # Case : 1 dimensional array
        Mtrx_array.extend(list(map(float, fin.readline().split())))
    else:
        for i in range(row):  # Redline() * n(row)
            # Save to List's List
            Mtrx_array.append(list(map(float, fin.readline().split())))

    return Mtrx_array


def main(): 
    print("2022-2 컴사파 Exam2C 학번: 21912070, 이름: 최은성") 
    mA = fgetArray("fA.txt") 
    mB = fgetArray("fB.txt") 
    print("mA = "); printArray(mA) 
    print("mB = "); printArray(mB)
    
    A = np.array(mA)
    B = np.array(mB)

    print("A = \n", A)
    print("B = \n", B)  

    # - 배열 A의 행렬식 (det_A) 계산 및 출력
    Det_A = np.linalg.det(A)
    print("Det_A = \n", Det_A)

    # - 배열 A의 역행렬 (inv_A) 계산 및 출력
    Inv_A = np.linalg.inv(A)
    print("Inv_A = \n", Inv_A)

    # Numpy의 solve() 함수를 사용하여 선형 시스템 AㆍX = B의 해 X를 산출
    X = np.linalg.solve(A, B)
    print("X = \n", X)  

    # Numpy의 matmul() 함수를 사용하여 B1 = AㆍX를 계산
    # 파일 fB.txt에서 설정된 값과 계산된 B1를 비교하여 볼 것
    B1 = np.matmul(A, X)
    print("B1 = A * X = \n", B1)  


if __name__ == "__main__": 
    main()