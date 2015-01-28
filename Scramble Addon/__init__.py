bl_info = {
	"name" : "Scramble Addon",
	"author" : "さいでんか(saidenka)",
	"version" : (0,1),
	"blender" : (2, 7),
	"location" : "色々",
	"description" : "さいでんか制作の拡張機能群の詰め合わせ",
	"warning" : "",
	"wiki_url" : "",
	"tracker_url" : "",
	"category" : "3D View"
}

if "bpy" in locals():
	import imp
	imp.reload(INFO_MT_file)
	imp.reload(INFO_MT_file_external_data)
	imp.reload(INFO_MT_mesh_add)
	imp.reload(MATERIAL_MT_specials)
	imp.reload(MESH_MT_shape_key_specials)
	imp.reload(MESH_MT_vertex_group_specials)
	imp.reload(VIEW3D_MT_bone_options_toggle)
	imp.reload(VIEW3D_MT_edit_armature)
	imp.reload(VIEW3D_MT_make_links)
	imp.reload(VIEW3D_MT_object)
	imp.reload(VIEW3D_MT_object_showhide)
	imp.reload(VIEW3D_MT_object_specials)
	imp.reload(VIEW3D_MT_pose_showhide)
	imp.reload(VIEW3D_MT_select_edit_mesh)
	imp.reload(VIEW3D_MT_select_pose)
	imp.reload(VIEW3D_MT_view)
	imp.reload(VIEW3D_MT_paint_weight)
	imp.reload(VIEW3D_MT_pose_constraints)
	imp.reload(INFO_MT_render)
	imp.reload(VIEW3D_MT_edit_mesh_showhide)
	imp.reload(VIEW3D_MT_pose_specials)
	imp.reload(VIEW3D_MT_armature_specials)
	imp.reload(IMAGE_MT_view)
	imp.reload(INFO_MT_window)
	imp.reload(VIEW3D_MT_view_align)
	imp.reload(VIEW3D_MT_edit_mesh)
	imp.reload(VIEW3D_MT_edit_mesh_delete)
	imp.reload(NODE_MT_node)
else:
	from . import INFO_MT_file
	from . import INFO_MT_file_external_data
	from . import INFO_MT_mesh_add
	from . import MATERIAL_MT_specials
	from . import MESH_MT_shape_key_specials
	from . import MESH_MT_vertex_group_specials
	from . import VIEW3D_MT_bone_options_toggle
	from . import VIEW3D_MT_edit_armature
	from . import VIEW3D_MT_make_links
	from . import VIEW3D_MT_object
	from . import VIEW3D_MT_object_showhide
	from . import VIEW3D_MT_object_specials
	from . import VIEW3D_MT_pose_showhide
	from . import VIEW3D_MT_select_edit_mesh
	from . import VIEW3D_MT_select_pose
	from . import VIEW3D_MT_view
	from . import VIEW3D_MT_paint_weight
	from . import VIEW3D_MT_pose_constraints
	from . import INFO_MT_render
	from . import VIEW3D_MT_edit_mesh_showhide
	from . import VIEW3D_MT_pose_specials
	from . import VIEW3D_MT_armature_specials
	from . import IMAGE_MT_view
	from . import INFO_MT_window
	from . import VIEW3D_MT_view_align
	from . import VIEW3D_MT_edit_mesh
	from . import VIEW3D_MT_edit_mesh_delete
	from . import NODE_MT_node
import bpy

class temp(bpy.types.Operator):
	pass

