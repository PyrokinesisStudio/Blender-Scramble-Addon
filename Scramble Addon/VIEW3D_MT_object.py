import bpy

##############
# その他関数 #
##############

################
# オペレーター #
################

class DeleteUnmassage(bpy.types.Operator):
	bl_idname = "object.delete_unmassage"
	bl_label = "確認せずに削除"
	bl_description = "削除する時の確認メッセージを表示せずにオブジェクトを削除します"
	bl_options = {'REGISTER', 'UNDO'}
	
	use_global = bpy.props.BoolProperty(name="全体的に削除", default=False)
	
	def execute(self, context):
		bpy.ops.object.delete(use_global=self.use_global)
		return {'FINISHED'}

####################
# オペレーター(UV) #
####################

class RenameUV(bpy.types.Operator):
	bl_idname = "object.rename_uv"
	bl_label = "UV名を変更"
	bl_description = "アクティブなUVの名前を変更します(テクスチャのUV指定もそれに伴って変更します)"
	bl_options = {'REGISTER', 'UNDO'}
	
	name =  bpy.props.StringProperty(name="新しいUV名", default="UV")
	
	def execute(self, context):
		obj = context.active_object
		if (obj.type == "MESH"):
			me = obj.data
			uv = me.uv_layers.active
			if (uv == None):
				self.report(type={"ERROR"}, message="UVが存在しません")
				return {"CANCELLED"}
			preName = uv.name
			uv.name = self.name
			for mat in me.materials:
				if (mat):
					for slot in mat.texture_slots:
						if (slot != None):
							if (slot.uv_layer == preName):
									slot.uv_layer = uv.name
									self.report(type={"INFO"}, message="マテリアル「"+mat.name+"」のUV指定を修正しました")
					for me2 in bpy.data.meshes:
						for mat2 in me2.materials:
							if (mat2):
								if (mat.name == mat2.name):
									try:
										me2.uv_layers[preName].name = uv.name
										self.report(type={"INFO"}, message="メッシュ「"+me2.name+"」のUV指定を修正しました")
									except KeyError: pass
		else:
			self.report(type={"ERROR"}, message="メッシュオブジェクトではありません")
			return {"CANCELLED"}
		return {'FINISHED'}

class DeleteEmptyUV(bpy.types.Operator):
	bl_idname = "object.delete_empty_uv"
	bl_label = "未使用のUVを削除"
	bl_description = "アクティブなオブジェクトのマテリアルで未使用なUVを全削除します(他の部分に使われているUVは消してしまいます)"
	bl_options = {'REGISTER', 'UNDO'}
	
	isAllSelected =  bpy.props.BoolProperty(name="全ての選択したメッシュ", default=False)
	
	def execute(self, context):
		objs = [context.active_object]
		if (self.isAllSelected):
			objs = context.selected_objects
		for obj in objs:
			if (obj.type == "MESH"):
				uvs = []
				for mat in obj.material_slots:
					if (mat):
						for slot in mat.material.texture_slots:
							if (slot):
								if (not slot.uv_layer in uvs):
									uvs.append(slot.uv_layer)
				me = obj.data
				preUV = me.uv_layers.active
				u = me.uv_layers[:]
				for uv in u:
					if (not uv.name in uvs):
						self.report(type={"INFO"}, message=uv.name+" を削除しました")
						me.uv_layers.active = uv
						bpy.ops.mesh.uv_texture_remove()
				me.uv_layers.active = preUV
			else:
				self.report(type={"WARNING"}, message=obj.name+"はメッシュオブジェクトではありません")
		return {'FINISHED'}

############################
# オペレーター(サブサーフ) #
############################

class SetRenderSubsurfLevel(bpy.types.Operator):
	bl_idname = "object.set_render_subsurf_level"
	bl_label = "レンダリング時の細分化数を設定"
	bl_description = "選択したオブジェクトのサブサーフモディファイアのレンダリング時の細分化数を設定します"
	bl_options = {'REGISTER', 'UNDO'}
	
	level = bpy.props.IntProperty(name="分割数", default=2, min=0, max=6)
	
	def execute(self, context):
		for obj in context.selected_objects:
			if (obj.type=="MESH" or obj.type=="CURVE" or obj.type=="SURFACE" or obj.type=="FONT" or obj.type=="LATTICE"):
				for modi in obj.modifiers:
					if (modi.type == "SUBSURF"):
						modi.render_levels = self.level
		return {'FINISHED'}

class EqualizeSubsurfLevel(bpy.types.Operator):
	bl_idname = "object.equalize_subsurf_level"
	bl_label = "プレビュー・レンダリングの細分化数を同じに"
	bl_description = "選択したオブジェクトのサブサーフモディファイアのプレビュー時とレンダリング時の細分化数を同じに設定します"
	bl_options = {'REGISTER', 'UNDO'}
	
	items = [
		("ToRender", "プレビュー → レンダリング", "", 1),
		("ToPreview", "レンダリング → プレビュー", "", 2),
		]
	mode = bpy.props.EnumProperty(items=items, name="設定方法")
	
	def execute(self, context):
		for obj in context.selected_objects:
			if (obj.type=="MESH" or obj.type=="CURVE" or obj.type=="SURFACE" or obj.type=="FONT" or obj.type=="LATTICE"):
				for modi in obj.modifiers:
					if (modi.type == "SUBSURF"):
						if (self.mode == "ToRender"):
							modi.render_levels = modi.levels
						else:
							modi.levels = modi.render_levels
		return {'FINISHED'}

