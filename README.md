## Table of Contents

- [Overview](#Overview)
- [Features](#Features)
- [Installation](#Installation)
- [Tests](#Tests)
- [Decisions](#Decisions)
- [Technology](#Technology)
- [Programming Language](#Programming Language)
- [Dependencies](#Dependencies)
- [Author](#Author)
- [Standards](#Standards)

### Overview

#### Context:

A company rents bikes under following options: 

1. Rental by hour, charging $5 per hour 
2. Rental by day, charging $20 a day 
3. Rental by week, changing $60 a week 
4. Family Rental, is a promotion that can include from 3 to 5 Rentals (of any type) with a discount of 30% of the total price 

#### Assigment: 
1. Implement a set of classes to model this domain and logic 
2. Add automated tests to ensure a coverage over 85% 
3. Use GitHub to store and version your code 
4. Apply all the recommended practices you would use in a real project 
5. Add a README.md file to the root of your repository to explain: your design, the development practices you applied and how run the tests. 

Note: we don't expect any kind of application, just a set of classes with its automated tests. 


### Features

- Fee calculation by hour, day and week.
- Fee calculation by Family package.

### Installation

Open a terminal with git installed:

`git clone git@github.com:yaritaft/intive.git `

If you want to run the test manually without coverage:

`python test.py`

And you will see an image like these one:

![](https://github.com/yaritaft/intive/blob/master/images/test_manually.PNG)

### Tests

**Results in coveralls**

[![Coverage Status](https://coveralls.io/repos/github/yaritaft/intive/badge.svg)](https://coveralls.io/github/yaritaft/intive)

In order to reproduce the coverage test follow these commands:

`pip install --trusted-host pypi.python.org -r requirements.txt`

`coverage run test.py`

`coverage report`

##### Results

![](https://github.com/yaritaft/intive/blob/master/images/coverage_report.PNG)





### Decisions



### Technology

##### Programming Language

Python version 3.7.0

##### Dependencies 
`coverage==4.5.4`

They can also be found in requirements.txt.

### Standards

- Google Python Style Guide: http://google.github.io/styleguide/pyguide.html


### Author
Yari Ivan Taft

https://github.com/yaritaft/