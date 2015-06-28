# UV/画像エディター > 「画像」メニュー

import bpy
import os, numpy

################
# オペレーター #
################

class RenameImageFileName(bpy.types.Operator):
	bl_idname = "image.rename_image_file_name"
	bl_label = "Using the name of the image file name"
	bl_description = "External images are using the name of the active image file name"
	bl_options = {'REGISTER', 'UNDO'}
	
	isExt = bpy.props.BoolProperty(name="Including the extension", default=True)
	
	@classmethod
	def poll(cls, context):
		if (not context.edit_image):
			return False
		if (context.edit_image.filepath == ""):
			return False
		return True
	def invoke(self, context, event):
		wm = context.window_manager
		return wm.invoke_props_dialog(self)
	def execute(self, context):
		img = context.edit_image
		name = bpy.path.basename(img.filepath_raw)
		if (not self.isExt):
			name, ext = os.path.splitext(name)
		try:
			img.name = name
		except: pass
		return {'FINISHED'}

class AllRenameImageFileName(bpy.types.Operator):
	bl_idname = "image.all_rename_image_file_name"
	bl_label = "In the file name to use for all image names"
	bl_description = "The names of all images using external image file name"
	bl_options = {'REGISTER', 'UNDO'}
	
	isExt = bpy.props.BoolProperty(name="Including the extension", default=True)
	
	@classmethod
	def poll(cls, context):
		if (len(bpy.data.images) <= 0):
			return False
		for img in bpy.data.images:
			if (img.filepath != ""):
				return True
		return False
	def execute(self, context):
		for img in  bpy.data.images:
			name = bpy.path.basename(img.filepath_raw)
			if (not self.isExt):
				name, ext = os.path.splitext(name)
			try:
				img.name = name
			except: pass
		return {'FINISHED'}

class ReloadAllImage(bpy.types.Operator):
	bl_idname = "image.reload_all_image"
	bl_label = "Load all images"
	bl_description = "Reloads all the image data referring to external file"
	bl_options = {'REGISTER', 'UNDO'}
	
	@classmethod
	def poll(cls, context):
		if (len(bpy.data.images) <= 0):
			return False
		for img in bpy.data.images:
			if (img.filepath != ""):
				return True
		return False
	def execute(self, context):
		for img in bpy.data.images:
			if (img.filepath != ""):
				img.reload()
				try:
					img.update()
				except RuntimeError:
					pass
		for area in context.screen.areas:
			area.tag_redraw()
		return {'FINISHED'}

class FillOverrideColor(bpy.types.Operator):
	bl_idname = "image.fill_override_color"
	bl_label = "Over the specified color"
	bl_description = "All over the colors you specify the active image"
	bl_options = {'REGISTER', 'UNDO'}
	
	color = bpy.props.FloatVectorProperty(name="色", description="Color fill", default=(1, 1, 1), min=0, max=1, soft_min=0, soft_max=1, step=10, precision=3, subtype='COLOR_GAMMA')
	alpha = bpy.props.FloatProperty(name="Transparency", description="Transparency", default=1, min=0, max=1, soft_min=0, soft_max=1, step=10, precision=3, subtype='PERCENTAGE')
	
	@classmethod
	def poll(cls, context):
		if (not context.edit_image):
			return False
		if (len(context.edit_image.pixels) <= 0):
			return False
		return True
	def invoke(self, context, event):
		wm = context.window_manager
		return wm.invoke_props_dialog(self)
	def execute(self, context):
		img = context.edit_image
		pixel = list(self.color[:])
		if (4 <= img.channels):
			pixel.append(self.alpha)
		img.pixels = pixel * (img.size[0] * img.size[1])
		img.gl_free()
		for area in context.screen.areas:
			area.tag_redraw()
		return {'FINISHED'}

