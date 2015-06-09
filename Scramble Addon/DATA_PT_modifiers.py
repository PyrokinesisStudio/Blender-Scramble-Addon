# プロパティ > モディファイアタブ

import bpy

################
# オペレーター #
################

class ApplyAllModifiers(bpy.types.Operator):
	bl_idname = "object.apply_all_modifiers"
	bl_label = "全モディファイア適用"
	bl_description = "選択オブジェクトの全てのモディファイアを適用します"
	bl_options = {'REGISTER', 'UNDO'}
	
	def execute(self, context):
		for obj in context.selected_objects:
			for mod in obj.modifiers[:]:
				bpy.ops.object.modifier_apply(apply_as='DATA', modifier=mod.name)
		return {'FINISHED'}

class DeleteAllModifiers(bpy.types.Operator):
	bl_idname = "object.delete_all_modifiers"
	bl_label = "全モディファイア削除"
	bl_description = "選択オブジェクトの全てのモディファイアを削除します"
	bl_options = {'REGISTER', 'UNDO'}
	
	def execute(self, context):
		for obj in context.selected_objects:
			modifiers = obj.modifiers[:]
			for modi in modifiers:
				obj.modifiers.remove(modi)
		return {'FINISHED'}

class ToggleApplyModifiersView(bpy.types.Operator):
	bl_idname = "object.toggle_apply_modifiers_view"
	bl_label = "ビューへのモディファイア適用を切り替え"
	bl_description = "選択オブジェクトの全てのモディファイアのビューへの適用を切り替えます"
	bl_options = {'REGISTER'}
	
	def execute(self, context):
		is_apply = True
		for mod in context.active_object.modifiers:
			if (mod.show_viewport):
				is_apply = False
				break
		for obj in context.selected_objects:
			for mod in obj.modifiers:
				mod.show_viewport = is_apply
		if is_apply:
			self.report(type={"INFO"}, message="ビューにモディファイアを適用しました")
		else:
			self.report(type={"INFO"}, message="ビューへのモディファイア適用を解除しました")
		return {'FINISHED'}

class SyncShowModifiers(bpy.types.Operator):
	bl_idname = "object.sync_show_modifiers"
	bl_label = "モディファイア使用を同期"
	bl_description = "選択オブジェクトのレンダリング時/ビュー時のモディファイア使用を同期します"
	bl_options = {'REGISTER', 'UNDO'}
	
	items = [
		("1", "レンダリング → ビュー", "", 1),
		("0", "ビュー → レンダリング", "", 2),
		]
	mode = bpy.props.EnumProperty(items=items, name="演算", default="0")
	
	def invoke(self, context, event):
		return context.window_manager.invoke_props_dialog(self)
	def execute(self, context):
		for obj in context.selected_objects:
			for mod in obj.modifiers:
				if (int(self.mode)):
					mod.show_viewport = mod.show_render
				else:
					mod.show_render = mod.show_viewport
		return {'FINISHED'}

class ToggleAllShowExpanded(bpy.types.Operator):
	bl_idname = "wm.toggle_all_show_expanded"
	bl_label = "全モディファイアの展開/閉じるを切り替え"
	bl_description = "アクティブオブジェクトの全モディファイアを展開/閉じるを切り替え(トグル)します"
	bl_options = {'REGISTER'}
	
	def execute(self, context):
		obj = context.active_object
		if (len(obj.modifiers)):
			vs = 0
			for mod in obj.modifiers:
				if (mod.show_expanded):
					vs += 1
				else:
					vs -= 1
			is_close = False
			if (0 < vs):
				is_close = True
			for mod in obj.modifiers:
				mod.show_expanded = not is_close
		else:
			self.report(type={'WARNING'}, message="モディファイアが1つもありません")
			return {'CANCELLED'}
		for area in context.screen.areas:
			area.tag_redraw()
		return {'FINISHED'}

