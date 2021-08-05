from collections import Counter
# Function to validate the password
def password_check(passwd):
    SpecialSym = ['!', '@', '#', '$', '&', '*']
    value = True

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
    count = 0
    for char in passwd:
        if (char.isdigit()):
            count = count + 1
        if count >= len(passwd)/2:
            print(count)
            return False
        else:
            value = True

    if not any(char.isupper() for char in passwd):
        print('Password should have at least one uppercase letter')
        return False

    if not any(char.islower() for char in passwd):
        print('Password should have at least one lowercase letter')
        return False

    if not any(char in SpecialSym for char in passwd):
        print('Password should have at least one of the symbols $@#')
        return False
    count = 0
    for char in passwd:
        if char in SpecialSym:
            count = count + 1
            print(count)

        if count > 4:
            print("sad")
            return False
        else:
            value = True

    if value:
        return value
# Main method
def main():
    passwd = 'zaq%qx$wC%EVF&12345#'

    if (password_check(passwd)):
        print("Password is valid")
    else:
        print("Invalid Password !!")


# Driver Code
if __name__ == '__main__':
    main()
