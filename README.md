# TM112 Unit Tests

The idea of this repository is to provide a suite of unit tests that support the Python 
quizzes and assignments for the October 2020 presentation of TM112 from the Open University.


I will do my best to ensure these are as accurate as possible but I accept no responsibility
for any marks lost if there's a bug or two here somewhere.  If you do find any problems
then raise an issue or PR to highlight and I'll do my best to sort it.

I plan to add to this overtime, mostly as I work through the course content but please shout
if you want anything in particular added and I'll see what can be done.

It goes without saying that I'm not providing any solutions here,  that's for you to do. So I
don't believe I'm breaking any OU rules in providing this.  If the repo dissapears you'll know I was
wrong and I've bean told off :-)
Hopefully having some unit tests will help you put solutions together more easily and 
give you some more confidence that you can try things locally to explore different ways
of doing things.

NB - somethings (e.g. turtle) really don't lend themselves brilliantly to unit testing. But
I'll do my best to cover as much as I can.

## What's this Unit Test thing all about anyway?
A Unit test is a piece of code that will run your code and check that with a given set
of inputs that the correct answer comes out the other end. For example, if you write a function
to add two numbers together then in plain English a unit would do this sort of thing
* Check that if input_1 = 1, and input_2 = 1 then output = 2
* Check that if input_1 = 10, and input_2 = 5 then output = 15
* Check that if input_1 = 10, and input_2 = -5 then output = 5
* Check that if input_1 = 10, and input_2 = "fish" then you get an error

This is a simple example, but hopefully you get the gist of things.

## But why Male Models (why are you doing this)?
This seemed like a good idea for a couple of reasons. 
* The quizzes let you submit code online and run a "check" - which is basically the same thing
we're doing here. It's just more convenient to be able to run things locally.
* Unit testing is a critical skill for software development, so for those people looking to do 
more of this some early exposure can only be a good thing.
* I thought by doing this it might be me think a little deeper about testing, and I should end up 
learning something.


## Some challenges
There's a few things here that make this slightly tricky.

* Unit tests are coupled quite strongly to the implementation of the code i.e. you will see
that each test has to import the relevant code in order to access it.  As a result, to 
easily run this stuff locally you'll need to replicate the folder structure I'm using (see the image below)

![folder layout](images/folder%20layout.png)

This a quite common way of laying stuff out - the important bit being to keep src files 
separate from tests (so you only deploy source code into your apps without cluttering them up with tests).

* The OU content has not yet got to the point where code is being encapsulated into functions. 
This means as soon as the module is imported the code runs, which is making it tricky to replace the points where 
the code is asking for user input.

## How do I run the unit tests?
I am using the Pytest library for running tests as opposed to the UnitTest library that
comes built in to Python.  This does offer much more functionality and a cleaner syntax
but for the relative beginners amongst it does mean that you have to install some extra
modules into your local environment.  I can only apologise for this small amount of additional
pain, but I can promise in the long run it will be worth it.

### Installing pytest and pytest-mock
There are a few ways to do this depending on how you are running Python.

##### Pipenv
This repo includes Pipfile and Pipfile.lock. So if you are using pipenv to manage virtual enviroments
(which I would reccomend, it's not that hard once you get your head around it) can just run `pipenv install -d`

If you want to check out Pipenv then this is a good guide - https://realpython.com/pipenv-guide/

##### Virtual Environment
If you're using virtualenv (or similar) to create an environment then make sure you've activated that environment
and run `pip install pytest pytest-mock`

##### System Python
Whilst I would never recommend running Python without making use of some form of virtual environment it's not strictly
required, and is another thing for new people to learn. So if you just want to get this stuff up and running in the local
Python install you can just run the command `pip install pytest pytest-mock` to get the packages installed.

### Running the tests
Open a command line / terminal prompt, and navigate to the folder that contains all of your code & tests
(you'll have to copy the tests into there).  You'll need to be in the same location as the src and tests folder.
Then run this command

`python -m pytest` 

This will find and run all of the unit tests that are present. Pytest does this by finding
any files that have a name starting with test - and then within that finding any functions
that also start with test.  These are then run through the pytest runner.

Note that I said _all_ tests, which will include tests for code you might not have written yet.
This isn't a problem per se, you'll just get errors you'll have to ignore.  Or you can filter
which tests run (https://stackoverflow.com/questions/36456920/is-there-a-way-to-specify-which-pytest-tests-to-run-from-a-file)

Those folks using things like PyCharm (the best and only correct option) or VSCode can run tests
directly within the IDE - and also pick which tests run.

### Looking at the results
In the ideal world everything will go green and all tests will pass.  
If not, then looking at the errors will help guide you as to what is wrong.

You will likely either see syntax errors (which means your code has a problem and couldn't run) or *Assertion Error*.
An assertion error means the code ran, but gave a difference answer than what the test was expecting.

Reviewing these assertion errors will help you understand what should have happened Vs what
did happen, and hopefully help you solve the problem.