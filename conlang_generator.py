from random import randint
from random import shuffle

#Create Consonant class in order to be able to delete blank ones
class Consonant:
    def __init__(self, is_voiced, is_aspirated, place_of_articulation, type_of_articulation, is_ejective, is_lateral, is_nasal):
        self.is_voiced = is_voiced
        self.is_aspirated = is_aspirated
        self.place_of_articulation = place_of_articulation
        self.type_of_articulation = type_of_articulation
        self.is_ejective = is_ejective
        self.is_lateral = is_lateral
        self.is_nasal = is_nasal

    def __str__(self):
        return_val = ''
        if self.type_of_articulation == 'plosive':
            if self.place_of_articulation == 'bilabial':
                if self.is_voiced == False:
                    if self.is_aspirated == False:
                        return_val = 'p'
                    else:
                        return_val = 'ph'
                else:
                    return_val = 'b'
            elif self.place_of_articulation == 'dental' or self.place_of_articulation == 'alveolar':
                if self.is_voiced == False:
                    if self.is_aspirated == False:
                        return_val = 't'
                    else:
                        return_val = 'th'
                else:
                    return_val = 'd'
            elif self.place_of_articulation == 'palatal':
                if self.is_voiced == False:
                    if self.is_aspirated == False:
                        return_val = 'c'
                    else:
                        return_val = 'ch'
                else:
                    return_val = 'j'
            elif self.place_of_articulation == 'velar':
                if self.is_voiced == False:
                    if self.is_aspirated == False:
                        return_val = 'k'
                    else:
                        return_val = 'kh'
                else:
                    return_val = 'g'
            elif self.place_of_articulation == 'uvular':
                if self.is_voiced == False:
                    if self.is_aspirated == False:
                        return_val = 'q'
                    else:
                        return_val = 'qh'
                else:
                    return_val = 'G'
            elif self.place_of_articulation == 'glottal':
                return_val = "'"
        if self.type_of_articulation == 'fricative':
            if self.place_of_articulation == 'bilabial':
                if self.is_voiced == False:
                    return_val = 'w'
                    if self.is_nasal == True:
                        return_val = 'hm'
                else:
                    return_val = 'v'
                    if self.is_nasal == True:
                        return_val = 'm'
            elif self.place_of_articulation == 'dental':
                return_val = 'th'
            elif self.place_of_articulation == 'alveolar':
                if self.is_voiced == False:
                    return_val = 's'
                    if self.is_nasal == True:
                        return_val = 'hn'
                else:
                    return_val = 'z'
                    if self.is_nasal == True:
                        return_val = 'n'
                    if self.is_lateral == True:
                        return_val = 'l'
            elif self.place_of_articulation == 'palatal':
                if self.is_voiced == False:
                    return_val = 'ç'
                    if self.is_nasal == True:
                        return_val = 'hñ'
                else:
                    return_val = 'y'
                    if self.is_nasal == True:
                        return_val = 'ñ'
            elif self.place_of_articulation == 'velar' or self.place_of_articulation == 'uvular':
                if self.is_voiced == False:
                    return_val = 'x'
                    if self.is_nasal == True:
                        return_val = 'hng'
                else:
                    return_val = 'gh'
                    if self.is_nasal == True:
                        return_val = 'ng'
            elif self.place_of_articulation == 'glottal':
                return_val = 'h'
        if self.type_of_articulation == 'affricate':
            if self.place_of_articulation == 'dental' or self.place_of_articulation == 'alveolar':
                if self.is_voiced == False:
                    if self.is_aspirated == False:
                        return_val = 'ts'
                        if self.is_lateral == True:
                            return_val = 'tl'
                    else:
                        return_val = 'tsh'
                else:
                    return_val = 'dz'
                    if self.is_lateral == True:
                        return_val = 'dl'
            elif self.place_of_articulation == 'palatal':
                if self.is_voiced == False:
                    if self.is_aspirated == False:
                        return_val = 'ch'
                    else:
                        return_val = 'chh'
                else:
                    return_val = 'j'
            elif self.place_of_articulation == 'velar' or self.place_of_articulation == 'uvular':
                if self.is_voiced == False:
                    if self.is_aspirated == False:
                        return_val = 'qx'
                    else:
                        return_val = 'qxh'
        if self.is_ejective == True and self.place_of_articulation != 'glottal' and (self.type_of_articulation == 'plosive' or self.type_of_articulation == 'affricate') and self.is_voiced == False and return_val != '' and self.is_aspirated == False:
            return_val += "'"
        elif self.is_ejective == True:
            return ''
        return return_val

