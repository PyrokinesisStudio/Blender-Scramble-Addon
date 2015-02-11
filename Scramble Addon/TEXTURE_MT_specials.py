# プロパティ > 「テクスチャ」タブ > リスト右の▼

import bpy

################
# オペレーター #
################

class RenameTextureFileName(bpy.types.Operator):
	bl_idname = "texture.rename_texture_file_name"
	bl_label = "テクスチャ名を使用する画像ファイル名に"
	bl_description = "アクティブなテクスチャの名前を使用している外部画像のファイル名にします"
	bl_options = {'REGISTER', 'UNDO'}
	
	isExt = bpy.props.BoolProperty(name="拡張子も含む", default=True)
	
	def execute(self, context):
		tex = context.active_object.active_material.active_texture
		if (not tex):
			self.report(type={"ERROR"}, message="画像/動画テクスチャで実行してください")
			return {"CANCELLED"}
		if (tex.type == "IMAGE"):
			if (not tex.image):
				self.report(type={"ERROR"}, message="画像が指定されていません")
				return {"CANCELLED"}
			name = tex.image.filepath_raw[2:].split("\\")[-1]
			if (not self.isExt):
				name, ext = os.path.splitext(name)
			try:
				tex.name = name
			except: pass
		else:
			self.report(type={"ERROR"}, message="画像/動画テクスチャで実行してください")
			return {"CANCELLED"}
		return {'FINISHED'}

################
# メニュー追加 #
################

# メニューを登録する関数
def menu(self, context):
	self.layout.separator()
	self.layout.operator(RenameTextureFileName.bl_idname, icon="PLUGIN")
