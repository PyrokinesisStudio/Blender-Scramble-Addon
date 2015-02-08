# 3Dビュー > メッシュ編集モード > 「メッシュ」メニュー > 「表示/隠す」メニュー

import bpy

################
# オペレーター #
################

class InvertHide(bpy.types.Operator):
	bl_idname = "mesh.invert_hide"
	bl_label = "表示/隠すを反転"
	bl_description = "表示状態と非表示状態を反転させます"
	bl_options = {'REGISTER', 'UNDO'}
	
	def execute(self, context):
		obj = context.active_object
		if (obj.type == "MESH"):
			bpy.ops.object.mode_set(mode="OBJECT")
			me = obj.data
			for v in me.vertices:
				v.hide = not v.hide
			for e in me.edges:
				for i in e.vertices:
					if (me.vertices[i].hide == True):
						e.hide = True
						break
				else:
					e.hide = False
			for f in me.polygons:
				for i in f.vertices:
					if (me.vertices[i].hide == True):
						f.hide = True
						break
				else:
					f.hide = False
			bpy.ops.object.mode_set(mode="EDIT")
		else:
			self.report(type={"ERROR"}, message="メッシュオブジェクトがアクティブな状態で実行してください")
		return {'FINISHED'}

################
# メニュー追加 #
################

# メニューを登録する関数
def menu(self, context):
	self.layout.separator()
	self.layout.operator(InvertHide.bl_idname, icon="PLUGIN")
