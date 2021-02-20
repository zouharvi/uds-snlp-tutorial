---
title:
- Conditional Random Fields
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

- Text Classification / Entity Recognition
- Rule-based
- HMM
- Log-linear 1st Order Sequential Model
- CRF

# Text Classification / Entity Recognition

> - `My name is V. Zouhar, I live in Saarbrücken and my ticket number is 10110.`
> - `My name is [V. Zouhar:person], I live in [Saarbrücken:loc] and my ticket number is [10110:ticket-num].`
> - NER as Sequence labeling: \newline
    $X$: sequence of words \newline
    $Y$: labels `{ticket-num, person, location, none}`

\note{
    - NER can be reformulated as sequence labeling, which includes also e.g. part of speech tagging
}

# Rule-based

> - Regex substitute: `ticket (number)? (is)? (\d+)` $\rightarrow$ `[\3:ticket-num]`
> - Gets out of hand quickly: `(am|name (is)?) (.*?) (and|\s[.,?])?` $\rightarrow$ `[\3:person]`
> - No automated learning

# HMM

> - Hidden states: `{ticket-num, person, location, none}`
> - Better hidden states: `{ticket-num, START+person, INTERNAL+person, END+person, location, none, ...}`
> - Transitions: MLE from annotated data
> - Emission probabilities: MLE from annotated data (+ smoothing)
> - Not performant enough
> - Optimizes $argmax p(x, y |\theta)$, though we are interested in $argmax p(y|x,\theta)$

\note{
    - The reason for low performance is that the emission probabilities capture only features that dependent only on the current state
    - Side note, HMM is a generative model, because it can model the joint distribution p(y,x)
    - In case we don't have annnotated data, we may still make use of HMMs by employing the Baum-Welsch algorithm.
    - The emission probabilities are just distributions over all observable variables and every latent variable gets a unique one. For example in POS tagging, it may be the partial counts, but in speech processing, it's gaussian mixture. The Baum-Welsch is able to estimate all these probabilities even if we don't know the latent labels.
}

# Log-linear 1st Order Sequential Model

Define just two features (loosened feature restriction):

> - Sequence of hidden states: $y$, `{ticket-num, person, location, none}`
> - Observed sequence of variables: $x$ (words)
> - $p(y|x) \propto \exp \big\{\sum_j a(y_{j-1}, y_{j}) + o(y_j, x_j)\}$
> - $p(y|x) = \frac{1}{Z(x)} \cdot  \exp \big\{\sum_j a(y_{j-1}, y_{j}) + o(y_j, x_j)\}$
> - $argmax p(y|x) \ldots$ 

\note{
    - Looks like logistic regression.
    - This has exactly the same number of parameters but they all model $p(y|x)$ and not $p(x,y)$. This is more ideal for us.
}

# Log-linear 1st Order Sequential Model

Viterbi:

\vspace{-0.4cm}
\begin{align*}
& argmax\ p(y|x) = argmax\ \log p(y|x) = argmax\ F(y,x) - \log \sum_{y'} \exp F(y', x) \\
& = argmax\ F(y,x) \\
& \alpha_t(y_j) = \max_i \exp \bigg( \log \alpha_{t-1}(y_i) + a(y_j, y_i) + o(y_j, x_t) \bigg) \\
& \alpha'_t(y_j) = argmax_i\ \alpha_{t-1}(y_i) + \exp \big( a(y_j, y_i) + o(y_j, x_t) \big)
\end{align*}


\note{
    - First we may be interested in just the argmax, for which we need to store the pointers (Viterbi algorithm)
}

# Log-linear 1st Order Sequential Model

Forward:

\vspace{-0.4cm}
\begin{align*}
& \log fw_t(y_j) = \log \sum_i\ \exp \bigg( \log fw_{t-1}(y_i) + a(y_j, y_i) + o(y_j, x_t) \bigg) \\
& Z(X) = \sum_i \exp \bigg( \log fw_{|T|-1}(y_i) + a(y_j, y_i) + o(y_j, x_t) \bigg) \\
& \rightarrow \\
& p(y|x) = \frac{\alpha_{|T|}(y_{:-1}) }{Z(x)}
\end{align*}

\note{
    - To compute the full conditional probability, we also need the partition function, which we can compute using the forward algorithm.
    - Finally, we have the argmax as well as the conditional probability.
}

# Log-linear 1st Order Sequential Model

> - Replace $o(y_j, x_t)$ with $\theta_1 h_1(y_j, x_t) + \theta_2 h_2(y_j, x_t) + \ldots$
> - Same with $a(y_j, y_i) = \theta'_1 g_1(y_j, y_i) + \theta'_2 g_2(y_j, y_i) + \ldots$ 
> - Why not just $\sum_{\text{feature } f} \theta_i f_i(y_i, y_j, x_t)$ ?
> - Why not allow $\sum_{\text{feature } f} \theta_i f_i(y_i, y_j, x, t)$ ?

