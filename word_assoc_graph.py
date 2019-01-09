import nltk
import pandas as pd
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
from nltk.sentiment.vader import SentimentIntensityAnalyzer

def word_association_graph(text, k=0.4, font_size=24):
    '''
    -The input text is a string of sentences ending in periods. If the text does not have any period, it does not produce a plot.
    -The output is a plot of the nouns in the text connected to the adjectives and verbs as they appear in the text.
    -k is the 'spread factor' - lower the k, lesser the intra-cluster spread,and vice versa.
    -The nodes are sized according to their degree.
    -Nodes are colored red if they are nouns, yellow if they are adjectives, and green if they are verbs.
    '''
    nouns_in_text = []
    is_noun = lambda pos: pos[:2] == 'NN'

    for sent in text.split('.')[:-1]:   
        tokenized = nltk.word_tokenize(sent)
        nouns=[word for (word, pos) in nltk.pos_tag(tokenized) if is_noun(pos)]
        nouns_in_text.append(' '.join([word for word in nouns if not (word=='' or len(word)==1)]))

    nouns_list = []
    
    for sent in nouns_in_text:
        temp = sent.split(' ')
        for word in temp:
            if word not in nouns_list:
                nouns_list.append(word)

    df = pd.DataFrame(np.zeros(shape=(len(nouns_list),2)), columns=['Nouns', 'Verbs & Adjectives'])
    df['Nouns'] = nouns_list

    is_adjective_or_verb = lambda pos: pos[:2]=='JJ' or pos[:2]=='VB'
    for sent in text.split('.'):
        for noun in nouns_list:
            if noun in sent:
                tokenized = nltk.word_tokenize(sent)
                adjectives_or_verbs = [word for (word, pos) in nltk.pos_tag(tokenized) if is_adjective_or_verb(pos)]
                ind = df[df['Nouns']==noun].index[0]
                df['Verbs & Adjectives'][ind]=adjectives_or_verbs

    fig = plt.figure(figsize=(30,20))
    G = nx.Graph()
    for i in range(len(df)):
        G.add_node(df['Nouns'][i])
        color_map.append('blue')
        for word in df['Verbs & Adjectives'][i]:
            G.add_edges_from([(df['Nouns'][i], word)])
            
    pos = nx.spring_layout(G, k)
    
    d = nx.degree(G)
    node_sizes = []
    for i in d:
        _, value = i
        node_sizes.append(value)
    
    color_list = []
    for i in G.nodes:
        value = nltk.pos_tag([i])[0][1]
        if (value=='NN' or value=='NNP' or value=='NNS'):
            color_list.append('red')
        elif value=='JJ':
            color_list.append('yellow')
        else:
            color_list.append('green')
        
    nx.draw(G, pos, node_size=[(v+1)*200 for v in node_sizes], with_labels=True, node_color=color_list, font_size=font_size)
    plt.show() 
