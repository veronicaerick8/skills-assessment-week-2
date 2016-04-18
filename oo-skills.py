## PART 1
"""
1)
Encapsulation is a benefit of OOP, since much of the details and individual parts of 
an object are in one place. Easier to understand and maintain, while reduces repetitive code. 
OOP models the real world more accurately. in most engineering and design, the wires and 
the moving parts are kept under the same hood, neatly tucked away. Finding errors is easier with 
OOP since with encapsulation, objects are self contained. Abstraction hides the details that 
we dont need to see. Polymorphism is the interchangeblility of components of code.

2)
A class is user defined prototype for an object, which defines a set of attributes that characterize
the instances that become real objects after instantiation.
Classes can model real world things and the general "idea" of them (like a Cat or a Car). I think of classes as a 
set instructions for creating objects. A class contains things that an object typically does, uses
or how it operates. Class variables are used when the variable should
apply to every single instance of that class.

3)
An instance attribute is a "real" attribute about a specific object
that has been created. So this would be a sticky note on arfy the dog
with information about arfy, not just dogs in general (superclass Dog).

4)
A method is a function that is defined within a class.

5) An instance is an object that is created with the __init__
method. Every instance of a class has its own specific data. instance
is just a word for a specific object created with instance 
attributes. 

6) A class attribute is a general attribute that applys to 
ALL instances of that class. So the parent class of Dog would have
class attributes that apply to all dogs (breathe, eat, sleep). These attributes
are true of all dogs. An instance attribute would be something
specific to an actual dog (object). A dogs fur color, breed, level
of bad breathe, name, etc. are all instance attributes that make up 
actual dogs. Instance attributes are most specific and take priority
over class attributes.
"""
##Part 2

class Student (object):
    def __init__(self, first_name, last_name, address):
        self.first_name = first_name
        self.last_name = last_name
        self.address = address

class Question (object):
    def __init__(self, question, correct_answer):
        self.question = question
        self.correct_answer = correct_answer
    
    def ask_and_evaluate(self):
        user_input = raw_input(self.question)
        if user_input == self.correct_answer:
            return True
        else:
            False
        
        

class Exam (object):
    def __init__(self, name, questions):
        self.name = name
        self.questions = []

    def question_add(self, question, correct_answer):
        pass

    def administer(self):
        score = 0
        for question in self.questions:
            ask_and_evaluate(self.question)
            if ask_and_evaluate == True:
                score += 1
        return score



