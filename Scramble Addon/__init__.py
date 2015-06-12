# アドオンを読み込む時に最初にこのファイルが読み込まれます

import os, csv, codecs

# アドオン情報
bl_info = {
	"name" : "Scramble Addon",
	"author" : "さいでんか(saidenka)",
	"version" : (0,1),
	"blender" : (2, 7),
	"location" : "様々なメニューの末尾",
	"description" : "さいでんか制作の拡張機能群の詰め合わせ",
	"warning" : "",
	"wiki_url" : "http://github.com/saidenka/Blender-Scramble-Addon",
	"tracker_url" : "http://github.com/saidenka/Blender-Scramble-Addon/issues",
	"category" : "3D View"
}

# サブスクリプト群をインポート
if "bpy" in locals():
	import imp
	imp.reload(IMAGE_MT_image)
	imp.reload(IMAGE_MT_select)
	imp.reload(IMAGE_MT_view)
	imp.reload(INFO_MT_file)
	imp.reload(INFO_MT_file_external_data)
	imp.reload(INFO_MT_mesh_add)
	imp.reload(INFO_MT_render)
	imp.reload(INFO_MT_window)
	imp.reload(MATERIAL_MT_specials)
	imp.reload(MESH_MT_shape_key_specials)
	imp.reload(MESH_MT_vertex_group_specials)
	imp.reload(NODE_MT_node)
	imp.reload(TEXTURE_MT_specials)
	imp.reload(VIEW3D_MT_armature_specials)
	imp.reload(VIEW3D_MT_bone_options_toggle)
	imp.reload(VIEW3D_MT_edit_armature)
	imp.reload(VIEW3D_MT_edit_mesh)
	imp.reload(VIEW3D_MT_edit_mesh_delete)
	imp.reload(VIEW3D_MT_edit_mesh_showhide)
	imp.reload(VIEW3D_MT_edit_mesh_specials)
	imp.reload(VIEW3D_MT_make_links)
	imp.reload(VIEW3D_MT_object)
	imp.reload(VIEW3D_MT_object_showhide)
	imp.reload(VIEW3D_MT_object_specials)
	imp.reload(VIEW3D_MT_paint_weight)
	imp.reload(VIEW3D_MT_pose_constraints)
	imp.reload(VIEW3D_MT_pose_showhide)
	imp.reload(VIEW3D_MT_pose_specials)
	imp.reload(VIEW3D_MT_select_edit_mesh)
	imp.reload(VIEW3D_MT_select_pose)
	imp.reload(VIEW3D_MT_view)
	imp.reload(VIEW3D_MT_view_align)
	imp.reload(VIEW3D_MT_select_edit_armature)
	imp.reload(VIEW3D_MT_edit_mesh_vertices)
	imp.reload(INFO_MT_help)
	imp.reload(DOPESHEET_MT_key)
	imp.reload(VIEW3D_MT_select_object)
	imp.reload(VIEW3D_MT_object_apply)
	imp.reload(VIEW3D_MT_view_align_selected)
	imp.reload(VIEW3D_MT_snap)
	imp.reload(VIEW3D_MT_uv_map)
	imp.reload(USERPREF_HT_header)
	imp.reload(PROPERTIES_HT_header)
	imp.reload(DATA_PT_modifiers)
	imp.reload(DATA_PT_uv_texture)
	imp.reload(DATA_PT_vertex_colors)
	imp.reload(USERPREF_PT_file)
else:
	from . import IMAGE_MT_image
	from . import IMAGE_MT_select
	from . import IMAGE_MT_view
	from . import INFO_MT_file
	from . import INFO_MT_file_external_data
	from . import INFO_MT_mesh_add
	from . import INFO_MT_render
	from . import INFO_MT_window
	from . import MATERIAL_MT_specials
	from . import MESH_MT_shape_key_specials
	from . import MESH_MT_vertex_group_specials
	from . import NODE_MT_node
	from . import TEXTURE_MT_specials
	from . import VIEW3D_MT_armature_specials
	from . import VIEW3D_MT_bone_options_toggle
	from . import VIEW3D_MT_edit_armature
	from . import VIEW3D_MT_edit_mesh
	from . import VIEW3D_MT_edit_mesh_delete
	from . import VIEW3D_MT_edit_mesh_showhide
	from . import VIEW3D_MT_edit_mesh_specials
	from . import VIEW3D_MT_make_links
	from . import VIEW3D_MT_object
	from . import VIEW3D_MT_object_showhide
	from . import VIEW3D_MT_object_specials
	from . import VIEW3D_MT_paint_weight
	from . import VIEW3D_MT_pose_constraints
	from . import VIEW3D_MT_pose_showhide
	from . import VIEW3D_MT_pose_specials
	from . import VIEW3D_MT_select_edit_mesh
	from . import VIEW3D_MT_select_pose
	from . import VIEW3D_MT_view
	from . import VIEW3D_MT_view_align
	from . import VIEW3D_MT_select_edit_armature
	from . import VIEW3D_MT_edit_mesh_vertices
	from . import INFO_MT_help
	from . import DOPESHEET_MT_key
	from . import VIEW3D_MT_select_object
	from . import VIEW3D_MT_object_apply
	from . import VIEW3D_MT_view_align_selected
	from . import VIEW3D_MT_snap
	from . import VIEW3D_MT_uv_map
	from . import USERPREF_HT_header
	from . import PROPERTIES_HT_header
	from . import DATA_PT_modifiers
	from . import DATA_PT_uv_texture
	from . import DATA_PT_vertex_colors
	from . import USERPREF_PT_file
