# 3Dビュー > アーマチュア編集モード > 「選択」メニュー

import bpy

################
# オペレーター #
################

class SelectAxisOver(bpy.types.Operator):
	bl_idname = "armature.select_axis_over"
	bl_label = "右半分を選択"
	bl_description = "ボーン群の右半分を選択します(その他設定も有)"
	bl_options = {'REGISTER', 'UNDO'}
	
	items = [
		("0", "X軸", "", 1),
		("1", "Y軸", "", 2),
		("2", "Z軸", "", 3),
		]
	axis = bpy.props.EnumProperty(items=items, name="軸")
	items = [
		("-1", "-(マイナス)", "", 1),
		("1", "+(プラス)", "", 2),
		]
	direction = bpy.props.EnumProperty(items=items, name="方向")
	offset = bpy.props.FloatProperty(name="オフセット", default=0, step=10, precision=3)
	threshold = bpy.props.FloatProperty(name="しきい値", default=-0.0001, step=0.01, precision=4)
	
	def execute(self, context):
		bpy.ops.object.mode_set(mode="OBJECT")
		activeObj = context.active_object
		arm = activeObj.data
		direction = int(self.direction)
		offset = self.offset
		threshold = self.threshold
		for bone in arm.bones:
			hLoc = bone.head_local[int(self.axis)]
			tLoc = bone.tail_local[int(self.axis)]
			if (offset * direction <= hLoc * direction + threshold):
				bone.select = True
			if (offset * direction <= tLoc * direction + threshold):
				bone.select = True
		bpy.ops.object.mode_set(mode="EDIT")
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
		self.layout.separator()
		self.layout.operator(SelectAxisOver.bl_idname, icon="PLUGIN")
	if (context.user_preferences.addons["Scramble Addon"].preferences.use_disabled_menu):
		self.layout.separator()
		self.layout.operator('wm.toggle_menu_enable', icon='CANCEL').id = __name__.split('.')[-1]
