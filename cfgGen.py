###TODOS####### TODO
#add intake volume, outtake volume to end of file summary
#put in handling for verifying that subscample volume doesn't exceed OUTTAKE
#put in handling to empty and zero chamber after an experiment

import os
import params
from datetime import datetime

stored_ports = []
est_runtime = 0


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
            
def port_selection(timepoint_samples):
    min_value = 2
    max_value = 98
    ports = []
    final_port = False

    print("Select port positions for this timepoint sample. Even ports only for an incubation study. PORT0 is HOME. PORT98 is last available port.")
    print("=====================================")
    #num_ports = int(input("Enter number of ports collecting samples for this study : "))
    num_ports = timepoint_samples

    if num_ports == 1: #handling for only one timepoint sample specified
        while not(final_port):
            port_selection = input("Enter port number for timepoint sample 1 : ")
            try:
                port_selection = int(port_selection)
            except:
                print("Integers only. No characters or letters allowed.")
                continue
            #print(check_port_usage(stored_ports,port_selection))
            if (port_selection < min_value) or (port_selection > max_value):
                print("Input must be a number between " + str(min_value) + " and " + str(max_value))
                continue
            elif port_selection in get_stored_ports():
                print("This port has already been used. Please select again.")
                continue
            elif not(port_selection % 2 == 0):
                print("Entry must be an even port to commence an incubation study")
                continue
            else:
                ports.append(port_selection) # add port to array for this study
                set_stored_ports(port_selection)  #set to global
                final_port = True # at the final port selection, exit loop
                break

    else:               #handling for any more than one timepoint samples
        for i in range(1, num_ports):
            while not(final_port):
                port_selection = input("Enter port number for timepoint sample "+str(i)+": ")
                try:
                    port_selection = int(port_selection)
                except:
                    print("Integers only. No characters or letters allowed.")
                    continue

                if (port_selection < min_value) or (port_selection > max_value):
                    print("Input must be a number between " + str(min_value) + " and " + str(max_value))
                    continue
                elif port_selection in get_stored_ports():
                    print("This port has already been used. Please select again.")
                    continue
                elif not(port_selection % 2 == 0):
                    print("Entry must be an even port to commence an incubation study")
                    continue
                else:
                    ports.append(port_selection) # add port to array for this timepoint
                    set_stored_ports(port_selection)  #set to global
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

def set_outtake(x):
     global outtake
     outtake = x

def get_outtake():
     return outtake

def set_est_runtime(x):
    global est_runtime
    est_runtime = x

def get_est_runtime():
    return est_runtime

def set_stored_ports(x):
    stored_ports.append(x)

def get_stored_ports():
    return stored_ports

def check_port_usage(stored_ports, port_request):

    if port_request not in stored_ports:
        stored_ports.append(port_request)
        return True
    else:
        print("This port already in use!")
        return False


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
    valid_response = False
    using_injector = False
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    f.write("#"+dt_string)
    f.write("\n\r")
    f.write("VB:1")                             # set verbose mode high to log all that happens, hard-coding on
    f.write("\n\r")
    f.write("TIM")                             # set Mclane time from PIC
    f.write("\n\r")
    print("Specify wait time in minutes to allow for instrument deployment, range is between "+str(params.deploymentWaitTime_min)+
          " and "+str(params.deploymentWaitTime_max)+". Default is "+str(params.deploymentWaitTime_dft))
    deploy_waittime = int_check("flush_waittime", params.deploymentWaitTime_min, params.deploymentWaitTime_max, params.deploymentWaitTime_dft)
    if deploy_waittime > 0:
        f.write("#Wait for deployment "+str(deploy_waittime)+" minutes")
        f.write("\n\r")
        f.write("wA:"+str(deploy_waittime))     # wait for x minutes
        f.write("\n\r")
    print("Note: this is a one-time setting recording physical parameters of the sytem. Specify physical total injector volume in mL, range is between "
          +str(params.injectorPhysicalVolume_min)+" and "+str(params.injectorPhysicalVolume_max)+". Default is "+str(params.injectorPhysicalVolume_dft))
    tV=int_check("tV", params.injectorPhysicalVolume_min, params.injectorPhysicalVolume_max, params.injectorPhysicalVolume_dft)
    print("Note: this is a one-time setting recording physical parameters of the sytem. Specify physical total incubator volume in mL, range is between "
          +str(params.incubatorPhysicalVolume_min)+" and "+str(params.incubatorPhysicalVolume_max)+". Default is "+str(params.incubatorPhysicalVolume_dft))
    iV=int_check("iV", params.incubatorPhysicalVolume_min, params.incubatorPhysicalVolume_max, params.incubatorPhysicalVolume_dft)
    f.write("tV:"+str(tV))                  # specify physical volume of instrument injection chamber
    f.write("\n\r")
    f.write("iV:"+str(iV))                  # specify physical volume of instrument incubation chamber
    f.write("\n\r")
    f.write("wHp")                          # go to HOME port to start
    f.write("\n\r")
            
