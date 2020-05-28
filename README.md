# doxygen - readthedocs test

Motivation: have documentation build for both C/C++ and Python in one documentation set. To do this, we'll use Doxygen and Sphinx.

We basically just need to follow the following:

1. Format docstrings according to [accepted formats](https://www.doxygen.nl/manual/docblocks.html)
2. Setup Exhale according to the [Quickstart guide](https://exhale.readthedocs.io/en/latest/usage.html#quickstart-guide)

Exhale sets up Sphinx to call Doxygen to deploy to readthedocs.

## Proposed format:

The key part is the second `*` on the first line. This is what tells Doxygen this is a docstring. There are other formats, but this one is easy. If you have a strong opinion, let me know

```c
/**
 * A brief history of JavaDoc-style (C-style) comments.
 *
 * This is the typical JavaDoc-style C-style comment. It starts with two
 * asterisks.
 *
 * @param theory Even if there is only one possible unified theory. it is just a
 *               set of rules and equations.
 */
void cstyle( int theory );
```

## Things to note

Exhale just sets ups Sphinx to call Doxygen. So we still need to call sphinx. The first time you run sphinx in a project, you'll first need to run

```
sphinx-quickstart
```

and fill out the prompts.  Then, modify the `conf.py` according to what Exhale asks for, add the `requirements.txt`, and update `index.rst`

Finally, you can make the docstrings by calling `make html` in the docs folder. Sphinx created a `makefile` when we executed `sphinx-quickstart`.

## Example

This repo is an example. I didn't gitignore anything, so you can navigate around the `docs` folder to see what it outputted. Open [docs/_build/html/index.html](docs/_build/html/index.html) to see the output - it's readthedocs but with C++!
