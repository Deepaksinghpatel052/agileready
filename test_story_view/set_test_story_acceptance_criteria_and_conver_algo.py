import spacy
import re
# import en_core_web_sm
from textstat.textstat import textstatistics, easy_word_set, legacy_round


def break_sentences(text):
    nlp = spacy.load('en')
    # nlp = spacy.load('en_core_web_sm')
    doc = nlp(text)
    return doc.sents

# Returns Number of Words in the text
def word_count(text):
    words = len(text.split())
    # sentences = break_sentences(text)
    # words = 0
    # words_1 = 0
    # get_word = ""
    # for sentence in sentences:
    #     words += len([token for token in sentence])
    #     for token in sentence:
    #         words_1 += 1
    #         get_word += str(token)+" => "+str(words_1)+" || "
    return words

# Returns the number of sentences in the text
def sentence_count(text):
    sentences = break_sentences(text)
    words = 0
    for sentence in sentences:
        words += 1
    return words

# Returns average sentence length
def avg_sentence_length(text):
    words = word_count(text)
    sentences = sentence_count(text)
    average_sentence_length = float(words / sentences)
    average_sentence_length = round(average_sentence_length, 2)
    return average_sentence_length


# Textstat is a python package, to calculate statistics from
# text to determine readability,
# complexity and grade level of a particular corpus.
# Package can be found at https://pypi.python.org/pypi/textstat
def syllables_count(word):
    return textstatistics().syllable_count(word)



# Returns the average number of syllables per
# word in the text
def avg_syllables_per_word(text):
    word = text.lower()
    words = word_count(text)
    count = 0
    vowels = "aeiou"
    if word[0] in vowels:
        count += 1
    for index in range(1, len(word)):
        if word[index] in vowels and word[index - 1] not in vowels:
            count += 1
    if count == 0:
        count += 1
    syllables_data = count / words
    # syllable = syllables_count(text)
    # words = word_count(text)
    # ASPW = float(syllable) / float(words)
    return legacy_round(syllables_data, 2)



# Return total Difficult Words in a text
def difficult_words(text):
    # Find all words in the text
    words = []
    sentences = break_sentences(text)
    for sentence in sentences:
        words += [str(token) for token in sentence]

        # difficult words are those with syllables >= 2
    # easy_word_set is provide by Textstat as
    # a list of common words
    diff_words_set = set()
    for word in words:
        syllable_count = syllables_count(word)
        if word not in easy_word_set and syllable_count >= 2:
            diff_words_set.add(word)
    # return diff_words_set
    return len(diff_words_set)


# A word is polysyllablic if it has more than 3 syllables
# this functions returns the number of all such words
# present in the text
def poly_syllable_count(text):
    count = 0
    words = []
    sentences = break_sentences(text)
    for sentence in sentences:
        words += [token for token in sentence]
    for word in words:
        syllable_count = syllables_count(word)
        if syllable_count >= 3:
            count += 1
    return count


def flesch_reading_ease_conversations(text):
    """
        Implements Flesch Formula:
        Reading Ease score = 206.835 - (1.015 × ASL) - (84.6 × ASW)
        Here,
          ASL = average sentence length (number of words
                divided by number of sentences)
          ASW = average word length in syllables (number of syllables
                divided by number of words)
    """
    FRE = 206.835 - float(1.015 * avg_sentence_length(text)) -\
          float(84.6 * avg_syllables_per_word(text))
    return legacy_round(int(FRE))


def flesch_reading_ease(text):
    """
        Implements Flesch Formula:
        Reading Ease score = 206.835 - (1.015 × ASL) - (84.6 × ASW)
        Here,
          ASL = average sentence length (number of words
                divided by number of sentences)
          ASW = average word length in syllables (number of syllables
                divided by number of words)
    """
    FRE = 206.835 - float(1.015 * avg_sentence_length(text)) -\
          float(84.6 * avg_syllables_per_word(text))
    return legacy_round(int(FRE))

def flesch_grade_level(text):
    """
        Implements Flesch Formula:
        Reading Ease score = 206.835 - (1.015 × ASL) - (84.6 × ASW)
        Here,
          ASL = average sentence length (number of words
                divided by number of sentences)
          ASW = average word length in syllables (number of syllables
                divided by number of words)
    """
    FGL = float(0.39 * avg_sentence_length(text)) + float(11.8 * avg_syllables_per_word(text)) - 15.59
    return legacy_round(FGL, 2)


def coleman_liau_index(text):
    characters = len(re.sub("[^a-zA-Z]", "", text))
    sentences = sentence_count(text)
    words = word_count(text)
    CLI = float(5.89 * (characters/words)) - float(0.3 * (sentences/words)) - 15.8
    return legacy_round(CLI, 2)


def automated_readability_index(text):
    characters = len(re.sub("[^a-zA-Z]", "", text))
    sentences = sentence_count(text)
    words = word_count(text)
    ARI = float(4.71 * (characters/words)) + float(0.5 * (words/sentences)) - 21.43
    return legacy_round(ARI, 2)
