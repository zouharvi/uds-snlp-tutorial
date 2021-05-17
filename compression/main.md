---
title:
- Assignment 3 + Compression
subtitle: |
    | (SNLP Tutorial 4)
author:
- Vilém Zouhar, Awantee Deshpande, Julius Steuer
theme:
- Boadilla
date: 18th, 20th May 2021
aspectratio: 169
header-includes:
  - \AtBeginDocument{}
---

# Assignment 3

- Exercise 1: Entropy Intuition
- Exercise 2: Uncertainty of events
- Exercise 3: KL Divergence
- Bonus: KL Divergence calculation

# Compression

- Prefix Codes: No whole code word is a prefix of any other code word 
- Uniquely decodable codes: Each word maps to one and only one code word

. . .

Prefix codes are a subset of uniquely decodable codes!

::: frame
## Optimal length of code words
$$l_i = -\log_D p(w_i)$$ <!--What does this imply? The most frequent words will have the shortest code lengths -->
:::

# Kraft's Inequality

$$\sum_{i=1}^m D^{-l_i} \le 1$$

> What does the sum < 1 imply? <!-- Redundancy -->

> What does the sum = 1 imply? <!-- Complete code -->

> What does the sum > 1 imply? <!-- Not uniquely decodable -->

> What does this tell us about uniquely decodable and prefix codes? <!-- Given a uniquely decodable code, we can construct a prefix code with the same lengths --->

## Exercise: Test Kraft's Inequality on Morse Code
(Hint: What is the encoding alphabet?)

# Encoding

::: frame
## Task
Create encoding (binary) for the following recipe: 

\footnotesize `apple apple banana cherries apple dark_chocolate eggplant banana cherries banana ...`

![](img/apple.png){width=20px}
![](img/apple.png){width=20px}
![](img/banana.png){width=20px}
![](img/banana.png){width=20px}
![](img/cherries.png){width=20px}
![](img/apple.png){width=20px}
![](img/dark_chocolate.png){width=20px}
![](img/eggplant.png){width=20px}
![](img/banana.png){width=20px}
![](img/cherries.png){width=20px}
![](img/banana.png){width=20px}
![](img/apple.png){width=20px}
![](img/eggplant.png){width=20px}
![](img/fries.png){width=20px}
:::

. . .

::: frame
## Fixed-width encoding
![](img/apple.png){width=20px} `000` \qquad
![](img/banana.png){width=20px} `001`  \qquad
![](img/cherries.png){width=20px} `010` \qquad
![](img/dark_chocolate.png){width=20px} `011` \qquad
![](img/eggplant.png){width=20px} `100` \qquad
![](img/fries.png){width=20px} `101` \qquad

Length = $14 \times 3 = 42$ 
:::

::: frame
## Issues?
- Encoding for ![](img/apple.png){width=20px} and ![](img/dark_chocolate.png){width=20px}?
- What do `110` and `111` mean? <!-- Are we underutilizing the channel?  -->
:::

# Encoding - Huffman

<!-- space for showing of huffman -->

\vspace{6cm}

::: frame
##
$4\times$ ![](img/apple.png){width=20px} A \qquad
$4\times$ ![](img/banana.png){width=20px} B \qquad 
$2\times$ ![](img/cherries.png){width=20px} C \qquad
$2\times$ ![](img/eggplant.png){width=20px} E \qquad
$1\times$ ![](img/dark_chocolate.png){width=20px} D \qquad
$1\times$ ![](img/fries.png){width=20px} F \qquad
:::

# Huffman Bonus

- When will the Huffman tree be balanced?
- How do we store the tree? Does the efficiency of this matter? 
- Are there undefined sequences of bits when using Huffman encoding? <!-- at most one -->
- Does the result of Huffman encoding depend on the text ordering? \newline
E.g. 
![](img/apple.png){width=20px}
![](img/banana.png){width=20px}
![](img/banana.png){width=20px}
![](img/dark_chocolate.png){width=20px}
vs.
![](img/banana.png){width=20px}
![](img/dark_chocolate.png){width=20px}
![](img/apple.png){width=20px}
![](img/banana.png){width=20px}
- Can there be two equally good Huffman encodings?

# Long Range Dependencies

- Correlation
- Conditional entropy

# Resources

1. Twitter emojis
2. https://www.ics.uci.edu/~dan/pubs/DC-Sec1.html
3. https://en.wikipedia.org/wiki/Shannon%27s_source_coding_theorem
