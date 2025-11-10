import random


LETTER_SCORES = {'А': 1, 'Б': 3, 'В': 1, 'Г': 3, 'Д': 2, 'Е': 1, 'Ё': 3, 'Ж': 5, 'З': 5, 'И': 1, 'Й': 4, 'К': 2, 'Л': 2, 'М': 2, 'Н': 1, 'О': 1, 'П': 2, 'Р': 1, 'С': 1, 'Т': 1, 'У': 2, 'Ф': 10, 'Х': 5, 'Ц': 5, 'Ч': 5, 'Ш': 8, 'Щ': 10, 'Ъ': 10, 'О': 1, 'Ы': 4, 'Ь': 3, 'Э': 8, 'Ю': 8, 'Я': 3,}
def get_random_letter():
    all_keys = LETTER_SCORES.keys()
    converted_dictionary = list(all_keys)
    random_letter = random.choice(converted_dictionary)
    return random_letter


def get_word_with_letter(random_letter):
    while True:
        word = input(f"Введите слово на букву '{random_letter}': ").upper()
        if word[0] == random_letter:
            return word
        print(f"Слово должно начинаться на букву: '{random_letter}'. Попробуйте снова.")


def calculate_score(word):
    all_scores = []
    for letter in word:
        scores = LETTER_SCORES.get(letter, 0)
        all_scores.append(scores)
    sum_scores = sum(all_scores)
    return sum_scores


def main():
    random_letter = get_random_letter()
    print(f"Начальная буква: {random_letter}")
    print("Игрок 1")
    first_player_word = get_word_with_letter(random_letter)
    print("Игрок 2")
    second_player_word = get_word_with_letter(random_letter)
    first_player_scores = calculate_score(first_player_word)
    print(f"Игрок 1 ввел слово '{first_player_word}' и набрал {first_player_scores} очков.")
    second_player_scores = calculate_score(second_player_word)
    print(f"Игрок 2 ввел слово '{second_player_word}' и набрал {second_player_scores} очков.")
    if first_player_scores > second_player_scores:
        print("Игрок 1 победил!")
    elif second_player_scores > first_player_scores:
        print("Игрок 2 победил!")
    elif first_player_scores == second_player_scores:
        print("У вас ничья!")
    else:
        print("что-то произошло не так, сожелеем, попробуйте снова.")


if __name__ == '__main__':
    main()