class ApplyModifiersAndJoin(bpy.types.Operator):
	bl_idname = "object.apply_modifiers_and_join"
	bl_label = "モディファイア適用+統合"
	bl_description = "オブジェクトのモディファイアを全適用してから統合します"
	bl_options = {'REGISTER', 'UNDO'}
	
	unapply_subsurf = bpy.props.BoolProperty(name="サブサーフ除く", default=True)
	unapply_armature = bpy.props.BoolProperty(name="アーマチュア除く", default=True)
	unapply_mirror = bpy.props.BoolProperty(name="ミラー除く", default=False)
	
	def execute(self, context):
		pre_active_object = context.active_object
		for obj in context.selected_objects:
			context.scene.objects.active = obj
			for mod in obj.modifiers[:]:
				if (self.unapply_subsurf and mod.type == 'SUBSURF'):
					continue
				if (self.unapply_armature and mod.type == 'ARMATURE'):
					continue
				if (self.unapply_mirror and mod.type == 'MIRROR'):
					continue
				bpy.ops.object.modifier_apply(apply_as='DATA', modifier=mod.name)
		context.scene.objects.active = pre_active_object
		bpy.ops.object.join()
		return {'FINISHED'}

class AutoRenameModifiers(bpy.types.Operator):
	bl_idname = "object.auto_rename_modifiers"
	bl_label = "モディファイア名を自動でリネーム"
	bl_description = "選択オブジェクトのモディファイア名を参照先などの名前にリネームします"
	bl_options = {'REGISTER', 'UNDO'}
	
	def execute(self, context):
		for obj in context.selected_objects:
			for mod in obj.modifiers:
				try:
					if (mod.subtarget):
						mod.name = mod.subtarget
					continue
				except AttributeError: pass
				try:
					if (mod.target):
						mod.name = mod.target.name
					continue
				except AttributeError: pass
				try:
					if (mod.object):
						mod.name = mod.object.name
					continue
				except AttributeError: pass
				try:
					if (mod.vertex_group):
						mod.name = mod.vertex_group
					continue
				except AttributeError: pass
		return {'FINISHED'}

############################
# オペレーター(ブーリアン) #
############################

class AddBoolean(bpy.types.Operator):
	bl_idname = "object.add_boolean"
	bl_label = "ブーリアンを追加"
	bl_description = "アクティブオブジェクトにその他選択オブジェクトのブーリアンを追加"
	bl_options = {'REGISTER', 'UNDO'}
	
	items = [
		("INTERSECT", "交差", "", 1),
		("UNION", "統合", "", 2),
		("DIFFERENCE", "差分", "", 3),
		]
	mode = bpy.props.EnumProperty(items=items, name="演算")
	
	def execute(self, context):
		activeObj = context.active_object
		for obj in context.selected_objects:
			if (obj.type == "MESH" and activeObj.name != obj.name):
				modi = activeObj.modifiers.new("Boolean", "BOOLEAN")
				modi.object = obj
				modi.operation = self.mode
				obj.draw_type = "BOUNDS"
		return {'FINISHED'}

class ApplyBoolean(bpy.types.Operator):
	bl_idname = "object.apply_boolean"
	bl_label = "ブーリアンを適用"
	bl_description = "アクティブオブジェクトにその他選択オブジェクトのブーリアンを適用"
	bl_options = {'REGISTER', 'UNDO'}
	
	items = [
		("INTERSECT", "交差", "", 1),
		("UNION", "統合", "", 2),
		("DIFFERENCE", "差分", "", 3),
		]
	mode = bpy.props.EnumProperty(items=items, name="演算")
	
	def execute(self, context):
		activeObj = context.active_object
		for obj in context.selected_objects:
			if (obj.type == "MESH" and activeObj.name != obj.name):
				modi = activeObj.modifiers.new("Boolean", "BOOLEAN")
				modi.object = obj
				modi.operation = self.mode
				bpy.ops.object.modifier_apply (modifier=modi.name)
				bpy.ops.object.select_all(action='DESELECT')
				obj.select = True
				bpy.ops.object.delete()
				activeObj.select = True
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

##############################
# オペレーター(アーマチュア) #
##############################

class SetArmatureDeformPreserveVolume(bpy.types.Operator):
	bl_idname = "object.set_armature_deform_preserve_volume"
	bl_label = "アーマチュアの「体積を維持」をまとめて設定"
	bl_description = "選択したオブジェクトのアーマチュアモディファイアの「体積を維持」をまとめてオン/オフします"
	bl_options = {'REGISTER', 'UNDO'}
	
	use_deform_preserve_volume =  bpy.props.BoolProperty(name="「体積を維持」を使用", default=True)
	
	def execute(self, context):
		for obj in context.selected_objects:
			if (obj.type == "MESH"):
				for mod in obj.modifiers:
					if (mod.type == 'ARMATURE'):
						mod.use_deform_preserve_volume = self.use_deform_preserve_volume
		return {'FINISHED'}

