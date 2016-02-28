class Prefix:
    def __init__(self, words=None):
        if words is not None:
            self.raw = words
        else:
            self.raw = []

    def add(self, word):
        """Add a word to the Words data structure.
        :param word: The word to be added to the data structure."""

        self.raw.append(word.strip())
        self.raw.sort()

    def get_words_simple(self, prefix):
        """Given an input prefix string, return the list of words that begin
        with prefix.
        :param prefix: The prefix of the word."""
        results = []

        for word in self.raw:
            if word.startswith(prefix):
                results.append(word)

        return results

    def __getitem__(self, item):
        # Check if the input is a string.
        if isinstance(item, str):
            return self.get_words_simple(item)

        # If the input isn't a string, raise error.
        raise ValueError("Only a string can go in the [] operator for Prefix.")