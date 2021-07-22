---
title: |
    | Information Retrieval + Q\&A
subtitle: |
    | (SNLP Tutorial 12)
author:
- Vilém Zouhar, Awantee Deshpande, Julius Steuer
theme:
- Boadilla
date: 13th July, 15th July
aspectratio: 169
header-includes:
  - \AtBeginDocument{\usepackage{tikz}\usetikzlibrary{positioning,shapes,arrows}}
documentclass: beamer
# classoption: 
# classoption: notes
classoption: handout,notes
---

# Evaluation metrics

- Documents $D$, queries $Q$
- System: $Q \rightarrow \mathcal{P}(D)$
- For $q\in Q:$ retrieved (output), relevant (gold)

. . .

::: columns
:::: column
## 
- Recall $\frac{|\text{retrieved} \cap \text{relevant}|}{|\text{relevant}|}$
- Precision $\frac{|\text{retrieved} \cap \text{relevant}|}{|\text{retrieved}|}$
::::

<!-- :::: column
## Questions?
- When will precision be high? ![](img/apple.png){width=15px}
- When will recall be high? ![](img/pineapple.png){width=15px} 
<!--example of classifing apples/not-apples in a dataset of apples and pineapples
::::
-->

:::: column
## How to cheat so that...
- precision is high?
- recall is high?
::::
:::

. . .

## {Precision,Recall}$@k$ : Retrieve $k$ documents (top $k$ scoring) 
- Recall$@k$ $\frac{|\text{retrieved}@k \cap \text{relevant}|}{|\text{relevant}|}$
- Precision$@k$ $\frac{|\text{retrieved}@k \cap \text{relevant}|}{|\text{retrieved}@k|} = \frac{|\text{retrieved}@k \cap \text{relevant}|}{k}$

# Evaluation metrics

- Average precision: $AveP(q) = \frac{\sum_k P@k \times rel(k)}{|\text{relevant}|}$
- $rel(k) = \begin{cases} 1 \qquad k\text{-th document relevant} \\ 0 \qquad otherwise\end{cases}$

. . .

- Mean average precision $MAP(Q) = \frac{\sum_{q\in Q} AveP(q)}{|Q|}$
- - $Q$ can be a "test set"

. . .

- F-score $2 \cdot \frac{P \cdot R}{P+R}$

# Evaluation metrics

- Taking the rank into consideration: Mean Reciprocal Rank
- $MRR(Q) = \frac{1}{|Q|}\sum_{q \in Q} \frac{1}{\text{rank}_q}$ \newline
  $\text{rank}_q =$ position of the first relevant document 

. . .

|document|rank|relevant|
|:-:|:-:|:-:|
|a|4|+|
|b|1||
|c|||
|d||+|
|e|2|+|
|f|3||

. . .

\vspace{-0.3cm}

- $Q = \{\text{example}\}, MRR(Q) = \frac{1}{\text{rank}_{example}} = \frac{1}{2}$

::: notes
Lots of others, accuracy, r-precision etc. Papers (as compared to MT) usually use a lot of different metrics.
:::


# Information retriveal - preprocessing

> - Stemming (_going $\rightarrow$ go_, _studies $\rightarrow$ studi_)
> - \- Not always: query _becomes stressed_ vs. _becom stress_
> - Lemmatization (_going $\rightarrow$ go_, _studies $\rightarrow$ study_)
> - \- Not always: query _becomes stressed_ vs. _become stress_
> - Stop words (_for, of, and, or_)
> - \- Not always: query _Wizard of Oz_ vs. _Wizard Oz_
> - Typo correction (_Wizzard $\rightarrow$ Wizard_)
> - \- Not always: query _Tokyo_ vs. _Tokio_

. . .

Always depends on the task.

# Document Retrieval - example

> - Query: **Goethe, devil** 
> - Document: \newline
    A: Wolfgang's idea of the demon Mephistopheles who makes a bet with God \newline
    B: Faust is Wolfgang **Goethe**'s play in German about a pact with the **devil** \newline
    C: **Devil**ishly good lasagne \newline
    D: The impact of **Goethe**'s demon play on the German literature
> - How to rank them? \newline
    B (contains the two key words)\newline
    D (Goethe)\newline
    A (Wolfgang - Goethe, Mephistopheles - devil)\newline
    C (unrelated context)
> - Can these inferences be made automatically?

<!-- # Document Retrieval - Bag of Words

