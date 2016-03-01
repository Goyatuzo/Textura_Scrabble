[![Build Status](https://travis-ci.org/Goyatuzo/Textura_Scrabble.svg?branch=master)](https://travis-ci.org/Goyatuzo/Textura_Scrabble)

## Problem Statement

Given the included dictionary file `words.txt` write a program to take a shuffled set of letters and return:

 - what words from the dictionary the user can spell with these letters?
 - what words begin with these letters as a prefix?
 - what words end with these letters as a suffix?

You may use any programming language with which you're comfortable.  

Include along with your sourcecode any documentation necessary to compile / run your program.
 
Extra credit for performance optimizations and/or unit tests.

## Example Usage

Assume you're program is called "scrabbler".

To find all the words you can spell with 7 letters "abcdefg" you should be able to type:

    $ scrabbler abcdefg

And get back a list of words as output.  Something like:

        abed
        accede
        acceded
        ace
         ...
        gaged
        gagged
        gee
        geed

To find all words that begin with a specific prefix:

    $ scrabbler --prefix fi
    fix
    fixed
    ...
    fiz
    fizzy
    
To find all words with a specific suffix:

    $ scrabbler --suffix o
    aero
    ...
    zydeco
    
## Solution
There are two parts to the solution.

### Default Solution
For the default solution, the initial idea was to iterate through the entire list, checking for the existence of certain letters. However, on the revised edition, the algorithm becomes slightly more complex.

Since the user wants to spell a certain word with the given 7 letters, the ordering is not as significant. What matters is the count of letters, so the best way to solve this would be to alphabetically sort the letters, and use it as a key to find the list of words that have the same set of letters.

### Prefix/Suffix Solution
Initially, I created a FP-growth-like structure to store the values. However, I soon realized that since the program only runs once on one input, constructing the tree takes unnecessary time.

The tree construction takes O(nm) worst case. n represents the word list length, and m represents the prefix length. This is the same worst case time as if each string was processed to see if its initial characters are the same as the input prefix. In other words, tree construction could potentially take as long as brute forcing the answer for one iteration. In addition to tree construction, the query involves DFS which adds even more time. Consequently, I decided to use brute force instead.

If there was a need for batch processing (such as find all possible prefixes with the current hand), then the tree would have greatly increased the time.

Suffixes are handled by reversing all words in the dictionary as well as the input prefix. In other words, I handle a suffix as a prefix at the end of a word.

## Usage
Runs on python 2.7.

For prefix and suffix querying.

    $ python scrabbler.py --[prefix | suffix] letters

Default query.

    $ python scrabbler.py letters

Testing

    $ cd Structures
    $ python runner.py
