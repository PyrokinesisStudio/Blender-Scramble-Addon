# 「プロパティ」エリア > 「カーブデータ」タブ > 「ジオメトリ」パネル

import bpy

################
# オペレーター #
################

class CopyTaperObject(bpy.types.Operator):
	bl_idname = "curve.copy_taper_object"
	bl_label = "Copy taper object"
	bl_description = "Tapered object that is specified in active curve object copies to other selection curves"
	bl_options = {'REGISTER', 'UNDO'}
	
	@classmethod
	def poll(cls, context):
		if not context.object:
			return False
		if context.object.type != 'CURVE':
			return False
		for obj in context.selected_objects:
			if obj.name != context.object.name:
				if obj.type == 'CURVE':
					src = context.object.data.taper_object.name if context.object.data.taper_object else ""
					trg = obj.data.taper_object.name if obj.data.taper_object else ""
					if src != trg:
						return True
		return False
	
	def execute(self, context):
		active_obj = context.object
		for obj in context.selected_objects:
			if (obj.name != active_obj.name):
				if (obj.type == 'CURVE'):
					obj.data.taper_object = active_obj.data.taper_object
		return {'FINISHED'}

class CopyBevelObject(bpy.types.Operator):
	bl_idname = "curve.copy_bevel_object"
	bl_label = "Copy bevel object"
	bl_description = "Bevel object that is specified in active curve object copies to other selection curves"
	bl_options = {'REGISTER', 'UNDO'}
	
	@classmethod
	def poll(cls, context):
		if not context.object:
			return False
		if context.object.type != 'CURVE':
			return False
		for obj in context.selected_objects:
			if obj.name != context.object.name:
				if obj.type == 'CURVE':
					src = context.object.data.bevel_object.name if context.object.data.bevel_object else ""
					trg = obj.data.bevel_object.name if obj.data.bevel_object else ""
					if src != trg:
						return True
		return False
	
	def execute(self, context):
		active_obj = context.object
		for obj in context.selected_objects:
			if (obj.name != active_obj.name):
				if (obj.type == 'CURVE'):
					obj.data.bevel_object = active_obj.data.bevel_object
		return {'FINISHED'}

class ActivateTaperObject(bpy.types.Operator):
	bl_idname = "curve.activate_taper_object"
	bl_label = "Tapered object, activate"
	bl_description = "curve is specified as tapered object"
	bl_options = {'REGISTER', 'UNDO'}
	
	@classmethod
	def poll(cls, context):
		ob = context.active_object
		if ob.type == 'CURVE':
			if ob.data.taper_object:
				return True
		return False
	
	def execute(self, context):
		ob = context.active_object.data.taper_object
		ob.select = True
		ob.hide = False
		context.scene.objects.active = ob
		for i, b in enumerate(ob.layers):
			if b:
				context.scene.layers[i] = True
		return {'FINISHED'}

class ActivateBevelObject(bpy.types.Operator):
	bl_idname = "curve.activate_bevel_object"
	bl_label = "Activate bevel object"
	bl_description = "curve is specified as beveled objects"
	bl_options = {'REGISTER', 'UNDO'}
	
	@classmethod
	def poll(cls, context):
		ob = context.active_object
		if ob.type == 'CURVE':
			if ob.data.bevel_object:
				return True
		return False
	
	def execute(self, context):
		ob = context.active_object.data.bevel_object
		ob.select = True
		ob.hide = False
		context.scene.objects.active = ob
		for i, b in enumerate(ob.layers):
			if b:
				context.scene.layers[i] = True
		return {'FINISHED'}

################
# メニュー追加 #
################

# メニューのオン/オフの判定
def IsMenuEnable(self_id):
	for id in bpy.context.user_preferences.addons["Scramble Addon"].preferences.disabled_menu.split(','):
		if (id == self_id):
			return False
	else:
		return True

# メニューを登録する関数
def menu(self, context):
	if (IsMenuEnable(__name__.split('.')[-1])):
		if 2 <= len(context.selected_objects):
			i = 0
			for obj in context.selected_objects:
				if obj.type == 'CURVE':
					i += 1
			if 2 <= i:
				row = self.layout.row()
				row.operator(CopyTaperObject.bl_idname, icon='COPY_ID')
				row.operator(CopyBevelObject.bl_idname, icon='COPY_ID')
		if context.active_object:
			data = context.active_object.data
			if data.bevel_object or data.taper_object:
				row = self.layout.split(percentage=0.5)
				if data.taper_object:
					sub = row.row()
					sub.operator(ActivateTaperObject.bl_idname, icon='PARTICLE_PATH', text="")
					sub.prop(data.taper_object.data, 'resolution_u')
				else:
					row.label("")
				if data.bevel_object:
					sub = row.row()
					sub.operator(ActivateBevelObject.bl_idname, icon='OUTLINER_OB_SURFACE', text="")
					sub.prop(data.bevel_object.data, 'resolution_u')
				else:
					row.label("")
	if (context.user_preferences.addons["Scramble Addon"].preferences.use_disabled_menu):
		self.layout.operator('wm.toggle_menu_enable', icon='CANCEL').id = __name__.split('.')[-1]
