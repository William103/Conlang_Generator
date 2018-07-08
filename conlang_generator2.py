from random import *
import numpy as np


# Create Vowel class
class Vowel:
    def __init__(self, is_rounded, backness, height, is_nasal, is_vowel = True, is_consonant = False, is_voiced = True):
        self.is_rounded = is_rounded
        self.backness = backness
        self.height = height
        self.is_nasal = is_nasal
        self.is_consonant = is_consonant
        self.is_vowel = is_vowel
        self.is_voiced = is_voiced

    def __str__(self): # builds what character it should be based on characteristics
        return_val = ''
        if self.is_rounded:
            if self.backness == 'back' or self.backness == 'near_back':
                if self.height == 'open':
                    return_val = 'o'
                else:
                    return_val = 'u'
            if self.backness == 'central':
                return_val = 'ò'
            if self.backness == 'front' or 'near_front':
                if self.height == 'close':
                    return_val = 'û'
                else:
                    return_val = 'u'
        else:
            if self.backness == 'back' or self.backness == 'near_back':
                if self.height == 'open':
                    return_val = 'a'
                else:
                    return_val = 'u'
            if self.backness == 'central':
                if self.height == 'open':
                    return_val = 'é'
                if self.height == 'mid':
                    return_val = 'e'
                if self.height == 'close':
                    return_val = 'i'
            if self.backness == 'front' or self.backness == 'near_front':
                if self.height == 'close':
                    return_val = 'i'
                else:
                    return_val = 'æ'
        if self.is_nasal:
            if return_val == 'a':
                return_val = 'ä'
            if return_val == 'e':
                return_val = 'ë'
            if return_val == 'i':
                return_val = 'ï'
            if return_val == 'o':
                return_val = 'ö'
            if return_val == 'u':
                return_val = 'ü'
        return return_val

    def __repr__(self):
        return str(self)

# Create Consonant
class Consonant:
    def __init__(self, is_voiced, is_aspirated, place_of_articulation, type_of_articulation, is_ejective, is_lateral,
                 is_nasal, is_vowel = False, is_consonant = True):
        self.is_voiced = is_voiced
        self.is_aspirated = is_aspirated
        self.place_of_articulation = place_of_articulation
        self.type_of_articulation = type_of_articulation
        self.is_ejective = is_ejective
        self.is_lateral = is_lateral
        self.is_nasal = is_nasal
        self.is_consonant = is_consonant
        self.is_vowel = is_vowel

    def __str__(self): # builds what character it should be based on characteristics
        return_val = ''
        if self.type_of_articulation == 'plosive':
            if self.place_of_articulation == 'bilabial':
                if not self.is_voiced:
                    if not self.is_aspirated:
                        return_val = 'p'
                    else:
                        return_val = 'ph'
                else:
                    return_val = 'b'
            elif self.place_of_articulation == 'dental' or self.place_of_articulation == 'alveolar':
                if not self.is_voiced:
                    if not self.is_aspirated:
                        return_val = 't'
                    else:
                        return_val = 'th'
                else:
                    return_val = 'd'
            elif self.place_of_articulation == 'palatal':
                if not self.is_voiced:
                    if not self.is_aspirated:
                        return_val = 'c'
                    else:
                        return_val = 'ch'
                else:
                    return_val = 'j'
            elif self.place_of_articulation == 'velar':
                if not self.is_voiced:
                    if not self.is_aspirated:
                        return_val = 'k'
                    else:
                        return_val = 'kh'
                else:
                    return_val = 'g'
            elif self.place_of_articulation == 'uvular':
                if not self.is_voiced:
                    if not self.is_aspirated:
                        return_val = 'q'
                    else:
                        return_val = 'qh'
                else:
                    return_val = 'G'
            else:
                return_val = "'"
        if self.type_of_articulation == 'fricative':
            if self.place_of_articulation == 'bilabial':
                if not self.is_voiced:
                    return_val = 'w'
                else:
                    return_val = 'v'
                    if self.is_nasal:
                        return_val = 'm'
            elif self.place_of_articulation == 'dental':
                return_val = 'th'
            elif self.place_of_articulation == 'alveolar':
                if not self.is_voiced:
                    return_val = 's'
                else:
                    return_val = 'z'
                    if self.is_nasal:
                        return_val = 'n'
                    if self.is_lateral:
                        return_val = 'l'
            elif self.place_of_articulation == 'palatal':
                if not self.is_voiced:
                    return_val = 'ç'
                else:
                    return_val = 'y'
                    if self.is_nasal:
                        return_val = 'ñ'
            elif self.place_of_articulation == 'velar' or self.place_of_articulation == 'uvular':
                if not self.is_voiced:
                    return_val = 'x'
                else:
                    return_val = 'gh'
                    if self.is_nasal:
                        return_val = 'ng'
            else:
                return_val = 'h'
        if self.type_of_articulation == 'affricate':
            if self.place_of_articulation == 'dental' or self.place_of_articulation == 'alveolar':
                if not self.is_voiced:
                    if not self.is_aspirated:
                        return_val = 'ts'
                        if self.is_lateral:
                            return_val = 'tl'
                    else:
                        return_val = 'tsh'
                else:
                    return_val = 'dz'
                    if self.is_lateral:
                        return_val = 'dl'
            elif self.place_of_articulation == 'palatal':
                if not self.is_voiced:
                    if not self.is_aspirated:
                        return_val = 'ch'
                    else:
                        return_val = 'chh'
                else:
                    return_val = 'j'
            else:
                if not self.is_voiced:
                    if not self.is_aspirated:
                        return_val = 'qx'
                    else:
                        return_val = 'qxh'
        if self.is_ejective and self.place_of_articulation != 'glottal' and (
                self.type_of_articulation == 'plosive' or self.type_of_articulation == 'affricate') and self.is_voiced == False and return_val != '' and self.is_aspirated == False:
            return_val += "'"
        return return_val

    def __repr__(self):
        return str(self)

