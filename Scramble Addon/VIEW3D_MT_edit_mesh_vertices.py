import bpy

################
# オペレーター #
################

class CellMenuSeparateEX(bpy.types.Operator):
	bl_idname = "mesh.cell_menu_separate_ex"
	bl_label = "別オブジェクトに分離 (拡張)"
	bl_description = "「別オブジェクトに分離」の拡張メニューを呼び出します"
	bl_options = {'REGISTER', 'UNDO'}
	
	def execute(self, context):
		bpy.ops.wm.call_menu(name=SeparateEXMenu.bl_idname)
		return {'FINISHED'}

class SeparateSelectedEX(bpy.types.Operator):
	bl_idname = "mesh.separate_selected_ex"
	bl_label = "選択物 (分離側をアクティブ)"
	bl_description = "「選択物で分離」した後に分離した側のエディトモードに入ります"
	bl_options = {'REGISTER', 'UNDO'}
	
	def execute(self, context):
		objs = []
		for obj in context.selectable_objects:
			objs.append(obj.name)
		bpy.ops.mesh.separate(type='SELECTED')
		bpy.ops.object.mode_set(mode='OBJECT')
		bpy.ops.object.select_all(action='DESELECT')
		for obj in context.selectable_objects:
			if (not obj.name in objs):
				obj.select = True
				context.scene.objects.active = obj
				break
		bpy.ops.object.mode_set(mode='EDIT')
		bpy.ops.mesh.select_all(action='SELECT')
		return {'FINISHED'}

class DuplicateNewParts(bpy.types.Operator):
	bl_idname = "mesh.duplicate_new_parts"
	bl_label = "選択部を複製/新オブジェクトに"
	bl_description = "選択部分を複製・分離し新オブジェクトにしてからエディトモードに入ります"
	bl_options = {'REGISTER', 'UNDO'}
	
	def execute(self, context):
		objs = []
		for obj in context.selectable_objects:
			objs.append(obj.name)
		bpy.ops.mesh.duplicate()
		bpy.ops.mesh.separate(type='SELECTED')
		bpy.ops.object.mode_set(mode='OBJECT')
		bpy.ops.object.select_all(action='DESELECT')
		for obj in context.selectable_objects:
			if (not obj.name in objs):
				obj.select = True
				context.scene.objects.active = obj
				break
		bpy.ops.object.mode_set(mode='EDIT')
		bpy.ops.mesh.select_all(action='SELECT')
		return {'FINISHED'}

################
# メニュー追加 #
################

class SeparateEXMenu(bpy.types.Menu):
	bl_idname = "VIEW3D_MT_edit_mesh_separate_ex"
	bl_label = "別オブジェクトに分離 (拡張)"
	bl_description = "「別オブジェクトに分離」の拡張メニューです"
	
	def draw(self, context):
		self.layout.operator("mesh.separate", text="選択物").type = 'SELECTED'
		self.layout.operator(SeparateSelectedEX.bl_idname, icon="PLUGIN")
		self.layout.separator()
		self.layout.operator("mesh.separate", text="マテリアルで").type = 'MATERIAL'
		self.layout.operator("mesh.separate", text="構造的に分離したパーツで").type = 'LOOSE'


# メニューを登録する関数
def menu(self, context):
	self.layout.separator()
	self.layout.operator(CellMenuSeparateEX.bl_idname, icon="PLUGIN")
	self.layout.separator()
	self.layout.operator(DuplicateNewParts.bl_idname, icon="PLUGIN")
