
har=['َ', 'ُ', 'ِ', 'ً', 'ٌ', 'ٍ', 'ّ', 'ْ']
har1=['َ', 'ُ', 'ِ', 'ً', 'ٌ', 'ٍ', 'ْ']
ar=list(' أبجدهوزحطيكلمنسعفصقرشتثخذضظغ ءاةإآؤىئ')
ham= [ 'ء', 'ا']  
taa= ['ت','ة']   
alf= ['إ','أ', 'آ'] 
waw= ['و', 'ؤ']
lam= ['ل','لا','لأ','لإ'] 
yaa=['ي','ى','ئ'] 
ar2=list('بجدهزحطكلمنسعفصقرشتثخذضظغ')
ar3=ham+alf+waw+yaa
en=list('abcdefghijklmnopqrstuvwxyz ')
en2=list('bcdfghjklmnpqrstvxzBCDFGHJKLMNPQRSTVXZ')
en3=list('AEIOUYWaeiouyw')
num=list('1234567890')



hlpl_arabic_tenses=[
'الماضي المعلوم',
 'المضارع المعلوم',
 'المضارع المجزوم',
 'المضارع المنصوب',
 'المضارع المؤكد الثقيل',
 'الأمر',
 'الأمر المؤكد',
 'الماضي المجهول',
 'المضارع المجهول',
 'المضارع المجهول المجزوم',
 'المضارع المجهول المنصوب',
 'المضارع المؤكد الثقيل المجهول ']


hlpl_arabic_pronouns=[
'أنا',
 'أنت',
 'أنتِ',
 'هو',
 'هي',
 'أنتما',
 'أنتما مؤ',
 'هما',
 'هما مؤ',
 'نحن',
 'أنتم',
 'أنتن',
 'هم',
 'هن']

list_articles=[]

dict_0={hlpl_arabic_tenses[0]:'مامع',hlpl_arabic_tenses[1]:'مضمع',hlpl_arabic_tenses[2]:'مضمج',hlpl_arabic_tenses[3]:'مضمن',hlpl_arabic_tenses[4]:'مضمؤثق',hlpl_arabic_tenses[5]:'أم',hlpl_arabic_tenses[6]:'أممؤ',hlpl_arabic_tenses[7]:'مامج',hlpl_arabic_tenses[8]:'مضمج',hlpl_arabic_tenses[9]:'مضمجمج',hlpl_arabic_tenses[10]:'مضمجمن',hlpl_arabic_tenses[11]:'مضمؤثقمج'}
dict_1=dict_1={hlpl_arabic_pronouns[0]:'أنا',hlpl_arabic_pronouns[1]:'أنت',hlpl_arabic_pronouns[2]:'أنتِ',hlpl_arabic_pronouns[3]:'هو',hlpl_arabic_pronouns[4]:'هي',hlpl_arabic_pronouns[5]:'أنتما1',hlpl_arabic_pronouns[6]:'أنتما0',hlpl_arabic_pronouns[7]:'هما1',hlpl_arabic_pronouns[8]:'هما0',hlpl_arabic_pronouns[9]:'نحن',hlpl_arabic_pronouns[10]:'أنتم',hlpl_arabic_pronouns[11]:'أنتن',hlpl_arabic_pronouns[12]:'هم',hlpl_arabic_pronouns[13]:'هن'}

dict_2={'فتحة':'ف','ضمة':'ض','كسرة':'ك'}
dict_3={1:'ة',2:'ون',3:'ات',4:'ين',5:'ان',6:'تان',7:'تا',8:'ا'}

dict_4={'indicative present':'indpre','indicative past tense':'indpas','indicative present continuous':'indprecon','indicative present perfect':'indpreper','infinitive present':'infpre','imperative present':'imppre'}

noun_front=['ال','أ','ب','ت','س','ف','ك','ل','و','يا','ها']+['بال','تال','فال','وال','ياال','أب','أس','أف','']    
noun_back=['ك','كم','هم','هنّ','ي','ا','ى','']

verb_front=['أ','ت','س','ف','ل','و','أف','أس','']    
verb_back=['ك','كم','هم','هنّ','ني','']

def hlpl_rebit_remover(lst):
    lst2=[]
    for x in lst:
        if x not in lst2:
           lst2.append(x)
    return lst2


