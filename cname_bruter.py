import requests
import dns.resolver
import requests.packages.urllib3
import sys
requests.packages.urllib3.disable_warnings()
filename = ''
print('')
print("   ______  _____   __  _______    ")
print("  / ___/ |/ / _ | /  |/  / __/    ")
print(" / /__/    / __ |/ /|_/ / _/      ")
print(" \___/_/|_/_/ |_/_/  /_/___/      ")
print("    ___  ___  __  _______________ ")
print("   / _ )/ _ \/ / / /_  __/ __/ _ \\")
print("  / _  / / _/ /_/ / / / / _// , _/")
print(" /____/_/|_|\____/ /_/ /___/_/|_| ")
print("              Author- Achal Pathak")                                          
print('')
if len(sys.argv) == 3 and sys.argv[1].lower()=="-o":
    filename = sys.argv[2]
    f = open(filename, 'w')
    f.write("   ______  _____   __  _______   ")
    f.write("\n  / ___/ |/ / _ | /  |/  / __/    ")
    f.write("\n / /__/    / __ |/ /|_/ / _/      ")
    f.write("\n \___/_/|_/_/ |_/_/  /_/___/      ")
    f.write("\n    ___  ___  __  _______________ ")
    f.write("\n   / _ )/ _ \/ / / /_  __/ __/ _ \\")
    f.write("\n  / _  / / _/ /_/ / / / / _// , _/")
    f.write("\n /____/_/|_|\____/ /_/ /___/_/|_| ")
    f.write("\n              Author- Achal Pathak\n\n")
    print(" Writing to file "+filename+" plz wait...")
with open ("url_list.txt", "r") as myfile:
    data = myfile.read().splitlines()
for each in range(len(data)):
	if filename:
		f.write(" [+] "+data[each]+"\n")
	else:
		print (" [+] "+data[each])
	try:
		if data[each][:8].lower()=="https://" :
			r = requests.head(data[each])
		elif data[each][:7].lower()=="http://":
			r = requests.head(data[each])
		else:
			r = requests.head("http://"+data[each])
		if filename:
			f.write("     [Response] "+str(r.status_code)+"\n")
		else:
			print("     [Response] "+str(r.status_code))
		try:
			if data[each][:8].lower()=="https://":
				cname = dns.resolver.query(data[each][8:], 'CNAME')
			elif data[each][:7].lower()=="http://":
				cname = dns.resolver.query(data[each][7:], 'CNAME')
			else:
				cname = dns.resolver.query(data[each], 'CNAME')
			for i in cname.response.answer:
				for j in i.items:
					if filename:
						f.write("     [   CNAME] "+j.to_text()[:-1]+"\n\n")
					else:
						print ("     [   CNAME] "+j.to_text()[:-1]+"\n")
		except:
			if filename:
				f.write("     [   CNAME] "+"--Not Found--"+"\n\n")
			else:
				print("     [   CNAME] "+"--Not Found--"+"\n")
	except requests.ConnectionError:
		if filename:
			f.write("     [Response] "+"--Failed to Connect--"+"\n")
		else:
			print("     [Response] "+"--Failed to Connect--")
		try:
			if data[each][:8].lower()=="https://":
				cname = dns.resolver.query(data[each][8:], 'CNAME')
			elif data[each][:7].lower()=="http://":
				cname = dns.resolver.query(data[each][7:], 'CNAME')
			else:
				cname = dns.resolver.query(data[each], 'CNAME')
			for i in cname.response.answer:
				for j in i.items:
					if filename:
						f.write("     [   CNAME] "+j.to_text()[:-1]+"\n\n")
					else:
						print ("     [   CNAME] "+j.to_text()[:-1]+"\n")
		except:
			if filename:
				f.write("     [   CNAME] "+"--Not Found--"+"\n\n")
			else:
				print("     [   CNAME] "+"--Not Found--"+"\n")
if filename:
	f.close()
raw_input(" Press Enter to continue...")