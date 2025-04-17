# EnglishDictionary
A little english dictionary that can check:
1. if a word is in English dictionary (natural language)
2. if a word is a common abbreviation (in programming context...)
3. the n-gram word frequency of a word


combine the list of Aman and Feitelson

delete unidentifiables - less common - far fetched expansion
pos - position/positive - ambiguous expansion
expand some non-expand becasuse I want to be more strict on non-expands: Only when it's actually pervalent and there is no ambiguity: there is no other things that could possibily use this. Another criteria: does the programmer know the english behind the abbrev. if they do then we expand it so that later in statistics we can see their size of vocab
library names: don't expand-- but only keep it when it's common enough and no other possible interpretations
dictionary word should include technical jargons, llibrary/programming language names when they are not abbreviation: javascript. 
But when a technical jargon is abbreviation of actual english word, then it will be treated as abbreviation. 
What about "originally its abbreviation of something, but then it get too pervalent it becomes a word" like sql
Domain specific term is considered abbreviation - even when they themsleves have abbreviation. Because sometimes they started with being acronymes of real english word like sql 
if it's abbrev of library/language name: eg: js - javascript (which is still not a word but 
