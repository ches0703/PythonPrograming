import threading
import time


def SampleThread(name, max_count=10):
    count = 0
    my_name = name
    print("Thread_{} is activated".format(my_name))
    while True:
        print("Thread_{} is still running (count = {})\n".format(my_name, count), end="")
        count += 1
        if count > max_count:
            break
        time.sleep(1)
    print("Thread_{} is terminating".format(my_name))


def main():
    thread_A = threading.Thread(target=SampleThread, kwargs={
                                "name": "A", "max_count": 10})
    thread_B = threading.Thread(target=SampleThread, kwargs={
                                "name": "B", "max_count": 10})
    thread_C = threading.Thread(target=SampleThread, kwargs={
                                "name": "C", "max_count": 10})

    threads = []
    threads.append(thread_A)
    threads.append(thread_B)
    threads.append(thread_C)

    for t in threads:
        print("Activating thread : {}".format(t.getName()))
        t.deamon = True
        t.start()
        t.join(timeout=1.0)
    while True:
        all_threads_terminated = True
        for t in threads:
            if t.is_alive():
                all_threads_terminated = False
        if all_threads_terminated is True:
            break
        else:
            num_active_threads = threading.active_count()
            active_threads = threading.enumerate()
            print("{} thread are active(include main)".format(num_active_threads))
            print(active_threads)
            time.sleep(1)
            continue
    print("main() : all thread are terminated now")


if __name__ == "__main__":
    main()
