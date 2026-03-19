def is_very_long(lenght):
    return len(lenght) >= 12


def has_digit(word):
    return any(c.isdigit() for c in word)


def has_words(word):
    return any(c.isalpha() for c in word)


def has_lowwer(word):
    return any(c.islower() for c in word)


def has_upper(word):
    return any(c.isupper() for c in word)


def has_symbols(digit):
    return "%" in digit or "#" in digit