class FillColor(bpy.types.Operator):
	bl_idname = "image.fill_color"
	bl_label = "Fill with color"
	bl_description = "All fill in the color you specify the active image"
	bl_options = {'REGISTER', 'UNDO'}
	
	color = bpy.props.FloatVectorProperty(name="色", description="Color fill", default=(1, 1, 1), min=0, max=1, soft_min=0, soft_max=1, step=10, precision=3, subtype='COLOR_GAMMA')
	alpha = bpy.props.FloatProperty(name="Transparency", description="Transparency", default=1, min=0, max=1, soft_min=0, soft_max=1, step=10, precision=3, subtype='PERCENTAGE')
	
	@classmethod
	def poll(cls, context):
		if (not context.edit_image):
			return False
		if (len(context.edit_image.pixels) <= 0):
			return False
		return True
	def invoke(self, context, event):
		return context.window_manager.invoke_props_dialog(self)
	def execute(self, context):
		img = context.edit_image
		color = self.color[:]
		alpha = self.alpha
		unalpha = 1.0 - alpha
		img_width, img_height, img_channel = img.size[0], img.size[1], img.channels
		pixels = numpy.array(img.pixels).reshape(img_height * img_width, img_channel)
		pixels[:,0] = (pixels[:,0] * unalpha) + (color[0] * alpha)
		pixels[:,1] = (pixels[:,1] * unalpha) + (color[1] * alpha)
		pixels[:,2] = (pixels[:,2] * unalpha) + (color[2] * alpha)
		img.pixels = pixels.flatten()
		img.gl_free()
		for area in context.screen.areas:
			area.tag_redraw()
		return {'FINISHED'}

class FillTransparency(bpy.types.Operator):
	bl_idname = "image.fill_transparency"
	bl_label = "Fill with transparency"
	bl_description = "The transparent parts of the image are active in the specified color fills"
	bl_options = {'REGISTER', 'UNDO'}
	
	color = bpy.props.FloatVectorProperty(name="Color fill", default=(1, 1, 1), min=0, max=1, soft_min=0, soft_max=1, step=10, precision=3, subtype='COLOR_GAMMA')
	
	@classmethod
	def poll(cls, context):
		if (not context.edit_image):
			return False
		if (len(context.edit_image.pixels) <= 0):
			return False
		if (context.edit_image.channels < 4):
			return False
		return True
	def invoke(self, context, event):
		return context.window_manager.invoke_props_dialog(self)
	def execute(self, context):
		img = context.edit_image
		color = self.color[:]
		img_width, img_height, img_channel = img.size[0], img.size[1], img.channels
		pixels = numpy.array(img.pixels).reshape(img_height, img_width, img_channel)
		if (4 <= img_channel):
			alphas = pixels[:,:,3]
			unalphas = 1.0 - alphas
		else:
			alphas = numpy.ones(img_height * img_width)
			unalphas = numpy.zeros(img_height * img_width)
		pixels[:,:,0]= (pixels[:,:,0] * alphas) + (color[0] * unalphas)
		pixels[:,:,1]= (pixels[:,:,1] * alphas) + (color[1] * unalphas)
		pixels[:,:,2]= (pixels[:,:,2] * alphas) + (color[2] * unalphas)
		pixels[:,:,3] = 1.0
		img.pixels = pixels.flatten()
		img.gl_free()
		for area in context.screen.areas:
			area.tag_redraw()
		return {'FINISHED'}

class Normalize(bpy.types.Operator):
	bl_idname = "image.normalize"
	bl_label = "Image normalization"
	bl_description = "Normalizes the active image"
	bl_options = {'REGISTER', 'UNDO'}
	
	@classmethod
	def poll(cls, context):
		if (not context.edit_image):
			return False
		if (len(context.edit_image.pixels) <= 0):
			return False
		return True
	def execute(self, context):
		img = context.edit_image
		img_width, img_height, img_channel = img.size[0], img.size[1], img.channels
		pixels = numpy.array(img.pixels).reshape(img_height, img_width, img_channel)
		rs = pixels[:,:,0]
		gs = pixels[:,:,1]
		bs = pixels[:,:,2]
		values = (rs + gs + bs) / 3
		min = numpy.amin(values)
		max = numpy.amax(values)
		multi = 1 / (max - min)
		for c in range(3):
			pixels[:,:,c] = (pixels[:,:,c] - min) * multi
		img.pixels = pixels.flatten()
		img.gl_free()
		for area in context.screen.areas:
			area.tag_redraw()
		return {'FINISHED'}

