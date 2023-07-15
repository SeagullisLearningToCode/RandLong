#!usr/bin/python3
"""
PPPP    A   N   N DDDD    A       FFFFF RRRR    A   M   M EEEEE W   W  OOO  RRRR  K   K
P   P  A A  NN  N D   D  A A      F     R   R  A A  MM MM E     W   W O   O R   R K  K
P   P A   A N N N D   D A   A     F     R   R A   A MM MM E     W   W O   O R   R K K
PPPP  AAAAA N  NN D   D AAAAA     FFF   RRRR  AAAAA M M M EEE   W W W O   O RRRR  KK
P     A   A N   N D   D A   A     F     R R   A   A M   M E     WW WW O   O R R   K K
P     A   A N   N D   D A   A     F     R  R  A   A M   M E     WW WW O   O R  R  K  K
P     A   A N   N DDDD  A   A     F     R   R A   A M   M EEEEE W   W  OOO  R   R K   K
========================================================================================
                                                                    Version: 1.7 Angry Ailurus

Gull Framework without Pygame!
This file stores very simple functions with the sole purpose of de-bloating the Main.py file (used to be)
This file is also makes stating certain things faster and possibly easier.
"""
# ;IMPORTS---------------------------------------------------------------------------------------------------------------------
try:
    import os
    import gc
    import sys
    import subprocess
    import platform as pt
    import getpass as gp
    from importlib import util
    from datetime import *
    from random import *
    from configparser import *
except ImportError as ie:
    print(f"Can't Import module called '{ie}'\n\ttry going to the terminal or commandline and type 'pip install {ie}' <-- if pip has it in library")
    sys.exit(1)

# ;VARIABLES-------------------------------------------------------------------------------------------------------------------

# ;PANDA FRAMEWORK
GF_VERSION = "1.7 Angry Ailurus"
GF_EDITION = "Panda"
GF_FILENAME = str(__file__)
# ;Today's Date
td = date.today()
td_c_s = str(td)  # Converts the current date into a String
td_c_s_yo = td_c_s[0:4]  # Get year only
# ;Today's Time
tt = datetime.now()
# ;Paths
GF_FILE_PATH = os.path.dirname(os.path.abspath(__file__))
GF_XTN_FOLDER_PATH = f"{GF_FILE_PATH}/EXT/"

# ;FUNCTIONS-------------------------------------------------------------------------------------------------------------------

# ;============================================================================================================================
# ;PRINT BASED FUNCTIONS
# ;============================================================================================================================

def p(t=f"passed {choice(['Record Player', 'Gameboy', 'Tea'])}", **kwargs):
    """
    Make print statements faster than python's print("Hello World")

    kwargs
    --------------------
    condition(Bool) Def: None
            |_____Prints statement if refrenced Boolean is True, unless you use 'value'
    value(Bool) Def: Conditional
        |_____Defaults to True if 'condition' is passed, unless you change this argument to false

    Examples

    p("Hello World") <-- Prints "Hello World"\n
    p(cond=False, value=True) <-- Prints default value if False is True\n
    p("Hello World", cond="Tea", compare='c', value="Record Player) <-- Prints "Hello World" if Tea has Record Player is in the word Tea\n
    """
    # KWARGS
    condition = kwargs.get("cond", None)
    # CODE
    if condition is not None:
        if type(condition) is bool:
            changeCValue = kwargs.get("value", True)
        elif type(condition) is int:
            changeCValue = kwargs.get("value", 0)
        elif type(condition) is float:
            changeCValue = kwargs.get("value", float(0))
        elif type(condition) is str:
            changeCValue = kwargs.get("value", "Hello, Gull!")
    if type(condition) is bool and type(changeCValue) is bool:
        # ; e = equal
        # ; ne = not equal
        compare_int = kwargs.get("compare", "e") # ;Equals to (if condition == value)
        if compare_int == "ne":
            if condition is not changeCValue:
                print(t)
        elif condition is changeCValue:
            print(t)
    elif type(condition) is int and type(changeCValue) is int:
        # ; e = equals
        # ; gt = Greater than
        # ; gte = Greater than or Equals to
        # ; lt = Less than
        # ; lte = Less than or Equals to
        # ; ne = Not equal to
        compare_int = kwargs.get("compare", "e") # ;Equals to (if condition == value)
        if compare_int == "e":
            if condition == changeCValue:
                print(t)
        elif compare_int == "gt":
            if condition > changeCValue:
                print(t)
        elif compare_int == "gte":
            if condition >= changeCValue:
                print(t)
        elif compare_int == "lt":
            if condition < changeCValue:
                print(t)
        elif compare_int == "lte":
            if condition <= changeCValue:
                print(t)
        elif compare_int == "ne":
            if condition != changeCValue:
                print(t)
    elif type(condition) is float and type(changeCValue) is float:
        # ; e = equals
        # ; gt = Greater than
        # ; gte = Greater than or Equals to
        # ; lt = Less than
        # ; lte = Less than or Equals to
        # ; ne = Not equal to
        compare_int = kwargs.get("compare", "e") # ;Equals to (if condition == value)
        if compare_int == "e":
            if condition == changeCValue:
                print(t)
        elif compare_int == "gt":
            if condition > changeCValue:
                print(t)
        elif compare_int == "gte":
            if condition >= changeCValue:
                print(t)
        elif compare_int == "lt":
            if condition < changeCValue:
                print(t)
        elif compare_int == "lte":
            if condition <= changeCValue:
                print(t)
        elif compare_int == "ne":
            if condition != changeCValue:
                print(t)
        # ;if condition == changeCValue:
        # ;    print(t)
    elif type(condition) is str and type(changeCValue) is str:
        # ; e = equal
        # ; ne = not equal
        # ; c = contains
        compare_int = kwargs.get("compare", "e") # ;Equals to (if condition == value)
        if compare_int == "e":
            if condition == changeCValue:
                print(t)
        elif compare_int == "ne":
            if condition != changeCValue:
                print(t)
        elif compare_int == "c":
            if condition.__contains__(changeCValue):
                print(t)
    if condition is None:
        print(t)

