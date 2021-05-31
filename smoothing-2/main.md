---
title:
- Assignment 5,6 + Smoothing 2
subtitle: |
    | (SNLP Tutorial 6)
author:
- Vilém Zouhar, Awantee Deshpande, Julius Steuer
theme:
- Boadilla
date: 1st, 2nd June 2021
aspectratio: 169
header-includes:
  - \AtBeginDocument{\usepackage{graphicx}}

documentclass: beamer
---

# Assignment 5

- Exercise 1: OOV Words
- Exercise 2: Additive smoothing
- Exercise 3: Perplexity, infinite smoothing, interpolation
- Bonus: Other language models

# Good-Turing

Data: ![](img/apple.png){width=15px}
![](img/apple.png){width=15px}
![](img/apple.png){width=15px}
![](img/eggplant.png){width=15px}
![](img/apple.png){width=15px}
![](img/banana.png){width=15px}
![](img/banana.png){width=15px}
![](img/cherries.png){width=15px}
![](img/apple.png){width=15px}
![](img/eggplant.png){width=15px}
![](img/banana.png){width=15px}
![](img/banana.png){width=15px}
![](img/cherries.png){width=15px}
![](img/eggplant.png){width=15px}
![](img/grapes.png){width=15px}
![](img/herb.png){width=15px}

. . .

::: columns
:::: column
- $N_4$ = \{![](img/banana.png){width=15px}\}
- $N_3$ = \{![](img/apple.png){width=15px}, ![](img/eggplant.png){width=15px}\}
- $N_2$ = \{![](img/cherries.png){width=15px}\}
- $N_1$ = \{![](img/grapes.png){width=15px}, ![](img/herb.png){width=15px}\}
- $N_0$ = \{![](img/ice_cream.png){width=15px}\}
::::

. . .

:::: column
$$p_r = \frac{(r+1)N_{r+1}}{N_r} \cdot \frac{1}{N}$$
::::
:::

. . .

- Nominator: expected total number of occurences of words that occur $r+1$ times
- Denominator-left: previous bucket size
- Fraction-left: expected number of occurences of a single word from that bucket
- Denominator-right: divide by total occurences

# Good-Turing - Questions

> - Let $k$ be the maximum occurence of a word. What's the issue?
> - A similar issue related to the one above? <!-- High frequency becomes sparse -->
> - Do the probabilities sum up to $1$?
> - How to make it work for anything above unigrams? <!-- Works for any freq distribution -->

# Assignment 6

- TODO

# Resources

1. UdS SNLP Class: <https://teaching.lsv.uni-saarland.de/snlp/>
2. Twitter emojis