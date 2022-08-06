# NOMBRE (Carranco, Diego):

from Bio import Entrez
from Bio import SeqIO
from Bio import GenBank
def download_pubmed(keyword): 
    """Permite descargar articulos desde PUB med"""
    Entrez.email = 'diego.carranco@est.ikiam.edu.ec'
    handle = Entrez.esearch(db="pubmed", term= keyword, usehistory="y")
    record = Entrez.read(handle)
    id_list = record["IdList"]
    record["Count"]
    webenv = record["WebEnv"]
    query_key = record["QueryKey"]
    handle = Entrez.efetch(db="pubmed", rettype="medline", retmode="text", retstart=0, retmax=543, webenv=webenv, query_key=query_key)
    out_handle = open("data/resultado_pubmed.txt", "w")
    resultado = handle.read()
    handle.close()
    out_handle.write(resultado)
    out_handle.close()
    return (id_list)  

import csv 
import re
import pandas as pd 
from collections import Counter

def science_plots(data):
    """Función para poder obtener los cinco paises que presentan mayor frecuencia"""
    
    with open("data/"+data, errors="ignore") as l: 
        texto = l.read()
    texto = re.sub(r"\n\s{6}", " ", texto)
    countries_1 = re.findall (r"AD\s{2}-\s[A-Za-z].*,\s([A-Za-z]*)\.\s", texto)
    unique_countries = list(set(countries_1))
    conteo=Counter(countries_1)
    resultado={}
     for clave in conteo:  
        valor=conteo[clave]
        if valor > 1:
            resultado[clave] = valor
    ordenar = (sorted(resultado.values()))
    ordenar.sort(reverse=True)
    import operator
    pais = [] 
    contador = []
        reverse = sorted(resultado.items(), key=operator.itemgetter(1), reverse=True)   
    for name in enumerate(reverse):
        pais.append(name[1][0])
        contador.append(resultado[name[1][0]])
    paises_cinco = pais[0:5]
    frecuencia_cinco = contador [0:5]
    fig = plt.figure(figsize =(10, 7))
    plt.pie(frecuencia_cinco, labels = paises_cinco)
    (plt.savefig("img/"+data, dpi=100, bbox_inches='tight'))
    plt.show()
    
