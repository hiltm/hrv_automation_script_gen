#import cfgGen
import params
import subprocess

print("Please select which automation script to generate")
print("1 - incubation study")
print("2 - filtration study")
print("3 - post-swim clean script")
#selection = cfgGen.int_check("selection", 0, 4, 0)
selection = input(": ")
if selection == '1':
    subprocess.run(["python", "inc_study.py"])
elif selection == '2':
    subprocess.run(["python", "filt_study.py"])
elif selection == '3':
    subprocess.run(["python", "post_swim_clean.py"])
#TODO handle any other inputs