- Text must be represented as a vector of numbers
- BoW model requires: i) Vocabulary, ii) Measure of presence of words
- e.g. Vocabulary = {'to', 'be', 'or', 'not', 'question'} \newline
Document: \emph{to be or not to be} \newline
BoW representation: {to:2, be:2, or:1, not:1} $\rightarrow$ [1 1 1 1 0]
- Can also store counts
- Disregard grammar, word order -->

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
$$tf(term, doc) = \frac{count_{doc}(term)}{|doc|}$$
$$df(term) = \frac{|\{doc| term \in doc, doc \in D\}|}{|D|}$$ 
$$idf'(term) = \frac{|D|}{|\{doc| term \in doc, doc \in D\}|}, idf(term) = \log_2\bigg(\frac{|D|}{|\{doc| term \in doc, doc \in D\}|}\bigg)$$
$$tf-idf(term, doc) = tf(term, doc) \times idf(term)$$
\end{block}

. . .

\begin{block}{Augmented  TF}
$$tf'(term, doc) = 0.5 + 0.5 \cdot \frac{count_{doc}(term)}{ max_{term'} \{count_{doc}(term')\}}$$
\end{block}


::: notes
- Probability that i-th term occurs k times in the document: $p_{\lambda_i}(k)=e^{-\lambda_i}\frac{\lambda_i^k}{k!}$ ($\lambda_i$ parameter of the distribution)
- Expected value of occurence: $N \cdot E_i(k) = N\cdot \lambda_i = \text{collection frequency}_i$
- Term present at least once: $N \cdot (1-P_{\lambda_i}(0)) = \text{document frequency}_i$
:::

# Solution 3 (tf-idf)

- Solution: vector of tf-idf
- Ranking: Cosine similarity between query and document vectors
- Good metrics to determine the significance of a term in a document collection

. . .

> - Issue: still enormous vectors
> - Issue: `devil - Mephistopheles` are equally separate concepts as `devil - lasagne`
> - Issue: independent terms assumption

# Document Retrieval - Probabilistic Retrieval
- Goal: Find P[R|d,q]
- Ranking: Proportional to relevance odds \newline
$$O(R|d, q) = \frac{P[R|d, q]}{P[\bar R|d, q]}$$
- Different probabilistic models calculate these probabilities differently \newline
e.g. Binary Independence model, Poisson model, BM25 \newline

     For Poisson, $P[d|\lambda] = \prod_{t \in V} \frac{e^{- \lambda_t} \cdot \lambda^{d_t}_t}{d_t!}$

# Document Retrieval - Statistical Language Model

- Pretend the query was generated by a LM based on the document
- Ranking: Proportional to query likelihood
- $argmax_d\ p(d|q) = argmax_d\ \frac{p(q|d)\cdot p(d)}{p(q)} = argmax_d\ p(q|d)\cdot p(d)$ \newline
<!-- Likelihood that query was generated by LM estimated from document d -->
  $\approx argmax_d\ p_{LM}(q|d)\cdot p(d)$ \newline
  \qquad $p(d) \approx \frac{1}{|D|}$ or p(d) is query independent \newline
  $\approx argmax_d\ p_{LM}(q|d)$
- Unigram: $p(d|q) \approx \prod_i p_{LM}(q_i|d)$

. . .

- LMs can be smoothed, as you remember e.g. Interpolation, Dirichlet smoothing
- Jelinek-Mercer smoothing: $p(q_i|d,D) = \lambda \cdot p(q_i|d) + (1-\lambda) \cdot p(q_i|D)$ \newline
High $\lambda$: documents with all query words (conjunctive) \newline
Low $\lambda$: suitable for long queries (disjunctive)

. . .

- Issue: Without word embeddings, no word relatedness \newline 
    Query: **Goethe, devil** \newline
    A: Wolfgang's idea of the demon Mephistopheles who makes a bet with God <!-- no synonymy, polysemy -->
- Can we model word co-occurence for a topic?

::: notes
- Other smoothing schemas exist, like discounting, adding epsilon or linear interpolation between multiple LMs, including zerogram
- Other improvements, such as special grammar, prior knowledge of the document (length), list of synonyms, etc 
:::

# Solution 4 (Latent Semantic Analysis)

- Assumption: Documents are composed of $k$ latent topics.
- Solution: Perform dimensionality reduction $\rightarrow$ eigenvalues, singular value decomposition
- $A_{i,j} =$ #occurences of term $t_i$ in document $d_j$

||$d_1$|$d_2$|$d_3$|$d_4$|
|-|-|-|-|-|
|Wolfgang|1|1|0|0|
|Mephistopheles|1|0|0|0|
|Faust|0|1|0|0|
|Goethe|0|1|0|1|
|devil|0|1|1|0|
|demon|1|0|0|1|
|lasagne|0|0|1|0|
|German|0|1|0|1|

::: notes
The example uses counts, but for better representation of term importance in the document, one would use tf-idf.
:::

# Approximation of $A$

::: columns
:::: column
||$d_1$|$d_2$|$d_3$|$d_4$|
|-|-|-|-|-|
|Wolfgang|1|1|0|0|
|Mephistopheles|1|**1**|0|**1**|
|Faust|**1**|1|0|0|
|Goethe|**1**|1|0|**0**|
|devil|**1**|1|**0**|**1**|
|demon|1|**1**|0|1|
|lasagne|0|0|1|0|
|German|**1**|1|0|**0**|
::::
:::: column
||$c_1$|$c_2$|$c_3$|
|-|-|-|-|
|Wolfgang|1|0|0|
|Mephistopheles|0|1|0|
|Faust|1|0|0|
|Goethe|1|0|0|
|devil|0|1|0|
|demon|0|1|0|
|lasagne|0|0|1|
|German|1|0|0|
::::
:::

3 latent concepts:\newline
{Goethe (Wolfgang, Faust, German), devil (Mephistopheles, demon), lasagne} 

\centering
$d_1 = 1\times c_1 + 1\times c_2$

::: notes
Given $k$ concepts, we try to find such a matrix $A'$, that's as close to the original one, but with every document being a combination of $k$ independent vectors.
:::

# Approximation of $A$

> - Given: $A, k$
> - $A' = argmin_{A' \text{rank} k} ||A-A'||$
> - Distance e.g. Frobenius $(\sqrt{\sum_{i,j} a_{i,j}})$ 


# Singular Value Decomposition

\centering
![SVD for LSA](img/LSA_illustration.png){height=40%}

\raggedright
- $U =$ eigenvectors of $A^TA$ (# intersection of documents $d_i$ and $d_j$) <!--maps terms to topics-->
- $V =$ eigenvectors of $AA^T$ (# documents in which both terms $t_i$ and $t_j$ occur) <!--maps documents to topics-->
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
\end{block} -->

# SVD 

## Proof sketch

\begin{gather*}
A=USV^T, A^T = VSU^T, S \text{ diagonal} \\
U^T U = V V^T = I \text{ orthogonal} \\
A A^T U = U S^2 \rightarrow U \text{ eigenvectors of } A A^T, S \text{ root of eigenvalues} \\
(\forall i: A A^T U_{i,*} = U_{i,*} \cdot S^2_{i,i}) \\
A^T A V = V S^2 \rightarrow V \text{ eigenvectors of } A^T A, S \text{ root of eigenvalues} \\
(\forall i: A^T A V_{i,*} = V_{i,*} \cdot S^2_{i,i}) \\
\end{gather*}

# LSA

1. Order eigenvalues by descending values ($S_{i,i} > S_{i+1,i+1} \ge 0$) \newline 
   (proof next slide)
2. Take top-k eigenvectors + values (or all above threshold)
3. $A_K = U_K S_K V^T_K$ $[(m\times n), (n\times n), (n\times n)] \rightarrow [(m\times k), (k\times k), (k\times n)]$

. . .

- Term $\rightarrow$ latent representation: $U_k S_k$
- Document $\rightarrow$ latent representation: $(S_k V_k^T)^T = V_k S_k^T = V_k S_k$

::: notes
- We are free to permute the eigenvalues, so we can order them (together with the vectors) and also we know that the eigenvalues are non-negative 
- Therefore we can just take the top-k eigenvalues and replace the rest with zero.
- Essentially this crops the neighbouring matricies to first k columns and first k rows of V^T.
:::

# Properties of S

## Descending

\begin{gather*}
U' = U \text{ +swapped $i, j$ column}, S' = S \text{ +swapped $i, j$ values}, {V'}^T = V^T \text{ +swapped $i, j$ row} \\
U' = U \times C(i,j), S' = S \times C(i, j), {V'}^T = V^T \times R(i,j) \\
U' S' = (US) \text{ with swapped $i, j$ columns}, U'S' = (US)\times C(i,j) \\
U' S' {V'}^T = (US)\times C(i,j) \times V^T \times R(i,j) = (US)\times C(i,j) \times C(i, j) V^T = USV^T
\end{gather*}

. . .

## Non-negative

\begin{gather*}
A^T A \text{ is positive semidefinite} \Rightarrow S_{i,i} \ge 0 \\
\forall x \ne \overrightarrow{0}: x^T A^T A x = (Ax)^T(Ax) = ||Ax|| \ge 0
\end{gather*}

# LSA Concepts

- $U_k S_k$ maps terms to latent "concepts" $(m \rightarrow k)$
- $V_k S_k$ maps documents to "concepts" $(n \rightarrow k)$

::: notes
- The k then becomes obvious is the number of concepts
- We don't specify the concepts, they are determined by SVD
- From our point of view, they are latent
:::

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
> - Map query to our topic space: $q \rightarrow U_k^t \cdot q = q'$ = [0.355, -0.07]^T
> - Query-document match: dot product, cosine similarity:  $\frac{r_q \cdot r_d}{|r_q| \cdot |r_d|} = \frac{0.01205}{0.10879} \approx 0.11$

\note{
    - Whether that's a good match or not depends on the ranking and/or threshold
}

# LSA Graphics

![Term-document matrix, no ordering, $k=5$; Source [6]](img/visualization_0.png){height=80%}

# LSA Graphics

![Term-document matrix, group documents, $k=5$; Source [6]](img/visualization_1.png){height=80%}

# LSA Graphics

![Term-document matrix, group documents+terms, $k=5$; Source [6]](img/visualization_2.png){height=80%}

# LSA Code

```
from sklearn.decomposition import TruncatedSVD
from sklearn.feature_extraction.text import TfidfVectorizer

vectorizer = TfidfVectorizer(stop_words='english', 
    max_features= 1000,
    max_df = 0.5, 
    smooth_idf=True)
X = vectorizer.fit_transform(documents)

svd_model = TruncatedSVD(n_components=20)
svd_model.fit(X)
```

\centering
Compression: $m\times n \rightarrow m\times k + n\times k + k\times k$

::: notes
- max_features takes to top 1000 terms, max_df removes all words which appear in at least half the documents.
- smooth_idf adds one to ever seen term
- The reason it's called Truncated SVD is because it can be used for matrix compression. Instead of transmitting $m\times n$ matrix, we can just transmit the three separate matricies.
:::

<!-- # Notes

Fast SVD

> - Naive approach $det (A-\lambda I) = 0$ solving $n$-th order polynomial (variable $\lambda$)\newline
    Eigenvector Decomposition (EVD), get eigenvectors
> - Jacobi rotation [4, 5], Jacobi eigenvalue algorithm [7]: \newline
    Create almost a diagonal matrix (bidiagonal): $A = U B V$, $O(m n^2)$ \newline
    Compute SVD of $2\times 2$ matricis $O(n^2)$
> - Can be parallelized (ARPACK)

. . .

Latent Semantic Analysis

> - Also called LSI (Latent Semantic Indexing)

\note{
    - tf-idf is not a vital part of LSA, though works well

    TODO

    - Can be parallelized at the cost of a slightly less accurate approximation
} -->

# Considerations

Notes:

> - tf-idf is just a weighting scheme (tf, counts)
> - SVD naive approach $det (A-\lambda I) = 0$ solving $n$-th order polynomial (variable $\lambda$)\newline
    Eigenvector Decomposition (EVD), get eigenvectors
> - Faster, approximate methods available

. . . 

::: columns
:::: column
Pros:

- Easy to implement
- Explainable terms
- Quite fast runtime
- Handles synonymy of words
::::

:::: column
Cons:

- Only surface dependencies
- Determination of k <!--depends on the rank of the matrix, thresholding of descending singular values-->
- SVD difficult to update <!-- Consider adding a new document to this corpus -->
::::
:::

# Dense Vectors

- (Sentence)BERT (CLS): $D \cup Q \rightarrow \mathbb{R}^{768}$
- $h_q = BERT(\textit{Goethe devil})$ 
- $h_a = BERT(\textit{Wolfgang's idea of the demon Mephistopheles who makes a bet with God})$
- $h_c = BERT(\textit{Devilishly good lasagne})$
- $h_q \cdot h_a = 14.1, h_q \cdot h_c = 0.9$

- Used in industry (with better models than BERT)

# Resources

1. Python code: <https://medium.com/acing-ai/what-is-latent-semantic-analysis-lsa-4d3e2d18417a>
2. Comprehensive tutorial for LSA+SVD: <https://www.engr.uvic.ca/~seng474/svd.pdf>
3. SVD example: <http://web.mit.edu/be.400/www/SVD/Singular_Value_Decomposition.htm>
4. Computation: <https://en.wikipedia.org/wiki/Singular_value_decomposition#Calculating_the_SVD>
5. Computation: <https://www.cs.utexas.edu/users/inderjit/public_papers/HLA_SVD.pdf>
6. Visualization: <https://topicmodels.west.uni-koblenz.de/ckling/tmt/svd_ap.html>
7. Computation: <https://en.wikipedia.org/wiki/Jacobi_eigenvalue_algorithm>
8. Python code: <https://www.analyticsvidhya.com/blog/2018/10/stepwise-guide-topic-modeling-latent-semantic-analysis/>
9. Jelinek-Mercer: <http://ctp.di.fct.unl.pt/~jmag/ir/slides/a05%20Language%20models.pdf>
10. LSI: <https://nlp.stanford.edu/IR-book/html/htmledition/latent-semantic-indexing-1.html>
