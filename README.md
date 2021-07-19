# UdS SNLP Tutorial

Slides for Statistical Natural Language Processing tutorials of Summer 2021 at University of Saarland.

## Outline

Schedule (links provided only to semi-finished materials):
- [Introduction](introduction/handout.pdf)
- [Language Properties](language-properties/handout.pdf)
- [KL Divergece](kl-divergence/handout.pdf)
- [Compression](compression/handout.pdf)
- [Smoothing 1](smoothing-1/handout.pdf)
- [Smoothing 2](smoothing-2/handout.pdf)
- [Smoothing 3](smoothing-3/handout.pdf)
- [Text Classification 1](text-classification-1/handout.pdf)
- [Text Classification 2](text-classification-2/handout.pdf)
- [Word Sense Disambiguation](word-sense-disambiguation/handout.pdf)
- [Conditional Random Fields](conditional-random-fields/handout.pdf)
- [Information Retrieval](information-retrieval/handout.pdf)
- [Machine Translation (incomplete, skipped)](machine-translation/handout.pdf)

## Contributing

Compile slides using pandoc and the provided script (handout includes notes and disables iterative lists):
- Slides: `./build.sh machine-translation tutorial`
- Handout version: `./build.sh machine-translation handout`
- Both: `./build.sh machine-translation`

Make sure you have `pandoc` and `texlive` installed. You don't need to build the presentations if you want to contribute - editing the markdown is enough. If you still wish to compile them (great!) and encounter technical issues, contact me.

## License

Feel free to update, present and distribute on your own accord. In all cases, however, preserve the names of the previous contributors.
