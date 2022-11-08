## https://www.geeksforgeeks.org/create-first-gui-application-using-python-tkinter/ as basis
## C:\Users\Michael\Documents\Repo\My Files\HRV GUI\>	python -m PyInstaller -c -F hrvGui.py


# Import Module
import tkinter as tk
from tkinter import ttk
from tkinter import LEFT,RIGHT
from tkinter.messagebox import askyesno
from tkinter.filedialog import asksaveasfile
import os.path
from datetime import date

LARGEFONT =("Verdana", 35)
class tkinterApp(tk.Tk):
	
	# __init__ function for class tkinterApp
	def __init__(self, *args, **kwargs):
		
		# __init__ function for class Tk
		tk.Tk.__init__(self, *args, **kwargs)
		tk.Tk.title(self,'MS-SID Automation Configuration')
		self.shared_data = {
			"currRep" : 0,
			"numReps" : 1,
			"configFile" : '',
			"paramArray" : []
		}

		# creating a container
		container = tk.Frame(self)
		container.pack(side = "top", fill = "both", expand = True)

		container.grid_rowconfigure(0, weight = 1)
		container.grid_columnconfigure(0, weight = 1)

		# initializing frames to an empty array
		self.frames = {}

		# iterating through a tuple consisting of the different page layouts
		for F in (StartPage, createNewConfigFile, modifyExistingConfigFile, fileConfiguration, parameterTabs, confirmationWindow, repetitionSummary):
			frame = F(container, self)

			# initializing frame of that object from above tuple respectively with for loop
			self.frames[F] = frame

			frame.grid(row = 0, column = 0, sticky ="nsew")

		self.show_frame(StartPage)

	# to display the current frame passed as parameter
	def show_frame(self, cont):
		frame = self.frames[cont]
		frame.tkraise()


#######################################################################################
#                                   Functions                                         #
#######################################################################################

def save_file(self):
	#filepath = os.path.abspath(os.path.dirname(__file__))
	filename = 'MS-SID_Automation_Configuration_' + date.today().strftime("%Y-%m-%d")
	configfile = asksaveasfile(initialfile = filename + '.cfg',
		defaultextension=".cfg",filetypes=[("All Files","*.*"),("Text Documents","*.cfg")])
	self.controller.shared_data["configFile"] = configfile

def write_text(passed_string):
	global configfile
	f = open(configfile.name, "w")
	f.write(passed_string)


def set_background_image(parent):
	my_path = os.path.abspath(os.path.dirname(__file__))
	icon = os.path.join(my_path, "img\WHOIropelogo2020_Black.ico")
	background_image=tk.PhotoImage(icon)
	background_label = tk.Label(parent, image=background_image)
	background_label.place(x=0, y=0, relwidth=1, relheight=1)

def set_num_reps(self,value):
	self.controller.shared_data["numReps"] = value

#######################################################################################
#                                   Root Window                                       #
#######################################################################################

class StartPage(tk.Frame):
	def __init__(self, parent, controller):
		set_background_image(parent)
		tk.Frame.__init__(self, parent)
		self.controller=controller

		label = ttk.Label(self, text ="HRV Automation Configuration", font = LARGEFONT)
		label.grid(row = 0, column = 1, padx = 20, pady = 20)

		button1 = ttk.Button(self, text ="Create New Config File",
		command = lambda : controller.show_frame(createNewConfigFile))
		button1.grid(row = 1, column = 1, padx = 20, pady = 20)

		button2 = ttk.Button(self, text ="Modify Existing Config File",
		command = lambda : controller.show_frame(modifyExistingConfigFile))
		button2.grid(row = 2, column = 1, padx = 20, pady = 20)


#######################################################################################
#                            Cancel Confirmation Window                               #
#######################################################################################
class confirmationWindow(tk.Frame):		
	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		self.controller=controller


		label=ttk.Label(self, text ="Cancel Confirmation", font = LARGEFONT)
		label.grid(row = 0, column = 1, padx = 10, pady = 10)

		cancelConfirmationLabelTabOne = tk.Label(self, text="Are you sure that you would like to cancel?")

		buttonConfirm = tk.Button(self, text="Yes", command = lambda : controller.show_frame(StartPage))
		buttonDisagree = tk.Button(self, text="No", command = lambda : controller.show_frame(parameterTabs))

		cancelConfirmationLabelTabOne.grid(row=1, column=0)
		buttonConfirm.grid(row=2, column = 1, padx=15, pady=15)
		buttonDisagree.grid(row=2, column = 2, padx=15, pady=15)

#######################################################################################
#                               Create New Config File                                #
#######################################################################################

