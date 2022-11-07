## https://www.geeksforgeeks.org/create-first-gui-application-using-python-tkinter/ as basis
## C:\Users\Michael\Documents\Repo\My Files\HRV GUI\>	python -m PyInstaller -c -F hrvGui.py


# Import Module
import tkinter as tk
from tkinter import ttk
from tkinter import LEFT,RIGHT
from tkinter.messagebox import askyesno
from tkinter.filedialog import asksaveasfile
#import configFileGenerator as cfg
import os.path

currRep = 0
numReps = 1


LARGEFONT =("Verdana", 35)
class tkinterApp(tk.Tk):
	
	# __init__ function for class tkinterApp
	def __init__(self, *args, **kwargs):
		
		# __init__ function for class Tk
		tk.Tk.__init__(self, *args, **kwargs)
		tk.Tk.title(self,'MS-SID Automation Configuration')
		#photo = 'C:\Users\Michael\Documents\Repo\My Files\HRV GUI\img\WHOIropelogo2020_Black.png'
		#tk.Tk.wm_iconbitmap(self, photo)

		# creating a container
		container = tk.Frame(self)
		container.pack(side = "top", fill = "both", expand = True)

		container.grid_rowconfigure(0, weight = 1)
		container.grid_columnconfigure(0, weight = 1)

		# initializing frames to an empty array
		self.frames = {}

		# iterating through a tuple consisting
		# of the different page layouts
		for F in (StartPage, createNewConfigFile, modifyExistingConfigFile, fileConfiguration, parameterTabs, confirmationWindow):

			frame = F(container, self)

			# initializing frame of that object from
			# startpage, createNewConfigFile, page2 respectively with
			# for loop
			self.frames[F] = frame

			frame.grid(row = 0, column = 0, sticky ="nsew")

		self.show_frame(StartPage)

	# to display the current frame passed as
	# parameter
	def show_frame(self, cont):
		frame = self.frames[cont]
		frame.tkraise()


#######################################################################################
#                                   Functions                                         #
#######################################################################################

def confirm(controller):			# TODO make this its own frame
    #answer = askyesno(title='Confirmation',
    #                message='Are you sure that you want to quit? All changes will be lost.')
    #print(answer)                
    #if answer:
	#command = lambda : tk.Tk.destroy # tk.Tk().withdraw() # controller.show_frame(StartPage)
	controller.show_frame(StartPage)

def save_file():
   f = asksaveasfile(initialfile = 'Untitled.txt',
defaultextension=".txt",filetypes=[("All Files","*.*"),("Text Documents","*.txt")])

def set_background_image(parent):
	my_path = os.path.abspath(os.path.dirname(__file__))
	icon = os.path.join(my_path, "img\WHOIropelogo2020_Black.ico")
	background_image=tk.PhotoImage(icon)
	background_label = tk.Label(parent, image=background_image)
	background_label.place(x=0, y=0, relwidth=1, relheight=1)

def set_num_reps(value):
	global numReps
	numReps = value

#######################################################################################
#                                   Root Window                                       #
#######################################################################################

class StartPage(tk.Frame):
	def __init__(self, parent, controller):
		set_background_image(parent)
		tk.Frame.__init__(self, parent)

		# label of frame Layout 2
		label = ttk.Label(self, text ="HRV Automation Configuration", font = LARGEFONT)

		# putting the grid in its place by using
		# grid
		label.grid(row = 0, column = 1, padx = 20, pady = 20)

		button1 = ttk.Button(self, text ="Create New Config File",
		command = lambda : controller.show_frame(createNewConfigFile))
	
		# putting the button in its place by
		# using grid
		button1.grid(row = 1, column = 1, padx = 20, pady = 20)

		## button to show frame 2 with text layout2
		button2 = ttk.Button(self, text ="Modify Existing Config File",
		command = lambda : controller.show_frame(modifyExistingConfigFile))
	
		# putting the button in its place by
		# using grid
		button2.grid(row = 2, column = 1, padx = 20, pady = 20)


