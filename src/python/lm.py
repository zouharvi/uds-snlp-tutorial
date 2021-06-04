from collections import Counter
import numpy as np
from typing import List, Tuple


class NGramLM:
    def __init__(self, train_tokens: List[str], test_tokens: List[str], N: int, alpha: float, epsilon=1.e-10):
        self.N = N
        self.aplha = alpha
        self.epsilon = epsilon
        self.train_counts = [Counter(self.get_n_grams(train_tokens, n)) for n in range(1,N+1)]
        self.test_tokens = test_tokens
        V = set(self.train_counts[0].keys())
        V = V.union([(test_token,) for test_token in test_tokens])
        self.V = V
        self._test_histories()

    def get_n_grams(self, tokens: List[str], n: int) -> List[Tuple[str]]:
        tokens_circular = tokens + tokens[:n-1] # circular n-grams
        n_grams = []
        for i in range(0, len(tokens_circular)-n+1):
            n_gram = tuple(tokens_circular[i:i+n])
            n_grams.append(n_gram)
        return n_grams

    def get_n_gram_count(self, n_gram: Tuple[str]) -> int:
        return self.train_counts[self.N-1][n_gram]

    def get_history_count(self, history: Tuple[str]) -> int:
        if len(history) == 0:
            return sum(self.train_counts[0].values())
        return self.train_counts[self.N-2][history]

    def get_smoothed_prob(self, n_gram: Tuple[str]) -> float:
        history = n_gram[:self.N-1]
        return (self.get_n_gram_count(n_gram) + self.aplha)/(self.get_history_count(history) + self.aplha*len(self.V))

    def perplexity(self):
        test_n_grams = self.get_n_grams(self.test_tokens, self.N)
        rel_freqs = {test_n_gram: count/len(test_n_grams) for test_n_gram, count in Counter(test_n_grams).items()}
        assert np.abs(1-sum(rel_freqs.values())) < self.epsilon, "Relative frequencies don't some up to 1!" 
        H = -1 * sum([rel_freq * np.log2(self.get_smoothed_prob(test_n_gram)) for test_n_gram, rel_freq in rel_freqs.items()])
        return 2**H

    def _test_histories(self):
        histories = [["I"], ["not"], ["I", "am"], ["not", "a"], ["not", "a", "man"], ["also", "not", "a"]]
        for history in histories:
            if len(history) == self.N-1:
                S = sum([self.get_smoothed_prob(tuple(history)+v) for v in self.V])
                assert np.abs(1-S) <= self.epsilon, "Conditional probabilities don't sum up to 1 for history {}".format(history)
                print("Checked probabilities for history {}".format(history))


if __name__ == "__main__":
    train_tokens = ["I", "am", "a", "man", "not", "a", "mouse", "and", "also", "not", "a", "dog"]
    test_tokens = ["I", "am", "a", "cow", "not", "a", "horse"]

    for n in range(1,4):
        LM = NGramLM(train_tokens, test_tokens, N=n, alpha=0.01)
        pp = LM.perplexity()
        print(pp)
