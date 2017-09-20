"""
        Source code for EngLang Programming Language

        Structure
        ==========================================

        tokens.py => Contains all the tokens for language execution
        More to be added...
"""

import tokens
import os


class EngLang:
    def __init__(self, program="start"):
        if program == "stop":
            exit(0)
        else:
            print
    def main(self):
       
        print
        print "Type 'compile:<FILE_NAME> (Note: FILE_NAME should be on path)"
        command = raw_input("EngLang:> ")

        compile_command = command.split(":")
        print compile_command
        if "compile" in compile_command:
            if ".egl" in compile_command[1]:
                self.source=compile_command[1]
                print "EngLangc ver1.0 : Found the file."
            else:
                print tokens.ERROR_CODES[004]
        else:
            print "EngLangc ver1.0 : Invalid command"

        print "ENGLANG PROCESSING DONE"
                

    def get_contents(self):
        try:
            parser = open(self.source_file, "r+")
            print tokens.SUCCESS_CODES[1]
        except:
            print tokens.ERROR_CODES[001]
            exit(0)

        # Parser object found! Now parsing
        code_lines = []
        for i in parser.readlines():
            code_lines.append(i)

        if tokens.__START__ in code_lines:
            if tokens.__STOP__ in code_lines:
                print tokens.SUCCESS_CODES[2]

                self.code_lines = code_lines

                self.parse_code()



    
    def parse_code(self):
        print self.code_lines

main = EngLang()

os.system("cls")

print tokens.__copyright__
while True:
    main.main()
    print 
