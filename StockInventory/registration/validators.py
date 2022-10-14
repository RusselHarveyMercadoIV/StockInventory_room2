from django.forms import forms


def checkNumber(value):
    numbers = [str(digit) for digit in range(10)]
    if (value[0] == '+') and (len(value) == 13):
        for digit in value[1:]:
            if digit not in numbers:
                raise forms.ValidationError("This is not a Number!", code = "invalid_num")
    else:
        raise forms.ValidationError("Invalid Number!", code = "invalid_num")