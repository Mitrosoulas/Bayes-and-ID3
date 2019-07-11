windowsFlag = True
try:
	import winsound
except ImportError:
	windowsFlag = False
music = False
import sys
sys.path.insert(0,'./ID3')
sys.path.insert(0,'./Bayes')
import test
import main
import ctypes


while(True):

	print("****************************************************************")
	print("\t\t\tP3150014 & P3150165")
	print("\t\t    MACHINE LEARNING ASSIGNMENT\t\t")
	print("\n\n\t   SUPPORTED ALGORITHMS ARE ID3 AND NAIVE BAYES")
	print("******************")
	print("* 1. NAIVE BAYES *")
	print("******************")
	print("**********")
	print("* 2. ID3 *")
	print("**********")
	if (windowsFlag):
		print("************")
		print("* 3. MUSIC *")
		print("************")
	choice = input("\nENTER CHOICE: ")
	if choice == "1":
		answ = main.run()
		ctypes.windll.user32.MessageBoxW(0, answ, "NAIVE BAYES", 1)
	elif choice == "2":
		answ = test.run()
		ctypes.windll.user32.MessageBoxW(0, answ, "ID3", 1)
	elif choice == "3" and windowsFlag:
		
		if music == False:
			print("****************************")
			winsound.PlaySound("aoua.wav",winsound.SND_FILENAME | winsound.SND_LOOP | winsound.SND_ASYNC)
			ctypes.windll.user32.MessageBoxW(0, "ENTER 3 AGAIN TO STOP PLAYING", "PKMN CRYSTAL", 1)
			music = True
		elif music == True:
			winsound.PlaySound(None, winsound.SND_FILENAME)
			music = False
	
	
	
	
	
	
	
	print("******************************************************************************")
