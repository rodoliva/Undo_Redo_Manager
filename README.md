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

The results looked good:

```shell
list  [5, 6, 7, 8]

first add
list  [5, 6, 7, 8, 1]
undo list [[5, 6, 7, 8], [5, 6, 7, 8, 1]]
redo list []

second add
list  [5, 6, 7, 8, 1, 2]
undo list [[5, 6, 7, 8], [5, 6, 7, 8, 1], [5, 6, 7, 8, 1, 2]]
redo list []

first undo
list  [5, 6, 7, 8, 1]
undo list [[5, 6, 7, 8], [5, 6, 7, 8, 1]]
redo list [[5, 6, 7, 8, 1, 2]]

second undo
list  [5, 6, 7, 8]
undo list [[5, 6, 7, 8]]
redo list [[5, 6, 7, 8, 1, 2], [5, 6, 7, 8, 1]]

third undo
list  [5, 6, 7, 8]
undo list [[5, 6, 7, 8]]
redo list [[5, 6, 7, 8, 1, 2], [5, 6, 7, 8, 1]]

first redo
list  [5, 6, 7, 8, 1]
undo list [[5, 6, 7, 8], [5, 6, 7, 8, 1]]
redo list [[5, 6, 7, 8, 1, 2]]

second redo
list  [5, 6, 7, 8, 1, 2]
undo list [[5, 6, 7, 8], [5, 6, 7, 8, 1], [5, 6, 7, 8, 1, 2]]
redo list []

third redo
list  [5, 6, 7, 8, 1, 2]
undo list [[5, 6, 7, 8], [5, 6, 7, 8, 1], [5, 6, 7, 8, 1, 2]]
redo list []
```


Here comes the disaster ... all the same and when changing a variable, it is the same:


```shell
------------Object list Test------------
list  [<__main__.Test object at 0x0225C3D0>, <__main__.Test object at 0x0225C298>, <__main__.Test object at 0x0225C358>, <__main__.Test object at 0x0225C388>]
['t1', 't2', 't3', 't4']
----------------------------------------

------------first add------------
list  [<__main__.Test object at 0x0225C3D0>, <__main__.Test object at 0x0225C298>, <__main__.Test object at 0x0225C358>, <__main__.Test object at 0x0225C388>, <__main__.Test object at 0x0225C3E8>]
['t1', 't2', 't3', 't4', 't5']
undo list [[<__main__.Test object at 0x0225C3D0>, <__main__.Test object at 0x0225C298>, <__main__.Test object at 0x0225C358>, <__main__.Test object at 0x0225C388>, <__main__.Test object at 0x0225C3E8>], [<__main__.Test object at 0x0225C3D0>, <__main__.Test object at 0x0225C298>, <__main__.Test object at 0x0225C358>, <__main__.Test object at 0x0225C388>, <__main__.Test object at 0x0225C3E8>]]
[['t1', 't2', 't3', 't4', 't5'], ['t1', 't2', 't3', 't4', 't5']]
redo list []
[]
------------------------------------

------------second add------------
list  [<__main__.Test object at 0x0225C3D0>, <__main__.Test object at 0x0225C298>, <__main__.Test object at 0x0225C358>, <__main__.Test object at 0x0225C388>, <__main__.Test object at 0x0225C3E8>, <__main__.Test object at 0x0225C418>]
['t1', 't2', 't3', 't4', 't5', 't6']
undo list [[<__main__.Test object at 0x0225C3D0>, <__main__.Test object at 0x0225C298>, <__main__.Test object at 0x0225C358>, <__main__.Test object at 0x0225C388>, <__main__.Test object at 0x0225C3E8>, <__main__.Test object at 0x0225C418>], [<__main__.Test object at 0x0225C3D0>, <__main__.Test object at 0x0225C298>, <__main__.Test object at 0x0225C358>, <__main__.Test object at 0x0225C388>, <__main__.Test object at 0x0225C3E8>, <__main__.Test object at 0x0225C418>], [<__main__.Test object at 0x0225C3D0>, <__main__.Test object at 0x0225C298>, <__main__.Test object at 0x0225C358>, <__main__.Test object at 0x0225C388>, <__main__.Test object at 0x0225C3E8>, <__main__.Test object at 0x0225C418>]]
[['t1', 't2', 't3', 't4', 't5', 't6'], ['t1', 't2', 't3', 't4', 't5', 't6'], ['t1', 't2', 't3', 't4', 't5', 't6']]
redo list []
[]
------------------------------------

------------first undo------------
list  [<__main__.Test object at 0x0225C3D0>, <__main__.Test object at 0x0225C298>, <__main__.Test object at 0x0225C358>, <__main__.Test object at 0x0225C388>, <__main__.Test object at 0x0225C3E8>, <__main__.Test object at 0x0225C418>]
['t1', 't2', 't3', 't4', 't5', 't6']
undo list [[<__main__.Test object at 0x0225C3D0>, <__main__.Test object at 0x0225C298>, <__main__.Test object at 0x0225C358>, <__main__.Test object at 0x0225C388>, <__main__.Test object at 0x0225C3E8>, <__main__.Test object at 0x0225C418>], [<__main__.Test object at 0x0225C3D0>, <__main__.Test object at 0x0225C298>, <__main__.Test object at 0x0225C358>, <__main__.Test object at 0x0225C388>, <__main__.Test object at 0x0225C3E8>, <__main__.Test object at 0x0225C418>]]
[['t1', 't2', 't3', 't4', 't5', 't6'], ['t1', 't2', 't3', 't4', 't5', 't6']]
redo list [[<__main__.Test object at 0x0225C3D0>, <__main__.Test object at 0x0225C298>, <__main__.Test object at 0x0225C358>, <__main__.Test object at 0x0225C388>, <__main__.Test object at 0x0225C3E8>, <__main__.Test object at 0x0225C418>]]
[['t1', 't2', 't3', 't4', 't5', 't6']]
------------------------------------

------------second undo------------
list  [<__main__.Test object at 0x0225C3D0>, <__main__.Test object at 0x0225C298>, <__main__.Test object at 0x0225C358>, <__main__.Test object at 0x0225C388>, <__main__.Test object at 0x0225C3E8>, <__main__.Test object at 0x0225C418>]
['t1', 't2', 't3', 't4', 't5', 't6']
undo list [[<__main__.Test object at 0x0225C3D0>, <__main__.Test object at 0x0225C298>, <__main__.Test object at 0x0225C358>, <__main__.Test object at 0x0225C388>, <__main__.Test object at 0x0225C3E8>, <__main__.Test object at 0x0225C418>]]
[['t1', 't2', 't3', 't4', 't5', 't6']]
redo list [[<__main__.Test object at 0x0225C3D0>, <__main__.Test object at 0x0225C298>, <__main__.Test object at 0x0225C358>, <__main__.Test object at 0x0225C388>, <__main__.Test object at 0x0225C3E8>, <__main__.Test object at 0x0225C418>], [<__main__.Test object at 0x0225C3D0>, <__main__.Test object at 0x0225C298>, <__main__.Test object at 0x0225C358>, <__main__.Test object at 0x0225C388>, <__main__.Test object at 0x0225C3E8>, <__main__.Test object at 0x0225C418>]]
[['t1', 't2', 't3', 't4', 't5', 't6'], ['t1', 't2', 't3', 't4', 't5', 't6']]
------------------------------------

------------third undo------------
list  [<__main__.Test object at 0x0225C3D0>, <__main__.Test object at 0x0225C298>, <__main__.Test object at 0x0225C358>, <__main__.Test object at 0x0225C388>, <__main__.Test object at 0x0225C3E8>, <__main__.Test object at 0x0225C418>]
['t1', 't2', 't3', 't4', 't5', 't6']
undo list [[<__main__.Test object at 0x0225C3D0>, <__main__.Test object at 0x0225C298>, <__main__.Test object at 0x0225C358>, <__main__.Test object at 0x0225C388>, <__main__.Test object at 0x0225C3E8>, <__main__.Test object at 0x0225C418>]]
[['t1', 't2', 't3', 't4', 't5', 't6']]
redo list [[<__main__.Test object at 0x0225C3D0>, <__main__.Test object at 0x0225C298>, <__main__.Test object at 0x0225C358>, <__main__.Test object at 0x0225C388>, <__main__.Test object at 0x0225C3E8>, <__main__.Test object at 0x0225C418>], [<__main__.Test object at 0x0225C3D0>, <__main__.Test object at 0x0225C298>, <__main__.Test object at 0x0225C358>, <__main__.Test object at 0x0225C388>, <__main__.Test object at 0x0225C3E8>, <__main__.Test object at 0x0225C418>]]
[['t1', 't2', 't3', 't4', 't5', 't6'], ['t1', 't2', 't3', 't4', 't5', 't6']]
------------------------------------

------------first redo------------
list  [<__main__.Test object at 0x0225C3D0>, <__main__.Test object at 0x0225C298>, <__main__.Test object at 0x0225C358>, <__main__.Test object at 0x0225C388>, <__main__.Test object at 0x0225C3E8>, <__main__.Test object at 0x0225C418>]
['t1', 't2', 't3', 't4', 't5', 't6']
undo list [[<__main__.Test object at 0x0225C3D0>, <__main__.Test object at 0x0225C298>, <__main__.Test object at 0x0225C358>, <__main__.Test object at 0x0225C388>, <__main__.Test object at 0x0225C3E8>, <__main__.Test object at 0x0225C418>], [<__main__.Test object at 0x0225C3D0>, <__main__.Test object at 0x0225C298>, <__main__.Test object at 0x0225C358>, <__main__.Test object at 0x0225C388>, <__main__.Test object at 0x0225C3E8>, <__main__.Test object at 0x0225C418>]]
[['t1', 't2', 't3', 't4', 't5', 't6'], ['t1', 't2', 't3', 't4', 't5', 't6']]
redo list [[<__main__.Test object at 0x0225C3D0>, <__main__.Test object at 0x0225C298>, <__main__.Test object at 0x0225C358>, <__main__.Test object at 0x0225C388>, <__main__.Test object at 0x0225C3E8>, <__main__.Test object at 0x0225C418>]]
[['t1', 't2', 't3', 't4', 't5', 't6']]
------------------------------------

------------second redo------------
list  [<__main__.Test object at 0x0225C3D0>, <__main__.Test object at 0x0225C298>, <__main__.Test object at 0x0225C358>, <__main__.Test object at 0x0225C388>, <__main__.Test object at 0x0225C3E8>, <__main__.Test object at 0x0225C418>]
['t1', 't2', 't3', 't4', 't5', 't6']
undo list [[<__main__.Test object at 0x0225C3D0>, <__main__.Test object at 0x0225C298>, <__main__.Test object at 0x0225C358>, <__main__.Test object at 0x0225C388>, <__main__.Test object at 0x0225C3E8>, <__main__.Test object at 0x0225C418>], [<__main__.Test object at 0x0225C3D0>, <__main__.Test object at 0x0225C298>, <__main__.Test object at 0x0225C358>, <__main__.Test object at 0x0225C388>, <__main__.Test object at 0x0225C3E8>, <__main__.Test object at 0x0225C418>], [<__main__.Test object at 0x0225C3D0>, <__main__.Test object at 0x0225C298>, <__main__.Test object at 0x0225C358>, <__main__.Test object at 0x0225C388>, <__main__.Test object at 0x0225C3E8>, <__main__.Test object at 0x0225C418>]]
[['t1', 't2', 't3', 't4', 't5', 't6'], ['t1', 't2', 't3', 't4', 't5', 't6'], ['t1', 't2', 't3', 't4', 't5', 't6']]
redo list []
[]
------------------------------------

------------third redo------------
list  [<__main__.Test object at 0x0225C3D0>, <__main__.Test object at 0x0225C298>, <__main__.Test object at 0x0225C358>, <__main__.Test object at 0x0225C388>, <__main__.Test object at 0x0225C3E8>, <__main__.Test object at 0x0225C418>]
['t1', 't2', 't3', 't4', 't5', 't6']
undo list [[<__main__.Test object at 0x0225C3D0>, <__main__.Test object at 0x0225C298>, <__main__.Test object at 0x0225C358>, <__main__.Test object at 0x0225C388>, <__main__.Test object at 0x0225C3E8>, <__main__.Test object at 0x0225C418>], [<__main__.Test object at 0x0225C3D0>, <__main__.Test object at 0x0225C298>, <__main__.Test object at 0x0225C358>, <__main__.Test object at 0x0225C388>, <__main__.Test object at 0x0225C3E8>, <__main__.Test object at 0x0225C418>], [<__main__.Test object at 0x0225C3D0>, <__main__.Test object at 0x0225C298>, <__main__.Test object at 0x0225C358>, <__main__.Test object at 0x0225C388>, <__main__.Test object at 0x0225C3E8>, <__main__.Test object at 0x0225C418>]]
[['t1', 't2', 't3', 't4', 't5', 't6'], ['t1', 't2', 't3', 't4', 't5', 't6'], ['t1', 't2', 't3', 't4', 't5', 't6']]
redo list []
[]
------------------------------------

------------Changing name 1------------
list  [<__main__.Test object at 0x0225C3D0>, <__main__.Test object at 0x0225C298>, <__main__.Test object at 0x0225C358>, <__main__.Test object at 0x0225C388>, <__main__.Test object at 0x0225C3E8>, <__main__.Test object at 0x0225C418>]
['t1', 'Name 1', 't3', 't4', 't5', 't6']
undo list [[<__main__.Test object at 0x0225C3D0>, <__main__.Test object at 0x0225C298>, <__main__.Test object at 0x0225C358>, <__main__.Test object at 0x0225C388>, <__main__.Test object at 0x0225C3E8>, <__main__.Test object at 0x0225C418>], [<__main__.Test object at 0x0225C3D0>, <__main__.Test object at 0x0225C298>, <__main__.Test object at 0x0225C358>, <__main__.Test object at 0x0225C388>, <__main__.Test object at 0x0225C3E8>, <__main__.Test object at 0x0225C418>], [<__main__.Test object at 0x0225C3D0>, <__main__.Test object at 0x0225C298>, <__main__.Test object at 0x0225C358>, <__main__.Test object at 0x0225C388>, <__main__.Test object at 0x0225C3E8>, <__main__.Test object at 0x0225C418>], [<__main__.Test object at 0x0225C3D0>, <__main__.Test object at 0x0225C298>, <__main__.Test object at 0x0225C358>, <__main__.Test object at 0x0225C388>, <__main__.Test object at 0x0225C3E8>, <__main__.Test object at 0x0225C418>]]
[['t1', 'Name 1', 't3', 't4', 't5', 't6'], ['t1', 'Name 1', 't3', 't4', 't5', 't6'], ['t1', 'Name 1', 't3', 't4', 't5', 't6'], ['t1', 'Name 1', 't3', 't4', 't5', 't6']]
redo list []
[]
------------------------------------
------------------------------------
Changing name 2
list  [<__main__.Test object at 0x0225C3D0>, <__main__.Test object at 0x0225C298>, <__main__.Test object at 0x0225C358>, <__main__.Test object at 0x0225C388>, <__main__.Test object at 0x0225C3E8>, <__main__.Test object at 0x0225C418>]
['t1', 'Name 2', 't3', 't4', 't5', 't6']
undo list [[<__main__.Test object at 0x0225C3D0>, <__main__.Test object at 0x0225C298>, <__main__.Test object at 0x0225C358>, <__main__.Test object at 0x0225C388>, <__main__.Test object at 0x0225C3E8>, <__main__.Test object at 0x0225C418>], [<__main__.Test object at 0x0225C3D0>, <__main__.Test object at 0x0225C298>, <__main__.Test object at 0x0225C358>, <__main__.Test object at 0x0225C388>, <__main__.Test object at 0x0225C3E8>, <__main__.Test object at 0x0225C418>], [<__main__.Test object at 0x0225C3D0>, <__main__.Test object at 0x0225C298>, <__main__.Test object at 0x0225C358>, <__main__.Test object at 0x0225C388>, <__main__.Test object at 0x0225C3E8>, <__main__.Test object at 0x0225C418>], [<__main__.Test object at 0x0225C3D0>, <__main__.Test object at 0x0225C298>, <__main__.Test object at 0x0225C358>, <__main__.Test object at 0x0225C388>, <__main__.Test object at 0x0225C3E8>, <__main__.Test object at 0x0225C418>], [<__main__.Test object at 0x0225C3D0>, <__main__.Test object at 0x0225C298>, <__main__.Test object at 0x0225C358>, <__main__.Test object at 0x0225C388>, <__main__.Test object at 0x0225C3E8>, <__main__.Test object at 0x0225C418>]]
[['t1', 'Name 2', 't3', 't4', 't5', 't6'], ['t1', 'Name 2', 't3', 't4', 't5', 't6'], ['t1', 'Name 2', 't3', 't4', 't5', 't6'], ['t1', 'Name 2', 't3', 't4', 't5', 't6'], ['t1', 'Name 2', 't3', 't4', 't5', 't6']]
redo list []
[]
------------------------------------

------------first undo------------
list  [<__main__.Test object at 0x0225C3D0>, <__main__.Test object at 0x0225C298>, <__main__.Test object at 0x0225C358>, <__main__.Test object at 0x0225C388>, <__main__.Test object at 0x0225C3E8>, <__main__.Test object at 0x0225C418>]
['t1', 'Name 2', 't3', 't4', 't5', 't6']
undo list [[<__main__.Test object at 0x0225C3D0>, <__main__.Test object at 0x0225C298>, <__main__.Test object at 0x0225C358>, <__main__.Test object at 0x0225C388>, <__main__.Test object at 0x0225C3E8>, <__main__.Test object at 0x0225C418>], [<__main__.Test object at 0x0225C3D0>, <__main__.Test object at 0x0225C298>, <__main__.Test object at 0x0225C358>, <__main__.Test object at 0x0225C388>, <__main__.Test object at 0x0225C3E8>, <__main__.Test object at 0x0225C418>], [<__main__.Test object at 0x0225C3D0>, <__main__.Test object at 0x0225C298>, <__main__.Test object at 0x0225C358>, <__main__.Test object at 0x0225C388>, <__main__.Test object at 0x0225C3E8>, <__main__.Test object at 0x0225C418>], [<__main__.Test object at 0x0225C3D0>, <__main__.Test object at 0x0225C298>, <__main__.Test object at 0x0225C358>, <__main__.Test object at 0x0225C388>, <__main__.Test object at 0x0225C3E8>, <__main__.Test object at 0x0225C418>]]
[['t1', 'Name 2', 't3', 't4', 't5', 't6'], ['t1', 'Name 2', 't3', 't4', 't5', 't6'], ['t1', 'Name 2', 't3', 't4', 't5', 't6'], ['t1', 'Name 2', 't3', 't4', 't5', 't6']]
redo list [[<__main__.Test object at 0x0225C3D0>, <__main__.Test object at 0x0225C298>, <__main__.Test object at 0x0225C358>, <__main__.Test object at 0x0225C388>, <__main__.Test object at 0x0225C3E8>, <__main__.Test object at 0x0225C418>]]
[['t1', 'Name 2', 't3', 't4', 't5', 't6']]
------------------------------------

------------second undo------------
list  [<__main__.Test object at 0x0225C3D0>, <__main__.Test object at 0x0225C298>, <__main__.Test object at 0x0225C358>, <__main__.Test object at 0x0225C388>, <__main__.Test object at 0x0225C3E8>, <__main__.Test object at 0x0225C418>]
['t1', 'Name 2', 't3', 't4', 't5', 't6']
undo list [[<__main__.Test object at 0x0225C3D0>, <__main__.Test object at 0x0225C298>, <__main__.Test object at 0x0225C358>, <__main__.Test object at 0x0225C388>, <__main__.Test object at 0x0225C3E8>, <__main__.Test object at 0x0225C418>], [<__main__.Test object at 0x0225C3D0>, <__main__.Test object at 0x0225C298>, <__main__.Test object at 0x0225C358>, <__main__.Test object at 0x0225C388>, <__main__.Test object at 0x0225C3E8>, <__main__.Test object at 0x0225C418>], [<__main__.Test object at 0x0225C3D0>, <__main__.Test object at 0x0225C298>, <__main__.Test object at 0x0225C358>, <__main__.Test object at 0x0225C388>, <__main__.Test object at 0x0225C3E8>, <__main__.Test object at 0x0225C418>]]
[['t1', 'Name 2', 't3', 't4', 't5', 't6'], ['t1', 'Name 2', 't3', 't4', 't5', 't6'], ['t1', 'Name 2', 't3', 't4', 't5', 't6']]
redo list [[<__main__.Test object at 0x0225C3D0>, <__main__.Test object at 0x0225C298>, <__main__.Test object at 0x0225C358>, <__main__.Test object at 0x0225C388>, <__main__.Test object at 0x0225C3E8>, <__main__.Test object at 0x0225C418>], [<__main__.Test object at 0x0225C3D0>, <__main__.Test object at 0x0225C298>, <__main__.Test object at 0x0225C358>, <__main__.Test object at 0x0225C388>, <__main__.Test object at 0x0225C3E8>, <__main__.Test object at 0x0225C418>]]
[['t1', 'Name 2', 't3', 't4', 't5', 't6'], ['t1', 'Name 2', 't3', 't4', 't5', 't6']]
------------------------------------
```


The solution was simple, import a python library to make a deep copy:

```shell
import copy
```
