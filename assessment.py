"""
Part 1: Discussion

1. What are the three main design advantages that object orientation
   can provide? Explain each concept.
        1) Abstraction: hiding complexity for ease of user interface
        2) Encapsulation: keeping all of the necessary components in one place
        3) Polymorphism: allowing interchangibility of components between different instances/types

2. What is a class?
    A class defines a data type, by defining particular attributes and methods that apply to 
    objects with that data type. Classes can be thought of as laying the abstract framework for the traits
    held by specific instances of that type. Using classes allows for encapsulation, abstraction, and polymorphism

3. What is an instance attribute?
    An instance attribute is an attribute that applies only to that specific instance
    of the class, as opposed to a class attribute, which is defined at the class level

4. What is a method?
    A method is similiar to a function, in that it takes parameters and contain code
    that performs some transformation or adjustment on the parameters. However, a method differs from
    a function in that it only exists within a specific class, and that in the formal definition of the 
    method the first parameter is self (but is called without the explicit self parameter)

5. What is an instance in object orientation?
    An instance is an occurance of a class created during runtime of the script

6. How is a class attribute different than an instance attribute?
   Give an example of when you might use each.
    A class attibute is initialized as the same value for all instances of that class. You would use a
    class variable for a configuration that will remain the same for all (or almost all) instances within that class.
    For example, all instances of the Dog class will have share a diet attribute of 'carnivore', 
    so you would make that a class attribute. On the other hand, each instance of the Dog class would have a specific name
    or owner that only applies to one specific instance of the class.


"""


# Parts 2 through 5:
# Create your classes and class methods

class Students(object):
    """Students class that holds student data"""

    def __init__(self, first_name, last_name, address):
        """Setting the instance attributes"""

        self.first_name = first_name
        self.last_name = last_name
        self.address = address


class Question(object):
    """Question class that holds a question and correct answer"""

    def __init__(self, question, correct_answer):
        """Setting the question and correct answer for the instance"""

        self.question = question
        self.correct_answer = correct_answer

    def guess_answer(self):
        """prints question to the console and tells user if answer is correct"""

        print self.question
        user_answer = raw_input("What is the answer: ")

        if user_answer == self.correct_answer:
            return True
        else:
            return False


class Exam(object):
    """Exam class that has list of questions as attribute"""

    def __init__(self, name):
        """Initializing name of exam and questions"""

        self.name = name
        self.questions = []

    def add_questions(self, question, correct_answer):
        """Takes a question and correct answer as parameters 
        and adds to questions attribute"""

        new_question = Question(question, correct_answer)
        self.questions.append(new_question)

    def administer_exam(self):
        """keeps track of questions asked and number of correct answers"""

        answered_correctly = 0.0
        questions_asked = 0.0
        for question in self.questions:
            if question.guess_answer() == True:
                answered_correctly += 1
            questions_asked += 1

        score_as_percent = (answered_correctly / questions_asked) * 100

        return score_as_percent

class Quiz(Exam):
    """Quiz subclass from Exam super class"""

    def administer_exam(self):

        raw_score = super(Quiz, self).administer_exam()
        if raw_score >= 50.0:
            return True
        else:
            return False


#Functions#

def take_test(exam, student):
    """administers the exam and assigns the score to the student instance"""

    exam_score = exam.administer_exam()
    student.score = exam_score


def example():
    """executing the exam"""

    new_exam = Exam("new_exam")
    current_student = Students('Lydia', 'Gorham', '4164 Emerald St. Oakland')

    first_q = "Who is the author of Python? "
    first_a = "Guido Van Rossum"
    new_exam.add_questions(first_q, first_a)

    second_q = "What are the three design advantages to classes? "
    second_a = "Abstraction, Encapsulation, Polymorphism"
    new_exam.add_questions(second_q, second_a)


    take_test(new_exam, current_student)

    return current_student.score


print example()





