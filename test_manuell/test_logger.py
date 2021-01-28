from time import sleep
from cli_logger import MessageClass, log, information, set_minimum_severity_level, error, debug, warning, returnCode, printProgressBar

set_minimum_severity_level = MessageClass.DEBUG #default is INFORMATION. Overwrite it for example more verbous output.

debug('Debug message.') # use debug for lowest-level messages.
information('Information message.') # information messages are usual output.
print('Returncode: %s' % returnCode()) # usually, only at program end, you can check the return code if any warnings or errors have occured.

warning('A warning.')
warning('Beware!')
print('Returncode: %s' % returnCode())

error('Error! Go home.')
print('Returncode: %s' % returnCode())

# and there's even a progress bar included.
printProgressBar(1, 4, 'Process running [name]', 'suffix')
sleep(1)
printProgressBar(2, 4, 'Process running [name]', 'suffix')
sleep(1)
printProgressBar(3, 4, 'Process running [name]', 'suffix')
sleep(1)
printProgressBar(4, 4, 'Process running [name]', 'suffix')
