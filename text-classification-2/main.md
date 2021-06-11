---
title:
- Assignment 8,9 + Text Classification Basics
subtitle: |
    | (SNLP Tutorial 8)
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

# Overview


- Decision Trees
- Naïve Bayes
- kNN
- Perceptron
- SVM
- Homework

# Classification 

TODO

# Decision Trees

TODO

# Naïve Bayes

TODO

# kNN

TODO

# SVM

- Find a boundary that maximizes the distance to closest vectors
- If not possible, find one that minimizes the error
- Add the kernel trick

# Perceptron

- Binary classification
- Linear boundary in feature space
- $\hat{y} = \text{sign}(wx+b)$

. . .

Algorithm:

- $w_0 = \overrightarrow{0}$
- For every data point $x_i$
- - $\hat{y_i} = \text{sign}(w_k x_i +b)$
- - if $\hat{y_i} \ne y_i$:
- - - $w_{k+1} = w_k - \hat{y_i} \cdot x$
- - else:
- - - $w_{k+1} = w_k$

. . .

- TODO: illustration
- TODO: advantages/disadvantages

# Resources

1. UdS SNLP Class, WSD: <https://teaching.lsv.uni-saarland.de/snlp/>