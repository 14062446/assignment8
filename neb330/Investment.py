import numpy as np
import sys

class Investment(object):
    '''this class includes the functions and initialization method for the 
    list of positions and number of simulations that will be input by the user'''
    
    def __init__(self, positions, num_trials):
        '''Initializes the position list and number of simulations'''
        self.positions = positions
        self.position_vals = []
        self.num_trials = num_trials
        try:
            self.num_trials =  int(num_trials)
              
        except:
            raise TypeError
        else:
            if self.num_trials <= 0:
                raise ValueError  
            for i in self.positions:
                self.position_vals.append(int(i)/1000)
                    
    
    def generate_outcome(self, pos_val):
        '''generates the outcome of betting a total of $1000, given a position value
        ie. if the position value is 1, it generates the outcome of making 
        1000 bets of $1'''
        num_shares = 1000/pos_val
        n = 0
        sum = 0
        while n < num_shares:
            '''x represents a random number between 0 and 1, which simulates the 
            probability measure that the user wins the bet or loses the bet, based
            on the value of x'''
            x = np.random.random_sample()
            if x >= 0.51:
                sum = sum + (pos_val*2)
            n = n + 1
        return sum        

    def repeat_investment(self, pos_val):
        '''this function inputs a position value, and outputs a list of the return
         for each simulation (num_trials)'''
        position = 1000/pos_val
        daily_ret = []
        n = 0
        while n< self.num_trials:
            daily_ret.append((self.generate_outcome(pos_val)/1000.) - 1)
            n = n + 1
        return daily_ret    
             
        
        
                