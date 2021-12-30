#!/usr/bin/env python
# coding: utf-8

# In[52]:


from pyopenms import *
from urllib.request import urlretrieve
gh = "https://raw.githubusercontent.com/OpenMS/pyopenms-extra/master"
urlretrieve (gh + "/src/data/P02769.fasta", "bsa.fasta")
dig = ProteaseDigestion()
dig.getEnzymeName()
bsa = "".join([l.strip() for l in open("uniprot-yourlist_M202112144ABAA9BC7178C81CEBC9459510EDDEA3365A72Z.fasta").readlines()[1:]])
bsa = AASequence.fromString(bsa)
result = []
dig.digest(bsa, result)
print(result[4].toString())
len(result)

