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
				row = self.layout.row()
				if data.taper_object:
					row.prop(data.taper_object.data, 'resolution_u')
				else:
					row.label("")
				if data.bevel_object:
					row.prop(data.bevel_object.data, 'resolution_u')
				else:
					row.label("")
	if (context.user_preferences.addons["Scramble Addon"].preferences.use_disabled_menu):
		self.layout.operator('wm.toggle_menu_enable', icon='CANCEL').id = __name__.split('.')[-1]
