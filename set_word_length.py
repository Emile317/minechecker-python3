import json

# set to True or False depending if you want the wordslist to be filtered
DONT_FILTER_BY_LENGTH = True

# set minimum and maximum word length here (both included)
SET_MIN_LENGTH_HERE = 3
SET_MAX_LENGTH_HERE = 20

with open('words_dictionary.json', 'r') as words_file:
    words_json = json.loads(words_file.read())

with open('words.txt', 'w') as output_file:
    for i, word in enumerate(words_json):
        if (len(word) >= SET_MIN_LENGTH_HERE and len(word) <= SET_MAX_LENGTH_HERE):
            output = word if i == len(words_json)-1 else f'{word}\n' # makes sure there's no newline at EOF
            output_file.write(output)
