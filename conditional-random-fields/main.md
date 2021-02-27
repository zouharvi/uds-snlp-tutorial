---
title:
- Conditional Random Fields
subtitle: |
    | (SNLP tutorial)
author:
- Vilém Zouhar
theme:
- Boadilla
date: \today
aspectratio: 169
header-includes:
  - \AtBeginDocument{\usepackage{tikz}\usetikzlibrary{positioning,shapes,arrows}}

documentclass: beamer
# classoption: notes
---

# Overview

- Sequence Labelling / Entity Recognition
- - Rule-based
- - HMM
- - Bayesian Network
- - Log-linear 1st Order Sequential Model
- - Linear Chain CRF / CRF
- Model comparison
- Code
- Homework

::: notes
- This part is mostly about sequence labeling and the different approaches which end with conditional random fields.
:::

# Sequence Labelling / Entity Recognition

> - `My name is V. Zouhar, I live in Saarbrücken and my matriculation number is 1234.`
> - `My name is [V. Zouhar:person], I live in [Saarbrücken:loc] and my matriculation number is [1234:mat-num].`
> - NER as Sequence labeling: \newline
    $X$: sequence of words \newline
    $Y$: labels `{mat-num, person, location, none}`

::: notes
- NER can be reformulated as sequence labeling, which includes also e.g. part of speech tagging
- Given a sentence we want to classify every token.
:::

# Rule-based

> - Regex substitute:\newline
    `matriculation (number)? (is)? (\d+)` $\rightarrow$ `[\3:mat-num]`
> - Gets out of hand quickly:\newline
    `(am|name (is)?) (.*?) (and|\s[.,?])?` $\rightarrow$ `[\3:person]`
> - No automated learning

::: notes
- The most straightforward solution just uses regex substitution, but that becomes very complex very soon and is also not performant enough, because it does not learn from the data.
- The only advantage is that we know explicitly which rules get applied.
- Still bad in general.
:::

# HMM

> - Hidden states: `{mat-num, person, location, none}`
> - Better hidden states: `{mat-num, START+person, INTERNAL+person, END+person, location, none, ...}`
> - Transitions: MLE from annotated data
> - Emission probabilities: MLE from annotated data (+ smoothing)
> - $p(x,y) = \prod_i a(y_{i-1}, y_{i}) \cdot o(y_i, x_i)$
> - Optimizes $argmax\ p(x, y |\theta)$, though we are interested in $argmax\ p(y|x,\theta)$

::: notes
- HMMs seem a better fit for this task, since it captures transition probabilities between latent variables and emission probabilities.
- The probability of the sequence is computed as the product of transitions and observations.
- The probabilities can be estimated using MLE counting + some smoothing
- Side note, HMM is a generative model, because it can model the joint distribution p(y,x)
- In case we don't have annnotated data, we may still make use of HMMs by employing the Baum-Welsch algorithm.
- The emission probabilities are just distributions over all observable variables and every latent variable gets a unique one. For example in POS tagging, it may be the partial counts, but in speech processing, it's gaussian mixture.
- We usually require supervised examples to do this MLE counting, but the Baum-Welsch is able to estimate all these probabilities even if we don't know the latent labels.
- The reason for low performance is that the emission probabilities capture only features that dependent only on the current state and we have little control over the features.
:::

# Bayesian Network

- DAG, $(x\rightarrow y) \in E:$ $y$ dependent on $x$

::: frame
## Local Markov Property
Node is conditionally independent of its nondescendants given its parents.\newline
$p(\text{Sprinkler}|\text{Cloudy},\text{Rain}) =p(\text{Sprinkler}|\text{Cloudy})$
:::

\centering
\begin{tikzpicture}[
  node distance=0.5cm and 0cm,
  mynode/.style={draw,ellipse,text width=1.7cm,align=center},
  observed/.style={draw,rectangle,text width=1.7cm,align=center}
]
\node[mynode] at (2, 2) (cl) {Cloudy};
\node[mynode] at (0, 1) (sp) {Sprinkler};
\node[mynode] at (4, 1) (ra) {Rain};
\node[observed] at (2, 0) (gw) {Grass wet};
\path
(cl) edge[-latex] (sp)
(cl) edge[-latex] (ra)
(ra) edge[-latex] (gw) 
(sp) edge[-latex] (gw);
\end{tikzpicture}

::: notes
- Has to be DAG, otherwise cycles
- It models dependence between variables which can be either latent or observed
- We use it to reason about events of which we know the observed values and we want to know the cause
- From the graph we may for example find out, that it makes no sense to condition _Sprinkler_ on _Rain_, because these two variables are independent. It would however be an approximation if we treated _Cloudy_ independent of _Grass wet_.
:::