#######################################################################################
#                            Cancel Confirmation Window                               #
#######################################################################################
class confirmationWindow(tk.Frame):		
	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
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
		label=ttk.Label(self, text ="Create New Config File", font = LARGEFONT)
		label.grid(row = 0, column = 1, padx = 10, pady = 10)

		button4=ttk.Button(self, text ="Save File Location", command = lambda : save_file())
		button4.grid(row = 1, column = 1, padx = 10, pady = 10)

		tk.Label(self, text="Save as a .cfg file").grid(row=1,column=2)

		# button to show frame 2 with text
		# layout2
		button1=ttk.Button(self, text ="Go Home", command = lambda : confirm(controller)) # TODO fix me
	
		# putting the button in its place
		# by using grid
		button1.grid(row = 2, column = 1, padx = 10, pady = 10)

		filepath = 'C:/Users/Michael/Documents/Repo/My Files/HRV GUI/'
		filename = 'test'
		completepath = os.path.join(filepath, filename+".txt")
		file1 = open(completepath, "w")
		toFile = "1"


		button2=ttk.Button(self, text ="Save and Close File", command = lambda : [
			file1.write(toFile),
			file1.close() ]
		)
		button2.grid(row = 5, column = 1, padx = 10, pady = 10)




		button3=ttk.Button(self, text ="Adjust Parameters", command = lambda : controller.show_frame(fileConfiguration))
		button3.grid(row = 6, column = 1, padx = 10, pady = 10)
		
  
		

#	def genConfig(self):
#		#cfg.generateConfigFile(self)
#		tk.Label(self, text="First Name").grid(row=0)
#		tk.Label(self, text="Last Name").grid(row=1)
#
#		e1 = tk.Entry(self)
#		e2 = tk.Entry(self)
#
#		e1.grid(row=2, column=1)
#		e2.grid(row=2, column=1)


#######################################################################################
#                            Modify Existing Config File                              #
#######################################################################################

# third window frame page2
class modifyExistingConfigFile(tk.Frame):
	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		label = ttk.Label(self, text ="Modify Existing Config File", font = LARGEFONT)
		label.grid(row = 0, column = 4, padx = 10, pady = 10)

		# button to show frame 2 with text
		# layout2
		button1 = ttk.Button(self, text ="Create New Config File",
							command = lambda : controller.show_frame(createNewConfigFile))
	
		# putting the button in its place by
		# using grid
		button1.grid(row = 1, column = 1, padx = 10, pady = 10)

		# button to show frame 3 with text
		# layout3
		button2 = ttk.Button(self, text ="Startpage",
							command = lambda : controller.show_frame(StartPage))
	
		# putting the button in its place by
		# using grid
		button2.grid(row = 2, column = 1, padx = 10, pady = 10)


#######################################################################################
#                            Parameter Tabs                              		 	  #
#######################################################################################

class parameterTabs(tk.Frame):
	def __init__(self, parent, controller):
		tk.Frame.__init__(self,parent)
	
		label=ttk.Label(self, text ="Configuration Parameters", font = LARGEFONT)
		#label.grid(row = 0, column = 1, padx = 10, pady = 10)

		tabControl = ttk.Notebook(self) 
		tab1 = ttk.Frame(tabControl)
		tab2 = ttk.Frame(tabControl)
		tab3 = ttk.Frame(tabControl)
		tab4 = ttk.Frame(tabControl)

		#for i in range(3):													# TODO replace hard-coded with numReps.get()
		tabControl.add(tab1, text ='Chamber Volume')
		tabControl.add(tab2, text ='Flushing')
		tabControl.add(tab3, text ='Sample Volume')
		tabControl.add(tab4, text ='Sample Ports and Timing')
		tabControl.pack(expand = 1, fill ="both")

		def increment_counter():
			global currRep
			currRep+=1
			repetitionLabel['text'] = 'Repetition # ' + str(currRep)

	
