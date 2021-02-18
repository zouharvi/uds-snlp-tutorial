---
title:
- Latent Semantic Analysis
author:
- Vilém Zouhar
theme:
- Boadilla
date:
- February, 2021
aspectratio: 169

documentclass: beamer
classoption: notes
---

# Overview

- Document retrieval
- Document representation
- - Solution 1
- - Solution 2
- - - TF-IDF
- - Solution 3 (tf-idf)
- - Solution 4 (LDA/LSI)
- - - SVD

# Document retrieval

> - Query: **Goethe, devil** 
> - Document: \newline
    A: Wolfgang's idea of the demon Mephistopheles who makes a bet with God \newline
    B: Faust is Wolfgang **Goethe**'s play in German about a pact with the **devil** \newline
    C: **Devil**ishly good lasagne \newline
    D: The impact of **Goethe**'s demon play on the German literature:
> - How to rank them? \newline
    B (contains the two key words)\newline
    D (Goethe, literature)\newline
    A (Wolfgang - Goethe, Mephistopheles - devil)\newline
    C (unrelated context)
> - Can these inferences be made automatically? [2]

# Document representation

> - Represent the query and all documents as a vector \newline
    Measure their similarity (cosine distance: $\frac{D\cdot Q}{|D||Q|}$)
> - How to represent a query/document as a fixed size vector?

# Solution 1

> - Solution: vector with counts of words: \newline
    `(<the>, <a>, <dog>, <president>, ...)` \newline
    `(57, 68, 0, 2, ...)`
> - Issue: representation vectors are enormous
> - Issue: longer documents have naturally higher counts
> - Issue: useless stop words

# Solution 2

> - Solution: vector with counts of non-stop words, normalized by total words:\newline
    `(<dog>, <president>, <princess>, <thing>, ...)` \newline
    `(0, 0.0003, 0.00001, 0.08, ...)`.
> - Issue: some words naturally occur with higher frequency
    but don't contribute to document meaning (`<thing>`)
> - Issue: how do we know which words are useful?

# Term Frequency - Inverse Document Frequency

\begin{block}{TF-IDF}
$$\text{Corpus} C$$
$$tf(term, doc) = \frac{count_{doc}(term)}{|doc|}$$
$$df(term) = |\{doc| term \in doc, doc \in C\}|$$ 
$$idf'(term) = \frac{|C|}{df(term)}, idf(term) = \log_2\bigg(\frac{|C|}{df(term)}\bigg)$$
$$tf-idf(term, doc) = tf(term, doc) \times idf(term)$$
\end{block}

# Solution 3

- Solution: vector of tf-idf
- Good metrics to determine the significance of a term in a document collection

> - Issue: still enormous vectors

# Solution 4 (LSA/LSI)

- Solution: Perform dimensionality reduction using SVD
- $\rightarrow$ eigenvalues, singular value decomposition
- $A_{i,j} =$ # occurences of term $t_i$ id document $d_j$ (replace with tf-idf later)

||$d_1$|$d_2$|$d_3$|$d_4$|
|-|-|-|-|-|
|Wolfgang|1|1|0|0|
|Mephistopheles|1|0|0|0|
|Faust|0|1|0|0|
|Goethe|0|1|0|1|
|devil|0|1|1|0|
|demon|1|0|0|1|
|lassagne|0|0|1|0|
|German|0|1|0|1|

# SVD

- $A_{i,j} =$ # occurences of term $t_i$ id document $d_j$ (replace with tf-idf later)
- $(A^TA)_{i,j} =$ # same terms of documents $d_i$ and $d_j$
- $(AA^T)_{i,j} =$ # documents in which both terms $t_i$ and $t_j$ occur
- $S =$ eigenvectors of $A^TA$
- $U =$ eigenvectors of $AA^T$
- $S =$ roots of corresponding eigenvalues of $A^TA$
- $A=U S V^T$

\begin{block}{Eigenvalue}
TODO
\end{block}

# SVD - proof
\begin{gather*}
A=USV^T, A^T = VSU^T, S \text{ diagonal} \\
U^T U = V V^T = I \text{ orthogonal} \\
A A^T U = U S^2 \rightarrow U \text{ eigenvectors of } A A^T, S \text{ root of eigenvalues} \\
(\forall U_{i,\*}: A A^T U_{i,\*} = U_{i,\*} \cdot S^2_{i,i}) \\
A^T A V = V S^2 \rightarrow V \text{ eigenvectors of } A^T A, S \text{ root of eigenvalues} \\
(\forall V_{i,\*}: A^T A V_{i,\*} = V_{i,\*} \cdot S^2_{i,i}) \\
\end{gather*}

# LSA/LSI
- Order eigenvectors 

# Resources

1. <https://medium.com/acing-ai/what-is-latent-semantic-analysis-lsa-4d3e2d18417a>
2. <https://www.engr.uvic.ca/~seng474/svd.pdf>
3. <http://web.mit.edu/be.400/www/SVD/Singular_Value_Decomposition.htm>
