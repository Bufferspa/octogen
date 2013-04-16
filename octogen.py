from optparse import OptionParser

parser = OptionParser()
parser.add_option("-l", "--lists", action="append", type="str", help="Listas negadas en pass")
parser.add_option("-w", "--whitelists", action="append", type="str", help="Listas pass")
parser.add_option("-f", "--file", dest="filename",
                  help="Archivo de salida", metavar="FILE")

(options, args) = parser.parse_args()

lists = options.lists or []
whitelists = options.whitelists or []

with open('squidGuard.conf', 'w') as f:
	f.write("dbhome /usr/local/squidGuard/db\n")
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
	f.write("    pass !"+" !".join(lists)+" "+" ".join(whitelists)+" all\n")
	f.write("    redirect http://localhost/block.html\n")
	f.write("  }\n")
	f.write("}\n")
