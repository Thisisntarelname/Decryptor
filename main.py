import itertools
import threading
import time
import sys
import os

#Loading screen animation
done = False
def animate():
    for c in itertools.cycle(['|', '/', '-', '\\']):
        if done:
            break
        sys.stdout.write('\rLoading ' + c)
        sys.stdout.flush()
        time.sleep(0.1)

t = threading.Thread(target=animate)
t.start()

def clear():
  os.system('cls' if os.name == 'nt' else 'clear')
i=0

done = True
clear()

def ceaserCipher(key):
  print('Ceaser cipher')
def ceasercipherUnknown():
  print("Ceaser Cipher unknown")







































choice = input("Do you want to decode:\n1. Cipher Unknown\n2. Ceaser cipher\n3. Substitution cipher\n4. Atbash\n5. Bacon cipher\n6. Reverse\n7. NATO Phonetic Alphabet\n8. Affine cipher\n9. Vigenere cipher\n10. Rail Fence cipher\n")

if choice=="1":
  print("Code Unknown")
elif choice=="2":
  print("Ceaser Cipher")
  choice = input("Do you know the key? (y\n) ")
  if choice =="y":
    key = input("Enter key: ")
    ceaserCipher(key)
  else:
    ceasercipherUnkown
  
elif choice=="3":
  print("Substitution cipher")
  choice = input("Do you know the key? (y\n) ")

elif choice=="4":
  print("Atbash")
  choice = input("Do you know the key? (y\n) ")

elif choice=="5":
  print("Bacon cipher")
elif choice=="6":
  print("Reverse")
elif choice=="7":
  print("NATO Phonetic Alphabet")
elif choice=="8":
  print("Affine Cipher")
elif choice=="9":
  print("Vigenere cipher")
elif choice=="10":
  print("Rail Fence cipher")