def list_of_objects_to_list_of_strings(raw): # because I'm lazy and don't want to type this out every time
    temp = []
    for thing in raw:
        temp.append(str(thing))
    return temp

# define 'stock' variables that I will then adjust
places_of_articulation = ['bilabial', 'dental', 'alveolar', 'palatal', 'velar', 'uvular', 'glottal']
types_of_articulation = ['plosive', 'fricative', 'ejective', 'affricate']
backnesses = ['front', 'near_front', 'central', 'near_back', 'back']
heights = ['close', 'mid', 'open']
is_voiced = [True, False]
is_aspirated = [True, False]
is_ejective = [True, False]
is_lateral = [True, False]
is_nasal = [True, False]
is_nasalized = [True, False]
is_rounded = [True, False]
cases = ['nominative', 'accusative', 'genitive', 'dative', 'locative', 'adpositional', 'ablative', 'instrumental', 'vocative', 'comitative']
numbers = ['singular', 'plural', 'dual', 'collective', 'paucal']
persons = ['first', 'second', 'third']
tenses = ['present', 'past', 'future', 'recent past', 'near future']
aspects = ['perfect', 'imperfect', 'progressive', 'habitual', 'stative', 'momentane', 'inceptive']
moods = ['indicative', 'subjunctive', 'optative', 'imperative']
parts_of_speech = ['noun', 'verb', 'adjective', 'adverb']
deriv_morph = []
vowel_harmony = ['is_rounded', 'backness', 'height']
consonant_attributes = ['place_of_articulation', 'type_of_articulation', 'is_voiced', 'is_nasal', 'is_lateral']
phonotactics = ['V']
stresses = ['initial', 'free', 'ultimate', 'penultimate', 'antipenultimate']
adpositions = ['circumposition', 'preposition', 'postposition']
morphological_typology = choice(['analytic', 'agglutinative', 'fusional'])
affixes = ['case', 'number', 'root', 'tense', 'aspect', 'mood', 'person']
vowels = []

# decide which distinctions our conlang will/won't make
print("Making Grammar and Phonology...")
stress = choice(stresses)
adposition = choice(adpositions)
# taking an axe to a bunch of these lists
while len(places_of_articulation) > randint(2, 8):
    del places_of_articulation[randint(0, len(places_of_articulation) - 1)]

