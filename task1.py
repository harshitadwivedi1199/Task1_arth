import pyttsx3
import os
import subprocess as sb
import webbrowser
import speech_recognition as sr



pyttsx3.speak("Hey Welcome to my tools")
pyttsx3.speak("Whats your name")
print("Whats ur name")
#name=speech()
name=input()
pyttsx3.speak("Okay  {} ".format(name))

while(True):
	print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
	#print(" How can i help you: ",end=" ")
	pyttsx3.speak("How can i help you")
	print("Your requirement:",end="")
	#p=speech()
	p=input()
	print(p)
	#p=input()
	p=p.lower()
	if (("run" in p ) or ("open" in p))  and ("chrome" in p):
		pyttsx3.speak("Opening Google chrome")
		os.system("chrome")
	elif ((("run" in p ) or ("execute" in p) or ("open" in p)) and (("notepad" in p) or ("editor" in p))) or("notepad" in p) :
		pyttsx3.speak("Opening notepad")
		n=sb.getoutput("notepad")
	elif ((("run" in p ) or ("execute" in p) or ("open" in p)) and (("player" in p) or ("media" in p))) or ("media player" in p):
		pyttsx3.speak("Opening windows media player")
		os.system("wmplayer")		
	elif ((("run" in p ) or ("execute" in p) or ("open" in p)) and (("internet" in p) or ("explorer" in p))) or ("internet explorer" in p):
		pyttsx3.speak("Opening internet explorer")
		os.system("iexplore")
	elif ((("run" in p) or ("execute" in p) or ("open" in p))	and (("vlc" in p) or ("video player" in p))) or ("vlc" in p) or  ("video player" in p):
		pyttsx3.speak("Opening vlc ")
		os.system("vlc")
	elif ((("run" in p ) or ("execute" in p) or ("open" in p)) and ("telegram" in p)) or ("telegram" in p):
		pyttsx3.speak("Opening telegram")
		os.system("telegram")	
	elif ((("run" in p ) or ("execute" in p) or ("open" in p)) and ("teamviewer" in p)) or ("teamviewer" in p):
		pyttsx3.speak("Opening TeamViewer")
		os.system("teamviewer")	
	elif (("run" in p ) or ("open" in p)) and ("google" in p):
		pyttsx3.speak("Opening Google")
		webbrowser.open("https://www.google.com/")
	elif("close" in p) and ("Google" in p):
		pyttsx3.speak("Closing Google")
		webbrowser.close("https://www.google.com/")
		print("Facebook closed")		
	elif((("run" in p ) or ("open" in p)) and ("facebook" in p)) and ("facebook" in p):
		pyttsx3.speak("opening facebook")
		webbrowser.open("https://www.facebook.com/")
		#print("Facebook closed")
	#elif ((("run" in p ) or ("open" in p)) and ("facebook" in p)) or ("facebook" in p) :
		#pyttsx3.speak("Opening facebook")
		#os.kill("https://www.facebook.com/")
		#webbrowser.open("https://www.facebook.com/")
	elif ((("run" in p ) or ("open" in p)) and ("linkedin" in p)) or ("linkedin" in p):
		pyttsx3.speak("Opening linkedin")
		webbrowser.open("http://www.linkedin.com/")
	elif ("cal" in p) or ("calender" in p):
		pyttsx3.speak("Wait showing calender")
		os.system("curl http://192.168.0.107/cgi-bin/form.py?c=cal")
		#webbrowser.open("http://192.168.0.107/cgi-bin/form.py?c=cal")
	elif ("date" in p):
		pyttsx3.speak("Wait showing date")
		os.system("curl http://192.168.0.107/cgi-bin/form.py?c=date")
		#webbrowser.open("http://192.168.0.107/cgi-bin/form.py?c=date")
	elif ("make" in p) or ("directory" in p) or ("file" in p):
		pyttsx3.speak("Tell me your new directory name")
		print("Directory name:")
		dname=input()
		pyttsx3.speak("Wait creating directory in virtual machine")
		#os.system("curl http://192.168.0.107/cgi-bin/form.py?c=mkdir {}".format(dname))
		webbrowser.open("http://192.168.0.107/cgi-bin/form.py?c=mkdir {}".format(dname))			
	elif ("exit" in p) or ("quit" in p) or ("close" in p):
		#print("Thankyou {} ".format(name))
		#pyttsx3.speak("Okay")
		pyttsx3.speak("Have a good day {}".format(name))
		print("Thankyou {} ".format(name))
		pyttsx3.speak("Thankyou !")
		break
	else:
		pyttsx3.speak("Sorry cant help you {} ")
		pyttsx3.speak("Try again")
		print("try again")	
	'''
	elif("command" in p):
		pyttsx3.speak("Enter command")
		print("Command:")
		cmd=input()
		if(cmd == "cal"):
			webbrowser.open("http://192.168.0.107/cgi-bin/form.py?c=cal")
		elif(cmd == "date"):
			webbrowser.open("http://192.168.0.107/cgi-bin/form.py?c=date")			
	'''