def sps(t: str, **sargs):
    """
    Same thing as p() but adds in "passed"

    sargs is KWARGS
    --------------
    replacePassed(str) Def: None
        Commands:
            |_____"<tt>" = Includes current time when executed
    addCond(bool or int) Def: None
        conditionals:
            |____bool = if the "condition" arg is bool and that bool is set to true, then print the statement
            |____int = same as bool but if the value is greater than 1, then print the statement

    Example: sps("it")
    Output: passed it
    """
    # SARGS
    replacePassed = sargs.get("rp", None)
    addCond = sargs.get("condition", None)
    # LIST
    replacePassedCMDS = ["<tt>", "<exec>"]
    # CODE
    if replacePassed is not None and replacePassed is str:
        if type(addCond) is int:
            if addCond >= 1:
                if replacePassed.__contains__(replacePassedCMDS[0]):
                    p(f"{replacePassed[len(replacePassedCMDS[0]):]}<{tt}> {t}")
                elif replacePassed.__contains__(replacePassedCMDS[1]):
                    exec(f"{replacePassed[len(replacePassedCMDS[1]):]}")
                else:
                    p(f"{replacePassed} {t}")
        elif type(addCond) is bool:
            if addCond:
                if replacePassed.__contains__(replacePassedCMDS[0]):
                    p(f"{replacePassed[len(replacePassedCMDS[0]):]}<{tt}> {t}")
                elif replacePassed.__contains__(replacePassedCMDS[1]):
                    exec(f"{replacePassed[len(replacePassedCMDS[1]):]}")
                else:
                    p(f"{replacePassed} {t}")
            else:
                pass
        elif type(addCond) is list:
            allAreTrue = False
            counter = 0
            for boolVar in addCond:
                if boolVar:
                    counter += 1
            if counter >= len(addCond):
                allAreTrue = True
            if allAreTrue:
                if replacePassed.__contains__(replacePassedCMDS[0]):
                    p(f"{replacePassed[len(replacePassedCMDS[0]):]}<{tt}> {t}")
                elif replacePassed.__contains__(replacePassedCMDS[1]):
                    exec(f"{replacePassed[len(replacePassedCMDS[1]):]}")
                else:
                    p(f"{replacePassed} {t}")
        elif addCond is None:
            if replacePassed.__contains__(replacePassedCMDS[0]):
                p(f"{replacePassed[len(replacePassedCMDS[0]):]}<{tt}> {t}")
            elif replacePassed.__contains__(replacePassedCMDS[1]):
                exec(f"{replacePassed[len(replacePassedCMDS[1]):]}")
            else:
                p(f"{replacePassed} {t}")
    else:
        p(f"passed {t}")