while len(vowel_harmony) > randint(0, 2):
    del vowel_harmony[randint(0, len(vowel_harmony) - 1)]

while len(backnesses) > randint(2, 5):
    del backnesses[randint(0, len(backnesses) - 1)]

while len(heights) > randint(2, 8):
    del heights[randint(0, len(heights) - 1)]

while len(types_of_articulation) > randint(2, 5):
    del types_of_articulation[randint(0, len(types_of_articulation) - 1)]

# strategically taking an axe to these lists to avoid things like only having a comitative case or whatever
cases = cases[:randint(0, 11)]
for i in range(randint(0, int(len(cases) / 4))):
    del cases[randint(0, len(cases) - 1)]
if len(cases) == 0:
    cases.append('')
if 'nominative' in cases and 'accusative' in cases and randint(0, 1) == 1:
    cases.remove('nominative')
    cases.remove('accusative')
    cases.insert(0, 'ergative')
    cases.insert(0, 'absolutive')

aspects = aspects[:randint(0, 7)]
for i in range(randint(0, int(len(aspects) / 4))):
    del aspects[randint(0, len(aspects) - 1)]
if len(aspects) == 0:
    aspects.append('')

numbers = numbers[:randint(0, 6)]
for i in range(randint(0, int(len(numbers) / 4))):
    del numbers[randint(0, len(numbers) - 1)]
if len(numbers) == 0:
    numbers.append('')

persons = persons[:randint(0, 4)]
for i in range(randint(0, int(len(persons) / 4))):
    del persons[randint(0, len(persons) - 1)]
if len(persons) == 0:
    persons.append('')

tenses = tenses[:randint(0, 5)]
for i in range(randint(0, int(len(tenses) / 4))):
    del tenses[randint(0, len(tenses) - 1)]
if len(tenses) == 0:
    tenses.append('')

moods = moods[:randint(0, 5)]
for i in range(randint(0, int(len(moods) / 4))):
    del moods[randint(0, len(moods) - 1)]
if len(moods) == 0:
    moods.append('')

# more axing, this time of smaller lists
if randint(0, 1) == 1:
    is_aspirated = [False]
if randint(0, 1) == 1:
    is_ejective = [False]
if randint(0, 5) == 1:
    is_lateral = [False]
if randint(0, 5) == 1:
    is_nasal = [False]
if randint(0, 5) == 1:
    is_nasalized = [False]
if randint(0, 5) == 1:
    is_rounded = [False]

consonant_inventory = []

# come up with possible ways to change part of speech (e.g. noun->verb) or other basic derivational morphologies
for i in range(randint(0, 20)):
    deriv_morph.append(parts_of_speech[randint(0, len(parts_of_speech) - 1)] + ' to ' + parts_of_speech[
        randint(0, len(parts_of_speech) - 1)])
if randint(0, 1) == 1:
    deriv_morph.append("Agent")
if randint(0, 1) == 1:
    deriv_morph.append("Diminuitive")
if randint(0, 1) == 1:
    deriv_morph.append("Augmentative")
if randint(0, 1) == 1:
    deriv_morph.append("Comparative")
if randint(0, 1) == 1:
    deriv_morph.append("Superlative")
if randint(0, 1) == 1:
    deriv_morph.append("Negation")
if randint(0, 1) == 1:
    deriv_morph.append("Indefinite")
if randint(0, 1) == 1:
    deriv_morph.append("Definite")
if randint(0, 1) == 1:
    deriv_morph.append("Compound")

# syntax: literally just shuffles a list for the word order and decides if it should be head first or head final
word_order = ['subject', 'verb', 'oblique', 'direct object']
modifiers_before_word = True
shuffle(word_order)
if randint(0, 1) == 1:
    modifiers_before_word = False

