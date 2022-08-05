# NOMBRE (apellido, nombre):

# Carga de librerías necesarias


def download_pubmed(dengue): 
    """
    Se descarcará información de PubMed para la obtención de información
    sobre opiniones, metodologías y técnicas sobre el manejo de la bacteria   
    bacillus subtilis.
    """
    Entrez.email = "diego.carranco@est.ikiam.edu.ec"
    handle = Entrez.esearch(db="pubmed", 
                        term="dengue [Title/Abstract]",
                        usehistory="y")
    record = Entrez.read(handle)
    id_list = record["IdList"]
    record["Count"]
    return record, id_list
    
    
    
    
    
    
    
    
    
    
    return 



def mapscience(       ):
    """
    Docstring map_science
    
    
    
    
    
    
    
    """
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    return 

    