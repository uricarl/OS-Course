import os
import multiprocessing


def getStrPIDandPPID():
    return str(os.getpid()) + " and parent PID is " + str(os.getppid())

def printUntil(limit):
    print("Now running printUntil function, the PID is " + getStrPIDandPPID())
    for i in range(0, limit + 1):
        print(i)

def main():
    print("The main PID (current process) is " + getStrPIDandPPID())
    process = multiprocessing.Process(target=printUntil, args=(10,))
    process.start()
    process.join()

if __name__ == "__main__":
    main()