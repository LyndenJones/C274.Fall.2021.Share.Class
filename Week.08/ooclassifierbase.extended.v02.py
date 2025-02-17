"""
Object-Oriented Classifier (ooclassifier).  Base for Assignment #1, CMPUT 274.

Bag of words sentiment analysis.  Extended comments and functionality.

Copyright 2020-2021 Paul Lu
"""

# Copyright 2020-2021 Paul Lu
import sys
import copy     # for deepcopy()

Debug = False   # Sometimes, print for debugging.  Overridable on command line.
InputFilename = "file.input.txt"
TargetWords = [
        'outside', 'today', 'weather', 'raining', 'nice', 'rain', 'snow',
        'day', 'winter', 'cold', 'warm', 'snowing', 'out', 'hope', 'boots',
        'sunny', 'windy', 'coming', 'perfect', 'need', 'sun', 'on', 'was',
        '-40', 'jackets', 'wish', 'fog', 'pretty', 'summer'
        ]


def open_file(filename=InputFilename):
    """
    Return an open file object or stdin for reading.
    Wrapper function for open() to handle common exceptions.
    Failed file open results in stdin used instead.

    Parameters
    ----------
    filename : string, default=InputFilename a global string literal
        Name/path to file.

    Returns
    -------
    file object
        Either a real file or stdin
    """
    try:
        f = open(filename, "r")
        return(f)
    except FileNotFoundError:
        # FileNotFoundError is subclass of OSError
        if Debug:
            print("File Not Found")
        return(sys.stdin)
    except OSError:
        if Debug:
            print("Other OS Error")
        return(sys.stdin)


def safe_input(f=None, prompt=""):
    """
    Return string with line of input, from file object or stdin, handling EOF

    Parameters
    ----------
    f : file object, default=None which causes stdin to be used
        File object or None for stdin
    prompt : string, default=""
        Optional prompt for input

    Returns
    -------
    tuple(string, boolean flag): string with line of input, flag=False means EOF
        flag=False means EOF reached, otherwise True and string is line of input
    """
    try:
        # Case:  Stdin
        if f is sys.stdin or f is None:
            line = input(prompt)
        # Case:  From file
        else:
            assert not (f is None)
            assert (f is not None)
            line = f.readline()
            if Debug:
                print("readline: ", line, end='')
            if line == "":  # Check EOF before strip()
                if Debug:
                    print("EOF")
                return("", False)
        return(line.strip(), True)
    except EOFError:
        return("", False)


class C274:
    """
    Superclass for all classifier-related classes.

    Attributes
    ----------
    type : string
        Modifiable version of __class__

    Methods
    -------
    __init__
        Constructor, sets attribute "type"
    __str__
        Returns human-readable identification string
    __repr__
        Returns comparable identification string
    """

    def __init__(self):
        """
        Sets attribute "type"

        Returns
        -------
        None
        """
        self.type = str(self.__class__)
        return

    def __str__(self):
        """
        Returns human-readable identification string

        Returns
        -------
        string
            Returns human-readable identification string, currently "type"

        To do
        -----
        Better content than just attribute "type"
        """
        return(self.type)

    def __repr__(self):
        """
        Returns comparable identification string

        Returns
        -------
        string
            Returns comparable identification string, with "id" adn "type"
        """
        s = "<%d> %s" % (id(self), self.type)
        return(s)


