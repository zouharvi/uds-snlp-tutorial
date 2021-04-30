# UdS SNLP Tutorial

Incomplete slides for Statistical Natural Language Processing tutorials of Summer 2021 at University of Saarland.

## Outline

Schedule (links provided only to semi-finished materials):
- [Introduction](introduction/handout.pdf)
- [Language Properties](introduction/handout.pdf)
- Entropy
- Language Modelling
- Text Classification
- Word Sense Disambiguation
- [Information Retrieval](information-retrieval/handout.pdf)
- [Machine Translation](machine-translation/handout.pdf)
- [Conditional Random Fields](conditional-random-fields/handout.pdf)

## Contributing

Compile slides using pandoc and the provided script (handout includes notes and disables iterative lists):
- Slides: `./build.sh machine-translation tutorial`
- Handout version: `./build.sh machine-translation handout`
- Both: `./build.sh machine-translation`

Make sure you have `pandoc` and `texlive` installed. You don't need to build the presentations if you want to contribute - editing the markdown is enough. If you still wish to compile them (great!) and encounter technical issues, contact me.
