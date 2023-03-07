# -*- coding: utf-8 -*-

from dynamicStack import stack
from calLogs import logManager


class Evaluator:
    """
    Postfix Expression Evaluator using a dynamic stack

    methods:

        getPostfix(self): returns the postfix expression in form of a list

        evaluate(self): returns the evaluation of the postfix expression

        changeExpression(self, new): changes the expression and generates the postfix for said expression

    """

    # Initialize the evaluation class with the required data
    def __init__(self, expression):
        self.expression = expression.replace(' ', '')
        self.__postfix = stack()
        self.__evaluator = stack()
        self.__operator = stack()
        self.__db = logManager()

    # Static method to return the priority of the passed operator
    @staticmethod
    def __priority(operator):
        if operator == '-' or operator == '+':
            return 1
        elif operator == '*' or operator == '×' or operator == 'x' or operator == '/' or operator == '÷':
            return 2
        elif operator == '^':
            return 3
        else:
            return 0

    # Static method to check if the character passed is an operator
    @staticmethod
    def __isOperator(character):
        if character == '-' or character == '+':
            return True
        elif character == '*' or character == '×' or character == 'x' or character == '/' or character == '÷':
            return True
        elif character == '^':
            return True
        else:
            return False

            # Static method to check if the character passed is a number

    @staticmethod
    def __isNumber(character):
        if character.isdigit():
            return True
        else:
            return False

    # Static method to check if the character passed is a dot defining a decimal
    @staticmethod
    def __isDecimal(character):
        if character == '.':
            return True
        else:
            return False

    # Static method to initialize the factorial of the given number
    @staticmethod
    def __isFactorial(character):
        if character == '!':
            return True
        else:
            return False

    # Static method to check if the character passed is an opening parenthesis
    @staticmethod
    def __isOpeningParenthesis(character):
        if character == '(':
            return True
        else:
            return False

    # Static method to check if the character passed is a closing parenthesis
    @staticmethod
    def __isClosingParenthesis(character):
        if character == ')':
            return True
        else:
            return False

    # Static method to check if the character passed is a parenthesis
    @staticmethod
    def __isParenthesis(character):
        if character == '(' or character == ')':
            return True
        else:
            return False

    # Static method to get the factorial of a value
    @staticmethod
    def __factorial(value):
        if isinstance(value, float):
            if abs(value) > abs(int(value)):
                raise SyntaxError('Incorrect Expression')
        factorial = 1
        for i in range(1, int(value) + 1):
            factorial = factorial * i
        return factorial

    # Operates between two numbers
    @staticmethod
    def __operate(a, b, operator):

        if operator == '-':
            return a - b
        elif operator == '+':
            return a + b
        elif operator == '*' or operator == '×' or operator == 'x':
            return a * b
        elif operator == '/' or operator == '÷':
            return a / b
        elif operator == '^':
            return a ** b

    # Checks for correct number of opening and closing parenthesis
    def __correctExpression(self):
        oP = 0
        cP = 0
        for parenthesis in self.expression:
            if self.__isOpeningParenthesis(parenthesis):
                oP = oP + 1
            elif self.__isClosingParenthesis(parenthesis):
                cP = cP + 1

        if oP == cP:
            return True
        else:
            return False

    # Generates a postfix expression
    def __generatePostfix(self):

        # Check if the parenthesis are in order
        if self.__correctExpression():

            # Holders and counters
            holder = 0
            d_holder = 0
            lastPriority = 0
            decimalCounter = 0

            # Condition booleans or in better words Flags
            First = True
            numFound = False
            decimal = False
            op_obtained = False
            isNegativeDigit = False
            blockClosed = False
            factorialFound = False

            # Loop through each character of the expression
            for character in self.expression:

                # If an operator is found
                if self.__isOperator(character):

                    # If there was a number found before the operator
                    # If the number found was a decimal
                    if decimal and numFound:
                        holder = holder + d_holder

                        # If the number acquired a negative integer
                        if isNegativeDigit:
                            holder = 0 - holder
                            self.__postfix.push(holder)

                        # If it was not a negative integer
                        else:
                            self.__postfix.push(holder)

                        # Reset some conditions and holders
                        d_holder = decimalCounter = holder = 0
                        decimal = factorialFound = numFound = isNegativeDigit = False

                    # If the number found was not a decimal
                    elif numFound:

                        # If the number acquired a negative integer
                        if isNegativeDigit:
                            holder = 0 - holder
                            self.__postfix.push(holder)

                        # If it was not a negative integer
                        else:
                            self.__postfix.push(holder)

                        # Reset some conditions and holders
                        holder = 0
                        decimal = factorialFound = numFound = isNegativeDigit = False

                    # Get the priority of the character
                    priority = self.__priority(character)

                    # Check if the priority is higher than 1 and whether the operator was obtained first
                    # If this is the case than we have a syntax error in the expression
                    if priority > 1 and First and not blockClosed:
                        raise SyntaxError('Incorrect Expression')

                    # If the operator obtained was first or was another operator acquired before this operator
                    elif priority == 1 and op_obtained or First and not blockClosed:
                        # If the newly acquired operator is a negative sign then we have a negative number amidst
                        if character == '-':
                            isNegativeDigit = True

                    # If the priority of the previously obtained operator had a greater priority than the new operator
                    # If yes, then we had a division or multiplication or a power before this operator
                    elif priority <= lastPriority and not op_obtained:

                        # In this case we empty the operator stack till it is empty or if we find an opening parenthesis
                        for operator in range(self.__operator.getLength()):
                            poppedValue = self.__operator.pop()

                            # If an opening parenthesis is not found and popped operator is of high or equal priority
                            if not self.__isOpeningParenthesis(poppedValue) and self.__priority(
                                    poppedValue) >= priority:

                                # Push the operator from the operator stack on the postfix stack
                                self.__postfix.push(poppedValue)

                            # If an opening parenthesis is found
                            else:
                                # Push the parenthesis on the operator stack again
                                self.__operator.push(poppedValue)
                                break

                        # Push the new operator into the operator stack
                        self.__operator.push(character)

                        # Set the condtions and holders
                        op_obtained = True
                        lastPriority = priority
                        First = blockClosed = False

                    # All the previous conditions have failed and everything is in correct sequence
                    else:

                        # Push the operator on the operator stack
                        self.__operator.push(character)

                        # Set the conditions and holders
                        op_obtained = True
                        lastPriority = priority
                        First = blockClosed = False

                # If the expression is a closing parenthesis
                elif self.__isClosingParenthesis(character):

                    # Same conditions to upload the number if any on the postfix stack
                    if decimal and numFound:
                        holder = holder + d_holder
                        if isNegativeDigit:
                            holder = 0 - holder
                            self.__postfix.push(holder)
                        else:
                            self.__postfix.push(holder)
                        d_holder = decimalCounter = holder = 0
                        decimal = factorialFound = numFound = isNegativeDigit = False

                    elif numFound:
                        if isNegativeDigit:
                            holder = 0 - holder
                            self.__postfix.push(holder)
                        else:
                            self.__postfix.push(holder)
                        holder = 0
                        decimal = factorialFound = numFound = isNegativeDigit = False

                        # Empty out all the operators until an opening parenthesis is found
                    # This means that the current block's operations have been given more priority
                    for operator in range(self.__operator.getLength()):
                        poppedValue = self.__operator.pop()

                        # If the popped value is not an opening parenthesis add it on postfix stack
                        if not self.__isOpeningParenthesis(poppedValue):
                            self.__postfix.push(poppedValue)

                        # If it is an opening parenthesis discard it
                        else:
                            break

                    # The priorities are set and some conditions have been refreshed
                    if not self.__operator.isEmpty():
                        tOperator = self.__operator.pop()
                        lastPriority = self.__priority(tOperator)
                        self.__operator.push(tOperator)
                    else:
                        lastPriority = 0
                    op_obtained = False
                    First = blockClosed = True

                # If the character is !, then change the number holder to its factorial
                elif self.__isFactorial(character):
                    # If the number is a decimal or if there is no number
                    if not numFound and decimal or decimal:
                        if decimal:
                            if d_holder == 0.0:
                                holder = self.__factorial(holder + d_holder)
                                factorialFound = True
                            else:
                                raise SyntaxError('Invalid Expression')
                        else:
                            raise SyntaxError('Invalid Expression')

                    # If the factorial is for a block of expression we push it on the stack for evaluator to calculate
                    elif First:
                        if blockClosed:
                            self.__postfix.push(character)
                            factorialFound = True
                            First = blockClosed = False
                        else:
                            raise SyntaxError('Invalid Expression')

                    # Set the holder to its decimal value
                    else:
                        holder = self.__factorial(holder)
                        factorialFound = True

                # If we find a number which is not a decimal, we hold the number
                elif self.__isNumber(character) and not decimal:

                    # If the number is not first and we don't have an operator before it, neither do we have any number before it
                    # This is an syntax error as the number is all alone
                    if not First and not op_obtained and not numFound and factorialFound:
                        raise SyntaxError('Invalid Expression')

                    # Holder holds the numeric value
                    holder = holder * 10 + int(character)

                    # Setting some conditions for later use
                    First = op_obtained = blockClosed = False
                    numFound = True

                # If the number we find is decimal, we hold the decimal in a separate holder
                elif decimal or self.__isDecimal(character):

                    # If the character is a dot then we initialize the decimal counter and decimal holder
                    if not self.__isDecimal(character) and decimal:
                        decimalCounter = decimalCounter + 1
                        d_holder = d_holder + (int(character) / (10 ** decimalCounter))
                    else:
                        decimal = True

                    # Decimal is also a number
                    numFound = True

                    # Reseting the first flag
                    First = blockClosed = False

                    # If an opening parenthesis is found
                elif self.__isOpeningParenthesis(character):

                    if not op_obtained and not First:
                        raise SyntaxError('Invalid Expression')

                    # We have a new block therefore a fresh operation
                    First = True
                    op_obtained = factorialFound = blockClosed = False
                    self.__operator.push(character)

                # No conditions match that means the expression is invalid
                else:
                    raise SyntaxError('Invalid Expression')

                # print(self.__operator.getList(), self.__operator.getLength(), holder, d_holder, op_obtained, First, isNegativeDigit, numFound, blockClosed)
                # print(self.__postfix.getList())

        # Parenthesis don't match
        else:
            raise TypeError('Parenthesis Don\'t Match')

        # If we are still holding onto a number, add it on the postfix stack
        if numFound:
            if decimal:
                holder = holder + d_holder
            if isNegativeDigit:
                holder = 0 - holder
                self.__postfix.push(holder)
            else:
                self.__postfix.push(holder)

        # If we have pending operators add them on the postfic stack
        if not self.__operator.isEmpty():
            while (not self.__operator.isEmpty()):
                self.__postfix.push(self.__operator.pop())

        # print(self.__operator.getList(), self.__operator.getLength(), holder, d_holder, op_obtained, First, isNegativeDigit, numFound)

    # Returns the postfix stack as a list
    # If the postfix stack is not generated it generates a new one
    def getPostfix(self):
        if self.__postfix.isEmpty():
            self.__generatePostfix()
            return self.__postfix.getList()
        else:
            return self.__postfix.getList()

    # Changes the expression and generates a postfix for it
    def changeExpression(self, new):
        self.expression = new.replace(' ', '')
        self.__generatePostfix()

    # Evaluates the expression
    def evaluate(self):

        # Gets the postfix list for iteration
        postfix = self.getPostfix()

        # Loop to iterate through the postfix list
        for value in postfix:

            # If the value is not an operator, then push the value on evaluator stack
            if not self.__isOperator(value):
                # If the obtained value is a factorial instruction
                if self.__isFactorial(value):
                    self.__evaluator.push(self.__factorial(self.__evaluator.pop()))
                # If not then push on the evaluator
                else:
                    self.__evaluator.push(value)

            # If it is an operator then pop 2 numbers and push their operation result on the evaluator stack
            else:

                # initialize the numbers a and b
                a = b = 0

                # If the evaluator stack is not empty
                if not self.__evaluator.isEmpty():
                    b = self.__evaluator.pop()

                # If the evaluator stack is not empty
                if not self.__evaluator.isEmpty():
                    a = self.__evaluator.pop()

                # Getting the result and pushing it on the evaluator stack
                result = self.__operate(a, b, value)
                self.__evaluator.push(result)

        # The top value on the evaluator is the answer, so pop that value
        finalResult = self.__evaluator.pop()

        # Checks for the validity of the answer
        if isinstance(finalResult, int) or isinstance(finalResult, float):
            self.__db.insertLog(self.expression, str(finalResult))
            return finalResult
        else:
            raise SystemError('System Crash')


if __name__ == '__main__':
    # expression = Evaluator('-1.34+23*(6.91^2!--1.0123)^(34+-9*10.11)-3')
    expression = Evaluator(input('Enter an expression: '))
    print('Expression:', expression.expression)
    print(expression.getPostfix())
    print('Answer:', expression.evaluate())
    logs = logManager()
    print(logs.getAllLogs())
    if input('Erase data (Y/N): ') == 'Y':
        logs.clearAllLogs()
