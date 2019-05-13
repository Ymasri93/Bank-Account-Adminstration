from django.core.exceptions import ValidationError
from django.forms import ModelForm

from bank_users.models import BankUser
import string

LETTERS = {ord(d): str(i) for i, d in enumerate(string.digits + string.ascii_uppercase)}


def _number_iban(iban):
    return (iban[4:] + iban[:4]).translate(LETTERS)


def generate_iban_check_digits(iban):
    number_iban = _number_iban(iban[:2] + '00' + iban[4:])
    return '{:0>2}'.format(98 - (int(number_iban) % 97))


def valid_iban(iban):
    return int(_number_iban(iban)) % 97 == 1


def has_numbers(inputString):
    return any(char.isdigit() for char in inputString)


class BankUserForm(ModelForm):
    class Meta:
        model = BankUser
        fields = ['first_name', 'last_name', 'iban']

    def clean(self):
        cleaned_data = super(BankUserForm, self).clean()

        first_name = cleaned_data.get('first_name')
        last_name = cleaned_data.get('last_name')
        iban = cleaned_data.get('iban').upper().replace(" ", "")

        if has_numbers(first_name):
            self.add_error(None, ValidationError('First Name field cannot contain any numbers'))
        if has_numbers(last_name):
            self.add_error(None, ValidationError('Last Name field cannot contain any numbers'))
        if not has_numbers(iban):
            self.add_error(None, ValidationError('IBAN field has to contain numbers'))
        if not (generate_iban_check_digits(iban) == iban[2:4] and valid_iban(iban)):
            self.add_error(None, ValidationError('The IBAN you entered is invalid'))
