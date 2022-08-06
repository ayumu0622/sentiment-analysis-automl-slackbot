def get_max(dict):
    maxx = 0
    indexx = 0
    sentence = "a"
    who = "human"
    #dict = {"ayu":[["a","b","c","d","e"],[1,2,3,4,5]],"emma":[["f","g","h","i","j"],[6,7,8,9,10]]}
    for name, list in dict.items():
        a = max(list[1])
        if maxx < a:
            maxx = a
            indexx = list[1].index(a)
            sentence = list[0][indexx]
            who = name
            
    return f"{who} said that {sentence} and score was {maxx}"
