# 「プロパティ」エリア > 「マテリアル」タブ

import bpy

################
# オペレーター #
################

class MoveMaterialSlot(bpy.types.Operator):
	bl_idname = "material.move_material_slot"
	bl_label = "マテリアルスロットを移動"
	bl_description = "アクティブなマテリアルスロットを移動させます"
	bl_options = {'REGISTER', 'UNDO'}
	
	items = [
		("UP", "上へ", "", 1),
		("DOWN", "下へ", "", 2),
		]
	mode = bpy.props.EnumProperty(items=items, name="モード")
	
	@classmethod
	def poll(cls, context):
		obj = context.active_object
		if (not obj):
			return False
		if (len(obj.material_slots) <= 1):
			return False
		return True
	def execute(self, context):
		activeObj = context.active_object
		if (self.mode == "UP"):
			sourceIndex = activeObj.active_material_index
			if (sourceIndex <= 0):
				self.report(type={"WARNING"}, message="既に一番上です")
				return {"CANCELLED"}
			targetIndex = sourceIndex - 1
		elif (self.mode == "DOWN"):
			sourceIndex = activeObj.active_material_index
			if (len(activeObj.material_slots)-1 <= sourceIndex):
				self.report(type={"WARNING"}, message="既に一番下です")
				return {"CANCELLED"}
			targetIndex = sourceIndex + 1
		sourceLink = activeObj.material_slots[sourceIndex].link
		sourceMaterial = activeObj.material_slots[sourceIndex].material
		activeObj.material_slots[sourceIndex].link = activeObj.material_slots[targetIndex].link
		activeObj.material_slots[sourceIndex].material = activeObj.material_slots[targetIndex].material
		activeObj.material_slots[targetIndex].link = sourceLink
		activeObj.material_slots[targetIndex].material = sourceMaterial
		activeObj.active_material_index = targetIndex
		
		me = activeObj.data
		for poly in me.polygons:
			if (poly.material_index == sourceIndex):
				poly.material_index = targetIndex
			elif (poly.material_index == targetIndex):
				poly.material_index = sourceIndex
		return {'FINISHED'}

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
		return True
	def execute(self, context):
		activeObj = context.active_object
		for i in range(activeObj.active_material_index):
			bpy.ops.material.move_material_slot(mode='UP')
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
		return True
	def execute(self, context):
		activeObj = context.active_object
		i = 0
		for slot in activeObj.material_slots:
			if (slot.material):
				lastSlotIndex = i
			i += 1
		for i in range(lastSlotIndex - activeObj.active_material_index):
			bpy.ops.material.move_material_slot(mode='DOWN')
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
		sub.operator(MoveMaterialSlot.bl_idname, icon='TRIA_UP', text="").mode = 'UP'
		sub.operator(MoveMaterialSlot.bl_idname, icon='TRIA_DOWN', text="").mode = 'DOWN'
		sub = row.row(align=True)
		sub.operator(MoveMaterialSlotTop.bl_idname, icon='TRIA_UP', text="一番上へ")
		sub.operator(MoveMaterialSlotBottom.bl_idname, icon='TRIA_DOWN', text="一番下へ")
	if (context.user_preferences.addons["Scramble Addon"].preferences.use_disabled_menu):
		self.layout.operator('wm.toggle_menu_enable', icon='CANCEL').id = __name__.split('.')[-1]
