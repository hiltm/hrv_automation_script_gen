###TODOS#######
#check if using injector or not; this will have different commands sent to the PIC TODO
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
            try:
                number1 = int(number1)
            except:
                print("Integers only. No characters or letters allowed.")
                continue
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
            
def port_selection(sample_cycles):
    min_value = 2
    max_value = 98
    ports = []
    final_port = False

    print("Select port positions for this sample. Even ports only for an incubation study. PORT0 is HOME. PORT98 is last available port.")
    print("=====================================")
    #num_ports = int(input("Enter number of ports collecting samples for this study : "))
    num_ports = sample_cycles

    if num_ports == 1: #handling for only one sample cycle specified
        while not(final_port):
            port_selection = input("Enter port number for sample 1 : ")
            try:
                port_selection = int(port_selection)
            except:
                print("Integers only. No characters or letters allowed.")
                continue
            if (port_selection < min_value) or (port_selection > max_value):
                print("Input must be a number between " + str(min_value) + " and " + str(max_value))
                continue
            elif not(port_selection % 2 == 0):
                print("Entry must be an even port to commence an incubation study")
                continue
            else:
                ports.append(port_selection) # add port to array for this study
                final_port = True # at the final port selection, exit loop
                break

    else:               #handling for any more than sample cycle
        for i in range(1, num_ports):
            while not(final_port):
                port_selection = input("Enter port number for sample "+str(i)+": ")
                try:
                    port_selection = int(port_selection)
                except:
                    print("Integers only. No characters or letters allowed.")
                    continue

                if (port_selection < min_value) or (port_selection > max_value):
                    print("Input must be a number between " + str(min_value) + " and " + str(max_value))
                    continue
                elif not(port_selection % 2 == 0):
                    print("Entry must be an even port to commence an incubation study")
                    continue
                else:
                    ports.append(port_selection) # add port to array for this study
                    if i == num_ports:
                        final_port = True # at the final port selection, exit loop
                        break
                    else:
                        i = i + 1 # go to next port selection
    return ports
            
def set_intake(x):
     global intake
     intake = x

def get_intake():
     return intake

def set_est_runtime(x):
    global est_runtime
    est_runtime = x

def get_est_runtime():
    return est_runtime

def yes_or_no():
    valid_answer = False
    while not(valid_answer):
        user_input = input('(y)es or (n)o: ')
        if user_input.lower() == 'yes' or user_input.lower() == 'y':
            var = True
            valid_answer = True
        elif user_input.lower() == 'no' or user_input.lower() == 'n':
            var = False
            valid_answer = True
        else:
            print('Type (y)es or (n)o')
            continue
    return var
            
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
    print("TODO any more init cfg params")#TODO
            
def flush():
    f.write("#Incubator pre-flush")
    f.write("\r")
    print("Specify flush cycles for incubator, range is between "+str(params.flushCycles_min)+" and "+str(params.flushCycles_max)+". Default is "+str(params.flushCycles_dft))
    flush_cycles = int_check("flush_cycles", params.flushCycles_min, params.flushCycles_max, params.flushCycles_dft)
    f.write("rP:"+str(flush_cycles))        #repeat for flush_cycles times
    f.write("\r")
    for x in range(flush_cycles):
        f.write("#Flush cycle "+str(x+1))
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
    
        #time = get_est_runtime() + params.emptyIncubationChamberTime * flush_cycles + flush_waittime * flush_cycles
        #set_est_runtime(time)

