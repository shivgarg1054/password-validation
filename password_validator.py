from collections import Counter
from logging import currentframe
import unittest
from fuzzywuzzy import fuzz

Current_Passwd = "zaqxswcdeVFRBGTMJU123456$$&"

def match_pwd(pwd):
    return pwd == get_current_pwd()

def get_current_pwd():
    return Current_Passwd

# Function to validate the password
def ChangePassword(Old_passwd, passwd):
    SpecialSym = ['!', '@', '#', '$', '&', '*']
    value = True
    upper, lower, number, special, count, total = 0, 0, 0, 0, 0, 0

    Ratio = fuzz.ratio(Old_passwd,passwd)

    if (Ratio >= 80):
        print(" old password is " + str(Ratio)+  "% match new password")
        return False

    if (passwd != ""):
        res = Counter(passwd)
        x = max(res, key=res.get)
        y = str(res[x])
        if y > '4':
            print()
            print('.duplicate repeat characters more than 4')
            return False
    
    if (passwd == ""):
        print("Password field cannot be empty")
        return False

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
        print("No more than 4 special characters")
        return False

    total = upper + lower + number + count

    if (len(passwd) - total != 0):
        print("invalid characters in password")
        return False

    if value:
        return value


# Main method
class ValidateTests(unittest.TestCase):

    def test_empty(self):
        self.assertFalse(ChangePassword(old_pass, ''))
        print()

    def test_too_short(self):
        self.assertFalse(ChangePassword(Current_Passwd, 'aAbB1!?'))
        print()

    def test_too_long(self):
        self.assertTrue(ChangePassword(Current_Passwd, 'zaqxswcdevfrBGTNHYMJUKILOp1234567890@#$&'))
        print("valid Password")
        print("Password is updated")
        print()

    def test_no_number(self):
        self.assertFalse(ChangePassword(Current_Passwd, "zaqxscdevfrbgtnhyqw$$&"))
        print()

    def test_no_upper(self):
        self.assertFalse(ChangePassword(Current_Passwd, "aabbzpoiuzqwetu123$"))
        print()

    def test_no_lower(self):
        self.assertFalse(ChangePassword(Current_Passwd, "%&AABBCCQWERTYZX1234$"))
        print()

    def test_no_special(self):
        self.assertFalse(ChangePassword(Current_Passwd, "aAbmMC19zaqxswASD123"))
        print()

    def test_duplicate_repeat(self):
        self.assertFalse(ChangePassword(Current_Passwd, 'aaaaaaaZAQXSWCDE1234#$'))
        print()

    def test_number_count(self):
        self.assertFalse(ChangePassword(Current_Passwd, "qweTYnm12345689012#$$"))
        print()

    def test_more_then_4_sc(self):
        self.assertFalse(ChangePassword(Current_Passwd, "qwertyPOIUYT12345#$#$#"))
        print()

    def test_sc_not_allowed(self):
        self.assertFalse(ChangePassword(Current_Passwd, "qwertyPOIUYT12345@#%"))
        print()

    def test_valid(self):
        self.assertTrue(ChangePassword(Current_Passwd, "qwertyPOIUYT12345@#$"))
        print("valid password")
        print("Password is Updated")
        print()

    def test_old_new_passmatch(self):
        self.assertFalse(ChangePassword(Current_Passwd,"ZAQxswcdeVFRBGTMJU123456$$&"))
        print()


# Driver Code
if __name__ == '__main__':
    old_pass = input("Enter the old password : ")
    value = match_pwd(old_pass)
    print(value)
    if value == True:
        unittest.main()
    else:
        print("please enter correct old password")