MORSE_CODE_DICT = {'A': '.-', 'B': '-...',
                   'C': '-.-.', 'D': '-..', 'E': '.',
                   'F': '..-.', 'G': '--.', 'H': '....',
                   'I': '..', 'J': '.---', 'K': '-.-',
                   'L': '.-..', 'M': '--', 'N': '-.',
                   'O': '---', 'P': '.--.', 'Q': '--.-',
                   'R': '.-.', 'S': '...', 'T': '-',
                   'U': '..-', 'V': '...-', 'W': '.--',
                   'X': '-..-', 'Y': '-.--', 'Z': '--..',
                   '1': '.----', '2': '..---', '3': '...--',
                   '4': '....-', '5': '.....', '6': '-....',
                   '7': '--...', '8': '---..', '9': '----.',
                   '0': '-----', ', ': '--..--', '.': '.-.-.-',
                   '?': '..--..', '/': '-..-.', '-': '-....-',
                   '(': '-.--.', ')': '-.--.-', ' ': '......'}

direction = input("Enter if you want to encode or decode the text: ")
text = input("Enter the text or code you want to convert to: ").upper()

# for code in MORSE_CODE_DICT:
#     print(code)


def encode():
    list_text = []
    list_data = []
    for letters in text:
        list_text.append(letters)

    for item in list_text:
        for code in MORSE_CODE_DICT:
            str(code)
            if item in code:
                list_data.append(MORSE_CODE_DICT[code])

    print(list_text)
    word = ' '.join([str(data)for data in list_data])
    print(word)


def decode():
    output = ''
    morse_text = text.split(" ")

    for letters in morse_text:
        for key, value in MORSE_CODE_DICT.items():
            if value == letters:
                output += key + ' '
    print(output.lower())


if direction == 'e':
    encode()
elif direction == 'd':
    decode()
else:
    print("Type a  way you want to convert")
