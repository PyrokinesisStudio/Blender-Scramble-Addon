import bpy

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
