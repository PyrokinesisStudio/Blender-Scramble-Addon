# 3Dビュー > 「ビュー」メニュー > 「視点を揃える」メニュー > 「アクティブに視点を揃える」メニュー

import bpy

################
# オペレーター #
################

class Viewnumpad7AlignEX(bpy.types.Operator):
	bl_idname = "view3d.viewnumpad_7_align_ex"
	bl_label = "面を正面から見る"
	bl_description = "選択中の面の法線方向から面を注視します"
	bl_options = {'REGISTER', 'UNDO'}
	
	def execute(self, context):
		pre_smooth_view = context.user_preferences.view.smooth_view
		context.user_preferences.view.smooth_view = 0
		bpy.ops.view3d.viewnumpad(type='TOP', align_active=True)
		bpy.ops.view3d.view_selected_ex()
		threshold = 0.01
		angle = 0.001
		while True:
			bpy.ops.view3d.view_roll(angle=angle, type='ROLLANGLE')
			view_rotation = context.region_data.view_rotation.copy().to_euler()
			if (-threshold <= view_rotation.y <= threshold):
					break
		if (view_rotation.x < 0):
			bpy.ops.view3d.view_roll(angle=3.14159, type='ROLLANGLE')
		return {'FINISHED'}

################
# メニュー追加 #
################

# メニューを登録する関数
def menu(self, context):
	self.layout.separator()
	self.layout.operator(Viewnumpad7AlignEX.bl_idname, icon="PLUGIN")
