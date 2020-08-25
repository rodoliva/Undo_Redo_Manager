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

    def print_list(self, urli):
        #Only to print the tests
        newli1 = []
        for li in urli:
            newli2 = []
            for obj in li:
                newli2.append(obj.name)
            newli1.append(newli2)
        print(newli1)


li = [5,6,7,8]


manager = UndoRedoManager(li.copy())

li.append(1)
manager.new_action(li.copy())
print('first add')
print('list ', li)
print('undo list', manager.undo_list)
print('redo list', manager.redo_list)
print('')

li.append(2)
manager.new_action(li)
print('second add')
print('list ', li)
print('undo list', manager.undo_list)
print('redo list', manager.redo_list)
print('')

li = manager.undo()
print('first undo')
print('list ', li)
print('undo list', manager.undo_list)
print('redo list', manager.redo_list)
print('')

li = manager.undo()
print('second undo')
print('list ', li)
print('undo list', manager.undo_list)
print('redo list', manager.redo_list)
print('')

li = manager.undo()
print('third undo')
print('list ', li)
print('undo list', manager.undo_list)
print('redo list', manager.redo_list)
print('')

li = manager.redo()
print('first redo')
print('list ', li)
print('undo list', manager.undo_list)
print('redo list', manager.redo_list)
print('')

li = manager.redo()
print('second redo')
print('list ', li)
print('undo list', manager.undo_list)
print('redo list', manager.redo_list)
print('')

li = manager.redo()
print('third redo')
print('list ', li)
print('undo list', manager.undo_list)
print('redo list', manager.redo_list)
print('')


print('------------Object list Test-------------')

class Test():

    def __init__(self, name):
        self.name = name


t1 = Test('t1')
t2 = Test('t2')
t3 = Test('t3')
t4 = Test('t4')
t5 = Test('t5')
t6 = Test('t6')

li = [t1, t2, t3, t4]


def print_list(li):
    newli = []
    for obj in li:
        newli.append(obj.name)
    print(newli)

manager = UndoRedoManager(li)

print('------------------------------------')
print('first add')
li.append(t5)
manager.new_action(li)
print('list ', li)
print_list(li)
print('undo list', manager.undo_list)
manager.print_list(manager.undo_list)
print('redo list', manager.redo_list)
manager.print_list(manager.redo_list)
print('------------------------------------')

print('------------------------------------')
print('second add')
li.append(t6)
manager.new_action(li)
print('list ', li)
print_list(li)
print('undo list', manager.undo_list)
manager.print_list(manager.undo_list)
print('redo list', manager.redo_list)
manager.print_list(manager.redo_list)
print('------------------------------------')

print('------------------------------------')
print('first undo')
li = manager.undo()
print('list ', li)
print_list(li)
print('undo list', manager.undo_list)
manager.print_list(manager.undo_list)
print('redo list', manager.redo_list)
manager.print_list(manager.redo_list)
print('------------------------------------')

print('------------------------------------')
print('second undo')
li = manager.undo()
print('list ', li)
print_list(li)
print('undo list', manager.undo_list)
manager.print_list(manager.undo_list)
print('redo list', manager.redo_list)
manager.print_list(manager.redo_list)
print('------------------------------------')

print('------------------------------------')
print('third undo')
li = manager.undo()
print('list ', li)
print_list(li)
print('undo list', manager.undo_list)
manager.print_list(manager.undo_list)
print('redo list', manager.redo_list)
manager.print_list(manager.redo_list)
print('------------------------------------')

print('------------------------------------')
print('first redo')
li = manager.redo()
print('list ', li)
print_list(li)
print('undo list', manager.undo_list)
manager.print_list(manager.undo_list)
print('redo list', manager.redo_list)
manager.print_list(manager.redo_list)
print('------------------------------------')

print('------------------------------------')
print('second redo')
li = manager.redo()
print('list ', li)
print_list(li)
print('undo list', manager.undo_list)
manager.print_list(manager.undo_list)
print('redo list', manager.redo_list)
manager.print_list(manager.redo_list)
print('------------------------------------')

print('------------------------------------')
print('third redo')
li = manager.redo()
print('list ', li)
print_list(li)
print('undo list', manager.undo_list)
manager.print_list(manager.undo_list)
print('redo list', manager.redo_list)
manager.print_list(manager.redo_list)
print('------------------------------------')

print('------------------------------------')
print('Changing name 1')
li[1].name = 'Name 1'
manager.new_action(li)
print('list ', li)
print_list(li)
print('undo list', manager.undo_list)
manager.print_list(manager.undo_list)
print('redo list', manager.redo_list)
manager.print_list(manager.redo_list)
print('------------------------------------')

print('------------------------------------')
print('Changing name 2')
li[1].name = 'Name 2'
manager.new_action(li)
print('list ', li)
print_list(li)
print('undo list', manager.undo_list)
manager.print_list(manager.undo_list)
print('redo list', manager.redo_list)
manager.print_list(manager.redo_list)
print('------------------------------------')

print('------------------------------------')
print('first undo')
li = manager.undo()
print('list ', li)
print_list(li)
print('undo list', manager.undo_list)
manager.print_list(manager.undo_list)
print('redo list', manager.redo_list)
manager.print_list(manager.redo_list)
print('------------------------------------')

print('------------------------------------')
print('second undo')
li = manager.undo()
print('list ', li)
print_list(li)
print('undo list', manager.undo_list)
manager.print_list(manager.undo_list)
print('redo list', manager.redo_list)
manager.print_list(manager.redo_list)
print('------------------------------------')


