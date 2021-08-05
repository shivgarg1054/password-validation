from collections import Counter
# Function to validate the password
def password_check(passwd):
    SpecialSym = ['!', '@', '#', '$', '&', '*']
    value = True
    upper, lower, number, special, count, total = 0, 0, 0, 0, 0, 0

    res = Counter(passwd)
    x = max(res, key=res.get)
    print(x)
    print(str(res[x]))


    if len(passwd) < 17:
        print('length should be at least 18')
        return False

    if not any(char.isdigit() for char in passwd):
        print('Password should have at least one numeral')
        return False
    
    for char in range(len(passwd)):
        if passwd[char].isupper():
            upper += 1
        elif passwd[char].islower():
            lower += 1
        elif passwd[char].isdigit():
            number += 1
        else:
            special += 1 

    if (number >= len(passwd) / 2):
        print("To check 50 % of password should not be a number")
        return False

    if not any(char.isupper() for char in passwd):
        print('Password should have at least one uppercase letter')
        return False

    if not any(char.islower() for char in passwd):
        print('Password should have at least one lowercase letter')
        return False

    if not any(char in SpecialSym for char in passwd):
        print('Password should have at least one of the symbols $@#')
        return False

    for char in passwd:
        if char in SpecialSym:
            count = count + 1
        else:
            pass
    
    if (count > 4):
        return False

    total = upper + lower + number + count 

    if (len(passwd) - total != 0):
        print("invalid characters in password")
        return False

    if value:
        return value

# Main method
def main():
    passwd = 'zaqqx$wC$E%VF&12345#'

    if (password_check(passwd)):
        print("Password is valid")
    else:
        print("Invalid Password !!")


# Driver Code
if __name__ == '__main__':
    main()
