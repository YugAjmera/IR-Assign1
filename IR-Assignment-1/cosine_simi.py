
#Calculate Cosine Score of every song with respect to query and return top -15 songs with their ids
def CosineSimilarity(processed_query,word_by_id,id_by_word,song_tf_idf_by_songid):
    song_weight={}
    print(processed_query)
    for i in range(len(processed_query)):
        processed_query[i]=(id_by_word[processed_query[i]])
    que=set(processed_query)
    for i in song_tf_idf_by_songid:
        songid=i
        tf_idf=song_tf_idf_by_songid[i]
        det=[]
        f=0
        for j in tf_idf:
            if j in processed_query:
                det.append(j)
                try:
                    song_weight[songid]+=tf_idf[j]
                except Exception as e:
                    song_weight[songid]=tf_idf[j]
                    f=1
        det=set(det)
        if f==1:
            song_weight[songid]/=10**(len(que)-len(det))
    sorted_scores = sorted(song_weight.items(), key=lambda kv: kv[1], reverse=True)
    relevant_songs=[]
    for i in sorted_scores:
        relevant_songs.append([i[0],i[1]])
    return relevant_songs[0:15]