import bpy

# アドオン設定
class AddonPreferences(bpy.types.AddonPreferences):
	bl_idname = __name__
	
	disabled_menu = bpy.props.StringProperty(name="無効なメニュー", default="")
	use_disabled_menu = bpy.props.BoolProperty(name="「追加項目のオン/オフ」の非表示", default=False)
	view_savedata = bpy.props.StringProperty(name="視点のセーブデータ", default="")
	key_config_xml_path = bpy.props.StringProperty(name="XMLキーコンフィグのパス", default="BlenderKeyConfig.xml")
	image_editor_path_1 = bpy.props.StringProperty(name="画像編集ソフトのパス 1", default="", subtype='FILE_PATH')
	image_editor_path_2 = bpy.props.StringProperty(name="画像編集ソフトのパス 2", default="", subtype='FILE_PATH')
	image_editor_path_3 = bpy.props.StringProperty(name="画像編集ソフトのパス 3", default="", subtype='FILE_PATH')
	
	def draw(self, context):
		layout = self.layout
		layout.prop(self, 'disabled_menu')
		layout.prop(self, 'use_disabled_menu')
		layout.prop(self, 'view_savedata')
		layout.prop(self, 'key_config_xml_path')
		box = layout.box()
		box.prop(self, 'image_editor_path_1')
		box.prop(self, 'image_editor_path_2')
		box.prop(self, 'image_editor_path_3')

# 追加メニューの有効/無効
class ToggleMenuEnable(bpy.types.Operator):
	bl_idname = "wm.toggle_menu_enable"
	bl_label = "追加項目のオン/オフ"
	bl_description = "ScrambleAddonによる追加メニューを有効/無効に切り替えます"
	bl_options = {'REGISTER', 'UNDO'}
	
	id = bpy.props.StringProperty()
	
	def execute(self, context):
		recovery = ""
		is_on = False
		for id in context.user_preferences.addons["Scramble Addon"].preferences.disabled_menu.split(','):
			if (id == ""):
				continue
			if (id == self.id):
				is_on = True
			else:
				recovery = recovery + id + ","
		if (not is_on):
			recovery = recovery + self.id + ","
		if (recovery != ""):
			if (recovery[-1] == ","):
				recovery = recovery[:-1]
		context.user_preferences.addons["Scramble Addon"].preferences.disabled_menu = recovery
		return {'FINISHED'}

# 翻訳辞書の取得
def GetTranslationDict():
	dict = {'en':{}}
	path = os.path.join(os.path.dirname(__file__), "TranslationDictionary.csv")
	with codecs.open(path, 'r', 'utf-8') as f:
		reader = csv.reader(f)
		for row in reader:
			#for context in bpy.app.translations.contexts:
			dict['en'][(bpy.app.translations.contexts.default, row[0])] = row[1]
			dict['en'][(bpy.app.translations.contexts.operator_default, row[0])] = row[1]
	return dict

