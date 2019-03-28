
# coding: utf-8

# In[18]:


import itertools
def card(a,b,c,d):
    list1=[a,b,c,d]
    m=itertools.permutations(list1,4)  
    p=[]
    for t in m:
        p.append(list(t))
    for w in p:
        if w[0]+w[1]+w[2]+w[3]==24:    ##+
            return "ok","{}+{}+{}+{}".format(w[0],w[1],w[2],w[3])
        elif w[0]+w[1]+w[2]-w[3]==24:   ##+-
            return "ok","{}+{}+{}-{}".format(w[0],w[1],w[2],w[3])
        elif w[0]+w[1]-w[2]-w[3]==24:
            return "ok","{}+{}-{}-{}".format(w[0],w[1],w[2],w[3])
        elif (w[0]+w[1]+w[2])*w[3]==24:##+ *
            return "ok","({}+{}+{})*{}".format(w[0],w[1],w[2],w[3])
        elif w[0]+(w[1]+w[2])*w[3]==24:##+ *
            return "ok","{}+({}+{})*{}".format(w[0],w[1],w[2],w[3])
        elif w[0]+w[1]+w[2]*w[3]==24:##+ *
            return "ok","{}+{}+{}*{}".format(w[0],w[1],w[2],w[3])
        elif (w[0]+w[1])*w[2]*w[3]==24:  ##**+
            return "ok","({}+{})*{}*{}".format(w[0],w[1],w[2],w[3])
        elif (w[0]+w[1]*w[2])*w[3]==24:  ##**+
            return "ok","({}+{}*{})*{}".format(w[0],w[1],w[2],w[3])
        elif w[0]+w[1]*w[2]*w[3]==24:  ##**+
            return "ok","{}+{}*{}*{}".format(w[0],w[1],w[2],w[3])
        elif w[0]*w[1]*w[2]*w[3]==24:
            return "ok","{}*{}*{}*{}".format(w[0],w[1],w[2],w[3])
        elif w[0]*w[1]*w[2]/w[3]==24:  ##*/
            return "ok","{}*{}*{}/{}".format(w[0],w[1],w[2],w[3])
        elif w[0]*w[1]/w[2]/w[3]==24:
            return "ok","{}*{}/{}/{}".format(w[0],w[1],w[2],w[3])
        elif w[0]+w[1]+w[2]/w[3]==24: ##+/
            return "ok","{}+{}+{}/{}".format(w[0],w[1],w[2],w[3])
        elif w[0]+w[1]/w[2]/w[3]==24: 
            return "ok","{}+{}/{}/{}".format(w[0],w[1],w[2],w[3])
        elif w[0]+w[1]-w[2]*w[3]==24:  ##+-*
            return "ok","{}+{}-{}*{}".format(w[0],w[1],w[2],w[3])
        elif w[0]+(w[1]-w[2])*w[3]==24:  ##+-*
            return "ok","{}+({}-{})*{}".format(w[0],w[1],w[2],w[3])
        elif (w[0]+w[1]-w[2])*w[3]==24:  ##+-*
            return "ok","({}+{}-{})*{}".format(w[0],w[1],w[2],w[3])
        elif w[0]+w[1]-w[2]/w[3]==24:  ##+-/
            return "ok","{}+{}-{}/{}".format(w[0],w[1],w[2],w[3])
        elif (w[0]+w[1])*w[2]/w[3]==24: ##+*/
            return "ok","({}+{})*{}/{}".format(w[0],w[1],w[2],w[3])
        elif (w[0]+w[1]*w[2])/w[3]==24: ##+*/
            
            return "ok","({}+{}*{})/{}".format(w[0],w[1],w[2],w[3])
        elif (w[0]+w[1]/w[2])*w[3]==24: ##+*/
            return "ok","({}+{}/{})*{}".format(w[0],w[1],w[2],w[3])
        elif (w[0]-w[1])*w[2]/w[3]==24: ##-*/
            return "ok","({}-{})*{}/{}".format(w[0],w[1],w[2],w[3])
        elif (w[0]-w[1]*w[2])/w[3]==24:
            return "ok","({}-{}*{})/{}".format(w[0],w[1],w[2],w[3])
        elif  w[0]-w[1]*w[2]/w[3]==24: ##-*/
            return "ok","{}-{}*{}/{}".format(w[0],w[1],w[2],w[3])
    return "No","error"


# # example

# In[24]:


a,b=card(4,12,4,1)
print(a,b)

#ok  12+(4-1)*4