class RenameImageFile(bpy.types.Operator):
	bl_idname = "image.rename_image_file"
	bl_label = "Change the name of the image file"
	bl_description = "Change the file name of the active image"
	bl_options = {'REGISTER'}
	
	new_name = bpy.props.StringProperty(name="New file name")
	
	@classmethod
	def poll(cls, context):
		if (not context.edit_image):
			return False
		if (context.edit_image.filepath == ""):
			return False
		return True
	def invoke(self, context, event):
		self.new_name = bpy.path.basename(context.edit_image.filepath_raw)
		if (self.new_name == ""):
			self.report(type={"ERROR"}, message="External file does not exist on this image")
			return {"CANCELLED"}
		return context.window_manager.invoke_props_dialog(self)
	def execute(self, context):
		pre_filepath = context.edit_image.filepath_raw
		dir = os.path.dirname(bpy.path.abspath(context.edit_image.filepath_raw))
		name = bpy.path.basename(context.edit_image.filepath_raw)
		if (self.new_name == name):
			self.report(type={"ERROR"}, message="The image file name is the same as the original")
			return {"CANCELLED"}
		bpy.ops.image.save_as(filepath=os.path.join(dir, self.new_name))
		context.edit_image.name = self.new_name
		os.remove(bpy.path.abspath(pre_filepath))
		return {'FINISHED'}

# ながとさんに協力して頂きました、感謝！
class BlurImage(bpy.types.Operator):
	bl_idname = "image.blur_image"
	bl_label = "(Note the heavy) blurs an image"
	bl_description = "Blurs an image of active"
	bl_options = {'REGISTER', 'UNDO'}
	
	strength = bpy.props.IntProperty(name="Blur amount", default=10, min=1, max=100, soft_min=1, soft_max=100)
	
	@classmethod
	def poll(cls, context):
		if (not context.edit_image):
			return False
		if (len(context.edit_image.pixels) <= 0):
			return False
		return True
	def invoke(self, context, event):
		return context.window_manager.invoke_props_dialog(self)
	def execute(self, context):
		img = context.edit_image
		if (not img):
			self.report(type={'ERROR'}, message="Active image not found")
			return {'CANCELLED'}
		w, h, c = img.size[0], img.size[1], img.channels
		ps = numpy.array(img.pixels)
		lengthes = []
		for i in range(999):
			length = 2 ** i
			lengthes.append(length)
			if (self.strength < sum(lengthes)):
				lengthes[-1] -= sum(lengthes) - self.strength
				if (2 <= len(lengthes)):
					if (lengthes[-1] == 0):
						lengthes = lengthes[:-1]
					elif (lengthes[-1] <= lengthes[-2] / 2):
						lengthes[-2] += lengthes[-1]
						lengthes = lengthes[:-1]
				break
		divisor = 16 ** len(lengthes)
		for length in lengthes:
			for (dx, dy, endX, endY) in [(w*c, c, h, w), (c, w*c, w, h)]:
				for (start, end, sign) in [(0, endX, 1), (endX-1, -1, -1)]:
					dir  = sign * dx
					diff = dir * length
					for y in range(0, dy*endY, dy):
						for x in range(start*dx, end*dx - diff, dir):
							for i in range(y + x, y + x + c):
								ps[i] = ps[i] + ps[i + diff]
						for x in range(end*dx - diff, end*dx, dir):
							for i in range(y + x, y + x + c):
								ps[i] = ps[i] * 2
		for y in range(0, h*w*c, w*c):
			for x in range(0, w*c, c):
				for i in range(y + x, y + x + c):
					ps[i] = ps[i] / divisor
		img.pixels = ps.tolist()
		img.gl_free()
		for area in context.screen.areas:
			area.tag_redraw()
		return {'FINISHED'}

