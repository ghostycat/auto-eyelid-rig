import maya.cmds as cmds

def UI(self):

    winWidth = 400
    
    mainWin = "auto_eyelid_rig"
    
    if cmds.window("auto_eyelid_rig", exists = 1):
        cmds.deleteUI("auto_eyelid_rig", window = 1)
    
    cmds.window("auto_eyelid_rig", title = "Auto Eyelid Rig")
    
    # Main layout
    cmds.columnLayout(co = ("both", 5))
    
    # Define eye name
    cmds.frameLayout(label = "Step 1. Name the eye", width = winWidth)
    cmds.setParent("..")
    cmds.text(height = 5, label = "")
    cmds.setParent("..")
    cmds.rowLayout(numberOfColumns = 2)
    cmds.text(align = "left", width = winWidth * 0.4, label = "Eye name (Example: right_Eye)")
    self.txtfEye = cmds.textField(width = winWidth * 0.6)
    cmds.setParent("..")

    cmds.separator(height = 15, width = winWidth)
    
    # Define eyeball center
    cmds.frameLayout(label = "Step 2. Place eye center", width = winWidth)
    cmds.setParent("..")
    cmds.text(height = 30, label = "Select eyeball, then click 'Place center'.")
    cmds.setParent("..")
    cmds.rowColumnLayout(numberOfRows = 1)
    self.btnPlaceCenter = cmds.button(width = winWidth * 0.4, label = "Place center", command = lambda _: placeEyeCenter(self))
    cmds.text(height = 30, label = "")
    self.txtfLoc = cmds.textField(width = winWidth * 0.6, editable = 0)
    cmds.setParent("..")
    
    cmds.separator(height = 15, width = winWidth)
    
    # List upper lid vertices
    cmds.frameLayout(label = "Step 3. Choose upper eyelid", width = winWidth)
    cmds.setParent("..")
    cmds.text(height = 30, label = "Select vertices of upper eyelid, then click 'Set'.")
    cmds.setParent("..")
    cmds.rowColumnLayout(numberOfRows = 1)
    self.btnUpLid = cmds.button(width = winWidth * 0.4, label = "Set")
    self.scrollfUpLid = cmds.scrollField(width = winWidth * 0.6, h = 50, wordWrap = 1, editable = 0, enable = 0)
    cmds.setParent("..")
    
    cmds.separator(height = 15, width = winWidth)
    
    # List lower lid vertices
    cmds.frameLayout(label = "Step 4. Choose lower eyelid", width = winWidth)
    cmds.setParent("..")
    cmds.text(height = 30, label = "Select vertices of lower eyelid, then click 'Set'.")
    cmds.setParent("..")
    cmds.rowColumnLayout(numberOfRows = 1)
    self.btnLowLid = cmds.button(width = winWidth * 0.4, label = "Set")
    self.scrollfLowLid = cmds.scrollField(width = winWidth * 0.6, height = 50, wordWrap = 1, editable = 0, enable = 0)
    cmds.setParent("..")
    
    cmds.separator(height = 15, width = winWidth)
    
    # Allow/disallow smart blink
    cmds.frameLayout(label = "Step 5. Smart blink", width = winWidth)
    cmds.setParent("..")
    self.isSmartBlink = cmds.checkBox(height = 30, label = "Add smart blink", value = 1)

    cmds.separator(height = 15, width = winWidth)
    
    # Build final rig
    self.btnBuild = cmds.button(width = winWidth, height = 70, label = "BUILD RIG", backgroundColor = (0.2,0.6,0.65))
    cmds.text(height = 5, label = "")
    
    cmds.showWindow("auto_eyelid_rig")


# Place locator to the eyeball center
def placeEyeCenter(self):
	selection = cmds.filterExpand(selectionMask = 12)
	self.eyeName = cmds.textField(self.txtfEye, query = 1, text = 1)
	
	if selection == None:
		self.eyeLoc = None
		self.eyeName = None
		cmds.warning("Please select the eyeball.")
	else :
		eyeball = selection[0]
		if not self.eyeName:
			self.eyeName = name = "DefaultEye"
		else :
			name = self.eyeName
		
		self.eyeLoc = cmds.spaceLocator(n = "{0}_eyeCenter_locator".format(name))[0]
		cmds.matchTransform(self.eyeLoc, selection)
		
		# Place locator above for aimUp
		self.eyeUpLoc = cmds.spaceLocator(n = "{0}_eyeUp_locator".format(name))[0]
		cmds.matchTransform(self.eyeUpLoc, selection)
		cmds.move(0, 10, 0, self.eyeUpLoc, relative = True)

		cmds.select(clear = 1)

		# Update UI
		cmds.button(self.btnPlaceCenter, e = True, enable = False)
		cmds.textField(self.txtfLoc, e = True, text=self.eyeLoc)

# List upLid vertices
def upLidVtxSet (self):
	
	self.upperLidVtx = cmds.filterExpand(sm = 31)
	
	if self.upperLidVtx == None :
		cmds.scrollField(self.scrollfUpLid, e = 1, clear = 1)
		cmds.warning("Please select vertices of the upper lid.")
	else :
		cmds.scrollField(self.scrollfUpLid, e = 1, clear = 1)
		for vtx in self.upperLidVtx :
			vtxNum = vtx.rpartition(".")[2] # <type 'unicode'>
			cmds.scrollField(self.scrollfUpLid, e = 1, it =(str (vtxNum) + " "))

# List lowLid vertices
def upLidVtxSet (self):
	
	self.lowerLidVtx = cmds.filterExpand(sm = 31)
	
	if self.lowerLidVtx == None :
		cmds.scrollField(self.scrollfLowLid, e = 1, clear = 1)
		cmds.warning("Please select vertices of the upper lid.")
	else :
		cmds.scrollField(self.scrollfLowLid, e = 1, clear = 1)
		for vtx in self.lowerLidVtx :
			vtxNum = vtx.rpartition(".")[2] # <type 'unicode'>
			cmds.scrollField(self.scrollfLowLid, e = 1, it =(str (vtxNum) + " "))

UI(UI)