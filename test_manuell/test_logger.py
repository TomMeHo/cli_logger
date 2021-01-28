from time import sleep
from cli_logger import MessageClass, log, information, set_minimum_severity_level, error, debug, warning, returnCode, printProgressBar

set_minimum_severity_level = MessageClass.DEBUG

debug('Debug message.')
print('Returncode: %s' % returnCode())

information('Information message.')
print('Returncode: %s' % returnCode())

warning('A warning. Beware!')
print('Returncode: %s' % returnCode())

error('Error! GO home.')
print('Returncode: %s' % returnCode())

printProgressBar(1, 10, 'Process running [name]', 'suffix')
sleep(2)
printProgressBar(5, 10, 'Process running [name]', 'suffix')
sleep(2)
printProgressBar(10, 10, 'Process running [name]', 'suffix')
