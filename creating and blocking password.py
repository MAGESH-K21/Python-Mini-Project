our_password="Abcd1234@"
your_answer=" "
number_of_try=0
number_max_of_try=5
max_try="Not Reached"

while your_answer!=our_password and max_try!="Reached":
    if number_of_try<number_max_of_try:
        your_answer=input("Enter password:\n")
        number_of_try=number_of_try+1
    else:
        max_try="Reached"


if max_try=="Reached":
    print("Account blocked! You Exceeded the Max Limit")
else:
    print("Access Granted")
