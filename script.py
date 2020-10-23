import math
import numpy as np

#This functions reads the dataset of words and lyrics and indexes all the words by ids and collects songs from dataset and return them
def dataset(filename):

    dataset = open(filename)
    lines = [line.rstrip('\n') for line in open(filename)]
    dataset.close()

    words= lines[17][1:].split(',') 	#distinct words in the dataset
    songs = lines[18:] 			#describe each song

    words_by_id = {}
    id_by_word = {}
    id = 1
    for i in words:
        words_by_id[id] = i
        id_by_word[i]=int(id)
        id += 1

    return words_by_id, songs, id_by_word


#Read dataset and gather Song details and index by Song id
def get_song_details(filename):

    dataset = open(filename)
    lines = [line.rstrip('\n') for line in open(filename)]
    dataset.close()
    lines = lines[18:]

    song_details_by_songid = {}

    for i in lines:
        string = i.split('<SEP>')
        details = {}
        details['Artist'] = string[2]
        details['Title'] = string[3]
        song_details_by_songid[string[0]] = details

    return song_details_by_songid


#Iterate through all lyrics and Calculate tf-idf score of each word in every lyrics of given songs
def tf_idf_calc(songs):

    word_freq={}
    tf_by_songid = {}
    N = 0 		#Corpus size
    df_wordid = {}	
    idf_by_wordid = {}

    k = 1
    for i in songs:
	    #For each song
        tf_by_wordid = {}
        total_words = 0
        string = i.split(',')
        song_id = string[0]
    
    for j in range(2, len(string)):
        string2 = string[j]
        word_freq = string2.split(':')
        tf_by_wordid[int(word_freq[0])] = float(word_freq[1])
        total_words +=  int(word_freq[1])
        
        try:
            df_wordid[int(word_freq[0])] += 1
        except Exception as e:
            df_wordid[int(word_freq[0])] = 1
    
    for i in tf_by_wordid:
        tf_by_wordid[i] = tf_by_wordid[i]/total_words
        
    tf_by_songid[song_id] = tf_by_wordid
    N += total_words

    for i in df_wordid:
	    idf_by_wordid[i] = 1 + math.log(N/df_wordid[i])

    tf_idf_by_songid={}


    for i in tf_by_songid: #for each song
	    tf_idf = {}
    tf_scores_by_wordid = tf_by_songid[i]
    
    
    for j in tf_scores_by_wordid: #for each word
        tf = tf_scores_by_wordid[j]
        idf = idf_by_wordid[j]
        tf_idf[j] = tf*idf

    tf_idf_by_songid[i] = tf_idf
	
    #print(tf_idf_by_songid)
    return tf_idf_by_songid



#Calculate Cosine Score of every song with respect to query and return top 10 songs with their ids
def cosine_simi(query, word_by_id, id_by_word, tf_idf_by_song_id):

    qv = np.zeros(len(word_by_id)) #query vector
    ids = {}
    sim_by_songid = {}
    
    a = 1
    for i in query:
	    ids[a] = id_by_word[i]
	    a += 1

    for i in ids:
	    qv[ids[i]-1] = 1


    for i in tf_idf_by_song_id:
	    song_id = i
    
    dv = np.zeros(len(word_by_id)) #document vector
    
    for j in tf_idf_by_song_id[i]:
        dv[j-1] = tf_idf_by_song_id[i][j]
        
    sim_by_songid[song_id] = cosine(qv, dv)
    
    print("before")
    print(sim_by_songid)
    sorted_scores = sorted(sim_by_songid.items(), key=lambda yug: yug[1], reverse=True)
    print("after")
    print(sorted_scores)

    relevant_songs=[]
    for i in sorted_scores:
        relevant_songs.append([i[0],i[1]])

    return relevant_songs[0:10]


def cosine(v1, v2):
    v1 = np.array(v1)
    v2 = np.array(v2)

    return np.dot(v1, v2) / (np.sqrt(np.sum(v1**2)) * np.sqrt(np.sum(v2**2)))
