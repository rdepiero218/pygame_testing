import secrets
import string
import random
padding = 6 # for the zeros
random_bytes = 12 # length of binary string

# alphabet = string.ascii_letters + string.digits + string.punctuation
alphabet = string.punctuation

def generate_fake_binary_dump(line_count, offset, word_list= None):
    word_dict = {}
    if word_list is not None:
        for word in word_list:
            #this deals with collisions by ruthless over writing
            word_dict[random.randint(0,line_count)] = word
            
    for x in range(line_count):
        random_data = ''.join(secrets.choice(alphabet) for i in range(random_bytes))
        if x in word_dict:
            # cut out the length of the word from the random characters
            random_data = random_data[len(word_dict[x]):]
            # split at a random point and add the word
            split_point = random.randint(0,len(random_data))

            random_data = random_data[split_point:] + word_dict[x] + random_data[-split_point:]

        # print(f'{x + offset:#0{padding}x} {random_data}')
        # print(f'{x + offset:#0{padding}X} {random_data} {x + offset + 100:#0{padding}X} {random_data}') 
        print(f'{x + offset:#0{padding}x} {random_data}') ## using X vs x after padding gives upper case in hex values
if __name__ == '__main__':

    word_list = ["WOMAN", "SUGAR", "IDIOT", "LAUGH", "APPLE", "QUEEN" ]
    generate_fake_binary_dump(32, 0x0990, word_list)