def makeBox(t: str, **kwargs):
    """
    From old version
    ____________________________________________________
    Make a printable box with text inside of it
    I may need to touch this up a bit to except newlines
    but you know how this code is made

    :param t:
    :param kwargs:
    :return:
    """
    # KWARGS
    condition = kwargs.get("cond", None)
    cmp = kwargs.get("compare", "e")
    changeCValue = kwargs.get("value")
    _return = kwargs.get("_return", False)
    # STR
    output = ""
    # INT
    new_line_count = len(t.split("\n"))
    c = genIterList(9)
    gl = len(t) # ; For compat.
    # LIST
    new_line_list = []
    lines = [lol for lol in [len(l) for l in t.split("\n")]]
    lines_writable = [x for x in range(new_line_count)]
    lines_str = [ls for ls in t.split("\n")]
    # CODE

    if condition is not None:
        if type(condition) is bool:
            changeCValue = kwargs.get("value", True)
        elif type(condition) is int:
            changeCValue = kwargs.get("value", 0)
        elif type(condition) is float:
            changeCValue = kwargs.get("value", float(0))
        elif type(condition) is str:
            changeCValue = kwargs.get("value", "Hello, Gull!")

    if t.__contains__("\n"):
        for l in range(new_line_count+2):
            new_line_list.append("")
        biggest_line = lines.index(max(lines)) # ; Accuratly determine what is the biggest line
        for i in range(len(new_line_list)): # ;here we go
            for n in range(len(new_line_list)):
                if n in [0, len(new_line_list)-1] and c[0] != 1:
                    for d in range(lines[biggest_line]+2): # ; Grab the largest line, this line builds the top line
                        if d == lines[biggest_line]+2:
                            pass
                        else:
                            if d == 0:
                                new_line_list[n] += " "
                            new_line_list[n] += "-"
                        c[3] = len(new_line_list[n])
                    if n == len(new_line_list)-1:
                        c[0] = 1
                elif c[1] != 1 and c[0] == 1:
                    for line in lines_writable:
                        new_line_list[line+1] = f"| {lines_str[line]}"
                        if c[2] != 1:
                            for add_space in range(len(lines_str[biggest_line][len(lines_str[line]):])+1):
                                if add_space != len(lines_str[biggest_line][len(lines_str[line]):]):
                                    new_line_list[line+1] += " "
                                else:
                                    new_line_list[line+1] += " |"
                            c[2] = 1
                        else:
                            for add_space in range(c[3]-len(f"| {lines_str[line]}")):
                                if add_space != c[3]-len(f"| {lines_str[line]}")-1:
                                    new_line_list[line+1] += " "
                                else:
                                    new_line_list[line+1] += " |"
                    c[1] = 1
                elif c[1] == 1:
                    break
        for line in new_line_list:
            output += line+"\n"
    else:
        for i in range(len(t) + 4 * 100):
            if c[0] == 0:
                output += " "
            else:
                if not c[0] >= gl + 3 and c[1] == 0:
                    output += "-"
                else:
                    if c[1] == 0:
                        output += "\n"
                    elif not c[1] == 1:
                        if c[2] == 0:
                            output += "|"
                        elif c[2] == 1:
                            if not c[3] == 1:
                                output += " "
                                c[3] += 1
                            else:
                                if not c[4] >= gl and c[2] == 1:
                                    output += t[c[4]]
                                c[4] += 1
                                if c[4] >= gl and c[2] == 1 and c[5] == 0:
                                    if c[6] == 0:
                                        output += " "
                                        c[6] += 1
                                    if c[6] == 1:
                                        output += "|"
                                        c[6] += 1
                                    if c[6] == 2:
                                        output += "\n"
                                        c[5] += 1
                        elif c[2] >= 2:
                            if c[7] == 0:
                                output += " "
                            elif not c[7] >= gl + 3 and not c[8] == 1:
                                output += "-"
                            elif c[7] >= gl + 3:
                                break
                            c[7] += 1
                        if not c[2] == 1:
                            c[2] += 1
                        elif c[5] == 1 and not c[2] == 2:
                            c[2] += 1
                    c[1] += 1
            c[0] += 1
    p(output, cond=condition, compare=cmp, value=changeCValue)


def flp(l: dict, **kwargs):
    """
    For in Loop Print From Dictionary

    kwargs
    -----------------
    additions(str) Def: None
        Commands(additionsCommander):
            |_____"<addfirst>" = puts the additions first before "key" or "value" (if type is list)
            |_____"<addinbetween>" =  puts the additions in between "key" and "l.get(key)" (not availible if the type is a list)
            |_____"<counter> = adds a counter
    returnValue(Bool) Def: False
        |
        |___________True = Return Value
        |___________False = Pass

    :param l:
    :param kwargs:
    :return:
    """
    # KWARGS
    additions = kwargs.get("add", None)
    returnValue = kwargs.get("_return", False)
    cond = kwargs.get("cond", None)
    # LIST
    additionsCommander = ["<addfirst>", "<addinbetween>", "<counter>"]
    # ABS
    add = additions
    # CODE
    if add is not None and type(add) is str:
        if add.__contains__(additionsCommander[2]):
            additionsCommanderCounter = 0
    if returnValue:
        rv = ""

    if type(l) is dict:
        for key in l:
            if add is not None and type(add) is str:
                if add.__contains__(additionsCommander[0]):
                    p(f"{add[len(additionsCommander[0]):]} {key}: {l.get(key)}", cond=cond)
                elif add.__contains__(additionsCommander[1]):
                    p(f"{key}: {add[len(additionsCommander[1]):]} {l.get(key)}", cond=cond)
                elif add.__contains__(additionsCommander[2]):
                    additionsCommanderCounter += 1
                    p(f"{key}: {l.get(key)} {add[len(additionsCommander[2]):]}<{additionsCommander}>", cond=cond)
                else:
                    p(f"{key}: {l.get(key)} {add}")
            else:
                if returnValue:
                    rv += f"{key}: {l.get(key)}\n"
                p(f"{key}: {l.get(key)}")
    elif type(l) is list:
        for value in l:
            if add is not None and type(add) is str:
                if add.__contains__(additionsCommander[0]):
                    p(f"{add[len(additionsCommander[0]):]} {value}")
                elif add.__contains__(additionsCommander[2]):
                    additionsCommanderCounter += 1
                    p(f"{value} {add[len(additionsCommander[2]):]}<{additionsCommander}>", cond=cond)
                else:
                    p(f"{value} {add}", cond=cond)
            else:
                rv = ""
                if returnValue:
                    rv += f"{value}\n"
                p(value, cond=cond)
    if returnValue:
        return rv

# ;============================================================================================================================
# ;FILE BASED FUNCTIONS
# ;============================================================================================================================

