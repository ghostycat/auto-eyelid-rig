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