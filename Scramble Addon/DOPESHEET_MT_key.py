# ドープシート > 「キー」メニュー

import bpy

################
# オペレーター #
################

class DeleteUnmessage(bpy.types.Operator):
	bl_idname = "action.delete_unmessage"
	bl_label = "キーフレームを削除 (確認しない)"
	bl_description = "選択した全てのキーフレームを確認せずに削除します"
	bl_options = {'REGISTER', 'UNDO'}
	
	def execute(self, context):
		bpy.ops.action.delete()
		return {'FINISHED'}

################
# メニュー追加 #
################

# メニューを登録する関数
def menu(self, context):
	self.layout.separator()
	self.layout.operator(DeleteUnmessage.bl_idname, icon="PLUGIN")
