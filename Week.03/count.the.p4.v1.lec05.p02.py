def safe_input( prompt ):
    try:
        word = input( prompt )
        return( word, True )
    except EOFError:
        return( "", False )

theCount = 0
allWords = 0
nonTarget = []
cFlag = True
while cFlag:
    word,cFlag = safe_input("")
    for w in word.split():
        if cFlag:
            allWords = allWords + 1
        if w in [ 'the', 'The' ]:
            theCount = theCount + 1
        elif w != '':
            if w not in nonTarget:
                nonTarget.append(w)
print( "All words:%3s. Target words:%3s" % (allWords,theCount) )
print( "Non-Target words: ", nonTarget )
