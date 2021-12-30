#!/usr/bin/env python
# coding: utf-8

# In[47]:


dig = ProteaseDigestion()
dig.getEnzymeName()
bsa = "".join([l.strip() for l in open("uniprot-yourlist_M202111216320BA52A5CE8FCD097CB85A53697A35301FDED.fasta").readlines()[1:]])
bsa = AASequence.fromString(bsa)
result = []
dig.digest(bsa, result)
peptides = [AASequence.fromString(s.toString()) for s in result]
for peptide in peptides:
    tsg = TheoreticalSpectrumGenerator()
    spec1 = MSSpectrum()
    p = Param()
    p.setValue("add_b_ions", "false")
    p.setValue("add_metainfo", "true")
    tsg.setParameters(p)
    tsg.getSpectrum(spec1, peptide, 1, 1)
    print("Spectrum 1 of", peptide, "has", spec1.size(), "peaks.")
    for ion, peak in zip(spec1.getStringDataArrays()[0], spec1):
        print(ion.decode(), "is generated at m/z", peak.getMZ())


# In[ ]:




