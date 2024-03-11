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
    print("hello world")

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
    print("Specify number of position to be collected, range is between "+str(params.filtrationPositions_min)+" and "+str(params.filtrationPositions_max)+". Default is "+str(params.filtrationPositions_dft))
    positions = shared_funcs.int_check("experiments", params.filtrationPositions_min, params.filtrationPositions_max, params.filtrationPositions_dft)
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
