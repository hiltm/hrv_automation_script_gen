import subprocess

valid_response = False

def print_valid_inputs():
    print("1 - incubation study")
    print("2 - filtration study")
    print("3 - post-swim clean script")

print(">>>>>>>>>>> HOW TO USE THIS SCRIPT <<<<<<<<<<<<<<<<")
print(" -  Please select the type of study to automate below")
print(" -  This will walk through various prompts for experiment control")
print(" -  Leaving blank and pressing Enter will use the default value")
print(" -  This will walk through various prompts for experiment control")
print(" -  The output is 'msconfig.cfg' This naming is unique to the PIC code")
print(" -  Utilize 'hrv_file_transfer' to send the automation script to the PIC")
print(">>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
print(" ")

print("Please select which automation script to generate")
print_valid_inputs()
#selection = cfgGen.int_check("selection", 0, 4, 0)

while not(valid_response):
    selection = input(": ")
    if selection == '1':
        valid_response = True
        subprocess.run(["python", "inc_study.py"])
    elif selection == '2':
        valid_response = True
        subprocess.run(["python", "filt_study.py"])
    elif selection == '3':
        valid_response = True
        subprocess.run(["python", "post_swim_clean.py"])
    else:
        print("Please enter a valid input")
        print_valid_inputs()
        continue