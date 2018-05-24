# Place locator to the eyeball center
def placeEyeCenter(self):
	
	name = "left_eye"
	selection = cmds.filterExpand(selectionMask = 12)
	#self.eyeName = cmds.textField(self.txtfEye, query = 1, text = 1)
	
	if selection == None:
		self.eyeLoc = None
		#self.eyeName = None
		cmds.warning("Please select the eyeball.\n")
	else :
		eyeball = selection[0]
		#if not self.eyeName:
			#self.eyeName = name = "DefaultEye"
		#else :
			#name = self.eyeName
		
		self.eyeLoc = cmds.spaceLocator(n = "{0}_eyeCenter_locator".format(name))[0]
		cmds.matchTransform(self.eyeLoc, selection)
		self.eyeUpLoc = cmds.spaceLocator(n = "{0}_eyeUp_locator".format(name))[0]
		cmds.matchTransform(self.eyeUpLoc, selection)
		cmds.move(0, 10, 0, self.eyeUpLoc, relative = True)

		
		# lock locator
		cmds.setAttr("{0}.overrideEnabled".format(self.eyeLoc), 1)
		cmds.setAttr("{0}.overrideDisplayType".format(self.eyeLoc), 2)
		
		cmds.select(clear = 1)

		# Update UI
		#cmds.textField(self.txtfLoc, editable = 1, text = self.eyeLoc)
		#cmds.button(self.btnPlaceCenter, editable = 1, enable = 0)
		
placeEyeCenter(placeEyeCenter)
