---
layout: info
title: Tips for LaTeX  
permalink: /blog/latex
---

## Tips for LaTeX 

### Tutorials
* [OverLeaf](https://www.overleaf.com/learn/latex/Tutorials) 

### Free Editors
* Online: [OverLeaf](https://www.overleaf.com) 
* Local: [VSCode](https://code.visualstudio.com) + [Latex Workshop](https://marketplace.visualstudio.com/items?itemName=James-Yu.latex-workshop)

### Some packages and commands
* ``\usepackage{physics}``
  * ``\qty`` for paired brackets
  * ``\mqty`` for matrices
  * ``\abs`` for absolute values
  * ``\norm`` for norms
  * See the [manual](http://mirrors.ibiblio.org/CTAN/macros/latex/contrib/physics/physics.pdf) for more useful commands
* ``\usepackage{mathtools}``
  * ``\mathtoolsset{showonlyrefs}`` Numbering an equation only if it is referred to
* Use ``'``, instead of ``\prime``,  for prime
* Define your shorthands, e.g.,``\newcommand{\R}{\mathbb{R}}``, ``\newcommand{\pbop}[2]{\Pi_{f_{#2, #1, n}}\bop_{#2}}``
* ``\usepackage{natbib}``
  * ``\citet`` and ``\citealt`` are enough for all my citation

### Misc
* Use APA style reference, ``\bibliographystyle{apalike}``
* Use Git for version control
* Keep your notations consistent across different papers (this can save LOTS of time when you write your thesis)