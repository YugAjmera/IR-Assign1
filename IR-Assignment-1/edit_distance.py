#autocorrect words based on the smallest edit-distance
def autocorrect(str1,str2,n,m) :
    # Create a table to store results of subproblems
    lev = []
    for i in range(n):
        lev.append([0] * m)  # initialize 2D array to zero


    for i in range(n) :
        for j in range(m) :
            if i==0 :
                lev[i][j] = j
            elif j==0 :
                lev[i][j] = i
            elif str1[i-1] == str2[j-1] :
                lev[i][j] = lev[i-1][j-1]
            else :
                lev[i][j] = 1 + min(lev[i][j-1],lev[i-1][j],lev[i-1][j-1])
    return lev[n-1][m-1]
