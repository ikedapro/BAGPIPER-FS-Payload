import sys
import time

import payload

class RadioParser():
    received = False
    cmd_lst = []
    def __init__(self):
        print("radio parser initiated")
        
    def receive(self):
        '''
        Received the commands by listening to radio
        Once commands received and verified will set received to true and update commands list
        '''
        self.cmd_lst = ["A1", "B2", "C3", "D4", "E5", "F6", "G7", "H8"]
        
    # def commands(self):
    #     cmds = ["A1", "B2", "C3", "D4", "E5", "F6", "G7", "H8"]
    #     for cmd in cmds:
    #         yield cmd