class ReverseWidthImage(bpy.types.Operator):
	bl_idname = "image.reverse_width_image"
	bl_label = "Flip horizontally"
	bl_description = "Active image flips horizontally"
	bl_options = {'REGISTER', 'UNDO'}
	
	@classmethod
	def poll(cls, context):
		if (not context.edit_image):
			return False
		if (len(context.edit_image.pixels) <= 0):
			return False
		return True
	def execute(self, context):
		img = context.edit_image
		if (not img):
			self.report(type={'ERROR'}, message="Active image not found")
			return {'CANCELLED'}
		img_width, img_height, img_channel = img.size[0], img.size[1], img.channels
		pixels = numpy.array(img.pixels).reshape(img_height, img_width, img_channel)
		#for i in range(img_height):
		#	pixels[i] = pixels[i][::-1]
		pixels[:,:] = pixels[:,::-1]
		img.pixels = pixels.flatten()
		img.gl_free()
		for area in context.screen.areas:
			area.tag_redraw()
		return {'FINISHED'}

class ReverseHeightImage(bpy.types.Operator):
	bl_idname = "image.reverse_height_image"
	bl_label = "Flip vertically"
	bl_description = "Active image flips vertical"
	bl_options = {'REGISTER', 'UNDO'}
	
	@classmethod
	def poll(cls, context):
		if (not context.edit_image):
			return False
		if (len(context.edit_image.pixels) <= 0):
			return False
		return True
	def execute(self, context):
		img = context.edit_image
		if (not img):
			self.report(type={'ERROR'}, message="Active image not found")
			return {'CANCELLED'}
		img_width, img_height, img_channel = img.size[0], img.size[1], img.channels
		pixels = numpy.array(img.pixels).reshape(img_height, img_width, img_channel)
		pixels = pixels[::-1]
		img.pixels = pixels.flatten()
		img.gl_free()
		for area in context.screen.areas:
			area.tag_redraw()
		return {'FINISHED'}

class Rotate90Image(bpy.types.Operator):
	bl_idname = "image.rotate_90_image"
	bl_label = "Rotate 90 degrees"
	bl_description = "Active image rotates 90 °"
	bl_options = {'REGISTER', 'UNDO'}
	
	@classmethod
	def poll(cls, context):
		if (not context.edit_image):
			return False
		if (len(context.edit_image.pixels) <= 0):
			return False
		return True
	def execute(self, context):
		img = context.edit_image
		img_width, img_height, img_channel = img.size[0], img.size[1], img.channels
		pixels = numpy.array(img.pixels).reshape(img_height, img_width, img_channel)
		new_pixels = numpy.zeros((img_width, img_height, img_channel))
		for y in range(img_height):
			new_pixels[:,y,:] = pixels[y,::-1,:]
		img.scale(img_height, img_width)
		img.pixels = new_pixels.flatten()
		img.gl_free()
		for area in context.screen.areas:
			area.tag_redraw()
		return {'FINISHED'}

class Rotate180Image(bpy.types.Operator):
	bl_idname = "image.rotate_180_image"
	bl_label = "Rotate 180 degrees"
	bl_description = "Active image rotates 180 °"
	bl_options = {'REGISTER', 'UNDO'}
	
	@classmethod
	def poll(cls, context):
		if (not context.edit_image):
			return False
		if (len(context.edit_image.pixels) <= 0):
			return False
		return True
	def execute(self, context):
		img = context.edit_image
		if (not img):
			self.report(type={'ERROR'}, message="Active image not found")
			return {'CANCELLED'}
		img_width, img_height, img_channel = img.size[0], img.size[1], img.channels
		pixels = numpy.array(img.pixels).reshape(img_height, img_width, img_channel)
		pixels[:,:] = pixels[:,::-1]
		pixels = pixels[::-1]
		img.pixels = pixels.flatten()
		img.gl_free()
		for area in context.screen.areas:
			area.tag_redraw()
		return {'FINISHED'}

class Rotate270Image(bpy.types.Operator):
	bl_idname = "image.rotate_270_image"
	bl_label = "Rotate 270 degrees"
	bl_description = "Active image rotates 270 degrees"
	bl_options = {'REGISTER', 'UNDO'}
	
	@classmethod
	def poll(cls, context):
		if (not context.edit_image):
			return False
		if (len(context.edit_image.pixels) <= 0):
			return False
		return True
	def execute(self, context):
		img = context.edit_image
		img_width, img_height, img_channel = img.size[0], img.size[1], img.channels
		pixels = numpy.array(img.pixels).reshape(img_height, img_width, img_channel)
		new_pixels = numpy.zeros((img_width, img_height, img_channel))
		for y in range(img_height):
			new_pixels[:,y,:] = pixels[-y-1,:,:]
		img.scale(img_height, img_width)
		img.pixels = new_pixels.flatten()
		img.gl_free()
		for area in context.screen.areas:
			area.tag_redraw()
		return {'FINISHED'}

