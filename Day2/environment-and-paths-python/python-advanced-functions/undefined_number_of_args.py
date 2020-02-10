
# Write a word count example for an undefined arguments using words.
# Example:
# >>> some_text = """When you look at the increasing sophistication of malware,
# it becomes apparent that you need to establish highly protected enclaves of
# data. The only way to achieve that is through modern encryption, properly
# implemented"""
# >>> func(some_text, "encryption", "science")
# >>> {"encryption": 1, "science": 0}

news_text = """Het Rijksmuseum in Amsterdam heeft een zeldzaam werk van
               Rembrandt-leerling Willem Drost in bruikleen gekregen van
               de Broere Charitable Foundation. Het gaat om Cimon en Pero,
               geschilderd omstreeks 1655. Het werk krijgt een plek op de
               Eregalerij, waar ook de Nachtwacht en de andere topstukken van
               het museum hangen. Van Willem Drost (1633-1659) zijn in totaal
               41 werken bekend. Na een opleiding in Amsterdam, vertrok hij
               naar Italië. Cimon en Pero schilderde hij rond zijn 22ste in
               Venetië. Het werd zijn grootste doek. Een paar jaar later
               stierf hij. Op Cimon en Pero is te zien hoe Drost de Hollandse
               manier van schilderen vermengt met Italiaanse invloeden.
               Het verhaal van Cimon en Pero stamt uit de Romeinse oudheid
               en gaat over ultieme opofferingsgezindheid en naastenliefde.
               Cimon is veroordeeld tot de hongerdood. Zijn dochter Pero
               bezoekt hem in de gevangenis en houdt hem in leven door hem
               stiekem de borst te geven."""


def simple_tokenizer(text):
    import re
    word_regex = re.compile(r"(\w+)")
    return re.findall(word_regex, text.lower())


def flexible_word_count(text, *args):
    tokenized_text = simple_tokenizer(text)
    word_dict = {}
    for word in tokenized_text:
        if word in args:
            word_dict.update({word: word_dict.get(word, 0) + 1})
    return word_dict


print(flexible_word_count(news_text, "hij", "geven"))
