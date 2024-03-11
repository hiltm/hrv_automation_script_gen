import os
import params
from datetime import datetime
import shared_funcs

stored_ports = []
est_runtime = 0

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
    print("Note: this is a one-time setting recording physical parameters of the sytem. Specify physical total injector volume in mL, range is between "
          +str(params.injectorPhysicalVolume_min)+" and "+str(params.injectorPhysicalVolume_max)+". Default is "+str(params.injectorPhysicalVolume_dft))
    tV=shared_funcs.int_check("tV", params.injectorPhysicalVolume_min, params.injectorPhysicalVolume_max, params.injectorPhysicalVolume_dft)
    f.write("tV:"+str(tV))                  # specify physical volume of instrument injection chamber
    f.write("\n")
    f.write("wHp")                          # go to HOME port to start
    f.write("\n")

def filtration():
    valid_response = False
    using_injector = False
    ports = []
    f.write("#filtration study")
    f.write("\n")

    ### intake ###
    while not(valid_response):
        print("Specify experiment total injector volume in mL, range is between "+str(params.injectorVolume_min)+" and "+str(params.injectorVolume_max)+". Default is "+str(params.injectorVolume_dft))
        iT=shared_funcs.int_check("iT", params.injectorVolume_min, params.injectorVolume_max, params.injectorVolume_dft)
        if iT > 0:
            using_injector = True
        if iT > params.injectorVolume_max:
            print("The specified values for injector volume ("+str(iT)+")is larger than maximum allowed ("+str(params.injectorVolume_max)+"). Please reenter.")
        else:
            valid_response = True
    if using_injector:
        f.write("NPO:1")                                    # go to NULL port 1
        f.write("\n")
        f.write("fT:"+str(fV)+","+str(iT))             #TODO change to injector only         #fill incubator nnnn & tt volume tracer mL
        f.write("\n")
    intake = iT                                             # intake is injector draw volume
    shared_funcs.set_intake(intake)                          # setting global to track intake volume
    print("INTAKE is "+str(intake))

    print("Specify amount of filtration timepoint samples to be completed, range is between "+str(params.filtrationPositions_min)+
      " and "+str(params.filtrationPositions_max)+". Default is "+str(params.filtrationPositions_dft))
    positions = shared_funcs.int_check("timepoint_samples", params.filtrationPositions_min, params.filtrationPositions_max, params.filtrationPositions_dft)
    print("Would you like to use the same volume between the "+str(positions)+" positions? If not you will be prompted to specify individual volumes for each port.")
    same_volume = shared_funcs.yes_or_no()
    if same_volume:
        print("Specify the volume to be used for all "+str(positions)+" positions, range is between "+str(params.filtrationSameVolume_min)+
          " and "+str(params.filtrationSameVolume_max)+". Default is "+str(params.filtrationSameVolume_dft))
        same_volume_throughout = shared_funcs.int_check("same_volume_throughout", params.filtrationSameVolume_min, params.filtrationSameVolume_max, params.filtrationSameVolume_dft)
    print("Would you like to wait the same amount of time in seconds between the "+str(positions)+" positions? If not you will be prompted to specify individual wait times for each port.")
    same_time = shared_funcs.yes_or_no()
    if same_time:
        print("Specify the time in seconds to wait between the "+str(positions)+" positions, range is between "+str(params.waitTimeBetweenTimepointSamples_min)+
          " and "+str(params.waitTimeBetweenTimepointSamples_max)+". Default is "+str(params.waitTimeBetweenTimepointSamples_dft))
    time_between_samples = shared_funcs.int_check("time_between_samples", params.waitTimeBetweenTimepointSamples_min, params.waitTimeBetweenTimepointSamples_max, params.waitTimeBetweenTimepointSamples_dft)
    ports = shared_funcs.port_selection(positions)
    for x in range(positions):
        (confirm_remaining_injector_vol) = False
        f.write("#Position "+str(x+1))
        f.write("\n")
        f.write("pO:"+str(ports[x]))    #go to PORT X
        f.write("\n")
        if same_volume:
            f.write("eV:"+str(round(same_volume_throughout,2)))         #sample volume
            f.write("\n")
        else:
            print("Remaining injector volume to use is "+str(remaining_injector_volume)+" mL")
            while not((confirm_remaining_injector_vol)):
                print("Specify amount of sample to pump through PORT "+str(ports[x])+" ,range is between "+str(params.filtrationSampleVolume_min)+
                    " and "+str(params.filtrationSampleVolume_max)+". Default is "+str(params.filtrationSampleVolume_dft))
                filtrationSampleVolume = shared_funcs.int_check("filtrationSampleVolume", params.filtrationSampleVolume_min, params.filtrationSampleVolume_max, params.filtrationSampleVolume_dft)
                print("Specify amount of sample to pump through PORT "+str(ports[x]+1)+" ,range is between "+str(params.filtrationTracerVolume_min)+
                    " and "+str(params.filtrationTracerVolume_max)+". Default is "+str(params.filtrationTracerVolume_dft))
                filtrationTracerVolume = shared_funcs.int_check("filtrationTracerVolume", params.filtrationTracerVolume_min, params.filtrationTracerVolume_max, params.filtrationTracerVolume_dft)
                ############ pick up here, next is to check that there is enough tracer remaining
                
                if filtrationTracerVolume > remaining_chamber_volume:
                    print("Sample volume specified exceeds remaining incubation chamber volume. Max allowed volume is "+str(remaining_chamber_volume)+". Please reenter.")
                else:
                    (confirm_remaining_injector_vol) = True
                    remaining_chamber_volume = remaining_chamber_volume - incubationTestSampleVolume
                    f.write("eV:"+str(incubationTestSampleVolume))         #sample volume
                    f.write("\n")
                    print("SUBSAMPLE is "+str(incubationTestSampleVolume))
        if time_divided_evenly:
            f.write("wS:"+str(round(time_between_samples,2)))                #wait for X seconds
            f.write("\n")
            time = shared_funcs.get_est_runtime() + timepoint_samples * params.fillFilterTime + timepoint_samples * time_between_samples
            shared_funcs.set_est_runtime(time)
        else:
            print("Specify the time in seconds to wait after "+str(ports[x])+", range is between "+str(params.incubationTestSampleVolume_min)+
              " and "+str(params.incubationTestSampleVolume_max)+". Default is "+str(params.incubationTestSampleVolume_dft))
            incubationTestSampleWaitTime = shared_funcs.int_check("incubationTestSampleWaitTime", params.incubationTestSampleVolume_min, params.incubationTestSampleVolume_max, params.incubationTestSampleVolume_dft)
            f.write("wS:"+str(incubationTestSampleWaitTime))       #wait for X seconds
            f.write("\n")
            time = shared_funcs.get_est_runtime() + timepoint_samples * params.fillFilterTime + timepoint_samples * incubationTestSampleWaitTime
            shared_funcs.set_est_runtime(time)
    if volume_divided_evenly:
        print("SUBSAMPLE for all "+str(timepoint_samples)+ " is "+str(round(incubationTestSampleVolume,2)))

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
    time = shared_funcs.get_est_runtime() * positions
    shared_funcs.set_est_runtime(time)
    print("Estimated runtime in seconds is "+str(shared_funcs.get_est_runtime())+" seconds which is "+str(round(shared_funcs.get_est_runtime()/60,2))+" minutes")
    print("Ports in use are "+str(shared_funcs.get_stored_ports()))

#file generation   
os.chdir(os.path.dirname(os.path.abspath(__file__)))
filename = 'msconfig.cfg'

#main calls
with open(filename, "w") as f:
    print("#####################################")
    print("Initial configutation/first-time setup")
    print("#####################################")
    init_cfg()
    #print("Specify number of position to be collected, range is between "+str(params.filtrationPositions_min)+" and "+str(params.filtrationPositions_max)+". Default is "+str(params.filtrationPositions_dft))
    #positions = shared_funcs.int_check("experiments", params.filtrationPositions_min, params.filtrationPositions_max, params.filtrationPositions_dft)
    for x in range(positions):
        f.write("#POSITION "+str(x+1)+"\n")
        print(" ")
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
