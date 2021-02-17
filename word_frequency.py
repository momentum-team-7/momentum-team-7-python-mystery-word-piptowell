import operator

STOP_WORDS = [
    'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from', 'has', 'he',
    'i', 'in', 'is', 'it', 'its', 'of', 'on', 'that', 'the', 'to', 'were',
    'will', 'with'
]


def print_word_freq(file):
#1. open file and save it as a variable
    with open(file) as open_file:
        text = open_file.read()
        #3 get all text to lowercase
        text = text.lower()
        text_dict = {}
        #2 get rid of all punctuation in open_file
        text = text.replace(".","")
        text = text.replace(",","")
        text = text.replace("’","")
        text = text.replace(":","")
        text = text.replace("-"," ")
        text = text.replace("\n"," ")
        text = text.split(" ")
        text_list_copy = text.copy()
        
        for element in text:
            if element in STOP_WORDS:
                text_list_copy.remove(element)
            elif element not in text_dict:
                temporary_count = text_list_copy.count(element)
                text_dict[element] = temporary_count
        # print(text_dict)        

        sorted_values = dict(sorted(text_dict.items(), 
                        key=operator.itemgetter(1),
                        reverse = True))
        
        # print(sorted_values)

        for key, value in sorted_values.items():
            print(key," | ", value)
        






if __name__ == "__main__":
    import argparse
    from pathlib import Path

    parser = argparse.ArgumentParser(
        description='Get the word frequency in a text file.')
    parser.add_argument('file', help='file to read')
    args = parser.parse_args()

    file = Path(args.file)
    if file.is_file():
        print_word_freq(file)
    else:
        print(f"{file} does not exist!")
        exit(1)
