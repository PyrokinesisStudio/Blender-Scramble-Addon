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
	imp.reload(VIEW3D_PT_tools_imagepaint_external)
	imp.reload(TEXT_MT_text)
	imp.reload(IMAGE_MT_uvs)
	imp.reload(OBJECT_PT_display)
	imp.reload(RENDER_PT_render)
	imp.reload(MATERIAL_PT_context_material)
	imp.reload(VIEW3D_PT_view3d_properties)
	imp.reload(SCENE_PT_rigid_body_world)
	imp.reload(NODE_MT_view)
	imp.reload(VIEW3D_PT_view3d_name)
	imp.reload(OBJECT_PT_context_object)
	imp.reload(BONE_PT_context_bone)
	imp.reload(DATA_PT_skeleton)
	imp.reload(TEXTURE_PT_context_texture)
	imp.reload(undisplay_commands)
	imp.reload(TEXTURE_PT_image)
	imp.reload(RENDER_PT_bake)
	imp.reload(TEXTURE_PT_mapping)
	imp.reload(VIEW3D_PT_imapaint_tools_missing)
	imp.reload(VIEW3D_PT_slots_projectpaint)
	imp.reload(DATA_PT_geometry_curve)
	imp.reload(VIEW3D_PT_transform_orientations)
	imp.reload(VIEW3D_PT_layers)
	#imp.reload(***)
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
	from . import VIEW3D_PT_tools_imagepaint_external
	from . import TEXT_MT_text
	from . import IMAGE_MT_uvs
	from . import OBJECT_PT_display
	from . import RENDER_PT_render
	from . import MATERIAL_PT_context_material
	from . import VIEW3D_PT_view3d_properties
	from . import SCENE_PT_rigid_body_world
	from . import NODE_MT_view
	from . import VIEW3D_PT_view3d_name
	from . import OBJECT_PT_context_object
	from . import BONE_PT_context_bone
	from . import DATA_PT_skeleton
	from . import TEXTURE_PT_context_texture
	from . import undisplay_commands
	from . import TEXTURE_PT_image
	from . import RENDER_PT_bake
	from . import TEXTURE_PT_mapping
	from . import VIEW3D_PT_imapaint_tools_missing
	from . import VIEW3D_PT_slots_projectpaint
	from . import DATA_PT_geometry_curve
	from . import VIEW3D_PT_transform_orientations
	from . import VIEW3D_PT_layers
	#from . import ***
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
	
	text_editor_path_1 = bpy.props.StringProperty(name="テキスト編集ソフトのパス 1", default="", subtype='FILE_PATH')
	text_editor_path_2 = bpy.props.StringProperty(name="テキスト編集ソフトのパス 2", default="", subtype='FILE_PATH')
	text_editor_path_3 = bpy.props.StringProperty(name="テキスト編集ソフトのパス 3", default="", subtype='FILE_PATH')
	
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
		box = layout.box()
		box.prop(self, 'text_editor_path_1')
		box.prop(self, 'text_editor_path_2')
		box.prop(self, 'text_editor_path_3')

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
		for area in context.screen.areas:
			area.tag_redraw()
		return {'FINISHED'}