def getPresSpec(file: str, **kwargs):
    """
    Does the file exist

    kwargs
    ------------------------
    GPS_RETURN_EXIST(Bool) Def: True
        |
        |_________True = Return result
        |_________False = Prints Result
    GPS_CREATE_FOLDER(Bool) Def: False
        |
        |_________True = Create folder if it doesn't exist
        |_________False = Don't create if doesn't exist
    GPS_SILENT_MODE(Bool) Def: True
        |
        |_________True = Don't print
        |_________False = Enable printing

    Returns: None by default
    """
    # KWARGS
    GPS_RETURN_EXIST = kwargs.get('return_result', True)
    GPS_CREATE_FOLDER = kwargs.get("create_folder", False)
    GPS_SILENT_MODE = kwargs.get("silence", True)
    # OSPATH
    getpres = os.path.exists
    # CODE
    if GPS_SILENT_MODE is False:
        p(f"{getpres(file)} This file/folder already exists", cond=GPS_RETURN_EXIST)
    if GPS_CREATE_FOLDER:
        if getpres(file) is False:
            if GPS_RETURN_EXIST is False:
                p(f"Making File/Folder:\n\t\t{file}", cond=GPS_SILENT_MODE, value=False)
            os.makedirs(file)
        elif GPS_RETURN_EXIST is False:
            p(f"Folder already exists:\n\t\t{file}", cond=GPS_SILENT_MODE, value=False)
    return getpres(file)


def ptry(cmd, err_num):
    """
    PrintTry is a conditional function that use try and except conditionals
    :param cmd:
    :param err_num:
    :return:
    """
    # DICT
    errStrs = {
        0: {
            0: "PermissionError",
            1: "OSError",
            2: "RuntimeError"
        },
        1: {
            0: "notAbleToCreateFolderOrFileAtGivenDir",
            1: "cantRunProcessDueToNotBeingInstalled",
            2: "pythonErr",
        },
        2: {
            0: f"{GF_FILENAME}: <{tt}> An error has occured (err code: {err_num})\n\tPermission to this '{cmd}' has been denied",
            1: f"{GF_FILENAME}: <{tt}> An error has occured (err code: {err_num})\n\tRunning '{cmd}' returned as 'Unknown Command'",
            2: f"{GF_FILENAME}: <{tt}> An error has occured (err code: {err_num})\n\tAccess to this path '{cmd}' doesn't exist",
            3: f"{GF_FILENAME}: <{tt}> An error has occured (err code: {err_num}\n\tPython has ran into an error\n\t\tPython: {cmd}"
        }
    }

    # CODE
    # ;    Command
    # ;       |
    # ;       |  Error Type
    # ;       |      |
    # ;       |      |    Variable
    # ;       |      |       |
    # ;       |      |       |   String From Dict Refrence (but takes int)
    # ;       |      |       |        |
    def runt(str1, err_type, var1, err_num_ref):
        exec(f"if err_num == {err_num_ref}:\n\ttry:\n\t\t{str1}\n\texcept {err_type} as {var1}:\n\t\tp(f'{{errStrs[2][err_num_ref]}}{{var1}}')\n\t\tsys.exit(2)")

    runt(cmd, errStrs[0][0], errStrs[1][0], 0)  # ;Permission Error
    runt(f"subprocess.run({cmd}, shell=True)", errStrs[0][1], errStrs[1][1], 1)  # ;Subprocess Unknown Error
    runt(cmd, errStrs[0][2], errStrs[1][2], 3)  # ;Python Error

def getDir(targetpath: str, **kwargs):
    """
    Takes the files within a folder and translate the paths to a dictionary (targetname --> returnname)

    kwargs
    -----------------------------------
    GD_FILTER(str or list of strings) Def: None
    GD_PRINT_DICT(Bool) Def: True
        |
        |_________True = Print Result
        |_________False = pass
    GD_ALSO_INCLUDE_FILE_NAME(Bool) Def: True
        |
        |_________True = adds in the name without the path
        |_________False = pass
    
    :param targetpath:
    :param kwargs:
    :return: Dict
    """
    # KWARGS
    GD_FILTER = kwargs.get("filter", None)  # ;acts like the search or find option you most likely find in a file manager
    GD_PRINT_DICT = kwargs.get("print_dict", True)
    GD_ALSO_INCLUDE_FILENAME = kwargs.get("alsoIncludeFileName", True)
    GD_DEBUG = kwargs.get("debug", False)
    # INT
    counter = 0
    # DICTIONARIES
    d = {}
    # LISTS
    nmi = []
    mi = []
    # CODE
    
    def file_extension_finder(s):
        # INT
        char_counter = 0
        # LIST
        period_tracker = []
        # CODE
        for char in s:
            char_counter += 1
            if char == ".":
                period_tracker.append(char_counter-1)
        
        if len(period_tracker) > 0:
            return s[period_tracker[-1]:]
        elif len(period_tracker) == 0:
            return s
        else:
            return s[period_tracker[0]:]
        
    
    for file in os.listdir(targetpath):  # ;Loop through directory
        if GD_FILTER is not None:  # ;if argument is not a NONE type
            try:
                if type(GD_FILTER) is str:
                    if file.__contains__(GD_FILTER):  # ;if filename contains a word, number or file type
                        counter += 1
                        if GD_ALSO_INCLUDE_FILENAME:
                            d.update({counter: [targetpath + file, file[:-len(file_extension_finder(file))]]})
                        else:
                            d.update({counter: targetpath + file})
                elif type(GD_FILTER) is list:
                    onlyExt = file_extension_finder(file)
                    p(onlyExt, cond=GD_DEBUG)
                    if onlyExt in GD_FILTER:
                        counter += 1
                        if GD_ALSO_INCLUDE_FILENAME:
                            d.update({counter: [targetpath + file, file[:-len(file_extension_finder(file))]]})
                            mi.append(counter)
                        else:
                            d.update({counter: targetpath + file})
                            mi.append(counter)
            except TypeError as valueTypeIsInvalid:
                p(f"<{tt}> Filter arg type error: {valueTypeIsInvalid}")
                sys.exit(2)
        else:
            counter += 1
            if GD_ALSO_INCLUDE_FILENAME:
                d.update({counter: [targetpath + file, file[:-len(file_extension_finder(file))]]})
            else:
                d.update({counter: targetpath + file})
    if GD_PRINT_DICT:
        flp(d)
        if len(nmi) != 0:
            p(f"--------------------\n\tMissing\n--------------------")
            flp(nmi)
    del mi, nmi  # ;These aren't needed anymore when the loop is done
    return d

