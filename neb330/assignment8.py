from Investment import Investment
import numpy as np
import matplotlib.pyplot as plt
import ast

'''Author: Nora Barry (neb330)'''

def main():
    
    '''This function will take the output from the user, test whether it's valid,
    and output the required histograms and statistical information'''    
    done = False
    while done == False:
        ValidInt = False
        ValidList = False
        
        while ValidList == False:
            '''Will run until user inputs a valid list. Note this program considers
            a valid list to be a list of numbers separated by commas, and enclosed 
            by brackets'''    
            try:
                input = raw_input("Enter a list of positions: ")
                if input in ['quit', 'quit()']:    
                    exit()
            except (KeyboardInterrupt, EOFError):
                continue
            else:      
                try:
                    position_list = ast.literal_eval(input)
                    instance = Investment(position_list, 1)
                    for i in position_list:
                        if 1000%i != 0:
                            raise ValueError
                        elif i <= 0:
                            raise ValueError 
                except ValueError:
                    print "Please enter a list of positive numbers that are factors of 1000."        
                except:
                    print "Please enter a valid list of numbers."
                else:                 
                    if len(position_list) < 2:
                        print "Please enter a list of more than one number."
                    else:
                        ValidList = True 

        while ValidInt == False and ValidList == True: 
            '''will run until the user inputs a valid number of simulations'''             
            try:
                num_trials = raw_input("Enter the number of trials you want to simulate: ")
                if num_trials in ['quit', 'quit()']:
                    exit()
            except (KeyboardInterrupt, EOFError):
                exit()
            else:     
                try:
                    instance = Investment(position_list, num_trials) 
                except ValueError:
                    print "Please enter an integer number greater than 0."         
                except TypeError:
                    print "Please enter an integer." 
                else:
                    ValidInt = True    
        if ValidInt == True and ValidList == True:  
                 
            for position in position_list:
                daily_ret = instance.repeat_investment(position)
                plt.hist(daily_ret, 100, range = [-1,1])
                plt.savefig('histogram_' + str(position)+ '.pdf')
                plt.close("all")
                
            #change the output to write to results.txt
            orig_stdout = sys.stdout
            f = file('results.txt', 'w')
            sys.stdout = f
            
            #iterate through position_list and output the mean and standard deviation for each
            for position in position_list:
                daily_ret = instance.repeat_investment(position)
                print "Position: ", position
                print "Mean: ", np.mean(daily_ret)
                print "Standard Deviation" , np.std(daily_ret)
                print "\n"
                done = True
            f.close()    
             
if __name__ == "__main__":
    main()      
            
    
