import pandas as pd
import itertools


def format_list(l):
    return f'{", ".join(l[:-1])} and {l[-1]}' if len(l) > 1 else l[0]


def main():
    try:
        data = pd.read_csv("nato_phonetic_alphabet.csv")
        phonetics = {row.letter: list() for (_, row) in data.iterrows()}
        for (_, row) in data.iterrows():
            phonetics[row['letter']].append(row['code'])
        print(phonetics)
        letter = input("Enter a letter: ").upper()
        result = list(itertools.chain(*[phonetics[letter] for _ in letter]))
        print(format_list(result))
    except KeyError:
        print(f"{letter} is not in the dictionary.")


if __name__ == '__main__':
    main()
