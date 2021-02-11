import base64
import os
from kahoot import client
import threading
from threading import *
import requests
screen_lock = Semaphore(value=1)
import colorama
from colorama import Fore
from dhooks import Webhook
from itertools import cycle
import ctypes
import termcolor
from termcolor import colored 
os.system('color')
buys = []





def checkcookiees():
  req = requests.Session()
  cookiefilefolder = os.path.dirname(__file__)
  cookiefile = (cookiefilefolder + "cookies.txt")
  cookie = open(cookiefile).read().splitlines()
  validcount = 0
  invalidcount = 0
  
  if len(cookie) > 0:
    print(str(len(cookie)) + " Cookie(s) Found")
    print(" ")
    pathnameforvalid = os.path.join(os.path.dirname(__file__), "validcookies.txt")
    newfileforvalid = open(pathnameforvalid, "w")
    newfileforvalid.truncate(0)
    pathnameforinvalid = os.path.join(os.path.dirname(__file__), "invalidcookies.txt")
    newfileforinvalid = open(pathnameforinvalid, "w")
    newfileforinvalid.truncate(0)
    for line in cookie:
        check = req.get('https://api.roblox.com/currency/balance', cookies={'.ROBLOSECURITY': str(line)})
        if check.status_code == 200:
            newfileforvalid.write(str(line) + "\n")
            validcount += 1
        else:
            newfileforinvalid.write(str(line) + "\n")
            invalidcount += 1
    print("Valid Cookie(s): " + str(validcount) + "\nInvalid Cookie(s):" + str(invalidcount))
    
  else:
    print("No cookies found.")

def botwithcookies():
  cookiesFile = open('cookies.txt', 'r');
  cookies = cookiesFile.read().split('\n');
  user_ID = input('Roblox\'s user ID?\nType the user ID... ');
  proxiesFile = open('proxies.txt', 'r');
  proxies = proxiesFile.read().split('\n');
  if proxies[0] == '':
    print('\x1b[33mNo proxies detected. The code will error.\x1b[0m');
  if cookies[0] == '':
    print('\x1b[33mThis feature will not work without cookies.\x1b[0m');
  for cookie in cookies:
    for proxy in proxies:
      proxyObj = {
        'https': 'https://{proxyThing}'.format(proxyThing=proxy),
        
      };
  print('\x1b[32mSending {amount} follower(s) to {user}\x1b[0m'.format(amount=len(cookies), user=user_ID));
  csrfHeaders = {
    'Cookie': '.ROBLOSECURITY=' + cookie,
    };
    ## CSRF Request ##
  try:
      csrfRequest = requests.post('https://auth.roblox.com/v2/logout', headers=csrfHeaders, proxies=proxyObj);
      ## If Statement For CSRF ##
      if csrfRequest.status_code == 403:
        csrfToken = csrfRequest.headers['x-csrf-token'];
        ## Headers ##
        headers = {
          'X-CSRF-TOKEN': csrfToken,
          'Cookie': '.ROBLOSECURITY=' + cookie,
        };
        ## Follow Request ##
        r = requests.post('https://friends.roblox.com/v1/users/{user}/follow'.format(user=user_ID), headers=headers);
        ## If Statement For Follow Botter ##
        if r.status_code == 200:
          print('\x1b[32mSuccessfully followed! Status code: 200\x1b[0m');
        ## Else Statement For Follow Botter ##
        elif r.status_code == 401:
          print('\x1b[31mInvalid cookie. Status code: 401\x1b[0m'); 
      ## Else Statement For CSRF ##
      else:
        print('\x1b[31mGetting the CSRF Token will not work with invalid cookies.\x1b[0m');
  except OSError as e:
    print('\x1b[31mAn error has occured! ' + e + '\x1b[0m')