#define 'stock' variables
places_of_articulation = ['bilabial','dental','alveolar','palatal','velar','uvular','glottal']
types_of_articulation = ['plosive','fricative', 'ejective', 'affricate']
vowels = ['a','e','i','o','u']
is_voiced = [True, False]
is_aspirated = [True, False]
is_ejective = [True, False]
is_lateral = [True, False]
is_nasal = [True, False]
cases = ['nominative', 'accusative', 'vocative', 'instrumental', 'dative', 'ablative', 'genitive']
numbers = ['singular', 'dual', 'plural', 'collective']
persons = ['first', 'second', 'third']
tenses = ['present', 'preterite', 'imperfect', 'future', 'perfect', 'progressive']
moods = ['indicative', 'subjunctive', 'optative', 'imperative']
parts_of_speech = ['noun','verb','adjective','adverb']
deriv_morph = []

#decide which distinctions our conlang will/won't make
while len(places_of_articulation) > randint(2,8):
    del places_of_articulation[randint(0,len(places_of_articulation)-1)]

while len(types_of_articulation) > randint(2,5):
    del types_of_articulation[randint(0,len(types_of_articulation)-1)]

while len(vowels) > randint(2,6):
    del vowels[randint(0,len(vowels)-1)]

while len(cases) > randint(0,8):
    del cases[randint(0,len(cases)-1)]
if len(cases) == 0:
    cases.append('')

while len(numbers) > randint(0,5):
    del numbers[randint(0,len(numbers)-1)]
if len(numbers) == 0:
    numbers.append('')

while len(persons) > randint(0,4):
    del persons[randint(0,len(persons)-1)]
if len(persons) == 0:
    persons.append('')

while len(tenses) > randint(0,7):
    del tenses[randint(0,len(tenses)-1)]
if len(tenses) == 0:
    tenses.append('')

while len(moods) > randint(0,5):
    del moods[randint(0,len(moods)-1)]
if len(moods) == 0:
    moods.append('')

if randint(0,1) == 1:
    is_aspirated = [False]
if randint(0,1) == 1:
    is_ejective = [False]
if randint(0,5) == 1:
    is_lateral = [False]
if randint(0,5) == 1:
    is_nasal = [False]

consonant_inventory = []
new_consonant_inventory = []

for i in range(randint(0, 20)):
    deriv_morph.append(parts_of_speech[randint(0,len(parts_of_speech)-1)]+' to '+parts_of_speech[randint(0,len(parts_of_speech)-1)])

#phonotactics
probability_of_init_plosive = randint(1,100)
probability_of_init_fricative = randint(1,100)
probability_of_double_vowel = randint(1,100)
probability_of_fin_fricative = randint(1,100)
probability_of_fin_plosive = randint(1,100)

if randint(1,3) == 1:
    probability_of_init_plosive = 0
if randint(1,3) == 1:
    probability_of_init_fricative = 0
if randint(1,3) == 1:
    probability_of_double_vowel = 0
if randint(1,3) == 1:
    probability_of_fin_fricative = 0
if randint(1,3) == 1:
    probability_of_fin_plosive = 0

#syntax
word_order = ['subject', 'verb', 'indirect object', 'direct object']
modifiers_before_word = True
shuffle(word_order)
if randint(0,1) == 1:
    modifiers_before_word = False

#actually create list of consonants
for i in is_voiced:
    for j in is_aspirated:
        for k in places_of_articulation:
            for l in types_of_articulation:
                for m in is_ejective:
                    for n in is_lateral:
                        for o in is_nasal:
                            consonant_inventory.append(Consonant(i,j,k,l,m,n,o))



for i in range(len(consonant_inventory)):
    if str(consonant_inventory[i]) != '' and new_consonant_inventory.count(consonant_inventory[i]) < 2:
        new_consonant_inventory.append(consonant_inventory[i])
for i in range(randint(0,len(new_consonant_inventory)-3)):
    del new_consonant_inventory[randint(0,len(new_consonant_inventory)-1)]

#setup for generating words
if 'plosive' or 'ejective' in types_of_articulation:
    plosives = [str(letter) for letter in new_consonant_inventory if (letter.type_of_articulation == 'plosive' or letter.type_of_articulation == 'ejective' or letter.type_of_articulation == 'affricate')]
    has_plosives = True
else:
    has_plosives = False
    plosives = []
