---
title:
- Assignment 7 + Text Classification Basics
subtitle: |
    | (SNLP Tutorial 7)
author:
- Vilém Zouhar
theme:
- Boadilla
date: 15th, 17th June
aspectratio: 169
header-includes:
  - \AtBeginDocument{\usepackage{graphicx}}

documentclass: beamer
# classoption: notes
---

# Assignment 7

- Exercise 1: Count Tree
- Exercise 2: Kneser-Ney Smoothing
- Bonus: Smoothing Techniques

# Text Classification

Fill in the classes:

> - $f: \text{Text} \rightarrow C$ (classes/categories)
> - Topic detection: $\text{Document} \rightarrow$
> - $\qquad \{\text{politics}, \text{NLP}, \text{healthcare}, \text{sport}, \ldots\}$
> - Spam detection: $\text{Document}\rightarrow$
> - $\qquad \{\text{SPAM}, \text{BENIGN}, \text{MARKETING}\}$
> - Author identification/profiling: $\text{Document(s)}\rightarrow$
> - $\qquad \{\text{F. Bacon}, \text{W. Shakespeare}, \ldots\}$
> - Native language identification: $\text{Document}\rightarrow$
> - $\qquad \{\text{German}, \text{Polish}, \ldots\}$
> - POS Tagging: $\text{Sentence}\rightarrow$
> - $\qquad \{NN, VERB, PART., \ldots\}^{|S|}$
> - Sense Disambiguation: $\text{Word+sentence}\rightarrow$
> - $\qquad \text{Senses of Word}$

Issues with this?
<!-- No structure preserved, not practical -->

# Classification vs. Clustering

||Classification|Clustering|
|-|-|-|
|Method|???|???|
|Classes|???|???|
|# Classes|???|???|

. . .

||Classification|Clustering|
|-|-|-|
|Method|Supervised|Unsupervised|
|Classes|Given|Unknown|
|# Classes|Given|(Mostly) unknown|

# Binary vs. Multi-Class Classification

## Multi-Class
- $f: D \rightarrow \{\text{politics}, \text{NLP}, \text{healthcare}, \text{sport}, \ldots\}$

How to turn this into a binary classification?

. . .

## Binary
- $f_1: D \rightarrow \{\text{politics}, \text{not politics}\}$
- $f_2: D \rightarrow \{\text{NLP}, \text{not NLP}\}$
- $f_3: D \rightarrow \{\text{healthcare}, \text{not healthcare}\}$
- ...

. . .

How to turn multiple multi-class into a single multi-class?  

# Flat vs. Hiearchical

## Flat Classification
$f_1: D \rightarrow$ 
![](img/banana.png){width=20px}
![](img/apple.png){width=20px}
![](img/eggplant.png){width=20px}
![](img/cherries.png){width=20px}
![](img/grapes.png){width=20px}
![](img/potato.png){width=20px}
![](img/cauliflower.png){width=20px}
![](img/poisonivy.png){width=20px}

. . . 

## Hierarchical Classification
\centering

![](img/hierarchical.png){width=250px}


# Single-Category vs Multi-Category

> - $f: D \rightarrow 2^C$
> - Topic detection: $\text{Document} \rightarrow \{\text{politics}, \text{NLP}, \text{healthcare}, \text{sport}, \ldots\}$
> - Sentiment analysis: $\text{Document} \rightarrow \{\text{positive}, \text{negative}, \text{interested}, \ldots\}$


> - Topic detection: $\text{Document} \rightarrow {\{\text{(politics, news)}, \text{(NLP, Machine Learning)}, \text{(healthcare, nutrition)}, \text{(sport, biography)}, \ldots\}}$
> - Sentiment analysis: $\text{Document} \rightarrow {\{\text{(positive, happy)}, \text{(negative, sad)}, \text{(neutral, ambivalent)}, \ldots\}}$

# Feature Extraction

- Move from text to more processable domain
- How? (at least three "approaches")

. . .

## Binary/indicator features

$f_b(doc) = \begin{cases} 1 \qquad \text{Contains string } \texttt{"Super free \$\$\$ discount"} \\ 0 \qquad \text{Otherwise} \end{cases}$

## Integer features

$f_i(doc) = \text{Number of occurences of } \texttt{"buy"}$

## Real-valued features

$f_r(doc) = \frac{\text{Number of occurences of } \texttt{"buy"}}{|doc|}$

# Feature Selection

TODO

# Document Frequency

\begin{block}{DF}
$$df(term) = \frac{|\{doc| term \in doc, doc \in D\}|}{|D|}$$ 
\end{block}

- Remove rare items ($df \le \frac{2}{|D|}$) \newline
  Won't occur in new documents anyway
- Remove frequent items ($df = 1$) \newline
  Usually stop words \newline
  No information

  <!--scales easily to very large corpora with an approximately linear computational complexity in the number of training documents
  when a term belong to more than one class ,the evaluate function will make high score to it; however, if the term belong to a single category, lower frequency of occurrence lead to a lower score. DF evaluation function theory based on a hypothesis that rare term does not contain useful information (hence used with IDF to balance this).
  -->

. . .

- Sometimes not a good idea (interaction with other terms, etc.)
- Stopword distribution gives information in author identification

# Information Gain

- Information gained (reduction in entropy) by knowing whether a term is present

## 

\begin{align*}
G(C,t) =& H(C) - H(C|t) \\
=& - \sum_i p(c_i) \log p(c_i) \\
&+\ p(t) \sum_i p(c_i, t) \log p(c_i, t) \\
&+\ p(\overline{t}) \sum_i p(c_i, \overline{t}) \log p(c_i, \overline{t})
\end{align*}

<!--terms whose information gain is less than some predetermined threshold are removed from the feature space-->

# Pointwise Mutual Information

- Difference between observed distribution and independent

## 

\begin{align*}
\text{pmi}(c_i, t) = \log \frac{p(c_i, t)}{p(c_i)\cdot p(t)}
\end{align*}

- TODO (relation to mutual information)

# Chi Square $\chi^2$

$\chi^2 (c_1, c_2) = \sum_{tt,tf,ft,ff} (O-E)^2$

- TODO example
- TODO table

# Term Strength

- Two documents: $d_1, d_2$
- Term $t$
- $p(t \in d_2 | t\in d1)$
- _What is the probability that the term $t$ will be in $d_2$ given that it is in $d_1$?_
- If two documents related $\rightarrow$ high probability
- If two documents not related $\rightarrow$ low probability
- "Constant" with stop words

# Resources

1. UdS SNLP Class, WSD: <https://teaching.lsv.uni-saarland.de/snlp/>