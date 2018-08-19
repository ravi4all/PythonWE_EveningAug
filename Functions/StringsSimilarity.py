# jaccard distance = a & b / a | b

text_1 = "Python is an interpreted, object-oriented programming language similar to PERL, that has gained popularity because of its clear syntax and readability. Python is said to be relatively easy to learn and portable, meaning its statements can be interpreted in a number of operating systems, including UNIX-based systems, Mac OS, MS-DOS, OS/2, and various versions of Microsoft Windows 98. Python was created by Guido van Rossum, a former resident of the Netherlands, whose favorite comedy group at the time was Monty Python's Flying Circus. The source code is freely available and open for modification and reuse. Python has a significant number of users."
text_2 = "Python is a multiparadigm, general-purpose, interpreted, high-level programming language. Python allows programmers to use different programming styles to create simple or complex programs, get quicker results and write code almost as if speaking in a human language. Some of the popular systems and applications that have employed Python during development include Google Search, YouTube, BitTorrent, Google App Engine, Eve Online, Maya and iRobot machines. Python is an interpreted language, which precludes the need to compile code before executing a program because Python does the compilation in the background."

def formatWords(text):
    # Step 1 - Tokenization
    tokens = text.split()
    for i in range(len(tokens)):
        tokens[i] = tokens[i].lower()

    # Step 2 - Remove Stopwords
    stopwords = ['is','an','a','of','am','the','has','have','this','that',
                 'and','by','to', 'that', 'its', 'be', 'or', 'get', 'if',
                 'whose', 'at', 'in', 'for', 'can', 'as', 'was']

    words = []
    for word in tokens:
        if word not in stopwords:
            words.append(word)

    for i in range(len(words)):
        if words[i].endswith(","):
            words[i] = words[i].replace(",","")
        elif words[i].endswith("."):
            words[i] = words[i].replace(".","")

    return words


def calculateDistance(text_1, text_2):
    set_1 = set(formatWords(text_1))
    set_2 = set(formatWords(text_2))

    numer = set_1.intersection(set_2)
    denom = set_1.union(set_2)

    j = len(numer) / len(denom)

    print("Similarity is",j*100)
    print("Similar words",numer)

calculateDistance(text_1,text_2)
