import itertools


class Words:

    def __init__(self, words):
        self.data = {}

        for word in words:
            sorted_word = "".join(set(sorted(word)))

            # If the word already exists in the dictionary, just append. Otherwise create new list.
            if sorted_word in self.data:
                self.data[sorted_word].append(word)
            else:
                self.data[sorted_word] = [word]

    def find_letters(self, letters):
        """Given a Words data structure, input a string of letters
        and find the words that contain any one of the letters.
        :param letters: String of letters to query list of words."""

        # Sort the letters and put them into a list.
        letters = set(sorted(letters))
        combos = []
        results = []

        # Create all possible combinations of the input string.
        for i in xrange(1, len(letters) + 1):
            curr_combos = list(itertools.combinations(letters, i))
            combos.extend(["".join(combo) for combo in curr_combos])

        # Now check self.data by searching all possible key combinations for the possible words, and when
        # found, combine the lists together.
        for combo in combos:
            # If the key doesn't exist, that means no word has the letters.
            if combo in self.data:
                results.extend(self.data[combo])

        # Sort the results so that it's alphabetical.
        results.sort()

        return results

    def __getitem__(self, item):
        # Confirm that it's a string being passed into the [] operator.
        if isinstance(item, str):
            return self.find_letters(item)

        # If any other value is passed in, raise an error.
        raise ValueError("Only a string can go in the [] operator for Words.")