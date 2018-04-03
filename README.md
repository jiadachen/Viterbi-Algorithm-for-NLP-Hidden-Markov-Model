# Viterbi Algorithm for NLP Hidden Markov Model
## Spec

This project is to build a trigram HMM tagger for named entities.

A training data set ner train.dat and a development set ner dev.key are provided. Both files are in the format of one word per line, word and token separated by space, a single blank line separates sentecnes.

There are four types of named entities: person names (PER), organizations (ORG), locations (LOC) and miscellaneous names (MISC). Named entity tags have the format I-TYPE. Only if two phrases of the same type immediately follow each other, the first word of the second phrase will have tag B-TYPE to show that it starts a new entity. Words marked with O are not part of a named entity.