# ;============================================================================================================================
# ;LIST BASED FUNCTIONS
# ;============================================================================================================================

def merge(target_list, **kwargs):
    """
    Takes a nested list into a single list

    kwargs
    --------------------------------------
    show_result(Bool) Def: False
        |_______True = Print Result
        |_______False = pass

    :param target_list:
    :param kwargs:
    :return:
    """
    # LISTS
    tl = target_list
    i = []  # ;result var
    # KWARGS_BOOLEANS
    show_result = kwargs.get("show_result", False)
    # CODE

    for cat in tl:
        for value in cat:
            i.append(value)

    p(f"{i} print 2", cond=show_result)

    return i

def bubble(var: list, start: int, stop:int, **bo):
    """
    easily remove multiple indexes

    :param var:
    :param start:
    :param stop:
    :return:
    """
    # BO
    bo_copy = bo.get("copy", False)
    bo_strip_it = bo.get("strip", False)
    # INT
    a = start
    # CODE
    if bo_copy:
        new_list = var.copy()
        for i in range(len(new_list)):
            if i >= start:
                new_list.pop(a)
            if i == stop:
                break
        if bo_strip_it is True:
            if len(var) == 1:
                return var[0]
        else:
            return new_list
    else:
        for i in range(len(var)):
            if i >= start:
                var.pop(a)
            if i >= stop:
                break
        if bo_strip_it:
            if len(var) == 1:
                return var[0]
        else:
            return var


def remDupesLst(target, **kwargs):
    """
    Removes any duplicates from a list (making unique ones stay)

    kwargs
    ----------------------------------
    print_result(Bool) Def: False
        |
        |_____True = Print Result
        |_____False = pass
    sender(list) Def: None
        |
        |______sends target value to another list

    :param target:
    :param kwargs:
    :return:
    """
    # LIST
    new_list = []
    # KWARGS
    print_result = kwargs.get("print_result", False)
    sender = kwargs.get("send", None)
    # CODE
    if sender is not None:
        for i in target:
            if i not in target:
                sender.append(i)
    else:
        for i in target:
            if i not in target:
                new_list.append(i)

    p(new_list, cond=print_result)

    if sender is not None:
        return new_list


def genIterList(amount, **kwargs):
    '''
    Generates an iteration list mainly comprised of 0's of course

    kwargs
    --------------------------
    GIL_PRINTRESULT(Bool) Def: False
        |
        |_______True = prints result
        |_______False = pass
    GIL_LISTNAME(list) Def: None

    :param amount:
    :param kwargs:
    :return:
    '''
    # KWARGS
    GIL_PRINTRESULT = kwargs.get('print_result', False)
    GIL_LISTNAME = kwargs.get('listname', None)
    # ABS
    a = amount
    # LIST
    l = []
    # CODE
    if GIL_LISTNAME is not None:
        for i in range(a):
            GIL_LISTNAME.append(0)
            p(GIL_LISTNAME, cond=GIL_PRINTRESULT)
        return GIL_LISTNAME
    else:
        for i in range(a):
            l.append(0)
            p(f"gen_iter_list <print_result>: {l}", cond=GIL_PRINTRESULT)
        return l

# ;============================================================================================================================
# ;RANDOMIZATION BASED FUNCTIONS
# ;============================================================================================================================

def boolRandom(**brargs):
    """
    Generates a list of random boolean values and choses it which index which will return with bool.

    kwargs
    ------------------------------
    generateBools(int) Def: 2
        |
        |________How many values in the pool
    rollDice(int) Def: 1
        |
        |________How many "rolls" till it gets it final result
    printResult(Bool) Def: False
        |
        |________True = Print result
        |________False = pass
    sleep(Bool) Def: False
        |
        |________True = the rate one does roll (1000 ticks)
        |________False = pass
    count(Bool) Def: False
        |
        |________True = Print true and false statements in the genList
        |________False = Don't count and print statements

    :param brargs:
    :return:
    """
    # brargs
    generateBools = brargs.get("genBools", 2)
    rollDice = brargs.get("rolls", 1)
    printResult = brargs.get("pr", False)
    count = brargs.get("count", False)
    # list
    bL = [False, True]
    genList = []
    # code
    if count:
        counters = genIterList(2)
    for var in range(generateBools):
        if count:
            value = choice(bL)
            if value:
                counters[1] += 1
            if value:
                counters[0] += 1
            genList.append(value)
        else:
            genList.append(choice(bL))

    if rollDice < 1:
        rollDice = 1

    for plays in range(rollDice):
        chose = choice(genList)

    p(chose, cond=printResult)

    if count:
        if counters[0] > counters[1]:
            p(f"\nFalse: {counters[0]}\nTrue: {counters[1]}\nThere is more of False values in the list than True values\n")
        elif counters[1] > counters[0]:
            p(f"\nFalse: {counters[0]}\nTrue: {counters[1]}\nThere is more of True values in the list than False values\n")
        elif counters[0] == counters[1]:
            p(f'\nFalse: {counters[0]}\nTrue: {counters[1]}\nTrue is half of False values "False == True"\n')

    return chose


