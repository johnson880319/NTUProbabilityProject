from math import e
import numpy as np

class Agent(object):

    def __init__(self, N):

        '''
        parameters:
        ----------------------------------------------------------------------------
            N: how many values you can pick from
        ----------------------------------------------------------------------------
        Notice that the class is for the setting of basic-1 problem:
            You don’t know the distribution of the values.
        '''

        self.N = N

    def restart(self):

        '''
        Will be called when every simulation starts.
        Initialize all your variables here.

        '''

        self.count = 0
        self.standard = float('-inf')

    def decide(self, value):

        '''
        parameters:
        ----------------------------------------------------------------------------
            value: the new value you get; you will only get a value when the decide
            function is called once.
        return:
        ----------------------------------------------------------------------------
            a boolean; True if you want to pick the value or False otherwise.
        '''

        self.count += 1
        # The last value, you have no choice afterward
        if self.count >= self.N:
            return True
        
        if self.count * e < self.N:
            # Record the value
            self.standard = max(self.standard, value)
            # Return False for the first n/e values.
            return False

        return (value > self.standard)

# TODO: basic-2
class Basic_2_Agent(Agent):

    def __init__(self, N, k):

        '''
        parameters:
        ----------------------------------------------------------------------------
            N: how many values you can pick from
            k: you need to pick one of the top-k values
        ----------------------------------------------------------------------------
        Notice that the class is for the setting of basic-2 problem:
            You don’t know the distribution of the values, and you only need to 
            pick up one of the top-k values.
        '''

        self.N = N
        self.k = k

    def restart(self):

        '''
        Will be called when every simulation starts.
        Initialize all your variables here.

        '''
        # The same restart function as sample code in the basic-1 problem.
        super(Basic_2_Agent, self).restart()

    def decide(self, value):

        '''
        parameters:
        ----------------------------------------------------------------------------
            value: the new value you get; you will only get a value when the decide
            function is called once.
        return:
        ----------------------------------------------------------------------------
            a boolean; True if you want to pick the value or False otherwise.
        '''

        self.count += 1
        k_bound = 1+(self.k+self.k-3)/10*(0.1+abs(1-self.k/100))
        # The last value, you have no choice afterward
        if self.count >= self.N:
    	    return True

        if self.count * e * k_bound < self.N:
			# Record the value
            self.standard = max(self.standard, value)
			# Return False for the first N/(e*k_bound) values.
            return False

        return (value > self.standard)

# TODO: basic-3
class Basic_3_Agent(Agent):

    def __init__(self, N, k):

        '''
        parameters:
        ----------------------------------------------------------------------------
            N: how many values you can pick from
            k: how many values you can pick
        ----------------------------------------------------------------------------
        Notice that the class is for the setting of basic-3 problem:
            You don’t know the distribution of the values. You can pick at most k
            values, but you still need to pick out the best values.
        '''

        self.N = N
        self.k = k

    def restart(self):

        '''
        Will be called when every simulation starts.
        Initialize all your variables here.

        '''
        # The same restart function as sample code in the basic-1 problem.
        super(Basic_3_Agent, self).restart()

    def decide(self, value):

        '''
        parameters:
        ----------------------------------------------------------------------------
            value: the new value you get; you will only get a value when the decide
            function is called once.
        return:
        ----------------------------------------------------------------------------
            a boolean; True if you want to pick the value or False otherwise.
        '''

        # The same decide function as sample code in the basic-1 problem.
        self.count += 1
        # The last value, you have no choice afterward
        if self.count >= self.N:
            return True

        if self.count * self.k * (np.exp(1/self.k)) < self.N:
            # Record the value
            self.standard = max(self.standard, value)
            # Return False for the first n/(k*e^(1/k)) values.
            return False

        if value > self.standard:
            self.standard = value
            return True
        else:
            return False

# TODO: advanced-1-Uniform
class Advanced_1u_Agent(Agent):

    def __init__(self, N):

        '''
        parameters:
        ----------------------------------------------------------------------------
            N: how many values you can pick from
        ----------------------------------------------------------------------------
        Notice that the class is for the setting of advanced-1 problem:
            You know the distribution of the values is a uniform distribution, 
            but you don’t know the parameter of the distribution.
        '''

        self.N = N

    def restart(self):

        '''
        Will be called when every simulation starts.
        Initialize all your variables here.

        '''
        # The same restart function as sample code in the basic-1 problem.
        super(Advanced_1u_Agent, self).restart()

    def decide(self, value):

        '''
        parameters:
        ----------------------------------------------------------------------------
            value: the new value you get; you will only get a value when the decide
            function is called once.
        return:
        ----------------------------------------------------------------------------
            a boolean; True if you want to pick the value or False otherwise.
        '''

        # The same decide function as sample code in the basic-1 problem.
        return super(Advanced_1u_Agent, self).decide(value)

# TODO: advanced-1-Normal
class Advanced_1n_Agent(Agent):

    def __init__(self, N):

        '''
        parameters:
        ----------------------------------------------------------------------------
            N: how many values you can pick from
        ----------------------------------------------------------------------------
        Notice that the class is for the setting of advanced-1 problem:
            You know the distribution of the values is a normal distribution, 
            but you don’t know the parameter of the distribution.
        '''

        self.N = N

    def restart(self):

        '''
        Will be called when every simulation starts.
        Initialize all your variables here.

        '''
        # The same restart function as sample code in the basic-1 problem.
        super(Advanced_1n_Agent, self).restart()

    def decide(self, value):

        '''
        parameters:
        ----------------------------------------------------------------------------
            value: the new value you get; you will only get a value when the decide
            function is called once.
        return:
        ----------------------------------------------------------------------------
            a boolean; True if you want to pick the value or False otherwise.
        '''

        # The same decide function as sample code in the basic-1 problem.
        return super(Advanced_1n_Agent, self).decide(value)

# TODO: advanced-2
class Advanced_2_Agent(Agent):

    def __init__(self, N, k):

        '''
        parameters:
        ----------------------------------------------------------------------------
            N: how many values you can pick from
            k: the parameter of the given distribution
        ----------------------------------------------------------------------------
        Notice that the class is for the setting of advanced-2 problem:
            You know the distribution of the i-th value is a uniform distribution,
            U[i/kN, 1+i/kN].
        '''
        self.N = N
        self.k = k

    def restart(self):

        '''
        Will be called when every simulation starts.
        Initialize all your variables here.

        '''
        # The same restart function as sample code in the basic-1 problem.
        super(Advanced_2_Agent, self).restart()

    def decide(self, value):

        '''
        parameters:
        ----------------------------------------------------------------------------
            value: the new value you get; you will only get a value when the decide
            function is called once.
        return:
        ----------------------------------------------------------------------------
            a boolean; True if you want to pick the value or False otherwise.
        '''

        # The same decide function as sample code in the basic-1 problem.
        return super(Advanced_2_Agent, self).decide(value)