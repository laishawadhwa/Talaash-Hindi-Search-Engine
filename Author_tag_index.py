from pprint import pprint as pp
from glob import glob
try: reduce
except: from functools import reduce
try:    raw_input
except: raw_input = input
import time 
 
def parsetexts(bit,fileglob='C:\\Users\\laisha wadhwa\\Documents\\sem5\\IR\\project\\IR project_IR_Course\\InputFiles\\*.txt'):
    texts, texts2,w1,w2 = {}, {},[],[]
    
    for txtfile in glob(fileglob):
        
        f=open(txtfile, encoding='utf-8-sig')
        tag = f.readline().rstrip()
        author= f.readline().rstrip()
        w1.append(tag)
        w2.append(author)
        texts[txtfile.split('\\')[-1]] = tag
        texts2[txtfile.split('\\')[-1]] = author
    if bit==2:
        return texts, list(set(w1))
    else:
        return texts2, list(set(w2))
    return 
 
def termsearch(term,bit): # Searches simple inverted index
    if bit==2:
        return invindex_tag[term]
    else:
        return invindex_author[term]
 



   
def author_search(author):
    global invindex_author
    Author_result,intmd_resu,it_str=[],[],''
    start = time.clock()
    texts, words = parsetexts(1)
    print('\nTexts')
    pp(texts)
    print('\nWords')
    pp(sorted(words))
    invindex_author = {word:set(txt
                        for txt, wrds in texts.items() if word in wrds)
            for word in words}
    print('\nInverted Index')
    pp({k:sorted(v) for k,v in invindex_author.items()})
    print('\nTerm Search for: ' + repr(author))
    intmd_resu=list(termsearch(author,1))
    for i in range(len(intmd_resu)):
        it_str=it_str+str(i+1)+ " " +  intmd_resu[i] +'\n'
    Author_result.append("===========================================================")
    Author_result.append("\n\n\n------- लेखक नाम से खोज के परिणाम---------------\n\n")
    Author_result.append("परिणाम प्राप्त करने के लिए "+  "  " + str(round(time.clock() - start,4))+ "s " +" का समय लिया गया")
    Author_result.append(it_str)    
    return Author_result
    #print("Search results obtained in"+  "  " + str(round(time.clock() - start,4))+"s")

def category_search(category):
    #category=input("Enter Category Name")
    #author index----------#
    global invindex_tag
    start = time.clock()
    categ_result,intmd_resu2,it_st=[],[],''
    texts2, words2=parsetexts(2)
    print('\nTexts2')
    pp(texts2)
    print('\nWords')
    pp(sorted(words2))
    invindex_tag= {word:set(txt
                        for txt, wrds in texts2.items() if word in wrds)
            for word in words2}
    print('\nInverted Index')
    pp({k:sorted(v) for k,v in invindex_tag.items()})

    print('\nTerm Search for: ' + repr(category))
    intmd_resu2=list(termsearch(category,2))
    for i in range(len(intmd_resu2)):
        it_st=it_st+str(i+1)+ " " +  intmd_resu2[i] +'\n'
    categ_result.append("===========================================================")
    categ_result.append("\n\n\n------- वर्ग के नाम से खोज के परिणाम---------------\n\n")
    categ_result.append("परिणाम प्राप्त करने के लिए "+  "  " + str(round(time.clock() - start,4))+"s " + "का समय लिया गया")
    categ_result.append(it_st)    
    return categ_result
    #print("Search results obtained in"+  "  " + str(round(time.clock() - start,4))+"s")
    
    

   
