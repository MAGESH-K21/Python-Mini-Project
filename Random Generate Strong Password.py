import random
def gen_password(length=8):
    special_l=['!','@','#','$','%','&']
    upper=chr(random.randint(65,90))
    lower=chr(random.randint(97,122))
    special_char=random.choice(special_l)
    digit=random.randint(10000,99999)
    password=upper+lower+str(digit)+special_char
    l=random.sample(password,length)
    password=("").join(l)
    return password
result=gen_password()
print(result)