# Naïve Bayes

- Assume absolute independence except for the one observed variable
- $p(y=\text{Mild}|x) = p(y_j|x) = \frac{p(x|y_j)p(y_j)}{p(x)} \propto p(x|y_j) p(y_j) \approx p(y_j) \prod_i p(x_i|y_j)$

\centering
\begin{tikzpicture}[
  node distance=0.5cm and 0cm,
  mynode/.style={draw,ellipse,text width=1.7cm,align=center},
  observed/.style={draw,rectangle,text width=1.7cm,align=center}
]
\node[mynode] at (-3, 1.3) (clf) {Forecast};
\node[mynode] at (0, 1.3) (cl) {Cloudy};
\node[mynode] at (3, 1.3) (ra) {Sprinkler};
\node[mynode] at (6, 1.3) (gw) {Grass wet};
\node[mynode] at (9, 1.3) (cs) {Car splash};
\node[observed] at (3, 0) (sp) {Rain \{N,M,H\}};
\path
(sp) edge[latex-] (clf)
(sp) edge[latex-] (cl)
(sp) edge[latex-] (ra)
(sp) edge[latex-] (gw)
(sp) edge[latex-] (cs);
\end{tikzpicture}

::: notes
- In Naïve Bayes we artificially flatten the network so that the observed variable is directly dependent to all causes and there are no other dependencies.
- The formula shows where the approximation is taking place.
- A practical example why this is naïve is that the variable _Cloudy_ is heavily dependent on the _Forecast_ variable. And if we put both there in the formula, then we give one "cause" double to power.
- Labels: None, Mild, Heavy
:::

# HMM

\centering
\begin{tikzpicture}[
  node distance=0.5cm and 0cm,
  mynode/.style={draw,ellipse,text width=1.5cm,align=center},
  observed/.style={draw,rectangle,text width=1.5cm,align=center}
]
\node[mynode] at (-3, 2) (y0) {Start};
\node[mynode] at (0, 2) (y1) {Weather};
\node[observed] at (0, 0) (x1) {X1 0.9 Walk};
\node[mynode] at (3, 2) (y2) {Weather};
\node[observed] at (3, 0) (x2) {X2 0.0 Walk};
\node[mynode] at (6, 2) (y3) {Weather};
\node[observed] at (6, 0) (x3) {X3 0.1 Walk};
\path
(y0) edge[-latex] (y1)
(y1) edge[-latex] (x1)
(y1) edge[-latex] (y2)
(y2) edge[-latex] (x2)
(y2) edge[-latex] (y3)
(y3) edge[-latex] (x3);
\end{tikzpicture}

\raggedright

Sketch of HMM structure\newline
observed variable _Walk duration_, latent variable: _Weather_ $\in$ \{_Sunny_, _Cloudy_\}

. . .

\centering

\begin{gather*}
p(y|x) = \prod_i p(y_i) \cdot o(y_i, x_i) \text{ (Naïve Bayes)}\\
\Rightarrow \\
p(y|x) = \prod_i a(y_{i-1}, y_{i}) \cdot o(y_i, x_i) \text{ (HMM)}
\end{gather*}

::: notes
- From bayesian network point of view, HMMs model a structure in which latent variable is connected to another one, which in turn is connected to observed ones.
- These relationships are explicitly modeled by the transition (horizontal) and emission (vertical) functions.
:::

# Logistic Regression

\centering 
$p(y|x) = \frac{\exp(\Phi(y,x))}{\sum_{y'} \exp(\Phi(y',x))}$

$\arg \max_y \frac{\exp(\Phi(y,x))}{\sum_{y'} \exp(\Phi(y',x))}$

::: notes
- Another approach is to assign a score to every sequence and then pick the best one.
- So Phi in this case would just score every possible sequence and by doing softmax we get a conditional probability
:::

# Log-linear 1st Order Sequential Model

> - Sequence of hidden states: $y$, `{mat-num, person, location, none}`
> - Observed sequence of variables: $x$ (words)
> - $p(y|x) \propto \exp \big\{\sum_j \log a(y_{j-1}, y_{j}) + \log o(y_j, x_j)\}$
> - $p(y|x) = \frac{1}{Z(x)} \cdot \exp \big\{\sum_j \log a(y_{j-1}, y_{j}) + \log o(y_j, x_j)\}$
> - $p(y|x) = \frac{1}{Z(x)} \cdot \prod_j  \{ a(y_{j-1}, y_{j}) o(y_j, x_j)\}$
> - $argmax\ p(y|x) \ldots$ 

