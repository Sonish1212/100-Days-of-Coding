import pandas

nato_alphabet = pandas.read_csv('nato_phonetic_alphabet.csv')
nato_dict = {row.letter: row.code for (index, row) in nato_alphabet.iterrows()}
print(nato_dict)
is_matched = False
while not is_matched:
    user_input = input("Enter the word: ").upper()

    try:
        result = [nato_dict[words] for words in user_input]
    except KeyError:
        print("Sorry the value does not exist")

    else:
        print(result)
        is_matched = True
