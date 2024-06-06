from contextlib import contextmanager
import os

f=open('sample.txt', 'w')
f.write("helo world")
f.close()

with open('sample.txt', 'w') as f:
    f.write("hello python")

#custom class context manager

class OpenFile:
    def __init__(self, file_name: str, mode: str):
        self.file_name = file_name
        self.mode = mode

    def __enter__(self):
        self.file = open(self.file_name, self.mode)
        return self.file
        
    
    def __exit__(self, exec_type, exec_value, callback):
        self.file.close()

with OpenFile("sample.txt", 'w') as f:
    f.write("hello ruby")

#custom function context manager
    

@contextmanager
def OpenFile(file_name, mode):
    file = open(file_name, mode)
    yield file
    file.close()

with OpenFile("sample.txt", "w") as f:
    f.write("hello helloooo")
    print(f.close())


#try-finaly
    
cwd = os.getcwd()
os.chdir('strawberry-demo')
print(os.listdir())
os.chdir(cwd)



@contextmanager
def change_directory(directory):
    try:
        cwd = os.getcwd()
        os.chdir(directory)
        yield
    finally:
        os.chdir(cwd)

with change_directory("strawberry-demo") as c:
    print(os.listdir())
        
        