# actually create list of consonants
for i in is_voiced:
    for j in is_aspirated:
        for k in places_of_articulation:
            for l in types_of_articulation:
                for m in is_ejective:
                    for n in is_lateral:
                        for o in is_nasal:
                            temp = Consonant(i, j, k, l, m, n, o)
                            if str(temp) == '' or str(temp) in list_of_objects_to_list_of_strings(consonant_inventory):
                                pass
                            else:
                                consonant_inventory.append(temp)

# now vowels
vowels = []
for i in is_nasalized:
    for j in is_rounded:
        for k in backnesses:
            for l in heights:
                temp = Vowel(j, k, l, i)
                if str(temp) == '' or str(temp) in list_of_objects_to_list_of_strings(vowels):
                    pass
                else:
                    vowels.append(temp)

# phonotactics: (C)V(C) type thing
initial_consonants = 0
final_consonants = 0
for i in range(randint(1, 5)):
    if randint(0, 1) == 1:
        phonotactics.append('(C)')
        final_consonants += 1
    else:
        phonotactics.insert(0, '(C)')
        initial_consonants += 1
print("Making Possible Clusters...")
# really ugly code to make possible consonant clusters
fricatives = []
for consonant in consonant_inventory:
    if consonant.type_of_articulation == 'fricative':
        fricatives.append(consonant)
word_initial = []
word_medial = []
word_final = []
for i in range(randint(initial_consonants * 3, initial_consonants * len(consonant_inventory) * 2)):
    if initial_consonants == 0:
        break
    length = randint(1, initial_consonants)
    word = []
    word.append(choice(consonant_inventory))
    if 'fricative' not in types_of_articulation:
        length = 1
    while len(word) < length:
        if word[-1].type_of_articulation == 'fricative':
            word.append(choice(consonant_inventory))
        else:
            word.append(choice(fricatives))
    word_initial.append(word)
temp2 = word_initial
for cluster in word_initial:
    temp = word_initial
    temp.remove(cluster)
    if cluster in temp:
        temp2.remove(cluster)
word_initial = temp2
for i in range(randint(0, initial_consonants * len(consonant_inventory) * 2) + 1):
    word_initial.append([''])

for i in range(randint((initial_consonants + final_consonants) * 3, (initial_consonants + final_consonants) * len(consonant_inventory) * 2)):
    length = randint(1, initial_consonants + final_consonants)
    word = []
    word.append(choice(consonant_inventory))
    if 'fricative' not in types_of_articulation:
        length = choice([1, 2])
    while len(word) < length:
        if word[-1].type_of_articulation == 'fricative' or len(word) == length - 1:
            word.append(choice(consonant_inventory))
        else:
            word.append(choice(fricatives))
    word_medial.append(word)
temp2 = word_medial
for cluster in word_medial:
    temp = word_medial
    temp.remove(cluster)
    if cluster in temp:
        temp2.remove(cluster)
word_medial = temp2
for i in range(randint(0, (initial_consonants + final_consonants) * len(consonant_inventory) * 2) + 1):
    word_medial.append([''])

for i in range(randint(final_consonants * 3, final_consonants * len(consonant_inventory) * 2)):
    if final_consonants == 0:
        break
    length = randint(1, final_consonants)
    word = []
    word.append(choice(consonant_inventory))
    if 'fricative' not in types_of_articulation:
        length = 1
    while len(word) < length:
        if word[-1].type_of_articulation == 'fricative':
            word.append(choice(consonant_inventory))
        else:
            word.append(choice(fricatives))
    word_final.append(word)
for i in range(randint(0, final_consonants * len(consonant_inventory) * 2) + 1):
    word_final.append([''])
temp2 = word_final
for cluster in word_final:
    temp = word_final
    temp.remove(cluster)
    if cluster in temp:
        temp2.remove(cluster)
word_final = temp2

# adding diphthongs
diphthongs = []
if randint(0, 1) == 1:
    for i in range(randint(0, 2*len(vowels))):
        diphthongs.append(sample(vowels, 2))
    for diphthong in diphthongs:
        if diphthong not in vowels:
            vowels.append(''.join(list_of_objects_to_list_of_strings(diphthong)))

