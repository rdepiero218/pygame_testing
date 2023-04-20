import secrets
import string
padding = 6
random_bytes = 40

alphabet = string.ascii_letters + string.digits + string.punctuation

def generate_fake_binary_dump(line_count, offset):
    for x in range(line_count):
        random_data = ''.join(secrets.choice(alphabet) for i in range(random_bytes))
        print(f'{x + offset:#0{padding}x} {random_data}')


if __name__ == '__main__':
    generate_fake_binary_dump(5, 0x0990)