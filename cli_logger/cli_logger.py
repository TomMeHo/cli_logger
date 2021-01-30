import click
from colorama import Fore, Back, Style
from datetime import datetime
#from enum import IntEnum

executionWithError = False
executionWithWarning = False

class MessageClass():
    DEBUG = 0
    INFORMATION = 1
    WARNING = 2
    ERROR = 3

MIN_SEVERITY_LEVEL = MessageClass.INFORMATION

def set_minimum_severity_level(severity: MessageClass):
    global MIN_SEVERITY_LEVEL
    MIN_SEVERITY_LEVEL = severity

def log(severity: MessageClass, msg : str, override_min_severity_level = False):
    
    global MIN_SEVERITY_LEVEL
    global executionWithWarning
    global executionWithError

    if (severity >= MIN_SEVERITY_LEVEL) or override_min_severity_level:

        format_string = {
            0: Fore.CYAN + Style.BRIGHT   + ' DEBUG        ' + Style.RESET_ALL + Style.DIM,
            1: Fore.GREEN + Style.BRIGHT  + ' INFORMATION  ' + Style.RESET_ALL + Style.DIM,
            2: Fore.YELLOW + Style.BRIGHT + ' WARNING      ' + Style.RESET_ALL + Style.DIM,
            3: Fore.RED + Style.BRIGHT    + ' ERROR        ' + Style.RESET_ALL + Style.DIM,
        }

        now = datetime.now()
        click.echo( now.strftime('%I:%M:%S %p') + '  ' + format_string[severity] + '  ' + msg + Style.RESET_ALL)    

    if severity == MessageClass.WARNING: executionWithWarning = True
    if severity == MessageClass.ERROR: executionWithError = True

def debug(msg : str):
    log(MessageClass.DEBUG, msg)

def information(msg : str):
    log(MessageClass.INFORMATION, msg)

def warning(msg : str):
    log(MessageClass.WARNING, msg)

def error(msg : str):
    log(MessageClass.ERROR, msg)

# Print iterations progress
def printProgressBar (iteration, total, prefix = '', suffix = '', decimals = 1, length = 50, fill = '█', printEnd = "\r", intend = True):
    """
    Call in a loop to create terminal progress bar
    @params:
        iteration   - Required  : current iteration (Int)
        total       - Required  : total iterations (Int)
        prefix      - Optional  : prefix string (Str)
        suffix      - Optional  : suffix string (Str)
        decimals    - Optional  : positive number of decimals in percent complete (Int)
        length      - Optional  : character length of bar (Int)
        fill        - Optional  : bar fill character (Str)
        printEnd    - Optional  : end character (e.g. "\r", "\r\n") (Str)
    """
    
    if intend:
        prefix = '                             ' + prefix

    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print('\r%s |%s| %s%% %s' % (prefix, bar, percent, suffix), end = printEnd)
    # Print New Line on Complete
    if iteration >= total: 
        print()

def returnCode() -> int:
    
    rc = 0

    if executionWithWarning: rc = 1
    if executionWithError: rc = 2

    return rc