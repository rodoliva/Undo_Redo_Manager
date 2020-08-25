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


Here comes the disaster ... all the same and when changing a variable, it's the same:


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

```python
import copy
```

With this method, it's possible to copy and create a new instance of the list, and also a new instance of each object within the list.

```python
def clone_li(self, li):
    """Clone the object in a list and make differents
    instances of each object"""
    auxli = []
    if not li == []:
        copyli = copy.deepcopy(li)
        for obj in copyli:
            auxli.append(copy.deepcopy(obj))
        return auxli
```

The new code:

```python
import copy

class UndoRedoManager(object):

    def __init__(self, li):
        self.undo_list = []
        self.undo_list.append(self.clone_li(li))
        self.redo_list = []

    def add_undo(self, action):
        #Add the action to the undo list.
        self.undo_list.append(action)

    def add_redo(self, action):
        #Add the action to the redo list
        self.redo_list.append(action)

    def delete_undo(self):
        # Remove the last action from the undo list and return it
        if not len(self.undo_list) <= 1:
            last_undo = self.undo_list.pop()
            return last_undo

    def delete_redo(self):
        #Remove the last action from the redo list and return it
        if not len(self.redo_list) == 0:
            last_redo = self.redo_list.pop()
            return last_redo

    def do_new_action(self, action):
        """Use this function for each action.
        This clear redo list with every new action and
        add new element in the undo list"""
        self.redo_list = []
        self.add_undo(self.clone_li(action))

    def undo(self):
        #Undo the last actions
        if not len(self.undo_list) <= 1:
            action = self.delete_undo()
            self.add_redo(action)
            return self.clone_li(self.undo_list[len(self.undo_list) - 1])
            #Return a cloned new list
        else:
            return self.clone_li(self.undo_list[0])

    def redo(self):
        #Redo the last actions
        if not len(self.redo_list) == 0:
            action = self.delete_redo()
            self.add_undo(action)
            # Return a cloned new list
            return self.clone_li(action)
        else:
            return self.clone_li(self.undo_list[len(self.undo_list) - 1])

    def clone_li(self, li):
        """Clone the object in a list and make differents
        instances of each object"""
        auxli = []
        if not li == []:
            copyli = copy.deepcopy(li)
            for obj in copyli:
                auxli.append(copy.deepcopy(obj))
            return auxli
```


And finally the results


