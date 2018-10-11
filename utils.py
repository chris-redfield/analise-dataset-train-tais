file = open("data/stopwords.txt","r")
lines = file.readlines()
stop_words = []
for line in lines:
    stop_words.append(" " + line.replace('\n',''))

def remove_stop_words(text):
    for stop_word in stop_words:
        text = text.replace(stop_word," ")
    return text