# defining some functions I forgot about
def generate_word(syllables):
    word = []
    thing = choice(word_initial)
    if isinstance(thing, list):
        for letter in thing:
            word.append(letter)
    else:
        word.append(thing)
    thing = choice(vowels)
    if isinstance(thing, list):
        for letter in thing:
            word.append(letter)
    else:
        word.append(thing)
    for i in range(syllables - 1):
        thing = choice(word_medial)
        if isinstance(thing, list):
            for letter in thing:
                word.append(letter)
        else:
            word.append(thing)
        thing = choice(vowels)
        if isinstance(thing, list):
            for letter in thing:
                word.append(letter)
        else:
            word.append(thing)
    if len(word_final) != 0:
        thing = choice(word_final)
    else:
        thing = ['']
    if isinstance(thing, list):
        for letter in thing:
            word.append(letter)
    else:
        word.append(thing)
    return word

def flatten(word):
    if isinstance(word, list):
        if isinstance(word[0], list):
            temp = []
            for syllable in word:
                for letter in syllable:
                    temp.append(letter)
            return temp
        else:
            return word
    else:
        return word

# verb conjugation time
print("Conjugating Verbs...")
verb_endings = []
if morphological_typology == 'fusional':
    for i in numbers:
        for j in persons:
            for k in tenses:
                for l in moods:
                    for m in aspects:
                        verb_endings.append(''.join(list_of_objects_to_list_of_strings(generate_word(1))))
elif morphological_typology == 'agglutinative':
    for i in numbers:
        verb_endings.append(''.join(list_of_objects_to_list_of_strings(generate_word(1))))
    for i in persons:
        verb_endings.append(''.join(list_of_objects_to_list_of_strings(generate_word(1))))
    for i in tenses:
        verb_endings.append(''.join(list_of_objects_to_list_of_strings(generate_word(1))))
    for i in moods:
        verb_endings.append(''.join(list_of_objects_to_list_of_strings(generate_word(1))))
    for i in aspects:
        verb_endings.append(''.join(list_of_objects_to_list_of_strings(generate_word(1))))
elif morphological_typology == 'analytic':
    for i in numbers:
        verb_endings.append(''.join(list_of_objects_to_list_of_strings(generate_word(1))))
    for i in persons:
        verb_endings.append(''.join(list_of_objects_to_list_of_strings(generate_word(1))))
    for i in tenses:
        verb_endings.append(''.join(list_of_objects_to_list_of_strings(generate_word(1))))
    for i in moods:
        verb_endings.append(''.join(list_of_objects_to_list_of_strings(generate_word(1))))
    for i in aspects:
        verb_endings.append(''.join(list_of_objects_to_list_of_strings(generate_word(1))))

# whee, noun declension
print("Declining Nouns...")
noun_endings = []
if morphological_typology == 'fusional':
    for i in cases:
        for j in numbers:
            noun_endings.append(''.join(list_of_objects_to_list_of_strings(generate_word(1))))
elif morphological_typology == 'agglutinative':
    for i in cases:
        noun_endings.append(''.join(list_of_objects_to_list_of_strings(generate_word(1))))
elif morphological_typology == 'analytic':
    for i in cases:
        noun_endings.append(''.join(list_of_objects_to_list_of_strings(generate_word(1))))

# actually coming up with the derivational morphology
print("Coming up with Derivational Morphology...")
derivational_morphology = {}
if morphological_typology != 'analytic':
    for thing in deriv_morph:
        if randint(0, 1) == 1:
            if thing != 'Compound':
                derivational_morphology[thing] = ''.join(list_of_objects_to_list_of_strings(generate_word(1))) + '-'
            else:
                derivational_morphology[thing] = '-' + ''.join(list_of_objects_to_list_of_strings(generate_word(1))) + '-'
        else:
            if thing != 'Compound':
                derivational_morphology[thing] = '-' + ''.join(list_of_objects_to_list_of_strings(generate_word(1)))
            else:
                derivational_morphology[thing] = '-' + ''.join(list_of_objects_to_list_of_strings(generate_word(1))) + '-'
else:
    for thing in deriv_morph:
        derivational_morphology[thing] = ''.join(list_of_objects_to_list_of_strings(generate_word(1)))

