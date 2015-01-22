import bpy

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
		bpy.ops.wm.call_menu_pie(name=ViewNumpadPiePie.bl_idname)
		return {'FINISHED'}
class ViewNumpadPiePie(bpy.types.Menu):
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

class ViewportShadePieOperator(bpy.types.Operator):
	bl_idname = "view3d.viewport_shade_pie_operator"
	bl_label = "シェーディング切り替え"
	bl_description = "シェーディング切り替えパイメニューです"
	bl_options = {'REGISTER', 'UNDO'}
	
	def execute(self, context):
		bpy.ops.wm.call_menu_pie(name=ViewportShadePie.bl_idname)
		return {'FINISHED'}
class ViewportShadePie(bpy.types.Menu):
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
class SetViewportShade(bpy.types.Operator):
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

class ApplyLayerGroup(bpy.types.Operator):
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
# オペレーター #
################

class ResetCursor(bpy.types.Operator):
	bl_idname = "view3d.reset_cursor"
	bl_label = "カーソルの位置をリセット"
	bl_description = "カーソルのXYZを0.0にします(他の位置も可)"
	bl_options = {'REGISTER', 'UNDO'}
	
	co = bpy.props.FloatVectorProperty(name="カーソル位置", default=(0.0, 0.0, 0.0), step=10, precision=3)
	isLookCenter = bpy.props.BoolProperty(name="視点を3Dカーソルに", default=False)
	
	def execute(self, context):
		context.space_data.cursor_location = self.co
		if (self.isLookCenter):
			bpy.ops.view3d.view_center_cursor()
		return {'FINISHED'}

################
# メニュー追加 #
################

# メニューを登録する関数
def menu(self, context):
	self.layout.separator()
	self.layout.operator(ResetCursor.bl_idname, icon="PLUGIN")
	self.layout.separator()
	self.layout.operator(ShowLayerGroupMenu.bl_idname, icon="PLUGIN")
	self.layout.separator()
	self.layout.menu(PieMenu.bl_idname, icon="PLUGIN")
