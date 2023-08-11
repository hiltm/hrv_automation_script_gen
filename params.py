#### PARAMETER LIMITS ####
## initial setup ##
incubatorVolume_min = 0 #mL
incubatorVolume_max = 2000 #mL
incubatorVolume_dft = 2000 #mL
injectorVolume_min = 0 #mL
injectorVolume_max = 250 #mL
injectorVolume_dft = 0 #mL
studyCycles_min = 0
studyCycles_max = 5
studyCycles_dft = 1
## flush ##
flushCycles_min = 0
flushCycles_max = 5
flushCycles_dft = 1
flushWaittime_min = 5 #sec
flushWaittime_max = 300 #sec
flushWaittime_dft = 30 #sec
flushAmount_min = 0 #mL
flushAmount_max = 2000 #mL
flushAmount_dft = 2000 #mL
## incubation ##
incubationTestSampleCycles_min = 0
incubationTestSampleCycles_max = 50
incubationTestSampleCycles_dft = 1
incubationTestIncubatorDrawVolume_min = 0 #mL
incubationTestIncubatorDrawVolume_max = 2000 #mL
incubationTestIncubatorDrawVolume_dft = 1000 #mL
incubationTestInjectorDrawVolume_min = 0 #mL
incubationTestInjectorDrawVolume_max = 2000 #mL
incubationTestInjectorDrawVolume_dft = 0 #mLc
incubationTestWaitBetweenStudies_min = 0 #sec
incubationTestWaitBetweenStudies_max = 200000 #sec
incubationTestWaitBetweenStudies_dft = 100 #sec
incubationTestWaitValvePorts_min = 0 #sec
incubationTestValvePorts = []
incubationTestSsampleVolume = 0 #mL
incubationTestSsampleVolume_min = 0 #mL
incubationTestSsampleVolume_max = 500 #mL
incubationTestSsampleVolume_dft = 500 #mL
## wait for next study ##
studyCycleWaitTime_min = 0 #minutes
studyCycleWaitTime_max = 43800 #one month in minutes
studyCycleWaitTime_dft = 60 #one hour in minutes
## time estimates ##
emptyIncubationChamberTime = 30 #seconds
fillIncubationChamberTime = 120 #seconds
moveToPort = 60 #seconds
fillFilterTime = 60 #seconds