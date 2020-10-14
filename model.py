import math

#This functions reads the dataset of words and lyrics and indexes all the words by ids and collects songs from dataset and return them
def dataset1(filename):
    dataset = open(filename)
    lines = [line.rstrip('\n') for line in open(filename)]
    dataset.close()

    words= lines[17][1:].split(',') #distinct words in the dataset
    songs = lines[18:] #describe each song

    word_by_id = {}
    id = 1
    for i in words:
        word_by_id[id] = i
        id += 1

    return words, word_by_id, songs


#Read dataset and gather Song details and index by Song id
def get_song_details(filename):
    dataset = open(filename)
    lines = [line.rstrip('\n') for line in open(filename)]
    dataset.close()

    song_details_by_songid = {}
    for i in lines:
        string = i.split('<SEP>')
        details = {}
        details['Artist_name'] = string[2]
        details['Title'] = string[3]
        song_details_by_songid[string[0]] = details

    return song_details_by_songid