class ExternalEditEX(bpy.types.Operator):
	bl_idname = "image.external_edit_ex"
	bl_label = "Editing in an external editor (enhanced)"
	bl_description = "Open the image in an external editor of the additional files page of the custom"
	bl_options = {'REGISTER', 'UNDO'}
	
	index = bpy.props.IntProperty(name="Number to use", default=1, min=1, max=3, soft_min=1, soft_max=3)
	
	@classmethod
	def poll(cls, context):
		if (not context.edit_image):
			return False
		if (context.edit_image.filepath == ""):
			return False
		return True
	def execute(self, context):
		img = context.edit_image
		if (not img):
			self.report(type={'ERROR'}, message="Image not found")
			return {'CANCELLED'}
		if (img.filepath == ""):
			self.report(type={'ERROR'}, message="Cannot find the image path")
			return {'CANCELLED'}
		path = bpy.path.abspath(img.filepath)
		pre_path = context.user_preferences.filepaths.image_editor
		if (self.index == 1):
			context.user_preferences.filepaths.image_editor = context.user_preferences.addons['Scramble Addon'].preferences.image_editor_path_1
		elif (self.index == 2):
			context.user_preferences.filepaths.image_editor = context.user_preferences.addons['Scramble Addon'].preferences.image_editor_path_2
		elif (self.index == 3):
			context.user_preferences.filepaths.image_editor = context.user_preferences.addons['Scramble Addon'].preferences.image_editor_path_3
		bpy.ops.image.external_edit(filepath=path)
		context.user_preferences.filepaths.image_editor = pre_path
		return {'FINISHED'}

class Resize(bpy.types.Operator):
	bl_idname = "image.resize"
	bl_label = "Image zoom in / out"
	bl_description = "Active image resizing"
	bl_options = {'REGISTER', 'UNDO'}
	
	def width_update(self, context):
		if (self.keep_ratio):
			img = bpy.context.edit_image
			w, h = img.size[0], img.size[1]
			ratio = w / h
			self.height = round(self.width / ratio)
		return None
	def height_update(self, context):
		if (self.keep_ratio):
			img = bpy.context.edit_image
			w, h = img.size[0], img.size[1]
			ratio = w / h
			self.width = round(self.height * ratio)
		return None
	
	width = bpy.props.IntProperty(name="Width", default=0, min=1, max=8192, soft_min=1, soft_max=8192, step=1, subtype='PIXEL', update=width_update)
	height = bpy.props.IntProperty(name="Vertical size", default=0, min=1, max=8192, soft_min=1, soft_max=8192, step=1, subtype='PIXEL', update=height_update)
	keep_ratio = bpy.props.BoolProperty(name="Keep ratio", default=True)
	
	@classmethod
	def poll(cls, context):
		if (not context.edit_image):
			return False
		if (len(context.edit_image.pixels) <= 0):
			return False
		return True
	def invoke(self, context, event):
		img = context.edit_image
		self.width, self.height = img.size[0], img.size[1]
		return context.window_manager.invoke_props_dialog(self)
	def execute(self, context):
		img = context.edit_image
		img.scale(self.width, self.height)
		img.gl_free()
		for area in context.screen.areas:
			area.tag_redraw()
		return {'FINISHED'}

class Duplicate(bpy.types.Operator):
	bl_idname = "image.duplicate"
	bl_label = "Reproduction of images"
	bl_description = "Duplicate the active picture"
	bl_options = {'REGISTER', 'UNDO'}
	
	@classmethod
	def poll(cls, context):
		if (not context.edit_image):
			return False
		if (len(context.edit_image.pixels) <= 0):
			return False
		return True
	def execute(self, context):
		src = context.edit_image
		new = bpy.data.images.new(
			name = 'temptemp',
			width = src.size[0],
			height = src.size[1],
			alpha = src.use_alpha,
			float_buffer = src.is_float,
			stereo3d = src.is_stereo_3d)
		for name in dir(src):
			if (name == 'pixels'):
				new.pixels = src.pixels[:]
				continue
			elif (name == 'name'):
				new.name = src.name + "_copy"
				continue
			value = src.__getattribute__(name)
			try:
				new.__setattr__(name, value)[:]
			except AttributeError:
				pass
			except TypeError:
				new.__setattr__(name, value)
		context.space_data.image = new
		for area in context.screen.areas:
			area.tag_redraw()
		return {'FINISHED'}

