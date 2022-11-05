from dataclasses import dataclass

def execute_command(command):
    match command:
        case 'dir':
            print('Listing files')
        case 'cd':
            print('Changing directory')
        case _: #Não obrigatório
            print('command not implemented')
            
            
def execute_command2(command):
    match command.split():
        case ['dir', *dirs, '--force']:
            for dir in dirs:
                print('Listing files forced', dir)
                
        case ['dir', *dirs]:
            for dir in dirs:
                print('Listing files', dir)
                
        case ['cd', path, *args]:
            print('Changing directory to', path)
            
        case _: #Não obrigatório
            print('command not implemented')  
            
            
def execute_command3(command):
    match command.split():
        case ['dir' | 'directory', *dirs]:
            for dir in dirs:
                print('cd:\ Listing files', dir)
        
        case ['cd' | 'change', path]:
            print('cd:\ Changing directory to', path)
            
        case _: #Não obrigatório
            print('cd:\ command not implemented')  
        
        
def execute_command4(command):
    match command.split():
        case ['dir' | 'directory' as the_command, *dirs] as the_list if len(dirs) > 1:
            for dir in dirs:
                print('cd:\ listing ALL dirs from: ', dir)
            print(f'{the_command=}, {the_list=}')
                
        case ['dir' | 'directory', *dirs] if len(dirs) <= 1:
            print('cd:\ listing ONE directory from:', dirs[0])
            
        case ['cd', path]:
            print('cd:\ changing directory to:', path)
            
        case _: #Não obrigatório
            print('cd:\ command not implemented') 
            

def execute_command5(command):
    match command:
        
        case {'command': 'ls', 'directories': [_, *_]}:
            for directory in command['directories']:
                print('cd:\ Listing all directories from', directory)
                
        case _: #Não obrigatório
            print('cd:\ command not implemented') 
            
    

            


#execute_command5({'command': 'ls', 'directories': ['/users']})

@dataclass
class Command:
    command: str
    directories: list[str]
    
def execute_command6(command: Command):
    match command:
        case Command(command='dir', directories=[_, *_]):
            for directory in command.directories:
                print('cd:\ listing ALL directories from', directory)
                
        case Command(command='cd', directories=[_, *_]):
            for directory in command.directories:
                print('cd:\ changing to', directory)
                
        case _: #Não obrigatório
            print('cd:\ command not implemented')


execute_command6(Command('dir', ['/users']))
execute_command6(Command('cd', ['/users']))          