::: notes
- Looks like logistic regression.
- This has exactly the same number of parameters but they all model $p(y|x)$ and not $p(x,y)$. This is more ideal for us.
:::

# Log-linear 1st Order Sequential Model

Viterbi:

\vspace{-0.4cm}
\begin{align*}
& argmax\ p(y|x) = argmax\ \log p(y|x) = argmax\ F(y,x) - \log \sum_{y'} \exp F(y', x) \\
& = argmax\ F(y,x) \\
& \alpha_t(y_j) = \max_i \exp \bigg( \log \alpha_{t-1}(y_i) + a(y_j, y_i) + o(y_j, x_t) \bigg) \\
& \alpha'_t(y_j) = argmax_i\ \alpha_{t-1}(y_i) + \exp \big( a(y_j, y_i) + o(y_j, x_t) \big)
\end{align*}

$O(|Y|^2\cdot T)$

::: notes
- First we may be interested in just the argmax, for which we need to store the pointers (Viterbi algorithm)
- Build trellis.
:::

# Log-linear 1st Order Sequential Model

Forward:

\vspace{-0.4cm}
\begin{align*}
& \log fw_t(y_j) = \log \sum_i\ \exp \bigg( \log fw_{t-1}(y_i) + a(y_j, y_i) + o(y_j, x_t) \bigg) \\
& Z(X) = \sum_i \exp \bigg( \log fw_{|T|-1}(y_i) + a(y_j, y_i) + o(y_j, x_t) \bigg) \\
& \rightarrow \\
& p(y|x) = \frac{\alpha_{|T|}(y_{:-1}) }{Z(x)}
\end{align*}

$O(|Y|^2\cdot T)$

::: notes
- To compute the full conditional probability, we also need the partition function, which we can compute using the forward algorithm.
- Finally, we have the argmax as well as the conditional probability.
- This can also be done using matrix methods TODO
:::

# Log-linear 1st Order Sequential Model

> - Replace $o(y_j, x_t)$ with $\theta_1 h_1(y_j, x_t) + \theta_2 h_2(y_j, x_t) + \ldots$
> - Same with $a(y_j, y_i) = \theta'_1 g_1(y_j, y_i) + \theta'_2 g_2(y_j, y_i) + \ldots$ 
> - Why not just $\sum_{\text{feature } f} \theta_i f_i(y_i, y_j, x_t)$ ?
> - Why not allow $\sum_{\text{feature } f} \theta_i f_i(y_i, y_j, x, t)$ ?

::: notes
- $o$ can be any scoring function, does not need to be a distribution like with HMMs
- It can be a sum of other feature functions.
- In fact, this can be generalized even further
- And finally, there is no reason to not allow features to observe the whole sequence, because neither Viterbi nor Forward decoding limits this.
:::

# Model overview

![CRF in relation to other models; Source [2]](img/model_overview.png){width=80%}

::: notes
- There is a system of models with different properties.
- First, there is naive bayes and the conditional version, multinomial logistic regression.
- These model single class predictions. While naive bayes does this generatively, logistic regression uses the scoring mechanism.
- On sequences, we can either have the HMMs or a conditional version, which are linear chain CRFs.
- Finally there are models for which there is no clear correspondence between a latent variable and a single observed one.
:::

# HMM $\rightarrow$ Linear Chain CRF

![HMM vs. Linear Chain CRF; Source [12]](img/hmm_to_crf.png){width=40%}

# Model overview

- Multinomial logistic regression: \newline
    $p(y_j|x) = \frac{exp(Z_j\cdot x)}{\sum_i exp(Z_i\cdot x)}$
- Multiclass naïve Bayes: \newline
    $p(y_j|x) = \frac{p(x|y_j)p(y_j)}{p(x)} \propto p(x|y_j) p(y_j) \approx p(y_j) \prod_i p(x_i|y_j)$

::: notes
- Bayes splits input features. 
- Why generative? p(x|y_j) is the generative part, while p(y_j|x) is discriminative.
:::

# Linear Chain CRF

- Sequence of hidden states: $y$, `{mat-num, person, location, none}`
- Observed sequence of variables: $x$ (words)
- $p(y|x) \propto \prod_t \exp \big\{\sum_{\text{feature } f} \theta_i f_i(y_{t-1}, y_t, x, t) \big\}$
- $p(y|x) = \frac{1}{Z(x)}\prod_t \exp \big\{\sum_{\text{feature } f_i} \theta_i f_i(y_{t-1}, y_t, x, t) \big\}$
- Features: $f_i(y_{t-1}, y_t, x, t) \rightarrow \mathbb{R}$
- Parameters: $\theta$