if 'fricative' in types_of_articulation:
    has_fricatives = True
    fricatives = [str(letter) for letter in new_consonant_inventory if (letter.type_of_articulation == 'fricative')]
else:
    has_fricatives = False
    fricatives = []
for letter in plosives:
    if plosives.count(letter) > 1:
        reps = plosives.count(letter)
        for i in range(reps - 1):
            plosives.remove(letter)

if has_fricatives == True:
    for letter in fricatives: #remove duplicates
        if fricatives.count(letter) > 1:
            reps = fricatives.count(letter)
            for i in range(reps - 1):
                fricatives.remove(letter)


if randint(0,1) == 1 and 'fricative' in types_of_articulation: #adding possible rhotic; you decide how you want to pronounce it
    fricatives.append('r')
for letter in plosives:
    if plosives.count(letter) > 1:
        plosives.remove(letter)
if has_fricatives == True:
    for letter in fricatives:
        if fricatives.count(letter) > 1:
            fricatives.remove(letter)

def generate_word(syllables, plosive_1, plosive_2, fricative_1, fricative_2, vowel_1, vowel_2):

    word = ""

    #syllables = int( 10 * randint(int(0.5*syllable), 2*syllable) / total) + randint(-1, 1)
    #if syllables <= 0 or syllable == 0:
        #syllables = 1

    for index in range(syllables):
        if randint(1,100)<probability_of_init_plosive:
            word += plosive_1
        if has_fricatives == True:
            if randint(1,100)<probability_of_init_fricative:
                word += fricative_1
        if randint(0,1)<probability_of_double_vowel:
            word += vowel_1
        else:
            word += vowel_1
            word += vowel_2
        if has_fricatives == True:
            if randint(1,100)<probability_of_fin_fricative:
                word += fricative_2
        if randint(1,100)<probability_of_fin_plosive:
            word += plosive_2

    return word

#verb conjugation time
verb_endings = []
for i in numbers:
    for j in persons:
        for k in tenses:
            for l in moods:
                new_ending = generate_word(1, plosives[randint(0,len(plosives)-1)], plosives[randint(0,len(plosives)-1)], fricatives[randint(0,len(fricatives)-1)], fricatives[randint(0,len(fricatives)-1)], vowels[randint(0,len(vowels)-1)], vowels[randint(0,len(vowels)-1)])
                if new_ending not in verb_endings:
                    verb_endings.append(new_ending)

#whee, noun declension
noun_endings = []
for i in cases:
    for j in numbers:
        new_ending = generate_word(1, plosives[randint(0,len(plosives)-1)], plosives[randint(0,len(plosives)-1)], fricatives[randint(0,len(fricatives)-1)], fricatives[randint(0,len(fricatives)-1)], vowels[randint(0,len(vowels)-1)], vowels[randint(0,len(vowels)-1)])
        if new_ending not in noun_endings:
            noun_endings.append(new_ending)

#derivational morphology
derivational_morphology = {}
for thing in deriv_morph:
    if randint(0,1) == 1:
        derivational_morphology[thing] = generate_word(1, plosives[randint(0,len(plosives)-1)], plosives[randint(0,len(plosives)-1)], fricatives[randint(0,len(fricatives)-1)], fricatives[randint(0,len(fricatives)-1)], vowels[randint(0,len(vowels)-1)], vowels[randint(0,len(vowels)-1)])+'-'
    else:
        derivational_morphology[thing] = '-'+generate_word(1, plosives[randint(0,len(plosives)-1)], plosives[randint(0,len(plosives)-1)], fricatives[randint(0,len(fricatives)-1)], fricatives[randint(0,len(fricatives)-1)], vowels[randint(0,len(vowels)-1)], vowels[randint(0,len(vowels)-1)])

#defining things that will be import soon
lexicon = {}
english_words = []
new_words = []

#copying dictionary over to variable
with open(r"C:\Users\willi\roots.txt", "r") as d:
    english_words = d.readlines()

tool = []
for root in english_words:
    tool.append(root.replace("\n",''))
english_words = tool
english_words.append("next")
english_words.append("ex")

total = len(english_words)
print("Generating words...")

#WOO! Generating words for every word in the dictionary
syllables = 0
while len(new_words) < total:
    syllables += 1
    for plosive_1 in plosives:
        for plosive_2 in plosives:
            for vowel_1 in vowels:
                for vowel_2 in vowels:
                    for fricative_1 in fricatives:
                        for fricative_2 in fricatives:
                           new_words.append(generate_word(syllables, plosive_1, plosive_2, fricative_1, fricative_2, vowel_1, vowel_2))