def rollDice(target, rolls, **rda):
    """
    it's like `random.choice()` and similiar `boolRandom()` except it can roll multiple times to get a final result

    rollDiceArgs (RDA)
    ---------------------------
    printResult(Bool) Def: False
            |_______True = Prints result
            |_______False = Pass
    showList(Bool) Def: False
            |_______True = Prints the targeted list
            |_______False = Pass
    :param target:
    :param rolls:
    :return:
    """
    # rda
    printResult = rda.get("pr", False)
    showList = rda.get("sl", False)
    # bool
    targetNotList = False
    # code
    if type(target) is list:
        for roll in range(rolls):
            result = choice(target)
    else:
        targetNotList = True
        l = []
        if target <= 0: # ; If target is int or float, then try again but more than 1
            for i in range(randint(1, 500)):
                l.append(i)
            for roll in range(rolls):
                result = choice(l)
        else:
            for i in range(target):
                l.append(i)
            for roll in range(rolls):
                result = choice(l)
    p(result, cond=printResult)
    if targetNotList:
        p(l, cond=showList)
    return result

# ;============================================================================================================================
# ;DETECTION BASED FUNCTIONS
# ;============================================================================================================================

def sysDetect(**sdopt):
    """
    Inherited From EccoPY

    sdopt
    ---------------------
    printResult(Bool) Def: False
            |________True = Prints Results
            |________False = pass

    :return:
    """
    # sdopt
    printResult = sdopt.get("getResults", False)
    # code
    p("Detecting Operating System and Hardware...")
    if sys.platform.startswith("win32") or sys.platform.startswith("cygwin"):
        extra_info = [info for info in os.environ]
        compinfo = {
            # ;Hardware
            "Machine".lower(): pt.machine(),
            "CPU".lower(): pt.processor(),
            # ;Software
            "System".lower(): pt.system(),
            "Version".lower(): f"Short: {pt.release()}, Full: {pt.platform()}",
            "Edition".lower(): pt.win32_edition(),
            # ;"DE".lower(): os.environ.get("desktop_session".upper()),
            # ;User
            "Username".lower(): gp.getuser(),
            # ;Python
            "Python_Build".lower(): pt.python_build(),
            "Python_Compiler".lower(): pt.python_compiler(),
            "Python_Release".lower(): pt.python_branch(),
            "Python_Version".lower(): pt.python_version(),
            # ;Gull Framework
            "Gull_Framework_Version".lower(): GF_VERSION,
            "Gull_Framework_Edition".lower(): GF_EDITION
        }
    elif sys.platform.startswith("darwin"):
        extra_info = [info for info in os.uname()]
        compinfo = {
            # ;Hardware
            "Machine".lower(): extra_info[4],
            "CPU".lower(): pt.processor(),
            # ;Software
            "System".lower(): pt.mac_ver()[0],
            "KernelVersion".lower(): extra_info[2],
            "KernalVersionExtended".lower(): extra_info[3],
            "DE".lower(): "Aqua",
            # ;User
            "NodeName".lower(): extra_info[1],
            "Username".lower(): gp.getuser(),
            # ;Python
            "Python_Build".lower(): pt.python_build(),
            "Python_Compiler".lower(): pt.python_compiler(),
            "Python_Release".lower(): pt.python_branch(),
            "Python_Version".lower(): pt.python_version(),
            # ;Gull Framework
            "Gull_Framework_Version".lower(): GF_VERSION,
            "Gull_Framework_Edition".lower(): GF_EDITION
        }
    else:
        extra_info = [info for info in os.uname()]
        compinfo = {
            # ;Hardware
            "Machine".lower(): extra_info[4],
            "CPU".lower(): pt.processor(),
            # ;Software
            "System".lower(): extra_info[0],
            "KernelVersion".lower(): extra_info[2],
            "Distro".lower(): extra_info[3],
            "DE".lower(): os.environ.get("desktop_session".upper()),
            # ;User
            "NodeName".lower(): extra_info[1],
            "Username".lower(): gp.getuser(),
            # ;Python
            "Python_Build".lower(): pt.python_build(),
            "Python_Compiler".lower(): pt.python_compiler(),
            "Python_Release".lower(): pt.python_branch(),
            "Python_Version".lower(): pt.python_version(),
            # ;Gull Framework
            "Gull_Framework_Version".lower(): GF_VERSION,
            "Gull_Framework_Edition".lower(): GF_EDITION
        }
    # ;else:
    # ;    compinfo = {
    # ;        # ;Hardware
    # ;        "Machine".lower(): pt.machine(),
    # ;        "CPU".lower(): pt.processor(),
    # ;        # ;Software
    # ;        "System".lower(): pt.system(),
    # ;        "OS".lower(): pt.platform(),
    # ;        # ;User
    # ;        "Username".lower(): gp.getuser(),
    # ;    }
    return compinfo

# ;============================================================================================================================
# ;TEXT (STRING) BASED FUNCTIONS
# ;============================================================================================================================