class createNewConfigFile(tk.Frame):
	def __init__(self, parent, controller):
		
		tk.Frame.__init__(self, parent)
		self.controller=controller

		label=ttk.Label(self, text ="Create New Config File", font = LARGEFONT)
		label.grid(row = 0, column = 1, padx = 10, pady = 10)

		button4=ttk.Button(self, text ="Save File Location", command = lambda : save_file(self))
		button4.grid(row = 1, column = 1, padx = 10, pady = 10)

		tk.Label(self, text="Save as a .cfg file").grid(row=1,column=2)

		button1=ttk.Button(self, text ="Go Home", command = lambda : controller.show_frame(StartPage))
		button1.grid(row = 2, column = 1, padx = 10, pady = 10)

		#button2=ttk.Button(self, text ="Save and Close File", command = lambda : [
		#	file1.write(toFile),
		#	file1.close() ]
		#)
		#button2.grid(row = 5, column = 1, padx = 10, pady = 10)

		button3=ttk.Button(self, text ="Adjust Parameters", command = lambda : controller.show_frame(fileConfiguration)) #TODO prevent button press without first save file location
		button3.grid(row = 6, column = 1, padx = 10, pady = 10)

#######################################################################################
#                            Modify Existing Config File                              #
#######################################################################################

# third window frame page2
class modifyExistingConfigFile(tk.Frame):
	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		self.controller=controller

		label = ttk.Label(self, text ="Modify Existing Config File", font = LARGEFONT)
		label.grid(row = 0, column = 4, padx = 10, pady = 10)

		button1 = ttk.Button(self, text ="Create New Config File",
							command = lambda : controller.show_frame(createNewConfigFile))
		button1.grid(row = 1, column = 1, padx = 10, pady = 10)

		button2 = ttk.Button(self, text ="Startpage",
							command = lambda : controller.show_frame(StartPage))
		button2.grid(row = 2, column = 1, padx = 10, pady = 10)

#######################################################################################
#                           	 Repetition Summary                            		  #
#######################################################################################

class repetitionSummary(tk.Frame):
	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		self.controller=controller

		#def increment_counter():
			#self.controller.shared_data["currRep"]+=1
			#repetitionLabel['text'] = 'Repetition # ' + str(currRep)

		label=ttk.Label(self, text ="Repetition Summary Confirmation", font = LARGEFONT)
		label.grid(row = 0, column = 0, padx = 10, pady = 10)

		cancelConfirmationLabelTabOne = tk.Label(self, text="Are you sure that you would like to continue to next repetition?")
		buttonConfirm = tk.Button(self, text="Yes", command = lambda : [write_text("Vb:1"),increment_counter(),controller.show_frame(parameterTabs)])
		buttonDisagree = tk.Button(self, text="No", command = lambda : controller.show_frame(StartPage))
		cancelConfirmationLabelTabOne.grid(row=1, column=0)
		buttonConfirm.grid(row=2, column = 0, padx=15, pady=15)
		buttonDisagree.grid(row=2, column = 1, padx=15, pady=15)														

#######################################################################################
#                            Parameter Tabs                              		 	  #
#######################################################################################

class parameterTabs(tk.Frame):
	def __init__(self, parent, controller):
		tk.Frame.__init__(self,parent)
		self.controller=controller
	
		label=ttk.Label(self, text ="Configuration Parameters", font = LARGEFONT)
		tabControl = ttk.Notebook(self) 
		tab1 = ttk.Frame(tabControl)
		tab2 = ttk.Frame(tabControl)
		tab3 = ttk.Frame(tabControl)
		tab4 = ttk.Frame(tabControl)

		tabControl.add(tab1, text ='Chamber Volume')
		tabControl.add(tab2, text ='Flushing')
		tabControl.add(tab3, text ='Sample Volume')
		tabControl.add(tab4, text ='Sample Ports and Timing')
		tabControl.pack(expand = 1, fill ="both")

		def increment_counter():
			self.controller.shared_data["currRep"]+=1
			repetitionLabel['text'] = 'Repetition # ' + str(self.controller.shared_data["currRep"])

	
