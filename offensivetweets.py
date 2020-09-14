import string

def foulLanguage(filename):
    #Storing potential swear words to a list
    with open ("swear_words.txt") as myfirstfile:
        swearwords = myfirstfile.readlines()
    swearwords = [x.strip() for x in swearwords]
    print(swearwords)

    #Finding swear words in tweets
    foul = []
    linenum = 0
    with open (filename, encoding = "utf8") as mysecondfile:
        for line in mysecondfile:
            line = line.lower()
            linenum +=1
            for i in range(len(swearwords)):
                if line.find(swearwords[i]) != -1:
                    foul.append("Line " +str(linenum) + ": " + line.rstrip("\n"))
    
    #Writing tweets with swear words to new file
    mythirdfile = open("potentially_offensive_tweets.txt", "w")
    for bad in foul:
        mythirdfile.write(bad)
        mythirdfile.write("\n")
    mythirdfile.close()

foulLanguage("twitter_data.txt")