import paramiko
import time

##########################################################################

print('')
print('================================================')
print('|                   SPRINT 2                   |')
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
	# connect to box
	print "Connecting to box ..."
	ssh = paramiko.SSHClient()
	ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	ssh.connect(server, username = server_username, key_filename = ssh_key)

	# pull code from git repo
	git_string = "https://ForNickRoss:fornickross1234@github.com/LenzDu/sprint.git"
	ssh.exec_command("rm -rf SprintSprintSprint; git clone %s SprintSprintSprint" % git_string)
	time.sleep(1) # allow git repository to be cloned
	print "Pull from Github successfully"
	
	ssh.exec_command('pkill python')
	print "Server establishing... exiting... "

	ssh.exec_command('python /home/%s/SprintSprintSprint/Amber/application.py %s' % (server_username, prefix))
	print "Server established"
	print "Only for you... %s:8080" % server

	ssh.close()

##########################################################################
## End of File ##

# Specify the parameters before running!
# deploy('sprint2.pem', 'ec2-34-216-68-78.us-west-2.compute.amazonaws.com', 'ha', server_username = 'ec2-user')




