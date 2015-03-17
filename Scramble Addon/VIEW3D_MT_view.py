# 3Dビュー > 「ビュー」メニュー

import bpy

################
# オペレーター #
################

class LocalViewEx(bpy.types.Operator):
	bl_idname = "view3d.local_view_ex"
	bl_label = "グローバルビュー/ローカルビュー(非ズーム)"
	bl_description = "選択したオブジェクトのみを表示し、視点の中央に配置します(ズームはしません)"
	bl_options = {'REGISTER'}
	
	def execute(self, context):
		pre_smooth_view = context.user_preferences.view.smooth_view
		context.user_preferences.view.smooth_view = 0
		pre_view_distance = context.region_data.view_distance
		pre_view_location = context.region_data.view_location.copy()
		pre_view_rotation = context.region_data.view_rotation.copy()
		pre_cursor_location = context.space_data.cursor_location.copy()
		bpy.ops.view3d.localview()
		context.space_data.cursor_location = pre_cursor_location
		context.region_data.view_distance = pre_view_distance
		context.region_data.view_location = pre_view_location
		context.region_data.view_rotation = pre_view_rotation
		context.user_preferences.view.smooth_view = pre_smooth_view
		#bpy.ops.view3d.view_selected_ex()
		return {'FINISHED'}

class TogglePanelsA(bpy.types.Operator):
	bl_idname = "view3d.toggle_panels_a"
	bl_label = "パネル表示切り替え(モードA)"
	bl_description = "プロパティ/ツールシェルフの「両方表示」/「両方非表示」をトグルします"
	bl_options = {'REGISTER'}
	
	def execute(self, context):
		toolW = 0
		uiW = 0
		for region in context.area.regions:
			if (region.type == 'TOOLS'):
				toolW = region.width
			if (region.type == 'UI'):
				uiW = region.width
		if (1 < toolW or 1 < uiW):
			if (1 < toolW):
				bpy.ops.view3d.toolshelf()
			if (1 < uiW):
				bpy.ops.view3d.properties()
		else:
			bpy.ops.view3d.toolshelf()
			bpy.ops.view3d.properties()
		return {'FINISHED'}

class TogglePanelsB(bpy.types.Operator):
	bl_idname = "view3d.toggle_panels_b"
	bl_label = "パネル表示切り替え(モードB)"
	bl_description = "「パネル両方非表示」→「ツールシェルフのみ表示」→「プロパティのみ表示」→「パネル両方表示」のトグル"
	bl_options = {'REGISTER'}
	
	def execute(self, context):
		toolW = 0
		uiW = 0
		for region in context.area.regions:
			if (region.type == 'TOOLS'):
				toolW = region.width
			if (region.type == 'UI'):
				uiW = region.width
		if (toolW <= 1 and uiW <= 1):
			bpy.ops.view3d.toolshelf()
		elif (toolW <= 1 and 1 < uiW):
			bpy.ops.view3d.toolshelf()
		else:
			bpy.ops.view3d.toolshelf()
			bpy.ops.view3d.properties()
		return {'FINISHED'}

################
# パイメニュー #
################

class PieMenu(bpy.types.Menu):
	bl_idname = "VIEW3D_MT_view_pie"
	bl_label = "パイメニュー"
	bl_description = "3Dビュー関係のパイメニューです"
	
	def draw(self, context):
		self.layout.operator(ViewNumpadPieOperator.bl_idname, icon="PLUGIN")
		self.layout.operator(ViewportShadePieOperator.bl_idname, icon="PLUGIN")

class ViewNumpadPieOperator(bpy.types.Operator):
	bl_idname = "view3d.view_numpad_pie_operator"
	bl_label = "プリセットビュー"
	bl_description = "プリセットビュー(テンキー1,3,7とか)のパイメニューです"
	bl_options = {'REGISTER', 'UNDO'}
	
	def execute(self, context):
		bpy.ops.wm.call_menu_pie(name=ViewNumpadPie.bl_idname)
		return {'FINISHED'}
class ViewNumpadPie(bpy.types.Menu): #
	bl_idname = "VIEW3D_MT_view_pie_view_numpad"
	bl_label = "プリセットビュー"
	bl_description = "プリセットビュー(テンキー1,3,7とか)のパイメニューです"
	
	def draw(self, context):
		self.layout.menu_pie().operator("view3d.viewnumpad", text="左", icon="TRIA_LEFT").type = "LEFT"
		self.layout.menu_pie().operator("view3d.viewnumpad", text="右", icon="TRIA_RIGHT").type = "RIGHT"
		self.layout.menu_pie().operator("view3d.viewnumpad", text="下", icon="TRIA_DOWN").type = "BOTTOM"
		self.layout.menu_pie().operator("view3d.viewnumpad", text="上", icon="TRIA_UP").type = "TOP"
		self.layout.menu_pie().operator("view3d.viewnumpad", text="後", icon="BBOX").type = "BACK"
		self.layout.menu_pie().operator("view3d.viewnumpad", text="カメラ", icon="CAMERA_DATA").type = "CAMERA"
		self.layout.menu_pie().operator("view3d.viewnumpad", text="前", icon="SOLID").type = "FRONT"
		self.layout.menu_pie().operator("view3d.view_persportho", text="透視投影/平行投影", icon="BORDERMOVE")

