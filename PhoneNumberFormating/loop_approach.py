import re
phone_numbers = [
 "(123) 456-7890",
 "1234567890",
 "123.456.7890",
 "+1 123 456-7890"
]

number_extractor = re.compile(r'\d')
clean_numbers = []

for number in phone_numbers:
    only_digits = number_extractor.findall(number)
    only_digits = ''.join(only_digits)
    area_code = only_digits[-10:-7]
    office_no = only_digits[-7:-4]
    subscriber_no = only_digits[-4:len(only_digits)]
    clean_numbers.append(f'({area_code}) {office_no}-{subscriber_no}')

print(clean_numbers)