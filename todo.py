#! /bin/env python

# Command line to do list as per Faye's spec

import time
import pickle

__author__ = 'mrsixw'

taskList = []

class TaskContainer:
    def __init__(self, description, duedate):
        self.due = duedate
        self.description = description
        self.complete = False



def displayCurrentItems():
    print("----------------------------------")
    print("AutoFocus Task List Python Edition")
    print("----------------------------------")

    if len(taskList) == 0:
        print("No tasks")
    else:
        for x in taskList:
            print(x.description)


def getDate():
    """ Returns a date tuple to user to represent the date entered. Will validate the input.
    """
    date = None
    dateValid = False
    while dateValid == False:
        taskDateString = raw_input("Please enter the task completion date (dd/mm/yyyy):- ")
        try:
            # note to self, y for year is two digit, Y is full year
            date = time.strptime(taskDateString,"%d/%m/%Y")
            dateValid = True
        except ValueError, valErr:
            print("Invalid time : "+str(valErr))
    return date


def addNew():
    taskDescription = raw_input("Please enter the task descrption :- ");
    taskDate = getDate()
    print("TASK: "+taskDescription+" DUE ON: "+time.strftime("%d/%m/%Y", taskDate))

    task = TaskContainer(taskDescription,None)

    taskList.append(task)
    taskList.sort()

    pickle.dump(taskList, open("todo.pickle", "wb"))
    return

def parseInput(input_string):
    """ Parses the input of the     """
    return

while True:
    # load the pickle file of todo list
    taskList = pickle.load(open("todo.pickle","rb"))
    print("")
    displayCurrentItems()
    print("")

    print("(n) New Task (q) Quit  | Or enter task number plus (c)omplete (w)orked (r) return to new")
    # note to self, raw_input gives you back string. input() grabs the string and tries to evaulate it.
    menuOption = raw_input("")

    if menuOption == 'q':
        print("Bye")
        break
    elif menuOption == 'n':
        addNew()
    else :
        parseInput(menuOption)



