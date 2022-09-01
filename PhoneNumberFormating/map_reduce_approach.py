import re
phone_numbers = [
 "(123) 456-7890",
 "1234567890",
 "123.456.7890",
 "+1 123 456-7890"
]

class PhoneFormatter:
    def __init__(self):
        self.r = re.compile(r'\d')

    def transform(self, number: str) -> str:
        only_digits = self.r.findall(number)
        only_digits = ''.join(only_digits)
        area_code = only_digits[-10:-7]
        office_no = only_digits[-7:-4]
        subscriber_no = only_digits[-4:len(only_digits)]
        return f'({area_code}) {office_no}-{subscriber_no}'

formatter = PhoneFormatter()

clean_numbers = map(formatter.transform, phone_numbers)
print(list(clean_numbers))