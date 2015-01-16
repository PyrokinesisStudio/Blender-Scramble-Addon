import bpy
import os.path

##############
# その他関数 #
##############

##############################
# オペレーター(オブジェクト) #
##############################

class AllOnShowAllEdges(bpy.types.Operator):
	bl_idname = "object.all_on_show_all_edges"
	bl_label = "全ての「すべての辺を表示」をオン"
	bl_description = "全てのオブジェクトの「すべての辺を表示」表示設定をオンにします(オフも可能)"
	bl_options = {'REGISTER', 'UNDO'}
	
	isOn = bpy.props.BoolProperty(name="オンにする", default=True)
	
	def execute(self, context):
		for obj in bpy.data.objects:
			obj.show_all_edges = self.isOn
		return {'FINISHED'}

class AllSetDrawType(bpy.types.Operator):
	bl_idname = "object.all_set_draw_type"
	bl_label = "全ての最高描画タイプを一括設定"
	bl_description = "全てのオブジェクトの「最高描画タイプ」を一括で設定します"
	bl_options = {'REGISTER', 'UNDO'}
	
	items = [
		("MESH", "メッシュ", "", 1),
		("CURVE", "カーブ", "", 2),
		("SURFACE", "サーフェイス", "", 3),
		("META", "メタボール", "", 4),
		("FONT", "テキスト", "", 5),
		("ARMATURE", "アーマチュア", "", 6),
		("LATTICE", "ラティス", "", 7),
		("EMPTY", "エンプティ", "", 8),
		("CAMERA", "カメラ", "", 9),
		("LAMP", "ランプ", "", 10),
		("SPEAKER", "スピーカー", "", 11),
		("ALL", "全てのオブジェクト", "", 12),
		]
	objType = bpy.props.EnumProperty(items=items, name="オブジェクトのタイプ")
	items = [
		("TEXTURED", "テクスチャ", "", 1),
		("SOLID", "ソリッド", "", 2),
		("WIRE", "ワイヤー", "", 3),
		("BOUNDS", "バウンド", "", 4),
		]
	type = bpy.props.EnumProperty(items=items, name="描画タイプ")
	
	def execute(self, context):
		for obj in bpy.data.objects:
			if (self.objType == obj.type or self.objType == "ALL"):
				obj.draw_type = self.type
		return {'FINISHED'}

class AllRenameObjectData(bpy.types.Operator):
	bl_idname = "object.all_rename_object_data"
	bl_label = "全てのデータ名をオブジェクト名と同じにする"
	bl_description = "全てのオブジェクトのデータ(メッシュデータなど)の名前を、リンクしているオブジェクト名に置換します"
	bl_options = {'REGISTER', 'UNDO'}
	
	isSelected = bpy.props.BoolProperty(name="選択中のオブジェクトのみ", default=False)
	
	def execute(self, context):
		if (self.isSelected):
			objs = context.selected_objects
		else:
			objs = bpy.data.objects
		for obj in objs:
			if (obj and obj.data):
				obj.data.name = obj.name
		return {'FINISHED'}

############################
# オペレーター(マテリアル) #
############################

class AllSetMaterialReceiveTransparent(bpy.types.Operator):
	bl_idname = "material.all_set_material_receive_transparent"
	bl_label = "全てのマテリアルの「半透明影の受信」をオン"
	bl_description = "全てのマテリアルの「半透明影を受信するかどうか」についての設定をオン(オフ)にします"
	bl_options = {'REGISTER', 'UNDO'}
	
	isOff = bpy.props.BoolProperty(name="オフにする", default=False)
	
	def execute(self, context):
		for mat in bpy.data.materials:
			mat.use_transparent_shadows = not self.isOff
		return {'FINISHED'}