#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^#
#									Tab 1											 #
#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^#
		chamberVolumeLabelTabOne = tk.Label(tab1, text="Chamber Volume (mL):")
		chamberVolumeEntryTabOne = tk.Entry(tab1)
		tk.Label(tab1, text="Max is 2000mL").grid(row=0,column=2)

		buttonForward = tk.Button(tab1, text="Forward", command = lambda : tabControl.select(tab2))
		buttonBack = tk.Button(tab1, text="Back")

		sampleSizeLabelTabOne = tk.Label(tab1, text="How many samples to collect?")
		sampleSizeEntryTabOne = tk.Entry(tab1)
		#tk.Label(tab1, text="Max is 2000mL").grid(row=0,column=2)

		buttonForward = tk.Button(tab1, text="Forward", command = lambda : tabControl.select(tab2))
		buttonBack = tk.Button(tab1, text="Back")

		#repetitionLabelTabOne = tk.Label(tab1, text=("Repetition # " + str(currRep)))

		# === ADD WIDGETS TO GRID ON TAB ONE
		chamberVolumeLabelTabOne.grid(row=0, column=0)
		chamberVolumeEntryTabOne.grid(row=0, column=1)
		sampleSizeLabelTabOne.grid(row=1, column=0)
		sampleSizeEntryTabOne.grid(row=1, column=1)
		#repetitionLabelTabOne.grid(row=3, column=0)

		buttonForward.grid(row=2, column = 0, padx=15, pady=15)
		buttonBack.grid(row=2, column = 2, padx=15, pady=15)
				

#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^#
#									Tab 2											 #
#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^#
		flushVolumeTextTabTwo=tk.StringVar(tab2, "Enter flush volume (mL)")
		flushVolumeLabelTabTwo=tk.Label(tab2, textvariable=flushVolumeTextTabTwo).grid(row = 1, column = 1)

		directory=tk.StringVar(None)
		dirname=ttk.Entry(tab2,textvariable=directory,width=10)
		dirname.grid(row=1,column=2)	

		flushRepetitionsTextTabTwo=tk.StringVar(tab2, "Enter flush repetitions")
		flushRepetitionsLabelTabTwo=tk.Label(tab2, textvariable=flushRepetitionsTextTabTwo).grid(row = 2, column = 1)

		directory=tk.StringVar(None)
		dirname=ttk.Entry(tab2,textvariable=directory,width=10)
		dirname.grid(row=2,column=2)	

		buttonForward = tk.Button(tab2, text="Forward", command = lambda : tabControl.select(tab3))
		buttonBack = tk.Button(tab2, text="Back", command = lambda : tabControl.select(tab1))

		buttonForward.grid(row=4, column = 0, padx=15, pady=15)
		buttonBack.grid(row=4, column = 2, padx=15, pady=15)

#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^#
#									Tab 3											 #
#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^#	
		injectorVolumeTextTabThree=tk.StringVar(tab3, "Enter injector tracer volume (mL)")
		injectorVolumeLabelTabThree=tk.Label(tab3, textvariable=injectorVolumeTextTabThree).grid(row = 1, column = 1)

		directory=tk.StringVar(None)
		dirname=ttk.Entry(tab3,textvariable=directory,width=10)
		dirname.grid(row=1,column=2)

		sampleVolumeTextTabThree=tk.StringVar(tab3, "Enter sample volume (mL)")
		sampleVolumeLabelTabThree=tk.Label(tab3, textvariable=sampleVolumeTextTabThree).grid(row = 2, column = 1)

		directory=tk.StringVar(None)
		dirname=ttk.Entry(tab3,textvariable=directory,width=10)
		dirname.grid(row=2,column=2)

		buttonForward = tk.Button(tab3, text="Forward", command = lambda : tabControl.select(tab4))
		buttonBack = tk.Button(tab3, text="Back", command = lambda : tabControl.select(tab2))

		buttonForward.grid(row=3, column = 0, padx=15, pady=15)
		buttonBack.grid(row=3, column = 2, padx=15, pady=15)

