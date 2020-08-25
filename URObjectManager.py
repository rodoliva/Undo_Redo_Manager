import copy

class UndoRedoManager(object):

    def __init__(self, li):
        self.undo_list = []
        self.undo_list.append(self.clone_li(li))
        self.redo_list = []

    def push_undo_command(self, action):
        """Push the given command to the undo command stack."""
        self.undo_list.append(action)

    def pop_undo_command(self):
        """Remove the last command from the undo command stack and return it."""
        if not len(self.undo_list) <= 1:
            last_undo = self.undo_list.pop()
            return last_undo

    def push_redo_command(self, action):
        """Push the given command to the redo command stack."""
        self.redo_list.append(action)

    def pop_redo_command(self):
        """Remove the last command from the redo command stack and return it."""
        if not len(self.redo_list) == 0:
            last_redo = self.redo_list.pop()
            return last_redo

    def do_new_action(self, action):
        """Use this function for each action, clear redo with every new command and add new element"""
        self.redo_list = []
        #clone_li, clone the given list and make new instances for every object in the list
        self.push_undo_command(self.clone_li(action))

    def undo(self):
        """Undo the last commands"""
        if not len(self.undo_list) <= 1:
            action = self.pop_undo_command()
            self.push_redo_command(action)
            return self.clone_li(self.undo_list[len(self.undo_list) - 1])
            #Return a cloned new list
        else:
            return self.clone_li(self.undo_list[0])

    def redo(self):
        """Redo the last n commands which have been undone using the undo method."""
        if not len(self.redo_list) == 0:
            action = self.pop_redo_command()
            self.push_undo_command(action)
            # Return a cloned new list
            return self.clone_li(action)
        else:
            return self.clone_li(self.undo_list[len(self.undo_list) - 1])

    def clone_li(self, li):
        """Clone the object in a list and make differents instances of each object"""
        auxli = []
        if not li == []:
            copyli = copy.deepcopy(li)
            for obj in copyli:
                auxli.append(copy.deepcopy(obj))
            return auxli

    def print_list(self, urli):
        """Only to print the tests"""
        newli1 = []
        for li in urli:
            newli2 = []
            for obj in li:
                newli2.append(obj.name)
            newli1.append(newli2)
        print(newli1)

        
class Test():
    
    def __init__(self, name):
        self.name = name


t1 = Test('t1')
t2 = Test('t2')
t3 = Test('t3')
t4 = Test('t4')
t5 = Test('t5')
t6 = Test('t6')

li = [t1,t2,t3,t4]

def print_list(li):
    newli = []
    for obj in li:
        newli.append(obj.name)
    print(newli)

manager = UndoRedoManager(li)


print('------------------------------------')
print('first add')
li.append(t5)
manager.do_new_action(li)
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
manager.do_new_action(li)
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
manager.do_new_action(li)
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
manager.do_new_action(li)
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