def find_text(s: str, file: str, **fto):
    """
    Shortened version

    with open("test_file.txt", "r+") as file:
        data = file.read()
        n1 = data.find("Hello")
        n2 = n1+len("hello")
        p(data[n1:n2])
        return data[n1:n2]

    :param s: = word/char
    :param file:
    :return:
    """
    # FTO
    fto_return_length = fto.get("return_length", False)
    # INT
    string_length = len(s)
    # CODE
    with open(file, "r+") as f:  # ;f is for file
        d = f.read()  # ; d as in data
        f.close()
        if fto_return_length:
            return [d.find(s), d.find(s) + string_length] # ;Returns a list of the beginning indice and the end indice instead of a string
        else:
            return d[d.find(s):d.find(s) + string_length]  # ;Return searched string

def backup_file(file, **bfo):
    """
    Backups file with options
    :param file:
    :param bfo:
    :return:
    """
    # BFO
    backup_file_save_to = bfo.get("save_to", "")
    # STR
    backup_file_name = f"{file[:file.index('.')]}_Backup_{f'{tt}'.split('.')[0].replace(':', '_')}"
    # CODE
    if backup_file_save_to == "":
        os.makedirs(f"Backup/{backup_file_name}")
        with open(f"Backup/{backup_file_name}/{file}", "w+") as backup:
            with open(file, "r") as f:
                data = f.read()
                f.close()
            backup.write(data)
            backup.close()
    else:
        backup_file_save_to_include_backup_folder = bfo.get("make_backup_folder", False)
        if backup_file_save_to_include_backup_folder:
            os.makedirs(f"{backup_file_save_to}/{backup_file_name}")
            with open(f"{backup_file_save_to}/{backup_file_name}/{file}", "w+") as backup:
                with open(file, "r") as f:
                    data = f.read()
                    f.close()
                backup.write(data)
                backup.close()
        else:
            os.makedirs(backup_file_save_to)
            with open(f"{backup_file_save_to}/{file}", "w+") as backup:
                with open(file, "r") as f:
                    data = f.read()
                    f.close()
                backup.write(data)
                backup.close()

def backup_project(**bpo):
    """
    Backup the whole project
    :param bpo:
    :return:
    """
    # BPO
    backup_project_save_to = bpo.get("save_to", "")
    backup_project_filter = bpo.get("filter", [])
    # STR
    backup_file_name = f"Project_Backup_{f'{tt}'.split('.')[0].replace(':', '_')}"
    # CODE
    if backup_project_filter == []:
        files_to_backup = getDir(GF_FILE_PATH + "/", alsoIncludeFileName=False, print_dict=False)
    else:
        files_to_backup = getDir(GF_FILE_PATH + "/", filter=backup_project_filter, alsoIncludeFileName=False, print_dict=False)

    if backup_project_save_to == "":
        os.makedirs(f"Backup/{backup_file_name}")
        for file in [files_to_backup[f] for f in files_to_backup]:
            with open(f"Backup/{backup_file_name}/{file.split('/')[-1]}", "w+") as backup:
                with open(file.split("/")[-1], "r") as f:
                    data = f.read()
                    f.close()
                backup.write(data)
                backup.close()
    else:
        backup_project_save_to_include_backup_folder = bpo.get("make_backup_folder", False)
        if backup_project_save_to_include_backup_folder:
            os.makedirs(f"{backup_project_save_to}/{backup_file_name}")
            for file in [files_to_backup[f] for f in files_to_backup]:
                with open(f"Backup/{backup_file_name}/{file.split(['/'])[-1]}", "w+") as backup:
                    with open(file.split("/")[-1], "r") as f:
                        data = f.read()
                        f.close()
                    backup.write(data)
                    backup.close()

# CLASSES------------------------------------------------------------------------------------------------------------------------------------------------------------------

class GF_GET_FILE_INFO(object):
    def __init__(self, target, types, **gfKwargs):
        # GFKWARGS
        self.printDict = gfKwargs.get("pDict", False)
        # STR
        self.target = target
        # DOUBLE
        self.types = types
        # GD
        self.dir = getDir(target, filter=types, alsoIncludeFileName=False, print_dict=self.printDict)

    def createDummyFiles(self, tar, types, **cdf):
        # CDF
        add = cdf.get("add", None)
        # LIST
        deleteMeAfter = []
        # CODE
        if add is None:
            for file in self.dir:
                if self.dir[file][self.dir[file].find('.'):] in types:
                    f = open(f"{tar}{file}.{self.dir[file][self.dir[file].find('.'):]}", "w+")
                    f.close()
                    deleteMeAfter.append(f"{tar}{file}.{self.dir[file][self.dir[file].find('.'):]}")
        else:
            for file in self.dir:
                if self.dir[file][self.dir[file].find('.'):] in types:
                    f = open(f"{tar}{file}{add}.{self.dir[file][self.dir[file].find('.'):]}", "w+")
                    f.close()
                    deleteMeAfter.append(f"{tar}{file}{add}.{self.dir[file][self.dir[file].find('.'):]}")
        return deleteMeAfter


class GF_MATH_CONVERT_FROM_LIST:
    """
    Functions Available
    -------------------
    hextoint() = Converts hex to int from list
    """

    def hextoint(self, tl: list, dl: list):
        # INT
        nothexval = 0
        # CODE
        for hexchecker in tl:
            for i in range(len(tl)):
                if type(hexchecker) is not hex:
                    nothexval += 1
        for value in tl:
            dl.append(int(value))

