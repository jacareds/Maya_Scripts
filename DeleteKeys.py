################################################################################################
#
#           Delete Keys version 1.0
#                                           
#  Delete selected Keys.
#
#  author:  Jose Paulo Gomes Filho
#  contact: jacareds@gmail.com
#
#  Instruction: set in maya node Shelves actions :
#  import maya.cmds as cmds
#  import DeleteKeys
#  reload(DeleteKeys)
#  DeleteKeys.noSeletedKeys()
#
################################################################################################

import maya.cmds as cmds

#get content of selection
sel = cmds.ls(selection=True, long=False);

def delKeys():
	cmds.cutKey( sel )
	#declare variable
	global window
	#Create UI
	window = cmds.window('DeletedKeysOK',title='DeleteKeys_V1.0',width=300,height=100)
	
	#creating interface element:
	layoutUI = cmds.columnLayout('mainColumnLayout', width=300, adjustableColumn=True)
	t1 = cmds.text('\nKeys successfully deleted.\n', parent=layoutUI)
	
	b1 = cmds.button('exit',label='exit', command='cmds.deleteUI("DeletedKeysOK", window=True)', parent=layoutUI)
	
	#Show window
	cmds.showWindow(window)
	
	
def noSeletedKeys():
	if not sel:
		#declare variable
		global window
		#Create UI
		window = cmds.window('DeleteKeys',title='DeleteKeys_V1.0',width=300,height=100)
		
		#creating interface element:
		layoutUI = cmds.columnLayout('mainColumnLayout', width=300, adjustableColumn=True)
		t1 = cmds.text('\nPlease select any object\n', parent=layoutUI)
		
		b1 = cmds.button('exit',label='exit', command='cmds.deleteUI("DeleteKeys", window=True)', parent=layoutUI)
		
		#Show window
		cmds.showWindow(window)
		 		 
	else:
		delKeys()
		
    
