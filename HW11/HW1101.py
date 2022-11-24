# HW1101.py
# Homework 11.2 Application of HashMap for Student Records
"""
Project : Application of HashMap for Student Records
Author: Eun-seong Choi
Date of last update: 2022 / 11 / 24
Update list:
    - v1.1 : 11 / 24
        Make myHashMap.py
        add main funtion
        Fix in main funtion v == None -> v is None
"""
import myHashMap

if __name__ == "__main__":
    HashMap_Capacity = 7
    print("Creating a HashMap of capacity ({})".format(HashMap_Capacity))
    # Make Hashmap
    hsMap = myHashMap.HashMap(capacity=HashMap_Capacity)

    # elememts
    Entries = [("Kim", 19345, "ICE", 4.0), ("Park", 18234, "CS", 4.2),
               ("Hong", 20456, "EE", 3.9), ("Lee", 20987, "ME", 3.8),
               ("Yoon", 21654, "ICE", 3.7), ("Moon", 21001, "CHEM", 4.1),
               ("Hwang", 21123, "CE", 3.7), ("Choi", 19003, "EE", 4.3),
               ("Yeo", 20234, "ME", 3.8), ("Jeong", 18005, "PH", 4.3)]

    # init Hashamap
    for i in range(len(Entries)):
        entry = Entries[i]
        key = entry[0]
        hsMap._setitem(key, entry)
        print("Entry[{:2}] : {}".format(i, Entries[i]))

    # print Hash bucket
    print("Current HashMap Internal Structure:\n", hsMap)

    # search area : each element's index
    print("Checking entry searching in HashMap")
    while True:
        key = input("Input student name to search (. to quit) : ")
        if key == '.':
            break
        v = hsMap._getitem(key)
        if v is None:
            print("key ({}) is not found in hashmap !!".format(key))
        else:
            print("key ({}) : Value ({})".format(key, v))
