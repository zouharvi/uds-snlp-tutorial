---
title:
- Assignment 9 + Word Sense Disambiguation
subtitle: |
    | (SNLP Tutorial 10)
author:
- Vilém Zouhar, Awantee Deshpande, Julius Steuer
theme:
- Boadilla
date: 29th June, 1st July
aspectratio: 169
header-includes:
  - \AtBeginDocument{\usepackage{graphicx}\usepackage{tikz}\usetikzlibrary{positioning,shapes,arrows}}

documentclass: beamer
# classoption: notes
---

# Assignment 9

- Exercise 1: Feature Engineering, Classification
- Bonus: Support Vector Machines

# Word Sense Disambiguation


\underline{Apple} is full of vitamins. \newline
\underline{Apple} was struggling last quarter. \newline
\underline{Apple} was thrown away from the meeting.

. . .

\centering 
![](img/apple_0.png){width=15%} \qquad \qquad \qquad ![](img/apple_1.png){width=13%}

. . .

\vspace{0.5cm}

\raggedright
$f(w, C) = s \in S_w$ \newline
$f(\text{Apple}, \text{* was thrown away from the meeting}) \in \{\text{fruit}, \text{company}\}$

# Word Sense Disambiguation

Machine translation:

- Apfel ist voller Vitamine.
- Apple ist voller Vitamine.
- Apfel hatte im letzten Quartal Probleme. 
- Apple hatte im letzten Quartal Probleme. 

. . .

Information retrieval:

- Query: Apple vitamins
- Relevant document: benefits of eating apples

. . .

Dialogue systems

Spelling correction

# One sense per ...

One sense per discourse

- One meaning per word+document

. . .

One sense per collocation

- Nearby words help determine the sense

# Dictionary 

- Dictionary/Thesaurus: $\forall w, s \in S_w: D(s) = \text{ description of sense } s$
- Context: $\forall w, C(w) = \text{ context of word } w \text{ in a specific occurence}$

## Lesk's Algorithm

- Idea: Sense $s_i$ of ambiguous word $w$ is likely to be the correct sense if many of the words used in the dictionary definition of $s_i$ are also used in the definitions of words in the ambiguous word's context.

\centering
$s_{opt} = \underset{s_k}{\text{argmax}} \: sim\left(D(s_k), \bigcup_{v_j \in C} E(v_j)\right)$

<!-- Explain each of these terms --->

::: frame
## Similarity
<!-- Give an example here -->
\vspace*{-0.4cm}
\begin{gather*}
\frac{2|X\cap Y|}{|X|+|Y|}
\qquad \qquad \frac{2|X\cap Y|}{|X\cup Y|}
\qquad \qquad \frac{|X\cap Y|}{\sqrt{|X|\cdot|Y|}}
\end{gather*}
:::

- Advantages? Disadvantages?
<!--Simple, fast, Low performance-->

# Simplified Lesk's Algorithm Example

Sentence: The	*bank* can guarantee deposits	will eventually cover	future	tuition	costs	 because	it	invests	in	adjustable-rate	mortgage	securities.

::: frame 
## Senses

- $bank^1$ Gloss/Def$^n$: a financial institution that accepts deposits and channels the money into lending activities. \newline
e.g.: "She cashed a cheque at the bank".

- $bank^2$ Gloss/Def$^n$: sloping land (especially the slope beside a body of water). \newline
e.g.: "They had a picnic on the river bank".
:::

<!--Choose	sense	with	most	word	overlap	between	gloss	and	context (not	counting	function	words)-->
<!--Explain Senseval and WordNet-->

```
from nltk.corpus import senseval
hard, interest, line, serve = senseval.fileids()
line_instances = senseval.instances(line)
```
- Improvements include weighting by measures like IDF

# Supervised Disambiguation

## Bayes Decision

\vspace*{-0.4cm}
\begin{align*}
\hat{s} &= \arg \max_s p(s|C) = \arg \max_s \frac{p(C|s)\cdot(p(s))}{p(C)} \\
&= \arg \max_s p(C|s)\cdot(p(s))
\end{align*}

::: frame 
## Naïve Bayes

\vspace*{-0.4cm}
\begin{align*}
p(C|s) = \prod_{x \in C} p(x|s)
\end{align*}
:::

- Estimate by MLE counts (+ smoothing)
- Independence within context
- Position in context does not matter
- What kind of feature vectors can exist? 
<!--
Collocational features: Features	about	words	at	specific positions	near	target	word, word+POS
Bag of words: words	that	occur	anywhere	in	the	window	(regardless of position), frequency counts
-->
- Advantages? Disadvantages? <!--Needs large, annotated training corpus, quick to train, scales well with data-->

# Supervised Disambiguation Features Example

Sentence: Transactions on a deposit account of the *bank* are recorded in books, and the resulting balance is recorded as its liability.

- Collocational features:

[$w_{i-3}, POS_{i-3}, w_{i-2}, POS_{i-2} ... , w_{i+3}, POS_{i+3}$] \newline
[account, NN, of, PP, the, DT, ... ]

[$w_{i-2}, w_{i-1}, w_{i+1}$]

