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
