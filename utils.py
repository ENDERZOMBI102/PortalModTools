from os import system, name
def clear():
      r"""
      a function that clears the console
      """
      # for windows
      if name == 'nt':
            _ = system('cls')

      # for mac and linux(here, os.name is 'posix')
      else:
            _ = system('clear')
