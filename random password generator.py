import random
def gen_password(length=8):
    special_character=['!','@','#','$','%','&']
    
    upper=chr(random.randint(65,90))
    
    lower=chr(random.randint(97,122))
    
    special_char=random.choice(special_character)
    
    digit=random.randint(10000,99999)
    
    password=upper+lower+str(digit)+special_char
    
    return password
    
result=gen_password()
print(result)