# プラグインをインストールしたときの処理
def register():
	bpy.utils.register_module(__name__)
	bpy.types.INFO_MT_file.append(INFO_MT_file.menu)
	bpy.types.INFO_MT_file_external_data.append(INFO_MT_file_external_data.menu)
	bpy.types.INFO_MT_mesh_add.append(INFO_MT_mesh_add.menu)
	bpy.types.MATERIAL_MT_specials.append(MATERIAL_MT_specials.menu)
	bpy.types.MESH_MT_shape_key_specials.append(MESH_MT_shape_key_specials.menu)
	bpy.types.MESH_MT_vertex_group_specials.append(MESH_MT_vertex_group_specials.menu)
	bpy.types.VIEW3D_MT_bone_options_toggle.append(VIEW3D_MT_bone_options_toggle.menu)
	bpy.types.VIEW3D_MT_edit_armature.append(VIEW3D_MT_edit_armature.menu)
	bpy.types.VIEW3D_MT_make_links.append(VIEW3D_MT_make_links.menu)
	bpy.types.VIEW3D_MT_object.append(VIEW3D_MT_object.menu)
	bpy.types.VIEW3D_MT_object_showhide.append(VIEW3D_MT_object_showhide.menu)
	bpy.types.VIEW3D_MT_object_specials.append(VIEW3D_MT_object_specials.menu)
	bpy.types.VIEW3D_MT_pose_showhide.append(VIEW3D_MT_pose_showhide.menu)
	bpy.types.VIEW3D_MT_select_edit_mesh.append(VIEW3D_MT_select_edit_mesh.menu)
	bpy.types.VIEW3D_MT_select_pose.append(VIEW3D_MT_select_pose.menu)
	bpy.types.VIEW3D_MT_view.append(VIEW3D_MT_view.menu)
	bpy.types.VIEW3D_MT_paint_weight.append(VIEW3D_MT_paint_weight.menu)
	bpy.types.VIEW3D_MT_pose_constraints.append(VIEW3D_MT_pose_constraints.menu)
	bpy.types.INFO_MT_render.append(INFO_MT_render.menu)
	bpy.types.VIEW3D_MT_edit_mesh_showhide.append(VIEW3D_MT_edit_mesh_showhide.menu)
	bpy.types.VIEW3D_MT_pose_specials.append(VIEW3D_MT_pose_specials.menu)
	bpy.types.VIEW3D_MT_armature_specials.append(VIEW3D_MT_armature_specials.menu)
	bpy.types.IMAGE_MT_view.append(IMAGE_MT_view.menu)
	bpy.types.INFO_MT_window.append(INFO_MT_window.menu)
	bpy.types.VIEW3D_MT_view_align.append(VIEW3D_MT_view_align.menu)
	bpy.types.VIEW3D_MT_edit_mesh.append(VIEW3D_MT_edit_mesh.menu)
	bpy.types.VIEW3D_MT_edit_mesh_delete.append(VIEW3D_MT_edit_mesh_delete.menu)
	bpy.types.NODE_MT_node.append(NODE_MT_node.menu)

# プラグインをアンインストールしたときの処理
def unregister():
	bpy.utils.unregister_module(__name__)
	bpy.types.INFO_MT_file.remove(INFO_MT_file.menu)
	bpy.types.INFO_MT_file_external_data.remove(INFO_MT_file_external_data.menu)
	bpy.types.INFO_MT_mesh_add.remove(INFO_MT_mesh_add.menu)
	bpy.types.MATERIAL_MT_specials.remove(MATERIAL_MT_specials.menu)
	bpy.types.MESH_MT_shape_key_specials.remove(MESH_MT_shape_key_specials.menu)
	bpy.types.MESH_MT_vertex_group_specials.remove(MESH_MT_vertex_group_specials.menu)
	bpy.types.VIEW3D_MT_bone_options_toggle.remove(VIEW3D_MT_bone_options_toggle.menu)
	bpy.types.VIEW3D_MT_edit_armature.remove(VIEW3D_MT_edit_armature.menu)
	bpy.types.VIEW3D_MT_make_links.remove(VIEW3D_MT_make_links.menu)
	bpy.types.VIEW3D_MT_object.remove(VIEW3D_MT_object.menu)
	bpy.types.VIEW3D_MT_object_showhide.remove(VIEW3D_MT_object_showhide.menu)
	bpy.types.VIEW3D_MT_object_specials.remove(VIEW3D_MT_object_specials.menu)
	bpy.types.VIEW3D_MT_pose_showhide.remove(VIEW3D_MT_pose_showhide.menu)
	bpy.types.VIEW3D_MT_select_edit_mesh.remove(VIEW3D_MT_select_edit_mesh.menu)
	bpy.types.VIEW3D_MT_select_pose.remove(VIEW3D_MT_select_pose.menu)
	bpy.types.VIEW3D_MT_view.remove(VIEW3D_MT_view.menu)
	bpy.types.VIEW3D_MT_paint_weight.remove(VIEW3D_MT_paint_weight.menu)
	bpy.types.VIEW3D_MT_pose_constraints.remove(VIEW3D_MT_pose_constraints.menu)
	bpy.types.INFO_MT_render.remove(INFO_MT_render.menu)
	bpy.types.VIEW3D_MT_edit_mesh_showhide.remove(VIEW3D_MT_edit_mesh_showhide.menu)
	bpy.types.VIEW3D_MT_pose_specials.remove(VIEW3D_MT_pose_specials.menu)
	bpy.types.VIEW3D_MT_armature_specials.remove(VIEW3D_MT_armature_specials.menu)
	bpy.types.IMAGE_MT_view.remove(IMAGE_MT_view.menu)
	bpy.types.INFO_MT_window.remove(INFO_MT_window.menu)
	bpy.types.VIEW3D_MT_view_align.remove(VIEW3D_MT_view_align.menu)
	bpy.types.VIEW3D_MT_edit_mesh.remove(VIEW3D_MT_edit_mesh.menu)
	bpy.types.VIEW3D_MT_edit_mesh_delete.remove(VIEW3D_MT_edit_mesh_delete.menu)
	bpy.types.NODE_MT_node.remove(NODE_MT_node.menu)

# メイン関数
if __name__ == "__main__":
	register()
