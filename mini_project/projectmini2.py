#CREATE A RANDOM PASSWORD USING LOOP

import random
import string

pass_len = 12
charvalues = string.ascii_letters + string.digits + string.punctuation

password = ""
for i in range(pass_len):
    password += random.choice(charvalues)

print("your password is : ", password)    


#CREATE A RANDOM PASSWORD USING LIST COMPREHENSION

import random
import string

pass_len = 12
charvalues = string.ascii_letters + string.digits + string.punctuation

password = "".join([random.choice(charvalues) for i in range(pass_len)])
print("your password is : ", password) 

 
