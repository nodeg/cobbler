#!/usr/bin/python3

from xmlrpc.client import ServerProxy
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-u","--user",dest="user",default="test")
parser.add_argument("-p","--pass",dest="password",default="test")

sp =  ServerProxy("http://127.0.0.1/cobbler_api")
args = parser.parse_args()
token = sp.login(args.user,args.password)

sp.read_autoinstall_snippet("some-snippet",token)
