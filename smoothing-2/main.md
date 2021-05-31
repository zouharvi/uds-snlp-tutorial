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

# Cross-validation
- K-fold cross-validation: Divide data into k subsets, train on k-1 subsets and test on the remaining 1. 
- Leave One Out cross-validation: Train on all data points except one. Do this N times.

::: frame
## Questions
- Why is cross-validation beneficial?
- How does shuffling the dataset affect the LOOV score?
- When is k-fold cross-validation beneficial over standard cross-validation?
::: 
<!-- CV prevents overfitting, used in hyperparameter estimation --->

# Smoothing Techniques
Remember the basics!

We perform smoothing to keep a language model from assigning 0 or ~0 probabilities to rare/unseen events.

Different ways to do this...

# Floor Discounting

\center
$$ P(w|h) = \frac{N(w,h) + \epsilon}{N(h) + \epsilon \cdot V}$$

Variants: Laplace smoothing, Lidstone smoothing, add-$\alpha$ smoothing...

<!-- Where is Laplace smoothing useful? Text classification, where zero counts are relatively fewer... -->

# Linear Intepolation/Jelinek-Mercer smoothing

Consider

\centering
$B_1$: (FROZEN YOGHURT)

$B_2$: (FROZEN RED)


What will floor discounting do here? Can we interpolate our bigram model with a unigram model?

$$P(w|h) = \lambda_1 P(w|h) + (1 - \lambda_1) P(w)$$
Can be generalised to higher order n-grams.

Question:
What condition must be fulfilled for higher n-grams? How is $\lambda_i$ determined?

<!-- lambda determined using EM/Baum-Welch Algorithm -->
<!-- Can also interpolate multiple LMs as in Assignment 5 -->

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
4. n-gram models: <https://web.stanford.edu/~jurafsky/slp3/3.pdf>
2. Twitter emojis