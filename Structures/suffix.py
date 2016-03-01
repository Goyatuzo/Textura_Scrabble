class Suffix:
    def __init__(self, words):
        self.data = []

        # Add all words reversed for suffix.
        for word in words:
            self.data.append(word[::-1])

    def get_words_simple(self, suffix):
        """Given an input suffix string, return the list of words that end with
        the letter sequence."
        :param suffix: The prefix of the word."""
        results = []

        # Reverse the letters since it's stored reverse in data.
        suffix = suffix[::-1]

        for word in self.data:
            if word.startswith(suffix):
                results.append(word[::-1])

        return results

    def __getitem__(self, item):
        # Check if the input is a string.
        if isinstance(item, str):
            return self.get_words_simple(item)

        # If the input isn't a string, raise error.
        raise ValueError("Only a string can go in the [] operator for Suffix.")
