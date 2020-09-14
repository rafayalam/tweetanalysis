import string

def topHashtags(n):
    #Finding hashtags in tweets
    hashtags = []
    linenum = 0
    substr = "#"
    with open ("twitter_data.txt", encoding = "utf8") as myfirstfile:
        for line in myfirstfile:
            line = line.lower()
            linenum +=1
            for word in line.split():
                if word.find(substr) != -1:
                    hashtags.append(word.rstrip("\n"))
    
    #Making list of tuples of most common hashtags
    from collections import Counter
    popularHashtags = [Counter(hashtags).most_common(n)]

    #Printing hashtags to new file in order from most popular to least
    mysecondfile = open("top_hashtags.txt", "w", encoding = "utf8")
    for i in popularHashtags:
        mysecondfile.write(str(i))
    mysecondfile.close()

n = int(input("Enter how many top hashtags you would like to view: "))
topHashtags(n)