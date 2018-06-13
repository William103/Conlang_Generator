from random import randint
from random import shuffle


# Create Vowel class for vowel harmony and assimilation
class Vowel:
    def __init__(self, is_rounded, backness, height, is_nasal, is_vowel = True, is_consonant = False, is_voiced = True):
        self.is_rounded = is_rounded
        self.backness = backness
        self.height = height
        self.is_nasal = is_nasal
        self.is_consonant = is_consonant
        self.is_vowel = is_vowel
        self.is_voiced = is_voiced

    def __str__(self):
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
                    return_val = 'y'
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

# Create Consonant class for assimilation
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

    def __str__(self):
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

def remove_duplicates(raw):
    temp = raw
    for thing in temp:
        if str(thing) == '':
            temp.remove(thing)
    i, j = 0, 0
    while i < len(temp)-1:
        while j < len(temp)-1:
            if str(temp[i]) == str(temp[j]):
                del temp[i]
                del temp[j]
            j += 1
        i += 1
        j = 0
    return temp

def list_of_objects_to_list_of_strings(raw):
    temp = raw
    for i in range(len(raw)):
        temp[i] = str(raw[i])
    return temp

# define 'stock' variables
places_of_articulation = ['bilabial', 'dental', 'alveolar', 'palatal', 'velar', 'uvular', 'glottal']
types_of_articulation = ['plosive', 'fricative', 'ejective', 'affricate']
vowels = ['a', 'e', 'i', 'o', 'u']
backnesses = ['front', 'near_front', 'central', 'near_back', 'back']
heights = ['close', 'mid', 'open']
is_voiced = [True, False]
is_aspirated = [True, False]
is_ejective = [True, False]
is_lateral = [True, False]
is_nasal = [True, False]
is_nasalized = [True, False]
is_rounded = [True, False]
cases = ['nominative', 'accusative', 'vocative', 'instrumental', 'dative', 'ablative', 'genitive']
numbers = ['singular', 'dual', 'plural', 'collective']
persons = ['first', 'second', 'third']
tenses = ['present', 'preterite', 'imperfect', 'future', 'perfect', 'progressive']
moods = ['indicative', 'subjunctive', 'optative', 'imperative']
parts_of_speech = ['noun', 'verb', 'adjective', 'adverb']
deriv_morph = []
vowel_harmony = ['is_rounded', 'backness', 'height']
consonant_attributes = ['place_of_articulation', 'type_of_articulation', 'is_voiced', 'is_nasal', 'is_lateral']

# decide which distinctions our conlang will/won't make
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

while len(vowels) > randint(2, 6):
    del vowels[randint(0, len(vowels) - 1)]

while len(cases) > randint(0, 8):
    del cases[randint(0, len(cases) - 1)]
if len(cases) == 0:
    cases.append('')

while len(numbers) > randint(0, 5):
    del numbers[randint(0, len(numbers) - 1)]
if len(numbers) == 0:
    numbers.append('')

while len(persons) > randint(0, 4):
    del persons[randint(0, len(persons) - 1)]
if len(persons) == 0:
    persons.append('')

while len(tenses) > randint(0, 7):
    del tenses[randint(0, len(tenses) - 1)]
if len(tenses) == 0:
    tenses.append('')

while len(moods) > randint(0, 5):
    del moods[randint(0, len(moods) - 1)]
if len(moods) == 0:
    moods.append('')

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

for i in range(randint(0, 20)):
    deriv_morph.append(parts_of_speech[randint(0, len(parts_of_speech) - 1)] + ' to ' + parts_of_speech[
        randint(0, len(parts_of_speech) - 1)])

# phonotactics
probability_of_init_plosive = randint(1, 100)
probability_of_init_fricative = randint(1, 100)
probability_of_double_vowel = randint(1, 100)
probability_of_fin_fricative = randint(1, 100)
probability_of_fin_plosive = randint(1, 100)

if randint(1, 3) == 1:
    probability_of_init_plosive = 0
if randint(1, 3) == 1:
    probability_of_init_fricative = 0
if randint(1, 3) == 1:
    probability_of_double_vowel = 0
if randint(1, 3) == 1:
    probability_of_fin_fricative = 0
if randint(1, 3) == 1:
    probability_of_fin_plosive = 0

# syntax
word_order = ['subject', 'verb', 'indirect object', 'direct object']
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
                            consonant_inventory.append(Consonant(i, j, k, l, m, n, o))

vowels = []
for i in is_nasalized:
    for j in is_rounded:
        for k in backnesses:
            for l in heights:
                vowels.append(Vowel(j, k, l, i))

consonant_inventory = remove_duplicates(consonant_inventory)
vowels = remove_duplicates(vowels)

# setup for generating words
if 'plosive' or 'ejective' in types_of_articulation:
    plosives = []
    for letter in consonant_inventory:
        if letter.type_of_articulation == 'plosive' or letter.type_of_articulation == 'ejective' or \
                letter.type_of_articulation == 'affricate':
            plosives.append(letter)
    has_plosives = True
