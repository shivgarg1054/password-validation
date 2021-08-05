<h2>Change password function<h2>

<p>This change password function will just return True or False back to function caller to inform the caller whether the password can be changed successfully or not.</p>

<h2>USAGE</h2>

len(passwd) > 17
length should be at least 18
          
char.isdigit() for char in passwd
To Check Password should have at least one numeral
          
char.isupper() for char in passwd
To Check Password should have at least one uppercase letter
          
char.islower() for char in passwd
To Check Password should have at least one lowercase letter
          
char in SpecialSym for char in passwd
to check Password should have at least one of the symbols !@#$&*

Counter is used in char.isdigit() 
To check 50 % of password should not be a number

Counter is used in char in SpecialSym
To check No more than 4 special characters

res = Counter(passwd) Function is used
To check No duplicate repeat characters more than 4
