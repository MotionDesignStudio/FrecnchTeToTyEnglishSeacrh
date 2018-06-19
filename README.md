# FrecnchTeToTyEnglishSeacrh

A best friend of mine Raphael wrote this on Facebook :

Language nerds:
patty (as in hamburger) and pâté...
same thing!

After speaking with him.  It became clearer to me that he was establishing the path of words from Latin to French to English.

Words with té as a suffix in French end up in English with a ty ending.  I am not sure if this is a absolute binary connection.  The process to discover more words that fit neatly into this observation are below.

The script can be modified for any suffix of words from a different language to compare against the English translated with very little modification. 


] Set Environmental Variables, Enter This Commandline [

You must crate a Google translation account to get this file.

EXAMPLE :  export GOOGLE_APPLICATION_CREDENTIALS="/home/user/Downloads/[FILE_NAME].json"

]    Use this to download and create text containing a comprehensive list of English words ending in ty.  [
This list we will use to search for French words.  Once we do the translation any French word that does not end with té  will be omited.

curl http://mo-de.net/d/wordsEn.txt  | egrep -i -h ".*ty$" | sort > englishTY.txt

] Must Do : Install these packages for Python 3. [

pip3 install --upgrade google-cloud-translate

] Links [

The source of the English words list. 
http://www-01.sil.org/linguistics/wordlists/english/

Information about getting and setting up a Google translate account.
https://cloud.google.com/translate/docs/reference/libraries#client-libraries-install-python
https://cloud.google.com/translate/docs/