def flush():
    flush_waittime = 0                      # pre-defining
    f.write("#Incubator pre-flush")
    f.write("\n\r")
    print("Specify flush cycles for incubator, range is between "+str(params.flushCycles_min)+" and "+str(params.flushCycles_max)+". Default is "+str(params.flushCycles_dft))
    flush_cycles = int_check("flush_cycles", params.flushCycles_min, params.flushCycles_max, params.flushCycles_dft)
    f.write("rP:"+str(flush_cycles))        #repeat for flush_cycles times
    f.write("\n\r")
    for x in range(flush_cycles):
        f.write("#Flush cycle "+str(x+1))
        f.write("\n\r")
        print("Specify wait time in seconds between flush cycles for flush cycle "+str(x)+", range is between "+str(params.flushWaittime_min)+
              " and "+str(params.flushWaittime_max)+". Default is "+str(params.flushWaittime_dft))
        flush_waittime = int_check("flush_waittime", params.flushWaittime_min, params.flushWaittime_max, params.flushWaittime_dft)
        print("Specify flush amount in mL, range is between "+str(params.flushAmount_min)+" and "+str(params.flushAmount_max)+". Default is "+str(params.flushAmount_dft))
        flush_amount = int_check("flush_amount", params.flushAmount_min, params.flushAmount_max, params.flushAmount_dft)
        f.write("wHp")                      #wait for home port
        f.write("\n\r")
        f.write("gSp")                      #get a prompt from the SID
        f.write("\n\r")
        f.write("eP")                       #completely empty incubator
        f.write("\n\r")
        f.write("rP:"+str(flush_cycles))    #loop flush_cycles times
        f.write("\n\r")
        f.write("fV:"+str(flush_amount))     #flush amount
        f.write("\n\r")
        f.write("wS:"+str(flush_waittime))   #wait for flush_waittime seconds
        f.write("\n\r")
        f.write("eP")                        # completely empty incubator
        f.write("\n\r")
    f.write("eRpn")                      # end loop
    f.write("\n\r")
    
    time = get_est_runtime() + params.emptyIncubationChamberTime * flush_cycles + flush_waittime * flush_cycles
    set_est_runtime(time)

def incubation():
    ports = []
    f.write("#incubation study")
    f.write("\n\r")

    while not(valid_response):
        print("Specify experiment total injector volume in mL, range is between "+str(params.injectorVolume_min)+" and "+str(params.injectorVolume_max)+". Default is "+str(params.injectorVolume_dft))
        iT=int_check("iT", params.injectorVolume_min, params.injectorVolume_max, params.injectorVolume_dft)
        print("Specify experiment total incubator volume in mL, range is between "+str(params.incubatorVolume_min)+" and "+str(params.incubatorVolume_max)+". Default is "+str(params.incubatorVolume_dft))
        fV=int_check("fV", params.incubatorVolume_min, params.incubatorVolume_max, params.incubatorVolume_dft)
        if iT > 0:
            using_injector = True
        if iT + fV > params.incubatorVolume_max:
            print("The specified values for injector volume ("+str(iT)+") and incubator intake volume ("+str(fV)+") are larger than maximum allowed ("+str(params.incubatorVolume_max)+"). Please reenter.")
        else:
            valid_response = True
    if using_injector:
        f.write("fT:"+str(fV)+","+str(iT))                      #fill incubator nnnn & tt volume tracer mL
        f.write("\n\r")
    else:
        f.write("fV:"+str(fV))                               #fill incubator nnnn mL 
        f.write("\n\r")
    intake = iT + fV                        # intake is total within incubation chamber, sum of injector and incbuator draw volumes
    set_intake(intake)                          # setting global to track intake volume
    print("Specify amount of incubation chamber volume to be used during incubation study, range is between "+str(params.incubationTestIncubatorDrawVolume_min)+" and "
          +str(params.incubationTestIncubatorDrawVolume_max)+". Default is "+str(params.incubationTestIncubatorDrawVolume_dft)+". This number will be referred to as the OUTTAKE.") # TODO do inject first and do total volume check
    outtake = int_check("outtake", params.incubationTestIncubatorDrawVolume_min, params.incubationTestIncubatorDrawVolume_max, params.incubationTestIncubatorDrawVolume_dft)
    set_outtake(outtake)
    print("Specify amount of injector chamber volume to be used during incubation study, range is between "+str(params.incubationTestInjectorDrawVolume_min)+" and "
          +str(params.incubationTestInjectorDrawVolume_max)+". Default is "+str(params.incubationTestInjectorDrawVolume_dft))
    incubation_test_injector_volume = int_check("incubation_test_injector_volume", params.incubationTestInjectorDrawVolume_min, params.incubationTestInjectorDrawVolume_max, params.incubationTestInjectorDrawVolume_dft)
    f.write("iT:"+str(incubation_test_injector_volume))
    f.write("\n\r")
    time = get_est_runtime() + params.fillIncubationChamberTime
    set_est_runtime(time)
    #f.write("#TODO verify cmd exists for pump incubation chamber to HRV\n\r")#TODO
    print("Specify amount of incubation timepoint sample to be completed, range is between "+str(params.timepointSamples_min)+
          " and "+str(params.timepointSamples_max)+". Default is "+str(params.timepointSamples_dft))
    timepoint_samples = int_check("timepoint_samples", params.timepointSamples_min, params.timepointSamples_max, params.timepointSamples_dft)

    print("Would you like to divide the sample volume evenly between the "+str(timepoint_samples)+" timepoint samples? If not you will be prompted to specify individual sample volumes for each port.")
    volume_divided_evenly = yes_or_no()

    print("Would you like to wait the same amount of time in seconds between the "+str(timepoint_samples)+" timepoint samples? If not you will be prompted to specify individual wait times for each sample.")
    time_divided_evenly = yes_or_no()
    if time_divided_evenly:
        print("Specify the time in seconds to wait between the "+str(timepoint_samples)+" timepoint samples, range is between "+str(params.waitTimeBetweenTimepointSamples_min)+
              " and "+str(params.waitTimeBetweenTimepointSamples_max)+". Default is "+str(params.waitTimeBetweenTimepointSamples_dft))
        time_between_samples = int_check("time_between_samples", params.waitTimeBetweenTimepointSamples_min, params.waitTimeBetweenTimepointSamples_max, params.waitTimeBetweenTimepointSamples_dft)

    ports = port_selection(timepoint_samples)
    for x in range(timepoint_samples):
        #f.write("\r\n")
        #f.write("\r\n")
        if volume_divided_evenly:
            incubationTestSampleVolume = intake / timepoint_samples
            f.write("eV:"+str(round(incubationTestSampleVolume,2)))         #sample volume
            f.write("\n\r")
        else:
            print("Specify amount of sample volume to pump through PORT  "+str(ports[x])+" ,range is between "+str(params.incubationTestSampleVolume_min)+
                  " and "+str(params.incubationTestSampleVolume_max)+". Default is "+str(params.incubationTestSampleVolume_dft))
            incubationTestSampleVolume = int_check("incubationTestSampleVolume", params.incubationTestSampleVolume_min, params.incubationTestSampleVolume_max, params.incubationTestSampleVolume_dft)
            f.write("eV:"+str(incubationTestSampleVolume))         #sample volume
            f.write("\n\r")
        if time_divided_evenly:
            f.write("wS:"+str(round(time_between_samples,2)))                #wait for X seconds
            f.write("\n\r")
            time = get_est_runtime() + timepoint_samples * params.fillFilterTime + timepoint_samples * time_between_samples
            set_est_runtime(time)
        else:
            print("Specify the time in seconds to wait after "+str(ports[x])+", range is between "+str(params.incubationTestSampleVolume_min)+
                  " and "+str(params.incubationTestSampleVolume_max)+". Default is "+str(params.incubationTestSampleVolume_dft))
            incubationTestSampleWaitTime = int_check("incubationTestSampleWaitTime", params.incubationTestSampleVolume_min, params.incubationTestSampleVolume_max, params.incubationTestSampleVolume_dft)
            f.write("wS:"+str(incubationTestSampleWaitTime))       #wait for X seconds
            f.write("\n\r")
            time = get_est_runtime() + timepoint_samples * params.fillFilterTime + timepoint_samples * incubationTestSampleWaitTime
            set_est_runtime(time)
        
        