# プラグインをインストールしたときの処理
def register():
	bpy.utils.register_module(__name__)
	
	translation_dict = GetTranslationDict()
	bpy.app.translations.register(__name__, translation_dict)
	
	bpy.types.IMAGE_MT_image.append(IMAGE_MT_image.menu)
	bpy.types.IMAGE_MT_select.append(IMAGE_MT_select.menu)
	bpy.types.IMAGE_MT_view.append(IMAGE_MT_view.menu)
	bpy.types.INFO_MT_file.append(INFO_MT_file.menu)
	bpy.types.INFO_MT_file_external_data.append(INFO_MT_file_external_data.menu)
	bpy.types.INFO_MT_mesh_add.append(INFO_MT_mesh_add.menu)
	bpy.types.INFO_MT_render.append(INFO_MT_render.menu)
	bpy.types.INFO_MT_window.append(INFO_MT_window.menu)
	bpy.types.MATERIAL_MT_specials.append(MATERIAL_MT_specials.menu)
	bpy.types.MESH_MT_shape_key_specials.append(MESH_MT_shape_key_specials.menu)
	bpy.types.MESH_MT_vertex_group_specials.append(MESH_MT_vertex_group_specials.menu)
	bpy.types.NODE_MT_node.append(NODE_MT_node.menu)
	bpy.types.TEXTURE_MT_specials.append(TEXTURE_MT_specials.menu)
	bpy.types.VIEW3D_MT_armature_specials.append(VIEW3D_MT_armature_specials.menu)
	bpy.types.VIEW3D_MT_bone_options_toggle.append(VIEW3D_MT_bone_options_toggle.menu)
	bpy.types.VIEW3D_MT_edit_armature.append(VIEW3D_MT_edit_armature.menu)
	bpy.types.VIEW3D_MT_edit_mesh.append(VIEW3D_MT_edit_mesh.menu)
	bpy.types.VIEW3D_MT_edit_mesh_delete.append(VIEW3D_MT_edit_mesh_delete.menu)
	bpy.types.VIEW3D_MT_edit_mesh_showhide.append(VIEW3D_MT_edit_mesh_showhide.menu)
	bpy.types.VIEW3D_MT_edit_mesh_specials.append(VIEW3D_MT_edit_mesh_specials.menu)
	bpy.types.VIEW3D_MT_make_links.append(VIEW3D_MT_make_links.menu)
	bpy.types.VIEW3D_MT_object.append(VIEW3D_MT_object.menu)
	bpy.types.VIEW3D_MT_object_showhide.append(VIEW3D_MT_object_showhide.menu)
	bpy.types.VIEW3D_MT_object_specials.append(VIEW3D_MT_object_specials.menu)
	bpy.types.VIEW3D_MT_paint_weight.append(VIEW3D_MT_paint_weight.menu)
	bpy.types.VIEW3D_MT_pose_constraints.append(VIEW3D_MT_pose_constraints.menu)
	bpy.types.VIEW3D_MT_pose_showhide.append(VIEW3D_MT_pose_showhide.menu)
	bpy.types.VIEW3D_MT_pose_specials.append(VIEW3D_MT_pose_specials.menu)
	bpy.types.VIEW3D_MT_select_edit_mesh.append(VIEW3D_MT_select_edit_mesh.menu)
	bpy.types.VIEW3D_MT_select_pose.append(VIEW3D_MT_select_pose.menu)
	bpy.types.VIEW3D_MT_view.append(VIEW3D_MT_view.menu)
	bpy.types.VIEW3D_MT_view_align.append(VIEW3D_MT_view_align.menu)
	bpy.types.VIEW3D_MT_select_edit_armature.append(VIEW3D_MT_select_edit_armature.menu)
	bpy.types.VIEW3D_MT_edit_mesh_vertices.append(VIEW3D_MT_edit_mesh_vertices.menu)
	bpy.types.INFO_MT_help.append(INFO_MT_help.menu)
	bpy.types.DOPESHEET_MT_key.append(DOPESHEET_MT_key.menu)
	bpy.types.VIEW3D_MT_select_object.append(VIEW3D_MT_select_object.menu)
	bpy.types.VIEW3D_MT_object_apply.append(VIEW3D_MT_object_apply.menu)
	bpy.types.VIEW3D_MT_view_align_selected.append(VIEW3D_MT_view_align_selected.menu)
	bpy.types.VIEW3D_MT_snap.append(VIEW3D_MT_snap.menu)
	bpy.types.VIEW3D_MT_uv_map.append(VIEW3D_MT_uv_map.menu)
	bpy.types.USERPREF_HT_header.append(USERPREF_HT_header.menu)
	bpy.types.PROPERTIES_HT_header.append(PROPERTIES_HT_header.menu)
	bpy.types.DATA_PT_modifiers.append(DATA_PT_modifiers.menu)
	bpy.types.DATA_PT_uv_texture.append(DATA_PT_uv_texture.menu)
	bpy.types.DATA_PT_vertex_colors.append(DATA_PT_vertex_colors.menu)
	bpy.types.USERPREF_PT_file.append(USERPREF_PT_file.menu)

