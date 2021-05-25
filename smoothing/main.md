---
title:
- Assignment 4+Smoothing
subtitle: |
    | (SNLP tutorial 4)
author:
- Vilém Zouhar, Awantee Deshpande, Julius Steuer
theme:
- Boadilla
date: 25th, 27th May 2021
aspectratio: 169
header-includes:
  - \AtBeginDocument{\usepackage{graphicx}}

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

# Assignment 4

- Exercise 1: Huffman encoding 
- Exercise 2: Conditional entropy of DNA
- Bonus: Huffman encoding adaptations

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

- Solutions? character-level, subword units

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



# Additive smoothing: Bigrams

Recall the additive smoothing formula for unigrams:

\begin{equation}
p_{smoothed}(w_i) = \frac{
  C(w_i) + \alpha
}{
  N + \alpha|V|
}
\end{equation}

. . .

* What is $N$? What is $V$?

Remember from Assignment 2 that:

\begin{equation}
p(w_i|w_{i-1}) = \frac{C(w_{i-1},w_i)}{C(w_{i-1})}
\end{equation}

. . .

* Smoothe the bigram count: $C(w_{i-1},w_i) \rightarrow C(w_{i-1}, w_i) + \alpha$

* Normalization: $p_{smoothed}(w_i|w_{i-1}) = \frac{C(w_{i-1},w_i) + \alpha}{\text{\large ?}}$


# Additive smoothing: Bigrams

::: frame
## Corpus 
![](img/apple.png){width=20px}
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

Bigrams:
![](img/apple.png){width=20px}![](img/apple.png){width=20px}, ![](img/apple.png){width=20px}![](img/apple.png){width=20px}, ![](img/apple.png){width=20px}![](img/eggplant.png){width=20px}, ![](img/eggplant.png){width=20px}![](img/apple.png){width=20px}, ..., ![](img/apple.png){width=20px}![](img/eggplant.png){width=20px}, ![](img/eggplant.png){width=20px}![](img/apple.png){width=20px} $\leftarrow$ circular bigram!

Bigrams: AA, AA, AE, EA, ..., AE, EA
:::


# Additive smoothing: Bigrams: bigram counts

* Collect bigram counts & condtional probabilities for history $A$

| Bigram | $C(w_i, w_{i-1})$ | $C(w_{i-1})$| $\frac{C(w_{i-1},w_i)}{C(w_{i-1})}$ |
| ------ | :-----: | :-----: | :---: |
| AE     | 3       | 6       | 1/2   |
| AA     | 2       | 6       | 1/3   |
| AB     | 1       | 6       | 1/6   |


# Additive smoothing: Bigrams: add alpha

* We encounter an unknown bigram $AF$

| Bigram | $C_{\alpha}(w_{i-1},w_i)$ | $C(w_{i-1})$| $\frac{C_{\alpha}(w_{i-1},w_i)}{C(w_{i-1})}$ |
| ------ | :-----: | :-----: | :---: |
| AE     | 3+1       | 6      | 4/6  |
| AA     | 2+1       | 6      | 3/6  |
| AB     | 1+1       | 6      | 2/6  |
| $\rightarrow$ AF | 0+1  | 6  | 1/6  |

. . .

* Not a probabilitiy distribution! 

. . .

* Solution: We need to adjust the divisor a tiny bit. But how tiny?


# Additive smoothing: Bigrams: normalization

* add $\alpha \cdot 4$ to history count! 
* Pretend that we have seen the history $|V| = 4$ times more.

. . .

| Bigram | $C{_\alpha}(w_{i-1}) + \alpha |V|$| $\frac{C_{\alpha}(w_{i-1},w_i)}{C(w_{i-1}) + \alpha |V|}$ |
| ------ | :-----: | :---: |
| AE     | 6 + 4   | 4/10  |
| AA     | 6 + 4   | 3/10  |
| AB     | 6 + 4   | 2/10  |
| $\rightarrow$ AF | 6 + 4 | 1/10 |

. . .

* Now the probabilities sum up to 1: $4/10 + 3/10 + 2/10 + 1/10 = 1$


# Additive smoothing: Bigrams: normalization

* We encounter another n-gram $AD$
* What is $|V|$ now?

. . .

| Bigram | $C{_\alpha}(w_{i-1}) + \alpha |V|$| $\frac{C_{\alpha}(w_{i-1},w_i)}{C(w_{i-1}) + \alpha |V|}$ |
| ------ | :-----: | :---: |
| AE     | 6 + 5   | 4/11  |
| AA     | 6 + 5   | 3/11  |
| AB     | 6 + 5   | 2/11  |
| $\rightarrow$ AF | 6 + 5 | 1/11 |
| $\rightarrow$ AD | 6 + 5 | 1/11 |

. . .

* $C(A)$ is constant, unsmoothed count
* Probabilities sum up to 1: $4/11 + 3/11 + 2/11 + 1/11 + 1/11 = 1$


# Additive smoothing: Bigrams: general case

* General formula for smoothed bigram Probabilities:

\begin{equation}
p(w_i|w_{i-1}) = \frac{C(w_{i-1},w_i) + \alpha}{C(w_{i-1}) + \alpha|V|}
\end{equation}

. . .

* What is $V$?

. . .

* $|V|$ = Number of bigram **types** starting with $w_{i-1}$

. . .

\begin{equation}
p(w_i|w_{i-1}) = \frac{C(w_{i-1},w_i) + \alpha}{C(w_{i-1}) + \alpha|V_{(w_{i-1},\bullet)}|}
\end{equation}

. . .

* For n-grams of length $n$:

\begin{equation}
p(w_i|w_{i-1}:w_{i-n+1} ) = \frac{C(w_{i-n+1}:w_i) + \alpha}{C(w_{i-n+1}:w_{i-1}) + \alpha|V_{(w_{i-n+1}:w_{i-1},\bullet)}|}
\end{equation}

# Additive smoothing: Bigrams: general case

* For n-grams of length $n$:

\begin{equation}
p(w_i|w_{i-1}:w_{i-n+1} ) = \frac{C(w_{i-n+1}:w_i) + \alpha}{C(w_{i-n+1}:w_{i-1}) + \alpha|V_{(w_{i-n+1}:w_{i-1},\bullet)}|}
\end{equation}

* We already now the shared (train + test) vocabulary $V$

. . .

* $V_{(A, \bullet)}$ is then $AA, AB, AC, AD, AE, AF$ $\Rightarrow$ $|V_{(A, \bullet)}| = 6 = |V|$

. . .

* We find that the formula we found is identical to the one on the lecture slides!

\begin{equation}
p(w_i|w_{i-1}:w_{i-n+1} ) = \frac{C(w_{i-n+1}:w_i) + \alpha}{C(w_{i-n+1}:w_{i-1}) + \alpha|V|}
\end{equation}


# Cross-Validation

TODO

# Estimating LOO Parameters


# Count Trees

- remove infrequent nodes

TODO

# Privacy

TODO differential privacy

# Resources

1. UdS SNLP Class, WSD: <https://teaching.lsv.uni-saarland.de/snlp/>
2. Classical Statistical WSD: <https://www.aclweb.org/anthology/P91-1034.pdf>
3. n-gram count trees: <http://ssli.ee.washington.edu/WS07/notes/ngrams.pdf>
