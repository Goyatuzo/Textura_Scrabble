class Words:

    def __init__(self, words):
        self.data = words

    def find_letters(self, letters):
        """Given a Words data structure, input a string of letters
        and find the words that contain any one of the letters.
        :param letters: String of letters to query list of words."""
        results = []

        letters = set(letters)

        for word in self.data:
            if any((c in letters) for c in word):
                results.append(word)

        return results

    def __getitem__(self, item):
        # Confirm that it's a string being passed into the [] operator.
        if isinstance(item, str):
            return self.find_letters(item)

        # If any other value is passed in, raise an error.
        raise ValueError("Only a string can go in the [] operator for Words.")