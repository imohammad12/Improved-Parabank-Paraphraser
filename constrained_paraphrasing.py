import os

def paraphrase(sent, neg_const, pos_const):
    ''' sent = str
        neg_const = List[str] 
        pos_const = List[str] 
    '''
    
    
    inp = sent + "\t" + "|".join(neg_const) + '\t' + "|".join(pos_const)
    
    f = open("inp_par.txt", "w")
    f.write(inp)
    f.close()
    
    f = open("out_par.txt", "w")
    f.close()
    
    bashCommand = "./paraphrase.sh < ./inp_par.txt > ./out_par.txt "

    os.system(bashCommand)
    
    f = open("out_par.txt", "r")
    return f.read()