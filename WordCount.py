def txtSplit( filename ) :
    f = open(filename, 'rt')
    word_list = f.read().replace(".","").replace(",","").replace("!","").replace("\"","").replace("\'","").replace("?","").upper().split()
    return word_list

def wordCnt( w_list ) :
    wordCount={}
    for w in w_list :
        if w not in wordCount :
            wordCount[w] = 1
        else :
            wordCount[w] += 1
    return wordCount

if __name__ == "__main__" :
    unsort_dic = wordCnt( txtSplit('/home/namsic2/Les_Miserables-Victor_Hugo.txt') )

    print( unsort_dic )