guffyguppy = input ("")
if guffyguppy == "1":
  def Dencrypt():
    choice = input("If you want to decrypt enter 'D' or if you wanna encrypt enter 'E': ")
  choice2e = input ("If you want to decrypt enter 'D' or if you wanna encrypt enter 'E': ")
  if (choice2e == 'D'):
    decode = input("Enter something to decode by base family: ")
    # try:
    #     print("\nAs bytes Encoded: ", base64.decodebytes(decode))
    # except:
    #     print("\nIt's not an bytes encoded, trying to decode with base16 algorithm...")
    try:
        print("Base16 Decoded: ", base64.b16decode(decode))
    except:
        print("It's not an base16 encoded, trying to decode with base32 algorithm...")
    try:
        print("Base32 Decoded: ", base64.b32decode(decode))
    except:
        print("It's not an base32 encoded, trying to decode with base64 algorithm...")
    try:
        print("Base64 Decoded: ", base64.b64decode(decode).strip())
    except:
        print("It's not an base64 encoded, trying to decode with base85 algorithm...")
    try:
        print("Base85 Decoded: ", base64.b85decode(decode))
    except:
        print("It's not an base85 encoded, it's not base85 algorithm...")
    
  elif (choice2e =='E'):
    encode = input("Enter something to encode by base family: ")
    # try:
    #     encode1 = encode.encode('ascii')
    #     encode2 = base64.encodebytes(encode1)
    #     encode3 = encode2.decode('ascii')
    #     print("\nEncoded by Bytes:  ",encode3, end='')
    # except:
    #     print("\nSo sorry, Something went wrong..")
    try:
        encode1 = encode.encode('ascii')
        encode2 = base64.b16encode(encode1)
        encode3 = encode2.decode('ascii')
        print("Encoded by Base16: ",encode3)
    except:
        print("So sorry, Something went wrong..")
    try:
        encode1 = encode.encode('ascii')
        encode2 = base64.b32encode(encode1)
        encode3 = encode2.decode('ascii')
        print("Encoded by Base32: ",encode3)
    except:
        print("So sorry, Something went wrong..")
    try:
        encode1 = encode.encode('ascii')
        encode2 = base64.b64encode(encode1)
        encode3 = encode2.decode('ascii')
        print("Encoded by Base64: ",encode3)
    except:
        print("So sorry, Something went wrong..")
    try:
        encode1 = encode.encode('ascii')
        encode2 = base64.b85encode(encode1)
        encode3 = encode2.decode('ascii')
        print("Encoded by Base85: ",encode3)
    except:
        print("So sorry, Something went wrong..")
   
  else:
    print("Wrong selected you've made, Give 1 or 2 as return!")

elif guffyguppy == "2":
  def join(bot, id, username, b):
    bot.join(id,username + str(b))
    screen_lock.acquire()
    print(f"Send bot {username + str(b)} to kahoot {id}")
    screen_lock.release()
  id = input("Enter an id: ")
  x = input("Enter a bot username: ")
  def get_choices(challengeId):
    try:
        r = requests.get(f"https://kahoot.it/rest/challenges/{challengeId}/answers").json()
        data = r['answers']
        counter = 0
        for i in data:
            choices = i['question']['choices']
            threading.Thread(target=get_correct_answer, args=[choices,]).start()
    except Exception as e:
        print(e)
  def get_correct_answer(choices):
    try:
        for i in choices:
            if i['correct'] == True:
                print(f"{i['answer']}")
            else:
                pass
    except Exception as e:
        print(e)
  threading.Thread(target=get_choices, args=["a0c57b82-6814-42a9-bdf4-d7a420e3e62d"]).start()
  b = 0
  while True:
    b+=1
    bot = client()
    threading.Thread(target=join, args=[bot, id, x, b]).start()

elif guffyguppy == "3":
  checkcookiees()

elif guffyguppy == "4":
  Webhoook = input ("Please enter your webhook ")
  hook = (Webhoook)
  x = (string.ascii_letters+string.digits)
  print ("Contacting DiscordApi...")
  time.sleep(2)
  print ("Setting up webhook...")
  time.sleep(2)
  print ("Starting...")
  time.sleep(1)
  while True:
    time.sleep(0.5)
    hook.send ("https://discord.gift/" + ''.join(random.sample(x, 19)))
    print (Fore.Green + "Successfully sent!") 

elif guffyguppy == "5":
  botwithcookies()

elif guffyguppy == "6":
  from dhooks import Webhook
  webtonuke = input ("Webhook to spam: ")
  hook = Webhook(webtonuke)
  while True:
    time.sleep(0.5)
    hook.send("@everyone RETARD ALERT @everyone")
    print ("sent!")
