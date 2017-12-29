+ Fuzzer based on Primal Security's FTP Server fuzzer.										  +
+ http://www.primalsecurity.net/0x0-exploit-tutorial-buffer-overflow-vanilla-eip-overwrite-2  +
+																							  +
+ This fuzzer is made for fuzzing any target TCP connection, just change the port number and  +
+ whatever other parameters the protocol that you are fuzzing requires. At the moment,        +
+ this is set up for an FTP server.                      									  +
+																							  +
+ the fuzzer sends 100 of each character from 0-255 in the hex table. Increase or decrese     +
+ this how you see fit.  																	  +
+																							  +
+ The reason for sending every character and not just AAAAAAAA is because some applications   +
+ can be tricky and don't crash with just any character. Sometimes only specific ones will    +
+ cause a crash.																	          +
+																							  +
+ Enjoy and feel free to fork and improve this code in any way like any of my code.			  +