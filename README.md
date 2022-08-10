# markov_haiku_generator
Генератор хокку на основе марковских цепей.
Идея взята из книги "Непрактичный Python" Ли Воган и адаптирована под особенности русского языка.
Чтобы сгенерировать хоккку, нужно запустить файл haiku_generator.py:
```
python3 haiku_generator.py
```
По умолчанию используется база хокку, собранная мной с помощью парсера parse.py с сайта japanpoetry.ru. Она находится в файле train.txt.
Можно и свою базу использовать, для этого в [haiku_generator.py](https://github.com/marydrobotun/markov_haiku_generator/blob/main/haiku_generator.py) в строке 14 передать путь к своему файлу.

Модуль [count_syllables.py](https://github.com/marydrobotun/markov_haiku_generator/blob/main/count_syllables.py) просто подсчитывает число слогов в русском слове.