# プラグインをアンインストールしたときの処理
def unregister():
	bpy.utils.unregister_module(__name__)
	
	bpy.app.translations.unregister(__name__)
	
	bpy.types.IMAGE_MT_image.remove(IMAGE_MT_image.menu)
	bpy.types.IMAGE_MT_select.remove(IMAGE_MT_select.menu)
	bpy.types.IMAGE_MT_view.remove(IMAGE_MT_view.menu)
	bpy.types.INFO_MT_file.remove(INFO_MT_file.menu)
	bpy.types.INFO_MT_file_external_data.remove(INFO_MT_file_external_data.menu)
	bpy.types.INFO_MT_mesh_add.remove(INFO_MT_mesh_add.menu)
	bpy.types.INFO_MT_render.remove(INFO_MT_render.menu)
	bpy.types.INFO_MT_window.remove(INFO_MT_window.menu)
	bpy.types.MATERIAL_MT_specials.remove(MATERIAL_MT_specials.menu)
	bpy.types.MESH_MT_shape_key_specials.remove(MESH_MT_shape_key_specials.menu)
	bpy.types.MESH_MT_vertex_group_specials.remove(MESH_MT_vertex_group_specials.menu)
	bpy.types.NODE_MT_node.remove(NODE_MT_node.menu)
	bpy.types.TEXTURE_MT_specials.remove(TEXTURE_MT_specials.menu)
	bpy.types.VIEW3D_MT_armature_specials.remove(VIEW3D_MT_armature_specials.menu)
	bpy.types.VIEW3D_MT_bone_options_toggle.remove(VIEW3D_MT_bone_options_toggle.menu)
	bpy.types.VIEW3D_MT_edit_armature.remove(VIEW3D_MT_edit_armature.menu)
	bpy.types.VIEW3D_MT_edit_mesh.remove(VIEW3D_MT_edit_mesh.menu)
	bpy.types.VIEW3D_MT_edit_mesh_delete.remove(VIEW3D_MT_edit_mesh_delete.menu)
	bpy.types.VIEW3D_MT_edit_mesh_showhide.remove(VIEW3D_MT_edit_mesh_showhide.menu)
	bpy.types.VIEW3D_MT_edit_mesh_specials.remove(VIEW3D_MT_edit_mesh_specials.menu)
	bpy.types.VIEW3D_MT_make_links.remove(VIEW3D_MT_make_links.menu)
	bpy.types.VIEW3D_MT_object.remove(VIEW3D_MT_object.menu)
	bpy.types.VIEW3D_MT_object_showhide.remove(VIEW3D_MT_object_showhide.menu)
	bpy.types.VIEW3D_MT_object_specials.remove(VIEW3D_MT_object_specials.menu)
	bpy.types.VIEW3D_MT_paint_weight.remove(VIEW3D_MT_paint_weight.menu)
	bpy.types.VIEW3D_MT_pose_constraints.remove(VIEW3D_MT_pose_constraints.menu)
	bpy.types.VIEW3D_MT_pose_showhide.remove(VIEW3D_MT_pose_showhide.menu)
	bpy.types.VIEW3D_MT_pose_specials.remove(VIEW3D_MT_pose_specials.menu)
	bpy.types.VIEW3D_MT_select_edit_mesh.remove(VIEW3D_MT_select_edit_mesh.menu)
	bpy.types.VIEW3D_MT_select_pose.remove(VIEW3D_MT_select_pose.menu)
	bpy.types.VIEW3D_MT_view.remove(VIEW3D_MT_view.menu)
	bpy.types.VIEW3D_MT_view_align.remove(VIEW3D_MT_view_align.menu)
	bpy.types.VIEW3D_MT_select_edit_armature.remove(VIEW3D_MT_select_edit_armature.menu)
	bpy.types.VIEW3D_MT_edit_mesh_vertices.remove(VIEW3D_MT_edit_mesh_vertices.menu)
	bpy.types.INFO_MT_help.remove(INFO_MT_help.menu)
	bpy.types.DOPESHEET_MT_key.remove(DOPESHEET_MT_key.menu)
	bpy.types.VIEW3D_MT_select_object.remove(VIEW3D_MT_select_object.menu)
	bpy.types.VIEW3D_MT_object_apply.remove(VIEW3D_MT_object_apply.menu)
	bpy.types.VIEW3D_MT_view_align_selected.remove(VIEW3D_MT_view_align_selected.menu)
	bpy.types.VIEW3D_MT_snap.remove(VIEW3D_MT_snap.menu)
	bpy.types.VIEW3D_MT_uv_map.remove(VIEW3D_MT_uv_map.menu)
	bpy.types.USERPREF_HT_header.remove(USERPREF_HT_header.menu)
	bpy.types.PROPERTIES_HT_header.remove(PROPERTIES_HT_header.menu)
	bpy.types.DATA_PT_modifiers.remove(DATA_PT_modifiers.menu)
	bpy.types.DATA_PT_uv_texture.remove(DATA_PT_uv_texture.menu)
	bpy.types.DATA_PT_vertex_colors.remove(DATA_PT_vertex_colors.menu)
	bpy.types.USERPREF_PT_file.remove(USERPREF_PT_file.menu)

# メイン関数
if __name__ == "__main__":
	register()
