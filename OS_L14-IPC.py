import os
import multiprocessing
import time


def printWithTime(str_1, start=0):
    str_1 = str(str_1)
    print(str(time.time() - start), end=" >> " + str_1 + "\n")


def getStrPIDandPPID():
    return str(os.getpid()) + " and parent PID is " + str(os.getppid())

def printUntil(limit, queue):
    run_start_time_P2 = queue.get()
    printWithTime("Now running printUntil function, the PID is " + getStrPIDandPPID(), run_start_time_P2)
    sum = 0
    for i in range(0, limit + 1):
        printWithTime(i, run_start_time_P2)
        sum += i
        time.sleep(1)
    queue.put(sum)

def main():
    run_start_time = time.time()
    queue = multiprocessing.Queue()
    queue.put(run_start_time)
    printWithTime("The main PID (current process) is " + getStrPIDandPPID())
    process = multiprocessing.Process(target=printUntil, args=(10,queue))
    process.start()
    printWithTime("Between Start to Join_1", run_start_time)
    time.sleep(1)
    printWithTime("Between Start to Join_2", run_start_time)
    time.sleep(1)
    printWithTime("Between Start to Join_3", run_start_time)
    time.sleep(5)
    printWithTime("Between Start to Join_4", run_start_time)
    time.sleep(1)
    process.join()
    return_from_process = queue.get()
    printWithTime("The process returned " + str(return_from_process), run_start_time)
    printWithTime("Done", run_start_time)
    

if __name__ == "__main__":
    start_time = time.time()
    main()
    end_time = time.time()
    time_total = end_time - start_time
    printWithTime(time_total)