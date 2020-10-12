import math

#This functions reads the dataset of words and lyrics and indexes all the words by ids and collects songs from dataset and return them
def dataset1(filename):
    dataset = open(filename)
    lines = [line.rstrip('\n') for line in open(filename)]
    dataset.close()

    words= lines[17][1:].split(',') #distinct words in the dataset
    songs = lines[18:] #describe each song
    word_by_id={}
    id_by_word={}
    id=1
    for i in words:
        word_by_id[id]=i
        id_by_word[i]=int(id)
        id+=1
    return words,word_by_id,id_by_word,songs

#Iterate through all lyrics and Calculate tf-idf score of each word in every lyrics of given songs
def tf_idf_calculation(songs):
    lyrics_by_songid_tf_score={}
    songlength_by_songid={}
    idf_by_wordid={}
    word_id_doc_freq={}
    for i in songs:
        a=i.split(',')
        tf={}
        le=0
        for j in range(2,len(a)):
            string=a[j]
            word_id_and_freq=string.split(':')
            tf[int(word_id_and_freq[0])]=float(word_id_and_freq[1])
            le+=int(word_id_and_freq[1])
            try:
                word_id_doc_freq[int(word_id_and_freq[0])]+=1
            except Exception as e:
                word_id_doc_freq[int(word_id_and_freq[0])]=1
        songlength_by_songid[a[0]]=le
        for i in tf:
            tf[i]=tf[i]/le
        lyrics_by_songid_tf_score[a[0]]=tf


    for i in word_id_doc_freq:
        idf_by_wordid[i]=1+math.log(len(lyrics_by_songid_tf_score)/word_id_doc_freq[i])

    song_tf_idf_by_songid={}
    for i in lyrics_by_songid_tf_score:
        toapp={}
        dic=lyrics_by_songid_tf_score[i]
        for j in dic:
            tf=dic[j]
            idf=idf_by_wordid[j]
            toapp[j]=tf*idf
        song_tf_idf_by_songid[i]=toapp
    return song_tf_idf_by_songid


#Read dataset and gather Song details and index by Song id
def get_song_details(filename):
    dataset=open(filename)
    lines=[line.rstrip('\n') for line in open(filename)]
    dataset.close()

    song_details_by_songid={}
    for i in lines:
        string=i.split(',')
        details={}
        details['Artist_name']=string[2]
        details['Title']=string[1]
        song_details_by_songid[string[0]]=details
    return song_details_by_songid
