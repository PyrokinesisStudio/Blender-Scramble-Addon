# 「3Dビュー」エリア > プロパティパネル > 「アイテム」パネル

import bpy

################
# オペレーター #
################

class CopyObjectName(bpy.types.Operator):
	bl_idname = "object.copy_object_name"
	bl_label = "オブジェクト名をコピー"
	bl_description = "オブジェクト名をクリップボードにコピーします"
	bl_options = {'REGISTER'}
	
	@classmethod
	def poll(cls, context):
		if (not context.object):
			return False
		return True
	def execute(self, context):
		context.window_manager.clipboard = context.object.name
		self.report(type={'INFO'}, message=context.object.name)
		return {'FINISHED'}

class CopyDataName(bpy.types.Operator):
	bl_idname = "object.copy_data_name"
	bl_label = "データ名をコピー"
	bl_description = "データ名をクリップボードにコピーします"
	bl_options = {'REGISTER'}
	
	@classmethod
	def poll(cls, context):
		if (not context.object):
			return False
		if (not context.object.data):
			return False
		return True
	def execute(self, context):
		context.window_manager.clipboard = context.object.data.name
		self.report(type={'INFO'}, message=context.object.data.name)
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
		row = self.layout.row(align=True)
		row.operator('object.object_name_to_data_name', icon='TRIA_DOWN', text="")
		row.operator(CopyObjectName.bl_idname, icon='MOVE_UP_VEC', text="コピー")
		row.operator(CopyDataName.bl_idname, icon='MOVE_DOWN_VEC', text="コピー")
		row.operator('object.data_name_to_object_name', icon='TRIA_UP', text="")
		row = self.layout.row()
		row.label(text="", icon='MESH_DATA')
		row.prop(context.object.data, 'name', text="")
	if (context.user_preferences.addons["Scramble Addon"].preferences.use_disabled_menu):
		self.layout.operator('wm.toggle_menu_enable', icon='CANCEL').id = __name__.split('.')[-1]
