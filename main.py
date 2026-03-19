from untils import is_very_long, has_digit, has_words, has_lowwer, has_upper, has_symbols

def main():
    password = input("Enter your password: ")
    functions = [is_very_long, has_digit, has_words, has_upper, has_lowwer, has_symbols]
    score = 0
    for func in functions:

        if func(password):
            score += 2
    print(score)


if __name__ == "__main__":
     main()