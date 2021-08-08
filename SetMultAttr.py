#    SetMultAtrr  V.1   
#                                             
# permite mudar atributos de varios objetos que estivem sobe sua seleção
#  
#  autor:  Jose Paulo Gomes Filho
#  contato: jacareds@gmail.com

import maya.cmds as cmds

#Cria a UI para checar seletion

def selectCheck():
	#Get selection
	
	global selected
	selected = cmds.ls(selection=True)
	if selected:
		start()
	#Create UI Alert
	else:
		WinAlert = cmds.window('winAl',title='windowsAlert',width=200)
		LayoutUI = cmds.columnLayout('LayoutAlert', width=400, adjustableColumn=True)
		cmds.text('Before, select the objects you want to change the attribute')
		cmds.button( label='Ok',command='SetMultAttr.start()', parent=LayoutUI )
		cmds.button( label='Exit',command='SetMultAttr.exit()', parent=LayoutUI )
		cmds.showWindow('winAl')
	
def start():
	if cmds.window('winAlAtt', exists=True):
		cmds.deleteUI('winAlAtt', window=True)
	if cmds.window('winAl', exists=True):
		cmds.deleteUI('winAl', window=True)
	if not selected:
		selectCheck()
	else:
		if cmds.window('win', exists=True):
			cmds.deleteUI('win', window=True)
		varWin = cmds.window('win',title='SetMultAttr',width=150 )
		cmds.columnLayout(adjustableColumn=True)
		cmds.text('Enter with attribute name' )
		getFieldAtt = cmds.textField('textFil',h=25, w=180)
		cmds.text('Enter with value' )
		getFieldValue = cmds.floatField('floatValue',h=25, w=180,precision=3)
		cmds.button( label='Ok',command='SetMultAttr.baseScript()' )
		cmds.button( label='Exit', command='SetMultAttr.exit()' )
		cmds.showWindow('win')

def baseScript():
	getFieldAtt = cmds.textField('textFil',h=25, w=180, query=True)
	getFieldValue = cmds.floatField('floatValue', query=True,value=True)
	if not getFieldAtt:
		winAlert()
	if not getFieldValue:
		winAlert()
	else:
		print getFieldAtt
		print getFieldValue
		print selected
		
		#Cria o for
		for nameObj in selected:
			cmds.setAttr(nameObj+'.'+getFieldAtt, getFieldValue)
	
						
def winAlert():	
	WinAlertAtt = cmds.window('winAlAtt',title='windowsAlertAtt',width=200)
	LayoutUIAtt = cmds.columnLayout('LayoutAlertAtt', width=400, adjustableColumn=True)
	cmds.text("No data found.")
	cmds.button( label='Ok',command='SetMultAttr.start()', parent=LayoutUIAtt )
	cmds.showWindow('winAlAtt')
		
def exit():
	if cmds.window('win', exists=True):
		cmds.deleteUI('win', window=True)
	if cmds.window('winAl', exists=True):
		cmds.deleteUI('winAl', window=True)
	print 'Saida pela direita'