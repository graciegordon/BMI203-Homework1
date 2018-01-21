## BMI203-Homework1

This repository contains quicksort and bubble functions. Given a list the function will retrun the sorted list, the number of assignments and the number of conditionals

##Travis link
[![Build
Status](https://travis-ci.org/graciegordon/example.svg?branch=master)](https://travis-ci.org/graciegordon/example)


## usage

To use the package, first make a new conda environment and activate it

```
conda create -n exampleenv python=3
source activate exampleenv
```

then run

```
conda install --yes --file requirements.txt
```

to install all the dependencies in `requirements.txt`. Then the package's
main function (located in `example/__main__.py`) can be run as follows

```
python -m example
```

## testing

Testing is as simple as running

```
python -m pytest
```

from the root directory of this project.
