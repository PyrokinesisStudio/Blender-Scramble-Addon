# 3Dビュー > オブジェクトモード > 「オブジェクト」メニュー

import bpy

################
# パイメニュー #
################

class CopyPieOperator(bpy.types.Operator):
	bl_idname = "object.copy_pie_operator"
	bl_label = "コピー"
	bl_description = "オブジェクトに関するコピーのパイメニューです"
	bl_options = {'REGISTER', 'UNDO'}
	
	def execute(self, context):
		bpy.ops.wm.call_menu_pie(name=CopyPie.bl_idname)
		return {'FINISHED'}
class CopyPie(bpy.types.Menu):
	bl_idname = "VIEW3D_MT_object_pie_copy"
	bl_label = "コピー"
	bl_description = "オブジェクトに関するコピーのパイメニューです"
	
	def draw(self, context):
		self.layout.menu_pie().operator("view3d.copybuffer", icon="COPY_ID")
		self.layout.menu_pie().operator(CopyObjectName.bl_idname, icon="MONKEY")

class ObjectModePieOperator(bpy.types.Operator):
	bl_idname = "object.object_mode_pie_operator"
	bl_label = "オブジェクト対話モード"
	bl_description = "オブジェクト対話モードのパイメニューです"
	bl_options = {'REGISTER', 'UNDO'}
	
	def execute(self, context):
		bpy.ops.wm.call_menu_pie(name=ObjectModePie.bl_idname)
		return {'FINISHED'}
class ObjectModePie(bpy.types.Menu):
	bl_idname = "VIEW3D_MT_object_pie_object_mode"
	bl_label = "オブジェクト対話モード"
	bl_description = "オブジェクト対話モードのパイメニューです"
	
	def draw(self, context):
		self.layout.menu_pie().operator(SetObjectMode.bl_idname, text="ポーズ", icon="POSE_HLT").mode = "POSE"
		self.layout.menu_pie().operator(SetObjectMode.bl_idname, text="スカルプト", icon="SCULPTMODE_HLT").mode = "SCULPT"
		self.layout.menu_pie().operator(SetObjectMode.bl_idname, text="ウェイトペイント", icon="WPAINT_HLT").mode = "WEIGHT_PAINT"
		self.layout.menu_pie().operator(SetObjectMode.bl_idname, text="オブジェクト", icon="OBJECT_DATAMODE").mode = "OBJECT"
		self.layout.menu_pie().operator(SetObjectMode.bl_idname, text="パーティクル編集", icon="PARTICLEMODE").mode = "PARTICLE_EDIT"
		self.layout.menu_pie().operator(SetObjectMode.bl_idname, text="編集", icon="EDITMODE_HLT").mode = "EDIT"
		self.layout.menu_pie().operator(SetObjectMode.bl_idname, text="テクスチャペイント", icon="TPAINT_HLT").mode = "TEXTURE_PAINT"
		self.layout.menu_pie().operator(SetObjectMode.bl_idname, text="頂点ペイント", icon="VPAINT_HLT").mode = "VERTEX_PAINT"
class SetObjectMode(bpy.types.Operator): #
	bl_idname = "object.set_object_mode"
	bl_label = "オブジェクト対話モードを設定"
	bl_description = "オブジェクトの対話モードを設定します"
	bl_options = {'REGISTER'}
	
	mode = bpy.props.StringProperty(name="対話モード", default="OBJECT")
	
	def execute(self, context):
		if (context.active_object):
			try:
				bpy.ops.object.mode_set(mode=self.mode)
			except TypeError:
				self.report(type={"WARNING"}, message=context.active_object.name+" はその対話モードに入る事が出来ません")
		else:
			self.report(type={"WARNING"}, message="アクティブなオブジェクトがありません")
		return {'FINISHED'}

class SubdivisionSetPieOperator(bpy.types.Operator):
	bl_idname = "object.subdivision_set_pie_operator"
	bl_label = "サブサーフ設定"
	bl_description = "サブサーフのレベルを設定するパイメニューです"
	bl_options = {'REGISTER', 'UNDO'}
	
	def execute(self, context):
		bpy.ops.wm.call_menu_pie(name=SubdivisionSetPie.bl_idname)
		return {'FINISHED'}
class SubdivisionSetPie(bpy.types.Menu):
	bl_idname = "VIEW3D_MT_object_pie_subdivision_set"
	bl_label = "サブサーフ設定"
	bl_description = "サブサーフのレベルを設定するパイメニューです"
	
	def draw(self, context):
		self.layout.menu_pie().operator("object.subdivision_set", text="レベル:2", icon="MOD_SUBSURF").level = 2
		self.layout.menu_pie().operator("object.subdivision_set", text="レベル:6", icon="MOD_SUBSURF").level = 6
		self.layout.menu_pie().operator("object.subdivision_set", text="レベル:0", icon="MOD_SUBSURF").level = 0
		self.layout.menu_pie().operator("object.subdivision_set", text="レベル:4", icon="MOD_SUBSURF").level = 4
		self.layout.menu_pie().operator("object.subdivision_set", text="レベル:3", icon="MOD_SUBSURF").level = 3
		self.layout.menu_pie().operator("object.subdivision_set", text="レベル:5", icon="MOD_SUBSURF").level = 5
		self.layout.menu_pie().operator("object.subdivision_set", text="レベル:1", icon="MOD_SUBSURF").level = 1

