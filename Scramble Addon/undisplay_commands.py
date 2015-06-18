# メニューに表示されないコマンド

import bpy

################
# オペレーター #
################

class ScrollEnd(bpy.types.Operator):
	bl_idname = "view2d.scroll_end"
	bl_label = "最後までスクロール"
	bl_description = "画面の一番下までスクロールします"
	bl_options = {'REGISTER'}
	
	def execute(self, context):
		for i in range(20):
			bpy.ops.view2d.scroll_down(page=True)
		bpy.ops.view2d.scroll_down(page=False)
		return {'FINISHED'}