def incubation():
    ports = []
    f.write("#incubation study")
    f.write("\r")
    print("The incubator chamber will be filled to the total incubator volume")
    f.write("fV:"+str(get_intake()))        # fill incubator chamber to total incubator volume
    f.write("\r")
    print("Specify amount of incubation chamber volume to be used during incubation study, range is between "+str(params.incubationTestIncubatorDrawVolume_min)+" and "
          +str(params.incubationTestIncubatorDrawVolume_max)+". Default is "+str(params.incubationTestIncubatorDrawVolume_dft)+". This number will be referred to as the OUTTAKE.")
    intake = int_check("intake", params.incubationTestIncubatorDrawVolume_min, params.incubationTestIncubatorDrawVolume_max, params.incubationTestIncubatorDrawVolume_dft)
    print("Specify amount of incubation chamber volume to be used during incubation study, range is between "+str(params.incubationTestInjectorDrawVolume_min)+" and "
          +str(params.incubationTestInjectorDrawVolume_max)+". Default is "+str(params.incubationTestInjectorDrawVolume_dft))
    incubation_test_injector_volume = int_check("incubation_test_injector_volume", params.incubationTestInjectorDrawVolume_min, params.incubationTestInjectorDrawVolume_max, params.incubationTestInjectorDrawVolume_dft)
    f.write("iT:"+str(incubation_test_injector_volume))
    f.write("\r")
    #time = get_est_runtime() + params.fillIncubationChamberTime
    #set_est_runtime(time)
    #f.write("#TODO verify cmd exists for pump incubation chamber to HRV\r")#TODO
    print("Specify amount of incubation sample cycles to be completed, range is between "+str(params.incubationTestSampleCycles_min)+" and "+str(params.incubationTestSampleCycles_max)+". Default is "+str(params.incubationTestSampleCycles_dft))
    sample_cycles = int_check("sample_cycles", params.incubationTestSampleCycles_min, params.incubationTestSampleCycles_max, params.incubationTestSampleCycles_dft)

    print("Would you like to divide the sample volume evenly between the "+str(sample_cycles)+" samples? If not you will be prompted to specify individual sample volumes for each port.")
    volume_divided_evenly = yes_or_no()

    print("Would you like to wait the same amount of time in seconds between the "+str(sample_cycles)+" samples? If not you will be prompted to specify individual wait times for each sample.")
    time_divided_evenly = yes_or_no()
    if time_divided_evenly:
        print("Specify the time in seconds to wait between the "+str(sample_cycles)+" samples, range is between "+str(params.incubationTestWaitBetweenStudies_min)+" and "+str(params.incubationTestWaitBetweenStudies_max)+". Default is "+str(params.incubationTestWaitBetweenStudies_dft))
        time_between_studies = int_check("time_between_studies", params.incubationTestWaitBetweenStudies_min, params.incubationTestWaitBetweenStudies_max, params.incubationTestWaitBetweenStudies_dft)

    ports = port_selection(sample_cycles)
    for x in range(sample_cycles):
        f.write("#Sample cycle "+str(x+1))
        f.write("\r")
        f.write("pO:"+str(ports[x]))    #go to PORT X
        f.write("\r")
        if volume_divided_evenly:
            incubationTestSampleVolume = intake / sample_cycles
            f.write("eV:"+str(round(incubationTestSampleVolume,2)))         #sample volume
            f.write("\r")
        else:
            print("Specify amount of sample volume to pump through PORT  "+str(ports[x])+" ,range is between "+str(params.incubationTestSsampleVolume_min)+" and "+str(params.incubationTestSsampleVolume_max)+". Default is "+str(params.incubationTestSsampleVolume_dft))
            incubationTestSampleVolume = int_check("incubationTestSampleVolume", params.incubationTestSsampleVolume_min, params.incubationTestSsampleVolume_max, params.incubationTestSsampleVolume_dft)
            f.write("eV:"+str(incubationTestSampleVolume))         #sample volume
            f.write("\r")
        if time_divided_evenly:
            f.write("wS:"+str(round(time_between_studies,2)))                #wait for X seconds
            f.write("\r")
        else:
            print("Specify the time in seconds to wait after "+str(ports[x])+", range is between "+str(params.incubationTestSsampleVolume_min)+" and "+str(params.incubationTestSsampleVolume_max)+". Default is "+str(params.incubationTestSsampleVolume_dft))
            incubationTestSampleWaitTime = int_check("incubationTestSampleWaitTime", params.incubationTestSsampleVolume_min, params.incubationTestSsampleVolume_max, params.incubationTestSsampleVolume_dft)
            f.write("wS:"+str(incubationTestSampleWaitTime))       #wait for X seconds
            f.write("\r")
    #time = get_est_runtime() + sample_cycles * params.fillFilterTime + sample_cycles * incubationTestSampleWaitTime
    #set_est_runtime(time)
        
        
def wait_for_next_study():
    print("Specify how long to wait until the start of the next study. This can be a long time. Range is between "+str(params.studyCycleWaitTime_min)+" and "+str(params.studyCycleWaitTime_max)+". Default is "+str(params.studyCycleWaitTime_dft))
    study_cycle_wait_time=int_check("study_cycle_wait_time", params.studyCycleWaitTime_min, params.studyCycleWaitTime_max, params.studyCycleWaitTime_dft)
    f.write("wHp")                              #wait for home port
    f.write("\r")
    f.write("eP")                                #completely empty incubator
    f.write("\r")
    f.write("wA:"+str(study_cycle_wait_time))    #wait for X minutes
    f.write("\r")
    #time = get_est_runtime() + study_cycle_wait_time * 60 #convert to seconds
    #set_est_runtime(time)


    
#file generation   
os.chdir(os.path.dirname(os.path.abspath(__file__)))
filename = 'msconfig.cfg'

#main calls
with open(filename, "w") as f:
    print("#####################################")
    print("Initial configutation/first-time setup")
    print("#####################################")
    init_cfg()
    print("Specify amount of study cycles will be ran, range is between "+str(params.studyCycles_min)+" and "+str(params.studyCycles_max)+". Default is "+str(params.studyCycles_dft))
    study_cycles = int_check("study_cycles", params.studyCycles_min, params.studyCycles_max, params.studyCycles_dft)
    for x in range(study_cycles):
        #TODO function for reading if chamber is empty
        f.write("#STUDY CYCLE 1\r")
        print(" ")
        print("#####################################")
        print("Incubator Pre-Flush Parameters")
        print("#####################################")
        flush()
        print(" ")
        print("#####################################")
        print("Incubation Test Parameters")
        print("#####################################")
        incubation()
        print(" ")
        print("#####################################")
        print("Between Study Parameters")
        print("#####################################")
        wait_for_next_study()
        print(" ")
        #time = get_est_runtime() * study_cycles
        #set_est_runtime(time)
        #print("est_runtime in seconds is "+get_est_runtime)


    f.close()
