Process Management


Author: Adio Adebayo



This repository contains various scripts and programs related to process management in Linux.

1. List Running Processes
The script 1-list_running_processes.sh displays a list of currently running processes for all users, including those which might not have a TTY. The process hierarchy is also displayed in a user-oriented format.

2. Get PID of Bash Process
The script 2-get_bash_pid.sh uses the ps command to display lines containing the word 'bash', allowing the user to easily get the PID of their Bash process.

3. Get PID and Process Name of Processes Containing 'bash'
The script 3-get_bash_pid_name.sh uses the lsof command to display the PID and process name of processes whose name contain the word 'bash'.

4. To Infinity and Beyond
The script 4-to_infinity_and_beyond.sh displays the message "To infinity and beyond" indefinitely, with a 2 second sleep in between each iteration.

5. Stop Me If You Can
The script 5-stop_me_if_you_can.sh stops the 4-to_infinity_and_beyond process using the pkill command.

6. Highlander
The script 6-highlander.sh displays "To infinity and beyond" indefinitely, with a 2 second sleep in between each iteration. It also displays "I am invincible!!!" when receiving a SIGTERM signal.

7. Stop Highlander
The script 7-stop_highlander.sh stops the 6-highlander process using the pkill command.

8. Manage My Process
The script 8-manage_my_process.sh creates a file /var/run/myscript.pid containing its PID. It displays "To infinity and beyond" indefinitely, with a 2 second sleep in between each iteration. It also displays "I hate the kill command" when receiving a SIGTERM signal and "Y U no love me?!" when receiving a SIGINT signal. It deletes the file /var/run/myscript.pid and terminates itself when receiving a SIGQUIT or SIGTERM signal.

9. Manage My Process Init Script
The script 9-manage_my_process.sh is an init script that manages the 8-manage_my_process.sh script. When passed the argument start, it starts 8-manage_my_process.sh, creates a file containing its PID in /var/run/my_process.pid, and displays "manage_my_process started". When passed the argument stop, it stops 8-manage_my_process.sh, deletes the file /var/run/my_process.pid, and displays "manage_my_process stopped". When passed the argument restart, it stops and restarts 8-manage_my_process.sh, creates a new file containing its PID in /var/run/my_process.pid, and displays "manage_my_process restarted". If any other argument or no argument is passed, it displays "Usage: manage_my_process {start|stop|restart}".

10. Zombie Processes
The program 10-zombie.c created 