class AllSetMaterialColorRamp(bpy.types.Operator):
	bl_idname = "material.all_set_material_color_ramp"
	bl_label = "アクティブマテリアルのカラーランプ設定を他にコピー"
	bl_description = "アクティブなマテリアルのカラーランプ設定を他の全マテリアル(選択オブジェクトのみも可)にコピーします"
	bl_options = {'REGISTER', 'UNDO'}
	
	isOnlySelected = bpy.props.BoolProperty(name="選択オブジェクトのマテリアルのみ", default=False)
	
	def execute(self, context):
		activeMat = context.active_object.active_material
		if (not activeMat):
			self.report(type={"ERROR"}, message="アクティブマテリアルがありません")
			return {"CANCELLED"}
		mats = []
		if (self.isOnlySelected):
			for obj in context.selected_objects:
				for mslot in obj.material_slots:
					if (mslot.material):
						mats.append(mslot.material)
		else:
			mats = bpy.data.materials
		for mat in mats:
			if (mat.name != activeMat.name):
				mat.use_diffuse_ramp = activeMat.use_diffuse_ramp
				mat.diffuse_ramp.color_mode = activeMat.diffuse_ramp.color_mode
				mat.diffuse_ramp.hue_interpolation = activeMat.diffuse_ramp.hue_interpolation
				mat.diffuse_ramp.interpolation = activeMat.diffuse_ramp.interpolation
				#mat.diffuse_ramp.evaluate = activeMat.diffuse_ramp.evaluate
				for i in range(len(activeMat.diffuse_ramp.elements)):
					if (len(mat.diffuse_ramp.elements) < i+1):
						color = mat.diffuse_ramp.elements.new(color.position)
					else:
						color = mat.diffuse_ramp.elements[i]
					color.position = activeMat.diffuse_ramp.elements[i].position
					color.alpha = activeMat.diffuse_ramp.elements[i].alpha
					color.color = activeMat.diffuse_ramp.elements[i].color
				mat.diffuse_ramp_input = activeMat.diffuse_ramp_input
				mat.diffuse_ramp_blend = activeMat.diffuse_ramp_blend
				mat.diffuse_ramp_factor = activeMat.diffuse_ramp_factor
		return {'FINISHED'}

############################
# オペレーター(テクスチャ) #
############################

class AllSetBumpMethod(bpy.types.Operator):
	bl_idname = "texture.all_set_bump_method"
	bl_label = "全てのバンプマップの品質を設定"
	bl_description = "全てのテクスチャのバンプマップの品質を一括で設定します"
	bl_options = {'REGISTER', 'UNDO'}
	
	items = [
		("BUMP_ORIGINAL", "オリジナル", "", 1),
		("BUMP_COMPATIBLE", "互換性", "", 2),
		("BUMP_LOW_QUALITY", "低品質", "", 3),
		("BUMP_MEDIUM_QUALITY", "中品質", "", 4),
		("BUMP_BEST_QUALITY", "最高品質", "", 5),
		]
	method = bpy.props.EnumProperty(items=items, name="バンプ品質", default="BUMP_BEST_QUALITY")
	
	def execute(self, context):
		for mat in  bpy.data.materials:
			for slot in mat.texture_slots:
				try:
					slot.bump_method = self.method
				except AttributeError: pass
		return {'FINISHED'}

class AllRenameTextureFileName(bpy.types.Operator):
	bl_idname = "texture.all_rename_texture_file_name"
	bl_label = "全てのテクスチャ名を使用する画像ファイル名に"
	bl_description = "全てのテクスチャの名前を、使用している外部画像のファイル名にします"
	bl_options = {'REGISTER', 'UNDO'}
	
	isExt = bpy.props.BoolProperty(name="拡張子も含む", default=True)
	
	def execute(self, context):
		for tex in  bpy.data.textures:
			if (tex.type == "IMAGE"):
				name = tex.image.filepath_raw[2:].split("\\")[-1]
				if (not self.isExt):
					name, ext = os.path.splitext(name)
				try:
					tex.name = name
				except: pass
		return {'FINISHED'}