class ViewportShadePieOperator(bpy.types.Operator):
	bl_idname = "view3d.viewport_shade_pie_operator"
	bl_label = "シェーディング切り替え"
	bl_description = "シェーディング切り替えパイメニューです"
	bl_options = {'REGISTER', 'UNDO'}
	
	def execute(self, context):
		bpy.ops.wm.call_menu_pie(name=ViewportShadePie.bl_idname)
		return {'FINISHED'}
class ViewportShadePie(bpy.types.Menu): #
	bl_idname = "VIEW3D_MT_view_pie_viewport_shade"
	bl_label = "シェーディング切り替え"
	bl_description = "シェーディング切り替えパイメニューです"
	
	def draw(self, context):
		self.layout.menu_pie().operator(SetViewportShade.bl_idname, text="バウンディングボックス", icon="BBOX").mode = "BOUNDBOX"
		self.layout.menu_pie().operator(SetViewportShade.bl_idname, text="レンダー", icon="SMOOTH").mode = "RENDERED"
		self.layout.menu_pie().operator(SetViewportShade.bl_idname, text="ソリッド", icon="SOLID").mode = "SOLID"
		self.layout.menu_pie().operator(SetViewportShade.bl_idname, text="テクスチャ", icon="POTATO").mode = "TEXTURED"
		self.layout.menu_pie().operator(SetViewportShade.bl_idname, text="ワイヤーフレーム", icon="WIRE").mode = "WIREFRAME"
		self.layout.menu_pie().operator(SetViewportShade.bl_idname, text="マテリアル", icon="MATERIAL").mode = "MATERIAL"
class SetViewportShade(bpy.types.Operator): #
	bl_idname = "view3d.set_viewport_shade"
	bl_label = "シェーディング切り替え"
	bl_description = "シェーディングを切り替えます"
	bl_options = {'REGISTER', 'UNDO'}
	
	mode = bpy.props.StringProperty(name="シェーディング", default="SOLID")
	
	def execute(self, context):
		context.space_data.viewport_shade = self.mode
		return {'FINISHED'}

########################
# グループレイヤー関係 #
########################

class ShowLayerGroupMenu(bpy.types.Operator):
	bl_idname = "view3d.show_layer_group_menu"
	bl_label = "グループで表示/非表示を切り替え"
	bl_description = "所属しているグループで表示/非表示を切り替えます"
	bl_options = {'REGISTER', 'UNDO'}
	
	def execute(self, context):
		bpy.ops.wm.call_menu(name=LayerGroupMenu.bl_idname)
		return {'FINISHED'}
class LayerGroupMenu(bpy.types.Menu):
	bl_idname = "VIEW3D_MT_object_layer_group"
	bl_label = "グループで表示/非表示を切り替え"
	bl_description = "所属しているグループで表示/非表示を切り替えます"
	
	def draw(self, context):
		objs = []
		for obj in bpy.data.objects:
			for l1 in obj.layers:
				for l2 in context.scene.layers:
					if (l1 and l2):
						for obj2 in objs:
							if (obj.name == obj2.name):
								break
						else:
							objs.append(obj)
		groups = []
		for obj in objs:
			for group in obj.users_group:
				if (not group in groups):
					groups.append(group)
		self.layout.operator(ApplyLayerGroup.bl_idname, icon="PLUGIN", text="グループ無所属").group = ""
		self.layout.separator()
		for group in groups:
			self.layout.operator(ApplyLayerGroup.bl_idname, icon="PLUGIN", text=group.name).group = group.name

class ApplyLayerGroup(bpy.types.Operator): #
	bl_idname = "view3d.apply_layer_group"
	bl_label = "グループで表示/非表示を切り替え実行"
	bl_description = "所属しているグループで表示/非表示を切り替えます"
	bl_options = {'REGISTER', 'UNDO'}
	
	group = bpy.props.StringProperty(name="グループ名")
	
	def execute(self, context):
		for obj in bpy.data.objects:
			for l1 in obj.layers:
				for l2 in context.scene.layers:
					if (l1 and l2):
						if (self.group != ""):
							for group in obj.users_group:
								if (group.name == self.group):
									obj.hide = False
									break
							else:
								obj.hide = True
						else:
							if (len(obj.users_group) == 0):
								obj.hide = False
							else:
								obj.hide = True
		return {'FINISHED'}

################
# サブメニュー #
################

class ShortcutsMenu(bpy.types.Menu):
	bl_idname = "VIEW3D_MT_view_shortcuts"
	bl_label = "ショートカット登録用"
	bl_description = "ショートカットに登録すると便利かもしれない機能群です"
	
	def draw(self, context):
		self.layout.operator(LocalViewEx.bl_idname, icon="PLUGIN")
		self.layout.separator()
		self.layout.operator(TogglePanelsA.bl_idname, icon="PLUGIN")
		self.layout.operator(TogglePanelsB.bl_idname, icon="PLUGIN")

################
# メニュー追加 #
################

# メニューを登録する関数
def menu(self, context):
	self.layout.separator()
	self.layout.prop(context.user_preferences.view, "use_rotate_around_active", icon="PLUGIN")
	self.layout.operator(ShowLayerGroupMenu.bl_idname, icon="PLUGIN")
	self.layout.separator()
	self.layout.menu(ShortcutsMenu.bl_idname, icon="PLUGIN")
	self.layout.menu(PieMenu.bl_idname, icon="PLUGIN")
