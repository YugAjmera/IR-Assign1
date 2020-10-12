from model import dataset1,tf_idf_calculation,get_song_details
import Tkinter as t
from query_process import process_query
from cosine_simi import CosineSimilarity


filename1="mxm_dataset_train.txt"
words,word_by_id,id_by_word,songs=dataset1(filename1) #Get words and index them in dictionary and make them accessible by both id and words
song_tf_idf_by_songid=tf_idf_calculation(songs) # Calculate tf-idf score of each word in each song document

filename2="new_dataset.txt"
song_details_by_songid=get_song_details(filename2) #Save the song details corresponding to SongID

#Fetch the query from tkinter Text field and get the processed query
def fetch_query():
    query=gbn.get()
    query=query.strip()
    T.delete(1.0,t.END)
    processed_query=process_query(query,id_by_word,words) #process query by autocorrecting , stemming and replacing words by ids
    print("Final : ",processed_query) #print processed query
    relevant_songs=CosineSimilarity(processed_query,word_by_id,id_by_word,song_tf_idf_by_songid) # Using CosineSimilarity get top 15 relevant songs
    write_in_text(relevant_songs)

# Write the top 15 songs in the Text Area
def write_in_text(relevant_songs):
    to_print="\t\tTop 15 Relevant Songs\n\n"
    j=1
    for i in relevant_songs:
        to_print+=str(j)+". TITLE : "
        to_print+=str(song_details_by_songid[i[0]]['Title'])+"\n"+"Artist : "+str(song_details_by_songid[i[0]]['Artist_name'])
        to_print+="\n\n"
        j+=1
    T.insert(t.END,to_print)

#Tkinter Window Setup
window = t.Tk()
window.title("Lyrics Search for Music Retrieval")
window.geometry('900x900')
window.configure(background = "white")
gbn=t.Entry(window,width=40)
gbn.pack()
bt1=t.Button(window,text="Search Songs",command=fetch_query)
bt1.pack()
S = t.Scrollbar(window)
T = t.Text(window, height=4, width=200)
S.pack(side='right', fill='y')
T.pack(side='left', fill='y')
S.config(command=T.yview)
T.config(yscrollcommand=S.set)
T.insert(t.END,"")
window.mainloop()
