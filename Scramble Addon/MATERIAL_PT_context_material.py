# 「プロパティ」エリア > 「マテリアル」タブ

import bpy

################
# オペレーター #
################

class MoveMaterialSlotTop(bpy.types.Operator):
	bl_idname = "material.move_material_slot_top"
	bl_label = "スロットを一番上へ"
	bl_description = "アクティブなマテリアルスロットを一番上に移動させます"
	bl_options = {'REGISTER', 'UNDO'}
	
	@classmethod
	def poll(cls, context):
		obj = context.active_object
		if (not obj):
			return False
		if (len(obj.material_slots) <= 2):
			return False
		if (obj.active_material_index <= 0):
			return False
		return True
	def execute(self, context):
		activeObj = context.active_object
		for i in range(activeObj.active_material_index):
			bpy.ops.object.material_slot_move(direction='UP')
		return {'FINISHED'}

class MoveMaterialSlotBottom(bpy.types.Operator):
	bl_idname = "material.move_material_slot_bottom"
	bl_label = "スロットを一番下へ"
	bl_description = "アクティブなマテリアルスロットを一番下に移動させます"
	bl_options = {'REGISTER', 'UNDO'}
	
	@classmethod
	def poll(cls, context):
		obj = context.active_object
		if (not obj):
			return False
		if (len(obj.material_slots) <= 2):
			return False
		if (len(obj.material_slots)-1 <= obj.active_material_index):
			return False
		return True
	def execute(self, context):
		activeObj = context.active_object
		lastSlotIndex = len(activeObj.material_slots) - 1
		for i in range(lastSlotIndex - activeObj.active_material_index):
			bpy.ops.object.material_slot_move(direction='DOWN')
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
		row = self.layout.row()
		sub = row.row(align=True)
		sub.operator(MoveMaterialSlotTop.bl_idname, icon='TRIA_UP', text="一番上へ")
		sub.operator(MoveMaterialSlotBottom.bl_idname, icon='TRIA_DOWN', text="一番下へ")
	if (context.user_preferences.addons["Scramble Addon"].preferences.use_disabled_menu):
		self.layout.operator('wm.toggle_menu_enable', icon='CANCEL').id = __name__.split('.')[-1]
