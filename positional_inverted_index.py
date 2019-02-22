import os
import re
import sys
import time

# list of  stop words
stopwords=['अत', 'अपना', 'अपनी', 'अपने', 'अभी', 'अंदर', 'आदि', 'आप', 'इत्यादि', 'इन ', 'इनका', 'इन्हीं', 'इन्हें', 'इन्हों', 'इस', 'इसका', 'इसकी', 'इसके', 'इसमें', 'इसी', 'इसे', 'उन', 'उनका', 'उनकी', 'उनके', 'उनको', 'उन्हीं', 'उन्हें', 'उन्हों', 'उस', 'उसके', 'उसी', 'उसे', 'एक', 'एवं', 'एस', 'ऐसे','कई', 'कर', 'करता', 'करते', 'करना', 'करने', 'करें', 'कहते', 'कहा', 'का', 'काफ़ी', 'कि', 'कितना', 'किन्हें', 'किन्हों', 'किया', 'किर', 'किस', 'किसी', 'किसे', 'की', 'कुछ', 'कुल', 'के', 'को', 'कोई', 'कौन', 'कौनसा', 'गया', 'घर', 'जब', 'जहाँ', 'जा', 'जितना', 'जिन', 'जिन्हें', 'जिन्हों', 'जिस', 'जिसे', 'जीधर', 'जैसा', 'जैसे', 'जो', 'तक', 'तब', 'तरह', 'तिन', 'तिन्हें', 'तिन्हों', 'तिस', 'तिसे', 'तो', 'था', 'थी', 'थे', 'दबारा', 'दिया', 'दुसरा', 'दूसरे', 'दो', 'द्वारा', 'न', 'नके', 'नहीं', 'ना', 'निहायत', 'नीचे', 'ने', 'पर', 'पहले', 'पे', 'फिर', 'बनी', 'बही', 'बहुत', 'बाद', 'बाला', 'बिलकुल', 'भी', 'भीतर', 'मगर', 'मानो', 'मे', 'में', 'यदि', 'यह', 'यहाँ', 'यही', 'या', 'यिह', 'ये', 'रखें', 'रहा', 'रहे', 'ऱ्वासा', 'लिए', 'लिये', 'लेकिन', 'व', 'वग़ैरह', 'वर्ग', 'वह', 'वहाँ', 'वहीं', 'वाले', 'वुह', 'वे', 'सकता', 'सकते', 'सबसे', 'सभी', 'साथ', 'साबुत', 'साभ', 'सारा', 'से', 'सो', 'संग', 'ही', 'हुआ', 'हुई', 'हुए', 'है', 'हैं', 'हो', 'होता', 'होती', 'होते', 'होना', 'होने', '']
#print(stopwords)

#---- Index Creation-------#

from collections import Counter
from pprint import pprint as pp
from glob import glob
try: reduce
except: from functools import reduce
try:    raw_input
except: raw_input = input


#---- Stemmer for Hindi---------------------#
suffixes = {
    1: ["ो", "े", "ू", "ु", "ी", "ि", "ा"],
    2: ["कर", "ाओ", "िए", "ाई", "ाए", "ने", "नी", "ना", "ते", "ीं", "ती", "ता", "ाँ", "ां", "ों", "ें"],
    3: ["ाकर", "ाइए", "ाईं", "ाया", "ेगी", "ेगा", "ोगी", "ोगे", "ाने", "ाना", "ाते", "ाती", "ाता", "तीं", "ाओं", "ाएं", "ुओं", "ुएं", "ुआं"],
    4: ["ाएगी", "ाएगा", "ाओगी", "ाओगे", "एंगी", "ेंगी", "एंगे", "ेंगे", "ूंगी", "ूंगा", "ातीं", "नाओं", "नाएं", "ताओं", "ताएं", "ियाँ", "ियों", "ियां"],
    5: ["ाएंगी", "ाएंगे", "ाऊंगी", "ाऊंगा", "ाइयाँ", "ाइयों", "ाइयां"],
}

def hi_stemmer(word):
    for L in 5, 4, 3, 2, 1:
        if len(word) > L + 1:
            for suf in suffixes[L]:
                if word.endswith(suf):
                    return word[:-L]
    return word

def stem_terms(terms_list):
    for term in terms_list:
        term=hi_stemmer(term)
    return terms_list
#-------------parsing splitting on | and , and then adding space before and after |--------------------#

#------------ PARSING TEXT-------------------#

