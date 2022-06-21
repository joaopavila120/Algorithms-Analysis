import cProfile, pstats, io

def profile(fnc):
    
    def inner(*args, **kwargs):
        
        #startando o profile
        pr = cProfile.Profile()
        pr.enable()
        #executando a funcao com os argumentos
        retval = fnc(*args, **kwargs)
        #pausando o profile
        pr.disable()
        #pegando a resposta (out, binary)
        s = io.StringIO()
        #imprimindo os resultados
        sortby = 'cumulative'
        ps = pstats.Stats(pr, stream=s).sort_stats(sortby)
        ps.print_stats()
        print(s.getvalue())
        return retval

    return inner

###################################################################################################
def read_movies(src):
    
    with open(src) as fd:
        return fd.read().splitlines()
    
###################################################################################################
#agulha e palheiro
def is_duplicate(needle, haystack):
    
    for movie in haystack:
        if needle.lower() == movie.lower():
        #na versao middle
        #if needle == movie:
            return True
    return False
    


###################################################################################################
@profile
def find_duplicate_movies_v4_final_fast(src='movies.txt'):
    
    movies = read_movies(src)
    movies = [movie.lower() for movie in movies]
    movies.sort()
    duplicates = [movie1 for movie1, movie2 in zip(movies[:-1], movies[1:]) if movie1 == movie2]
    return duplicates

#@profile
def find_duplicate_movies_v3(src='movies.txt'):
    
    movies = read_movies(src)
    #adicionar essa linha inicialmente
    movies = [movie.lower() for movie in movies]
    duplicates = []
    while movies:
        movie = movies.pop()
        #if is_duplicate(movie, movies):
        if movie in movies:
            duplicates.append(movie)
    return duplicates



###################################################################################################
#@profile
def find_duplicate_movies_v2(src='movies.txt'):
    
    movies = read_movies(src)
    #adicionar essa linha inicialmente
    movies = [movie.lower() for movie in movies]
    duplicates = []
    while movies:
        #remove um item da lista ate esvaziar ela...fim do laço
        movie = movies.pop()
        if is_duplicate(movie, movies):
            duplicates.append(movie)
    return duplicates



###################################################################################################
#@profile
def find_duplicate_movies_v1(src='movies.txt'):
 
 movies = read_movies(src)
 duplicates = []
 while movies:
     #remove um item da lista ate esvaziar ela...fim do laço
     movie = movies.pop()
     if is_duplicate(movie, movies):
         duplicates.append(movie)
 return duplicates

###################################################################################################
find_duplicate_movies_v4_final_fast() #lembrar de descomentar o @profile
#find_duplicate_movies_middle()
#print(find_duplicate_movies_v4_final_fast())