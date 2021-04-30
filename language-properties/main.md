---
title:
- Introduction
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
---

# Overview 

- Perplexity
- Maximum Likelihood Estimation
- Smoothing

# Perplexity

::: frame
## Formulas

\begin{gather*}
2^{\frac{1}{n} \sum^n_1 \log p(w_i|w_{i-1})} \\
2^{-\sum_{w,h}f(w,h)\log_2 P(w|h)}
\end{gather*}
::: 

TODO

# Maximum Likelihood Estimation

TODO

- A way to estimate language model (distribution) parameters
- Trying to maximize probability of the training data

# LM Smoothing

TODO

- Q: What happens if an unknown token is encountered and LM assigns it 0 probability?

# Homework

- Perplexity calculation by hand
- Plotting n-grams
- MLE language model and smoothing
- Custom alternative to perplexity

# Resources

1. TODO