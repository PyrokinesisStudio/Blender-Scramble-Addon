# UV/画像エディター > 「画像」メニュー

import bpy

################
# オペレーター #
################

class AllRenameImageFileName(bpy.types.Operator):
	bl_idname = "image.all_rename_image_file_name"
	bl_label = "全ての画像名を使用するファイル名に"
	bl_description = "全ての画像の名前を、使用している外部画像のファイル名にします"
	bl_options = {'REGISTER', 'UNDO'}
	
	isExt = bpy.props.BoolProperty(name="拡張子も含む", default=True)
	
	def execute(self, context):
		for img in  bpy.data.images:
			name = img.filepath_raw[2:].split("\\")[-1]
			if (not self.isExt):
				name, ext = os.path.splitext(name)
			try:
				img.name = name
			except: pass
		return {'FINISHED'}

class ReloadAllImage(bpy.types.Operator):
	bl_idname = "image.reload_all_image"
	bl_label = "全ての画像を再読み込み"
	bl_description = "外部ファイルを参照している画像データを全て読み込み直します"
	bl_options = {'REGISTER', 'UNDO'}
	
	def execute(self, context):
		for img in bpy.data.images:
			if (img.filepath != ""):
				img.reload()
				try:
					img.update()
				except RuntimeError:
					pass
		return {'FINISHED'}

################
# メニュー追加 #
################

# メニューを登録する関数
def menu(self, context):
	self.layout.separator()
	self.layout.operator(AllRenameImageFileName.bl_idname, icon="PLUGIN")
	self.layout.operator(ReloadAllImage.bl_idname, icon="PLUGIN")
