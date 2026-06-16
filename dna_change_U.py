def transcriber(sequence):
    print(len(sequence))
    transcribed=""
    for base in sequence:
        if base!="T":
            transcribed+=base
        else:
            transcribed+="U"
    print(len(transcribed))
    return transcribed