# 翻訳辞書の取得
def GetTranslationDict():
	dict = {'en':{}}
	path = os.path.join(os.path.dirname(__file__), "TranslationDictionary.csv")
	with codecs.open(path, 'r', 'utf-8') as f:
		reader = csv.reader(f)
		for row in reader:
			for context in bpy.app.translations.contexts:
				dict['en'][(context, row[0])] = row[1]
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
	bpy.types.VIEW3D_PT_tools_imagepaint_external.append(VIEW3D_PT_tools_imagepaint_external.menu)
	bpy.types.TEXT_MT_text.append(TEXT_MT_text.menu)
	bpy.types.IMAGE_MT_uvs.append(IMAGE_MT_uvs.menu)
	bpy.types.OBJECT_PT_display.append(OBJECT_PT_display.menu)
	bpy.types.RENDER_PT_render.append(RENDER_PT_render.menu)
	bpy.types.MATERIAL_PT_context_material.append(MATERIAL_PT_context_material.menu)
	bpy.types.VIEW3D_PT_view3d_properties.append(VIEW3D_PT_view3d_properties.menu)
	bpy.types.SCENE_PT_rigid_body_world.append(SCENE_PT_rigid_body_world.menu)
	bpy.types.NODE_MT_view.append(NODE_MT_view.menu)
	bpy.types.VIEW3D_PT_view3d_name.append(VIEW3D_PT_view3d_name.menu)
	bpy.types.OBJECT_PT_context_object.append(OBJECT_PT_context_object.menu)
	bpy.types.BONE_PT_context_bone.append(BONE_PT_context_bone.menu)
	bpy.types.DATA_PT_skeleton.append(DATA_PT_skeleton.menu)
	bpy.types.TEXTURE_PT_context_texture.append(TEXTURE_PT_context_texture.menu)
	bpy.types.TEXTURE_PT_image.append(TEXTURE_PT_image.menu)
	bpy.types.RENDER_PT_bake.append(RENDER_PT_bake.menu)
	bpy.types.TEXTURE_PT_mapping.append(TEXTURE_PT_mapping.menu)
	bpy.types.VIEW3D_PT_imapaint_tools_missing.append(VIEW3D_PT_imapaint_tools_missing.menu)
	bpy.types.VIEW3D_PT_slots_projectpaint.append(VIEW3D_PT_slots_projectpaint.menu)
	bpy.types.DATA_PT_geometry_curve.append(DATA_PT_geometry_curve.menu)
	bpy.types.VIEW3D_PT_transform_orientations.append(VIEW3D_PT_transform_orientations.menu)
	bpy.types.VIEW3D_PT_layers.append(VIEW3D_PT_layers.menu)
	#bpy.types.***.append(***.menu)

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
	bpy.types.VIEW3D_PT_tools_imagepaint_external.remove(VIEW3D_PT_tools_imagepaint_external.menu)
	bpy.types.TEXT_MT_text.remove(TEXT_MT_text.menu)
	bpy.types.IMAGE_MT_uvs.remove(IMAGE_MT_uvs.menu)
	bpy.types.OBJECT_PT_display.remove(OBJECT_PT_display.menu)
	bpy.types.RENDER_PT_render.remove(RENDER_PT_render.menu)
	bpy.types.MATERIAL_PT_context_material.remove(MATERIAL_PT_context_material.menu)
	bpy.types.VIEW3D_PT_view3d_properties.remove(VIEW3D_PT_view3d_properties.menu)
	bpy.types.SCENE_PT_rigid_body_world.remove(SCENE_PT_rigid_body_world.menu)
	bpy.types.NODE_MT_view.remove(NODE_MT_view.menu)
	bpy.types.VIEW3D_PT_view3d_name.remove(VIEW3D_PT_view3d_name.menu)
	bpy.types.OBJECT_PT_context_object.remove(OBJECT_PT_context_object.menu)
	bpy.types.BONE_PT_context_bone.remove(BONE_PT_context_bone.menu)
	bpy.types.DATA_PT_skeleton.remove(DATA_PT_skeleton.menu)
	bpy.types.TEXTURE_PT_context_texture.remove(TEXTURE_PT_context_texture.menu)
	bpy.types.TEXTURE_PT_image.remove(TEXTURE_PT_image.menu)
	bpy.types.RENDER_PT_bake.remove(RENDER_PT_bake.menu)
	bpy.types.TEXTURE_PT_mapping.remove(TEXTURE_PT_mapping.menu)
	bpy.types.VIEW3D_PT_imapaint_tools_missing.remove(VIEW3D_PT_imapaint_tools_missing.menu)
	bpy.types.VIEW3D_PT_slots_projectpaint.remove(VIEW3D_PT_slots_projectpaint.menu)
	bpy.types.DATA_PT_geometry_curve.remove(DATA_PT_geometry_curve.menu)
	bpy.types.VIEW3D_PT_transform_orientations.remove(VIEW3D_PT_transform_orientations.menu)
	bpy.types.VIEW3D_PT_layers.remove(VIEW3D_PT_layers.menu)
	#bpy.types.***.remove(***.menu)

# メイン関数
if __name__ == "__main__":
	register()
