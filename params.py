#### PARAMETER LIMITS ####
## initial setup ##
incubatorVolume_min = 0 #mL
incubatorVolume_max = 1950 #mL
incubatorVolume_dft = 1950 #mL
injectorVolume_min = 0 #mL
injectorVolume_max = 500 #mL
injectorVolume_dft = 0 #mL
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
## wait for next study ##
experimentWaitTime_min = 0 #minutes
experimentWaitTime_max = 43800 #one month in minutes
experimentWaitTime_dft = 60 #one hour in minutes
## time estimates ##
emptyIncubationChamberTime = 30 #seconds
fillIncubationChamberTime = 120 #seconds
moveToPort = 60 #seconds
fillFilterTime = 60 #seconds