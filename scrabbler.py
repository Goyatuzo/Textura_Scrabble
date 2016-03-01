import sys

from Structures.prefix import Prefix
from Structures.words import Words
from Structures.suffix import Suffix


def get_cmd_args():
    return sys.argv[1::]


def create_word_list(filename):
    """Construct a list of words from the words in filename. If rev
    is flagged, reverse each string.
    :param filename: The filename containing the list of words."""
    f = open(filename, 'r')

    return [line.strip() for line in f]


def create_words(filename):
    """Create a word object based on the words in filename.
    :param filename: The filename containing the list of words."""
    return Words(create_word_list(filename))


def create_prefix(filename):
    """Create prefix object based on words in filename.
    :param filename: The filename containing the list of words."""
    return Prefix(create_word_list(filename))


def create_suffix(filename):
    """Create suffix object based on words in filename.
    :param filename: The filename containing the list of words."""
    return Suffix(create_word_list(filename))

####################################

args = get_cmd_args()

if len(args) == 2:
    input_string = args[1]
else:
    input_string = args[0]

# Input arg --suffix
if args[0] == '--suffix':
    # The input argument has to be backwards too, since the words are stored in reverse.
    words = create_suffix('words.txt')[input_string]

    if not words:
        print "No match for suffix of " + input_string
    else:
        print "\n".join(words)


# Input arg --prefix
elif args[0] == '--prefix':
    words = create_prefix('words.txt')[input_string]
    if not words:
        print "No match for prefix of " + input_string
    else:
        print "\n".join(words)

# No additional input arg
else:
    words = create_words('words.txt').find_letters(args[0])
    if not words:
        print "No match for any of the letters of " + input_string
    else:
        print "\n".join(words)
