import os
import multiprocessing
import time


def printWithTime(str_1):
    str_1 = str(str_1)
    print(str(time.time()), end=" >> " + str_1 + "\n")


def getStrPIDandPPID():
    return str(os.getpid()) + " and parent PID is " + str(os.getppid())

def printUntil(limit):
    printWithTime("Now running printUntil function, the PID is " + getStrPIDandPPID())
    for i in range(0, limit + 1):
        printWithTime(i)
        time.sleep(1)

def main():
    printWithTime("The main PID (current process) is " + getStrPIDandPPID())
    process = multiprocessing.Process(target=printUntil, args=(10,))
    process.start()
    printWithTime("Between Start to Join_1")
    time.sleep(1)
    printWithTime("Between Start to Join_2")
    time.sleep(1)
    printWithTime("Between Start to Join_3")
    time.sleep(5)
    printWithTime("Between Start to Join_4")
    time.sleep(1)
    process.join()
    printWithTime("Done")
    

if __name__ == "__main__":
    start_time = time.time()
    main()
    end_time = time.time()
    time_total = end_time - start_time
    printWithTime(time_total)