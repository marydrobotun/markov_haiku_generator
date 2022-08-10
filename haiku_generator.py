"""Produce new haiku from training corpus of existing haiku."""
import logging
import sys

from make_train_data import make_train_data
from markov_haiku import prep_training, map_word_to_word, map_2_words_to_word, haiku_line



def main():
    """Give user choice of building a haiku or modifying an existing haiku."""
    print('\n\n Пожалуйста, подождите, компьютер обучается...\n\n')

    raw_haiku = make_train_data('train.txt')
    corpus = prep_training(raw_haiku)
    suffix_map_1 = map_word_to_word(corpus)
    suffix_map_2 = map_2_words_to_word(corpus)
    final = []

    choice = None
    while choice != "0":

        print(
            """
            Генератор хокку

            Нажмите 0, чтобы выйти
            Нажмите 1, чтобы сгенерировать новое хокку
            Нажмите 2, если хотите перегенерировать вторую строку 
            Нажмите 3, если хотите перегенерировать третью строку 

            """
        )

        choice = input("Введите команду: ")
        print()

        # exit
        if choice == "0":
            print("Sayonara.")
            sys.exit()

        # generate a full haiku
        elif choice == "1":
            final = []
            end_prev_line = []
            first_line, end_prev_line1 = haiku_line(suffix_map_1, suffix_map_2,
                                                    corpus, end_prev_line, 5)
            final.append(first_line)
            line, end_prev_line2 = haiku_line(suffix_map_1, suffix_map_2,
                                              corpus, end_prev_line1, 7)
            final.append(line)
            line, end_prev_line3 = haiku_line(suffix_map_1, suffix_map_2,
                                              corpus, end_prev_line2, 5)
            final.append(line)

        # regenerate line 2
        elif choice == "2":
            if not final:
                print("Сначала нужно сгенерировать хокку (Нажмите 1).")
                continue
            else:
                line, end_prev_line2 = haiku_line(suffix_map_1, suffix_map_2,
                                                  corpus, end_prev_line1, 7)
                final[1] = line

        # regenerate line 3
        elif choice == "3":
            if not final:
                print("Сначала нужно сгенерировать хокку (Нажмите 1).")
                continue
            else:
                line, end_prev_line3 = haiku_line(suffix_map_1, suffix_map_2,
                                                  corpus, end_prev_line2, 5)
                final[2] = line

        # some unknown choice
        else:
            print("\nЯ не знаю, что вы хотите.", file=sys.stderr)
            continue

        print(' '.join(final[0]))
        print(" ".join(final[1]))

        print(" ".join(final[2]))

    input("\n\nНажмите Enter для выхода.")


if __name__ == '__main__':
    main()