#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^#
#									Tab 1											 #
#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^#
		chamberVolumeLabelTabOne = tk.Label(tab1, text="Chamber Volume (mL):") #TODO check for valid entry, complain if not valid
		chamberVolumeEntryTabOne = tk.Entry(tab1)
		tk.Label(tab1, text="Max is 2000mL").grid(row=0,column=2)

		buttonForward = tk.Button(tab1, text="Forward", command = lambda : tabControl.select(tab2))
		buttonBack = tk.Button(tab1, text="Back")

		sampleSizeLabelTabOne = tk.Label(tab1, text="How many samples to collect?") #TODO check for valid entry, complain if not valid
		sampleSizeEntryTabOne = tk.Entry(tab1)

		buttonForward = tk.Button(tab1, text="Forward", command = lambda : tabControl.select(tab2))
		buttonBack = tk.Button(tab1, text="Back")

		chamberVolumeLabelTabOne.grid(row=0, column=0)
		chamberVolumeEntryTabOne.grid(row=0, column=1)
		sampleSizeLabelTabOne.grid(row=1, column=0)
		sampleSizeEntryTabOne.grid(row=1, column=1)

		buttonForward.grid(row=2, column = 0, padx=15, pady=15)
		buttonBack.grid(row=2, column = 2, padx=15, pady=15)
				

#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^#
#									Tab 2											 #
#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^#
		flushVolumeTextTabTwo=tk.StringVar(tab2, "Enter flush volume (mL)") #TODO check for valid entry, complain if not valid
		flushVolumeLabelTabTwo=tk.Label(tab2, textvariable=flushVolumeTextTabTwo).grid(row = 1, column = 1)

		directory=tk.StringVar(None)
		flushVolumeEntryTabTwo=ttk.Entry(tab2,textvariable=directory,width=10)
		flushVolumeEntryTabTwo.grid(row=1,column=2)	

		flushRepetitionsTextTabTwo=tk.StringVar(tab2, "Enter flush repetitions") #TODO check for valid entry, complain if not valid
		flushRepetitionsLabelTabTwo=tk.Label(tab2, textvariable=flushRepetitionsTextTabTwo).grid(row = 2, column = 1)

		directory=tk.StringVar(None)
		flushRepetitionsEntryTabTwo=ttk.Entry(tab2,textvariable=directory,width=10)
		flushRepetitionsEntryTabTwo.grid(row=3,column=2)	

		buttonForward = tk.Button(tab2, text="Forward", command = lambda : tabControl.select(tab3))
		buttonBack = tk.Button(tab2, text="Back", command = lambda : tabControl.select(tab1))

		buttonForward.grid(row=4, column = 0, padx=15, pady=15)
		buttonBack.grid(row=4, column = 2, padx=15, pady=15)

#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^#
#									Tab 3											 #
#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^#	
		injectorVolumeTextTabThree=tk.StringVar(tab3, "Enter injector tracer volume (mL)") #TODO check for valid entry, complain if not valid
		injectorVolumeLabelTabThree=tk.Label(tab3, textvariable=injectorVolumeTextTabThree).grid(row = 1, column = 1)

		directory=tk.StringVar(None)
		injectorVolumeEntryTabThree=ttk.Entry(tab3,textvariable=directory,width=10)
		injectorVolumeEntryTabThree.grid(row=1,column=2)

		sampleVolumeTextTabThree=tk.StringVar(tab3, "Enter sample volume (mL)") #TODO check for valid entry, complain if not valid
		sampleVolumeLabelTabThree=tk.Label(tab3, textvariable=sampleVolumeTextTabThree).grid(row = 2, column = 1)

		directory=tk.StringVar(None)
		sampleVolumeEntryTabThree=ttk.Entry(tab3,textvariable=directory,width=10)
		sampleVolumeEntryTabThree.grid(row=2,column=2)

		buttonForward = tk.Button(tab3, text="Forward", command = lambda : tabControl.select(tab4))
		buttonBack = tk.Button(tab3, text="Back", command = lambda : tabControl.select(tab2))

		buttonForward.grid(row=3, column = 0, padx=15, pady=15)
		buttonBack.grid(row=3, column = 2, padx=15, pady=15)

