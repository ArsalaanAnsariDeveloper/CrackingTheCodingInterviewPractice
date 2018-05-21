# Check if two strings are permutations of each other


testcase1 = ['sumit', 'abcd' ]
testcase2 = ['tiums', 'bdea']

def permChecker(word1, word2):
    # Check if words are the same length

    if(len(word1) != len(word2)):
        return False
    
    letterSet = set()
    for w in word1:
        letterSet.add(w)
    for w in word2:
        if w not in letterSet:
            return False
    return True

for i in range(0, len(testcase1)):
    print(permChecker(testcase1[i], testcase2[i]))

        