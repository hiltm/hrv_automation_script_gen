est_runtime = 0
stored_ports = []

def int_check(parameter, min_value, max_value, dft_value):
    valid_answer = False
    while not(valid_answer):
            number1 = input(': ') or dft_value
            try:
                number1 = int(number1)
            except:
                print("Integers only. No characters or letters allowed.")
                continue
            if (number1 < min_value) or (number1 > max_value):
                print("Input must be a number between " + str(min_value) + " and " + str(max_value))
                continue
            if not(isinstance(number1,int)):
                print(type(number1))
                print("Enter a number")
                continue
            else:
                valid_answer = True
                return number1
            
def port_selection(timepoint_samples, study_type):
    min_value = 2
    max_value = 98
    ports = []
    final_port = False
    if (study_type == 'incubation'):
        print("Select port positions for this timepoint sample. Even ports only for an incubation study. PORT0 is HOME. PORT98 is last available port.")
    else:
        print("Select port positions for this filtration study. Even ports only. PORT0 is HOME. PORT98 is last available port.")
    print("=====================================")
    #num_ports = int(input("Enter number of ports collecting samples for this study : "))
    num_ports = timepoint_samples

    if num_ports == 1: #handling for only one timepoint sample specified
        while not(final_port):
            port_selection = input("Enter port number for timepoint sample 1 : ")
            try:
                port_selection = int(port_selection)
            except:
                print("Integers only. No characters or letters allowed.")
                continue
            #print(check_port_usage(stored_ports,port_selection))
            if (port_selection < min_value) or (port_selection > max_value):
                print("Input must be a number between " + str(min_value) + " and " + str(max_value))
                continue
            elif port_selection in get_stored_ports():
                print("This port has already been used. Please select again.")
                continue
            elif not(port_selection % 2 == 0):
                if (study_type == 'incubation'):
                    print("Entry must be an even port to commence an incubation study")
                else:
                    print("Entry must be an even port")
                continue
            else:
                ports.append(port_selection) # add port to array for this study
                set_stored_ports(port_selection)  #set to global
                final_port = True # at the final port selection, exit loop
                break

    else:               #handling for any more than one timepoint samples
        for i in range(1, num_ports):
            while not(final_port):
                port_selection = input("Enter port number for timepoint sample "+str(i)+": ")
                try:
                    port_selection = int(port_selection)
                except:
                    print("Integers only. No characters or letters allowed.")
                    continue

                if (port_selection < min_value) or (port_selection > max_value):
                    print("Input must be a number between " + str(min_value) + " and " + str(max_value))
                    continue
                elif port_selection in get_stored_ports():
                    print("This port has already been used. Please select again.")
                    continue
                elif not(port_selection % 2 == 0):
                    if (study_type == 'incubation'):
                        print("Entry must be an even port to commence an incubation study")
                    else:
                        print("Entry must be an even port")
                    continue
                else:
                    ports.append(port_selection) # add port to array for this timepoint
                    set_stored_ports(port_selection)  #set to global
                    if i == num_ports:
                        final_port = True # at the final port selection, exit loop
                        break
                    else:
                        i = i + 1 # go to next port selection
    return ports
            
def set_intake(x):
     global intake
     intake = x

def get_intake():
     return intake

def set_outtake(x):
     global outtake
     outtake = x

def get_outtake():
     return outtake

def set_est_runtime(x):
    global est_runtime
    est_runtime = x

def get_est_runtime():
    return est_runtime

def set_stored_ports(x):
    stored_ports.append(x)

def get_stored_ports():
    return stored_ports

def check_port_usage(stored_ports, port_request):

    if port_request not in stored_ports:
        stored_ports.append(port_request)
        return True
    else:
        print("This port already in use!")
        return False


def yes_or_no():
    valid_answer = False
    while not(valid_answer):
        user_input = input('(y)es or (n)o: ')
        if user_input.lower() == 'yes' or user_input.lower() == 'y':
            var = True
            valid_answer = True
        elif user_input.lower() == 'no' or user_input.lower() == 'n':
            var = False
            valid_answer = True
        else:
            print('Type (y)es or (n)o')
            continue
    return var