class GF_DEVLOG:
    """
    This deals with Logging stuff into a file

    Functions Avaible
    ---------------------------
    RECORD_CONSOLE(self, what: sys.stderr, sys.stdout, sys.stdin)
    """

    def __init__(self, filepath: str = "/Documents/SIS/EccoPY/LOGS/", textfile: str = "DEVELOPERLOG", filetype: str = ".log", limit_fs: float = 0x164210, isThisEnabled: bool = True):
        # STRINGS
        self.fp = filepath
        self.tf = textfile
        self.ft = filetype
        # FLOATS
        self.lfs = limit_fs
        # BOOLEANS
        self.ise = isThisEnabled
        # STATEMENTS
        self.gun = gp.getuser()

    def RECORD_CONSOLE(self, what):
        # CODE
        if what is not sys.stderr or sys.stdout or sys.stdin:
            p(f"Gull: ARGUMENT OF RECORD WHICH IS {what} ISN'T 'sys.stderr', 'sys.stdout OR 'sys.stdin'\n SOLUTION: Try changing 'what' to one of those options")
            raise ValueError
        os.makedirs(f"/Users/{self.gun}{self.fp}")
        what = open(f"/Users/{self.gun}{self.fp}{self.tf}{str(what)}", "w+")
        if self.ise:
            if os.path.getsize(f"/Users/{self.gun}{self.fp}/{self.tf}") >= self.lfs:
                what.close()
        else:
            p("Ok")


class GF_WRITE_SETTING_FILES:
    """
    This deals with writing non-existant settings file/s (mainly uses '.ini' files ATM)

    Functions Avaible
    ---------------------------
    writeSettingsFile(self, dir: str *optional*, name: str *optional*, **kwargs)
    """

    def __init__(self):
        super().__init__()
        # USERNAME
        self.gun = gp.getuser()  # ;Get Current Username
        # DIRECTORIES
        self.subdir = f"{self.gun}/EP_S/"
        self.user_settings_folder = f"/Documents/Seagulls/EccoPY/"

    def writeSettingsFile(self, dir: str = "/Documents/Seagulls/EccoPY/", name: str = "Settings", **kwargs):
        # KWARGS
        WSF_RETURN_FILEPATH = kwargs.get('return_path', True)
        # STRINGS
        d = dir
        n = name
        getdir = f"/Users/{self.gun}{dir}{self.subdir}"
        # CODE
        if os.path.exists(getdir) is False:
            os.makedirs(getdir)

        newfile = open(f"{getdir}{name}.ini", "w+")  # Creates new file
        newfile.close()

        if WSF_RETURN_FILEPATH:
            path_name = f"{getdir}{n}.ini"
            p(path_name)
            return path_name

class GF_INIT:
    """
    Gull Framework Root class

    Functions Available
    -------------------
    self.enable_assembly_mode(Bool) Def: True
        |
        |_______True = Makes the vars smaller and faster to type
        |_______False = Uses a more longer var set
    self.init_all_classes(Bool) Def: False
        |
        |_______True = initalizes all classes
        |_______False = Manual Mode
    self.load_all_palm_trees(Bool) Def: False *May need to return to this later*
        |
        |_______True = loads all *palm trees* from the "EXT" folder
        |_______False = pass
    self.no_print(Bool) Def: True
        |
        |______True = Disables the Gull Framework Ascii Art print
        |______False = Enables
    """

    def __init__(self, **kwargs):
        # KWARGS_BOOLEANS
        self.enable_assembly_mode = kwargs.get("assembly_mode", True) # ;Shortens init values to a few or more characters
        self.init_all_classes = kwargs.get("init_all", False)  # ;Runs all initilized classes
        self.no_start_print = kwargs.get("no_print", False) # ;Shhhhhhhh quiet \/
        #   CODE
        p(f"\nPanda Framework v: {GF_VERSION}\n\tCode: https://github.com/SeagullisLearningToCode/Gull-Framework\n\tNOTE: No repo is avalible as of this version of PF, it will soon be added\n------------------------------------------------------------------------------------------------------------", cond=self.no_start_print, value=False)
        if self.init_all_classes:
            if self.enable_assembly_mode:
                self.dl = GF_DEVLOG()
                self.wsf = GF_WRITE_SETTING_FILES()
                self.cl = GF_MATH_CONVERT_FROM_LIST()
                self.gef = GF_GET_FILE_INFO()
            else:
                self.log = GF_DEVLOG()
                self.set = GF_WRITE_SETTING_FILES()
                self.convert = GF_MATH_CONVERT_FROM_LIST()
                self.getFileInfo = GF_GET_FILE_INFO()
        if self.enable_assembly_mode and self.init_all_classes is False:  # ;gives it somewhat of an assembly feel
            self.dl = GF_DEVLOG  # ;Logs stuff
            self.wsf = GF_WRITE_SETTING_FILES  # ;Writes INI files
            self.cl = GF_MATH_CONVERT_FROM_LIST  # ;Deals with converting lists/dicts to differnt types of values inside them
            self.gef = GF_GET_FILE_INFO  # ;This is very limited as of now, this deals with getting the size of a file (as in resolution)
        if self.enable_assembly_mode is False and self.init_all_classes is False:  # ;New age stuff
            self.log = GF_DEVLOG
            self.set = GF_WRITE_SETTING_FILES
            self.convert = GF_MATH_CONVERT_FROM_LIST
            self.getFileInfo = GF_GET_FILE_INFO


# INIT_GULL_FRAMEWORK----------------------------------------------------------------------------------------------------------------------------------------------------------------

GF = GF_INIT(assembly_mode=True, no_print=False)
