from stemming.porter2 import stem
from edit_distance import autocorrect

#process query by replacing some characters , autocorrecting it and replacing the words by their ids
def process_query(query,id_by_word,words):
    query = query.replace("'re ", " are ")
    query = query.replace("'ve ", " have ")
    query = query.replace("'d ", " would ")
    query = query.replace("'ll ", " will ")
    query = query.replace(" he's ", " he is ")
    query = query.replace(" she's ", " she is ")
    query = query.replace(" it's ", " it is ")
    query = query.replace(" ain't ", " is not ")
    query = query.replace("n't ", " not ")
    query = query.replace("'s ", " ")
    query=query.split(' ')
    print(query)
    for i in range(len(query)):
        query[i]=query[i].lower()
        query[i]=stem(query[i])
        if query[i] not in id_by_word:
            dis=len(query[i])*100
            wrd=""
            for j in words:
                ed=autocorrect(query[i],j,len(query[i]),len(j))
                if ed<dis:
                    dis=ed
                    wrd=j
            query[i]=wrd
    return query
