
def complementing(sequence):

    complementing_non=""

    for base in sequence:

        if base == "A":

            complementing_non+="T"

        elif base == "G":

            complementing_non+="C"

        elif base =="C":

            complementing_non+="G"

        else:

            complementing_non+="A"


    counter = len(complementing_non)-1
    complementin=""

    while counter>=0:
        complementin += complementing_non[counter:counter+1]
        counter-=1
    
    return complementin