class FixEmptyTextureUVLayer(bpy.types.Operator):
	bl_idname = "texture.fix_empty_texture_uv_layer"
	bl_label = "UV指定が空欄な場合アクティブUVで埋める"
	bl_description = "テクスチャのUV指定欄が空欄の場合、リンクしているメッシュオブジェクトのアクティブなUV名で埋めます"
	bl_options = {'REGISTER', 'UNDO'}
	
	isSelectedOnly = bpy.props.BoolProperty(name="選択オブジェクトのみ", default=False)
	
	def execute(self, context):
		objs = bpy.data.objects
		if (self.isSelectedOnly):
			objs = context.selected_objects
		for obj in objs:
			if (obj.type == "MESH"):
				me = obj.data
				if (len(me.uv_layers) > 0):
					uv = me.uv_layers.active
				for mslot in obj.material_slots:
					mat = mslot.material
					if (mat):
						for tslot in mat.texture_slots:
							if (tslot != None):
								if (tslot.texture_coords == "UV"):
									if(tslot.uv_layer == ""):
										tslot.uv_layer = uv.name
		return {'FINISHED'}

######################
# オペレーター(画像) #
######################

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

##########################
# サブメニュー(Modifier) #
##########################

class EntireProcessMenu(bpy.types.Menu):
	bl_idname = "INFO_MT_entire_process"
	bl_label = "全体処理(使用には注意を)"
	bl_description = "全データを一括処理する機能群です"
	
	def draw(self, context):
		self.layout.menu(EntireProcessObjectMenu.bl_idname, icon="PLUGIN")
		self.layout.menu(EntireProcessMaterialMenu.bl_idname, icon="PLUGIN")
		self.layout.menu(EntireProcessTextureMenu.bl_idname, icon="PLUGIN")
		self.layout.menu(EntireProcessImageMenu.bl_idname, icon="PLUGIN")

class EntireProcessObjectMenu(bpy.types.Menu):
	bl_idname = "INFO_MT_entire_process_object"
	bl_label = "オブジェクト"
	bl_description = "全オブジェクトを一括処理する機能群です"
	
	def draw(self, context):
		self.layout.operator(AllOnShowAllEdges.bl_idname, icon="PLUGIN")
		self.layout.operator(AllSetDrawType.bl_idname, icon="PLUGIN")
		self.layout.operator(AllRenameObjectData.bl_idname, icon="PLUGIN")

class EntireProcessMaterialMenu(bpy.types.Menu):
	bl_idname = "INFO_MT_entire_process_material"
	bl_label = "マテリアル"
	bl_description = "全マテリアルを一括処理する機能群です"
	
	def draw(self, context):
		self.layout.operator(AllSetMaterialReceiveTransparent.bl_idname, icon="PLUGIN")
		self.layout.operator(AllSetMaterialColorRamp.bl_idname, icon="PLUGIN")

class EntireProcessTextureMenu(bpy.types.Menu):
	bl_idname = "INFO_MT_entire_process_texture"
	bl_label = "テクスチャ"
	bl_description = "全テクスチャを一括処理する機能群です"
	
	def draw(self, context):
		self.layout.operator(AllRenameTextureFileName.bl_idname, icon="PLUGIN")
		self.layout.operator(AllSetBumpMethod.bl_idname, icon="PLUGIN")
		self.layout.operator(FixEmptyTextureUVLayer.bl_idname, icon="PLUGIN")

class EntireProcessImageMenu(bpy.types.Menu):
	bl_idname = "INFO_MT_entire_process_image"
	bl_label = "画像"
	bl_description = "全画像を一括処理する機能群です"
	
	def draw(self, context):
		self.layout.operator(AllRenameImageFileName.bl_idname, icon="PLUGIN")

################
# メニュー追加 #
################

# メニューを登録する関数
def menu(self, context):
	self.layout.separator()
	self.layout.separator()
	self.layout.separator()
	self.layout.menu(EntireProcessMenu.bl_idname, icon="PLUGIN")