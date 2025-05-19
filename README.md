# EnglishDictionary
A little english dictionary that can check:
1. if a word is in English dictionary (natural language)
2. if a word is a common abbreviation (in programming context...: Including domain specific terms, technical terms like library names)
3. if a word is common programming types. (strings like "list", "lst", "set", "dict")
4. if a word has irregular verb form

## Identify Dictionary words
Usage: 

    EnglishDictionary().is_english(word)
Identifying dictionary words might seem trivial at frist, but there are many versions of dictionary, some includes "too many" words and some includes "too few" words. For example, the word "gen" is technically a word that means "information" in British English, but "normally" people wouldn't treat it as a dictioanry word, but rather abbreviation for "generation". 

So far I found a few dictionary of choice, I will list their link here:
NLTK

    https://www.nltk.org/
ENABLE (Enhanced North American Benchmark Lexicon)

    https://github.com/dolph/dictionary.git
SCOWL (Spell Checker Oriented Word Lists)

    https://github.com/en-wl/wordlist.git
Some random dictionary on internet?

    https://github.com/dwyl/english-words.git

 COCA (Corpus of Contemporary American English )

     https://www.english-corpora.org/coca/

After usage, I feel like NLTK contains too little words, COCA contains way too much, also of course if I combine everything, it contains too much words. I set default to ENABLE. 

## Identify Abbreviations
Usage:

    EnglishDictionary().is_abbrev(word)
**Previous attempts**:
In "large-scale investigation of local variable names in java programs: Is longer name better for broader scope variable?" 2021, Aman built a dictionary of 201 common abbreviations by referencing https://www.abbreviations.com/. The file can be download from their official website, and I just kept a copy here:

    Official website: https://se.cite.ehime-u.ac.jp/data/QUATIC2021/
    File path: EnglishDictionarySource/abbreviations_Aman.txt
  
In "Reanalysis of empirical data on java local variables with narrow and broad scope" 2023, Feitelson scanned more names, and manually expand them. He build his work based on Aman's work, and ended up with 302 word-abbreviation pairs. Mr. Feitelson send me his list, and I also kept a copy of this list in this project:

    File path: EnglishDictionarySource/abbreviations_Feitelson.txt

**What I did**
1. I combined all the identified abbreviations in Aman and Feitelson's file, and manually expand them with the help of internet, chatgpt and stuff.
2. I deleted some less common - far fetched expansion; or the name is very common in java programming but not so much in programming in general. (Some famous java libraries such as AWT - Abstract Window Toolkit; some domain specific terms in communication networks such as uuid - unique user identifier).
3. I deleted some ambiguous ones: for example: "pos" can mean "position" or "positive" depend on context and there is no predominant one. 
4. Feitelson decided that some technical terms/domain specific terms are so pervalent that we do not need to expand them, but rather treat them as new words. I agree to a large extend, but I added two new rules: First the name have to be very common to a certain extent (I decide): names like "java" and "mysql". Second, the name does not have other common interpretations.
5. I then added some common python library names like numpy and scipy. (Since this original list is build on Java programs).
6. I also made a list of common programming types and their common abbraviations. (like string, str, list, lst)

**Any potential problems?**
Expanding abbreviations is a semantic task, it also depends on context. But some abbreviations are so common that they almost always have only one kind of expansion. I try to use my subjective judgement to decide if this abbreviaiton is pervalent enough that there is almost only one kind of expansion. In later project I will use other ways such as LLM to expand abbreviations. Check out my ZipflawAnalysis repo. 

## Identify Common Programming Types 
I manually collected strings that represents types in programming, like "list" or "lst". This is some sort of domain specific jargon. But it's useful to make the distinction for the purpose of my masters thesis, so I added this functionality to the dictionary. 

    File path: EnglishDictionarySource/common_programming_type_name.csv

Usage:

    EnglishDictionary().is_program_type(word)

## Identify verbs has irregular past tense
I gathered a list of strings that represents past and present tenses of common irregular verbs. 

    File path: EnglishDictionarySource/irregular_verbs.csv

Usage:

    EnglishDictionary().is_irregular_past_tense(word)


## Word frequency
I use other people's repository directory, so just go look at theirs. One major thing is word frequency is google's n-gram data, and this python library does contain the google n-gram data, so I think it is very comprehensive. Here is the link:

    https://github.com/rspeer/wordfreq.git


## Classification Problem
Just like any classifier, there is always this TP/FN problem. So what I noticed here is that when I used this dictionary for identifying words in programming variables, it could cause some problem:

    TP: actual English word classified as actual English word, like "hello" -> is English
    TN: non English word classified as English word. like "gen" -> is English. Technically it is, but it's very uncommon, and likely an abbreviation
    FP: non English word classified as non English word. Like "asdf" -> not english
    FN: English word classified as non English word. I can't find such examples yet...

So to evaluate this dictionary, we will see the trade-off of ROC. So far, feeling-wise, I feel like for concern of my thesis, ENABLE is the best dictionary...