```shell
------------Object list Test------------
list  [<__main__.Test object at 0x01AFF4F0>, <__main__.Test object at 0x01CBC268>, <__main__.Test object at 0x01CBC3B8>, <__main__.Test object at 0x01CBC2F8>]
['t1', 't2', 't3', 't4']
------------------------------------

------------first add------------
list  [<__main__.Test object at 0x01AFF4F0>, <__main__.Test object at 0x01CBC268>, <__main__.Test object at 0x01CBC3B8>, <__main__.Test object at 0x01CBC2F8>, <__main__.Test object at 0x01CBC4A8>]
['t1', 't2', 't3', 't4', 't5']
undo list [[<__main__.Test object at 0x01E3A940>, <__main__.Test object at 0x01E3AA30>, <__main__.Test object at 0x01E3AA78>, <__main__.Test object at 0x01E3AAC0>], [<__main__.Test object at 0x01E3ABC8>, <__main__.Test object at 0x01E3AC10>, <__main__.Test object at 0x01E3AC58>, <__main__.Test object at 0x01E3ACA0>, <__main__.Test object at 0x01E3ACE8>]]
[['t1', 't2', 't3', 't4'], ['t1', 't2', 't3', 't4', 't5']]
redo list []
[]
------------------------------------

------------second add------------
list  [<__main__.Test object at 0x01AFF4F0>, <__main__.Test object at 0x01CBC268>, <__main__.Test object at 0x01CBC3B8>, <__main__.Test object at 0x01CBC2F8>, <__main__.Test object at 0x01CBC4A8>, <__main__.Test object at 0x01CBC4D8>]
['t1', 't2', 't3', 't4', 't5', 't6']
undo list [[<__main__.Test object at 0x01E3A940>, <__main__.Test object at 0x01E3AA30>, <__main__.Test object at 0x01E3AA78>, <__main__.Test object at 0x01E3AAC0>], [<__main__.Test object at 0x01E3ABC8>, <__main__.Test object at 0x01E3AC10>, <__main__.Test object at 0x01E3AC58>, <__main__.Test object at 0x01E3ACA0>, <__main__.Test object at 0x01E3ACE8>], [<__main__.Test object at 0x01E3ADF0>, <__main__.Test object at 0x01E3AE38>, <__main__.Test object at 0x01E3AE80>, <__main__.Test object at 0x01E3AEC8>, <__main__.Test object at 0x01E3AF10>, <__main__.Test object at 0x01E3AF58>]]
[['t1', 't2', 't3', 't4'], ['t1', 't2', 't3', 't4', 't5'], ['t1', 't2', 't3', 't4', 't5', 't6']]
redo list []
[]
------------------------------------

------------first undo------------
list  [<__main__.Test object at 0x01E3AFE8>, <__main__.Test object at 0x01E4E058>, <__main__.Test object at 0x01E4E0A0>, <__main__.Test object at 0x01E4E0E8>, <__main__.Test object at 0x01E4E130>]
['t1', 't2', 't3', 't4', 't5']
undo list [[<__main__.Test object at 0x01E3A940>, <__main__.Test object at 0x01E3AA30>, <__main__.Test object at 0x01E3AA78>, <__main__.Test object at 0x01E3AAC0>], [<__main__.Test object at 0x01E3ABC8>, <__main__.Test object at 0x01E3AC10>, <__main__.Test object at 0x01E3AC58>, <__main__.Test object at 0x01E3ACA0>, <__main__.Test object at 0x01E3ACE8>]]
[['t1', 't2', 't3', 't4'], ['t1', 't2', 't3', 't4', 't5']]
redo list [[<__main__.Test object at 0x01E3ADF0>, <__main__.Test object at 0x01E3AE38>, <__main__.Test object at 0x01E3AE80>, <__main__.Test object at 0x01E3AEC8>, <__main__.Test object at 0x01E3AF10>, <__main__.Test object at 0x01E3AF58>]]
[['t1', 't2', 't3', 't4', 't5', 't6']]
------------------------------------

------------second undo------------
list  [<__main__.Test object at 0x01E4E1A8>, <__main__.Test object at 0x01E4E1F0>, <__main__.Test object at 0x01E4E238>, <__main__.Test object at 0x01E4E280>]
['t1', 't2', 't3', 't4']
undo list [[<__main__.Test object at 0x01E3A940>, <__main__.Test object at 0x01E3AA30>, <__main__.Test object at 0x01E3AA78>, <__main__.Test object at 0x01E3AAC0>]]
[['t1', 't2', 't3', 't4']]
redo list [[<__main__.Test object at 0x01E3ADF0>, <__main__.Test object at 0x01E3AE38>, <__main__.Test object at 0x01E3AE80>, <__main__.Test object at 0x01E3AEC8>, <__main__.Test object at 0x01E3AF10>, <__main__.Test object at 0x01E3AF58>], [<__main__.Test object at 0x01E3ABC8>, <__main__.Test object at 0x01E3AC10>, <__main__.Test object at 0x01E3AC58>, <__main__.Test object at 0x01E3ACA0>, <__main__.Test object at 0x01E3ACE8>]]
[['t1', 't2', 't3', 't4', 't5', 't6'], ['t1', 't2', 't3', 't4', 't5']]
------------------------------------

------------third undo------------
list  [<__main__.Test object at 0x01E4E100>, <__main__.Test object at 0x01E4E160>, <__main__.Test object at 0x01E4E2C8>, <__main__.Test object at 0x01E4E310>]
['t1', 't2', 't3', 't4']
undo list [[<__main__.Test object at 0x01E3A940>, <__main__.Test object at 0x01E3AA30>, <__main__.Test object at 0x01E3AA78>, <__main__.Test object at 0x01E3AAC0>]]
[['t1', 't2', 't3', 't4']]
redo list [[<__main__.Test object at 0x01E3ADF0>, <__main__.Test object at 0x01E3AE38>, <__main__.Test object at 0x01E3AE80>, <__main__.Test object at 0x01E3AEC8>, <__main__.Test object at 0x01E3AF10>, <__main__.Test object at 0x01E3AF58>], [<__main__.Test object at 0x01E3ABC8>, <__main__.Test object at 0x01E3AC10>, <__main__.Test object at 0x01E3AC58>, <__main__.Test object at 0x01E3ACA0>, <__main__.Test object at 0x01E3ACE8>]]
[['t1', 't2', 't3', 't4', 't5', 't6'], ['t1', 't2', 't3', 't4', 't5']]
------------------------------------

------------first redo------------
list  [<__main__.Test object at 0x01E4E340>, <__main__.Test object at 0x01E4E388>, <__main__.Test object at 0x01E4E3D0>, <__main__.Test object at 0x01E4E418>, <__main__.Test object at 0x01E4E460>]
['t1', 't2', 't3', 't4', 't5']
undo list [[<__main__.Test object at 0x01E3A940>, <__main__.Test object at 0x01E3AA30>, <__main__.Test object at 0x01E3AA78>, <__main__.Test object at 0x01E3AAC0>], [<__main__.Test object at 0x01E3ABC8>, <__main__.Test object at 0x01E3AC10>, <__main__.Test object at 0x01E3AC58>, <__main__.Test object at 0x01E3ACA0>, <__main__.Test object at 0x01E3ACE8>]]
[['t1', 't2', 't3', 't4'], ['t1', 't2', 't3', 't4', 't5']]
redo list [[<__main__.Test object at 0x01E3ADF0>, <__main__.Test object at 0x01E3AE38>, <__main__.Test object at 0x01E3AE80>, <__main__.Test object at 0x01E3AEC8>, <__main__.Test object at 0x01E3AF10>, <__main__.Test object at 0x01E3AF58>]]
[['t1', 't2', 't3', 't4', 't5', 't6']]
------------------------------------

------------second redo------------
list  [<__main__.Test object at 0x01E4E4A8>, <__main__.Test object at 0x01E4E4F0>, <__main__.Test object at 0x01E4E538>, <__main__.Test object at 0x01E4E580>, <__main__.Test object at 0x01E4E5C8>, <__main__.Test object at 0x01E4E610>]
['t1', 't2', 't3', 't4', 't5', 't6']
undo list [[<__main__.Test object at 0x01E3A940>, <__main__.Test object at 0x01E3AA30>, <__main__.Test object at 0x01E3AA78>, <__main__.Test object at 0x01E3AAC0>], [<__main__.Test object at 0x01E3ABC8>, <__main__.Test object at 0x01E3AC10>, <__main__.Test object at 0x01E3AC58>, <__main__.Test object at 0x01E3ACA0>, <__main__.Test object at 0x01E3ACE8>], [<__main__.Test object at 0x01E3ADF0>, <__main__.Test object at 0x01E3AE38>, <__main__.Test object at 0x01E3AE80>, <__main__.Test object at 0x01E3AEC8>, <__main__.Test object at 0x01E3AF10>, <__main__.Test object at 0x01E3AF58>]]
[['t1', 't2', 't3', 't4'], ['t1', 't2', 't3', 't4', 't5'], ['t1', 't2', 't3', 't4', 't5', 't6']]
redo list []
[]
------------------------------------

------------third redo------------
list  [<__main__.Test object at 0x01E4E058>, <__main__.Test object at 0x01E4E640>, <__main__.Test object at 0x01E4E688>, <__main__.Test object at 0x01E4E6D0>, <__main__.Test object at 0x01E4E718>, <__main__.Test object at 0x01E4E760>]
['t1', 't2', 't3', 't4', 't5', 't6']
undo list [[<__main__.Test object at 0x01E3A940>, <__main__.Test object at 0x01E3AA30>, <__main__.Test object at 0x01E3AA78>, <__main__.Test object at 0x01E3AAC0>], [<__main__.Test object at 0x01E3ABC8>, <__main__.Test object at 0x01E3AC10>, <__main__.Test object at 0x01E3AC58>, <__main__.Test object at 0x01E3ACA0>, <__main__.Test object at 0x01E3ACE8>], [<__main__.Test object at 0x01E3ADF0>, <__main__.Test object at 0x01E3AE38>, <__main__.Test object at 0x01E3AE80>, <__main__.Test object at 0x01E3AEC8>, <__main__.Test object at 0x01E3AF10>, <__main__.Test object at 0x01E3AF58>]]
[['t1', 't2', 't3', 't4'], ['t1', 't2', 't3', 't4', 't5'], ['t1', 't2', 't3', 't4', 't5', 't6']]
redo list []
[]
------------------------------------

------------Changing name 1------------
list  [<__main__.Test object at 0x01E4E058>, <__main__.Test object at 0x01E4E640>, <__main__.Test object at 0x01E4E688>, <__main__.Test object at 0x01E4E6D0>, <__main__.Test object at 0x01E4E718>, <__main__.Test object at 0x01E4E760>]
['t1', 'Name 1', 't3', 't4', 't5', 't6']
undo list [[<__main__.Test object at 0x01E3A940>, <__main__.Test object at 0x01E3AA30>, <__main__.Test object at 0x01E3AA78>, <__main__.Test object at 0x01E3AAC0>], [<__main__.Test object at 0x01E3ABC8>, <__main__.Test object at 0x01E3AC10>, <__main__.Test object at 0x01E3AC58>, <__main__.Test object at 0x01E3ACA0>, <__main__.Test object at 0x01E3ACE8>], [<__main__.Test object at 0x01E3ADF0>, <__main__.Test object at 0x01E3AE38>, <__main__.Test object at 0x01E3AE80>, <__main__.Test object at 0x01E3AEC8>, <__main__.Test object at 0x01E3AF10>, <__main__.Test object at 0x01E3AF58>], [<__main__.Test object at 0x01E4E460>, <__main__.Test object at 0x01E4E100>, <__main__.Test object at 0x01E4E7A8>, <__main__.Test object at 0x01E4E7F0>, <__main__.Test object at 0x01E4E838>, <__main__.Test object at 0x01E4E880>]]
[['t1', 't2', 't3', 't4'], ['t1', 't2', 't3', 't4', 't5'], ['t1', 't2', 't3', 't4', 't5', 't6'], ['t1', 'Name 1', 't3', 't4', 't5', 't6']]
redo list []
[]
------------------------------------

------------Changing name 2------------
list  [<__main__.Test object at 0x01E4E058>, <__main__.Test object at 0x01E4E640>, <__main__.Test object at 0x01E4E688>, <__main__.Test object at 0x01E4E6D0>, <__main__.Test object at 0x01E4E718>, <__main__.Test object at 0x01E4E760>]
['t1', 'Name 2', 't3', 't4', 't5', 't6']
undo list [[<__main__.Test object at 0x01E3A940>, <__main__.Test object at 0x01E3AA30>, <__main__.Test object at 0x01E3AA78>, <__main__.Test object at 0x01E3AAC0>], [<__main__.Test object at 0x01E3ABC8>, <__main__.Test object at 0x01E3AC10>, <__main__.Test object at 0x01E3AC58>, <__main__.Test object at 0x01E3ACA0>, <__main__.Test object at 0x01E3ACE8>], [<__main__.Test object at 0x01E3ADF0>, <__main__.Test object at 0x01E3AE38>, <__main__.Test object at 0x01E3AE80>, <__main__.Test object at 0x01E3AEC8>, <__main__.Test object at 0x01E3AF10>, <__main__.Test object at 0x01E3AF58>], [<__main__.Test object at 0x01E4E460>, <__main__.Test object at 0x01E4E100>, <__main__.Test object at 0x01E4E7A8>, <__main__.Test object at 0x01E4E7F0>, <__main__.Test object at 0x01E4E838>, <__main__.Test object at 0x01E4E880>], [<__main__.Test object at 0x01E4E958>, <__main__.Test object at 0x01E4E9A0>, <__main__.Test object at 0x01E4E9E8>, <__main__.Test object at 0x01E4EA30>, <__main__.Test object at 0x01E4EA78>, <__main__.Test object at 0x01E4EAC0>]]
[['t1', 't2', 't3', 't4'], ['t1', 't2', 't3', 't4', 't5'], ['t1', 't2', 't3', 't4', 't5', 't6'], ['t1', 'Name 1', 't3', 't4', 't5', 't6'], ['t1', 'Name 2', 't3', 't4', 't5', 't6']]
redo list []
[]
------------------------------------

------------first undo------------
list  [<__main__.Test object at 0x01E4EB98>, <__main__.Test object at 0x01E4EBE0>, <__main__.Test object at 0x01E4EC28>, <__main__.Test object at 0x01E4EC70>, <__main__.Test object at 0x01E4ECB8>, <__main__.Test object at 0x01E4ED00>]
['t1', 'Name 1', 't3', 't4', 't5', 't6']
undo list [[<__main__.Test object at 0x01E3A940>, <__main__.Test object at 0x01E3AA30>, <__main__.Test object at 0x01E3AA78>, <__main__.Test object at 0x01E3AAC0>], [<__main__.Test object at 0x01E3ABC8>, <__main__.Test object at 0x01E3AC10>, <__main__.Test object at 0x01E3AC58>, <__main__.Test object at 0x01E3ACA0>, <__main__.Test object at 0x01E3ACE8>], [<__main__.Test object at 0x01E3ADF0>, <__main__.Test object at 0x01E3AE38>, <__main__.Test object at 0x01E3AE80>, <__main__.Test object at 0x01E3AEC8>, <__main__.Test object at 0x01E3AF10>, <__main__.Test object at 0x01E3AF58>], [<__main__.Test object at 0x01E4E460>, <__main__.Test object at 0x01E4E100>, <__main__.Test object at 0x01E4E7A8>, <__main__.Test object at 0x01E4E7F0>, <__main__.Test object at 0x01E4E838>, <__main__.Test object at 0x01E4E880>]]
[['t1', 't2', 't3', 't4'], ['t1', 't2', 't3', 't4', 't5'], ['t1', 't2', 't3', 't4', 't5', 't6'], ['t1', 'Name 1', 't3', 't4', 't5', 't6']]
redo list [[<__main__.Test object at 0x01E4E958>, <__main__.Test object at 0x01E4E9A0>, <__main__.Test object at 0x01E4E9E8>, <__main__.Test object at 0x01E4EA30>, <__main__.Test object at 0x01E4EA78>, <__main__.Test object at 0x01E4EAC0>]]
[['t1', 'Name 2', 't3', 't4', 't5', 't6']]
------------------------------------

------------second undo------------
list  [<__main__.Test object at 0x01E4E8C8>, <__main__.Test object at 0x01E4EB20>, <__main__.Test object at 0x01E4ED60>, <__main__.Test object at 0x01E4EDA8>, <__main__.Test object at 0x01E4EDF0>, <__main__.Test object at 0x01E4EE38>]
['t1', 't2', 't3', 't4', 't5', 't6']
undo list [[<__main__.Test object at 0x01E3A940>, <__main__.Test object at 0x01E3AA30>, <__main__.Test object at 0x01E3AA78>, <__main__.Test object at 0x01E3AAC0>], [<__main__.Test object at 0x01E3ABC8>, <__main__.Test object at 0x01E3AC10>, <__main__.Test object at 0x01E3AC58>, <__main__.Test object at 0x01E3ACA0>, <__main__.Test object at 0x01E3ACE8>], [<__main__.Test object at 0x01E3ADF0>, <__main__.Test object at 0x01E3AE38>, <__main__.Test object at 0x01E3AE80>, <__main__.Test object at 0x01E3AEC8>, <__main__.Test object at 0x01E3AF10>, <__main__.Test object at 0x01E3AF58>]]
[['t1', 't2', 't3', 't4'], ['t1', 't2', 't3', 't4', 't5'], ['t1', 't2', 't3', 't4', 't5', 't6']]
redo list [[<__main__.Test object at 0x01E4E958>, <__main__.Test object at 0x01E4E9A0>, <__main__.Test object at 0x01E4E9E8>, <__main__.Test object at 0x01E4EA30>, <__main__.Test object at 0x01E4EA78>, <__main__.Test object at 0x01E4EAC0>], [<__main__.Test object at 0x01E4E460>, <__main__.Test object at 0x01E4E100>, <__main__.Test object at 0x01E4E7A8>, <__main__.Test object at 0x01E4E7F0>, <__main__.Test object at 0x01E4E838>, <__main__.Test object at 0x01E4E880>]]
[['t1', 'Name 2', 't3', 't4', 't5', 't6'], ['t1', 'Name 1', 't3', 't4', 't5', 't6']]
------------------------------------
```