# defining things that will be important soon
lexicon = {}
new_words = []

# copying dictionary of roots over to variable named english_words for historical reasons
with open(r"C:\Conlang_Generator\roots.txt", "r") as d:
    english_words = d.readlines()

tool = []
for root in english_words:
    tool.append(root.replace("\n", ''))
english_words = tool

total = len(english_words)
print("Generating Roots...")

# WOO! Generating words for every root in the dictionary
root_lexicon = {}
for root in english_words:
    root_lexicon[root.replace("\n", '')] = generate_word(1)

# going through the list of actual words and reconstructing them from roots, adding the roots in the new language to the new word
print("Putting Roots Together to Make Words...")
with open(r"C:\Conlang_Generator\dictionary.txt", "r") as d:
    real_words = d.readlines()
tool = []
for word in real_words:
    tool.append(word.replace("\n", ''))
real_words = tool

for word in real_words:
    reps = 0
    use_word = word
    recon = ""
    new_word = []
    if word in english_words:
        lexicon[word] = root_lexicon[word]
    else:
        while recon != word:
            for i in range(len(use_word) + 1):
                if use_word[:i] in english_words:
                    recon += use_word[:i + 1]
                    new_word.append(root_lexicon[use_word[:i]])
                    use_word = use_word[i + 1:]
                    break
            reps += 1
            if reps > 10:
                new_word.append(generate_word(randint(1, 2)))
                reps = 0
                recon = word
        letter = 0
        harmony_settings = []
        new_word = flatten(new_word)
        lexicon[word] = new_word
print("Done with Words...")

# converting everything to strings
print("Converting to Usable Format...")
consonant_inventory = list_of_objects_to_list_of_strings(consonant_inventory)
vowels = list_of_objects_to_list_of_strings(vowels)
for key in range(len(verb_endings)):
    verb_endings[key] = ''.join(list_of_objects_to_list_of_strings(verb_endings[key]))
for key in range(len(noun_endings)):
    noun_endings[key] = ''.join(list_of_objects_to_list_of_strings(noun_endings[key]))
for key in lexicon:
    lexicon[key] = ''.join(list_of_objects_to_list_of_strings(lexicon[key]))

