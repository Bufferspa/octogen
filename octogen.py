from optparse import OptionParser

parser = OptionParser()
parser.add_option("-f", "--file", dest="filename",
                  help="write report to FILE", metavar="FILE")
parser.add_option("-q", "--quiet",
                  action="store_false", dest="verbose", default=True,
                  help="don't print status messages to stdout")

(options, args) = parser.parse_args()

with open('squidGuard.conf', 'w') as f:
	f.write("dbhome /usr/local/squidGuard/db")
	f.write("logdir /usr/local/squidGuard/logs")
	

dest porn {
        domainlist porn/domains
        urllist porn/urls
        }

acl {
        default {
                pass !porn all
                redirect http://localhost/block.html
        }
 }
