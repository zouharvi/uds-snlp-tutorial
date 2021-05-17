---
title:
- Smoothing
subtitle: |
    | (SNLP tutorial 4)
author:
- Vilém Zouhar, Awantee Deshpande, Julius Steuer
theme:
- Boadilla
date: TODOth, TODOth May 2021
aspectratio: 169
header-includes:
  - \AtBeginDocument{}

documentclass: beamer
# classoption: notes
---

# Overview

\begin{itemize}
\setlength{\itemsep}{-0.2cm}
\item Task, Metrics
\item Differential Privacy
\item Homework
\end{itemize}

# Entropy

- Amount of information / compressed size in bits
- $H(p) = E[-\log(p(V))] = - \sum p(v) \log(p(v))$
- For binomial distribution highest in the middle
- For uniform distribution: $\log(W)$
- Entropy is always non-negative
- H((W,W)) = H(W)+H(W) when statistically independent p(w1,w2) = p(w1)p(w2)
- Conditional entropy: $H(X|Y) = -\sum p(x,y) \log p(x|y)$

# Kullback-Leibler Divergence

- $D(p||q) = \sum p_i \log p_i/q_i$
- Not symmetric
- Non-negative
- How many extra bits if we use bad encoding

- Cross-entropy: $- \sum p_i \log q_i$

# Code

- Mapping of word to a finite string of a $D$-nary alphabet
- Prefix code
- $\sum D^{-l_i} \le 1$
- - Krafts inequality
- - true for prefix codes
- - for every length distribution satisfying this, there exists a prefix code

- Expected length: $\sum l_i p(w_i)$
- Optimal length: $-\log_D p(w_i)$

# Correlation Function

- $p_d(w1,w2)/( p(w1) p(w2))$


# OOV words

::: frame
## Corpus
* Train set: 

\qquad ![](img/apple.png){width=20px}
![](img/apple.png){width=20px}
![](img/apple.png){width=20px}
![](img/eggplant.png){width=20px}
![](img/apple.png){width=20px}
![](img/banana.png){width=20px}
![](img/banana.png){width=20px}
![](img/cherries.png){width=20px}
![](img/apple.png){width=20px}
![](img/eggplant.png){width=20px}
![](img/banana.png){width=20px}
![](img/banana.png){width=20px}
![](img/cherries.png){width=20px}
![](img/banana.png){width=20px}
![](img/apple.png){width=20px}
![](img/eggplant.png){width=20px}


* Test set:

\qquad ![](img/dark_chocolate.png){width=20px}
![](img/apple.png){width=20px}
![](img/fries.png){width=20px}
![](img/banana.png){width=20px}
![](img/apple.png){width=20px}
![](img/eggplant.png){width=20px}
![](img/eggplant.png){width=20px}
![](img/banana.png){width=20px}
![](img/cherries.png){width=20px}
![](img/fries.png){width=20px}
![](img/apple.png){width=20px}
![](img/apple.png){width=20px}

:::

. . .

::: frame
## Accumulate counts

* 
![](img/apple.png){width=20px} `6` \qquad
![](img/banana.png){width=20px} `5`  \qquad
![](img/eggplant.png){width=20px} `3` \qquad
![](img/cherries.png){width=20px} `2` \qquad


* 
![](img/apple.png){width=20px} `4` \qquad
![](img/banana.png){width=20px} `2`  \qquad
![](img/fries.png){width=20px} `2` \qquad
![](img/eggplant.png){width=20px} `2` \qquad
![](img/cherries.png){width=20px} `1` \qquad
![](img/dark_chocolate.png){width=20px} `1` \qquad
:::

. . .

:::frame
## OOV words
* What about ![](img/dark_chocolate.png){width=20px} and ![](img/fries.png){width=20px}?
* OOV rate: $2+1/4+2+2+1+1+1 = 27\%$
:::


# Additive smoothing (add-$\alpha$-smoothing)

:::frame
## Unigrams
* Add zero counts to frequency table

![](img/apple.png){width=20px} `6` \qquad
![](img/banana.png){width=20px} `5`  \qquad
![](img/eggplant.png){width=20px} `3` \qquad
![](img/cherries.png){width=20px} `2` \qquad
![](img/fries.png){width=20px} `0` \qquad
![](img/dark_chocolate.png){width=20px} `0` \qquad

* Increase all counts by $\alpha = 1$

![](img/apple.png){width=20px} `6+1` \qquad
![](img/banana.png){width=20px} `5+1`  \qquad
![](img/eggplant.png){width=20px} `3+1` \qquad
![](img/cherries.png){width=20px} `2+1` \qquad
![](img/fries.png){width=20px} `0+1` \qquad
![](img/dark_chocolate.png){width=20px} `0+1` \qquad

* Divide by $N = 22$

![](img/apple.png){width=20px} `0.32` \qquad
![](img/banana.png){width=20px} `0.27`  \qquad
![](img/eggplant.png){width=20px} `0.18` \qquad
![](img/cherries.png){width=20px} `0.13` \qquad
![](img/fries.png){width=20px} `0.05` \qquad
![](img/dark_chocolate.png){width=20px} `0.05` \qquad
:::

:::frame
## Perplexity
* Relative frequencies on test corpus:

![](img/apple.png){width=20px} `0.33` \qquad
![](img/banana.png){width=20px} `0.17`  \qquad
![](img/fries.png){width=20px} `0.17` \qquad
![](img/eggplant.png){width=20px} `0.17` \qquad
![](img/cherries.png){width=20px} `0.08` \qquad
![](img/dark_chocolate.png){width=20px} `0.08` \qquad

. . .

* PP = $2^{(0.33 \cdot 0.32 + 0.27 \cdot 0.17 + 0.18 \cdot 0.17 + 0.13 \cdot 0.17 + 2 \cdot (0.05 \cdot 0.08))} = 1.4$
:::

# Kneser-Ney Smoothing

TODO

- absolute discounting

# Cross-Validation

TODO

# Estimating LOO Parameters

TODO ??

# Laplace Smoothing

- add epsilon

TODO

# Linear Discounting

- linear interpolation


# Good-Turing Discounting

TODO

# Count Trees

- remove infrequent nodes

TODO

# Privacy

TODO differential privacy

# Resources

1. UdS SNLP Class, WSD: <https://teaching.lsv.uni-saarland.de/snlp/>
2. Classical Statistical WSD: <https://www.aclweb.org/anthology/P91-1034.pdf>
3. n-gram count trees: <http://ssli.ee.washington.edu/WS07/notes/ngrams.pdf>
