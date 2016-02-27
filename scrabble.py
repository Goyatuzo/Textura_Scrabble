import sys

from Structures.prefix import Prefix


def get_cmd_args():
    return sys.argv[1::]


def get_dictionary(filename, suffix = False):
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
    words = get_dictionary(args[1], True)
# Input arg --prefix
elif args[0] == '--prefix':
    words = get_dictionary(args[1])
# No additional input arg
else:
    words = get_dictionary(args[0])
