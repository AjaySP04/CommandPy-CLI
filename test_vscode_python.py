#!/usr/bin/env python
import os
import time
"""
Boiler plate code for python coding standard.

created by - Ajay Singh Parmar
dated - September 06, 2019 
"""
#-----------------------------------------------------------#
#                     Application Constants                 #                  
#-----------------------------------------------------------#
TERMINAL_PROMPT = ">>> "                                    #
COMMAND_PREFIX = 'command'                                  #
COMMAND_LIST = ['run', 'create', 'fetch', 'count', 'exit']  #
#-----------------------------------------------------------#

class TestVSCode:
    """"""
    static_counter_variable = 0

    def __init__(self, class_variable=None):
        """"""
        self.class_variable = class_variable
        TestVSCode.static_counter_variable = TestVSCode.static_counter_variable + 1
    
    def get_class_variable(self):
        """"""
        return self.class_variable

    @staticmethod
    def get_static_counter_variable():
        """"""
        return TestVSCode.static_counter_variable

    def __str__(self):
        """"""
        return "Class variable is {}".format(get_class_variable())
    pass


def test_vscode(command=''):
    """"""
    if (command=='run'):
        #print("<<test_vscode>> Reached run command.")
        tvsc = TestVSCode(class_variable="cv")
        print(tvsc)
    elif (command=='create'):
        #print("<<test_vscode>> Reached create command.")
        tvsc = TestVSCode(class_variable="cv")
    elif (command=='fetch'):
        #print("<<test_vscode>> Reached fetch command.")
        tvsc = TestVSCode(class_variable="cv")
        print(tvsc.get_class_variable())
    elif (command=='count'):
        print("<<test_vscode>> Reached count command.")
        print(TestVSCode.get_static_counter_variable())
    else:
        print("<<test_vscode>> Bad Command Input.")


def main():
    #print("<<main>> Entry point for module run as main.")
    print('''
    *******************************************
      /\_/\       |^^^^^^^^^^^^^^^^^|
      (o_o)  -----|  Programming    |
    {[  I  ]}     |  Command <type> |
     [ <3  ]      |_________________|
      \/-\/
    *******************************************
    ''')
    print("Enter command as 'command <type of command>' when prompted")

    time.sleep(2)
    exit_command = False
    
    try:
        while (not exit_command):
            input_command = str(raw_input(TERMINAL_PROMPT)).strip()
            command_tokens_list = input_command.split()

            #: handle command prefix.
            if command_tokens_list[0] != COMMAND_PREFIX:
                print("Unrecognised '{0}' command input".format(command_tokens_list[0]))
                continue
            
            #: handle actual command action.
            if len(command_tokens_list) > 1:
                if command_tokens_list[1] not in COMMAND_LIST:
                    print("Unrecognised '{0}' command input".format(command_tokens_list[1]))
            elif len(command_tokens_list) == 1:
                print("Incomplete Command")
                continue
                
            #: handle exit command.
            if command_tokens_list[1] == 'exit':
                exit_command = True
                break
            elif command_tokens_list[1] == 'quit' or command_tokens_list[1] == 'exit()' or command_tokens_list[1] == 'quit()':
                print("To exit the terminal type 'command exit'")
                continue

            #: handle run command
            if command_tokens_list[1] in COMMAND_LIST:
                test_vscode(command=command_tokens_list[1])
                continue
    except Exception as err:
        print("Error occured, message : {0}".format(err))
    finally:
        print("Leaving gently, bye bye!")   


if __name__=='__main__':
    main()
