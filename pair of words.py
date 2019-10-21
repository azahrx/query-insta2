import pandas as pd
import re
import pymongo

file = input("File untuk pair of words:\n")
output = 'pairofwords.csv'
df = pd.read_csv(file)
length = len(df)
print("Banyak data: "+str(length))

df.drop_duplicates(keep=False,inplace=True)
length = len(df)
print("Hapus duplikat: "+str(length)+"\n")

acc = df.Account.drop_duplicates()
databaru = pd.DataFrame(columns=["userid","username", "word1", "word2", "jumlah"])
userid = 1
idx = 0

# Mengolah data per user
for i, username in acc.iteritems():
    print("Data untuk user: "+username)
    setiapacc = df.loc[df['Account'] == username]
    psgn = set()
    forcapt = ""
    for j, row in setiapacc.iterrows():
        capt = str(row['Post'])
        allcapt += capt+" "
        splitcapt = caption.split()
        pjg = len(splitcapt)
        for a in range(pjg-1):
            pairofwords = splitcapt[a] + " " + splitcapt[a+1]
            psgn.add(pairofwords)
    forcapts = forcapts.replace("\n","")
    occurences = {}
    count = 0
    psgnallcapt = []
    splitcapts = forcapts.split()
    pjgall = len(splitcapts)
    for a in range(pjgall - 1):
        pairofwords = splitcapts[a] + " " + splitcapts[a+1]
        psgntiapcapt.append(pairofwords)
    for b in psgn:
        count = 0
        for c in psgntiapcapt:
            if b == c:
                count += 1
        occurences[b] = count
    occurences = dict(sorted(occurences.items(), key=lambda x: x[1], reverse=True))
    for key, value in occurences.items():
        words = key.split()
        word1 = words[0]
        word2 = words[1]
        if word1 == '' or word2 == '':
            continue
        data = pd.DataFrame({"userid":[userid], "word1":[word1], "word2":[word2], "jumlah":[value]}, index=[idx])
        with open(output, 'a', encoding="utf-8", newline='') as f:
            data.to_csv(f, header=f.tell()==0)
        idx += 1
    id_user += 1

db.myCollection.insert(df.to_dict())
