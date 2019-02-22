import os
import re
import sys
import time

# list of  stop words
stopwords=['अत', 'अपना', 'अपनी', 'अपने', 'अभी', 'अंदर', 'आदि', 'आप', 'इत्यादि', 'इन ', 'इनका', 'इन्हीं', 'इन्हें', 'इन्हों', 'इस', \
           'इसका', 'इसकी', 'इसके', 'इसमें', 'इसी', 'इसे', 'उन', 'उनका', 'उनकी', 'उनके', 'उनको', 'उन्हीं', 'उन्हें', 'उन्हों', 'उस', \
           'उसके', 'उसी', 'उसे', 'एक', 'एवं', 'एस', 'ऐसे', 'और', 'कई', 'कर', 'करता', 'करते', 'करना', 'करने', 'करें', 'कहते', \
           'कहा', 'का', 'काफ़ी', 'कि', 'कितना', 'किन्हें', 'किन्हों', 'किया', 'किर', 'किस', 'किसी', 'किसे', 'की', 'कुछ', 'कुल', 'के', \
           'को', 'कोई', 'कौन', 'कौनसा', 'गया', 'घर', 'जब', 'जहाँ', 'जा', 'जितना', 'जिन', 'जिन्हें', 'जिन्हों', 'जिस', 'जिसे', 'जीधर', \
           'जैसा', 'जैसे', 'जो', 'तक', 'तब', 'तरह', 'तिन', 'तिन्हें', 'तिन्हों', 'तिस', 'तिसे', 'तो', 'था', 'थी', 'थे', 'दबारा', 'दिया', \
           'दुसरा', 'दूसरे', 'दो', 'द्वारा', 'न', 'नके', 'नहीं', 'ना', 'निहायत', 'नीचे', 'ने', 'पर', 'पहले', 'पूरा', 'पे', 'फिर', 'बनी', \
           'बही', 'बहुत', 'बाद', 'बाला', 'बिलकुल', 'भी', 'भीतर', 'मगर', 'मानो', 'मे', 'में', 'यदि', 'यह', 'यहाँ', 'यही', 'या', 'यिह', \
           'ये', 'रखें', 'रहा', 'रहे', 'ऱ्वासा', 'लिए', 'लिये', 'लेकिन', 'व', 'वग़ैरह', 'वर्ग', 'वह', 'वहाँ', 'वहीं', 'वाले', 'वुह', 'वे', \
           'सकता', 'सकते', 'सबसे', 'सभी', 'साथ', 'साबुत', 'साभ', 'सारा', 'से', 'सो', 'संग', 'ही', 'हुआ', 'हुई', 'हुए', 'है', 'हैं', \
           'हो', 'होता', 'होती', 'होते', 'होना', 'होने', '']


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
    2: ["कर", "ाओ", "िए", "ाई", "ाए", "ने", "नी", "ना", "ते", \
        "ीं", "ती", "ता", "ाँ", "ां", "ों", "ें"],
    3: ["ाकर", "ाइए", "ाईं", "ाया", "ेगी", "ेगा", "ोगी", "ोगे", "ाने", \
        "ाना", "ाते", "ाती", "ाता", "तीं", "ाओं", "ाएं", "ुओं", "ुएं", "ुआं"],
    4: ["ाएगी", "ाएगा", "ाओगी", "ाओगे", "एंगी", "ेंगी", "एंगे", "ेंगे", "ूंगी",\
        "ूंगा", "ातीं", "नाओं", "नाएं", "ताओं", "ताएं", "ियाँ", "ियों", "ियां"],
    5: ["ाएंगी", "ाएंगे", "ाऊंगी", "ाऊंगा", "ाइयाँ", "ाइयों", "ाइयां"],
}


#-------------------------------------------------Stemming----------------------------------------#
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


#------------ PARSING TEXT-------------------#
#-------------parsing splitting on | and , and then adding space before and after |--------------------#


content={}
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
        per_file_words = list(set(per_file_words))
        per_file_words =list(set(per_file_words)-set(stopwords))
        #time to stem
        per_file_words=stem_terms(per_file_words)
        filename= txtfile.split('\\')[-1]
        texts[filename] = per_file_words
        #content[filename]=txt
        
        words=words+per_file_words
        
    return  texts, list(set(words))

def termsearch(terms): 
    return reduce(set.intersection,
                  (invindex[term] for term in terms),
                  set(texts.keys()))
 

#print('\nWords')
#pp(sorted(words))

#print('\nInverted Index')
#pp({k:sorted(v) for k,v in invindex.items()})


def search_inv_idx(phrase):
    #phrase = '"चुपचाप कुएँ में मिट्टी डालते रहे"'
    global texts,words,invindex,intmd_res
    it_str=''
    result=[]
    start = time.clock()
    texts, words = parsetexts()
    invindex = {word:set(txt for txt, wrds in texts.items() if word in wrds) for word in words}
    query_terms = phrase.strip().strip('"').split()
    query_terms=list(set(query_terms)-set(stopwords))
    query_terms=stem_terms(query_terms)
    intmd_res=list(termsearch(query_terms))
    for i in intmd_res:
        it_str=it_str+ i +'\n'
    
    print('\nTerm Search on full inverted index for: ' + repr(query_terms))
    pp(sorted(termsearch(query_terms)))
    result.append("===========================================================")
    result.append("\n\n\n-------सामान्य खोज के परिणाम---------------\n\n")
    result.append("परिणाम प्राप्त करने के लिए "+  "  " + str(round(time.clock() - start,4))+"s " +"का समय लिया गया")
    result.append(it_str)
    return result
#def main():
    #print("\t\t\t चलो खोज करें\t\t\t\t")
    #query=input("आप क्या खोजना चाहते हैं")
    #query=f'"{query}"'
    #print(query)
    #search_inv_idx(query)
#main()
#search_inv_idx()    