else:
    has_plosives = False
    plosives = []
if 'fricative' in types_of_articulation:
    has_fricatives = True
    fricatives = [letter for letter in consonant_inventory if (letter.type_of_articulation == 'fricative')]
else:
    has_fricatives = False
    fricatives = []
for letter in plosives:
    if plosives.count(letter) > 1:
        reps = plosives.count(letter)
        for i in range(reps - 1):
            plosives.remove(letter)

if has_fricatives:
    for letter in fricatives:  # remove duplicates
        if fricatives.count(letter) > 1:
            reps = fricatives.count(letter)
            for i in range(reps - 1):
                fricatives.remove(letter)

for letter in plosives:
    if plosives.count(letter) > 1:
        plosives.remove(letter)
if has_fricatives:
    for letter in fricatives:
        if fricatives.count(letter) > 1:
            fricatives.remove(letter)


def generate_word(syllables, plosive_1, plosive_2, fricative_1, fricative_2, vowel_1, vowel_2):
    word = []

    for index in range(syllables):
        if randint(1, 100) < probability_of_init_plosive:
            word.append(plosive_1)
        if has_fricatives:
            if randint(1, 100) < probability_of_init_fricative:
                word.append(fricative_1)
        if randint(0, 1) < probability_of_double_vowel:
            word.append(vowel_1)
        else:
            word.append(vowel_1)
            word.append(vowel_2)
        if has_fricatives:
            if randint(1, 100) < probability_of_fin_fricative:
                word.append(fricative_2)
        if randint(1, 100) < probability_of_fin_plosive:
            word.append(plosive_2)

    return word

def flatten(word):
    temp = []
    for syllable in word:
        for letter in syllable:
            temp.append(letter)
    return temp

# verb conjugation time
verb_endings = []
for i in numbers:
    for j in persons:
        for k in tenses:
            for l in moods:
                new_ending = ''.join(list_of_objects_to_list_of_strings(generate_word(1, plosives[randint(0, len(plosives) - 1)],
                                           plosives[randint(0, len(plosives) - 1)],
                                           fricatives[randint(0, len(fricatives) - 1)],
                                           fricatives[randint(0, len(fricatives) - 1)],
                                           vowels[randint(0, len(vowels) - 1)], vowels[randint(0, len(vowels) - 1)])))
                if new_ending not in verb_endings:
                    verb_endings.append(new_ending)

# whee, noun declension
noun_endings = []
for i in cases:
    for j in numbers:
        new_ending = ''.join(list_of_objects_to_list_of_strings(generate_word(1, plosives[randint(0, len(plosives) - 1)], plosives[randint(0, len(plosives) - 1)],
                                   fricatives[randint(0, len(fricatives) - 1)],
                                   fricatives[randint(0, len(fricatives) - 1)], vowels[randint(0, len(vowels) - 1)],
                                   vowels[randint(0, len(vowels) - 1)])))
        if new_ending not in noun_endings:
            noun_endings.append(new_ending)

# derivational morphology
derivational_morphology = {}
for thing in deriv_morph:
    if randint(0, 1) == 1:
        derivational_morphology[thing] = ''.join(list_of_objects_to_list_of_strings(generate_word(1, plosives[randint(0, len(plosives) - 1)],
                                                       plosives[randint(0, len(plosives) - 1)],
                                                       fricatives[randint(0, len(fricatives) - 1)],
                                                       fricatives[randint(0, len(fricatives) - 1)],
                                                       vowels[randint(0, len(vowels) - 1)],
                                                       vowels[randint(0, len(vowels) - 1)]))) + '-'
    else:
        derivational_morphology[thing] = '-' + ''.join(list_of_objects_to_list_of_strings(generate_word(1, plosives[randint(0, len(plosives) - 1)],
                                                             plosives[randint(0, len(plosives) - 1)],
                                                             fricatives[randint(0, len(fricatives) - 1)],
                                                             fricatives[randint(0, len(fricatives) - 1)],
                                                             vowels[randint(0, len(vowels) - 1)],
                                                             vowels[randint(0, len(vowels) - 1)])))

# defining things that will be import soon
lexicon = {}
new_words = []

# copying dictionary over to variable
with open(r"C:\Users\Public\Documents\roots.txt", "r") as d:
    english_words = d.readlines()

tool = []
for root in english_words:
    tool.append(root.replace("\n", ''))
english_words = tool

total = len(english_words)
print("Generating...")

# WOO! Generating words for every word in the dictionary
syllables = 0
while len(new_words) < total:
    syllables += 1
    for plosive_1 in plosives:
        for plosive_2 in plosives:
            for vowel_1 in vowels:
                for vowel_2 in vowels:
                    for fricative_1 in fricatives:
                        for fricative_2 in fricatives:
                            new_words.append(
                                generate_word(syllables, plosive_1, plosive_2, fricative_1, fricative_2, vowel_1,
                                              vowel_2))

