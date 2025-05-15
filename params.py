#### PARAMETER LIMITS ####
#### INCUBATION STUDY ####
## initial setup ##
deploymentWaitTime_min = 0 #min
deploymentWaitTime_max = 240 #min
deploymentWaitTime_dft = 0 #min
incubatorVolume_min = 0 #mL
incubatorVolume_max = 1950 #mL
incubatorVolume_dft = 1950 #mL
injectorVolume_min = 0 #mL
injectorVolume_max = 500 #mL
injectorVolume_dft = 500 #mL
incubatorPhysicalVolume_min = 0 #mL
incubatorPhysicalVolume_max = 1950 #mL
incubatorPhysicalVolume_dft = 1950 #mL
injectorPhysicalVolume_min = 0 #mL
injectorPhysicalVolume_max = 500 #mL
injectorPhysicalVolume_dft = 500 #mL
experiments_min = 0
experiments_max = 20
experiments_dft = 1
## flush ##
flushCycles_min = 0
flushCycles_max = 5
flushCycles_dft = 1
flushWaittime_min = 5 #sec
flushWaittime_max = 300 #sec
flushWaittime_dft = 30 #sec
flushAmount_min = 0 #mL
flushAmount_max = 1950 #mL
flushAmount_dft = 1950 #mL
## incubation ##
timepointSamples_min = 0
timepointSamples_max = 50
timepointSamples_dft = 1
incubationTestIncubatorDrawVolume_min = 0 #mL
incubationTestIncubatorDrawVolume_max = 1950 #mL
incubationTestIncubatorDrawVolume_dft = 1000 #mL
incubationTestInjectorDrawVolume_min = 0 #mL
incubationTestInjectorDrawVolume_max = 500 #mL
incubationTestInjectorDrawVolume_dft = 0 #mLc
waitTimeBetweenTimepointSamples_min = 0 #sec
waitTimeBetweenTimepointSamples_max = 200000 #sec
waitTimeBetweenTimepointSamples_dft = 100 #sec
incubationTestWaitValvePorts_min = 0 #sec
incubationTestValvePorts = []
incubationTestSsampleVolume = 0 #mL
incubationTestSampleVolume_min = 0 #mL
incubationTestSampleVolume_max = 500 #mL
incubationTestSampleVolume_dft = 500 #mL
## wait for the next position ##
incubationWaitTimeBetweenPositions_min = 0 #seconds
incubationWaitTimeBetweenPositions_max = 4800 #seconds
incubationWaitTimeBetweenPositions_dft = 500 #seconds
## wait for next study ##
experimentWaitTime_min = 0 #minutes
experimentWaitTime_max = 43800 #one month in minutes
experimentWaitTime_dft = 60 #one hour in minutes
## time estimates ##
emptyIncubationChamberTime = 30 #seconds
fillIncubationChamberTime = 120 #seconds
moveToPort = 60 #seconds
fillFilterTime = 60 #seconds
## filtration ##
filtrationPositions_min = 1
filtrationPositions_max = 49
filtrationPositions_dft = 4
filtrationSameVolume_min = 25 #mL
filtrationSameVolume_max = 3000 #mL
filtrationTracerSameVolume_dft = 50 #mL
filtrationTracerSameVolume_min = 0 #mL
filtrationTracerSameVolume_max = 500 #mL
filtrationSameVolume_dft = 500 #mL
filtrationSampleVolume_min = 25 #mL
filtrationSampleVolume_max = 5000 #mL
filtrationSampleVolume_dft = 500 #mL
filtrationTracerVolume_min = 0 #mL
filtrationTracerVolume_max = 500 #mL
filtrationTracerVolume_dft = 50 #mL
filtrationMicrogearPumpRate_min = 0 #mL/min
filtrationMicrogearPumpRate_max = 100 #mL/min
filtrationMicrogearPumpRate_dft = 100 #mL/min
filtrationMicrogearTimeout = 100 #seconds
filtrationMicrogearDirection_dft = 1 #1 forward, 0 reverse
## wait for the next position ##
filtrationWaitTimeBetweenPositions_min = 0 #seconds
filtrationWaitTimeBetweenPositions_max = 4800 #second
filtrationWaitTimeBetweenPositions_dft = 500 #seconds


#### POST-DIVE CLEANING ####
## wait to begin cleaning ##
cleaningWaitTime_min = 0 #min
cleaningWaitTime_max = 60 #min
cleaningWaitTime_dft = 0 #min
## wait for next study ##
rinseCycleWaitTime_min = 0 #minutes
rinseCycleWaitTime_max = 5 #minutes
rinseCycleWaitTime_dft = 1 #minutes