def hlpl_lst_to_st(lst,s):
    st=''
    for x in lst:
        st+=x+s
    st=st[0:len(st)-len(s)]
    return st
    
def hlpl_remover(st,lst):
    st2=''
    for x in st:
        if x not in lst:
           st2+=x
    return st2

def hlpl_word_template(word,case):
    template=''
    if case=='en':
       for x in word:
           if x in en3:
              template+=x.lower()
           if x in en2:
              for y in en2:
                  if y not in template:
                     template+=y
                     break
    if case=='ar':
       for x in word:
           if x in ar3:
              template+=x
           if x in ar2:
              for y in ar2:
                  if y not in template:
                     template+=y
                     break                                   
    return template
  
  
 
b1='[';b2=']'
def hlpl_arabic_phrase_template(phrase,cur):
    st2='';dct={}
    lst=phrase.split()  
    for x in lst:
        y='"'+x+'"';lst2=[]
        row0=cur.execute("SELECT * FROM ar_articles_lst WHERE word="+y).fetchone()
        if row0!=None:
           st2+=b1+x+b2+' '
           dct[x]=x
        else:
           k=0
           row1=cur.execute("SELECT * FROM ar_nouns_lst WHERE word="+y).fetchone()
           row2=cur.execute("SELECT * FROM ar_verbs_lst WHERE word="+y).fetchone()

           if row1!=None:
              lst2.append(row1[1]);k=1
           if row2!=None:
              lst2.append(row2[1]);k=1              
           if k==0:
              lst2.append(x) 
           xxx=hlpl_lst_to_st(lst2,' ')  
           dct[x]=xxx           
           st2+=b1+xxx+b2+' '
    return dct,st2
 
 
def hlpl_english_phrase_template(st,cur):
    st2='';dct={}
    lst=st.split(' ')
    for x in lst:
        y='"'+x+'"';lst2=[]
        row0=cur.execute("SELECT * FROM en_articles_lst WHERE word="+y).fetchone()
        if row0!=None:
           st2+=b1+x+b2+' '
           dct[x]=x
        else:
           row1=cur.execute("SELECT * FROM en_adv_lst WHERE word="+y).fetchone()
           row2=cur.execute("SELECT * FROM en_adj_lst WHERE word="+y).fetchone()
           row3=cur.execute("SELECT * FROM en_nouns_s_lst WHERE word="+y).fetchone()
           row4=cur.execute("SELECT * FROM en_nouns_p_lst WHERE word="+y).fetchone()
           row5=cur.execute("SELECT * FROM en_verbs_lst WHERE word="+y).fetchone()

           k=0
           if  row1!=None:
              lst2.append(row1[1]);k=1  
           if  row2!=None:
              lst2.append(row2[1]);k=1  
           if  row3!=None:
              lst2.append(row3[1]);k=1  
           if  row4!=None:
              lst2.append(row4[1]);k=1  
           if  row5!=None:
              lst2.append(row5[1]);k=1  
           if k==0:
              lst2.append(x) 
           xxx=hlpl_lst_to_st(lst2,' ')  
           dct[x]=xxx           
           st2+=b1+xxx+b2+' '
    return dct,st2
    
        

pt='.'
def hlpl_remove_point(xxx):
   try:
    if xxx[0]=='.':
       xxx=xxx[1:len(xxx)]
    if xxx[len(xxx)-1]=='.':
       xxx=xxx[0:len(xxx)-1]
    if '..' in xxx:
       xxx=xxx[0:xxx.index('..')]+xxx[xxx.index('..')+1:len(xxx)]          
    return xxx
   except:
    return xxx
 
def hlpl_rl(st):
    st=st.split()[0]
    if st[len(st)-1] in har1:
       st=st[0:len(st)-1]
    if st[len(st)-1] =='ة':
       st=st[0:len(st)-1]
    if st[len(st)-1] in har1:
       st=st[0:len(st)-1] 
    return st 
  