class ClassifyByTarget(C274):
    """
    Prose summary.

    Attributes
    ----------

    Methods
    -------

    See Also
    --------
    Prose

    Examples
    --------
    doctest
    """
    def __init__(self, lw=[]):
        """
        Prose summary.

        Parameters
        ----------
        param1 : type
            Prose
        param2 : type
            Prose

        Returns
        -------
        type
            Prose

        See Also
        --------
        Prose

        Examples
        --------
        doctest
        """
        super().__init__() # Call superclass
        # self.type = str(self.__class__)
        self.allWords = 0
        self.theCount = 0
        self.nonTarget = []
        self.set_target_words(lw)
        self.initTF()
        return

    def initTF(self):
        """
        Prose summary.

        Parameters
        ----------
        param1 : type
            Prose
        param2 : type
            Prose

        Returns
        -------
        type
            Prose

        See Also
        --------
        Prose

        Examples
        --------
        doctest
        """
        self.TP = 0
        self.FP = 0
        self.TN = 0
        self.FN = 0
        return

    # FIXME:  Incomplete.  Finish get_TF() and other getters/setters.
    def get_TF(self):
        """
        Prose summary.

        Parameters
        ----------
        param1 : type
            Prose
        param2 : type
            Prose

        Returns
        -------
        type
            Prose

        See Also
        --------
        Prose

        Examples
        --------
        doctest
        """
        return(self.TP, self.FP, self.TN, self.FN)

    # TODO: Could use Use Python properties
    #     https://www.python-course.eu/python3_properties.php
    def set_target_words(self, lw):
        """
        Prose summary.

        Parameters
        ----------
        param1 : type
            Prose
        param2 : type
            Prose

        Returns
        -------
        type
            Prose

        See Also
        --------
        Prose

        Examples
        --------
        doctest
        """
        # Could also do self.targetWords = lw.copy().  Thanks, TA Jason Cannon
        self.targetWords = copy.deepcopy(lw)
        return

    def get_target_words(self):
        """
        Prose summary.

        Parameters
        ----------
        param1 : type
            Prose
        param2 : type
            Prose

        Returns
        -------
        type
            Prose

        See Also
        --------
        Prose

        Examples
        --------
        doctest
        """
        return(self.targetWords)

    def get_allWords(self):
        """
        Prose summary.

        Parameters
        ----------
        param1 : type
            Prose
        param2 : type
            Prose

        Returns
        -------
        type
            Prose

        See Also
        --------
        Prose

        Examples
        --------
        doctest
        """
        return(self.allWords)

    def incr_allWords(self):
        """
        Prose summary.

        Parameters
        ----------
        param1 : type
            Prose
        param2 : type
            Prose

        Returns
        -------
        type
            Prose

        See Also
        --------
        Prose

        Examples
        --------
        doctest
        """
        self.allWords += 1
        return

    def get_theCount(self):
        """
        Prose summary.

        Parameters
        ----------
        param1 : type
            Prose
        param2 : type
            Prose

        Returns
        -------
        type
            Prose

        See Also
        --------
        Prose

        Examples
        --------
        doctest
        """
        return(self.theCount)

    def incr_theCount(self):
        """
        Prose summary.

        Parameters
        ----------
        param1 : type
            Prose
        param2 : type
            Prose

        Returns
        -------
        type
            Prose

        See Also
        --------
        Prose

        Examples
        --------
        doctest
        """
        self.theCount += 1
        return

    def get_nonTarget(self):
        """
        Prose summary.

        Parameters
        ----------
        param1 : type
            Prose
        param2 : type
            Prose

        Returns
        -------
        type
            Prose

        See Also
        --------
        Prose

        Examples
        --------
        doctest
        """
        return(self.nonTarget)

    def add_nonTarget(self, w):
        """
        Prose summary.

        Parameters
        ----------
        param1 : type
            Prose
        param2 : type
            Prose

        Returns
        -------
        type
            Prose

        See Also
        --------
        Prose

        Examples
        --------
        doctest
        """
        self.nonTarget.append(w)
        return

    def print_config(self,printSorted=True):
        """
        Prose summary.

        Parameters
        ----------
        param1 : type
            Prose
        param2 : type
            Prose

        Returns
        -------
        type
            Prose

        See Also
        --------
        Prose

        Examples
        --------
        doctest
        """
        print("-------- Print Config --------")
        ln = len(self.get_target_words())
        print("TargetWords (%d): " % ln, end='')
        if printSorted:
            print(sorted(self.get_target_words()))
        else:
            print(self.get_target_words())
        return

    def print_run_info(self,printSorted=True):
        """
        Prose summary.

        Parameters
        ----------
        param1 : type
            Prose
        param2 : type
            Prose

        Returns
        -------
        type
            Prose

        See Also
        --------
        Prose

        Examples
        --------
        doctest
        """
        print("-------- Print Run Info --------")
        print("All words:%3s. " % self.get_allWords(), end='')
        print(" Target words:%3s" % self.get_theCount())
        print("Non-Target words (%d): " % len(self.get_nonTarget()), end='')
        if printSorted:
            print(sorted(self.get_nonTarget()))
        else:
            print(self.get_nonTarget())
        return

    def print_confusion_matrix(self, targetLabel, doKey=False, tag=""):
        """
        Prose summary.

        Parameters
        ----------
        param1 : type
            Prose
        param2 : type
            Prose

        Returns
        -------
        type
            Prose

        See Also
        --------
        Prose

        Examples
        --------
        doctest
        """
        assert (self.TP + self.TP + self.FP + self.TN) > 0
        print(tag+"-------- Confusion Matrix --------")
        print(tag+"%10s | %13s" % ('Predict', 'Label'))
        print(tag+"-----------+----------------------")
        print(tag+"%10s | %10s %10s" % (' ', targetLabel, 'not'))
        if doKey:
            print(tag+"%10s | %10s %10s" % ('', 'TP   ', 'FP   '))
        print(tag+"%10s | %10d %10d" % (targetLabel, self.TP, self.FP))
        if doKey:
            print(tag+"%10s | %10s %10s" % ('', 'FN   ', 'TN   '))
        print(tag+"%10s | %10d %10d" % ('not', self.FN, self.TN))
        return

    def eval_training_set(self, tset, targetLabel, lines=True):
        """
        Prose summary.

        Parameters
        ----------
        param1 : type
            Prose
        param2 : type
            Prose

        Returns
        -------
        type
            Prose

        See Also
        --------
        Prose

        Examples
        --------
        doctest
        """
        print("-------- Evaluate Training Set --------")
        self.initTF()
        # zip is good for parallel arrays and iteration
        z = zip(tset.get_instances(), tset.get_lines())
        for ti, w in z:
            lb = ti.get_label()
            cl = ti.get_class()
            if lb == targetLabel:
                if cl:
                    self.TP += 1
                    outcome = "TP"
                else:
                    self.FN += 1
                    outcome = "FN"
            else:
                if cl:
                    self.FP += 1
                    outcome = "FP"
                else:
                    self.TN += 1
                    outcome = "TN"
            explain = ti.get_explain()
            # Format nice output
            if lines:
                w = ' '.join(w.split())
            else:
                w = ' '.join(ti.get_words())
                w = lb + " " + w

            # TW = testing bag of words words (kinda arbitrary)
            print("TW %s: ( %10s) %s" % (outcome, explain, w))
            if Debug:
                print("-->", ti.get_words())
        self.print_confusion_matrix(targetLabel)
        return

    def classify_by_words(self, ti, update=False, tlabel="last"):
        """
        Prose summary.

        Parameters
        ----------
        param1 : type
            Prose
        param2 : type
            Prose

        Returns
        -------
        type
            Prose

        See Also
        --------
        Prose

        Examples
        --------
        doctest
        """
        inClass = False
        evidence = ''
        lw = ti.get_words()
        for w in lw:
            if update:
                self.incr_allWords()
            if w in self.get_target_words():    # FIXME Write predicate
                inClass = True
                if update:
                    self.incr_theCount()
                if evidence == '':
                    evidence = w            # FIXME Use first word, but change
            elif w != '':
                if update and (w not in self.get_nonTarget()):
                    self.add_nonTarget(w)
        if evidence == '':
            evidence = '#negative'
        if update:
            ti.set_class(inClass, tlabel, evidence)
        return(inClass, evidence)

    # Could use a decorator, but not now
    def classify(self, ti, update=False, tlabel="last"):
        """
        Prose summary.

        Parameters
        ----------
        param1 : type
            Prose
        param2 : type
            Prose

        Returns
        -------
        type
            Prose

        See Also
        --------
        Prose

        Examples
        --------
        doctest
        """
        cl, e = self.classify_by_words(ti, update, tlabel)
        return(cl, e)

    def classify_all(self, ts, update=True, tlabel="classify_all"):
        """
        Prose summary.

        Parameters
        ----------
        param1 : type
            Prose
        param2 : type
            Prose

        Returns
        -------
        type
            Prose

        See Also
        --------
        Prose

        Examples
        --------
        doctest
        """
        for ti in ts.get_instances():
            cl, e = self.classify(ti, update=update, tlabel=tlabel)
        return


