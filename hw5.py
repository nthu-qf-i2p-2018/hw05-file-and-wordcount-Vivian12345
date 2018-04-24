
# coding: utf-8

# In[74]:


import csv
import string

def main(filename):
    with open(filename) as g:
        lines = g.readlines()
        all_words = []
        for line in lines:
            words = line.split()
        # check the format of words and append it to "all_words" list
            for word in words:
                word = word.strip(string.punctuation)
                if word != ' ':
                    all_words.append(word)
        
        w = csv.writer(open("wordcount.csv","w",newline=''),quoting=csv.QUOTE_ALL)
        w.writerow(['word', 'count'])
        for ch in set(all_words):
            w.writerow([ch,str(all_words.count(ch))])
        
        asd = {}
        for ch in set(all_words):
            k = all_words.count(ch)
            asd.update({ch:k})
        import json
        json.dump(asd, open("wordcount.json", 'w'))
        
       
        import pickle
        from collections import Counter
        counter = Counter(all_words)
        pickle.dump(counter, open("wordcount.pkl", 'wb'))
   
        

    
   
main("I_have_a_dream.txt")

