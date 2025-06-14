## Overview
This repo contains python scripts used to generate text files using unique syntax for commands related to automated deployment of an MS-SID instrument. See hrv repo for the microcontroller gear related to that instrument.  
## Building
python -m PyInstaller script.py  
## Installing
python -m auto_py_to_exe  
This will open a localhost in web browser  
Point to cfgGen.py in Script Location  
Point to either .ico image in the img folder for Icon  
Run Convert .py to .exe  
The generated files will appear in the output folder in the project directory  
## Operating the Script
To use the script, run the generated program.  
The terminal will prompt for various inputs.  
1. Not entering a value (e.g. hititng enter) will input a default value.  
2. Not entering an integer (e.g. entering a letter or character) will prompt the user to continue retrying submissions until an integer is submitted.  
Upon completion of the script a text file will be created at the path of the script.  
This script can then be transferred to the SD card on the MS-SID microcontroller board to allow for autonomous control.  

## Parameters
| Command | Parameter | Target | Function |
| --- | --- | --- | --- |
| VB: | 1 or 0 |  | Verbose operation 1=on, 0=off |
| IV: | nnn |  | Actual total incubator volume (mL) |
| TIM |  | SCB | Sets Mclane time and date from SCB |
| GSP |  | SID | Get a prompt from the SID |
| WHP |  | SCB | Wait for home port |
| PO: | nn (0…99) | SCB | Go to port nn, 0 to 99 |
| WA: | nnn | SCB | Wait for nnn minutes |
| WS: | nnn | SCB | Wait for nnn seconds |
| RP: | n | SCB | Repeat n times the instructions that follow until ERPN |
| ERPN |  | SCB | End the above numeric repeat loop |
| FV: | nnn | SID | Fill incubator nnn (mL) |
| FT: | nnn,tt | SID | Fill incubator nnn (mL) & tt volume tracer (mL) |
| EV: | nnn | SID | Empty incubator nnn (mL) |
| EP |  | SID | Completely empty incubator |
| IT: | SID | Inject incubator nnn (mL) tracer |
| END | SCB | The last command, ends the script |

# Exported Repo Path
https://git.whoi.edu/ms-sid/hrv_automation_script_gen