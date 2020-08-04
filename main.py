import os
import datetime
from shutil import rmtree

path = ''#put your project directory here
def main():
	'''Main control function'''
	os.chdir(path)

	print('\n'*20)
	print('JOURNAL TIME')
	print('LETS ROCK N ROLL')
	print('\n')
	print('here are your options: ')
	print('1: Create a new journal')
	print('2: See all existing journals')
	print('3: Rename an existing journal')
	print('4: Remove an existing journal')
	print('5: Exit')

	choice = int(input('Pick a number from the above options: '))

	if choice == 1:
		create_new_journal()
	elif choice == 2:
		open_journal()
	elif choice == 3:
		rename_journal()
	elif choice == 4:
		remove_journal()
	elif choice == 5:
		quit()
	else:
		print('not a valid option')
		main()


def create_new_journal():
	''' Function for creating a new journal directory '''
	print('\n'*20)
	# obtaining name, folder name, and cwd variables
	folder_name = input('Name of your new journal: ').replace(' ','-') #this will be the folders name
	author = input('What is your name? ') #this will be copied into any entry in this journal

	cwd = os.getcwd()

	# create a path
	path = cwd +'/'+folder_name

	# create a dir
	try:
		os.mkdir(path)
	except OSError as e:
		print(e)
	else:
		print(f'Successfully created directory: {path}')
		print('\n')
	
	# an author.txt file be created for each journal automatically
	os.chdir(path)
	with open('author.txt','w') as a:
		a.write(f'{author}')

	#giving the user the option to create a first intial entry
	enter = input('wanna write an entry? (y/n) ')
	if enter[0].lower() == 'y':
		create_entry() 
	else:
		main()


def open_journal():
	''' Function for opening an existing journal
		Returns a list of open journal and gives the ootion to choose
	 '''
	print('\n'*20)
	# change to main dir
	os.chdir(os.getcwd())
	# get open journal as a list
	journal_list = os.listdir()

	# loop thru journals
	print(f'Current open journals: {len(journal_list)}') #shoiwing how many are currently open
	for index, journal in enumerate(journal_list): # i use enumerate to make selecting easier
		print(index, journal)

	# get name of open journal
	choice = int(input('which journal would you like to open? ')) #we return a integer for the index

	#getting the journal by the given index and changing our directory
	journal = journal_list[choice]
	path = os.getcwd() + '/'+ journal
	os.chdir(path)

	# display entries
	entry_list = os.listdir()
	print('\n'*20)
	print(f'Current entries: {len(entry_list)}')
	for entry in entry_list:
		print(entry)

	# getting a choice from the user
	print('\n'*2)
	print('what would you like to do? ')
	print('1: Add an entry')
	print('2: Delete an entry')
	print('3: Read an entry')
	print('4: Back')
	print('\n')

	option = int(input('well choose already: '))

	if option == 1:
		create_entry()
	elif option == 2:
		remove_entry()
	elif option == 3:
		open_entry()
	elif option == 4:
		main()
	else:
		main()


def open_entry():
	''' function for reading an existing entry '''

	print('\n'*20)
	# option are the curren entry txt files
	options = os.listdir()
	for index, option in enumerate(options): #again, i used enumerare() to make selecting easier for the user
		print(index, option)

	choice = int(input('Which entry would you like to read? '))
	file_name = options[choice]

	print('\n'*15)

	stuff = open(file_name, 'r')
	text = stuff.read()
	print(text)
	stuff.close()
	
	done = input('Type anything to go back  ')
	if done:
		main()


def get_content():
	''' Function for getting entry content
		this func is kinda superflous and could be replaced with a single line of code if needed
	 '''
	content = input('Type away: ')
	return(content)



def create_entry():
	''' Function for adding a new entry to an existing journal '''
	print('\n'*20)
	
	item_list = os.listdir() #this will list the journals direcory (py/journal/(journal-name))

	for item in item_list:
		print(item)

	# this is why i create the author.txt file at the beginning
	with open('author.txt','r') as a:
		author = a.read()

	# get a title for entry
	title = input('Title: ')

	date = datetime.datetime.now() #getting the current date
	my_date = f'{date.day}-{date.month}-{date.year}' #formatiting it bc god knows the datetime module doesnt do that for us

	entry_name = title.replace(' ','-')+ '_' + my_date +'.txt' #the file name will be the title plus the date it was created

	# fetch content
	content = get_content()


	# create file with title
	entry = open(entry_name, 'a')

	# open and write to file
	entry.write(f"Title: {title}" + '\n') #writing the title
	entry.write(f"Date: {my_date}" +'\n') #writing the date
	entry.write(f"Author: {author}" +'\n') # writing the author
	
	# ok this is a little complicated
	count = 0
	prev = 0
	for i in range(0, len(content)-1):
		if content[i] == " ": # i write each word individually with a counter that goes to ten
			entry.write(content[prev:i])
			count += 1
			prev = i
		if count == 10: # when the word count goes to ten, it writes a new line
			entry.write('\n')
			count = 0 # here we go again
		# for some reason this will sometimes not write the last word, a way arund this is to add some whitespace at the end


	entry.close()
	print(f'Successfully added entry {title}')
	main()



def remove_entry():
	'''Remove an entry file from a journal'''
	print('\n'*20)

	entry_list = os.listdir()
	for index, entry in enumerate(entry_list): # heres that enumerate() again
		print(index, entry)

	index = int(input('Which entry to remove? '))
	entry = entry_list[index]
	os.remove(entry) #deleting the file

	print(f'Successfully removed file {entry}')

	main() #take me hooooommmmeeee

def remove_journal():
	''' Function to remove an entire journal and all its entries '''
	print('\n'*20)


	journal_list = os.listdir()
	for index, journal in enumerate(journal_list): # enumerate(), again, you get the point
		print(index, journal)

	index = int(input('Which journal would you like to kil- i mean delete: '))
	journal = journal_list[index]

	# I use shutil.rmtree for this, deletes a non-empty folder with ease
	rmtree(journal) 
	print(f"Successfully delete directory: {journal} ")

	main()


def rename_journal():
	''' Function to rename an existing journal '''
	print('\n'*20)

	journal_list = os.listdir()

	for index, journal in enumerate(journal_list):
		print(index, journal)

	index = int(input('Which journal to rename? '))
	journal = journal_list[index]

	new_name = input('New name: ').replace(' ','-')

	os.rename(journal, new_name)
	print(f'Successfully renamed {journal} to {new_name}')

	main()


if __name__ == '__main__':
	main()




