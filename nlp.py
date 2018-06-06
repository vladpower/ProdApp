import pymorphy2

morph = pymorphy2.MorphAnalyzer()

def get_normal(sentence):
        sentence=sentence.lower()
        words = sentence.split()
        new_sentece = ""
        for word in words:
            p = morph.parse(word)[0]
            if(new_sentece != ""):
                new_sentece+=" "
            new_sentece+=p.normal_form
        return new_sentece