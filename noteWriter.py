from evernote.api.client import *
from evernote.edam.type import ttypes as Types
from evernote.edam.notestore import ttypes as NoteStoreTypes
import time

dev_token="S=s1:U=8f584:E=14fa4b14194:C=1484d0014a0:P=1cd:A=en-devtoken:V=2:H=05ec5b5cb0c2ca942f6814c699b46678"

token = dev_token

client = EvernoteClient(token=dev_token)
userStore = client.get_user_store()
noteStore = client.get_note_store()
user = userStore.getUser()
# print user.usernamek

# checke & create notebook
# print(dir(userStore))
notebooks = noteStore.listNotebooks()

notebookName = "Food Roulette"
notebook = None

# exist
for n in notebooks:
    if n.name == notebookName:
        notebook = n
    
# doesn't exist
if notebook == None:
    new_notebook = Types.Notebook()
    new_notebook.name = notebookName
    notebook = noteStore.createNotebook(token, new_notebook)
        
notebookGuid = notebook.guid
#===================test================
# actually created?
# print noteStore.listNotebooks()
# print notebook.name

# create & check for today
date = time.strftime("%c").split(' ')[:4]
noteName = date[0] + ' ' + date[1] + ' ' + date[2] + date[3]

# get note of today
notes = noteStore.findNotes(token, NoteStoreTypes.NoteFilter(notebookGuid = notebook.guid, words = noteName), 0, 100).notes

# check if there's any note today
if len(notes) == 0:
    # if not, create it
    note = Types.Note()
    note.title = noteName
    note.content = '<?xml version=\"1.0\" encoding=\"UTF-8\"?>'
    note.content += '<!DOCTYPE en-note SYSTEM \"http://xml.evernote.com/pub/enml2.dtd\">'
    note.content += '<en-note></en-note>'
    note.notebookGuid = notebookGuid
    note = noteStore.createNote(token, note)
else:
    note = notes[0]
    
def writeToNote(foodString):
    # guid = note.guid
    # name = note.title
    # print note
    content = noteStore.getNoteContent(token, note.guid)
    prev = content[:-10]
    end = content[-10:]
    prev += foodString
    prev += end
    note.content = prev
    noteStore.updateNote(token, note)
    
# while True:
#     writeToNote(input('enter: '))