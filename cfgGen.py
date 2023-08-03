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

#### PARAMETER LIMITS ####
## initial setup ##
incubatorVolume_min = 0 #mL
incubatorVolume_max = 2000 #mL
injectorVolume_min = 0 #mL
injectorVolume_max = 250 #mL
## flush ##
flushCycles_min = 0
flushCycles_max = 5
flushWaittime_min = 5 #sec
flushWaittime_max = 300 #sec
flushAmount_min = 0 #mL
flushAmount_max = 2000 #mL
## filtration ##
filtrationTestCycles_min = 0
filtrationTestCycles_max = 50
filtrationTestIncubatorDrawVolume_min = 0 #mL
filtrationTestIncubatorDrawVolume_max = 2000 #mL
filtrationTestInjectorDrawVolume_min = 0 #mL
filtrationTestInjectorDrawVolume_max = 2000 #mL
filtrationTestWaitBetweenPorts_min = 0 #sec
filtrationTestWaitBetweenPorts_max = 300 #sec
filtrationTestWaitBetweenStudies_min = 0 #sec
filtrationTestWaitBetweenStudies_max = 200000 #sec


acceptable_chars = set('0123456789')


import sys
import os

def int_check(parameter, min_value, max_value):
    valid_answer = False
    while not(valid_answer):
            number1 = input(': ')
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
    print("Specify actual total incubator volume in mL, range is between "+str(incubatorVolume_min)+" and "+str(incubatorVolume_max))
    iV=int_check("iV", incubatorVolume_min, incubatorVolume_max)
    f.write("iV:"+str(iV)+"\r")
    print("Specify actual total injector volume in mL, range is between "+str(injectorVolume_min)+" and "+str(injectorVolume_max))
    tV=int_check("tV", injectorVolume_min, injectorVolume_max)
    f.write("tV:"+str(tV)+"\r")
    print("TODO any more init cfg params")
            
def flush():
    print("Specify flush cycles for incubator, range is between "+str(flushCycles_min)+" and "+str(flushCycles_max))
    flush_cycles = int_check("flush_cycles", flushCycles_min, flushCycles_max)
    print("Specify wait time in seconds between flush cycles, range is between "+str(flushWaittime_min)+" and "+str(flushWaittime_max))
    flush_waittime = int_check("flush_waittime", flushWaittime_min, flushWaittime_max)
    print("Specify flush amount in mL, range is between "+str(flushAmount_min)+" and "+str(flushAmount_max))
    flush_amount = int_check("flush_amount", flushAmount_min, flushAmount_max)
    f.write("#Incubator pre-flush")
    f.write("\r")
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

def filtration():
    print("Specify amount of filtration cycles to be completed, range is between "+str(filtrationTestCycles_min)+" and "+str(filtrationTestCycles_max))
    filtration_test_cycles = int_check("flush_cycles", filtrationTestCycles_min, filtrationTestCycles_max)
    f.write("#Filtration study")

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
    print('filler')
    
    
os.chdir(os.path.dirname(os.path.abspath(__file__)))
filename = 'msconfig.cfg'
iV_dft=2000 #default in mL
tV_dft=250 #default in mL

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
    print("Filtration Test Parameters")
    print("#####################################")
    print("Specify total amount of filtration test cycles")

    f.close()
