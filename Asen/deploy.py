#!/usr/bin/env python

import paramiko
import time

##########################################################################

print('')
print('================================================')
print('|                   SPRINT 1                   |')
print('================================================')
print('|                                              |')
print('|        Group Name: SprintSprintSprint        |')
print('|                                              |')
print('|    Bingyi Li, Guoqiang Liang, Lingzhi Du     |')
print('|    Feiran Ji, Vanessa Zheng, Zizhen Song     |')
print('|                                              |')
print('================================================')
print('')
print('')

##########################################################################

def deploy(ssh_key, server, prefix, server_username = 'testtest'):
	# Question 1
	print "Connecting to box ..."
	ssh = paramiko.SSHClient()
	ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	ssh.connect(server, username = server_username, key_filename = ssh_key)

	# Question 2
	git_string = "https://ForNickRoss:fornickross1234@github.com/LenzDu/sprint.git"
	ssh.exec_command("rm -rf whatever; git clone %s whatever" % git_string)
	print "Pull from Github successful"

	# Question 3
	# Depending on the objective, we may not want to include the next line?
	# ssh.exec_command('crontab -r')
	ssh.exec_command('(crontab -l ; echo "*/5 * * * * python /home/%s/whatever/Asen/program.py %s") | crontab -' % (server_username, prefix))

	time.sleep(1)
	print "Script fully executed ... exiting" 
	ssh.close()

##########################################################################
## End of File ##

# Specify the parameters before running!
