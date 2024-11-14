import unreal


def RenameAndFixSyntySkeleton(source_mesh, asset):
    ####
    #   source_mesh - Source skeletal mesh to which the asset is aligned to
    #   asset - Skeletal Mesh whose skeleton is changed
    ####

    # Loading Libs
    # load the skeleton modifier
    skeleton_modifier = unreal.SkeletonModifier()
    # Set the source mesh path
    source_skeletal_mesh_path = unreal.EditorAssetLibrary.get_path_name_for_loaded_asset(source_mesh)

    # Get the path for target skeletal mesh
    skeletal_mesh_path = unreal.EditorAssetLibrary.get_path_name_for_loaded_asset(asset)
    source_skeletal_mesh = unreal.EditorAssetLibrary.load_asset(source_skeletal_mesh_path)
    skeleton_modifier.set_skeletal_mesh(source_skeletal_mesh)
    source_bones_array = skeleton_modifier.get_all_bone_names()

    # Hard coded saves for ik bones and jaw bone
    jaw_transform = skeleton_modifier.get_bone_transform("jaw")
    # IK bones
    ik_foot_root_transform = skeleton_modifier.get_bone_transform("ik_foot_root")
    ik_foot_l_transform = skeleton_modifier.get_bone_transform("ik_foot_l")
    ik_foot_r_transform = skeleton_modifier.get_bone_transform("ik_foot_r")
    ik_hand_root_transform = skeleton_modifier.get_bone_transform("ik_hand_root")
    ik_hand_gun_transform = skeleton_modifier.get_bone_transform("ik_hand_gun")
    ik_hand_l_transform = skeleton_modifier.get_bone_transform("ik_hand_l")
    ik_hand_r_transform = skeleton_modifier.get_bone_transform("ik_hand_r")

    skeleton_modifier.commit_skeleton_to_skeletal_mesh()
    missing_bones = []
    # Load the skeletal mesh asset
    skeletal_mesh = unreal.EditorAssetLibrary.load_asset(skeletal_mesh_path)
    # Get the array of Bone structures of the skeletal mesh to be changed
    skeleton_modifier.set_skeletal_mesh(skeletal_mesh)
    bones_array = skeleton_modifier.get_all_bone_names()
    # Iterate over the bones and rename to default pattern
    for bone in bones_array:
        # Fixing various missspellings of bones
        if bone == "Thight_L":
            skeleton_modifier.rename_bone("Thight_L", "Thigh_L")
        if bone == "Thight_R":
            skeleton_modifier.rename_bone("Thight_R", "Thigh_R")
        if bone == "_ik_foot_root":
            # If the root is wrongly named, so are its children
            skeleton_modifier.rename_bone("_ik_foot_root", "ik_foot_root")
            skeleton_modifier.rename_bone("_ik_foot_l", "ik_foot_l")
            skeleton_modifier.rename_bone("_ik_foot_r", "ik_foot_r")
        if bone == "_ik_hand_root":
            # If the root is wrongly named, so are its children
            skeleton_modifier.rename_bone("_ik_hand_root", "ik_hand_root")
            skeleton_modifier.rename_bone("_ik_hand_gun", "ik_hand_gun")
            skeleton_modifier.rename_bone("_ik_hand_l", "ik_hand_l")
            skeleton_modifier.rename_bone("_ik_hand_r", "ik_hand_r")
    for bone in source_bones_array:
        if bone not in bones_array:
            print(bone)  # For debug purposes
            missing_bones.append(bone)

    # Iterate over the bones and add them at the correct locations (hard coded for now)
    for bone in missing_bones:
        if bone == "ik_foot_root":
            # If the foot root is missing all ik_foot bones are missing -> add them all in order
            skeleton_modifier.add_bone("ik_foot_root", "root", ik_foot_root_transform)
            skeleton_modifier.add_bone("ik_foot_l", "ik_foot_root", ik_foot_l_transform)
            skeleton_modifier.add_bone("ik_foot_r", "ik_foot_root", ik_foot_r_transform)
        elif bone == "ik_hand_root":
            # If the hand root is missing all ik_hand bones are missing -> add them all in order
            skeleton_modifier.add_bone("ik_hand_root", "root", ik_hand_root_transform)
            skeleton_modifier.add_bone("ik_hand_gun", "ik_hand_root", ik_hand_gun_transform)
            skeleton_modifier.add_bone("ik_hand_l", "ik_hand_gun", ik_hand_l_transform)
            skeleton_modifier.add_bone("ik_hand_r", "ik_hand_gun", ik_hand_r_transform)
        elif bone == "jaw":
            # If the jaw is missing, just add it
            skeleton_modifier.add_bone("jaw", "head", jaw_transform)
        else:
            print(bone)

    # Complete the bone operations, commit changes to skeletal mesh
    mesh_name = skeletal_mesh.get_name()
    skeleton_modifier.commit_skeleton_to_skeletal_mesh()
    msg_string = "Missing Bones added to Skeletal Mesh " + mesh_name
    unreal.log(msg_string)

    unreal.log("Skeleton renamer completed for " + asset)
    return


def UnifyGenericSkeletalMesh(source_mesh, asset):

    return