::: notes
- From the formulation we can see that it's again a discriminative model.
- The right side is not a probability, but rather a score, so we need to normalize it.
- Z, is the partition function for normalization (just like in softmax)
:::

# Linear Chain CRF - Features

\begin{align*}
& f_i(y_{t-1}, y_t, x, t) =
\begin{cases}
    1 \qquad \text{if } \text{cond}_f (y_{t-1}, y_t, x, t) \\
    0 \qquad \text{else}
\end{cases}
\end{align*}

. . .

\begin{align*}
& f_1(y_{t-1}, y_t, x, t) =
\begin{cases}
    1 \qquad \text{if } x_{t-2} \text{ is capitalized} \\
    0 \qquad \text{else}
\end{cases} \\
& f_a(y_{t-1}, y_t, x, t) =
\begin{cases}
    1 \qquad \text{if } x_{t-1} = y_{t-1} = \texttt{number} \wedge y_t = \texttt{none} \\
    0 \qquad \text{else}
\end{cases} \\
& \qquad \qquad \qquad \qquad \theta_a = a(\text{number}, \texttt{none}) \\
& f_o(y_{t-1}, y_t, x, t) =
\begin{cases}
    1 \qquad \text{if } x_{t-1} = y_{t} = \texttt{number} \wedge x_t = \texttt{<num>} \\
    0 \qquad \text{else}
\end{cases} \\
& \qquad \qquad \qquad \qquad  \theta_o = o(\text{number}, \texttt{<num>})
\end{align*}

::: notes
- The feature functions here are indicators, that produce 1 in case of some conditions.
- These conditions have access to the current and the last latent variable, but also to all observed variables and the current position.
- This way we can emulate the log-linear 1st order sequential model by using these indicator functions and setting the corresponding variables.
- The theta parameters are learnable from the data.
:::

# Linear Chain CRF - Features

\begin{align*}
& f_w(y_{t-1}, y_t, x, t) = x_t \text{ word length} \\
& f_s(y_{t-1}, y_t, x, t) = x_t \text{ number of non-alphabetic characters}
\end{align*}

::: notes
- The features do not necessarily have to be indicators, in the second case here the whole sentence is processed into a single vector by an LSTM and the final hidden state multiplied by a single dense layer.
- In CRFs it is common to have an order of thousands features
:::

# CRF - Operations

Inference:
\vspace{-0.6cm}
\begin{gather*}
argmax_y\ p(y|x,\theta)
\end{gather*}

. . .

Decoding:
\vspace{-0.6cm}
\begin{gather*}
p(y|x,\theta)
\end{gather*}

. . .

Training:
\vspace{-0.6cm}
\begin{gather*}
argmax_{\theta}\ p(y_{D}|x_{D},\theta)
\end{gather*}

::: notes
- Inference - viterbi
- Decoding - forward
- Training - gradient methods
:::

# Linear Chain CRF - Estimating $\theta$

Gradient descent (ascent):

$$\frac{\partial \log p(y|x, \theta)}{\partial \theta_i} = \sum_{t=1}^T f_i(y_{t-1}, y_t, x, t) - \sum_{y'} \sum_{t=1}^T f_i(y'_{t-1}, y'_t, x, t) \cdot p (y'|x)$$

$$\theta_f \leftarrow \theta_f + \epsilon \Bigg[ \sum_{t=1}^T F(y_{t-1}, y_t, x, t) - \sum_{y'} \sum_{t=1}^T F(y'_{t-1}, y'_t, x, t) \cdot p (y'|x, \theta) \Bigg]$$

. . .

Limited-memory BFGS (quasi-Newton method)

::: notes
- As for the parameter estimation, there exists a solution, since the function is concave (negative is convex).
- It can be reached iteratively as no closed-form exists
- Note that we are adding the gradient, that's because we want to maximize the objective function.

- For the actual optimization, limited memory approximation of BFGS (Broyden–Fletcher–Goldfarb–Shanno) algorithm is used.
- It's a quasi Newtonian method, which means that it makes local approximation with the second term of the taylor expansion
- And for that it approximates the inverse of the hessian matrix
:::

# Linear Chain CRF - Regularization

Objective function:

$\mathcal{L} = \sum_{s} \log p(y^{(s)}|x^{(s)},\theta)$ 

