# プロパティ > 「マテリアル」タブ > リスト右の▼

import bpy

################
# オペレーター #
################

class RemoveNoAssignMaterial(bpy.types.Operator):
	bl_idname = "material.remove_no_assign_material"
	bl_label = "割り当てのないマテリアルを削除"
	bl_description = "面に一つも割り当てられてないマテリアルを全て削除します"
	bl_options = {'REGISTER', 'UNDO'}
	
	def execute(self, context):
		preActiveObj = context.active_object
		for obj in context.selected_objects:
			if (obj.type == "MESH"):
				context.scene.objects.active = obj
				preActiveMaterial = obj.active_material
				slots = []
				for slot in obj.material_slots:
					slots.append((slot.name, 0))
				me = obj.data
				for face in me.polygons:
					slots[face.material_index] = (slots[face.material_index][0], slots[face.material_index][1] + 1)
				for name, count in slots:
					if (name != "" and count == 0):
						i = 0
						for slot in obj.material_slots:
							if (slot.name == name):
								break
							i += 1
						obj.active_material_index = i
						bpy.ops.object.material_slot_remove()
		context.scene.objects.active = preActiveObj
		return {'FINISHED'}

class RemoveAllMaterialSlot(bpy.types.Operator):
	bl_idname = "material.remove_all_material_slot"
	bl_label = "マテリアルスロット全削除"
	bl_description = "このオブジェクトのマテリアルスロットを全て削除します"
	bl_options = {'REGISTER', 'UNDO'}
	
	def execute(self, context):
		activeObj = context.active_object
		if (activeObj.type == "MESH"):
			while True:
				if (0 < len(activeObj.material_slots)):
					bpy.ops.object.material_slot_remove()
				else:
					break
		return {'FINISHED'}

class RemoveEmptyMaterialSlot(bpy.types.Operator):
	bl_idname = "material.remove_empty_material_slot"
	bl_label = "空のマテリアルスロット削除"
	bl_description = "このオブジェクトのマテリアルが割り当てられていないマテリアルスロットを全て削除します"
	bl_options = {'REGISTER', 'UNDO'}
	
	def execute(self, context):
		activeObj = context.active_object
		if (activeObj.type == "MESH"):
			slots = activeObj.material_slots[:]
			slots.reverse()
			i = 0
			for slot in slots:
				active_material_index = i
				if (not slot.material):
					bpy.ops.object.material_slot_remove()
				i += 1
		return {'FINISHED'}

################
# メニュー追加 #
################

# メニューを登録する関数
def menu(self, context):
	self.layout.separator()
	self.layout.operator(RemoveAllMaterialSlot.bl_idname, icon="PLUGIN")
	self.layout.operator(RemoveEmptyMaterialSlot.bl_idname, icon="PLUGIN")
	self.layout.operator(RemoveNoAssignMaterial.bl_idname, icon="PLUGIN")
