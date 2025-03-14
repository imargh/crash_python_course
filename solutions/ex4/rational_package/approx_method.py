import math
from .ex3_5_method import *

def continued_fraction(x, precision=1e-5):
        """A function that converts a number into a rational approximation using continued fractions.

    		Parameters
    		----------
   		 x : float 
       		 the value we want to convert

    		Returns
    		-------
    		: tuple
        		That contains the numerator and the denominator of
        """
        # Initialize numerators and denominators for the continued fraction
        a0 = math.floor(x)  # integer part
        x_i = x - a0        # x_1 = x - a_0, fractional part
        n_prev, n_curr = 1, a0  # n_0 = 1, n_1 = a_0, initialization
        d_prev, d_curr = 0, 1   # d_0 = 0, d_1 = 1
        
        # Check if the fractional part is already 0
        if x_i == 0:
            return a0, 1
    
    
        while True:
            # Compute a_i = floor(1 / x_i)
            a_i = math.floor(1 / x_i)
            
            # Update numerators and denominators
            n_i = a_i * n_curr + n_prev
            d_i = a_i * d_curr + d_prev
            
            # Check if the approximation is within the required precision
            if abs(n_i / d_i - x) < precision:
                break  # Stop if the difference is small enough
            
            # Update for the next iteration
            n_prev, n_curr = n_curr, n_i
            d_prev, d_curr = d_curr, d_i
            
            # Update x_i for the next step
            x_i = 1 / (x_i) - a_i
        
        n_s, d_s = simplify(n_i, d_i)
       
        return (n_s, d_s)

        
        
        
        
def simplify(num, denom):
    """A function that finds all the prime numbers up to a given value

    Parameters
    ----------
    n : int 
        the value up to which we find the prime numbers

    Returns
    -------
    : list
        a list with the prime numbers up to n
    """
    nfact = scomposition(num)
    dfact = scomposition(denom)
    
    common = []
    temp_list2 = dfact  # Copia per non modificare l'originale
    for elem in nfact:
        if elem in temp_list2:
            common.append(elem)
            temp_list2.remove(elem)
    
    
    # devo calcolare l'mcd
    if not common:
        return num, denom
    else:
        #fare qualcosa per semplificare
        gcd = 1
        for factor in common:
            gcd *= factor
            
        num = num / gcd
        denom = denom /gcd
        return num, denom

