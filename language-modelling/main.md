---
title:
- Word Sense Disambiguation
subtitle: |
    | (SNLP tutorial)
author:
- Vilém Zouhar
theme:
- Boadilla
date: \today
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

# Zipf's Law

rank*freq = const

# Language Modelling

TODO

perplexity, mean rank;

# OOV

- OOV (train vs. test)
- OOV rate
- OOV-rate $\propto \frac{1}{\text{vocab size}^\alpha}$
- curse of dimensioniality

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