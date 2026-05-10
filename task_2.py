import random
def get_numbers_ticket(min,max,quantity): 
    if min < 1 or max > 1000 or quantity > max - min +1:
        return [] 
    
    lotterry_num = random.sample(range(min, max+1), quantity)
    lotterry_num = sorted(lotterry_num)
    
   
    return lotterry_num

get_numbers_ticket(1,1000,9)