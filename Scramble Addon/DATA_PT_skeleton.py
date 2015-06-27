# 「プロパティ」エリア > 「アーマチュアデータ」タブ > 「スケルトン」パネル

import bpy

################
# オペレーター #
################

class ShowAllBoneLayers(bpy.types.Operator):
	bl_idname = "armature.show_all_bone_layers"
	bl_label = "全ボーンレイヤーを表示"
	bl_description = "全てのボーンレイヤーをオンにして表示します"
	bl_options = {'REGISTER'}
	
	layers = [False] * 32
	layers[0] = True
	pre_layers = bpy.props.BoolVectorProperty(name="直前のレイヤー情報", size=32, default=layers[:])
	
	@classmethod
	def poll(cls, context):
		if (context.object):
			if (context.object.type == 'ARMATURE'):
				return True
		return False
	
	def execute(self, context):
		if (all(context.object.data.layers)):
			context.object.data.layers = self.pre_layers[:]
		else:
			self.pre_layers = context.object.data.layers[:]
			for i in range(len(context.object.data.layers)):
				context.object.data.layers[i] = True
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
		col = self.layout.column(align=True)
		col.operator('pose.toggle_pose_position', icon='PLUGIN')
		col.operator(ShowAllBoneLayers.bl_idname, icon='PLUGIN')
	if (context.user_preferences.addons["Scramble Addon"].preferences.use_disabled_menu):
		self.layout.operator('wm.toggle_menu_enable', icon='CANCEL').id = __name__.split('.')[-1]
