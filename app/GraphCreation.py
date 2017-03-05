import networkx as nx
import pickle as pkl
import wordsEn
import string
graph=nx.Graph()
characters=string.ascii_lowercase
word_set=wordsEn.word
def createEdge():
    for word in word_set:
        graph.add_node(word)
    for word in word_set:
        for i in range(len(word)):
            remove=word[:i]+word[i+1:]
            if graph.has_node(remove):
                graph.add_edge(word,remove)
            for char in characters:
                change=word[:i]+char+word[i+1:]
                if graph.has_node(change):
                    graph.add_edge(word,change)
                insert=word[:i]+char+word[i:]
                if graph.has_node(insert):
                    graph.add_edge(word,insert)
createEdge()

nx.write_gpickle(graph,"nodelist.gpickle")
