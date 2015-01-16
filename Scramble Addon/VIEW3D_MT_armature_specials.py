import bpy
import re

################
# オペレーター #
################

class RenameBoneRegularExpression(bpy.types.Operator):
	bl_idname = "armature.rename_bone_regular_expression"
	bl_label = "ボーンを正規表現で置換"
	bl_description = "(選択中の)ボーンを正規表現に一致する部分で置換します"
	bl_options = {'REGISTER', 'UNDO'}
	
	isAll = bpy.props.BoolProperty(name="非選択も含め全て", default=False)
	pattern = bpy.props.StringProperty(name="置換前(正規表現)", default="^")
	repl = bpy.props.StringProperty(name="置換後", default="@")
	
	def execute(self, context):
		obj = context.active_object
		if (obj.type == "ARMATURE"):
			if (obj.mode == "EDIT"):
				bones = context.selected_bones
				if (self.isAll):
					bones = obj.data.bones
				for bone in bones:
					bone.name = re.sub(self.pattern, self.repl, bone.name)
			else:
				self.report(type={"ERROR"}, message="エディトモードで実行してください")
		else:
			self.report(type={"ERROR"}, message="アーマチュアオブジェクトではありません")
		return {'FINISHED'}

################
# メニュー追加 #
################

# メニューを登録する関数
def menu(self, context):
	self.layout.separator()
	self.layout.operator(RenameBoneRegularExpression.bl_idname, icon="PLUGIN")