################
# サブメニュー #
################

class ModifierMenu(bpy.types.Menu):
	bl_idname = "VIEW3D_MT_object_specials_modifier"
	bl_label = "モディファイア操作"
	bl_description = "モディファイア関係の操作です"
	
	def draw(self, context):
		self.layout.menu(SubsurfMenu.bl_idname, icon="PLUGIN")
		self.layout.menu(ArmatureMenu.bl_idname, icon="PLUGIN")
		self.layout.menu(BooleanMenu.bl_idname, icon="PLUGIN")
		self.layout.separator()
		self.layout.separator()
		self.layout.operator(ApplyAllModifiers.bl_idname, icon="PLUGIN")
		self.layout.operator(ApplyModifiersAndJoin.bl_idname, icon="PLUGIN")
		self.layout.separator()
		self.layout.operator(DeleteAllModifiers.bl_idname, icon="PLUGIN")
		self.layout.separator()
		self.layout.operator(AutoRenameModifiers.bl_idname, icon="PLUGIN")
		self.layout.separator()
		self.layout.operator(ToggleApplyModifiersView.bl_idname, icon="PLUGIN")
		self.layout.operator(ToggleAllShowExpanded.bl_idname, icon="PLUGIN")
		self.layout.operator(SyncShowModifiers.bl_idname, icon="PLUGIN")

class SubsurfMenu(bpy.types.Menu):
	bl_idname = "VIEW3D_MT_object_specials_subsurf"
	bl_label = "サブサーフ関係"
	bl_description = "サブサーフェイス関係の操作です"
	
	def draw(self, context):
		self.layout.operator(AddSubsurf.bl_idname, icon="PLUGIN")
		self.layout.operator(DeleteSubsurf.bl_idname, icon="PLUGIN")
		self.layout.separator()
		self.layout.operator(SetRenderSubsurfLevel.bl_idname, icon="PLUGIN")
		self.layout.operator(EqualizeSubsurfLevel.bl_idname, icon="PLUGIN")
		self.layout.operator(SetSubsurfOptimalDisplay.bl_idname, icon="PLUGIN")

class BooleanMenu(bpy.types.Menu):
	bl_idname = "VIEW3D_MT_object_specials_boolean"
	bl_label = "ブーリアン関係"
	bl_description = "ブーリアン関係の操作です"
	
	def draw(self, context):
		self.layout.operator(AddBoolean.bl_idname, icon="PLUGIN", text="ブーリアン追加 (交差)").mode = "INTERSECT"
		self.layout.operator(AddBoolean.bl_idname, icon="PLUGIN", text="ブーリアン追加 (統合)").mode = "UNION"
		self.layout.operator(AddBoolean.bl_idname, icon="PLUGIN", text="ブーリアン追加 (差分)").mode = "DIFFERENCE"
		self.layout.separator()
		self.layout.operator(ApplyBoolean.bl_idname, icon="PLUGIN", text="ブーリアン適用 (交差)").mode = "INTERSECT"
		self.layout.operator(ApplyBoolean.bl_idname, icon="PLUGIN", text="ブーリアン適用 (統合)").mode = "UNION"
		self.layout.operator(ApplyBoolean.bl_idname, icon="PLUGIN", text="ブーリアン適用 (差分)").mode = "DIFFERENCE"

class ArmatureMenu(bpy.types.Menu):
	bl_idname = "VIEW3D_MT_object_specials_armature"
	bl_label = "アーマチュア関係"
	bl_description = "アーマチュア関係の操作です"
	
	def draw(self, context):
		self.layout.operator(SetArmatureDeformPreserveVolume.bl_idname, icon="PLUGIN")

################
# メニュー追加 #
################

# メニューを登録する関数
def menu(self, context):
	self.layout.menu(ModifierMenu.bl_idname, icon="PLUGIN")
