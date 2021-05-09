
b1=open("book1.txt",'r',encoding='utf-8')
b2=open("book2.txt",'r',encoding='utf-8')

b1_words=set()
b2_words=set()
punc = '''!()-[]{};:'"\, <>./?@#$%^&*_~'''

for w in b1.read().split():
    for x in w :
        if x in punc :
            w=w.replace(x,"")
    
    b1_words.add(w.lower())
        
for word in b2.read().split():
    for x in w :
        if x in punc :
            w=w.replace(x,"")
    
    b2_words.add(word.lower())       
        
#common_words = b1_words.intersection(b2_words) - {'i', 'a', 'an', 'is', 'are', 'm', 'am', 'to', 'in', 'into', 'on', 'onto', 'in', 'at', 'on', 'inside', 'since', 'for', 'by', 'during', 'from', 'with', 'within', 'over', 'above', 'below', 'beneath', 'under', 'underneath', 'he', 'we', 'you', 'she', 'they', 'it', 'of', 'by', 'do', 'does', 'did', 'there', 'this', 'that', 'these', 'those', 'me', 'him', 'her', 'us', 'them'}     
c_words=b1_words.intersection(b2_words)
print (c_words)