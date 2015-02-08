# 3Dビュー > オブジェクトモード > 「オブジェクト」メニュー > 「表示/隠す」メニュー

import bpy

################
# オペレーター #
################

class InvertHide(bpy.types.Operator):
	bl_idname = "object.invert_hide"
	bl_label = "表示/隠すを反転"
	bl_description = "オブジェクトの表示状態と非表示状態を反転させます"
	bl_options = {'REGISTER', 'UNDO'}
	
	def execute(self, context):
		objs = []
		for obj in bpy.data.objects:
			for i in range(len(bpy.context.scene.layers)):
				if (bpy.context.scene.layers[i] and obj.layers[i]):
					for obj2 in objs:
						if (obj.name == obj2.name):
							break
					else:
						objs.append(obj)
		for obj in objs:
			obj.hide = not obj.hide
		return {'FINISHED'}

class HideOnlyType(bpy.types.Operator):
	bl_idname = "object.hide_only_mesh"
	bl_label = "特定の種類のオブジェクトのみを隠す"
	bl_description = "表示されている特定タイプのオブジェクトを隠します"
	bl_options = {'REGISTER', 'UNDO'}
	
	items = [
		("MESH", "メッシュ", "", 1),
		("CURVE", "カーブ", "", 2),
		("SURFACE", "サーフェイス", "", 3),
		("META", "メタボール", "", 4),
		("FONT", "テキスト", "", 5),
		("ARMATURE", "アーマチュア", "", 6),
		("LATTICE", "ラティス", "", 7),
		("EMPTY", "エンプティ", "", 8),
		("CAMERA", "カメラ", "", 9),
		("LAMP", "ランプ", "", 10),
		("SPEAKER", "スピーカー", "", 11),
		]
	type = bpy.props.EnumProperty(items=items, name="隠すオブジェクトのタイプ")
	
	def execute(self, context):
		for obj in context.selectable_objects:
			if (obj.type == self.type):
				obj.hide = True
		return {'FINISHED'}

class HideExceptType(bpy.types.Operator):
	bl_idname = "object.hide_except_mesh"
	bl_label = "特定の種類のオブジェクト以外を隠す"
	bl_description = "表示されている特定タイプのオブジェクト以外を隠します"
	bl_options = {'REGISTER', 'UNDO'}
	
	items = [
		("MESH", "メッシュ", "", 1),
		("CURVE", "カーブ", "", 2),
		("SURFACE", "サーフェイス", "", 3),
		("META", "メタボール", "", 4),
		("FONT", "テキスト", "", 5),
		("ARMATURE", "アーマチュア", "", 6),
		("LATTICE", "ラティス", "", 7),
		("EMPTY", "エンプティ", "", 8),
		("CAMERA", "カメラ", "", 9),
		("LAMP", "ランプ", "", 10),
		("SPEAKER", "スピーカー", "", 11),
		]
	type = bpy.props.EnumProperty(items=items, name="残すオブジェクトのタイプ")
	
	def execute(self, context):
		for obj in context.selectable_objects:
			if (obj.type != self.type):
				obj.hide = True
		return {'FINISHED'}

class SetRenderHide(bpy.types.Operator):
	bl_idname = "object.set_render_hide"
	bl_label = "選択物をレンダリングしない"
	bl_description = "選択中のオブジェクトをレンダリングしない設定にします(逆も可)"
	bl_options = {'REGISTER', 'UNDO'}
	
	reverse = bpy.props.BoolProperty(name="レンダリングしない", default=True)
	
	def execute(self, context):
		for obj in context.selected_objects:
			obj.hide_render = self.reverse
		return {'FINISHED'}

class SetHideSelect(bpy.types.Operator):
	bl_idname = "object.set_hide_select"
	bl_label = "選択物を選択不可に"
	bl_description = "選択中のオブジェクトを選択出来なくします"
	bl_options = {'REGISTER', 'UNDO'}
	
	reverse = bpy.props.BoolProperty(name="選択不可に", default=True)
	
	def execute(self, context):
		for obj in context.selected_objects:
			obj.hide_select = self.reverse
			if (self.reverse):
				obj.select = not self.reverse
		return {'FINISHED'}

class AllResetRenderHide(bpy.types.Operator):
	bl_idname = "object.all_reset_render_hide"
	bl_label = "全オブジェクトの非レンダリングを解除"
	bl_description = "全てのオブジェクトのレンダリングしない設定を解除します(逆も可)"
	bl_options = {'REGISTER', 'UNDO'}
	
	reverse = bpy.props.BoolProperty(name="レンダリングしない", default=False)
	
	def execute(self, context):
		for obj in bpy.data.objects:
			obj.hide_render = self.reverse
		return {'FINISHED'}

class AllResetHideSelect(bpy.types.Operator):
	bl_idname = "object.all_reset_hide_select"
	bl_label = "全オブジェクトの選択不可を解除"
	bl_description = "全てのオブジェクトの選択不可設定を解除します(逆も可)"
	bl_options = {'REGISTER', 'UNDO'}
	
	reverse = bpy.props.BoolProperty(name="選択不可に", default=False)
	
	def execute(self, context):
		for obj in bpy.data.objects:
			obj.hide_select = self.reverse
			if (self.reverse):
				obj.select = not self.reverse
		return {'FINISHED'}

################
# メニュー追加 #
################

# メニューを登録する関数
def menu(self, context):
	self.layout.separator()
	self.layout.operator(InvertHide.bl_idname, icon="PLUGIN")
	self.layout.separator()
	self.layout.operator(HideOnlyType.bl_idname, icon="PLUGIN")
	self.layout.operator(HideExceptType.bl_idname, icon="PLUGIN")
	self.layout.separator()
	self.layout.operator(SetRenderHide.bl_idname, icon="PLUGIN")
	self.layout.operator(SetHideSelect.bl_idname, icon="PLUGIN")
	self.layout.separator()
	self.layout.operator(AllResetRenderHide.bl_idname, icon="PLUGIN")
	self.layout.operator(AllResetHideSelect.bl_idname, icon="PLUGIN")