################
# サブメニュー #
################

class TransformMenu(bpy.types.Menu):
	bl_idname = "IMAGE_MT_image_transform"
	bl_label = "Deformation"
	bl_description = "Image deformation processing menu."
	
	def draw(self, context):
		self.layout.operator(Resize.bl_idname, icon='PLUGIN')
		self.layout.separator()
		self.layout.operator(ReverseWidthImage.bl_idname, icon='PLUGIN')
		self.layout.operator(ReverseHeightImage.bl_idname, icon='PLUGIN')
		self.layout.separator()
		self.layout.operator(Rotate90Image.bl_idname, icon='PLUGIN')
		self.layout.operator(Rotate180Image.bl_idname, icon='PLUGIN')
		self.layout.operator(Rotate270Image.bl_idname, icon='PLUGIN')

################
# メニュー追加 #
################

# メニューのオン/オフの判定
def IsMenuEnable(self_id):
	for id in bpy.context.user_preferences.addons['Scramble Addon'].preferences.disabled_menu.split(','):
		if (id == self_id):
			return False
	else:
		return True

# メニューを登録する関数
def menu(self, context):
	if (IsMenuEnable(__name__.split('.')[-1])):
		if (context.user_preferences.addons['Scramble Addon'].preferences.image_editor_path_1):
			self.layout.separator()
			path = os.path.basename(context.user_preferences.addons['Scramble Addon'].preferences.image_editor_path_1)
			name, ext = os.path.splitext(path)
			self.layout.operator(ExternalEditEX.bl_idname, icon='PLUGIN', text=name+" In the open").index = 1
		if (context.user_preferences.addons['Scramble Addon'].preferences.image_editor_path_2):
			path = os.path.basename(context.user_preferences.addons['Scramble Addon'].preferences.image_editor_path_2)
			name, ext = os.path.splitext(path)
			self.layout.operator(ExternalEditEX.bl_idname, icon='PLUGIN', text=name+" In the open").index = 2
		if (context.user_preferences.addons['Scramble Addon'].preferences.image_editor_path_3):
			path = os.path.basename(context.user_preferences.addons['Scramble Addon'].preferences.image_editor_path_3)
			name, ext = os.path.splitext(path)
			self.layout.operator(ExternalEditEX.bl_idname, icon='PLUGIN', text=name+" In the open").index = 3
		self.layout.separator()
		self.layout.operator(FillOverrideColor.bl_idname, icon='PLUGIN')
		self.layout.operator(FillColor.bl_idname, icon='PLUGIN')
		self.layout.operator(FillTransparency.bl_idname, icon='PLUGIN')
		self.layout.separator()
		self.layout.operator(Normalize.bl_idname, icon='PLUGIN')
		self.layout.operator(BlurImage.bl_idname, icon='PLUGIN')
		self.layout.menu(TransformMenu.bl_idname, icon='PLUGIN')
		self.layout.separator()
		self.layout.operator(Duplicate.bl_idname, icon='PLUGIN')
		self.layout.operator(RenameImageFile.bl_idname, icon='PLUGIN')
		self.layout.separator()
		self.layout.operator(RenameImageFileName.bl_idname, icon='PLUGIN')
		self.layout.operator(AllRenameImageFileName.bl_idname, icon='PLUGIN')
		self.layout.separator()
		self.layout.operator(ReloadAllImage.bl_idname, icon='PLUGIN')
	if (context.user_preferences.addons['Scramble Addon'].preferences.use_disabled_menu):
		self.layout.separator()
		self.layout.operator('wm.toggle_menu_enable', icon='CANCEL').id = __name__.split('.')[-1]
