#!/usr/bin/env python
# coding: utf-8

# In[19]:


from pyopenms import *
feature = Feature()
feature.setMZ( 500.9 )
feature.setCharge(2)
feature.setRT( 1500.1 )
feature.setIntensity( 30500 )
feature.setOverallQuality( 10 )


# In[20]:


fm = FeatureMap()
fm.push_back(feature)
feature.setRT(1600.5 )
feature.setCharge(2)
feature.setMZ( 600.0 )
feature.setIntensity( 80500.0 )
fm.push_back(feature)
FeatureXMLFile().store("test.featureXML", fm)


# In[21]:


fmap = FeatureMap()
FeatureXMLFile().load("test.featureXML", fmap)
for feature in fmap:
    print("Feature: ", feature.getIntensity(), feature.getRT(), feature.getMZ())


# In[22]:


feature = ConsensusFeature()
feature.setMZ( 500.9 )
feature.setCharge(2)
feature.setRT( 1500.1 )
feature.setIntensity( 80500 )

f_m1 = ConsensusFeature()
f_m1.setRT(500)
f_m1.setMZ(300.01)
f_m1.setIntensity(200)
f_m1.ensureUniqueId()
 
f_m2 = ConsensusFeature()
f_m2.setRT(505)
f_m2.setMZ(299.99)
f_m2.setIntensity(600)
f_m2.ensureUniqueId()
feature.insert(1, f_m1 )
feature.insert(2, f_m2 )
for fh in feature.getFeatureList():
    print(fh.getMapIndex(), fh.getIntensity(), fh.getRT())

print(feature.getMZ())
feature.computeMonoisotopicConsensus()
print(feature.getMZ())



# In[23]:


cmap = ConsensusMap()
fds = { 1 : ColumnHeader(), 2 : ColumnHeader() }
fds[1].filename = "file1"
fds[2].filename = "file2"
cmap.setColumnHeaders(fds)

feature.ensureUniqueId()
cmap.push_back(feature)
ConsensusXMLFile().store("test.consensusXML", cmap)

cmap = ConsensusMap()
ConsensusXMLFile().load("test.consensusXML", cmap)
for cfeature in cmap:
    cfeature.computeConsensus()
    print("ConsensusFeature", cfeature.getIntensity(), cfeature.getRT(), cfeature.getMZ())
    
for fh in cfeature.getFeatureList():
     print(" -- Feature", fh.getMapIndex(), fh.getIntensity(), fh.getRT())

