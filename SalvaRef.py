################################################################################################
#
#           SalvaRef version 3.0                                            
#  Save a file with specific name or not,
# and re-open the old file that was working.
#  
#
#  author:  Jose Paulo Gomes Filho
#  contact: jacareds@gmail.com
#
#  v 1.0 _ 2012-08-29 - first version created:creation Jose Paulo
#  v 2.0 _ 2013-01-15 - creation IU and Defs
#  v 3.0 _ 2013-05-22 - corretion inputs and paths
#
#
################################################################################################

import maya.cmds as cmds

def SalvaRefComn():	
	if True:
		try:
			#declare variable Global			
			global sav
			global sm
			global str
			global sn
			
			#Save current file		
			str = sav = cmds.file(force = True , save = True)
			#handles shorts and longs name	
			sm = str[:-3]
			savShort = cmds.file(sav, query=True, location=True, shortName=True)
			cont = len(savShort)
			sn = str[:-cont] 
			
		except:
			#creating UI Chec window 
			ChecWindow = cmds.window('ChecWindow', title='Chec UI',width=220, height=80)
			#creating element Chec window
			ChecWindowLay = cmds.columnLayout('mainColumnLayout', width=220,height=80, adjustableColumn=True)
			cmds.text('\n\n Save the scene before using the script.', parent=ChecWindowLay)
			#Show UI:
			cmds.showWindow(ChecWindow)	
		else:
			if cmds.window('ChecWindow', exists=True):
				cmds.deleteUI('ChecWindow', window=True)
			
			following()
			
def following():	
	#declare variable
	global window
	#Create UI
	window = cmds.window('SalvaRef',title='SalvaRef_V3.0',width=400,height=200)
	
	#creating interface element:
	layoutUI = cmds.columnLayout('mainColumnLayout', width=400, adjustableColumn=True)
	t1 = cmds.text('\nIf necessary, clean the history before continuing\n', parent=layoutUI)
	
	b1 = cmds.button('definput', label='rename file reference \n (in the next window enter the file name)', command ='SalvaRef.Refinput()', parent=layoutUI)
	b2 = cmds.button('defdirect', label='create the file reference with the current name.', command='SalvaRef.RefDirect()',parent=layoutUI)
	b3 = cmds.button('exit',label='exit', command='cmds.deleteUI("SalvaRef", window=True)', parent=layoutUI)
	
	#Show window
	cmds.showWindow(window)
	
def RefDirect():
	#save current file with extension REF
	cmds.file(rename =sm + '_REF.mb')
	cmds.file( force = True, save = True, options='v=1;p=17',type='mayaBinary')
	#open  initial file
	cmds.file( sav, force = True , open = True)
	#check and close all windows
	if cmds.window('SalvaRef', exists=True):
		cmds.deleteUI('SalvaRef', window=True)
	
def Refinput():
	#create and save a reference and open current file
	#check content variable nameRef
	if True:
		try:
			#open input window
			nameRef = raw_input()
			#rename file to input enter
			cmds.file(rename =sn + nameRef + '_REF.mb')
			#save file
			cam = cmds.file( force = True, save = True, options='v=1;p=17',type='mayaBinary')
			#abre o arquivo inicial
			cmds.file( sav, force = True , open = True)
			#check and close all windos
			if cmds.window('SalvaRef', exists=True):
				cmds.deleteUI('SalvaRef', window=True)
		except:
			#close exit windows
			if cmds.window('SalvaRef', exists=True):
				cmds.deleteUI('SalvaRef', window=True)