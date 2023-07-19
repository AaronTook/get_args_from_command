def get_args_from_command(command, seperator):
	"""Take two strings as arguments, with the first representing a command with arguments and the second being the argument seperator (commonly '-' or '--') and teturn the command name and the arguments as a string and a list respectively."""
	command_parts = command.split(' ' + seperator)
	name = command_parts[0]
	if len(command_parts) > 0: # Arguments were included in the command.
		arguments = command_parts[1:]
	else: # No arguments were included in the command.
		arguments = []
	return name, arguments