# outputting everything to a document
print("Writing to Document...")
with open(r"C:\Conlang_Generator\Conlang_Dictionary.txt", "w") as f:
    f.write("A Complete Grammar and Dictionary of " + ''.join(list_of_objects_to_list_of_strings(generate_word(randint(1, 10)))).capitalize())
    f.write("\n" * 3)
    f.write("Morphology: \n" + "Typology: " + morphological_typology)
    if morphological_typology == 'fusional':
        f.write("\nVerbs Conjugation: \n")
        f.write("Infinitive: " + ''.join(list_of_objects_to_list_of_strings(generate_word(1))))
        f.write("\n")
        if len(verb_endings) > 0:
            ending = 0
            for i in numbers:
                for j in persons:
                    for k in tenses:
                        for l in moods:
                            for m in aspects:
                                f.write(i + ", " + j + ", " + k + ", " + l + ", " + m + ': ' + str(''.join(list_of_objects_to_list_of_strings(verb_endings[ending])) + '\n'))
                                ending += 1
                                if ending > len(verb_endings) - 1:
                                    break
                            if ending > len(verb_endings) - 1:
                                break
                        if ending > len(verb_endings) - 1:
                            break
                    if ending > len(verb_endings) - 1:
                        break
                if ending > len(verb_endings) - 1:
                    break
        f.write("\nNoun Declension: \n")
        ending = 0
        for i in numbers:
            for j in cases:
                f.write(i + ', ' + j + ', ' + ': ' + str(''.join(list_of_objects_to_list_of_strings(noun_endings[ending])) + '\n'))
                ending += 1
                if ending >= len(noun_endings) - 1:
                    break
    elif morphological_typology == 'agglutinative':
        f.write("\nInfinitive: " + ''.join(list_of_objects_to_list_of_strings(generate_word(1))) + "\n")
        shuffle(affixes)
        f.write("\nOrder of Affixes: " + '-'.join(affixes))
        f.write("\nNumbers: \n")
        for i in range(len(numbers)):
            f.write(numbers[i] + ": " + verb_endings[i] + "\n")
        f.write("\nPersons: \n")
        for i in range(len(persons)):
            f.write(persons[i] + ": " + verb_endings[i + len(numbers)] + "\n")
        f.write("\nTenses: \n")
        for i in range(len(tenses)):
            f.write(tenses[i] + ": " + verb_endings[i + len(numbers) + len(persons)] + "\n")
        f.write("\nMoods: \n")
        for i in range(len(moods)):
            f.write(moods[i] + ": " + verb_endings[i + len(numbers) + len(persons) + len(tenses)] + "\n")
        f.write("\nAspects: \n")
        for i in range(len(aspects)):
            f.write(aspects[i] + ": " + verb_endings[i + len(numbers) + len(persons) + len(tenses) + len(moods)] + "\n")
        f.write("\nCases: \n")
        for i in range(len(cases)):
            f.write(cases[i] + ": " + noun_endings[i] + "\n")
    elif morphological_typology == 'analytic':
        f.write("\nNumber particles: \n")
        for i in range(len(numbers)):
            f.write(numbers[i] + ": " + verb_endings[i] + "\n")
        f.write("\nPerson particles: \n")
        for i in range(len(persons)):
            f.write(persons[i] + ": " + verb_endings[i + len(numbers)] + "\n")
        f.write("\nTense particles: \n")
        for i in range(len(tenses)):
            f.write(tenses[i] + ": " + verb_endings[i + len(numbers) + len(persons)] + "\n")
        f.write("\nMood particles: \n")
        for i in range(len(moods)):
            f.write(moods[i] + ": " + verb_endings[i + len(numbers) + len(persons) + len(tenses)] + "\n")
        f.write("\nAspect particles: \n")
        for i in range(len(aspects)):
            f.write(aspects[i] + ": " + verb_endings[i + len(numbers) + len(persons) + len(tenses) + len(moods)] + "\n")
        f.write("\nCase particles: \n")
        for i in range(len(cases)):
            f.write(cases[i] + ": " + noun_endings[i] + "\n")
    if morphological_typology != "analytic":
        f.write("\nDerivational Morphology:\n")
    else:
        f.write("\nDerivational Particles:\n")
    for i in derivational_morphology:
        f.write(i + ': ' + str(''.join(list_of_objects_to_list_of_strings(derivational_morphology[i])) + '\n'))
    f.write("\nPhonology: \n \nConsonants: \n")
    f.write(', '.join(consonant_inventory))
    f.write("\nVowels: \n")
    f.write(', '.join(vowels))
    f.write("\nStress: " + stress)
    f.write("\n\nSyntax:\n")
    f.write(' - '.join(word_order) + '\n')
    if modifiers_before_word:
        f.write("Head Final")
    else:
        f.write("Head First")
    f.write("\nAdpositions: " + adposition)
    f.write("\n\nPhonotactics: \n")
    f.write(' '.join(phonotactics))
    f.write("\nWord Initial Clusters \n")
    for cluster in word_initial:
        if list_of_objects_to_list_of_strings(cluster) != ['']:
            f.write("".join(list_of_objects_to_list_of_strings(cluster)) + ", ")
    f.write("\nWord Medial Clusters \n")
    for cluster in word_medial:
        if list_of_objects_to_list_of_strings(cluster) != ['']:
            f.write("".join(list_of_objects_to_list_of_strings(cluster)) + ", ")
    f.write("\nWord Final Clusters \n")
    for cluster in word_final:
        if list_of_objects_to_list_of_strings(cluster) != ['']:
            f.write("".join(list_of_objects_to_list_of_strings(cluster)) + ", ")
    f.write("\n \nLexicon: \n")
    for word in lexicon:
        print_word = ''.join(list_of_objects_to_list_of_strings(lexicon[word]))
        f.write(word + ': ' + print_word + '\n')
print("Done!")
