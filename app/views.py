from flask import Flask, render_template
from app import app
import random
import networkx as nx
import pickle as pkl
import wordsEn


G=nx.read_gpickle("nodelist.gpickle")
word_set=wordsEn.word

nodes=G.nodes()
def createWordList():
    while(1):
            word1=random.choice(nodes)
            word2=random.choice(nodes)
            try:
                lpath=nx.shortest_path_length(G, word1, word2)
                if lpath>4 and lpath<11:
                    words=nx.shortest_path(G,word1,word2)
                    return words
                else:
                    continue
            except nx.NetworkXNoPath:
                continue


@app.route('/')
@app.route('/index')
def wordlist():
    words=createWordList()
    slicedWords = words[1:len(words)-1]
    shuffword = slicedWords.copy()
    random.shuffle(shuffword)

    return render_template('index.html', words=words, shuffword=shuffword, slicedWords=slicedWords)


if __name__ == "__main__":
    app.run(debug=True)
