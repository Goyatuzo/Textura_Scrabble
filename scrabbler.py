import sys

from Structures.prefix import Prefix
from Structures.words import Words


def get_cmd_args():
    return sys.argv[1::]


def create_words(filename):
    f = open(filename, 'r')
    lines = [line.strip() for line in f]

    return Words(lines)


def create_prefix(filename, suffix=False):
    f = open(filename, 'r')

    word_list = []

    for line in f:
        # Strip the newline
        line = line.strip()

        if suffix:
            word_list.append(line[::-1])
        else:
            word_list.append(line)

    return Prefix(word_list)

####################################

args = get_cmd_args()

input_string = args[1]

# Input arg --suffix
if args[0] == '--suffix':
    # The input argument has to be backwards too, since the words are stored in reverse.
    words = create_prefix('words.txt', True)[input_string[::-1]]
    if not words:
        print "No match for prefix of " + input_string
    # Fix the reversed strings when printing.
    else:
        for word in words:
            print word[::-1]


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
