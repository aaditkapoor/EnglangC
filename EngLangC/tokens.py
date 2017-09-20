__author__ = "Aadit Kapoor"
__version__ = "EngLangc ver1.0"
__copyright__ = "EngLangc ver1.0 (c) Aadit Kapoor 2017"


# This file contains all the tokens
__START__ = "start"
__STOP__ = "stop"
__PRINT__ = "print"
__COMMAND__ = "command"

__RECOGNIZED_TOKENS = ["program", "programs", "write", "how", "why"]


def get_version():
    return __version__

def get_author():
    return __author__


ERROR_CODES = {001: "EngLangc ver1.0 [**ERROR**] : File not found.",
               002:"EngLangc ver1.0 [**ERROR**] : Unable to parse.",
               003:"EngLangc ver1.0 [**ERROR**] : Inavlid token.",
               004: "EngLangc ver1.0 (c) [**ERROR**] : File must end with .egl"}

SUCCESS_CODES = {1: "EngLangc ver1.0: Opening file complete.",
                 2: "EngLangc ver1.0: Getting content complete.",
                 3: "EngLangc ver1.0: Parsing done.",
                 4: "EngLangc ver1.0: Process completed.",
                 5: "EngLangc ver1.0: Thanks for using"}
