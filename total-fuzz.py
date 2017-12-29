###############################################################################################
# Fuzzer based on Primal Security's FTP Server fuzzer.										  #
# http://www.primalsecurity.net/0x0-exploit-tutorial-buffer-overflow-vanilla-eip-overwrite-2  #
#																							  #
# This fuzzer is made for fuzzing any target TCP connection, just change the port number and  #
# whatever other parameters the protocol that you are fuzzing requires. At the moment,        #
# this is set up for an FTP server.                      									  #
#																							  #
# the fuzzer sends 100 of each character from 0-255 in the hex table. Increase or decrese     #
# this how you see fit.  																	  #
#																							  #
# The reason for sending every character and not just AAAAAAAA is because some applications   #
# can be tricky and don't crash with just any character. Sometimes only specific ones will    #
# cause a crash.																	          #
#																							  #
# Enjoy and feel free to fork and improve this code in any way like any of my code.			  #
###############################################################################################

import sys, socket
from time import sleep

target = sys.argv[1]

chars = ['\x01', '\x02', '\x03', '\x04', '\x05', '\x06', '\x07', '\x08', '\x09', '\x0a', 
		'\x0b', '\x0c', '\x0d', '\x0e', '\x0f', '\x10', '\x11', '\x12', '\x13', '\x14', 
		'\x15', '\x16', '\x17', '\x18', '\x19', '\x1a', '\x1b', '\x1c', '\x1d', '\x1e', 
		'\x1f', '\x20', '\x21', '\x22', '\x23', '\x24', '\x25', '\x26', '\x27', '\x28', 
		'\x29', '\x2a', '\x2b', '\x2c', '\x2d', '\x2e', '\x2f', '\x30', '\x31', '\x32', 
		'\x33', '\x34', '\x35', '\x36', '\x37', '\x38', '\x39', '\x3a', '\x3b', '\x3c', 
		'\x3d', '\x3e', '\x3f', '\x40', '\x41', '\x42', '\x43', '\x44', '\x45', '\x46', 
		'\x47', '\x48', '\x49', '\x4a', '\x4b', '\x4c', '\x4d', '\x4e', '\x4f', '\x50', 
		'\x51', '\x52', '\x53', '\x54', '\x55', '\x56', '\x57', '\x58', '\x59', '\x5a', 
		'\x5b', '\x5c', '\x5d', '\x5e', '\x5f', '\x60', '\x61', '\x62', '\x63', '\x64', 
		'\x65', '\x66', '\x67', '\x68', '\x69', '\x6a', '\x6b', '\x6c', '\x6d', '\x6e', 
		'\x6f', '\x70', '\x71', '\x72', '\x73', '\x74', '\x75', '\x76', '\x77', '\x78', 
		'\x79', '\x7a', '\x7b', '\x7c', '\x7d', '\x7e', '\x7f', '\x80', '\x81', '\x82', 
		'\x83', '\x84', '\x85', '\x86', '\x87', '\x88', '\x89', '\x8a', '\x8b', '\x8c', 
		'\x8d', '\x8e', '\x8f', '\x90', '\x91', '\x92', '\x93', '\x94', '\x95', '\x96', 
		'\x97', '\x98', '\x99', '\x9a', '\x9b', '\x9c', '\x9d', '\x9e', '\x9f', '\xa0', 
		'\xa1', '\xa2', '\xa3', '\xa4', '\xa5', '\xa6', '\xa7', '\xa8', '\xa9', '\xaa', 
		'\xab', '\xac', '\xad', '\xae', '\xaf', '\xb0', '\xb1', '\xb2', '\xb3', '\xb4', 
		'\xb5', '\xb6', '\xb7', '\xb8', '\xb9', '\xba', '\xbb', '\xbc', '\xbd', '\xbe', 
		'\xbf', '\xc0', '\xc1', '\xc2', '\xc3', '\xc4', '\xc5', '\xc6', '\xc7', '\xc8', 
		'\xc9', '\xca', '\xcb', '\xcc', '\xcd', '\xce', '\xcf', '\xd0', '\xd1', '\xd2', 
		'\xd3', '\xd4', '\xd5', '\xd6', '\xd7', '\xd8', '\xd9', '\xda', '\xdb', '\xdc', 
		'\xdd', '\xde', '\xdf', '\xe0', '\xe1', '\xe2', '\xe3', '\xe4', '\xe5', '\xe6', 
		'\xe7', '\xe8', '\xe9', '\xea', '\xeb', '\xec', '\xed', '\xee', '\xef', '\xf0', 
		'\xf1', '\xf2', '\xf3', '\xf4', '\xf5', '\xf6', '\xf7', '\xf8', '\xf9', '\xfa', 
		'\xfb', '\xfc', '\xfd', '\xfe', '\xff']

count = 0

for num in chars:

	try:
		buff = num*100
	 
		s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		s.settimeout(2)
		s.connect((target,21))
		s.recv(1024)
		
		print "####################################################################################"
		print "[+] Iteration: "
		print count
		print "[+] BUFFER CHARACTER: " + num*10
		print "\r\n"
		print "####################################################################################"
		
		s.send("USER " + buff)
		s.close()
		count += 1
		sleep(1)
	
	except:
		print "[+] Crash occured: "
		sys.exit()