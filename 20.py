n=int(raw_input())
main=[]
new=[]
for i in range(n):
    r=raw_input()
    main.append(r)
for word in main:
    l=[]
    for each in word:
        l.append(each)
    wordlen=len(word)
    new_word=[]
    new_word2=[]
    if(wordlen%2==0):
        l.insert(wordlen,"0")
        for t in range(0,wordlen+1,2):
            new_word.append(l[t])
        for y in range(1,wordlen,2):
            new_word2.append(l[y])
            new_word3=new_word2[::-1]
        last_word = new_word3 + new_word
        last_word=last_word[::-1]
        last_word.remove('0')
        new.append("".join(last_word))
    elif(wordlen%2!=0):
        for t in range(0,wordlen,2):
            new_word.append(l[t])
        for y in range(1,wordlen-1,2):
            new_word2.append(l[y])
            new_word3=new_word2[::-1]
        last_word = new_word3 + new_word
        new.append("".join(last_word))
for q in new:
    print q


