# word-association-graph
A simple function to plot a word association graph between the nouns in a given text with the adjectives and verbs in the text.

* The input text is a string of sentences ending in periods. If the text does not have any period, it does not produce a plot.
* The output is a plot of the nouns in the text connected to the adjectives and verbs as they appear in the text.
* k is the 'spread factor' - lower the k, lesser the intra-cluster spread,and vice versa.
* The nodes are sized according to their degree.
* Nodes are colored red if they are nouns, yellow if they are adjectives, and green if they are verbs.

How to use:
```
# Download the file. Then:
from word_assoc_graph import plot_word_associations as pwa

# take the first paragraph of Wikipedia's description of Wikipedia as a sample text
import re
text = "Wikipedia was launched on January 15, 2001, by Jimmy Wales and Larry Sanger.[10] Sanger coined its name,[11][12] as a portmanteau of wiki[notes 3] and 'encyclopedia'. Initially an English-language encyclopedia, versions in other languages were quickly developed. With 5,748,461 articles,[notes 4] the English Wikipedia is the largest of the more than 290 Wikipedia encyclopedias. Overall, Wikipedia comprises more than 40 million articles in 301 different languages[14] and by February 2014 it had reached 18 billion page views and nearly 500 million unique visitors per month.[15] In 2005, Nature published a peer review comparing 42 science articles from Encyclopadia Britannica and Wikipedia and found that Wikipedia's level of accuracy approached that of Britannica.[16] Time magazine stated that the open-door policy of allowing anyone to edit had made Wikipedia the biggest and possibly the best encyclopedia in the world and it was testament to the vision of Jimmy Wales.[17] Wikipedia has been criticized for exhibiting systemic bias, for presenting a mixture of 'truths, half truths, and some falsehoods',[18] and for being subject to manipulation and spin in controversial topics.[19] In 2017, Facebook announced that it would help readers detect fake news by suitable links to Wikipedia articles. YouTube announced a similar plan in 2018." 
text = re.sub("[\[].*?[\]]", "", text) # Do more processing (like lemmatization, stemming, etc if you want)
pwa(text, k=0.5, font_size=26)
```
![capture](https://user-images.githubusercontent.com/39755678/50878135-25ef9000-1410-11e9-9992-56434eecd041.PNG)
