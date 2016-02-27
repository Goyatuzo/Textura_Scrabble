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
I created a prefix tree based on the FP-Tree structure. However, since we care about each word, the support counts are not being counted. Instead, each word will keep traversing through the data structure, creating new nodes if necessary, until there are no letters to be processed. The end of the word is labeled as a whitespace to help with processing.

Using this structure, one can input the prefix and the structure will traverse appropriately to the end of the prefix. Once the end is reached, all possible subtrees from that point will be printed out, and since each path to a leaf is a unique word, all possible words will be printed.

Once the prefix structure is completed, one can use it to work for suffixes as well with one small tweak. Suffixes are prefixes if a string is reversed. So if the input words are all reversed, and the input suffix is also reversed, the exact same algorithm can be run to produce the desired answers.