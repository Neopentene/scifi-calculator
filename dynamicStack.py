# -*- coding: utf-8 -*-

class stack:
    '''
    Dynamic Stack using python list
    
    methods:
        
        isEmpty(): returns true if the stack is empty, else returns false
        
        push(self, value): appends the value provided on top of the stack
        
        pop(self): pops the element on top of the stack
        
        getList(self): returns the entire stack list
        
        getLength(self): returns the length of the list
            
    '''
    
    #Constructor to initialize the stack elements
    def __init__(self):
        self.__List = []
        self.__top = -1
        
    def isEmpty(self):
        if(self.__top == -1):
            return True
        else:
            return False
        
    def push(self, value):
        self.__List.append(value)
        self.__top = self.__top + 1
        
    def pop(self):
        if(self.__top > -1):
            value = self.__List.pop(self.__top)
            self.__top = self.__top - 1
            return value
        else:
            raise ValueError('Stack Underflow')
            
    def getList(self):
        return self.__List
    
    def getLength(self):
        return self.__top + 1