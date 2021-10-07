Debug = False
InputObjectsList = []
InputObjectsHash = []
allWords = 0
theCount = 0
nonTarget = [] 
TargetWords = ['outside', 'today', 'weather', 'raining', 'nice' ]


Index = 0
FakeFile = [
        "#weather        nice weather eh",
        "#weather        snow is coming",
        "#weather        wind is high",
        "#negative       good food",
        "#negative       i need a coffee"
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


def print_training_data_obj(inObjList, inObjHash):
    i = 0
    while i < len(inObjList):
        print("( %s) %s" % (inObjHash[i]["label"], inObjList[i]))
        if Debug:
            print("-->", inObjHash[i]["words"])
        i += 1


def process_input_line(line):
    global allWords, theCount, nonTarget

    trainInstance = {}
    trainInstance["label"] = "None"
    trainInstance["words"] = []
    for w in line.split():
        allWords = allWords + 1
        if w[0] == "#":
            trainInstance["label"] = w
        else:
            trainInstance["words"].append(w)

        if w in TargetWords:
            theCount = theCount + 1
        elif w != '':
            if w not in nonTarget:
                nonTarget.append(w)
    return(trainInstance)


def process_input_stream(inFile, inObjList, inObjHash):
    assert not (inFile is None), "Assume valid file object"

    cFlag = True
    while cFlag:
        line, cFlag = safe_input(inFile)
        if not cFlag:
            break
        assert cFlag, "Assume valid input hereafter"
        inObjList.append(line)
        inObjHash.append(process_input_line(line))


def main():
    inFile = open_file()
    assert not (inFile is None), "Assume valid file object"

    process_input_stream(inFile, InputObjectsList, InputObjectsHash)
    # inFile.close()

    print("TargetWords Hardcoded (%d): " % len(TargetWords), TargetWords)
    print_training_data_obj(InputObjectsList, InputObjectsHash)

    print("All words:%3s. Target words:%3s" % (allWords, theCount))
    print("Non-Target words: ", nonTarget)


if __name__ == "__main__":
    main()


# http://pythontutor.com/visualize.html#code=Debug%20%3D%20False%0AInputObjectsList%20%3D%20%5B%5D%0AInputObjectsHash%20%3D%20%5B%5D%0AallWords%20%3D%200%0AtheCount%20%3D%200%0AnonTarget%20%3D%20%5B%5D%0ATargetWords%20%3D%20%5B'outside',%20'today',%20'weather',%20'raining',%20'nice'%20%5D%0A%0A%0AIndex%20%3D%200%0AFakeFile%20%3D%20%5B%0A%20%20%20%20%20%20%20%20%22%23weather%20%20%20%20%20%20%20%20nice%20weather%20eh%22,%0A%20%20%20%20%20%20%20%20%22%23weather%20%20%20%20%20%20%20%20snow%20is%20coming%22,%0A%20%20%20%20%20%20%20%20%22%23weather%20%20%20%20%20%20%20%20wind%20is%20high%22,%0A%20%20%20%20%20%20%20%20%22%23negative%20%20%20%20%20%20%20good%20food%22,%0A%20%20%20%20%20%20%20%20%22%23negative%20%20%20%20%20%20%20i%20need%20a%20coffee%22%0A%20%20%20%20%5D%0A%0A%0Adef%20open_file%28filename%3D%22%22%29%3A%0A%20%20%20%20return%28FakeFile%29%0A%0A%0Adef%20safe_input%28f%3DNone,%20prompt%3D%22%22%29%3A%0A%20%20%20%20global%20Index%0A%20%20%20%20if%20Index%20%3C%20len%28FakeFile%29%3A%0A%20%20%20%20%20%20%20%20Index%20%2B%3D%201%0A%20%20%20%20%20%20%20%20return%28FakeFile%5BIndex-1%5D,%20True%29%0A%20%20%20%20else%3A%0A%20%20%20%20%20%20%20%20return%28%22%22,%20False%29%0A%0A%0Adef%20print_training_data_obj%28inObjList,%20inObjHash%29%3A%0A%20%20%20%20i%20%3D%200%0A%20%20%20%20while%20i%20%3C%20len%28inObjList%29%3A%0A%20%20%20%20%20%20%20%20print%28%22%28%20%25s%29%20%25s%22%20%25%20%28inObjHash%5Bi%5D%5B%22label%22%5D,%20inObjList%5Bi%5D%29%29%0A%20%20%20%20%20%20%20%20if%20Debug%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20print%28%22--%3E%22,%20inObjHash%5Bi%5D%5B%22words%22%5D%29%0A%20%20%20%20%20%20%20%20i%20%2B%3D%201%0A%0A%0Adef%20process_input_line%28line%29%3A%0A%20%20%20%20global%20allWords,%20theCount,%20nonTarget%0A%0A%20%20%20%20trainInstance%20%3D%20%7B%7D%0A%20%20%20%20trainInstance%5B%22label%22%5D%20%3D%20%22None%22%0A%20%20%20%20trainInstance%5B%22words%22%5D%20%3D%20%5B%5D%0A%20%20%20%20for%20w%20in%20line.split%28%29%3A%0A%20%20%20%20%20%20%20%20allWords%20%3D%20allWords%20%2B%201%0A%20%20%20%20%20%20%20%20if%20w%5B0%5D%20%3D%3D%20%22%23%22%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20trainInstance%5B%22label%22%5D%20%3D%20w%0A%20%20%20%20%20%20%20%20else%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20trainInstance%5B%22words%22%5D.append%28w%29%0A%0A%20%20%20%20%20%20%20%20if%20w%20in%20TargetWords%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20theCount%20%3D%20theCount%20%2B%201%0A%20%20%20%20%20%20%20%20elif%20w%20!%3D%20''%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20if%20w%20not%20in%20nonTarget%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20nonTarget.append%28w%29%0A%20%20%20%20return%28trainInstance%29%0A%0A%0Adef%20process_input_stream%28inFile,%20inObjList,%20inObjHash%29%3A%0A%20%20%20%20assert%20not%20%28inFile%20is%20None%29,%20%22Assume%20valid%20file%20object%22%0A%0A%20%20%20%20cFlag%20%3D%20True%0A%20%20%20%20while%20cFlag%3A%0A%20%20%20%20%20%20%20%20line,%20cFlag%20%3D%20safe_input%28inFile%29%0A%20%20%20%20%20%20%20%20if%20not%20cFlag%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20break%0A%20%20%20%20%20%20%20%20assert%20cFlag,%20%22Assume%20valid%20input%20hereafter%22%0A%20%20%20%20%20%20%20%20inObjList.append%28line%29%0A%20%20%20%20%20%20%20%20inObjHash.append%28process_input_line%28line%29%29%0A%0A%0Adef%20main%28%29%3A%0A%20%20%20%20inFile%20%3D%20open_file%28%29%0A%20%20%20%20assert%20not%20%28inFile%20is%20None%29,%20%22Assume%20valid%20file%20object%22%0A%0A%20%20%20%20process_input_stream%28inFile,%20InputObjectsList,%20InputObjectsHash%29%0A%20%20%20%20%23%20inFile.close%28%29%0A%0A%20%20%20%20print%28%22TargetWords%20Hardcoded%20%28%25d%29%3A%20%22%20%25%20len%28TargetWords%29,%20TargetWords%29%0A%20%20%20%20print_training_data_obj%28InputObjectsList,%20InputObjectsHash%29%0A%0A%20%20%20%20print%28%22All%20words%3A%253s.%20Target%20words%3A%253s%22%20%25%20%28allWords,%20theCount%29%29%0A%20%20%20%20print%28%22Non-Target%20words%3A%20%22,%20nonTarget%29%0A%0A%0Aif%20__name__%20%3D%3D%20%22__main__%22%3A%0A%20%20%20%20main%28%29%0A&cumulative=true&heapPrimitives=true&mode=edit&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false
