###TODOS#######
#put limits on input values
#put error handling
#create command to get start time

####PARAMS
#Sample volume amount
#Tracer volume amount
#TIMEZERO start time
#TIMEZERO ports
#TIMEZERO time between ports
#TIMEZERO volume amount
#Amount of time between TIMEZERO and TIMEONE
#TIMEONE start time
#TIMEONE ports
#TIMEONE time between ports
#Number of incubation studies to be ran

import sys
import os

def int_check(parameter, min_value, max_value):
    valid_answer = False
    while not(valid_answer):
            number1 = input(': ')
            number1 = int(number1)
            if (number1 < min_value) or (number1 > max_value):
                print("Input must be a number between " + str(min_value) + " and " + str(max_value)) #raise Exception
                continue
            #if not(type(number1) == "int"):
            #num_type = type(number1)
            if not(isinstance(number1,int)):
                print(type(number1))
                print("Enter a number")
                continue
            else:
                valid_answer = True
                return number1
    
    
os.chdir(os.path.dirname(os.path.abspath(__file__)))
filename = 'msconfig.cfg'
iV_dft=2000 #default in mL
tV_dft=250 #default in mL

with open(filename, "w") as f:
#while True:
#try:
    print("Initial configutation/first-time setup")
    print("#####################################")
    print("Specify actual total incubator volume in mL")
    iV=int_check("iV", 0, 2000)
    f.write("iV:"+str(iV)+"\r")
    print("Specify actual total injector volume in mL")
    tV=int_check("tV", 0, 500)
    f.write("tV:"+str(tV)+"\r")
    print("TODO any more init cfg params")
    print(" ")
    print("#####################################")
    print("Incubator Pre-Flush Parameters")
    print("#####################################")
    print("Specify flush cycles for incubator")
    flush_cycles = input()
    print("Specify wait time between flush cycles, min. 5 seconds")
    flush_waittime = input()
    print("Specify flush amount in mL")
    flush_amount = input()
    def flush():
        f.write("#Incubator pre-flush")
        f.write("\r")
        f.write("wHp")          #wait for home port
        f.write("\r")
        f.write("gSp")          #get a prompt from the SID
        f.write("\r")
        f.write("eP")           #completely empty incubator
        f.write("\r")
        f.write("rP:"+flush_cycles)     #loop flush_cycles times
        f.write("\r")
        f.write("fV:"+flush_amount)     #flush amount
        f.write("\r")
        f.write("wS:"+flush_waittime)   #wait for flush_waittime seconds
        f.write("\r")
        f.write("eP")                   # completely empty incubator
        f.write("\r")
        f.write("eRpn")                 # end loop
        f.write("\r")
    print("#####################################")
    print("Filtration Test Parameters")
    print("#####################################")
    print("Specify total amount of filtration test cycles")
    #filtration_test_cycles = input()
   # for 1:filtration_test_cycles
        ##incubation draw volume
        ##injection draw volume
        ##CMD pump incubation chamber to HRV
        ##CMD pump HRV to filters
        ##at TIMEZERO pump to 1-5 ports
        ##wait adjustable time
        ##pump to next port
        ##repeat for up to 24 hours
    
    #flush()
    f.close()
    
#except EOFError:
#break
