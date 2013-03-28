#!/usr/bin/env python

# Command line to do list as per Faye's spec

import time
import pickle
import datetime

__author__ = 'mrsixw'

class TaskContainer:
    def __init__(self, description, duedate=datetime.date.today(), complete=False):
        self.due = duedate
        self.description = description
        self.complete = complete

    def makeComplete(self):
        self.complete = True

    def setDescription(self, description):
        self.description = description

    def setNewCompleteDate(self, newDate=datetime.date.today):
        self.due = newDate


class TaskList:
    TASK_FILE = "todo.pickle"
    tasklist = []

    def __init__(self):
        self.list = []

    def saveList(self):
        """Saves the task list to persistent storage"""
        pickle_file = open(TaskList.TASK_FILE, "wb")
        pickle.dump(self.list, pickle_file)
        pickle_file.close()

    def loadList(self):
        pickle_file = open(TaskList.TASK_FILE, "rb")
       # self.list = pickle.load(pickle_file)
        pickle_file.close()

    def displayCurrnetTasks(self):
        for x in self.list:
            print(x.description)

    def addTask(self, task):

        print type(self.list)
        #print type(self.tasklist)

        self.list.append(task)




def getDate():
    """ Returns a date tuple to user to represent the date entered. Will validate the input.
    """
    date = None
    dateValid = False
    while not dateValid:
        taskDateString = raw_input("Please enter the task completion date (dd/mm/yyyy):- ")
        try:
            # note to self, y for year is two digit, Y is full year
            date = time.strptime(taskDateString, "%d/%m/%Y")
            dateValid = True
        except ValueError, valErr:
            print("Invalid time : " + str(valErr))

    return date


def addNew(taskList):
    taskDescription =  "Steve "# raw_input("Please enter the task descrption :- ")
   # taskDate = getDate()
#    print("TASK: " + taskDescription + " DUE ON: " + time.strftime("%d/%m/%Y", taskDate))

    task = TaskContainer(taskDescription, None)

    taskList.addTask(task)

#    pickle.dump(taskList, open("todo.pickle", "wb"))
    return


def parseInput(input_string):
    """ Parses the input of the     """
    # regex
    return


tasks = TaskList()
tasks.loadList()

while True:

    # note to self, raw_input gives you back string. input() grabs the string and tries to evaluate it.
    menuOption = 'n'#raw_input("(n) New Task (q) Quit  | Or enter task number plus (c)omplete (w)orked (r) return to new")

    if menuOption == 'q':
        print("Bye")
        tasks.saveList()
        break
    elif menuOption == 'n':
        addNew(tasks)
    else:
        parseInput(menuOption)
