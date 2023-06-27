import wikipedia

language = "ru"
wikipedia.set_lang(language)

user = input("Введи одним словом запрос: ")

result = wikipedia.summary(user)
print(result)


