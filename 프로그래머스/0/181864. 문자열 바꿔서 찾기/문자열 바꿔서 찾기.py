def solution(myString, pat):

    myString = myString.replace("B","C").replace("A","B").replace("C","A")
    return 1 if pat in myString else 0
        