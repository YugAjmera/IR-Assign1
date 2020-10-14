
import Tkinter as t

#Fetch the query from tkinter Text field and get the processed query
def fetch_query():
   

# Write the top 10 songs in the Text Area
def write_in_text(relevant_songs):
    to_print="\t\tTop 10 Relevant Songs\n\n"
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
window.geometry('400x400')
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