. . .

LASSO:

$\mathcal{L}_{+lasso} = \sum_{s} \log p(y^{(s)}|x^{(s)},\theta) - \lambda_1 \sum_i |\theta_i|$

. . .

Ridge:

$\mathcal{L}_{+ridge} = \sum_{s} \log p(y^{(s)}|x^{(s)},\theta) - \frac{\lambda_2}{2} \sum_i \theta_i^2$

. . .

Elastic net:

$\mathcal{L}_{+elastic} = \sum_{s} \log p(y^{(s)}|x^{(s)}\theta) - \frac{\lambda_2}{2} \sum_i \theta_i^2  - \lambda_1 \sum_i |\theta_i|$

# General CRF

- Factorization to maximal clicques.
- Allow access to a whole clicque

::: columns
:::: column
## Clique
$G = (V, E) \quad C \subseteq V: \forall x,y \in C: (x,y) \in E$

## CRF
$p(Y|X) = \frac{1}{Z(X)} \prod_{C\in Y} \Psi_C(X_C)$\newline
$\Psi_C(Y, X) \sum_i \theta_i f_i(Y_{i-1}, Y_i, X, i)\ge 0$

::::

:::: column
::::: frame
## Maximal Clique
$C \subseteq C' \Rightarrow C = C'$
:::::

![Linear Chain CRF [2]](img/linear_crf.png){width=40%}
::::
:::

::: notes
- We may generalize CRFs to allow access to more data in the feature functions
- This requires the graph to be factorized into maximal clicques on which we define the potential function 
- Linear Chain CRFs fulfill these requirements, because they form a chain of latent variables, so maximal cliques are single nodes
- Explain cliques
- There is just a single decomposition into maximal clicque and it creates a factorization of the whole graph
:::

# Code

```
from sklearn_crfsuite import CRF

X_train = [
    [word2features(s, i) for i in range(len(s))]
    for s in train_sents]
y_train = [
    [label for token, postag, label in s]
    for s in train_sents]

crf = sklearn_crfsuite.CRF(
    algorithm='lbfgs',
    c1=0.1, c2=0.1,
    max_iterations=100,
)
crf.fit(X_train, y_train)
```

::: notes
c1 = lambda1, c2 = lambda2
:::

# Notes

Feature selection:

1. Start with all features.
2. a. If there exists a feature removing which worsens the performance by $< t$, remove it. Repeat 2.
2. b. If not, exit.

. . .

1. Start with no features.
2. a. If there exists a feature adding which improves the performance by $> t$, add it. Repeat 2.
2. b. If not, exit.

. . . 

Properties

- Hard to setup & train
- Fast inference

::: notes
- In practice, one may also wish to use just a limited number of features.
- When adding, it is possible to consider also combining with existing ones. Especially for indicator features, it is possible to combine them using boolean operators. 
- This can also be done in reverse - remove least useful features.
:::

# Homework

TBD

# Resources

1. Overview: <https://www.analyticsvidhya.com/blog/2018/08/nlp-guide-conditional-random-fields-text-classification>
2. Very detailed: <http://homepages.inf.ed.ac.uk/csutton/publications/crftut-fnt.pdf>
3. NER using CRF: <https://medium.com/data-science-in-your-pocket/named-entity-recognition-ner-using-conditional-random-fields-in-nlp-3660df22e95c>
4. Forward-backward for CRF: <https://www.cs.cornell.edu/courses/cs5740/2016sp/resources/collins_fb.pdf>
5. Academic-level introduction to CRF: <https://www.youtube.com/watch?v=7L0MKKfqe98>
6. Generalized CRF: <https://people.cs.umass.edu/~wallach/technical_reports/wallach04conditional.pdf>
7. Accessible introduction: <http://pages.cs.wisc.edu/~jerryzhu/cs769/CRF.pdf>
8. Python code: <https://sklearn-crfsuite.readthedocs.io/en/latest/tutorial.html#let-s-use-conll-2002-data-to-build-a-ner-system>

# Resources

9. Fast Linear Chain CRFs (C): <http://www.chokkan.org/software/crfsuite/>
10. Fast Linear Chain CRFs (C++): <https://taku910.github.io/crfpp/>
11. Bayesian Networks: <https://www.ics.uci.edu/~rickl/courses/cs-171/0-ihler-2016-fq/Lectures/Ihler-final/09b-BayesNet.pdf>
12. Naïve Bayes to HMM to CRF: <http://cnyah.com/2017/08/26/from-naive-bayes-to-linear-chain-CRF/>