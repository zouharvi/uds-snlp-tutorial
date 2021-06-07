---
title:
- Assignment 6 + Smoothing 3
subtitle: |
    | (SNLP Tutorial 7)
author:
- Vilém Zouhar, Awantee Deshpande, Julius Steuer
theme:
- Boadilla
date: 8th, 10th June 2021
aspectratio: 169
header-includes:
  - \AtBeginDocument{\usepackage{graphicx}}

documentclass: beamer
---

# Slides repository

\centering

[github.com/zouharvi/uds-snlp-tutorial](https://github.com/zouharvi/uds-snlp-tutorial)

\vspace{1cm}

\raggedright 

- Contributions welcome
- "Cheating" allowed

# Assignment 6

- Exercise 1: MAP and MLE
- Exercise 2: Good Turing Smoothing
- Exercise 3: Cross-Validation

# Kneser-Ney Smoothing

Idea: Can we use the lower order distributions in a better way?

\centering
I WENT TO THE GROCERY _________ .

Options:

$W_1$: STORE

$W_2$: YORK

. . .

Use the fact that YORK generally appears as context or \textit{continuation} of the word NEW. 

<!--add fruits example slide-->

# Kneser-Ney Smoothing

$$P_{continuation}(w) = \frac{|\{w': C(w',w) > 0\}|}{|\{(w_i, w_j): C(w_i, w_j) > 0\}|}  $$ 
<!--the history that precedes our word of interest-->

For bigrams,

$$P_{KN}(w_i|w_{i-1}) = \frac{\max\{C(w_{i-1}, w_i)-d,0\}}{\sum_{w'}C(w_{i-1}w')} + \lambda(w_{i-1})P_{CONTINUATION}(w_i)$$

$$ \lambda(w_{i-1}) = \frac{d}{c(w_{i-1})} \cdot |\{w: C(w_{i-1},w) > 0\}|$$ 
<!--Part 1: Normalised discount, Part 2: #times we apply normalised discount-->

# Kneser-Ney Smoothing

\centering

General Formula

$$P_{KN}(w_i|w_{i-n+1:i-1}) = \frac{\max\{C_{KN}(w_{i-n+1:i-1}, w_i)-d,0\}}{\sum_{w'}C_{KN}(w_{i-n+1:i-1}w')} + \lambda(w_{i-n+1:i-1}) \cdot P_{KN}(w_i|w_{i-n+2:i-1})$$

\begin{equation}
{ \text{where}
  C_{KN}(\bullet) = 
  \begin{cases}
  \text{count}(\bullet) & \text{for highest order} \\
  \text{continuation\_count}(\bullet) & \text{for lower orders}
  \end{cases}
}
\end{equation}

<!--Continuation count = #unique single word contexts for o -->

# Kneser-Ney Smoothing Questions

- How are unseen words handled by KN Smoothing? 
<!-- Back off to uniform distribution
https://stats.stackexchange.com/questions/114863/in-kneser-ney-smoothing-how-are-unseen-words-handled
-->

- For a KN-Smoothed language model,
$$\text{Information content("Vader")} = 15$$
$$\text{Information content("Star")} = 10$$
Which unigram is assigned a higher probability by KN smoothing? Would the information content be the same for absolute discounting?
<!-- p(vader) < p(star) -->

- Will the probabilities be affected for frequent higher order n-grams?
<!--the lower-order model is signficant only when count is small or zero in the higher-order model-->

- Can Kneser-Ney smoothing be implemented for unigrams?
<!--Kneyser-Ney is not designed for smoothing unigrams, because in this case it's nothing but additive smoothing-->

# Pruning

- Back-off models and interpolation save n-grams of all orders.

We are storing all $V^n + V^{n-1} + ... + V + 1$ distributions!

- Idea: Store the counts which exceed a threshold $c(\bullet) \geq K$. Also called a "cut-off".

# Assignment 7

- Exercise 1: Count Trees and Pruning
- Exercise 2: Kneser-Ney Smoothing
- Bonus: Comparison of smoothing techniques

# Resources

1. UdS SNLP Class: <https://teaching.lsv.uni-saarland.de/snlp/>
2. n-gram models: <https://web.stanford.edu/~jurafsky/slp3/3.pdf>
3. Kneser-Ney Smoothing: <https://medium.com/@dennyc/a-simple-numerical-example-for-kneser-ney-smoothing-nlp-4600addf38b8>
4. Comparison of Smoothing Techniques: <https://people.eecs.berkeley.edu/~klein/cs294-5/chen_goodman.pdf>