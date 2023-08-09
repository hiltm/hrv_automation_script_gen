###TODOS#######
#put limits on input values
#put error handling
#create command to get start time
#find some way to estimate runtime

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

import params

acceptable_chars = set('0123456789')


import sys
import os

def int_check(parameter, min_value, max_value, dft_value):
    valid_answer = False
    while not(valid_answer):
            number1 = input(': ') or dft_value
            #if not(number1 in acceptable_chars):
            #     print('nah')
            #     continue
            #else:
            number1 = int(number1)
            if (number1 < min_value) or (number1 > max_value):
                print("Input must be a number between " + str(min_value) + " and " + str(max_value))
                continue
            if not(isinstance(number1,int)):
                print(type(number1))
                print("Enter a number")
                continue
            else:
                valid_answer = True
                return number1
            
def init_cfg():
    print("Specify actual total incubator volume in mL, range is between "+str(params.incubatorVolume_min)+" and "+str(params.incubatorVolume_max)+". Default is "+str(params.incubatorVolume_dft))
    iV=int_check("iV", params.incubatorVolume_min, params.incubatorVolume_max, params.incubatorVolume_dft)
    f.write("iV:"+str(iV)+"\r")
    print("Specify actual total injector volume in mL, range is between "+str(params.injectorVolume_min)+" and "+str(params.injectorVolume_max)+". Default is "+str(params.injectorVolume_dft))
    tV=int_check("tV", params.injectorVolume_min, params.injectorVolume_max, params.injectorVolume_dft)
    f.write("tV:"+str(tV)+"\r")
    print("TODO any more init cfg params")
            
def flush():
    f.write("#Incubator pre-flush")
    f.write("\r")
    print("Specify flush cycles for incubator, range is between "+str(params.flushCycles_min)+" and "+str(params.flushCycles_max)+". Default is "+str(params.flushCycles_dft))
    flush_cycles = int_check("flush_cycles", params.flushCycles_min, params.flushCycles_max, params.flushCycles_dft)
    f.write("rP:"+str(flush_cycles))   #repeat for flush_cycles times
    f.write("\r")
    for x in range(flush_cycles):
        print("Specify wait time in seconds between flush cycles for flush cycle "+str(x)+", range is between "+str(params.flushWaittime_min)+" and "+str(params.flushWaittime_max)+". Default is "+str(params.flushWaittime_dft))
        flush_waittime = int_check("flush_waittime", params.flushWaittime_min, params.flushWaittime_max, params.flushWaittime_dft)
        print("Specify flush amount in mL, range is between "+str(params.flushAmount_min)+" and "+str(params.flushAmount_max)+". Default is "+str(params.flushAmount_dft))
        flush_amount = int_check("flush_amount", params.flushAmount_min, params.flushAmount_max, params.flushAmount_dft)
        f.write("wHp")          #wait for home port
        f.write("\r")
        f.write("gSp")          #get a prompt from the SID
        f.write("\r")
        f.write("eP")           #completely empty incubator
        f.write("\r")
        f.write("rP:"+str(flush_cycles))    #loop flush_cycles times
        f.write("\r")
        f.write("fV:"+str(flush_amount))     #flush amount
        f.write("\r")
        f.write("wS:"+str(flush_waittime))   #wait for flush_waittime seconds
        f.write("\r")
        f.write("eP")                   # completely empty incubator
        f.write("\r")
        f.write("eRpn")                 # end loop
        f.write("\r")

def incubation():
    print("Specify amount of incubation cycles to be completed, range is between "+str(params.incubationTestCycles_min)+" and "+str(params.incubationTestCycles_max)+". Default is "+str(params.incubationTestCycles_dft))
    incubation_test_cycles = int_check("flush_cycles", params.incubationTestCycles_min, params.incubationTestCycles_max, params.incubationTestCycles_dft)
    f.write("#incubation study")

         #incubation_test_cycles = input()
   # for 1:incubation_test_cycles
        ##incubation draw volume
        ##injection draw volume
        ##CMD pump incubation chamber to HRV
        ##CMD pump HRV to filters
        ##at TIMEZERO pump to 1-5 ports
        ##wait adjustable time
        ##pump to next port
        ##repeat for up to 24 hours
    print('filler')
    
    
os.chdir(os.path.dirname(os.path.abspath(__file__)))
filename = 'msconfig.cfg'

with open(filename, "w") as f:
    print("#####################################")
    print("Initial configutation/first-time setup")
    print("#####################################")
    init_cfg()
    print(" ")
    print("#####################################")
    print("Incubator Pre-Flush Parameters")
    print("#####################################")
    flush()
    print(" ")
    print("#####################################")
    print("incubation Test Parameters")
    print("#####################################")
    print("Specify total amount of incubation test cycles")

    f.close()
