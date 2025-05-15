#TODO fix time estimate

import os
import params
from datetime import datetime
import shared_funcs

study_type = 'filtration'

def set_num_positions(x):
    global number_of_positions
    number_of_positions = x

def get_num_positions():
    return number_of_positions

def set_tracer_source_is_incubation_chamber(x):
    global tracer_source_is_incubation_chamber
    tracer_source_is_incubation_chamber = x

def get_tracer_source_is_incubation_chamber():
    return tracer_source_is_incubation_chamber

def init_cfg():
    f.write("#Init config")
    f.write("\n")
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    f.write("#"+dt_string)
    f.write("\n")
    f.write("VB:1")                             # set verbose mode high to log all that happens, hard-coding on
    f.write("\n")
    f.write("TIM")                             # set Mclane time from PIC
    f.write("\n")
    print("Specify wait time in minutes to allow for instrument deployment, range is between "+str(params.deploymentWaitTime_min)+
          " and "+str(params.deploymentWaitTime_max)+". Default is "+str(params.deploymentWaitTime_dft))
    deploy_waittime = shared_funcs.int_check("flush_waittime", params.deploymentWaitTime_min, params.deploymentWaitTime_max, params.deploymentWaitTime_dft)
    if deploy_waittime > 0:
        f.write("#Wait for deployment "+str(deploy_waittime)+" minutes")
        f.write("\n")
        f.write("wA:"+str(deploy_waittime))     # wait for x minutes
        f.write("\n")
    print("Are you using the incubation chamber or injection pump as the tracer source? Yes for incubation chamber, no for injector")
    tracer_src = shared_funcs.yes_or_no()
    set_tracer_source_is_incubation_chamber(tracer_src)
    if (tracer_src):
        # incubation chamber
        print("Note: this is a one-time setting recording physical parameters of the sytem. Specify physical total injector volume in mL, range is between "
            +str(params.incubatorVolume_min)+" and "+str(params.incubatorVolume_max)+". Default is "+str(params.incubatorVolume_dft))
        tV=shared_funcs.int_check("tV", params.incubatorVolume_min, params.incubatorVolume_max, params.incubatorVolume_dft)
    else:
        # injection pump
        print("Note: this is a one-time setting recording physical parameters of the sytem. Specify physical total injector volume in mL, range is between "
                +str(params.injectorPhysicalVolume_min)+" and "+str(params.injectorPhysicalVolume_max)+". Default is "+str(params.injectorPhysicalVolume_dft))
        tV=shared_funcs.int_check("tV", params.injectorPhysicalVolume_min, params.injectorPhysicalVolume_max, params.injectorPhysicalVolume_dft)
    f.write("tV:"+str(tV))                  # specify physical volume of instrument tracer source
    f.write("\n")
    f.write("wHp")                          # go to HOME port to start
    f.write("\n")

def microgear_pump_config(microgear_volume):
    # direction, 1 forward, 0 reverse
    # volume in mL
    # rate in mL/min
    # min rate in mL/min
    # timeout in seconds

    print("Specify the microgear pump rate in mL/min, range is between "+str(params.filtrationMicrogearPumpRate_min)+
        " and "+str(params.filtrationMicrogearPumpRate_max)+". Default is "+str(params.filtrationMicrogearPumpRate_dft))
    microgear_pump_rate = shared_funcs.int_check("microgear_pump_rate", params.filtrationMicrogearPumpRate_min, params.filtrationMicrogearPumpRate_max, params.filtrationMicrogearPumpRate_dft)

    microgear_pump_string = str( str(params.filtrationMicrogearDirection_dft) + " " + str(round(microgear_volume,2)) + " "
                                + str(round(microgear_pump_rate,2)) + " " + str(params.filtrationMicrogearPumpRate_min)
                                + " " + str(params.filtrationMicrogearTimeout) )
    f.write("fO:"+microgear_pump_string)         #sample volume
    #f.write("\n")

