# a - " Brute Force Approach "
def bin_dec(n):
    result = 0
    for i in range( 0 , len(str(n))):
            if int(str(n)[i]) == 0 or int(str(n)[i]) == 1:
                s = (int(str(n)[i]))*(2**((len(str(n))) - (i + 1)))
                result += s
            else:
                raise ValueError        
    print(result)                     


bin_dec(10011100)


# b - Built- in py fn 
print(int('10011100' , 2))
            

            
