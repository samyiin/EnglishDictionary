from nltk.corpus import words
from wordfreq import word_frequency
import numpy as np
# This will give all conjugations of a verb
# https://pypi.org/project/word-forms/
from word_forms.word_forms import get_word_forms
import os
import pandas as pd


class EnglishDictionary:
    def __init__(self, root_dir="Utils/"):
        # This will only be called in the root directory of the project.
        # By default we use the NLTK dictionary
        self.abbrev_dict = None
        self.abbrev_set = None
        self.abbreviations = None
        self.dictionary = set(words.words())
        self.source_directory = os.path.join(root_dir, 'EnglishDictionarySource/')
        irregular_verbs_csv = os.path.join(self.source_directory, 'irregular_verbs.csv')
        self.df_irregular_verbs = pd.read_csv(irregular_verbs_csv)
        # initialize with ENABLE
        self.load_dictionary()
        # initialize the list of common abbreviations
        self.load_abbreviation_list()

    @staticmethod
    def _load_word_list(file_path):
        """Load a large word list from a file into a set."""
        with open(file_path, 'r') as f:
            return set(line.strip().lower() for line in f)

    def load_dictionary(self, dictionary_name="ENABLE"):
        """
        The default value is ENABLE, but there are other values
        :param dictionary_name: [ENABLE, dwyl-english_words, SCOWL, NLTK]
        :return:
        """
        if dictionary_name == "ENABLE":
            # Credit: https://github.com/dolph/dictionary.git
            word_list_path = os.path.join(self.source_directory, 'enable1.txt')
            self.dictionary = self._load_word_list(word_list_path)
        elif dictionary_name == "dwyl-english_words":
            # Credit: https://github.com/dwyl/english-words.git
            word_list_path = os.path.join(self.source_directory, 'words_alpha.txt')
            self.dictionary = self._load_word_list(word_list_path)
        elif dictionary_name == "SCOWL":
            # Credit: https://github.com/en-wl/wordlist.git
            '''
            clone and go to terminal
            make
            ./scowl word-list scowl.db > wl.txt
            :return:
            '''
            word_list_path = os.path.join(self.source_directory, 'wl.txt')
            self.dictionary = self._load_word_list(word_list_path)
        elif dictionary_name == "NLTK":
            import nltk
            nltk.download('words', download_dir=os.path.join(self.source_directory, 'nltk_data'))
            nltk.download('brown', download_dir=os.path.join(self.source_directory, 'nltk_data'))
            self.dictionary = set(words.words())
        else:
            raise ValueError("PARAMETER dictionary_name: [ENABLE, dwyl-english_words, SCOWL, NLTK]")

    def is_english(self, word):
        return (word in self.dictionary) or (word.lower() in self.dictionary)

    # =================function 2: get words frequency ==========================
    def get_word_natural_frequency(self, word):
        """
        # This word_frequency actually includes GoogleBooksNgram
        # https://github.com/rspeer/wordfreq.git
        # Good for single english word, Limited functionality for n-grams (a strings that contains many words)
        :param word:
        :return:
        """
        freq = word_frequency(word, 'en')
        return freq

    # =================function 3: check abbreviations ==========================
    def load_abbreviation_list(self, abbreviation_list="my_list"):
        """
        So far I only have one abbreviation list
        :param abbreviation_list: ["my_list"]
        :return:
        """
        if abbreviation_list != "my_list":
            raise ValueError("Do not support other abbrev list yet...")
        self.abbreviations = pd.read_csv(os.path.join(self.source_directory, "abbreviations_my_list.csv"))
        self.abbreviations.map(str.lower)
        self.abbrev_set = set(self.abbreviations['abbreviation'])  # for O(1) lookup
        # maps abbrev -> expansion
        self.abbrev_dict = dict(zip(self.abbreviations['abbreviation'], self.abbreviations['expansion']))

    def is_abbrev(self, word):
        return word.lower() in self.abbrev_set

    def expand_abbrev(self, word):
        if word in self.abbrev_set:
            return self.abbrev_dict[word]
        else:
            return None

    # =================function 3: check word forms ==========================

    def word_forms(self, word):
        # Unused....
        return get_word_forms(word)

    def is_irregular_past_tense(self, verb):
        for index, row in self.df_irregular_verbs.iterrows():
            if verb == row['Past Simple'] or verb == row['-ed']:
                if verb != row['Base Form']:
                    return True
        return False
