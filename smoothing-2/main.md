---
title:
- Assignment 5 + Smoothing 2
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

# Linear Intepolation/Jelinek-Mercer smoothing

\centering
$B_1$: (FROZEN YOGHURT)

$B_2$: (FROZEN RED)

What will floor discounting do here? Can we interpolate our bigram model with a unigram model?

$$P(w|h) = \lambda_1 P(w|h) + (1 - \lambda_1) P(w)$$
Can be generalised to higher order n-grams.

::: frame
## Questions
- What condition must be fulfilled for higher n-grams?
- How is $\lambda_i$ determined?
- Can you smooth the above probabilities?
::: 

<!-- lambda determined using EM/Baum-Welch Algorithm -->
<!-- Can also interpolate multiple LMs as in Assignment 5 -->

# Backing-Off models
What other way can we use the lower-order n-gram distributions? Is a lot of context always a good thing?

Idea behind back-off models: Use information from a lower order n-gram distribution.

A "recursion" strategy...

\begin{equation}
{
  P(w|h) = 
  \begin{cases}
  \frac{N(w,h)-d}{N(h)} + \alpha(h)\beta(w|h) & \text{for N(w,h) > 0}\\
  \alpha(h)\beta(w|h) & \text{otherwise}
  \end{cases}
}
\end{equation}

# Absolute Discounting

::: frame
## Corpus
* Train set: 


\qquad ![](img/apple.png){width=12px}
![](img/apple.png){width=12px}
![](img/apple.png){width=12px}
![](img/eggplant.png){width=12px}
![](img/apple.png){width=12px}
![](img/banana.png){width=12px}
![](img/banana.png){width=12px}
![](img/cherries.png){width=12px}
![](img/apple.png){width=12px}
![](img/eggplant.png){width=12px}
![](img/banana.png){width=12px}
![](img/banana.png){width=12px}
![](img/cherries.png){width=12px}
![](img/banana.png){width=12px}
![](img/apple.png){width=12px}
![](img/eggplant.png){width=12px}


* Test set:

\qquad ![](img/dark_chocolate.png){width=12px}
![](img/apple.png){width=12px}
![](img/fries.png){width=12px}
![](img/banana.png){width=12px}
![](img/apple.png){width=12px}
![](img/eggplant.png){width=12px}
![](img/eggplant.png){width=12px}
![](img/banana.png){width=12px}
![](img/cherries.png){width=12px}
![](img/fries.png){width=12px}
![](img/apple.png){width=12px}
![](img/apple.png){width=12px}

:::

. . .

:::frame
## Distribution
* Vocabulary counts

![](img/apple.png){width=12px} `6` \qquad
![](img/banana.png){width=12px} `5`  \qquad
![](img/eggplant.png){width=12px} `3` \qquad
![](img/cherries.png){width=12px} `2` \qquad
![](img/fries.png){width=12px} `0` \qquad
![](img/dark_chocolate.png){width=12px} `0` \qquad

* Decrease all non-zero counts by some parameter d = 0.75

![](img/apple.png){width=12px} `6-0.75` \qquad
![](img/banana.png){width=12px} `5-0.75`  \qquad
![](img/eggplant.png){width=12px} `3-0.75` \qquad
![](img/cherries.png){width=12px} `2-0.75` \qquad
![](img/fries.png){width=12px} `0` \qquad
![](img/dark_chocolate.png){width=12px} `0` \qquad

* Divide by $N = 16$

![](img/apple.png){width=12px} `0.33` \qquad
![](img/banana.png){width=12px} `0.26`  \qquad
![](img/eggplant.png){width=12px} `0.14` \qquad
![](img/cherries.png){width=12px} `0.11` \qquad
![](img/fries.png){width=12px} `0` \qquad
![](img/dark_chocolate.png){width=12px} `0` \qquad
:::

Sum = 0.33+0.26+0.14+0.11 = 0.84 $\ne$ 1.

. . .

Idea: Utilise this probability mass for zero counts.

# Absolute Discounting

$$P(w|h) = \frac{c(w,h) - d}{c(h)}$$

Adjust the probability mass $1 - \sum_{h} \frac{c(w,h) - d}{c(h)}$

e.g. For bigrams,

$$P_{abs}(w_i|w_{i-1}) = \frac{max{N(w_{i-1}, w_i)-d, 0}}{\sum_{w'}N(w_{i-1}, w')} + \lambda(w_{i-1})P_{abs}(w_i)$$
$$P_{abs}(w_i) = \frac{max{N(w_i)-d, 0}}{\sum_{w'}N(w')} + \lambda(.)P_{unif}(w_i)$$
$$\texttt{where } \lambda(w_{i-1}) = \frac{d}{\sum_{w'}N(w_{i-1},w')} \cdot N_{1+}(w_{i-1}, \bullet)$$
$$\lambda(.) = \frac{d}{\sum_{w'}N(w')} \cdot N_{1+}$$

# Kneser-Ney Smoothing

TODO

# Pruning

TODO

# Assignment 6

- Exercise 1: MAP and MLE estimates
- Exercise 2: Good Turing Smoothing
- Exercise 3: Cross-Validation

# Resources

1. UdS SNLP Class: <https://teaching.lsv.uni-saarland.de/snlp/>
4. n-gram models: <https://web.stanford.edu/~jurafsky/slp3/3.pdf>
2. Twitter emojis