shuffle(new_words)
print("Done with syllables...")
i = 0
root_lexicon = {}
for root in english_words:
    root_lexicon[root.replace("\n", '')] = new_words[i]
    i += 1

with open(r"C:\Users\Public\Documents\dictionary.txt", "r") as d:
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
                new_word.append(generate_word(randint(1, 2), plosives[randint(0, len(plosives) - 1)],
                                          plosives[randint(0, len(plosives) - 1)],
                                          fricatives[randint(0, len(fricatives) - 1)],
                                          fricatives[randint(0, len(fricatives) - 1)],
                                          vowels[randint(0, len(vowels) - 1)], vowels[randint(0, len(vowels) - 1)]))
                reps = 0
                recon = word
        letter = 0
        harmony_settings = []
        new_word = flatten(new_word)
        new_new_word = ''
        while new_word[letter].is_consonant:
            letter += 1
        for harmony in vowel_harmony:
            if harmony == 'is_rounded':
                harmony_settings.append(new_word[letter].is_rounded)
            if harmony == 'backness':
                harmony_settings.append(new_word[letter].backness)
            if harmony == 'height':
                harmony_settings.append(new_word[letter].height)
        for letter in new_word:
            if letter.is_vowel:
                if 'is_rounded' in vowel_harmony:
                    old_stat = letter.is_rounded
                    letter.is_rounded = harmony_settings[vowel_harmony.index('is_rounded')]
                    new_new_word += str(letter)
                    letter.is_rounded = old_stat
                if 'backness' in vowel_harmony:
                    old_stat = letter.backness
                    letter.backness = harmony_settings[vowel_harmony.index('backness')]
                    new_new_word += str(letter)
                    letter.backness = old_stat
                if 'height' in vowel_harmony:
                    old_stat = letter.height
                    letter.height = harmony_settings[vowel_harmony.index('height')]
                    new_new_word += str(letter)
                    letter.height = old_stat
                if new_word.index(letter) < len(new_word)-1:
                    if new_word[new_word.index(letter)+1].is_consonant and new_word[new_word.index(letter)+1].is_nasal:
                        old_stat = letter.is_nasal
                        letter.is_nasal = True
                        new_new_word += str(letter)
                        letter.is_nasal = old_stat
            if letter.is_consonant:
                if new_word.index(letter) in range(1, len(new_word)-1):
                    if new_word[new_word.index(letter) - 1].is_voiced == new_word[new_word.index(letter) + 1].is_voiced:
                        old_stat = letter.is_voiced
                        letter.is_voiced = new_word[new_word.index(letter) - 1].is_voiced
                        new_new_word += str(letter)
                        letter.is_voiced = old_stat
                    if new_word[new_word.index(letter) - 1].is_consonant and new_word[new_word.index(letter) + 1].is_consonant:
                        if new_word[new_word.index(letter)-1].place_of_articulation == new_word[new_word.index(letter)+1].place_of_articulation:
                            old_stat = letter.place_of_articulation
                            letter.place_of_articulation = new_word[new_word.index(letter)-1].place_of_articulation
                            new_new_word += str(letter)
                            letter.place_of_articulation = old_stat
                        if new_word[new_word.index(letter)-1].is_nasal == new_word[new_word.index(letter)+1].is_nasal:
                            old_stat = letter.is_nasal
                            letter.is_nasal = True
                            new_new_word += str(letter)
                            letter.is_nasal = old_stat

        lexicon[word] = new_new_word
print("Done with words...")

# converting everything to strings
plosives = list_of_objects_to_list_of_strings(plosives)
fricatives = list_of_objects_to_list_of_strings(fricatives)
vowels = list_of_objects_to_list_of_strings(vowels)

# outputting everything to a document
print("Writing to document...")
with open(r"C:\Users\Public\Documents\Conlang_Dictionary.txt", "w") as f:
    f.write("Morphology: \n \nVerbs: \n")
    ending = 0
    for i in numbers:
        for j in persons:
            for k in tenses:
                for l in moods:
                    f.write(i + ', ' + j + ', ' + k + ', ' + l + ': ' + str(verb_endings[ending]) + '\n')
                    ending += 1
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
            f.write(i + ', ' + j + ': ' + str(noun_endings[ending]) + '\n')
            ending += 1
            if ending >= len(noun_endings) - 1:
                break
    f.write("\nDerivational Morphology:\n")
    for i in derivational_morphology:
        f.write(i + ': ' + str(derivational_morphology[i]) + '\n')
    f.write("\nPhonology: \n \nConsonants: \n")
    f.write(', '.join(plosives + fricatives))
    f.write("\nVowels: \n")
    f.write(', '.join(vowels))
    f.write("\n\nSyntax:\n")
    f.write(' - '.join(word_order) + '\n')
    if modifiers_before_word:
        f.write("Head Final")
    else:
        f.write("Head First")
    f.write("\n \nLexicon: \n")
    for word in lexicon:
        print_word = ''
        for letter in lexicon[word]:
            print_word += str(letter)
        f.write(word + ': ' + print_word + '\n')
print("Done!")
