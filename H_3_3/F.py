text = 'Мама мыла раму!'
print({i: text.lower().count(i) for i in text.casefold() if i.isalpha()})
text = '''Ехали медведи
На велосипеде.

А за ними кот
Задом наперёд.'''
print({i: text.lower().count(i) for i in text.casefold() if i.isalpha()})