def SetUniformBoneTransform(source_mesh, asset):
    ####
    #   source_mesh - Source skeletal mesh which
    #   asset - Skeletal Mesh whose skeleton is changed
    ####
    # Loading Libs
    # load the skeleton modifier
    source_skeleton_modifier = unreal.SkeletonModifier()
    target_skeleton_modifier = unreal.SkeletonModifier()
    # Source Skeletal mesh setup
    # Set the source mesh path
    source_skeletal_mesh_path = unreal.EditorAssetLibrary.get_path_name_for_loaded_asset(source_mesh)
    source_skeletal_mesh = unreal.EditorAssetLibrary.load_asset(source_skeletal_mesh_path)
    source_skeleton_modifier.set_skeletal_mesh(source_skeletal_mesh)

    # Target Skeletal mesh setup
    target_skeletal_mesh_path = unreal.EditorAssetLibrary.get_path_name_for_loaded_asset(asset)
    target_skeletal_mesh = unreal.EditorAssetLibrary.load_asset(target_skeletal_mesh_path)
    target_skeleton_modifier.set_skeletal_mesh(target_skeletal_mesh)

    # Get a list of bones in target skeletal mesh and in source mesh (only change matching ones)
    target_bones_array = target_skeleton_modifier.get_all_bone_names()
    source_bones_array = source_skeleton_modifier.get_all_bone_names()
    if set(target_bones_array) != set(source_bones_array):
        msg_string = 'INFO: The provided skeletal meshes ' + source_skeletal_mesh.get_name() + ' and ' + target_skeletal_mesh.get_name() + 'have differing bones. Process will still proceed'
        unreal.log(msg_string)
    common_bones_array = set(target_bones_array) & set(source_bones_array)
    # Apply bone transform of source to target
    for bone in common_bones_array:
        source_transform= source_skeleton_modifier.get_bone_transform(bone, False)
        target_transform=target_skeleton_modifier.get_bone_transform(bone,False)
        msg_transform = str(bone) + ' Source Translation: ' + str(source_transform) + ' || Target Translation ' + str(target_transform)
        unreal.log(msg_transform)
        target_skeleton_modifier.set_bone_transform(bone, unreal.Transform(source_transform.translation, source_transform.rotation.rotator(), source_transform.scale3d),True) #If not working change True to False (True should work better though)
    source_skeleton_modifier.commit_skeleton_to_skeletal_mesh()
    target_skeleton_modifier.commit_skeleton_to_skeletal_mesh()
    return


def SKM2SMOffsetCorrection(path_asset_skm, correct_offset):
    ###
    # Inputs:
    # path_asset_skm : skeletal mesh path that will be turned into a static mesh
    # correct_offset : bool, should the pivot offset be corrected for the last weighted bone?
    # Outputs:
    # NONE
    ###
    # Get a ref to the folder
    asset_folder = "/".join(path_asset_skm.split("/")[:-1])
    # Load the skeletal mesh
    asset_skm = unreal.EditorAssetLibrary.load_asset(path_asset_skm)

    unreal.log(asset_skm)
    weight_modifier = unreal.SkinWeightModifier()
    skeleton_modifier = unreal.SkeletonModifier()
    weight_modifier.set_skeletal_mesh(asset_skm)
    skeleton_modifier.set_skeletal_mesh(asset_skm)

    # a = skeleton_modifier.get_num_vertices()
    NameFloatMap = weight_modifier.get_vertex_weights(1)
    bone_name = list(NameFloatMap.keys())[0]
    world_location = skeleton_modifier.get_bone_transform(bone_name, True)
    # world_location={}
    # for bone in bone_name:
    # world_location = skeleton_modifier.get_bone_transform(bone_name, True)
    # rel_location = skeleton_modifier.get_bone_transform(bone_name, False)

    return world_location


def RotateBoneInMesh(skel_mesh, bone_name, rotation_vec, b_absolute_coords):
    ####
    #   skel_mesh - the skeletal mesh that is changed
    #   bone_name - the bone that is rotated
    #   rotation_vec - the 3d vector of the bone rotation
    #   b_absolute_coords - Is the new rotation in relative or world (absolute) space?
    ####
    # Loading Libs
    # load the weight modifier
    weight_modifier = unreal.SkinWeightModifier()
    # load the skeleton modifier
    skeleton_modifier = unreal.SkeletonModifier()
    EUL = unreal.EditorUtilityLibrary
    unreal.log(skel_mesh)
    # Start editing of the skeleton
    skeleton_modifier.set_skeletal_mesh(skel_mesh)
    bone_transform = skeleton_modifier.get_bone_transform(bone_name, b_absolute_coords)
    if not bone_transform:
        unreal.log("Bone could not be found, make sure spelling is correct and the specified bone exists in the entered mesh")
    else:
        unreal.log(bone_transform)
    # Build the new transform
    location = bone_transform.translation
    rotation = unreal.Rotator(rotation_vec.y, rotation_vec.z, rotation_vec.x)
    scale = bone_transform.scale3d
    new_transform = unreal.Transform(location, rotation, scale)
    unreal.log(new_transform)
    skeleton_modifier.set_bone_transform(bone_name, new_transform, True)
    skeleton_modifier.commit_skeleton_to_skeletal_mesh()

    return bone_transform


def AddBoneInMesh(skel_mesh, bone_name, bone_parent, bone_transform, b_absolute_coords):
    ####
    #   skel_mesh - the skeletal mesh that is changed
    #   bone_name - the new bone that is created
    #   bone_parent - the parent of the new bone
    #   bone_transform - the final transform of the bone
    #   b_absolute_coords - Is the new rotation in relative or world (absolute) space?
    # ToDO: Conversion of absolute world space bone transform into transform of local space for new bone
    # load the skeleton modifier
    skeleton_modifier = unreal.SkeletonModifier()
    # Start editing of the skeleton
    skeleton_modifier.set_skeletal_mesh(skel_mesh)
    skeleton_modifier.add_bone(bone_name,bone_parent,bone_transform)
    skeleton_modifier.commit_skeleton_to_skeletal_mesh()

    return bone_transform
