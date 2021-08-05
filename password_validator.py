from collections import Counter
import unittest


# Function to validate the password
def ChangePassword(passwd):
    SpecialSym = ['!', '@', '#', '$', '&', '*']
    value = True
    upper, lower, number, special, count, total = 0, 0, 0, 0, 0, 0

    if (passwd != ""):
        res = Counter(passwd)
        x = max(res, key=res.get)
        y = str(res[x])
        if y > '4':
            print()
            print('duplicate repeat characters more than 4')
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
        self.assertFalse(ChangePassword(''))
        print()
        print(".Password field cannot be empty")
        print()

    def test_too_short(self):
        self.assertFalse(ChangePassword('aAbB1!?'))
        print()

    def test_too_long(self):
        self.assertTrue(ChangePassword('zaqxswcdevfrBGTNHYMJUKILOp1234567890@#$&'))
        print("valid")
        print()

    def test_no_number(self):
        self.assertFalse(ChangePassword("zaqxscdevfrbgtnhyqw$$&"))
        print()

    def test_no_upper(self):
        self.assertFalse(ChangePassword("aabbzpoiuzqwetu123$"))
        print()

    def test_no_lower(self):
        self.assertFalse(ChangePassword("%&AABBCCQWERTYZX1234$"))
        print()

    def test_no_special(self):
        self.assertFalse(ChangePassword("aAbmMC19zaqxswASD123"))
        print()

    def test_duplicate_repeat(self):
        self.assertFalse(ChangePassword('aaaaaaaZAQXSWCDE1234#$'))
        print()

    def test_number_count(self):
        self.assertFalse(ChangePassword("qweTYnm12345689012#$$"))
        print()

    def test_more_then_4_sc(self):
        self.assertFalse(ChangePassword("qwertyPOIUYT12345#$#$#"))
        print()

    def test_sc_not_allowed(self):
        self.assertFalse(ChangePassword("qwertyPOIUYT12345@#%"))
        print()

    def test_valid(self):
        self.assertTrue(ChangePassword("qwertyPOIUYT12345@#$"))
        print("valid")
        print()


# Driver Code
if __name__ == '__main__':
    unittest.main()