def parsetexts(fileglob='C:\\Users\\laisha wadhwa\\Documents\\sem5\\IR\\project\\IR project_IR_Course\\InputFiles\\*.txt'):
    texts = {}
    words=[]
    for txtfile in glob(fileglob):
        per_file_words=[]
        arr=[]
        f=open(txtfile, encoding='utf-8-sig')
        txt = f.read()
        arr=txt.split("।")
        for i in arr:
            i=i.replace(',','')
            i=i.replace('.','')
            i=i.replace('!','')
            i=i.replace(')','')
            i=i.replace('(','')
            i=i.replace('"','')
            i=i.replace('\'','')
            per_file_words=per_file_words+ i.strip().strip('"').split()
        #per_file_words = list(set(per_file_words))
        per_file_words =[word for word in per_file_words if word not in stopwords] #list(set(per_file_words)-set(stopwords))
        #time to stem
        per_file_words=stem_terms(per_file_words)
        filename= txtfile.split('\\')[-1]
        texts[filename] = per_file_words
        words=words+per_file_words
        
    return  texts, words

#-------------PRINTING DICTIONARY-------------------
texts, words = parsetexts()
#print('\nTexts')
#pp(texts)
#print('\nWords')
#pp(sorted(words))


def termsearch(terms): # Searches full inverted index
    if not set(terms).issubset(words):
        return set()
    return reduce(set.intersection,
                  (set(x[0] for x in txtindx)
                   for term, txtindx in finvindex.items()
                   if term in terms),
                  set(texts.keys()) )
 
def phrasesearch(phrase):
    wordsinphrase = phrase.strip().strip('"').split()
    wordsinphrase=[word for word in wordsinphrase if word not in stopwords]
    wordsinphrase=stem_terms(wordsinphrase)
    if not set(wordsinphrase).issubset(words):
        return set()
    #firstword, *otherwords = wordsinphrase 
    firstword, otherwords = wordsinphrase[0], wordsinphrase[1:]
    found = []
    for txt in termsearch(wordsinphrase):
        # Searching text files
        for firstindx in (indx for t,indx in finvindex[firstword]
                          if t == txt):
            # Over all positions of the first word of the phrase in this txt
            if all( (txt, firstindx+1 + otherindx) in finvindex[otherword]
                    for otherindx, otherword in enumerate(otherwords) ):
                found.append(txt)
    return found
 
 
finvindex = {word:set((txt, wrdindx)
                      for txt, wrds in texts.items()
                      for wrdindx in (i for i,w in enumerate(wrds) if word==w)
                      if word in wrds)
             for word in words}

def pos_term_search(phrase):
    #phrase = '"एक चिड़िया थी वह बहुत उच उड़ती  इधर उधर चहचहाती रहती"'
    result,intmd_result,it_st=[],[],''
    start = time.clock()
    query_terms = phrase.strip().strip('"').split()
    query_terms=list(set(query_terms)-set(stopwords))
    query_terms=stem_terms(query_terms)
    print('\nTerm Search on full inverted index for: ' + repr(query_terms))
    intmd_result=list(termsearch(query_terms))
    for i in range(len(intmd_result)):
        it_st=it_st+ str(i+1)+ " "+ intmd_result[i] +'\n'
    #pp(finvindex)
    result.append("===========================================================")
    result.append("\n\n\n-------स्थितित्मक उलटा सूचकांक पर सामान्य खोज के परिणाम---------------\n\n")
    result.append("परिणाम प्राप्त करने के लिए "+  "  " + str(round(time.clock() - start,4))+"s " +"का समय लिया गया")
    result.append(it_st)
    return result

#phrasal query search
    
def pos_phrase_search(phrase):
    #phrase = '"दैनिक कार्यों"'#'" पूरा जीवन झुंझलाते"'
    result,intmd_resul,it_st=[],[],''
    start = time.clock()
    phrase=f'"{phrase}"'
    print('\nPhrase Search for: ' + phrase)
    intmd_resul=list(phrasesearch(phrase))
    for i in range(len(intmd_resul)):
        it_st=it_st+ str(i+1)+ " "+ intmd_resul[i] +'\n'
    #pp(finvindex)
    result.append("===========================================================")
    result.append("\n\n\n-------स्थितित्मक उलटा सूचकांक पर वाक्यांश खोज के परिणाम---------------\n\n")
    result.append("परिणाम प्राप्त करने के लिए "+  "  " + str(round(time.clock() - start,4))+"s " +"का समय लिया गया")
    result.append(it_st)
    return result


