# ##### BEGIN GPL LICENSE BLOCK #####
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; either version 2
#  of the License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software Foundation,
#  Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
# ##### END GPL LICENSE BLOCK #####

bl_info = {
    "name": "LowPolyFactory",
    "author": "Lubos Lenco",
    "version": (1, 0),
    "blender": (2, 80, 0),
    "location": "View3D > Add > Mesh > LowPoly",
    "description": "Add lowpoly objects",
    "wiki_url": "http://lowpolyfactory.com/",
    "category": "Add Mesh",
}

if "bpy" in locals():
    import importlib
    importlib.reload(LowPolyFactory)
else:
    from add_mesh_LowPolyFactory import LowPolyFactory
    from add_mesh_LowPolyFactory import editor
    from add_mesh_LowPolyFactory import LPFAddonPreferences
    import bpy
    from bpy.props import *


class MENU_MT_LPF(bpy.types.Menu):
    bl_idname = "MENU_MT_LPF_Menu_Add"
    bl_label = "LowPoly"
    def draw(self, context):
        self.layout.operator_context = 'INVOKE_REGION_WIN'
        rock_id = LowPolyFactory.add_mesh_rock.bl_idname
        tree_id = LowPolyFactory.add_mesh_tree.bl_idname
        bush_id = LowPolyFactory.add_mesh_bush.bl_idname
        grass_id = LowPolyFactory.add_mesh_grass.bl_idname
        cloud_id = LowPolyFactory.add_mesh_cloud.bl_idname
        terrain_id = LowPolyFactory.add_mesh_terrain.bl_idname
        water_id = LowPolyFactory.add_mesh_water.bl_idname
        self.layout.operator(rock_id, text="Rock", icon="PLUGIN")
        self.layout.operator(tree_id, text="Tree", icon="PLUGIN")
        self.layout.operator(bush_id, text="Bush", icon="PLUGIN")
        self.layout.operator(grass_id, text="Grass", icon="PLUGIN")
        self.layout.operator(cloud_id, text="Cloud", icon="PLUGIN")
        self.layout.operator(terrain_id, text="Terrain", icon="PLUGIN")
        self.layout.operator(water_id, text="Water", icon="PLUGIN")


# REGISTER

def menu_func(self, context):
    self.layout.menu(MENU_MT_LPF.bl_idname, icon="PLUGIN")


classes = (
    MENU_MT_LPF,
    LowPolyFactory.add_mesh_rock,
    LowPolyFactory.add_mesh_tree,
    LowPolyFactory.add_mesh_bush,
    LowPolyFactory.add_mesh_grass,
    LowPolyFactory.add_mesh_cloud,
    LowPolyFactory.add_mesh_terrain,
    LowPolyFactory.add_mesh_water,
    LPFAddonPreferences.LPFAddonPreferences,
    editor.LPF_Panel,
    editor.LPF_UpdateMaterialsButton,
    editor.LPF_UpdateLightingButton,
    editor.LPF_PopulateButton,
    
    
)
def register():
    for cls in classes:
        bpy.utils.register_class(cls)
    #bpy.utils.register_module(__name__)
    bpy.types.VIEW3D_MT_mesh_add.append(menu_func)


def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)
    bpy.types.VIEW3D_MT_mesh_add.remove(menu_func)


if __name__ == "__main__":
    register()
