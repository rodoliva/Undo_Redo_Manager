# Undo and Redo Manager
 
This is an undo and redo solution that arose from a problem in the development of one of my personal projects, a pricing model interface.


# The Problem

During the development of the first interface (product interface), I looked for ways to make a function to undo and redo the actions that were carried out in the interface.

![Screen record Gif](https://github.com/rodoliva/Product_Interface/blob/master/Others/screenprodinf.gif)

The problem, I was working with objects and their instances. After studying some examples, I managed to get to the first Undo and Redo Manager:

```python
class UndoRedoManager():

    def __init__(self, li):
        self.undo_list = []
        self.undo_list.append(li)
        self.redo_list = []

    def add_undo(self, action):
        #Add the action to the undo list.
        self.undo_list.append(action)

    def add_redo(self, action):
        #Add the action to the redo list
        self.redo_list.append(action)

    def delete_undo(self):
        #Remove the last action from the undo list and return it
        if not len(self.undo_list) <=1:
            last_undo = self.undo_list.pop()
            return last_undo

    def delete_redo(self):
        #Remove the last action from the redo list and return it
        if not len(self.redo_list) == 0:
            last_redo = self.redo_list.pop()
            return last_redo

    def new_action(self, action):
        """Use this function for each action.
        This clear redo list with every new action and
        add new element in the undo list"""
        self.redo_list = []
        self.add_undo(action)

    def undo(self):
        #Undo the last actions
        if not len(self.undo_list) <=1:
            action = self.delete_undo()
            self.add_redo(action)
            return self.undo_list[len(self.undo_list)-1]
        else:
            return self.undo_list[0]

    def redo(self):
        #Redo the last actions
        if not len(self.redo_list) == 0:
            action = self.delete_redo()
            self.add_undo(action)
            return action
        else:
            return self.undo_list[len(self.undo_list)-1]
```
