# 3Dビュー > オブジェクトモード > Ctrl+Aキー

import bpy

################
# オペレーター #
################

class TransformApplyAll(bpy.types.Operator):
	bl_idname = "object.transform_apply_all"
	bl_label = "位置/回転/拡縮を適用"
	bl_description = "オブジェクトの位置/回転/拡縮を適用します"
	bl_options = {'REGISTER', 'UNDO'}
	
	def execute(self, context):
		bpy.ops.object.transform_apply(location=True, rotation=False, scale=False)
		bpy.ops.object.transform_apply(location=False, rotation=True, scale=True)
		return {'FINISHED'}

################
# メニュー追加 #
################

# メニューを登録する関数
def menu(self, context):
	self.layout.separator()
	operator = self.layout.operator(TransformApplyAll.bl_idname, text="位置と回転と拡縮", icon="PLUGIN")
