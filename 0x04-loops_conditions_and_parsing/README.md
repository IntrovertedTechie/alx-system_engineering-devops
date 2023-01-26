0x04. Loops, Conditions and Parsing

This project is about using loops, conditions and parsing in Bash scripting.

Learning Objectives

How to create SSH keys

What is the advantage of using #!/usr/bin/env bash over #!/bin/bash

How to use while, until and for loops

How to use if, else, elif and case condition statements

How to use the cut command

What are files and other comparison operators, and how to use them

Requirements

Allowed editors: vi, vim, emacs

All files will be interpreted on Ubuntu 20.04 LTS

All files should end with a new line

A README.md file, at the root of the folder of the project, is mandatory

All Bash script files must be executable

You are not allowed to use awk

Your Bash script must pass Shellcheck (version 0.7.0) without any error

The first line of all Bash scripts should be exactly #!/usr/bin/env bash

The second line of all Bash scripts should be a comment explaining what the script is doing

Tasks

0. Create a SSH RSA key pair

Create a RSA key pair and share your public key in the file 0-RSA_public_key.pub

Fill the SSH public key field of your intranet profile with the public key you just generated

Keep the private key in a secure location for later use

If a passphrase is added to the key, make sure to save it in a secure location

1. For Best School loop

Write a Bash script that displays "Best School" 10 times using the for loop

2. While I am user gnu

Write a Bash script that displays "I am user gnu" while the user is gnu.

3. Until I am root

Write a Bash script that displays "I am user gnu" until the user is root.

4. If 9, say Hi!

Write a Bash script that displays "Hi" if the number stored in the environment variable BETTY is 9.

5. 4 bad luck, 8 is your chance

Write a Bash script that displays "Best School" 10 times, but for the 9th iteration, displays "Holberton School and I am an intern".

6. Superstitious numbers

Write a Bash script that displays "Best School" 10 times, but for the 4th, 5th and 6th iteration, displays "Best School and I am an intern"

7. Clock

Write a Bash script that displays the time for 12 hours and 59 minutes:

Display hours from 0 to 12

Display minutes from 1 to 59

8. For ls, in a list of words

Write a Bash script that displays:

The content of the current directory in a list format

The content of the current directory in a list format, including hidden files (starting with .). Use the ls command

The content of the current directory in a long format

The content of the current directory in a long format, including hidden files (starting with .). Use the ls -la command

9. To file, or not to file

Write a Bash script that gives you information about the school file.

10.  FizzBuzz

Write a Bash script that displays numbers from 1 to 100.


