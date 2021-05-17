---
title:
- Compression
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
---

# Organisation

TODO

# Compression

TODO

# Encoding

::: frame
## Task
Create coding (into binary) for the following recipe: 

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

# Resources

1. Twitter emojis