class TrainingInstance(C274):
    """
    Prose summary.

    Attributes
    ----------

    Methods
    -------

    See Also
    --------
    Prose

    Examples
    --------
    doctest
    """
    def __init__(self):
        """
        Prose summary.

        Parameters
        ----------
        param1 : type
            Prose
        param2 : type
            Prose

        Returns
        -------
        type
            Prose

        See Also
        --------
        Prose

        Examples
        --------
        doctest
        """
        super().__init__() # Call superclass
        # self.type = str(self.__class__)
        self.inst = dict()
        # FIXME:  Get rid of dict, and use attributes
        self.inst["label"] = "N/A"      # Class, given by oracle
        self.inst["words"] = []         # Bag of words
        self.inst["class"] = ""         # Class, by classifier
        self.inst["explain"] = ""       # Explanation for classification
        self.inst["experiments"] = dict()   # Previous classifier runs
        return

    def get_label(self):
        """
        Prose summary.

        Parameters
        ----------
        param1 : type
            Prose
        param2 : type
            Prose

        Returns
        -------
        type
            Prose

        See Also
        --------
        Prose

        Examples
        --------
        doctest
        """
        return(self.inst["label"])

    def get_words(self):
        """
        Prose summary.

        Parameters
        ----------
        param1 : type
            Prose
        param2 : type
            Prose

        Returns
        -------
        type
            Prose

        See Also
        --------
        Prose

        Examples
        --------
        doctest
        """
        return(self.inst["words"])

    def set_class(self, theClass, tlabel="last", explain=""):
        """
        Prose summary.

        Parameters
        ----------
        param1 : type
            Prose
        param2 : type
            Prose

        Returns
        -------
        type
            Prose

        See Also
        --------
        Prose

        Examples
        --------
        doctest
        """
        # tlabel = tag label
        self.inst["class"] = theClass
        self.inst["experiments"][tlabel] = theClass
        self.inst["explain"] = explain
        return

    def get_class_by_tag(self, tlabel):             # tlabel = tag label
        """
        Prose summary.

        Parameters
        ----------
        param1 : type
            Prose
        param2 : type
            Prose

        Returns
        -------
        type
            Prose

        See Also
        --------
        Prose

        Examples
        --------
        doctest
        """
        cl = self.inst["experiments"].get(tlabel)
        if cl is None:
            return("N/A")
        else:
            return(cl)

    def get_explain(self):
        """
        Prose summary.

        Parameters
        ----------
        param1 : type
            Prose
        param2 : type
            Prose

        Returns
        -------
        type
            Prose

        See Also
        --------
        Prose

        Examples
        --------
        doctest
        """
        cl = self.inst.get("explain")
        if cl is None:
            return("N/A")
        else:
            return(cl)

    def get_class(self):
        """
        Prose summary.

        Parameters
        ----------
        param1 : type
            Prose
        param2 : type
            Prose

        Returns
        -------
        type
            Prose

        See Also
        --------
        Prose

        Examples
        --------
        doctest
        """
        return self.inst["class"]

    def process_input_line(
                self, line, run=None,
                tlabel="read", inclLabel=False
            ):
        """
        Prose summary.

        Parameters
        ----------
        param1 : type
            Prose
        param2 : type
            Prose

        Returns
        -------
        type
            Prose

        See Also
        --------
        Prose

        Examples
        --------
        doctest
        """
        for w in line.split():
            if w[0] == "#":
                self.inst["label"] = w
                if inclLabel:
                    self.inst["words"].append(w)
            else:
                self.inst["words"].append(w)

        if not (run is None):
            cl, e = run.classify(self, update=True, tlabel=tlabel)
        return(self)