"""  
import libqutrub 
from libqutrub.mosaref_main import do_sarf
def hlpl_arabic_verbs_templates(verb):
        templates_list={}
        for y in ('فتحة', 'ضمة', 'كسرة'):
            x_conjugated=do_sarf(verb, y, alltense = True, past = True, future = True,passive = True, imperative = True,future_moode = True, confirmed = True,transitive = True, display_format = "DICT")
            if x_conjugated!=None:
             for z in x_conjugated.keys(): 
                for w in x_conjugated[z].keys():
                    word=x_conjugated[z][w]
                    template=dict_1[w]+pt+hlpl_word_template(verb,'ar')+pt+dict_0[z]+pt+dict_2[y]
                    if word not in templates_list.keys():
                       templates_list[word]=[template]
                    else:
                       templates_list[word].append(template)
                    for z2 in verb_front:
                        for w2 in verb_back:
                            xxx=z2+word+w2
                            yyy=z2+pt+template+pt+w2
                            xxx=hlpl_remove_point(xxx)
                            yyy=hlpl_remove_point(yyy)
                            if xxx not in templates_list.keys():
                               templates_list[xxx]=[yyy]
                            else:
                              templates_list[xxx].append(yyy)
        return templates_list  """                  
        
      
      
def hlpl_arabic_nouns_templates(noun,prefix=''):
        templates_list={}
        noun=hlpl_rl(noun)
        for y in range(1,9):
            word=noun+dict_3[y]
            if prefix=='':
               template=hlpl_word_template(noun,'ar')+pt+dict_3[y] 
            else:
               template=prefix+'.'+hlpl_word_template(noun,'ar')+pt+dict_3[y] 
               template2=hlpl_word_template(noun,'ar')+pt+dict_3[y] 
            if word not in templates_list.keys():
               templates_list[word]=[template]
            else:
               templates_list[word].append(template)
            for z in noun_front:
                for w in noun_back:
                
                    if w!='':
                       xxx=z+hlpl_rl(word)+w
                    else:
                       xxx=z+word+w
                       
                    if prefix=='':
                       yyy= z+pt+template+pt+w
                    else:
                       yyy= prefix+'.'+z+pt+template2+pt+w
                       
                    xxx=hlpl_remove_point(xxx)
                    yyy=hlpl_remove_point(yyy)                    
                    if xxx not in templates_list.keys():
                       templates_list[xxx]=[yyy]
                    else:
                       templates_list[xxx].append(yyy)
        return templates_list

def hlpl_articles_templates(article):
            templates_list={}      
            templates_list[article]=[article]
            return templates_list



lst_adj=[];lst_adv=[];lst_n_s=[];lst_n_p=[];lst_v=[]
def hlpl_english_nouns_templates(word,case):
    templates_list={}
    if case=='adj':
            template=hlpl_word_template(word,'en')+'.adj'
            templates_list[word]=[template]

    if case=='adv':
            template=hlpl_word_template(word,'en')+'.adv'     
            templates_list[word]=[template]

    if case=='ns':
            template=hlpl_word_template(word,'en')+'.ns'      
            templates_list[word]=[template]

    if case=='np':
            template=hlpl_word_template(word,'en')+'.np'      
            templates_list[word]=[template]

    return templates_list



"""
import mlconjug3 
default_conjugator = mlconjug3.Conjugator(language='en')
def hlpl_english_verbs_templates(verb): 
        templates_list={}  
        x_conjugated = default_conjugator.conjugate(verb).iterate()
        for i in range(len(x_conjugated)):
            y=x_conjugated[i]
            if i==24:
               word='to-'+y[2].split()[1]
            else:
               word=y[3]
            template=hlpl_word_template(verb,'en')+pt+dict_4[y[1]]+pt+y[2]
            if word not in templates_list.keys():            
               templates_list[word]=[template]
            else:
               templates_list[word].append(template)       
        return templates_list"""




def hlpl_extract_phrases(txts,n):
    lst_phrases=[]
    for txt in txts:
        lst1=txt.split();len1=len(lst1)
        for j in range(1,n):
            i=0
            while i+j<=len1:
                  lst_phrases.append(hlpl_lst_to_st(lst1[i:i+j],' '))
                  i+=1
    return lst_phrases 
    
    
en=list('abcdefghijklmnopqrstuvwxyz')
ar=list('أبجدهوزحطيكلمنسعفصقرشتثخذضظغءاةإآؤىئ')   
def hlpl_phrases_codes(phrase,case):
    dct_codes={};code=''
    if case=='ar':
           for x in ar:
               code+=str(phrase.count(x))
    if case=='en':
           for x in en:
               code+=str(phrase.count(x))+str(phrase.count(x.upper()))             
    return code

















    
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 