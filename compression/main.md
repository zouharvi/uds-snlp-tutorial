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
## OOV fruits
* What about ![](img/dark_chocolate.png){width=20px} and ![](img/fries.png){width=20px}?
* OOV rate: $2+1/4+2+2+1+1+1 = 27\%$
:::


# Additive smoothing (add-$\alpha$-smoothing)

:::frame
## Unifruits
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