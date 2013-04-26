from optparse import OptionParser
import subprocess
import os
parser = OptionParser()
parser.add_option("-l", "--lists", action="append", type="string", help="Listas negadas en pass")
parser.add_option("-w", "--whitelists", action="append", type="string", help="Listas pass")
parser.add_option("-d", "--dir", dest="directory", action="store", type="string",
                  help="Directorio de blacklists")
parser.add_option("-f", "--file", dest="filename", action="store", type="string",
                  help="Archivo de salida", metavar="FILE")

(options, args) = parser.parse_args()

directory = options.directory or "/usr/local/squiGuard/db"
filename = options.filename or "squidGuard.conf"
lists = options.lists or []
whitelists = options.whitelists or []

available_lists = [db_name for db_name in os.listdir(directory) if ("domains" in os.listdir("/".join([directory,db_name])) or "urls" in os.listdir("/".join([directory,db_name])))]

lists = [i for i in lists if i in available_lists] 
whitelists = [i for i in whitelists if i in available_lists]

with open(filename, 'w') as f:
	f.write("dbhome "+directory+"\n")
	f.write("logdir /usr/local/squidGuard/logs\n")
	f.write("\n")
	for lista in lists+whitelists:
		f.write("dest "+lista+" {\n")
		f.write("  domainlist "+lista+"/domains\n")
		f.write("  urllist "+lista+"/urls\n")
		f.write("}\n")
		f.write("\n")
	f.write("\n")
	f.write("acl {\n")
	f.write("  default {\n")
	f.write("    pass "+" ".join(whitelists)+" !".join([""]+lists)+" all\n")
	f.write("    redirect http://localhost/block.html\n")
	f.write("  }\n")
	f.write("}\n")
