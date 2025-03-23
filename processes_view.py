from pcb import PCB, ststeProcessOption

process_1 = PCB("System", 4, ststeProcessOption.RUN, 22705, [False, False, False, True, True, True], (22705, 23705), [])
process_2 = PCB("girobex.exe", 489, ststeProcessOption.WAITING, 32157, [True, False, False, True, True, True], (30105, 33147), [])
process_3 = PCB("dritermoflex.exe", 705, ststeProcessOption.READY, 78385, [True, True, False, True, True, True], (77052, 79351), [r"C:\Users\Gilad\Desktop\GitCourse\first-python-project\main.exe", r"C:\Users\Gilad\Desktop\GitCourse\first-python-project\data.csv"])
process_list = [process_1, process_2, process_3]
PID_dict = {process_1.getId(): process_1,
            process_2.getId(): process_2,
            process_3.getId(): process_3,}

def mainFunc():
   
   while True:
      selection = printMenu()
      if selection == 1:
         printBrifProcesses(process_list)
      elif selection == 2:
         serchByPID(PID_dict)
      elif selection == 3:
         printAllNames(process_list)
      elif selection == 4:
         printAllIds(process_list)
      elif selection == 5:
         if exitProgram():
            break
      input("Press enter to continue")

def printBrifProcesses(process_list):
   for i in range(0, len(process_list)):
    process_list[i].printBrifProcess()


# 2. Search by ID
def serchByPID(PID_dict):
    id = input("enter the PID you want to look for: ")
    id = int(id)
    PID_dict[id].printAllDetails()
    
 
# 3. Print all names
def printAllNames(process_list):
    for i in range(0, len(process_list)):
        print(process_list[i].getName())
        
 
# 4. Print all IDs
def printAllIds(process_list):
    for i in range(0, len(process_list)):
        print(process_list[i].getId())


# 5. exit
def exitProgram():
   while True:
      choise = input("Are you sure? (y/n) ")
      if choise == "y":
         print("Goodbye!")
         return True
      elif choise == "n":
         return False
 

def printMenu():
   print("1. Print Brif Of Processes")
   print("2. Search by PID")
   print("3. Print all names")
   print("4. Print all IDs")
   print("5. Exit")
   choise = input("Please enter your choise: ")
   if not choise.isdigit(): # is_integer_number
     return errOptionNotExist(choise)
   choise = int(choise)
   if choise > 0 and choise < 9: # in_range
     return choise
   else:
     return errOptionNotExist(choise)

def errOptionNotExist(in_put):
	print("Error: Option [" + str(in_put) + "] does not exist. Please try again")
	return   

# Run code
try:
    mainFunc()
except:
   print("========= Error =========")