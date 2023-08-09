###TODOS#######
#check if using injector or not; this will have different commands sent to the PIC
#create command to get start time
#find some way to estimate runtime

import os
import params
from datetime import datetime

acceptable_chars = set('0123456789')


def int_check(parameter, min_value, max_value, dft_value):
    valid_answer = False
    while not(valid_answer):
            number1 = input(': ') or dft_value
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
            
def set_intake(x):
     global intake
     intake = x

def get_intake():
     return intake
            
def init_cfg():
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    f.write("#"+dt_string)
    f.write("\r")
    print("Specify actual total incubator volume in mL, range is between "+str(params.incubatorVolume_min)+" and "+str(params.incubatorVolume_max)+". Default is "+str(params.incubatorVolume_dft))
    iV=int_check("iV", params.incubatorVolume_min, params.incubatorVolume_max, params.incubatorVolume_dft)
    set_intake(iV)                          # setting global to track intake volume
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
    f.write("rP:"+str(flush_cycles))        #repeat for flush_cycles times
    f.write("\r")
    for x in range(flush_cycles):
        f.write("#Flush cycle "+str(x))
        f.write("\r")
        print("Specify wait time in seconds between flush cycles for flush cycle "+str(x)+", range is between "+str(params.flushWaittime_min)+" and "+str(params.flushWaittime_max)+". Default is "+str(params.flushWaittime_dft))
        flush_waittime = int_check("flush_waittime", params.flushWaittime_min, params.flushWaittime_max, params.flushWaittime_dft)
        print("Specify flush amount in mL, range is between "+str(params.flushAmount_min)+" and "+str(params.flushAmount_max)+". Default is "+str(params.flushAmount_dft))
        flush_amount = int_check("flush_amount", params.flushAmount_min, params.flushAmount_max, params.flushAmount_dft)
        f.write("wHp")                      #wait for home port
        f.write("\r")
        f.write("gSp")                      #get a prompt from the SID
        f.write("\r")
        f.write("eP")                       #completely empty incubator
        f.write("\r")
        f.write("rP:"+str(flush_cycles))    #loop flush_cycles times
        f.write("\r")
        f.write("fV:"+str(flush_amount))     #flush amount
        f.write("\r")
        f.write("wS:"+str(flush_waittime))   #wait for flush_waittime seconds
        f.write("\r")
        f.write("eP")                        # completely empty incubator
        f.write("\r")
        f.write("eRpn")                      # end loop
        f.write("\r")

def incubation():
    f.write("#incubation study")
    f.write("\r")
    print("The incubator chamber will be filled to the total incubator volume")
    f.write("fV:"+str(get_intake()))        # fill incubator chamber to total incubator volume
    f.write("\r")
    print("Specify amount of incubation chamber volume to be used during incubation study, range is between "+str(params.incubationTestIncubatorDrawVolume_min)+" and "
          +str(params.incubationTestIncubatorDrawVolume_max)+". Default is "+str(params.incubationTestIncubatorDrawVolume_dft)+". This number will be referred to as the OUTTAKE.")
    intake = int_check("flush_cycles", params.incubationTestIncubatorDrawVolume_min, params.incubationTestIncubatorDrawVolume_max, params.incubationTestIncubatorDrawVolume_dft)
    print("Specify amount of incubation chamber volume to be used during incubation study, range is between "+str(params.incubationTestInjectorDrawVolume_min)+" and "
          +str(params.incubationTestInjectorDrawVolume_max)+". Default is "+str(params.incubationTestInjectorDrawVolume_dft))
    incubation_test_injector_volume = int_check("flush_cycles", params.incubationTestInjectorDrawVolume_min, params.incubationTestInjectorDrawVolume_max, params.incubationTestInjectorDrawVolume_dft)
    f.write("iT:"+str(incubation_test_injector_volume))
    f.write("\r")
    f.write("#TODO verify cmd exists for pump incubation chamber to HRV")
    print("Specify amount of incubation sample cycles to be completed, range is between "+str(params.incubationTestSampleCycles_min)+" and "+str(params.incubationTestSampleCycles_max)+". Default is "+str(params.incubationTestSampleCycles_dft))
    sample_cycles = int_check("flush_cycles", params.incubationTestSampleCycles_min, params.incubationTestSampleCycles_max, params.incubationTestSampleCycles_dft)
    for x in range(sample_cycles):
        f.write("#Sample cycle "+str(x))
        f.write("\r")
        ###########TODO port selection command

    print('filler')
    
#file generation   
os.chdir(os.path.dirname(os.path.abspath(__file__)))
filename = 'msconfig.cfg'

#main calls
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
    incubation()
    print(" ")

    f.close()
