#!/usr/bin/env python
# coding: utf-8

# In[38]:


protein_id = ProteinIdentification()
peptide_id = PeptideIdentification()
protein_id.setIdentifier("IdentificationRun1")
peptide_id.setIdentifier("IdentificationRun1")
print("Protein Identifier -", protein_id.getIdentifier())
print("Peptide Identifier -", peptide_id.getIdentifier())


# In[39]:


from pyopenms import *
protein_id = ProteinIdentification()
protein_id.setIdentifier("IdentificationRun1")
protein_hit = ProteinHit()
protein_hit.setAccession("sp|MyAccession")
protein_hit.setSequence("PEPTIDERDLQMTQSPSSLSVSVGDRPEPTIDE")
protein_hit.setScore(1.0)
protein_hit.setMetaValue("target_decoy", b"target")

protein_id.setHits([protein_hit])


# In[40]:


now = DateTime.now()
date_string = now.getDate()
protein_id.setDateTime(now)

 
search_parameters = SearchParameters()  
search_parameters.db = "database"
search_parameters.charges = "+2"
protein_id.setSearchParameters(search_parameters)

 
protein_id.setSearchEngineVersion("v1.0.0")
protein_id.setSearchEngine("SearchEngine")
protein_id.setScoreType("HyperScore")

 
for hit in protein_id.getHits():
  print("Protein hit accession:", hit.getAccession())
  print("Protein hit sequence:", hit.getSequence())
  print("Protein hit score:", hit.getScore())


# In[42]:


peptide_id = PeptideIdentification()
peptide_id.setRT(1243.56)
peptide_id.setMZ(440.0)
peptide_id.setScoreType("ScoreType")
peptide_id.setHigherScoreBetter(False)
peptide_id.setIdentifier("IdentificationRun1")
peptide_id.setMetaValue("AdditionalMetaValue", "Value")
peptide_hit = PeptideHit()
peptide_hit.setScore(1.0)
peptide_hit.setRank(1)
peptide_hit.setCharge(2)
peptide_hit.setSequence(AASequence.fromString("DLQM(Oxidation)TQSPSSLSVSVGDR"))
ev = PeptideEvidence()
ev.setProteinAccession("sp|MyAccession")
ev.setAABefore(b"R")
ev.setAAAfter(b"P")
ev.setStart(123)  
ev.setEnd(141)
peptide_hit.setPeptideEvidences([ev])
peptide_hit2 = PeptideHit()
peptide_hit2.setScore(0.5)
peptide_hit2.setRank(2)
peptide_hit2.setCharge(2)
peptide_hit2.setSequence(AASequence.fromString("QDLMTQSPSSLSVSVGDR"))
peptide_hit2.setPeptideEvidences([ev])
peptide_id.setHits([peptide_hit, peptide_hit2])


# In[43]:


peptide_ids = [peptide_id]
for peptide_id in peptide_ids:
    
  print ("Peptide ID m/z:", peptide_id.getMZ())
  print ("Peptide ID rt:", peptide_id.getRT())
  print ("Peptide ID score type:", peptide_id.getScoreType())

  for hit in peptide_id.getHits():
    print(" - Peptide hit rank:", hit.getRank())
    print(" - Peptide hit sequence:", hit.getSequence())
    print(" - Peptide hit score:", hit.getScore())
    print(" - Mapping to proteins:", [ev.getProteinAccession()
                                        for ev in hit.getPeptideEvidences() ] )


# In[44]:


IdXMLFile().store("out.idXML", [protein_id], peptide_ids)
prot_ids = []; pep_ids = []
IdXMLFile().load("out.idXML", prot_ids, pep_ids)
 
for protein_id in prot_ids:
  for hit in protein_id.getHits():
    print("Protein hit accession:", hit.getAccession())
    print("Protein hit sequence:", hit.getSequence())
    print("Protein hit score:", hit.getScore())
    print("Protein hit target/decoy:", hit.getMetaValue("target_decoy"))
 
for peptide_id in pep_ids:
  
  print ("Peptide ID m/z:", peptide_id.getMZ())
  print ("Peptide ID rt:", peptide_id.getRT())
  print ("Peptide ID score type:", peptide_id.getScoreType())
   
  for hit in peptide_id.getHits():
    print(" - Peptide hit rank:", hit.getRank())
    print(" - Peptide hit sequence:", hit.getSequence())
    print(" - Peptide hit score:", hit.getScore())
    print(" - Mapping to proteins:", [ev.getProteinAccession() for ev in hit.getPeptideEvidences() ] )