def wait_for_next_experiment():
    print("Specify how long to wait until the start of the next experiment. This can be a long time. Range is between "+str(params.experimentWaitTime_min)+
          " and "+str(params.experimentWaitTime_max)+". Default is "+str(params.experimentWaitTime_dft))
    experiment_wait_time=int_check("experiment_wait_time", params.experimentWaitTime_min, params.experimentWaitTime_max, params.experimentWaitTime_dft)
    f.write("#POST EXPERIMENT")
    f.write("\n\r")
    f.write("#INTAKE "+str(get_intake())+" mL")      #report intake volume
    f.write("\n\r")
    f.write("#OUTTAKE "+str(get_outtake())+" mL")    #report outtake volume
    f.write("\n\r")
    f.write("wHp")                              #wait for home port
    f.write("\n\r")
    f.write("eP")                                #completely empty incubator
    f.write("\n\r")
    f.write("wA:"+str(experiment_wait_time))    #wait for X minutes
    f.write("\n\r")
    time = get_est_runtime() + experiment_wait_time * 60 #convert to seconds
    set_est_runtime(time)

def config_summary():
    f.write("\n\r")
    f.write("#SUMMARY")
    f.write("\n\r")
    f.write("#"+str(get_est_runtime())+" SECONDS")
    f.write("\n\r")
    f.write("#PORTS IN USE ARE "+str(get_stored_ports()))
    f.write("\n\r")
    print("vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv")
    print("Experiment Summary")
    print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
    time = get_est_runtime() * experiments
    set_est_runtime(time)
    print("Estimated runtime in seconds is "+str(get_est_runtime())+" seconds which is "+str(round(get_est_runtime()/60,2))+" minutes")
    print("Ports in use are "+str(get_stored_ports()))
    
#file generation   
os.chdir(os.path.dirname(os.path.abspath(__file__)))
filename = 'msconfig.cfg'

#main calls
with open(filename, "w") as f:
    print("#####################################")
    print("Initial configutation/first-time setup")
    print("#####################################")
    init_cfg()
    print("Specify amount of experiments will be ran, range is between "+str(params.experiments_min)+" and "+str(params.experiments_max)+". Default is "+str(params.experiments_dft))
    experiments = int_check("experiments", params.experiments_min, params.experiments_max, params.experiments_dft)
    for x in range(experiments):
        #TODO function for reading if chamber is empty
        f.write("#EXPERIMENT "+str(x+1)+"\n\r")
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
        print("Between Experiment Parameters")
        print("#####################################")
        wait_for_next_experiment()
        print(" ")
    config_summary()
    f.write("eNd")                              #end of script
    f.write("\n\r")
    f.write("#END")                              #end of script
    f.write("\n\r")


    f.close()
