import re
import random


def make_train_data(filename):
    with open(filename, 'r') as file:
        content = file.read()

    haiku_list = content.split('\n\n')
    haiku_dict = {}
    train_set = ''
    for i in range(len(haiku_list) * 30):
        haiku_number = random.randint(0, len(haiku_list) - 1)
        plain = re.sub(r'[.,"\'-?:!;]', '', haiku_list[haiku_number]).lower()
        plain = ' '.join(plain.split())
        train_set = train_set + plain + ' '
    return train_set


if __name__=='__main__':
    print(make_train_data('train.txt'))
