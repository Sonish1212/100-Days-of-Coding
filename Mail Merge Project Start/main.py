PLACEHOLDER = "[name]"
with open('E:\\from day 24 python\\Mail Merge Project Start\\Input\\Names\\invited_names.txt') as name_file:
    names = name_file.readlines()

with open('E:/from day 24 python/Mail Merge Project Start/Input/Letters/starting_letter.txt') as letter_file:
    letter = letter_file.read()

    for name in names:
        stripped_name = name.strip()
        new_letter = letter.replace(PLACEHOLDER, stripped_name)
        with open(f'E:\\from day 24 python\\Mail Merge Project Start\\Output\\ReadyToSend\\letter_for_{stripped_name}.txt', mode='w') as completed_letter:
            completed_letter.write(new_letter)






