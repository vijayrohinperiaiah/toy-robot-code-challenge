from toyrobot.commands_controller import CommandsController
from toyrobot.toyrobot import ToyRobot
import re

place_cmd_introduced = False

# Main function for executing the functionality of the program
def execute_main():
	is_simulator_running = True
	commands_controller = CommandsController(print)
	robot = ToyRobot()

	print("-------------------------------------------------------------------------------")
	print("-------------------------Toy Robot Program ( 5 X 5 )-------------------------")
	print("-------------------------------------------------------------------------------")
	print("=========================Available Commands and Syntax=========================")
	print("-------------------------------------------------------------------------------")
	print("(1) PLACE [x_position],[y_position],[face_direction] - To place it on the table")
	print("*Parameters definitions:*")
	print("**[x_position] -> between 0 and 4")
	print("**[y_position] -> between 0 and 4")
	print("**[face_direction] -> NORTH,SOUTH,EAST,WEST")
	print("(2) MOVE - To move robot one step forward in its facing direction")
	print("(3) RIGHT - To turn robot 90 degrees to its right side")
	print("(4) LEFT - To turn robot 90 degrees to its left side")
	print("(5) REPORT - To print current positions and facing direction")
	print("(6) EXIT - To exit the program")
	print("===============================================================================")
	print("Type the input commands for the robot...")

	while is_simulator_running: # Infinte loop - stops only when user types in EXIT Command
		given_command = input("New Command: ") # Getting input from the user, single command at one instance
		ansi_escape = re.compile(r'\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])') # Removing any escape sequence characters included in raw string
		given_command = ansi_escape.sub('', given_command)
		given_command = given_command.strip()
		given_command_split_up = given_command.split(" ") # Splitting up to get the intended command
		invoked_command = (given_command_split_up[0]).upper()

		if invoked_command == "EXIT" and len(given_command_split_up) == 1: # To check if its exit command
			is_simulator_running = False
			print("Thanks for executing toy robot program!!!")
			return
		if hasattr(robot, 'coordinates') or invoked_command == "PLACE": # To skip over the commands until PLACE command is introduced
			cmd = commands_controller.to_cmd(given_command)
			cmd.move_on(robot)
		else:
			print("Please start with the `PLACE [x_position],[y_position],[face_direction]` Command.")


if __name__ == '__main__':
	execute_main()

#EOF