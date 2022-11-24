# myhashMap.py
# Homework 11.2 Application of HashMap for Student Records
"""
Project : myhashMap
Author: Eun-seong Choi
Date of last update: 2022 / 11 / 24
Update list:
    - v1.1 : 11 / 24
        Refer to lecture materials : basical bucket hash map
        Fix : Parameter name, _getitem add print 
"""


class Entry:
    def __init__(self, k, v):
        self._key = k
        self._value = v

    def __str__(self):
        return str(self._value)

    def CyclicShiftHashCode(str_key):  # str_key is string
        mask = (1 << 32) - 1  # limit to 32-bit integers
        h = 0
        for ch in str_key:
            h = (h << 5 & mask) | (h >> 27)  # cyclic shift hash code
            h += ord(ch)
        return h


def CyclicShiftHashCode(str_key):  # str_key is string
    mask = (1 << 32) - 1  # limit to 32-bit integers
    h = 0
    for ch in str_key:
        h = (h << 5 & mask) | (h >> 27)  # cyclic shift hash code
        h += ord(ch)
    return h


class Bucket(Entry):
    def __init__(self):
        self._bucket = []  # implement bucket using list

    def _getitem(self, k):
        for item in self._bucket:
            if k == item._key:
                return item._value
        return None

    def _setitem(self, k, v):
        for item in self._bucket:
            if k == item._key:
                item._value = v
                return
        self._bucket.append(Entry(k, v))

    def _delitem(self, k):
        for j in range(len(self._bucket)):
            if k == self._bucket[j]._key:
                self._bucket.pop(j)
                return 1
        return None

    def __len__(self):
        return len(self._bucket)

    def __iter__(self):  # provides iterator as generator function
        for item in self._bucket:
            yield item._key


class HashMap(Bucket):
    def __init__(self, capacity=11, prm=109345121):
        self._hash_tbl = capacity * [None]
        self._hash_tbl_size = capacity
        self._num_entry = 0
        self._prime = prm

    def _hash_value(self, k):
        return CyclicShiftHashCode(k) % self._prime % self._hash_tbl_size

    def __len__(self):
        return self._num_entry

    def _getitem(self, k):
        hv = self._hash_value(k)
        bucket = self._hash_tbl[hv]
        print("key({}) => hash_tbl[{}]".format(k, hv))
        return bucket._getitem(k)

    def _setitem(self, k, v):
        hv = self._hash_value(k)
        if self._hash_tbl[hv] is None:
            self._hash_tbl[hv] = Bucket()
        bucket = self._hash_tbl[hv]
        bucket._setitem(k, v)

    def _delitem(self, k):
        hv = self._hash_value(k)
        bucket = self._hash_tbl[hv]
        bucket._delitem(k)
        self._num_entry -= 1

    def __str__(self):
        s = ''
        for h in range(len(self._hash_tbl)):
            bucket = self._hash_tbl[h]
            if bucket is not None:
                s += "bucket[{:2d}] : ".format(h)
                for item in bucket:
                    s += str(item) + ", "
                s += "\n "
        return s