class DrawTypePieOperator(bpy.types.Operator):
	bl_idname = "object.draw_type_pie_operator"
	bl_label = "最高描画タイプ"
	bl_description = "最高描画タイプを設定するパイメニューです"
	bl_options = {'REGISTER', 'UNDO'}
	
	def execute(self, context):
		bpy.ops.wm.call_menu_pie(name=DrawTypePie.bl_idname)
		return {'FINISHED'}
class DrawTypePie(bpy.types.Menu):
	bl_idname = "VIEW3D_MT_object_pie_draw_type"
	bl_label = "最高描画タイプ"
	bl_description = "最高描画タイプを設定するパイメニューです"
	
	def draw(self, context):
		self.layout.menu_pie().operator(SetDrawType.bl_idname, text="バウンド", icon="BBOX").type = "BOUNDS"
		self.layout.menu_pie().operator(SetDrawType.bl_idname, text="ワイヤーフレーム", icon="WIRE").type = "WIRE"
		self.layout.menu_pie().operator(SetDrawType.bl_idname, text="ソリッド", icon="SOLID").type = "SOLID"
		self.layout.menu_pie().operator(SetDrawType.bl_idname, text="テクスチャ", icon="POTATO").type = "TEXTURED"
class SetDrawType(bpy.types.Operator): #
	bl_idname = "object.set_draw_type"
	bl_label = "最高描画タイプ設定"
	bl_description = "最高描画タイプを設定します"
	bl_options = {'REGISTER'}
	
	type = bpy.props.StringProperty(name="描画タイプ", default="OBJECT")
	
	def execute(self, context):
		for obj in context.selected_objects:
			obj.draw_type = self.type
		return {'FINISHED'}

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

class CopyObjectName(bpy.types.Operator):
	bl_idname = "object.copy_object_name"
	bl_label = "オブジェクト名をクリップボードにコピー"
	bl_description = "アクティブなオブジェクトの名前をクリップボードにコピーします"
	bl_options = {'REGISTER', 'UNDO'}
	
	def execute(self, context):
		context.window_manager.clipboard = context.active_object.name
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

################################
# オペレーター(モディファイア) #
################################

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

class PieMenu(bpy.types.Menu):
	bl_idname = "VIEW3D_MT_object_pie_menu"
	bl_label = "パイメニュー"
	bl_description = "オブジェクト操作に関するパイメニューです"
	
	def draw(self, context):
		self.layout.operator(CopyPieOperator.bl_idname, icon="PLUGIN")
		self.layout.operator(ObjectModePieOperator.bl_idname, icon="PLUGIN")
		self.layout.operator(SubdivisionSetPieOperator.bl_idname, icon="PLUGIN")
		self.layout.operator(DrawTypePieOperator.bl_idname, icon="PLUGIN")

class ArmatureMenu(bpy.types.Menu):
	bl_idname = "VIEW3D_MT_object_armature"
	bl_label = "アーマチュア関係"
	bl_description = "アーマチュア関係の操作です"
	
	def draw(self, context):
		self.layout.operator(SetArmatureDeformPreserveVolume.bl_idname, icon="PLUGIN")

class BooleanMenu(bpy.types.Menu):
	bl_idname = "VIEW3D_MT_object_boolean"
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

class SubsurfMenu(bpy.types.Menu):
	bl_idname = "VIEW3D_MT_object_subsurf"
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
	bl_idname = "VIEW3D_MT_object_modifier"
	bl_label = "モディファイア関係"
	bl_description = "モディファイア関係の操作です"
	
	def draw(self, context):
		self.layout.operator(ToggleApplyModifiersView.bl_idname, icon="PLUGIN")
		self.layout.operator(DeleteAllModifiers.bl_idname, icon="PLUGIN")
		self.layout.separator()
		self.layout.menu(SubsurfMenu.bl_idname, icon="PLUGIN")
		self.layout.menu(ArmatureMenu.bl_idname, icon="PLUGIN")
		self.layout.menu(BooleanMenu.bl_idname, icon="PLUGIN")

class UVMenu(bpy.types.Menu):
	bl_idname = "VIEW3D_MT_object_uv"
	bl_label = "UV関係"
	bl_description = "UV関係の操作です"
	
	def draw(self, context):
		self.layout.operator(RenameUV.bl_idname, icon="PLUGIN")
		self.layout.operator(DeleteEmptyUV.bl_idname, icon="PLUGIN")

class ShortcutMenu(bpy.types.Menu):
	bl_idname = "VIEW3D_MT_object_shortcut"
	bl_label = "ショートカット登録用"
	bl_description = "ショートカットに登録すると便利そうな機能群です"
	
	def draw(self, context):
		self.layout.operator(CopyObjectName.bl_idname, icon="PLUGIN")
		self.layout.operator(DeleteUnmassage.bl_idname, icon="PLUGIN")
		self.layout.operator(ApplyModifiersAndJoin.bl_idname, icon="PLUGIN")

################
# メニュー追加 #
################

# メニューを登録する関数
def menu(self, context):
	self.layout.separator()
	self.layout.menu(ModifierMenu.bl_idname, icon="PLUGIN")
	self.layout.menu(UVMenu.bl_idname, icon="PLUGIN")
	self.layout.separator()
	self.layout.menu(ShortcutMenu.bl_idname, icon="PLUGIN")
	self.layout.menu(PieMenu.bl_idname, icon="PLUGIN")
