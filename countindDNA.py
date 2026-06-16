def counter_DNA(sequence):
  countA=0
  countC=0
  countG=0
  countT=0
  
  for base in sequence:
    if base=="A":
      countA+=1
    elif base=="G":
      countG+=1
    elif base=="C":
      countC+=1
    else: countT+=1
  
  
  return "The sequence has the following count of bases: A= " + str(countA) + ", C= " +str(countC) +  ", T= " + str(countT) +  ", G= " + str(countG)




print(counter_DNA("AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC"))

    
    
