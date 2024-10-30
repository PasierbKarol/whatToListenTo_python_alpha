import secrets
import string

def generate_random_number():
    # Use a probability to determine whether to generate 1-9 or 10-19
    if secrets.randbelow(10) < 7:  # 70% chance to generate 1-9
        return secrets.choice(range(1, 10))  # Random number between 1 and 9
    else:  # 20% chance to generate 10-19
        return secrets.choice(range(10, 20))  # Random number between 10 and 19
    
alphabet = string.ascii_uppercase
digits = string.digits[1:]

band_letter = ''.join(secrets.choice(alphabet) for _ in range(1))
band_number = str(generate_random_number())
album_number = str(generate_random_number())
print('Band starts with ' + band_letter + ', Band number is: ' + band_number + ', Album number is: ' + album_number)
