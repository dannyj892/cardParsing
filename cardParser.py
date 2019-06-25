# Asymmetrik Programming Challenge
# Daniel Jun
# June 24, 2019

import enchant
import string
import sys
from genderize import Genderize
from pathlib import Path

class ContactInfo:
	def __init__(self, name, phoneNumber, emailAddress):
		self.name = name
		self.phoneNumber = phoneNumber
		self.emailAddress = emailAddress

	def getName(self):
		return self.name

	def getPhoneNumber(self):
		return self.phoneNumber

	def getEmailAddress(self):
		return self.emailAddress

class BusinessCardParser:
	def __init__(self):
		name = "N/A"
		phoneNumber = "N/A"
		emailAddress = "N/A"
		contactInfo = ContactInfo(name, phoneNumber, emailAddress)
		self.contactInfo = contactInfo

	def getContactInfo(self, document):
		fileToOpen = document

		with open(fileToOpen) as file:
			data = file.readlines()
			self.contactInfo.name = self.findName(data)
			self.contactInfo.phoneNumber = self.findNumber(data)
			self.contactInfo.emailAddress = self.findEmail(data)

		print ("Name: ", (self.contactInfo.getName()))
		print ("Number: ", (self.contactInfo.getPhoneNumber()))
		print ("Email: ", (self.contactInfo.getEmailAddress()))
		return self.contactInfo

	def findName(self, data):
		dictionary = enchant.request_pwl_dict("firstNames.txt")
		name = "N/A"
		for line in data:
			wordList = line.split()
			isName = False
			for word in wordList:
				if dictionary.check(word) == True:
					isName = True
			if isName:
				name = line.lstrip().rstrip()
		return name

	def findNumber(self, data):
		number = "N/A"
		for line in data:
			new = ''
			if line.upper().find("FAX") == -1:
				for letter in line:
					if (letter.isdigit()):
						new+=letter
				if len(new) >= 10:
					number = new
				else:
					new = ''
		return number

	def findEmail(self, data):
		email = "N/A"
		for line in data:
			if line.rfind("@") != -1:
				emailLine = line.split()
				for word in emailLine:
					if word.rfind("@") != 1:
						email = word
		return email

businessCardParser = BusinessCardParser()

textFile = input("Input text file: ")
businessCardParser.getContactInfo(textFile)
