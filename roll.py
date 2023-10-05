import random as r

def roll():
        die1 = r.randrange(1, 6)
        die2 = r.randrange(1, 6)
        die3 = r.randrange(1, 6)
        roll = die1 + die2 + die3
        return roll
def defRoll():
        roll()    
        defroll = roll
        return defroll
def atkRoll():
        roll()  
        atkroll = roll
        return atkroll
