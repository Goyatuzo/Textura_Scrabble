class Prefix:
    def __init__(self):
        self.data = {}

    @staticmethod
    def _sanitize(word):
        return word + ' '

    def add(self, word):
        """Add a word to the Words data structure.
        :param word: The word to be added to the data structure."""
        word = self._sanitize(word)

        curr_dict = self.data

        for c in word:
            # If c doesn't exist in dictionary, create new empty dict.
            if c not in curr_dict:
                curr_dict[c] = {}

            # Advance to the index of c within dictionary.
            curr_dict = curr_dict[c]

    def exists(self, query):
        """Determine whether or not a partuclar word exists within this
        data structure.
        :param query: The word to be queried for its existence."""
        query = self._sanitize(query)

        curr_dict = self.data

        for c in query:
            # If the current letter doesn't exist, return false.
            if c not in curr_dict:
                return False

            # Otherwise go one level deeper into the nested dictionaries.
            curr_dict = curr_dict[c]

        # If it's made it to here, that means the word exists.
        return True


    def get_words(self, prefix):
        """Given an input prefix string, return the list of words that begin
        with prefix.
        :param prefix: The prefix of the word."""
        curr_dict = self.data

        # Store the strings here.
        results = []

        # Go in as far as possible in the dictionary with input prefix.
        for c in prefix:
            curr_dict = curr_dict[c]





    def __str__(self):
        """This function will be called when the Words data structure is
        being printed."""

        return "Test"
