<h2>Change password function<h2>
This change password function will just return True or False back to function caller to inform the caller whether the password can be changed successfully or not.

<h2>Validation Implemented</h2>

<ul>
<li>length should be at least 18</li>
          
<li>To Check Password should have at least one numeral</li>
          
<li>To Check Password should have at least one uppercase letter</li>
          
<li>To Check Password should have at least one lowercase letter</li>
          
<li>To check Password should have at least one of the symbols !@#$&*</li>

<li>To check 50 % of password should not be a number</li>

<li>To check No more than 4 special characters</li>

<li>To check No duplicate repeat characters more than 4</li>

</ul>

<h2>Usage</h2>

from password_validator import PasswordValidator

# Create a schema
Value = ChangePassword()

# Add properties to it
.min(18)\
.has().uppercase()\
.has().lowercase()\
.has().digits()\
.has().SpecialSymbol()\

# Validate against a password string
print(ChangePassword('validPASS123'));
# => True
print(ChangePassword('invalidPASS'));
# => False


<h2>Rules</h2>
Rules supported as of now are:

<table style="width:100%">
  <tr>
    <th>Rules</th>
    <th>Descriptions</th>
  </tr>
  <tr>
    <td>digits()</td>
    <td>specifies password must include digits</td>
  </tr>
  <tr>
    <td>letters()</td>
    <td>specifies password must include letters</td>
  </tr>
    <tr>
    <td>lowercase()</th>
    <td>specifies password must include lowercase letters</th>
  </tr>
  <tr>
    <td>uppercase()</td>
    <td>specifies password must include uppercase letters</td>
  </tr>
  <tr>
    <td>symbols()</td>
    <td>specifies password must include symbols</td>
  </tr>
      <tr>
    <td>len()</th>
    <td>length of password should be more then 18</th>
  </tr>
  <tr>
    <td>Counter in char.isdigit() </td>
    <td>To check 50 % of password should not be a number</td>
  </tr>
  <tr>
    <td>Counter(passwd)</td>
    <td>specifies password must include symbols</td>
  </tr>
  <tr>
    <td>Counter in symbols()</td>
    <td>not more than 4 special symbols</td>
  </tr>
</table>