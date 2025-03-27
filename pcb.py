from enum import Enum, auto

class PCB():
   
    def __init__(self, process_name: str, process_id: int, process_state: Enum, program_counter: int,
                  registers: list[bool], memory_limits: tuple[int, int], list_of_open_files: list[str]):
        self._process_name = process_name
        self._process_id = process_id
        self._process_state = process_state
        self._program_counter = program_counter
        self._registers = registers
        self._memory_limits = memory_limits
        self._list_of_open_files = list_of_open_files


    def getName(self):
        return self._process_name
    
   
    def getId(self):
        return self._process_id
    

    def getProcessState(self):
        return self._process_state.name
    

    def getProgramCounter(self):
        return self._program_counter
    

    def getRegisters(self):
        return self._registers
    

    def getMemoryLimits(self):
        return self._memory_limits
    

    def getListOfOpenFiles(self):
        return self._list_of_open_files
    
    def printBrifProcess(self):
        print("Name: " + self.getName() + " | PID: " + str(self.getId()) + " | State: " + str(self.getProcessState()))

    def printAllDetails(self):
        print("=====| " + str(self.getId()) + " |=====")
        print("Name: " + self.getName())
        print("Process state: " + self.getProcessState())
        print("Program counter: " + str(self.getProgramCounter()))
        print("Registers: " + str(self.getRegisters()))
        print("Memory limits: " + str(self.getMemoryLimits()))
        print("List of open files: " + str(self.getListOfOpenFiles()))
        print("===== | *** | =====")


class ststeProcessOption(Enum):
    NEW = auto()
    READY = auto()
    RUN = auto()
    WAITING = auto()
    TERMINATED = auto()