#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^#
#									Tab 4											 #
#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^#

		sampleSizeTimeTabFour=tk.StringVar(tab4, "Enter Sample Start Time") #TODO check for valid entry, complain if not valid
		sampleSizetimeLabelTabFour=tk.Label(tab4, textvariable=sampleSizeTimeTabFour).grid(row = 1, column = 1)
		tk.Label(tab4, text="Enter in military time e.g. 18:00").grid(row=1,column=3)

		directory=tk.StringVar(None)
		sampleSizetimeEntryTabFour=ttk.Entry(tab4,textvariable=directory,width=10)
		sampleSizetimeEntryTabFour.grid(row=1,column=2)

		samplePortsTextTabFour=tk.StringVar(tab4, "Enter Ports") #TODO check for valid entry, complain if not valid
		samplePortsLabelTabFour=tk.Label(tab4, textvariable=samplePortsTextTabFour).grid(row = 2, column = 1)
		tk.Label(tab4, text="Enter even ports with commas e.g. 2,4,6").grid(row=2,column=3)

		directory=tk.StringVar(None)
		samplePortsEntryTabFour=ttk.Entry(tab4,textvariable=directory,width=10)
		samplePortsEntryTabFour.grid(row=2,column=2)

		sampleWaitTimesTextTabFour=tk.StringVar(tab4, "Enter between Samples") #TODO check for valid entry, complain if not valid
		sampleWaitTimesLabelTabFour=tk.Label(tab4, textvariable=sampleWaitTimesTextTabFour).grid(row = 3, column = 1)
		tk.Label(tab4, text="Enter in seconds").grid(row=3,column=3)

		directory=tk.StringVar(None)
		sampleWaitTimesEntryTabFour=ttk.Entry(tab4,textvariable=directory,width=10)
		sampleWaitTimesEntryTabFour.grid(row=3,column=2)

		repetitionWaitTimesTextTabFour=tk.StringVar(tab4, "Time between next Sample Study") #TODO check for valid entry, complain if not valid
		repetitionWaitTimesLabelTabFour=tk.Label(tab4, textvariable=repetitionWaitTimesTextTabFour).grid(row = 4, column = 1)
		tk.Label(tab4, text="Enter in seconds").grid(row=4,column=3)

		directory=tk.StringVar(None)
		repetitionWaitTimesEntryTabFour=ttk.Entry(tab4,textvariable=directory,width=10)
		repetitionWaitTimesEntryTabFour.grid(row=4,column=2)

		buttonForward = tk.Button(tab4, text="Forward", command = lambda : tabControl.select(tab1))
		buttonBack = tk.Button(tab4, text="Back", command = lambda : tabControl.select(tab3))

		buttonForward.grid(row=5, column = 0, padx=15, pady=15)
		buttonBack.grid(row=5, column = 2, padx=15, pady=15)

		parameterArray = [self.controller.shared_data["currRep"], chamberVolumeEntryTabOne.get(), sampleSizeEntryTabOne.get(), flushVolumeEntryTabTwo.get(), flushRepetitionsEntryTabTwo.get(),
		injectorVolumeEntryTabThree.get(), sampleVolumeEntryTabThree.get(), sampleSizetimeEntryTabFour.get(), samplePortsEntryTabFour.get(), sampleWaitTimesEntryTabFour.get(), repetitionWaitTimesEntryTabFour.get()]
		self.controller.shared_data["paramArray"] = parameterArray


#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^#
#								Bottom of Window									 #
#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^#
		spacerLabel = tk.Label(self, text=(""))																# TODO use this later, possibly for start time? runtime?
		spacerLabel.pack(expand=True, fill='none', side = LEFT)
		
		button2 = ttk.Button(self, text ="Repetition Confirmation", command = lambda : [increment_counter()]) # TODO go to summary window before confirming
		button2.pack(expand = 1, side = LEFT)

		repetitionLabel = tk.Label(self, text=("Repetition # " + str(self.controller.shared_data["currRep"])))
		repetitionLabel.pack(expand=True, fill='none', side = RIGHT)

		button2 = ttk.Button(self, text ="Cancel", command = lambda : controller.show_frame(confirmationWindow))
		button2.pack(expand = 1, side = RIGHT)

#######################################################################################
#                            File Configuration                              		  #
#######################################################################################

class fileConfiguration(tk.Frame):
	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		self.controller=controller


		label=ttk.Label(self, text ="File Configuration", font = LARGEFONT)
		label.grid(row = 0, column = 1, padx = 10, pady = 10)

		numRepsInput=tk.IntVar(None)
		dirname=ttk.Entry(label,numRepsInput.get(),width=10)
		dirname.grid(row=2,column=1)

		button3 = ttk.Button(self, text ="OK", command = lambda : set_num_reps(self,dirname.get()))
		button3.grid(row = 2, column = 5, padx = 20, pady = 20)

		tk.Label(self, text="Confirm system repetitions then click Continue").grid(row=3,column=1) #TODO check for valid entry, complain if not valid
		button4 = ttk.Button(self, text ="Continue", command = lambda : [controller.show_frame(parameterTabs)])
		button4.grid(row = 4, column = 1, padx = 20, pady = 20)

#######################################################################################
#                                    Run code                                         #
#######################################################################################
# Driver Code
app = tkinterApp()

# set application icon
my_path = os.path.abspath(os.path.dirname(__file__))
icon = os.path.join(my_path, "img\WHOIropelogo2020_Black.ico")
app.iconbitmap(icon)

app.mainloop()


