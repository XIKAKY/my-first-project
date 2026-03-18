password = input("Enter your password: ")

def is_very_long(lenght):
    return len(lenght) >= 12

def has_digit(word):
   return any(c.isdigit() for c in word)

def has_words(word):
    return any(c.isalpha() for c in word)

def has_lower(word):
    return any(c.islower() for c in  word)

def has_upper(word):
   return any(c.isupper() for c in word)

def has_symbols(digit):
    return "%" in digit or "#" in digit

functions = [is_very_long, has_digit, has_words, has_upper, has_lower, has_symbols]


def rating():
    score = 0
    for func in functions:

        if func(password):
            score += 2
    print(score)

if __name__ == "__main__":
    rating()