def filtration():
    valid_response = False
    using_injector = False
    ports = []
    f.write("#filtration study")
    f.write("\n")

    ### intake ###
    while not(valid_response):
        if():
            #incubation chamber
            print("Specify total tracer volume to be used in mL, range is between "+str(params.incubatorVolume_min)+" and "+str(params.incubatorVolume_max)+". Default is "+str(params.incubatorVolume_dft))
            iT=shared_funcs.int_check("iT", params.incubatorVolume_min, params.incubatorVolume_max, params.incubatorVolume_dft)
        else:
            #injection pump
            print("Specify total tracer volume to be used in mL, range is between "+str(params.injectorVolume_min)+" and "+str(params.injectorVolume_max)+". Default is "+str(params.injectorVolume_dft))
            iT=shared_funcs.int_check("iT", params.injectorVolume_min, params.injectorVolume_max, params.injectorVolume_dft)
        if iT > 0:
            using_injector = True
        valid_response = True
    if using_injector:
        if get_tracer_source_is_incubation_chamber():
            # incubation chamber
            f.write("NPO:1")                                    # go to NULL port 1
            f.write("\n")
            f.write("fV:"+str(iT))                               #fill incubator nnnn mL
            f.write("\n")
        else:
            # injection pump
            f.write("NPO:1")                                    # go to NULL port 1 #TODO determine if necessary, likely not
            f.write("\n")
            f.write("iT:"+str(iT))                               #fill tt volume tracer mL
            f.write("\n")

    intake = iT                                             # intake is injector draw volume
    shared_funcs.set_intake(intake)                          # setting global to track intake volume
    print("INJECTOR INTAKE is "+str(intake))
    remaining_injector_volume = intake

    print("Specify amount of filtration timepoint samples to be completed, range is between "+str(params.filtrationPositions_min)+
      " and "+str(params.filtrationPositions_max)+". Default is "+str(params.filtrationPositions_dft))
    positions = shared_funcs.int_check("timepoint_samples", params.filtrationPositions_min, params.filtrationPositions_max, params.filtrationPositions_dft)
    set_num_positions(positions)
    print("Would you like to use the same volume between the "+str(positions)+" positions? If not you will be prompted to specify individual volumes for each port.")
    same_volume = shared_funcs.yes_or_no()
    if same_volume:
        print("Specify the sample volume in mL to be used for all "+str(positions)+" positions, range is between "+str(params.filtrationSameVolume_min)+
          " and "+str(params.filtrationSameVolume_max)+". Default is "+str(params.filtrationSameVolume_dft))
        same_volume_throughout = shared_funcs.int_check("same_volume_throughout", params.filtrationSameVolume_min, params.filtrationSameVolume_max, params.filtrationSameVolume_dft)
        #TODO confirm is ok to use same tracer volume if same sample volume utilized; otherwise need more logic here
        params.filtrationTracerSameVolume_max = intake / positions              #can't use more than the amount of tracer in the bag
        print("Specify the tracer volume in mL to be used for all "+str(positions)+" positions, range is between "+str(params.filtrationTracerSameVolume_min)+
          " and "+str(params.filtrationTracerSameVolume_max)+". Default is "+str(params.filtrationTracerSameVolume_dft))
        same_injector_volume_throughout = shared_funcs.int_check("same_volume_throughout", params.filtrationTracerSameVolume_min, params.filtrationTracerSameVolume_max, params.filtrationTracerSameVolume_dft)
    print("Would you like to wait the same amount of time in seconds between the "+str(positions)+" positions? If not you will be prompted to specify individual wait times for each port.")
    same_time = shared_funcs.yes_or_no()
    if same_time:
        print("Specify the time in seconds to wait between each of the "+str(positions)+" positions, range is between "+str(params.waitTimeBetweenTimepointSamples_min)+
          " and "+str(params.waitTimeBetweenTimepointSamples_max)+". Default is "+str(params.waitTimeBetweenTimepointSamples_dft))
        time_between_samples = shared_funcs.int_check("time_between_samples", params.waitTimeBetweenTimepointSamples_min, params.waitTimeBetweenTimepointSamples_max, params.waitTimeBetweenTimepointSamples_dft)
    
    ports = shared_funcs.port_selection(positions,study_type)
    for x in range(positions):
        (confirm_remaining_injector_vol) = False
        f.write("#Position "+str(x+1))
        f.write("\n")
        f.write("pO:"+str(ports[x]))    #go to PORT X
        f.write("\n")
        if same_volume:
            microgear_pump_config(same_volume_throughout)
            f.write("wS:1")                                    #wait for 1 second
            f.write("\n")
            f.write("pO:"+str(ports[x]+1))                        #go to odd PORT X+1 for tracer
            f.write("\n")
            if get_tracer_source_is_incubation_chamber(): #incubation chamber tracer source
                f.write("eV:"+str(same_injector_volume_throughout))         #pump injector mL
            else: #injector tracer source
                f.write("iT:"+str(same_injector_volume_throughout))         #fill tt volume tracer mL
            f.write("\n")
        else:
            print("Remaining injector volume to use is "+str(remaining_injector_volume)+" mL")
            while not((confirm_remaining_injector_vol)):
                print("Specify amount of sample to pump through PORT "+str(ports[x])+", range is between "+str(params.filtrationSampleVolume_min)+
                    " and "+str(params.filtrationSampleVolume_max)+". Default is "+str(params.filtrationSampleVolume_dft))
                filtrationSampleVolume = shared_funcs.int_check("filtrationSampleVolume", params.filtrationSampleVolume_min, params.filtrationSampleVolume_max, params.filtrationSampleVolume_dft)
                print("Specify amount of tracer to pump through PORT "+str(ports[x]+1)+", range is between "+str(params.filtrationTracerVolume_min)+
                    " and "+str(params.filtrationTracerVolume_max)+". Default is "+str(params.filtrationTracerVolume_dft))
                filtrationTracerVolume = shared_funcs.int_check("filtrationTracerVolume", params.filtrationTracerVolume_min, params.filtrationTracerVolume_max, params.filtrationTracerVolume_dft)
                if filtrationTracerVolume > remaining_injector_volume:
                    print("Tracer volume specified exceeds remaining tracer bag volume. Max allowed volume is "+str(remaining_injector_volume)+". Please reenter.")
                else:
                    (confirm_remaining_injector_vol) = True
                    remaining_injector_volume = remaining_injector_volume - filtrationTracerVolume        
                    microgear_pump_config(filtrationSampleVolume)       #sample volume
                    f.write("\n")
                    f.write("wS:1")                                    #wait for 1 second
                    f.write("\n")
                    f.write("pO:"+str(ports[x]+1))                        #go to odd PORT X+1 for tracer
                    f.write("\n")
                    if get_tracer_source_is_incubation_chamber(): #incubation chamber tracer source
                        f.write("eV:"+str(filtrationTracerVolume))         #pump injector mL
                    else: #injector tracer source
                        f.write("iT:"+str(filtrationTracerVolume))         #fill tt volume tracer mL
                    f.write("\n")

        if same_time:
            f.write("wS:"+str(round(time_between_samples,2)))                #wait for X seconds
            f.write("\n")
            time = shared_funcs.get_est_runtime() + positions * params.fillFilterTime + positions * time_between_samples
            shared_funcs.set_est_runtime(time)
        else:
            print("Specify the time in seconds to wait after PORT "+str(ports[x])+", range is between "+str(params.filtrationWaitTimeBetweenPositions_min)+
              " and "+str(params.filtrationWaitTimeBetweenPositions_max)+". Default is "+str(params.filtrationWaitTimeBetweenPositions_dft))
            incubationTestSampleWaitTime = shared_funcs.int_check("filtrationTestSampleWaitTime", params.filtrationWaitTimeBetweenPositions_min, params.filtrationWaitTimeBetweenPositions_max, params.filtrationWaitTimeBetweenPositions_dft)
            f.write("wS:"+str(incubationTestSampleWaitTime))       #wait for X seconds
            f.write("\n")
            time = shared_funcs.get_est_runtime() + positions * params.fillFilterTime + positions * incubationTestSampleWaitTime
            shared_funcs.set_est_runtime(time)
    if same_volume:
        print("SUBSAMPLE for all "+str(positions)+ " is "+str(round(same_volume_throughout,2)) + "mL")