- Bag of Word Features \newline
Let V : {institution, account, water, land} \newline
Vector: [0, 1, 0, 0] for given sentence

# Unsupervised Disambiguation

> - Machine translation is able to choose the right sense \newline
  (assuming different senses have different translations)
> - \underline{Apple} was struggling last quarter. \newline
  \underline{Apple} hatte im letzten Quartal Probleme.
> - \underline{Apple} is full of vitamins. \newline
  \underline{Apfel} ist voller Vitamine.
> - Translations (in German): \{Apfel, Äpfel, Apple\}
> - Indicator words: \{struggling, quarter, full, vitamins\} (stopwords removed)

. . .

Partition translated words ($\{Q_1, Q_2\}$) and indicator words ($\{P_1, P_2\}$) to maximize:

\centering
$I(P;Q) = \sum_{i\in Q, t\in P} \log \frac{p(i, t)}{p(i)\cdot p(t)}$

# Flip-Flop Algorithm

<!--tries to find a single contextual feature that reliably indicates which sense of the ambiguous word is being used.-->

1. find random partition P = {$P_1$, $P_2$} of $t_1, ..., t_m$
2. while improving I(P;Q) do
3.  - find partition Q = {$Q_1$, $Q_2$} of $x_1, ..., x_n$ that maximises I(P;Q)
4.  - find partition P = {$P_1$, $P_2$} of $t_1, ..., t_m$ that maximises I(P;Q)
5. end

- $t_i$ : translations of the ambiguous word
- $x_i$ : indicator words
- I(P;Q) monotonically increases until convergence

. . . 

- Disambiguation \newline
Determine $x_i$

if $x_i \in Q_1$ assign sense 1 

if $x_i \in Q_2$ assign sense 2

<!--The Flip-Flop algorithm only disambiguates between 2 senses.-->

# EM Algorithm

- Idea: Random initialisation followed by parameter estimation
- Paramaters? **$P(v_j|s_k)$** and **$P(s_k)$**
- Maximise log-likelihood $\log \prod_i \sum_k P(c_i|s_k)P(s_k)$
- E step: $h_{ik} = \frac{P(c_i|s_k)P(s_k)}{\sum_l P(c_i|s_l)P(s_l)}$
- M step: $P(v_j|s_k) = \frac{\sum_i C(v_j \in c_i) \cdot h_{ik}}{\sum_j \sum_i C(v_j \in c_i) \cdot h_{ik}}$ \newline
  $P(s_k) = \frac{\sum_i h_{ik}}{\sum_k \sum_i h_{ik}}$ 
- Disambiguation: $s_{opt} = argmax_{s_k} [\log P(s_k) + \sum_{v_j \in C} \log P(v_j|S_k)]$

# Yarowsky Algorithm
- Utilises one sense per discourse and one sense per collocation
- Algorithm:

1. In a large corpus, identify all examples of a polysemous word, and store their contexts as an untagged training set. \newline
e.g. \newline
\scriptsize 
The company *plant* is still operational... \newline
The region abounts in *plant* life... \newline
The classification of *plant* and animal kingdoms...

\normalsize
2. For each sense of the word ($s_1 ... s_k$), identify collocations representative of the sense, and tag all the sentences from (1) which contain the seed collocation with the respective label. \newline <!--The remaining examples are left untagged-->
e.g. \newline
\scriptsize
Sense 1: The company *plant* is still operational \newline
Sense 2: The region abounds in *plant* life... \newline
Sense 2: The classification of *plant* and animal kingdoms

# Yarowsky Algorithm

3. a) Train on the seed sets (Sense 1, Sense 2). <!--This identifies the collocations that reliably partition the training data-->
   b) Apply the obtained classifier on the entire sample set. Only retain those tags that are above a certain probability threshold. Add these examples to the seed set. <!--These now include new collocations indicative of the seed set-->
   c) Use one sense per discourse to augment and correct the available data. \newline
e.g. \newline
\scriptsize 
Sense 1: The company *plant* is still operational \newline
? $\rightarrow$ Sense 1: The *plant* was shut down due to inflation.
\normalsize
   d) Repeat (3a) to (3c)
4. Hold training parameters constant, and the algorithm will converge on the residual set.
5. Apply the classifier to new data or original untagged data.

<!--If multiple collocations are indicative of the sense, the maximal Log L sense is picked where
log L = ln P(sense 1 | collocation)/P(sense 1 | collocation)-->

# Resources

1. UdS SNLP Class, WSD: <https://teaching.lsv.uni-saarland.de/snlp/>
2. Classical Statistical WSD: <https://www.aclweb.org/anthology/P91-1034.pdf>
3. WSD: <https://www.cs.toronto.edu/~frank/csc2501/Lectures/8%20Word%20sense%20disambiguation.pdf>
4. Lesk Algorithm: <https://www.c-sharpcorner.com/article/lesk-algorithm-in-python-to-remove-word-ambiguity/>
5. Yarowsky Algorithm: <https://www.coli.uni-saarland.de/courses/comsem-10/material/Victor_Santos_Yarowsky.pdf>
6. <https://www.aclweb.org/anthology/P95-1026.pdf>
7. <https://web.stanford.edu/~jurafsky/slp3/slides/Chapter18.wsd.pdf>