class TrainingSet(C274):
    """
    Prose summary.

    Attributes
    ----------

    Methods
    -------

    See Also
    --------
    Prose

    Examples
    --------
    doctest
    """
    def __init__(self):
        """
        Prose summary.

        Parameters
        ----------
        param1 : type
            Prose
        param2 : type
            Prose

        Returns
        -------
        type
            Prose

        See Also
        --------
        Prose

        Examples
        --------
        doctest
        """
        super().__init__() # Call superclass
        # self.type = str(self.__class__)
        self.inObjList = []     # Unparsed lines, from training set
        self.inObjHash = []     # Parsed lines, in dictionary/hash
        self.variable = dict()  # NEW: Configuration/environment variables
        return

    def set_env_variable(self, k, v):
        """
        Prose summary.

        Parameters
        ----------
        param1 : type
            Prose
        param2 : type
            Prose

        Returns
        -------
        type
            Prose

        See Also
        --------
        Prose

        Examples
        --------
        doctest
        """
        self.variable[k] = v
        return

    def get_env_variable(self, k):
        """
        Prose summary.

        Parameters
        ----------
        param1 : type
            Prose
        param2 : type
            Prose

        Returns
        -------
        type
            Prose

        See Also
        --------
        Prose

        Examples
        --------
        doctest
        """
        if k in self.variable:
            return(self.variable[k])
        else:
            return ""

    def inspect_comment(self, line):
        """
        Prose summary.

        Parameters
        ----------
        param1 : type
            Prose
        param2 : type
            Prose

        Returns
        -------
        type
            Prose

        See Also
        --------
        Prose

        Examples
        --------
        doctest
        """
        if len(line) > 1 and line[1] != ' ':      # Might be variable
            v = line.split(maxsplit=1)
            self.set_env_variable(v[0][1:], v[1])
        return

    def get_instances(self):
        """
        Prose summary.

        Parameters
        ----------
        param1 : type
            Prose
        param2 : type
            Prose

        Returns
        -------
        type
            Prose

        See Also
        --------
        Prose

        Examples
        --------
        doctest
        """
        return(self.inObjHash)      # FIXME Should protect this more

    def get_lines(self):
        """
        Prose summary.

        Parameters
        ----------
        param1 : type
            Prose
        param2 : type
            Prose

        Returns
        -------
        type
            Prose

        See Also
        --------
        Prose

        Examples
        --------
        doctest
        """
        return(self.inObjList)      # FIXME Should protect this more

    def print_training_set(self):
        """
        Prose summary.

        Parameters
        ----------
        param1 : type
            Prose
        param2 : type
            Prose

        Returns
        -------
        type
            Prose

        See Also
        --------
        Prose

        Examples
        --------
        doctest
        """
        print("-------- Print Training Set --------")
        z = zip(self.inObjHash, self.inObjList)
        for ti, w in z:
            lb = ti.get_label()
            cl = ti.get_class_by_tag("last")     # Not used
            explain = ti.get_explain()
            print("( %s) (%s) %s" % (lb, explain, w))
            if Debug:
                print("-->", ti.get_words())
        return

    def process_input_stream(self, inFile, run=None):
        """
        Prose summary.

        Parameters
        ----------
        param1 : type
            Prose
        param2 : type
            Prose

        Returns
        -------
        type
            Prose

        See Also
        --------
        Prose

        Examples
        --------
        doctest
        """
        assert not (inFile is None), "Assume valid file object"
        cFlag = True
        while cFlag:
            line, cFlag = safe_input(inFile)
            if not cFlag:
                break
            assert cFlag, "Assume valid input hereafter"

            if len(line) == 0:   # Blank line.  Skip it.
                continue

            # Check for comments *and* environment variables
            if line[0] == '%':  # Comments must start with % and variables
                self.inspect_comment(line)
                continue

            # Save the training data input, by line
            self.inObjList.append(line)
            # Save the training data input, after parsing
            ti = TrainingInstance()
            ti.process_input_line(line, run=run)
            self.inObjHash.append(ti)
        return


