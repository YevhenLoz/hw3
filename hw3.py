# 1. Зформуйте строку, яка містить певну інформацію про символ в відомому слові.
# Наприклад "The [номер символу] symbol in [тут слово] is '[символ з відповідним порядковим номером]'".
# Слово та номер отримайте за допомогою input() або скористайтеся константою.
# Наприклад (слово - "Python" а номер символу 3) - "The 3 symbol in "Python" is 't' ".




user_word = 'Mouse'
user_idx = int(input(f'Enter number of symbol in \'{user_word}\':'))
print(f' The {user_idx} symbol in {user_word} is {user_word[user_idx - 1]}')


# 2. Написати цикл, який буде вимагати від користувача ввести слово, в якому є буква "о"
# (враховуються як великі так і маленькі).
# Цикл не повинен завершитися, якщо користувач ввів слово без букви о.
while True:
          userinput = input('Enter the word with letter o:')
          if userinput.__contains__('o') or userinput.__contains__('O'):
              print('Thnx!')
              break
          else:
              print('You entered word without letter "o"!')