class SetSubsurfOptimalDisplay(bpy.types.Operator):
	bl_idname = "object.set_subsurf_optimal_display"
	bl_label = "最適化表示を設定"
	bl_description = "選択したオブジェクトのサブサーフモディファイアの最適化表示を設定します"
	bl_options = {'REGISTER', 'UNDO'}
	
	mode =  bpy.props.BoolProperty(name="最適化表示")
	
	def execute(self, context):
		for obj in context.selected_objects:
			if (obj.type=="MESH" or obj.type=="CURVE" or obj.type=="SURFACE" or obj.type=="FONT" or obj.type=="LATTICE"):
				for modi in obj.modifiers:
					if (modi.type == "SUBSURF"):
						modi.show_only_control_edges = self.mode
		return {'FINISHED'}

class DeleteSubsurf(bpy.types.Operator):
	bl_idname = "object.delete_subsurf"
	bl_label = "選択オブジェクトのサブサーフを削除"
	bl_description = "選択したオブジェクトのサブサーフモディファイアを削除します"
	bl_options = {'REGISTER', 'UNDO'}
	
	def execute(self, context):
		for obj in context.selected_objects:
			if (obj.type=="MESH" or obj.type=="CURVE" or obj.type=="SURFACE" or obj.type=="FONT" or obj.type=="LATTICE"):
				for modi in obj.modifiers:
					if (modi.type == "SUBSURF"):
						obj.modifiers.remove(modi)
		return {'FINISHED'}

class AddSubsurf(bpy.types.Operator):
	bl_idname = "object.add_subsurf"
	bl_label = "選択オブジェクトにサブサーフを追加"
	bl_description = "選択したオブジェクトにサブサーフモディファイアを追加します"
	bl_options = {'REGISTER', 'UNDO'}
	
	
	subdivision_type = bpy.props.EnumProperty(items=[("CATMULL_CLARK", "カトマルクラーク", "", 1), ("SIMPLE", "シンプル", "", 2)], name="細分化方法")
	levels = bpy.props.IntProperty(name="ビューの分割数", default=2, min=0, max=6)
	render_levels = bpy.props.IntProperty(name="レンダーの分割数", default=2, min=0, max=6)
	use_subsurf_uv =  bpy.props.BoolProperty(name="UVを細分化", default=True)
	show_only_control_edges =  bpy.props.BoolProperty(name="最適化表示")
	
	def execute(self, context):
		for obj in context.selected_objects:
			if (obj.type=="MESH" or obj.type=="CURVE" or obj.type=="SURFACE" or obj.type=="FONT" or obj.type=="LATTICE"):
				modi = obj.modifiers.new("Subsurf", "SUBSURF")
				modi.subdivision_type = self.subdivision_type
				modi.levels = self.levels
				modi.render_levels = self.render_levels
				modi.use_subsurf_uv = self.use_subsurf_uv
				modi.show_only_control_edges = self.show_only_control_edges
		return {'FINISHED'}

##########################
# サブメニュー(Modifier) #
##########################

class SubsurfMenu(bpy.types.Menu):
	bl_idname = "object.subsurf_menu"
	bl_label = "サブサーフ関係"
	bl_description = "サブサーフェイス関係の操作です"
	
	def draw(self, context):
		self.layout.operator(AddSubsurf.bl_idname, icon="PLUGIN")
		self.layout.operator(DeleteSubsurf.bl_idname, icon="PLUGIN")
		self.layout.separator()
		self.layout.operator(SetRenderSubsurfLevel.bl_idname, icon="PLUGIN")
		self.layout.operator(EqualizeSubsurfLevel.bl_idname, icon="PLUGIN")
		self.layout.operator(SetSubsurfOptimalDisplay.bl_idname, icon="PLUGIN")

class ModifierMenu(bpy.types.Menu):
	bl_idname = "object.modifier_menu"
	bl_label = "モディファイア関係"
	bl_description = "モディファイア関係の操作です"
	
	def draw(self, context):
		self.layout.menu(SubsurfMenu.bl_idname, icon="PLUGIN")

class UVMenu(bpy.types.Menu):
	bl_idname = "VIEW3D_MT_object_uv_saidenka"
	bl_label = "UV関係"
	bl_description = "UV関係の操作です"
	
	def draw(self, context):
		self.layout.operator(RenameUV.bl_idname, icon="PLUGIN")
		self.layout.operator(DeleteEmptyUV.bl_idname, icon="PLUGIN")

################
# メニュー追加 #
################

# メニューを登録する関数
def menu(self, context):
	self.layout.separator()
	self.layout.operator(DeleteUnmassage.bl_idname, icon="PLUGIN")
	self.layout.menu(ModifierMenu.bl_idname, icon="PLUGIN")
	self.layout.menu(UVMenu.bl_idname, icon="PLUGIN")