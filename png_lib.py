import math as m
import sys


def non_linear_generator(k: int, png_params = [11, 13, 17, 119], k0 = 19) -> int:
    """
    Description: algorithm work by phormula "ki=(a1*ki-1+a2*ki-1+b) mod c"
    
    :params: k          -- the sequence number of the generated number,
             png_params -- list of parameters pseudorandom number generator [a1, a2, b, c]
             k0         -- start element of sequence of pseudorandom numbers
    
    :return: pseudorandom number[k]
    """
    
    
    # init_params
    a1  = png_params[0]
    a2  = png_params[1]
    b   = png_params[2]
    c   = png_params[3]
    k_i = [k0] 
    
    #calculate
    for i in range(1, k+1):
        k_i.append((a1*k_i[-1]+a2*k_i[i-1]+b)%c)
    
    return k_i[i]
    
    
def linear_generator(k: int, png_params = [15, 13, 101], k0 = 10) -> int:
    """
    Description: algorithm work by phormula "ki=(a*k_i[-1]+b) mod c"
    
    :params: k          -- the sequence number of the generated number,
             png_params -- list of parameters pseudorandom number generator [a, b, c]
             k0         -- start element of sequence of pseudorandom numbers
    
    :return: pseudorandom number[k]
    """
    
    # init_params
    a   = png_params[0]
    b   = png_params[1]
    c   = png_params[2]
    k_i = [k0] 
    
    #calculate
    for i in range(1, k+1):
        k_i.append((a*k_i[i-1]+b)%c)
    
    return k_i[i]
    
    
def fib_generator(k: int, png_params = [5, 2], 
                  k_i = [0.94, 0.81, 0.12, 0.01, 0.09, 0.72]) -> int:
    """
    Description: algorithm work by phormula "k_i = k_i-a-k_i-b"
                 if k_i-a < k_i-b, then k_i+=1
                 
    :params: k          -- the sequence number of the generated number,
             png_params -- list of parameters pseudorandom number generator [a, b]
             k_i        -- start of sequence of pseudorandom numbers
    
    :return: pseudorandom number[k]
    """
    # init_params
    a=png_params[0]
    b=png_params[1]
    
    #calculate
    for i in range(a+1, k+1):
        k_calculate = k_i[i-a] - k_i[i-b]
        if (k_i[i-a] < k_i[i-b]):
            k_calculate += 1
        k_i.append(k_calculate)
        
    return k_i[k]


def BBS(k: int, png_params = [1019, 1031, 5]) -> int:
    """
    Description: algorithm work by phormula r"x_0^(2^n mod ((p-1)(q-1)) mod M",
                 where M = p*q
                 
    :params: k          -- the sequence number of the generated number,
             png_params -- list of parameters pseudorandom number generator [p, q, x_0]
    
    :return: pseudorandom number[k]
    """
    # init_params
    p   = png_params[0]
    q   = png_params[1]
    x_0 = png_params[2]
    
    #calculate
    M   = p*q
    sys.set_int_max_str_digits(10000)
    pow_value = int(m.pow(2,k)%((p-1)*(q-1)))
    x_k = (x_0**pow_value)%M
    sys.set_int_max_str_digits(4300)
    return x_k


if __name__ == "__main__":
    #example of usage
    #print(fib_generator(33))
    #print(non_linear_generator(33))
    #print(linear_generator(15)
    #print(BBS(33))