def config_summary():
    f.write("\n")
    f.write("#SUMMARY")
    f.write("\n")
    f.write("#"+str(shared_funcs.get_est_runtime())+" SECONDS")
    f.write("\n")
    f.write("#PORTS IN USE ARE "+str(shared_funcs.get_stored_ports()))
    f.write("\n")
    print("vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv")
    print("Filtration Study Summary")
    print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
    time = shared_funcs.get_est_runtime() * get_num_positions()
    shared_funcs.set_est_runtime(time)
    print("Estimated runtime in seconds is "+str(shared_funcs.get_est_runtime())+" seconds which is "+str(round(shared_funcs.get_est_runtime()/60,2))+" minutes")
    print("Ports in use are "+str(shared_funcs.get_stored_ports()))

#file generation   
os.chdir(os.path.dirname(os.path.abspath(__file__)))
filename = 'msconfig.cfg'

#main calls
with open(filename, "w") as f:
    print("#####################################")
    print("Initial configuration/first-time setup")
    print("#####################################")
    init_cfg()
    #print("Specify number of position to be collected, range is between "+str(params.filtrationPositions_min)+" and "+str(params.filtrationPositions_max)+". Default is "+str(params.filtrationPositions_dft))
    #positions = shared_funcs.int_check("experiments", params.filtrationPositions_min, params.filtrationPositions_max, params.filtrationPositions_dft)
    print("#####################################")
    print("Filtration Test Parameters")
    print("#####################################")
    filtration()
    print(" ")
    config_summary()
    f.write("eNd")                              #end of script
    f.write("\n")
    f.write("#END")                              #end of script
    f.write("\n")


    f.close()
