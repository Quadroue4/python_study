import operator

def sort_dic(dic) :
    sortList = list( sorted(dic.items(), key=operator.itemgetter(1), reverse = True) )
    return sortList

def solution() :
    word_dic = {}
    with open('Les_Miserables-Victor_Hugo.txt', 'r') as f :
        words = f.read().upper().replace(".","").replace("?","").replace("!","").replace("-","").replace("/","").replace(",","").replace(":","").replace(";","").replace("\"","").replace("(","").replace(")","").replace("0","").replace("1","").replace("2","").replace("3","").replace("4","").replace("5","").replace("6","").replace("7","").replace("8","").replace("9","").replace(" '"," ").replace("' "," ").replace("\t'"," ").replace("'\n"," ").split()

    for word in words :
        word_dic[word] = word_dic.get(word,0) + 1

    ret_list = sort_dic( word_dic )

    return ret_list

if __name__ == '__main__' :
    solution_list = solution()
    for each in solution_list :
        print(each)
