#REMOVE PASS AND FIX THIS FUNCTION
def anagram(word1, word2):
    if len(word1) != 0 and len(word2) != 0:
        if len(word1) == len(word2):
            word1 = word1.lower()
            word2 = word2.lower()
            for i in range(len(word1)):
                if word1[i] in word2:
                    yes = "yay"
                else:
                    return(False)
                    yes = "sad"
                    break
                if yes == "yay":
                    return(True)
        else:
            return(False)
    else:
        return(False)


if __name__ == '__main__':
    word1 = input()
    word2 = input()
    print(anagram(word1,word2))

    