shuffle(new_words)
i = 0
root_lexicon = {}
for root in english_words:
    root_lexicon[root.replace("\n",'')] = new_words[i]
    i += 1

with open(r"C:\Users\willi\dictionary.txt","r") as d:
    real_words = d.readlines()
tool = []
for word in real_words:
    tool.append(word.replace("\n", ''))
real_words = tool

for word in real_words:
    reps = 0
    english_words
    use_word = word
    recon = ""
    new_word = ""
    if word in english_words:
        lexicon[word] = root_lexicon[word]
    else:
        while recon != word:
            for i in range(len(use_word)+1):
                if use_word[:i] in english_words:
                    recon += use_word[:i+1]
                    new_word += root_lexicon[use_word[:i]]
                    use_word = use_word[i+1:]
                    break
            reps += 1
            if reps > 10:
                new_word += generate_word(randint(1,2), plosives[randint(0,len(plosives)-1)], plosives[randint(0,len(plosives)-1)], fricatives[randint(0,len(fricatives)-1)], fricatives[randint(0,len(fricatives)-1)], vowels[randint(0,len(vowels)-1)], vowels[randint(0,len(vowels)-1)])
                reps = 0
                recon = word
        lexicon[word] = new_word
            
#outputting everything to a document
with open(r"C:\Users\willi\Conlang_Dictionary.txt","w") as f:
        f.write("Morphology: \n \nVerbs: \n")
        ending = 0
        for i in numbers:
            for j in persons:
                for k in tenses:
                    for l in moods:
                        f.write(i+', '+j+', '+k+', '+l+': '+verb_endings[ending]+'\n')
                        ending += 1
                        if ending > len(verb_endings)-1:
                            break
                    if ending > len(verb_endings)-1:
                        break
                if ending > len(verb_endings)-1:
                    break
            if ending > len(verb_endings)-1:
                break
        f.write("\nNoun Declension: \n")
        ending = 0
        for i in numbers:
            for j in cases:
                f.write(i+', '+j+': '+noun_endings[ending]+'\n')
                ending += 1
                if ending >= len(noun_endings)-1:
                    break
        f.write("\nDerivational Morphology:\n")
        for i in derivational_morphology:
            f.write(i+': '+derivational_morphology[i]+'\n')
        f.write("\nPhonology: \n \nConsonants: \n")
        f.write(', '.join(plosives+fricatives))
        f.write("\nVowels: \n")
        f.write(', '.join(vowels))
        f.write("\n\nSyntax:\n")
        f.write(' - '.join(word_order)+'\n')
        if modifiers_before_word == True:
            f.write("Head Final")
        else:
            f.write("Head First")
        f.write("\n \nLexicon: \n")
        for word in lexicon:
            f.write(word+': '+lexicon[word]+'\n')

#user interface
answer = input("Type an English word or type 'v-' for conjugations and 'n-' for declensions:")
while answer != "STOP":
    if answer in lexicon:
        print(lexicon[answer])
    elif answer == 'v-':
        ending = 0
        for i in numbers:
            for j in persons:
                for k in tenses:
                    for l in moods:
                        print(i+', '+j+', '+k+', '+l+': '+verb_endings[ending])
                        ending += 1
                        if ending > len(verb_endings)-1:
                            break
                    if ending > len(verb_endings)-1:
                            break
                if ending > len(verb_endings)-1:
                            break
            if ending > len(verb_endings)-1:
                            break
        
    elif answer == 'n-':
        ending = 0
        for i in numbers:
            for j in cases:
                print(i+', '+j+': '+noun_endings[ending])
                ending += 1
                if ending >= len(noun_endings)-1:
                    break
    elif ' ' in answer:
        phrase = answer.split()
        translation = []
        for word in phrase:
            if word in lexicon:
                translation.append(str(lexicon[word]))
            else:
                print("Error, "+word+" not in dictionary")
                break
        else:
            print(' '.join(translation))
    elif answer == 'c-':
        print(plosives + fricatives)
    elif answer == 'vo-':
        print(vowels)
    elif answer == 's-':
        print(word_order)
        print(modifiers_before_word)
    elif answer == 'd-':
        for i in derivational_morphology:
            print(i+': '+derivational_morphology[i])
    else:
        print("Error, not in dictionary")
    answer = input()


