# 「プロパティ」エリア > 「カーブデータ」タブ > 「ジオメトリ」パネル

import bpy

################
# オペレーター #
################

class CopyTaperObject(bpy.types.Operator):
	bl_idname = "curve.copy_taper_object"
	bl_label = "テーパー指定コピー"
	bl_description = "アクティブカーブオブジェクトに指定されているテーパーオブジェクトを、他の選択カーブオブジェクトにコピーします"
	bl_options = {'REGISTER', 'UNDO'}
	
	@classmethod
	def poll(cls, context):
		if (not context.object):
			return False
		if (context.object.type != 'CURVE'):
			return False
		for obj in context.selected_objects:
			if (obj.name != context.object.name):
				if (obj.type == 'CURVE'):
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
	bl_label = "ベベル指定コピー"
	bl_description = "アクティブカーブオブジェクトに指定されているベベルオブジェクトを、他の選択カーブオブジェクトにコピーします"
	bl_options = {'REGISTER', 'UNDO'}
	
	@classmethod
	def poll(cls, context):
		if (not context.object):
			return False
		if (context.object.type != 'CURVE'):
			return False
		for obj in context.selected_objects:
			if (obj.name != context.object.name):
				if (obj.type == 'CURVE'):
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
		if (2 <= len(context.selected_objects)):
			i = 0
			for obj in context.selected_objects:
				if (obj.type == 'CURVE'):
					i += 1
			if (2 <= i):
				row = self.layout.row()
				row.operator(CopyTaperObject.bl_idname, icon='PLUGIN')
				row.operator(CopyBevelObject.bl_idname, icon='PLUGIN')
	if (context.user_preferences.addons["Scramble Addon"].preferences.use_disabled_menu):
		self.layout.operator('wm.toggle_menu_enable', icon='CANCEL').id = __name__.split('.')[-1]