\note{
    - $o$ can be any scoring function, does not need to be a distributionlike with HMMs
    - It can be a sum of other feature functions.
    - In fact, this can be generalized even further
    - And finally, there is no reason to not allow features to observe the whole sequence
}

# CRF

- Sequence of hidden states: $y$, `{ticket-num, person, location, none}`
- Observed sequence of variables: $x$ (words)
- $p(y|x) \propto \prod_t \exp \big\{\sum_{\text{feature } f} \theta_i f_i(y_{t-1}, y_t, x, t) \big\}$
- $p(y|x) = \frac{1}{Z(x)}\prod_t \exp \big\{\sum_{\text{feature } f_i} \theta_i f_i(y_{t-1}, y_t, x, t) \big\}$
- Features: $f_i(y_{t-1}, y_t, x, t) \rightarrow \mathbb{R}$

\note{
    - From the formulation we can see that it's again a discriminative model.
    - The right side is not a probability, but rather a score, so we need to normalize it.
    - Z, is the partition function for normalization (just like in softmax)
}

# CRF indicator features

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
    1 \qquad \text{if } x_{t-1} = \texttt{number} \wedge x_{t} = \texttt{is} \wedge y_t = \texttt{none} \\
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

\note{
    - The feature functions here are indicators, that produce 1 in case of some conditions.
    - These conditions have access to the current and the last latent variable, but also to all observed variables and the current position.
    - This was we can emulate the log-linear 1st order sequential model by using these indicator functions and setting the corresponding variables.
}

# CRF features

\begin{align*}
& f_w(y_{t-1}, y_t, x, t) = x_t \text{ word length} \\
& f_e(y_{t-1}, y_t, x, t) = LSTM(x) W_{y_t} \qquad W_* \in \mathbb{R}^{n \times 1} \\
\end{align*}

\note{
    - The features do not necessarily have to be indicators, in the second case here the whole sentence is processed into a single vector by an LSTM and the final hidden state multiplied by a single dense layer.
    - In CRFs it is common to have an order of thousands features
}

# CRF - Estimating $\theta$


Gradient descent:

$$\frac{\partial \log p_\theta(y|x)}{\partial \theta_i} = \sum_{t=1}^T f_i(y_{t-1}, y_t, x, t) - \sum_{y'} \sum_{t=1}^T f_i(y'_{t-1}, y'_t, x, t) \cdot p (y'|x)$$

$$\theta_f \leftarrow \theta_f + \epsilon \Bigg[ \sum_{t=1}^T f(y_{t-1}, y_t, x, t) - \sum_{y'} \sum_{t=1}^T f(y'_{t-1}, y'_t, x, t) \cdot p_\theta (y'|x) \Bigg]$$

\note{
    - As for the parameter estimation, there exists a solution, since the function is convex
    - It can be reached iteratively as no closed-form exists
}

# Notes

> - Markov Random Fields - more than two latent variables in feature function
> - Feature selection \newline
    1. Start with no features. \newline  
    2a. If there exists a feature that improves the performance by $> t$, add it. Repeat 2. \newline
    2b. If not, exit.
      

\note{
    - CRF is a specific case of Markov Random Fields, which requires more theory regarding graph based probability model. In general, it allows the feature functions to access latent variables beyond the current and the last one. It is based on the 
    - In practice, one may also wish to use just a limited number of features.
    - When adding, it is possible to consider also combining with existing ones. Especially for indicator features, it is possible to combine them using boolean operators. 
    - This can also be done in reverse - remove least useful features.
}

# Resources

1. Overview: <https://www.analyticsvidhya.com/blog/2018/08/nlp-guide-conditional-random-fields-text-classification>
2. Very detailed: <http://homepages.inf.ed.ac.uk/csutton/publications/crftut-fnt.pdf>
3. NER using CRF: <https://medium.com/data-science-in-your-pocket/named-entity-recognition-ner-using-conditional-random-fields-in-nlp-3660df22e95c>
4. Forward-backward for CRF: <https://www.cs.cornell.edu/courses/cs5740/2016sp/resources/collins_fb.pdf>
5. Academic-level introduction to CRF: <https://www.youtube.com/watch?v=7L0MKKfqe98>
6. Generalized CRF: <https://people.cs.umass.edu/~wallach/technical_reports/wallach04conditional.pdf>
7. Accessible introduction: <http://pages.cs.wisc.edu/~jerryzhu/cs769/CRF.pdf>