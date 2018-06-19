#!/usr/bin/env python3.6

from time import sleep

class translateWords:
	# Imports the Google Cloud client library
	from google.cloud import translate

	# Instantiates a client
	translate_client = translate.Client()
	
	def __init__(self, myWord, destinationLanguage):
		self.myWord = myWord
		self.destinationLanguage = destinationLanguage
		
	def translationMyWord(self):
		# Translates some text into French
		translation = self.translate_client.translate(
			self.myWord,
			target_language=self.destinationLanguage)

		return u'{}'.format(translation['translatedText'])
		
if __name__ == "__main__":
	
	#Loop over list of words
	def loopOverListOfWords( filename ):
		with open (filename) as f:
			for line in f:			
				#create Translated Object.  Ths is a design flaw and should only be done once.

				translated = translateWords( line.strip() , "fr");
				
				if translated.translationMyWord()[-2:] == "té" :
					print( translated.translationMyWord() + " | "  + line.strip(), file= open ("translated.txt", "a") )

				# Many words can be translated from English to French we are searching for words that end with té
				# The té ending we are tracing to English word 
				
				if "str" in line:
					break
				sleep(4)	# Adjust this timeout to match how much bandwidth and volume of requests
				#you cna make before your code fails and you manually resume
	
	#Thsi is the text file containing the source langage.
	loopOverListOfWords( "englishTY.txt" )
	

#If confused why I used __main__ http://ibiblio.org/g2swap/byteofpython/read/module-name.html
		
		