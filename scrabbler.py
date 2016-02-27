import sys

from Structures.prefix import Prefix
from Structures.words import Words


def get_cmd_args():
    return sys.argv[1::]


def create_words(filename):
    f = open(filename, 'r')
    lines = [line.strip() for line in f]

    return Words(lines)


def create_prefix(filename, suffix = False):
    f = open(filename, 'r')

    prefix_list = Prefix()

    for line in f:
        # If the reversed flag is raised, reverse the string.
        if suffix:
            line = line[::-1]
        # Add the word to the dictionary.
        prefix_list.add(line)

    return prefix_list

args = get_cmd_args()

# Input arg --suffix
if args[0] == '--suffix':
    words = create_prefix(args[1], True)
# Input arg --prefix
elif args[0] == '--prefix':
    words = create_prefix(args[1])
# No additional input arg
else:
    words = create_words(args[0])
    print "\n".join(words.find_letters(args[1]))
