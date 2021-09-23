Debug = False   # Sometimes, print for debugging
Index = 0
FakeFile = [
        "Try writing your own words.2 file first",
        "the course honours cs and ce",
        "The course moves very quick about python and the unix command line",
        "and things like that"
    ]


def open_file(filename=""):
    return(FakeFile)


def safe_input(f=None, prompt=""):
    global Index
    if Index < len(FakeFile):
        Index += 1
        return(FakeFile[Index-1], True)
    else:
        return("", False)


def main():
    # Important scope implications of using main()
    theCount = 0
    allWords = 0
    nonTarget = []
    inFile = open_file()
    assert not (inFile is None), "Assume valid file object"

    cFlag = True
    while cFlag:
        line, cFlag = safe_input(inFile)
        if not cFlag:
            break
        assert cFlag, "Assume valid input hereafter"
        for w in line.split():
            allWords = allWords + 1
            if w in ['the', 'The']:
                theCount = theCount + 1
            elif w != '':
                if w not in nonTarget:
                    nonTarget.append(w)
    print("All words:%3s. Target words:%3s" % (allWords, theCount))
    print("Non-Target words: ", nonTarget)


if __name__ == "__main__":
    main()

# http://pythontutor.com/visualize.html#code=Debug%20%3D%20False%20%20%20%23%20Sometimes,%20print%20for%20debugging%0AIndex%20%3D%200%0AFakeFile%20%3D%20%5B%0A%20%20%20%20%20%20%20%20%22Try%20writing%20your%20own%20words.2%20file%20first%22,%0A%20%20%20%20%20%20%20%20%22the%20course%20honours%20cs%20and%20ce%22,%0A%20%20%20%20%20%20%20%20%22The%20course%20moves%20very%20quick%20about%20python%20and%20the%20unix%20command%20line%22,%0A%20%20%20%20%20%20%20%20%22and%20things%20like%20that%22%0A%20%20%20%20%5D%0A%0A%0Adef%20open_file%28filename%3D%22%22%29%3A%0A%20%20%20%20return%28FakeFile%29%0A%0A%0Adef%20safe_input%28f%3DNone,%20prompt%3D%22%22%29%3A%0A%20%20%20%20global%20Index%0A%20%20%20%20if%20Index%20%3C%20len%28FakeFile%29%3A%0A%20%20%20%20%20%20%20%20Index%20%2B%3D%201%0A%20%20%20%20%20%20%20%20return%28FakeFile%5BIndex-1%5D,%20True%29%0A%20%20%20%20else%3A%0A%20%20%20%20%20%20%20%20return%28%22%22,%20False%29%0A%0A%0Adef%20main%28%29%3A%0A%20%20%20%20%23%20Important%20scope%20implications%20of%20using%20main%28%29%0A%20%20%20%20theCount%20%3D%200%0A%20%20%20%20allWords%20%3D%200%0A%20%20%20%20nonTarget%20%3D%20%5B%5D%0A%20%20%20%20inFile%20%3D%20open_file%28%29%0A%20%20%20%20assert%20not%20%28inFile%20is%20None%29,%20%22Assume%20valid%20file%20object%22%0A%0A%20%20%20%20cFlag%20%3D%20True%0A%20%20%20%20while%20cFlag%3A%0A%20%20%20%20%20%20%20%20line,%20cFlag%20%3D%20safe_input%28inFile%29%0A%20%20%20%20%20%20%20%20if%20not%20cFlag%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20break%0A%20%20%20%20%20%20%20%20assert%20cFlag,%20%22Assume%20valid%20input%20hereafter%22%0A%20%20%20%20%20%20%20%20for%20w%20in%20line.split%28%29%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20allWords%20%3D%20allWords%20%2B%201%0A%20%20%20%20%20%20%20%20%20%20%20%20if%20w%20in%20%5B'the',%20'The'%5D%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20theCount%20%3D%20theCount%20%2B%201%0A%20%20%20%20%20%20%20%20%20%20%20%20elif%20w%20!%3D%20''%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20if%20w%20not%20in%20nonTarget%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20nonTarget.append%28w%29%0A%20%20%20%20print%28%22All%20words%3A%253s.%20Target%20words%3A%253s%22%20%25%20%28allWords,%20theCount%29%29%0A%20%20%20%20print%28%22Non-Target%20words%3A%20%22,%20nonTarget%29%0A%0A%0Aif%20__name__%20%3D%3D%20%22__main__%22%3A%0A%20%20%20%20main%28%29&cumulative=false&curInstr=0&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false