#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^#
#									Tab 4											 #
#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^#

		sampleSizeTimeTabFour=tk.StringVar(tab4, "Enter Sample Start Time")
		sampleSizetimeLabelTabFour=tk.Label(tab4, textvariable=sampleSizeTimeTabFour).grid(row = 1, column = 1)
		tk.Label(tab4, text="Enter in military time e.g. 18:00").grid(row=1,column=3)

		directory=tk.StringVar(None)
		dirname=ttk.Entry(tab4,textvariable=directory,width=10)
		dirname.grid(row=1,column=2)

		samplePortsTextTabFour=tk.StringVar(tab4, "Enter Ports")
		samplePortsLabelTabFour=tk.Label(tab4, textvariable=samplePortsTextTabFour).grid(row = 2, column = 1)
		tk.Label(tab4, text="Enter even ports with commas e.g. 2,4,6").grid(row=2,column=3)

		directory=tk.StringVar(None)
		dirname=ttk.Entry(tab4,textvariable=directory,width=10)
		dirname.grid(row=2,column=2)

		sampleWaitTimesTextTabFour=tk.StringVar(tab4, "Enter between Samples")
		sampleWaitTimesLabelTabFour=tk.Label(tab4, textvariable=sampleWaitTimesTextTabFour).grid(row = 3, column = 1)
		tk.Label(tab4, text="Enter in seconds").grid(row=3,column=3)

		directory=tk.StringVar(None)
		dirname=ttk.Entry(tab4,textvariable=directory,width=10)
		dirname.grid(row=3,column=2)

		repetitionWaitTimesTextTabFour=tk.StringVar(tab4, "Time between next Sample Study")
		repetitionWaitTimesLabelTabFour=tk.Label(tab4, textvariable=repetitionWaitTimesTextTabFour).grid(row = 4, column = 1)
		tk.Label(tab4, text="Enter in seconds").grid(row=4,column=3)

		directory=tk.StringVar(None)
		dirname=ttk.Entry(tab4,textvariable=directory,width=10)
		dirname.grid(row=4,column=2)

		buttonForward = tk.Button(tab4, text="Forward", command = lambda : tabControl.select(tab1))
		buttonBack = tk.Button(tab4, text="Back", command = lambda : tabControl.select(tab3))

		buttonForward.grid(row=5, column = 0, padx=15, pady=15)
		buttonBack.grid(row=5, column = 2, padx=15, pady=15)


#######################################################################################
		spacerLabel = tk.Label(self, text=(""))																# TODO use this later, possibly for start time? runtime?
		spacerLabel.pack(expand=True, fill='none', side = LEFT)
		
		button2 = ttk.Button(self, text ="Repetition Confirmation", command = lambda : [increment_counter(),self.update()])
		button2.pack(expand = 1, side = LEFT)
		print(currRep)

		repetitionLabel = tk.Label(self, text=("Repetition # " + str(currRep)))
		repetitionLabel.pack(expand=True, fill='none', side = RIGHT)


		button2 = ttk.Button(self, text ="Cancel", command = lambda : controller.show_frame(confirmationWindow))
		button2.pack(expand = 1, side = RIGHT)

#######################################################################################
#                            File Configuration                              		  #
#######################################################################################

class fileConfiguration(tk.Frame):
	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		label=ttk.Label(self, text ="File Configuration", font = LARGEFONT)
		label.grid(row = 0, column = 1, padx = 10, pady = 10)

		userinput = 2																							# TODO fix entry of repetitions
		numRepsInput=tk.IntVar(None)
		dirname=ttk.Entry(label,numRepsInput.get(),width=10)
		dirname.grid(row=2,column=1)

		button3 = ttk.Button(self, text ="OK", command = lambda : set_num_reps(dirname.get()))
		button3.grid(row = 2, column = 5, padx = 20, pady = 20)

		tk.Label(self, text="Confirm system repetitions then click Continue").grid(row=3,column=1)
		button4 = ttk.Button(self, text ="Continue", command = lambda : controller.show_frame(parameterTabs)) # param_tab(self,parent,controller,numReps))
		button4.grid(row = 4, column = 1, padx = 20, pady = 20)

#######################################################################################
#                                    Run code                                         #
#######################################################################################
# Driver Code
app = tkinterApp()

my_path = os.path.abspath(os.path.dirname(__file__))
icon = os.path.join(my_path, "img\WHOIropelogo2020_Black.ico")
app.iconbitmap(icon)

app.mainloop()


