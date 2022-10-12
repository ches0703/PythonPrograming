import time
import calendar
t1 = time.time()
print(t1)
print(time.gmtime())
print(time.localtime())
print(time.perf_counter_ns())
time.sleep(1)
print(time.perf_counter_ns())

print(calendar.prcal(2022))