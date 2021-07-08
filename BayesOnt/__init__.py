import numpy as np
import networkx as nx
import ddot
from ddot import Ontology
from scipy.stats import norm, stats

class BayesOnt:
    def __init__(self):
        pass

    @staticmethod
    #inputs: sim, similarity network between genes;
    #        ont, ontology DAG of with genes at the leaves
    #output: number of edges in sim that is significantly enriched in ont
    def hypergeometricTestPairCount(sim, ont, threshold):
        """
        Converts a string to lowercase
        """
        total = len(sim)*(len(sim)-1)/2
        eCount = len(sim.edges())
        pairCollect = set() #for collecting significant edges
        #propagate genes to full pathways
        ont2 = ont.propagate(direction='forward', gene_term=True, term_term=False)
        for system in ont2.term_2_gene: #per internal terms
            pool = ont2.term_2_gene[system] #all genes connected with the term
            geneSet = [] #for collecting gene pairs
            if len(pool)>1: #make sure the system has more than 1 gene 
                for idx in pool: #grabbing gene ids
                    if ont2.genes[idx] in sim.nodes(): #filter for genes in the network
                        geneSet.append(ont2.genes[idx]) #add gene name
                total2 = len(geneSet)*(len(geneSet)-1)/2
                subG = sim.subgraph(geneSet) #get the subgraph corresponding to the system
                eCount2 = len(subG.edges())
                #print(total-total2-eCount)
                #print(total2-eCount2)
                oddsratio, pvalue = scipy.stats.fisher_exact([[eCount, total-total2-eCount], [eCount2, total2-eCount2]])
                eList = set([frozenset(pair) for pair in subG.edges()])
                #print("pvalue is ")
                #print(pvalue)
                if pvalue<0.01:
                    pairCollect.update(eList)
            #Need to handle case for 1 gene system 
            #Need to handle len(pool)=len(sim) 
        if len(pairCollect)>len(sim.edges()):
            print("overcounted")
        return(len(pairCollect))
