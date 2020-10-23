from script import dataset,get_song_details, tf_idf_calc, cosine_simi
import tkinter as t
from nltk.corpus import stopwords
from nltk import PorterStemmer
import string
import re

filename1 = "yug_test.txt" 
#change this to original dataset: mxm_dataset_train.txt

words_by_id, songs, id_by_word = dataset(filename1) 

tf_idf_by_song_id = tf_idf_calc(songs) 


filename2 = "yug_dataset.txt" 
#change this to original dataset: song_dataset.txt

song_details_by_songid = get_song_details(filename2)


#Fetch the query from tkinter Text field and get the processed query
def fetch_query():
    query = gbn.get()
    query = query.strip()
    T.delete(1.0, t.END)

    #Prcoess Query here
    ps = PorterStemmer()
    sw_set = set(stopwords.words('english'))
    query = query.strip(string.punctuation)
    token = re.sub('[^a-zA-Z]', ' ',query).split()
    token2 = [ps.stem(token) for word in token if word not in sw_set]
    query = token2

    relevant_songs = cosine_simi(query, words_by_id, id_by_word, tf_idf_by_song_id) # Use Cosine similatiry get top 10 songs
    write_in_text(relevant_songs)


# Write the top 10 songs in the Text Area
def write_in_text(relevant_songs):

    to_print = "\t\tTop 10 Relevant Songs\n\n"
    j = 1

    for i in relevant_songs:
        to_print += str(j)+". TITLE : "
        to_print += str(song_details_by_songid[i[0]]['Title']) + "\n"+"Artist : " + str(song_details_by_songid[i[0]]['Artist'])
        to_print += "\n\n"
        j += 1

    T.insert(t.END,to_print)

#Tkinter Window Setup
window = t.Tk()
window.title("Lyrics Search for Music Retrieval")
window.geometry('400x400')
window.configure(background = "white")
gbn = t.Entry(window,width=40)
gbn.pack()
bt1 = t.Button(window,text="Search Songs",command=fetch_query)
bt1.pack()
S = t.Scrollbar(window)
T = t.Text(window, height = 4, width = 200)
S.pack(side = 'right', fill = 'y')
T.pack(side = 'left', fill = 'y')
S.config(command = T.yview)
T.config(yscrollcommand = S.set)
T.insert(t.END,"")
window.mainloop()
