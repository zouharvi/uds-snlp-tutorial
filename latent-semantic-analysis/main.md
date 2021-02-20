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
# classoption: notes
---

# Overview

- Document retrieval
- Document representation
- - Solution 1 (counts)
- - Solution 2 (tf)
- - Solution 3 (tf-idf)
- - Solution 4 (LSA, SVD)

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
    Measure their similarity (L-norm, cosine distance: $\frac{D\cdot Q}{|D||Q|}$)
> - How to represent a query/document as a fixed size vector?

# Solution 1 (counts)

> - Solution: vector with counts of words: \newline
    `(<the>, <a>, <dog>, <president>, ...)` \newline
    `(57, 68, 0, 2, ...)`
> - Issue: representation vectors are enormous
> - Issue: longer documents have naturally higher counts
> - Issue: useless stop words

# Solution 2 (tf)

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
> - Issue: `demon - Mephistopheles` are equally separate concepts as `demon - lassagne`

# Solution 4 (LSA)

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

\note{
    The example uses counts, but for better representation of term importance in the document, one would use tf-idf.
}

# SVD

- $A_{i,j} =$ # occurences of term $t_i$ id document $d_j$ (replace with tf-idf later)
- $(A^TA)_{i,j} =$ # same terms of documents $d_i$ and $d_j$
- $(AA^T)_{i,j} =$ # documents in which both terms $t_i$ and $t_j$ occur
- $S =$ eigenvectors of $A^TA$
- $U =$ eigenvectors of $AA^T$
- $S =$ roots of corresponding eigenvalues of $A^TA$
- $A=U S V^T$

# Eigen{vector,value}

Nonzero $v \in \mathbb{R}^n, \lambda \in \mathbb{R}$

\begin{block}{Eigenvector}

$$
Av = \lambda v \qquad
Av = \lambda I v \qquad
(A-\lambda I)v = 0 \qquad
ker (A-\lambda I)
$$

"Directions ($v$) which $A$ only scales."
\end{block}


\begin{block}{Eigenvalue}

$$Av = \lambda v$$

"The stretch ($\lambda$) of eigenvector $v$ by $A$."
\end{block}

# SVD - "proof"
\begin{gather*}
A=USV^T, A^T = VSU^T, S \text{ diagonal} \\
U^T U = V V^T = I \text{ orthogonal} \\
A A^T U = U S^2 \rightarrow U \text{ eigenvectors of } A A^T, S \text{ root of eigenvalues} \\
(\forall U_{i,\*}: A A^T U_{i,\*} = U_{i,\*} \cdot S^2_{i,i}) \\
A^T A V = V S^2 \rightarrow V \text{ eigenvectors of } A^T A, S \text{ root of eigenvalues} \\
(\forall V_{i,\*}: A^T A V_{i,\*} = V_{i,\*} \cdot S^2_{i,i}) \\
\end{gather*}

# LSA

1. Order eigenvectors by descending values ($S_{i,i} > S_{i+1,i+1}$)
2. Take top-k eigenvectors + values (or all above threshold)
3. $A_K = U_K S_K V^T_K$ $[(m\times n), (n\times n), (n\times n)] \rightarrow [(m\times k), (k\times k), (k\times n)]$

> - Term $\rightarrow$ term representation: $U_k S_k$
> - Term representation $\rightarrow$ term representation: $S_k V_k^T$

# LSA Concepts

- $U_k \S_k$ maps terms to "concepts" $(m \rightarrow k)$
- $(\S_k V_k^T)^T=V_k \S_k^T=V_k \S_k$ maps documents to "concepts" $(n \rightarrow k)$
- "concepts" are latent

\note{
    - The k then becomes obvious is the number of concepts
    - We don't specify the concepts, they are determined by SVD
    - From our point of view, they are latent
}

# LSA Example


||$d_1$|$d_2$|$d_3$|$d_4$|
|-|-|-|-|-|
|Wolfgang|1|1|0|0|
|Mephistopheles|1|0|0|0|
|...||||

> - Choose $k=2$
> - Representation of `Goethe`: fourth row of $U_k$ ($m\times k \rightarrow 1\times 2$) scaled by $S_k$: $[0.13, -0.13]^T$
> - Representation of `devil`: fifth row of $U_k$ ($m\times k \rightarrow 1\times 2$) scaled by $S_k$: $[0.58, -0.01]^T$
> - Representation of $d_1$: first column of $V_k^T$ ($k\times n \rightarrow 2\times 1$) scaled first by $S_k$: $r_d = [0.3, 0.02]^T$
> - Query representation: vector average: $r_q = [0.13, -0.13]^T/2 + [0.58, -0.01]^T/2 = [0.355, -0.07]^T$
> - Query-document match: cosine similairty:  $\frac{r_q \cdot r_d}{|r_q| \cdot |r_d|} = \frac{0.01205}{.10879} \approx 0.11$

\note{
    - Whether that's a good match or not depends on the ranking and/or threshold
}

# LSA Graphics

![Term-document matrix, no ordering, $k=5$; Source [6]](img/visualization_0.png){height=80%}

# LSA Graphics

![Term-document matrix, group documents, $k=5$; Source [6]](img/visualization_1.png){height=80%}

# LSA Graphics

![Term-document matrix, group documents+terms, $k=5$; Source [6]](img/visualization_2.png){height=80%}

# Notes

Fast SVD

> - Naive approach $det (A-\lambda I) =$ solving $n$-th order polynomial (variable $\lambda$)
> - Jacobi rotation [4, 5]: \newline
    Create almost a diagonal matrix (bidiagonal): $A = U B V$, $O(m n^2)$ \newline
    Compute SVD of $2\times 2$ matricis $O(n^2)$

. . .

Latent Semantic Analysis

> - Also called LSI (Latent Semantic Indexing)
> - tf-idf is just a weighting scheme (tf, counts)

\note{
    - tf-idf is not a vital part of LSA, though works well

    TODO
}

# Resources

1. Python code: <https://medium.com/acing-ai/what-is-latent-semantic-analysis-lsa-4d3e2d18417a>
2. Comprehensive tutorial for LSA+SVD: <https://www.engr.uvic.ca/~seng474/svd.pdf>
3. SVD example: <http://web.mit.edu/be.400/www/SVD/Singular_Value_Decomposition.htm>
4. Computation: <https://en.wikipedia.org/wiki/Singular_value_decomposition#Calculating_the_SVD>
5. Computation: <https://www.cs.utexas.edu/users/inderjit/public_papers/HLA_SVD.pdf>
6. Visualization: <https://topicmodels.west.uni-koblenz.de/ckling/tmt/svd_ap.html>