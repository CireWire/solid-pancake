#!/usr/bin/python3

from Crypto import Random
from Crypto.Cipher import AES
import os
import os.path
from os import listdir
from os.path import isfile, join
import time

#Corny class name... check

class encrypt_maker():
  def __init__(self, key):
    self.key = key

  def pad(self, s):
    return s + b"\0" * (AES.block_size - len(s) % AES.block_size)
# Encryption function... or is this the self-destruct function... oh well.
  def encrypt(self, message, key, key_size = 256):
    message = self.pad(message)
    iv = Random.new().read(AES.block_size)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    return iv + cipher.encrypt(message)
# Encrypt the sexiness
  def encrypt_file(self, file_name):
    with open(file_name, 'rb') as fo:
      plaintext = fo.read()
    enc = self.encrypt(plaintext, self.key)
    with open(file_name + ".enc", 'wb') as fo:
        fo.write(enc)
    os.remove(file_name)
# Unlike your parents... this does have decryption...
  def decrypt(self, ciphertext, key):
    iv = ciphertext[:AES.block_size]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    plaintext = cipher.decrypt(ciphertext[AES.block_size:])
    return plaintext.rstrip(b"\0")
# Decrypt the sexiness
  def decrypt_file(self, file_name):
    with open(file_name, "rb") as fo:
      ciphertext = fo.read()
    dec = self.decrypt(ciphertext, self.key)
    with open(file_name[:-4], 'wb') as fo:
      fo.write(dec)
    os.remove(file_name)


key = b'Vc3VXn)`0:X`53&^aRr+*!tH`>)0yrM<uBnU68<p)&Zi6om?HQBCx>vil1A9/YoUkhzeCxJzoyd6LcREGhgx1PK4J'
enc = encrypt_maker(key)
clear = lambda: os.system('cls')
# This here will check if password matches to decrypt the sexiness.
if os.path.isfile('data.txt.enc'):
  while True:
    password = str(input("Please insert password: "))
    enc.decrypt_file('data.txt.enc')
    p = ''
    with open("data.txt", 'r') as f:
      p = f.readlines()
    if p[0] == password:
      enc.encrypt_file('data.txt')
      break
# This will be the first step into becoming the world's greatest spy!
  while True:
    clear()
    choice = int(input(
    "1. Press 'E' to encrypt file.\n2. Press 'D' to decrypt file. \n3. Press 'X' to exit. \n"))
    clear()

    if choice == 'E' or choice == 'e':
      enc.encrypt_file(str(input("Enter name of file you want to encrypt: ")))
    elif choice == "D" or choice == "d":
      enc.decrypt_file(str(input("Enter name of file you want to decrypt: ")))
    elif choice == "X" or choice == "x":
      exit()
    else:
      print("Please select what is shown... please. I got stuff to do!")
# Create a password to encrypt this here documents.
else:
  while True:
    clear()
    password = str(input("Let's begin. Please type a password that will be used for decryption: "))
    confirm_password = str(input("Please confirm your password: "))
    if password == confirm_password:
      break
    else:
      print("Sorry, passwords don't match...")
  f = open("data.txt", "w+")
  f.write(password)
  f.close()
  enc.encrypt_file('data.txt')
  print("Please allow program to restart to finish setting up...beep...boop...beep")
  time.sleep(10)
