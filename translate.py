message = " "
print("""which language do you want to translate?
        swedish - for swedish
        english - for english
        russian - for russian
        quit - to quit
        """)
def English ():
    print("Type the words you want to translate, and 'change' to change language")
    output = ""
    message = input("> ")
    kelime = message.split(' ')
    kelimeler = {
        "ben":"I",
        "sen":"you",
        "seni":"you",
        "seviyor":"love",
        "beni":"me",
        "anliyor":"understand",
        "katiliyor":"agree"
        }
    if message != "change":
        for word in kelime:
            output += kelimeler.get(word, word) + " "
        print(">" + output +" was your words")
        English()


def Swedish(output=" "):
    print("Type the words you want to translate, and 'change' to change language")
    message = input("> ")
    kelime = message.split(' ')
    kelimeler = {
        "ben": "jag",
        "sen": "du",
        "seni": "sig",
        "seviyor": "älskar",
        "beni": "mig",
        "anliyor": "förstår",
        "katiliyor": "håller med"
    }

    if message != "change":
        for word in kelime:
            output += kelimeler.get(word, word) + " "
        print(">" + output +" was your words")
        Swedish()


def Russian (output=" "):
    print("> Type the words you want to translate, and 'change' to change language")
    message = input("> ")
    kelime = message.split(' ')
    kelimeler ={
        "ben": "я",
        "sen": "вы",
        "beni": "я",
        "seni": "вы",
        "seviyor":"люблю",
        "anliyor":"понять",
        "katiliyor":"дать согласие"
    }
    if message != "change":
        for word in kelime:
            output += kelimeler.get(word, word) + " "
        print(">" + output +" was your words")
        Russian()


while True:
    print("choose language")
    message = input("> ").lower()
    if message =="swedish":
        Swedish()
    elif message =="russian":
        Russian()
    elif message== "english":
        English()
    elif message=="quit":
        break
    else:
        print("""which language do you want to translate?
                swedish - for swedish
                english - for English
                russian - for russian
                quit - to quit""")
