# -*- coding: utf-8 -*-

import sqlite3

class logManager:
    '''
    A database manager class that has methods to access, insert and delete calculator logs
    
    methods:
        
        getAllLogs(self): returns a list of all logs available in the table
        
        insertLog(self, expression, value): adds a log into the table
        
        clearAllLogs(self): Drops the table and creates a new one with no logs
    
    '''
    
    def __init__(self):
        self.__connection = sqlite3.connect('calLog.db')
        self.__cursor = self.__connection.cursor()
        self.__createLogs()
        
        
    def __createLogs(self):
        self.__cursor.execute('''CREATE TABLE IF NOT EXISTS calLogs(
                                    expression TEXT,
                                    result TEXT
                                    )''')
        self.__connection.commit()
    
    def getAllLogs(self):
        self.__cursor.execute('SELECT * FROM calLogs')
        List = self.__cursor.fetchall()
        self.__connection.commit()
        return List
    
    def insertLog(self, expression, value):
        self.__cursor.execute("INSERT INTO calLogs VALUES (:expression, :value)"
                              , {'expression':expression, 'value':value})
        self.__connection.commit()
        
    def clearAllLogs(self):
        self.__cursor.execute('DROP TABLE calLogs')
        self.__connection.commit()
        self.__createLogs()