# http://pythontutor.com/visualize.html#code=Debug%20%3D%20False%20%20%20%23%20Sometimes,%20print%20for%20debugging%0AIndex%20%3D%200%0AFakeFile%20%3D%20%5B%0A%20%20%20%20%20%20%20%20%22Try%20writing%20your%20own%20words.2%20file%20first%22,%0A%20%20%20%20%20%20%20%20%22the%20course%20honours%20cs%20and%20ce%22,%0A%20%20%20%20%20%20%20%20%22The%20course%20moves%20very%20quick%20about%20python%20and%20the%20unix%20command%20line%22,%0A%20%20%20%20%20%20%20%20%22and%20things%20like%20that%22%0A%20%20%20%20%5D%0A%0A%0Adef%20open_file%28filename%3D%22%22%29%3A%0A%20%20%20%20return%28FakeFile%29%0A%0A%0Adef%20safe_input%28f%3DNone,%20prompt%3D%22%22%29%3A%0A%20%20%20%20global%20Index%0A%20%20%20%20if%20Index%20%3C%20len%28FakeFile%29%3A%0A%20%20%20%20%20%20%20%20Index%20%2B%3D%201%0A%20%20%20%20%20%20%20%20return%28FakeFile%5BIndex-1%5D,%20True%29%0A%20%20%20%20else%3A%0A%20%20%20%20%20%20%20%20return%28%22%22,%20False%29%0A%0A%0Adef%20main%28%29%3A%0A%20%20%20%20%23%20Important%20scope%20implications%20of%20using%20main%28%29%0A%20%20%20%20theCount%20%3D%200%0A%20%20%20%20allWords%20%3D%200%0A%20%20%20%20nonTarget%20%3D%20%5B%5D%0A%20%20%20%20inFile%20%3D%20open_file%28%29%0A%20%20%20%20assert%20not%20%28inFile%20is%20None%29,%20%22Assume%20valid%20file%20object%22%0A%0A%20%20%20%20cFlag%20%3D%20True%0A%20%20%20%20while%20cFlag%3A%0A%20%20%20%20%20%20%20%20line,%20cFlag%20%3D%20safe_input%28inFile%29%0A%20%20%20%20%20%20%20%20if%20not%20cFlag%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20break%0A%20%20%20%20%20%20%20%20assert%20cFlag,%20%22Assume%20valid%20input%20hereafter%22%0A%20%20%20%20%20%20%20%20for%20w%20in%20line.split%28%29%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20allWords%20%3D%20allWords%20%2B%201%0A%20%20%20%20%20%20%20%20%20%20%20%20if%20w%20in%20%5B'the',%20'The'%5D%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20theCount%20%3D%20theCount%20%2B%201%0A%20%20%20%20%20%20%20%20%20%20%20%20elif%20w%20!%3D%20''%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20if%20w%20not%20in%20nonTarget%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20nonTarget.append%28w%29%0A%20%20%20%20print%28%22All%20words%3A%253s.%20Target%20words%3A%253s%22%20%25%20%28allWords,%20theCount%29%29%0A%20%20%20%20print%28%22Non-Target%20words%3A%20%22,%20nonTarget%29%0A%0A%0Aif%20__name__%20%3D%3D%20%22__main__%22%3A%0A%20%20%20%20main%28%29&cumulative=false&curInstr=237&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false