# Very basic test of functionality
def basemain():
    """
    Prose summary.

    Parameters
    ----------
    param1 : type
        Prose
    param2 : type
        Prose

    Returns
    -------
    type
        Prose

    See Also
    --------
    Prose

    Examples
    --------
    doctest
    """
    global Debug
    tset = TrainingSet()
    run1 = ClassifyByTarget(TargetWords)
    if Debug:
        print(run1)     # Just to show __str__
        lr = [run1]
        print(lr)       # Just to show __repr__

    argc = len(sys.argv)
    if argc == 1:   # Use stdin, or default filename
        inFile = open_file()
        assert not (inFile is None), "Assume valid file object"
        tset.process_input_stream(inFile, run1)
        inFile.close()
    else:
        for f in sys.argv[1:]:
            # Allow override of Debug from command line
            if f == "Debug":
                Debug = True
                continue
            if f == "NoDebug":
                Debug = False
                continue

            inFile = open_file(f)
            assert not (inFile is None), "Assume valid file object"
            tset.process_input_stream(inFile, run1)
            inFile.close()

    print("--------------------------------------------")
    plabel = tset.get_env_variable("pos-label")
    print("pos-label: ", plabel)
    print("NOTE: Not using any target words from the file itself")
    print("--------------------------------------------")

    if Debug:
        tset.print_training_set()
    run1.print_config()
    run1.print_run_info()
    run1.eval_training_set(tset, plabel)

    return


if __name__ == "__main__":
    basemain()
