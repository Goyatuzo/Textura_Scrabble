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

    ache
    ...
    chafed
    
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
For the default usage, the solution was to iterate through the word list and the letter string to find matches.

### Prefix/Suffix Solution
Initially, I created a FP-growth-like structure to store the values. However, I soon realized that since the program only runs once on one input, constructing the tree takes unnecessary time.

The tree construction takes O(n^2) worst case. This is the same worst case time as if each string was processed to see if its initial characters are the same as the input prefix.

Consequently, my previous data structure will be most useful for when there is batch processing, or when there are multiple prefixes to be scanned. Consequently, I chose to implement the easier variant because it is less prone to bugs and is much simpler to maintain.

Suffixes are handled by reversing all words in the dictionary as well as the input prefix. In other words, I handle a suffix as a prefix at the end of a word.