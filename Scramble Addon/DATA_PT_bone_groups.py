# 「プロパティ」エリア > 「アーマチュアデータ」タブ > 「ボーングループ」パネル

import bpy

################
# オペレーター #
################

class GroupShow(bpy.types.Operator):
	bl_idname = "pose.group_show"
	bl_label = "このボーングループのボーンのみ表示"
	bl_description = "アクティブなボーングループのみを表示し、その他のボーンを隠します"
	bl_options = {'REGISTER', 'UNDO'}
	
	reverse = bpy.props.BoolProperty(name="反転", default=False)
	
	@classmethod
	def poll(cls, context):
		if (context.active_object):
			if (context.active_object.type == 'ARMATURE'):
				if (len(context.active_object.pose.bone_groups)):
					return True
		return False
	
	def execute(self, context):
		obj = context.active_object
		arm = obj.data
		for pbone in obj.pose.bones:
			bone = arm.bones[pbone.name]
			for i in range(len(arm.layers)):
				if (arm.layers[i] and bone.layers[i]):
					if (not pbone.bone_group):
						if (not self.reverse):
							bone.hide = True
						else:
							bone.hide = False
						break
					if (obj.pose.bone_groups.active.name == pbone.bone_group.name):
						if (not self.reverse):
							bone.hide = False
						else:
							bone.hide = True
					else:
						if (not self.reverse):
							bone.hide = True
						else:
							bone.hide = False
					break
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
		split = self.layout.split(percentage=0.5)
		split.row()
		row = split.row(align=True)
		row.operator(GroupShow.bl_idname, icon='RESTRICT_VIEW_OFF', text="表示").reverse = False
		row.operator(GroupShow.bl_idname, icon='RESTRICT_VIEW_ON', text="隠す").reverse = True
	if (context.user_preferences.addons["Scramble Addon"].preferences.use_disabled_menu):
		self.layout.operator('wm.toggle_menu_enable', icon='CANCEL').id = __name__.split('.')[-1]
