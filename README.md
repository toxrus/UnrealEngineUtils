Asset / Actor Action Utilities
Inspired by the work of Simon Blakeney at https://dev.epicgames.com/community/learning/tutorials/1x0V/unreal-engine-automate-with-33-scripted-action-utilities.

UEUtils53 is a sample project for unreal engine 5.3 containing various Asset Action Utilities and the associated python scripts.
Beta release (current and upcoming features)
SkeletalMesh Actions:
  - Add new Bone to parent Bone (implemented, untested)
  - Batch create static meshes from skeletal meshes with optional offset to set the pivot to the last corrected bone instead of the root of the original skeletal mesh (implemented, tested with Synty Polygon Mechs)
  - Synty Unreal Engine 4 Mannequin Gen1->Gen2 Transform correction (implemented, tested with Apoc Gen 2 and StarterPack Gen1, will ignore extra bones/sockets on either skeletal mesh)
  - Synty Skeleton Unifier (implemented, tested across various packs. Might not support the knights pack characters)
  - Generic Skeleton Unifier (Work In Progress)
  - AddMissingIKBones adds IK and Jaw bones to selected skeletal meshes (Tested with Starter and ApocGen2, both UE4 skeletons. Need to apply Gen2 fix first for correct rotations. Should also work with any other skeleton)

Setup Instructions: Set an additional Python Path in project settings -> plugins -> python that targets the exact subfolder containing the .py file (Isolate Interpreter Environment is optional and most likely shouldn't be enabled)

IF USING IN ANOTHER PROJECT PLEASE ENABLE THE FOLLOWING PLUGINS:
  - ModelingToolsEditorMode
  - SkeletalMeshModelingTools
  - GeometryScripting

#### NOTE ####
If using translation retargeting options in any skeleton any skeleton changes seems to reset them.
To use the Gen1 Fix and Add missing IK bones options try the following work around:
  - Advance copy the intended source skeletal mesh with its skeleton to a new folder. Use this as source instead
  - After running the fixes the copied source can be deleted (or kept around for reuse)
  - Assign the original source skeleton to the fixed, former gen1 skeletal meshes.

Since translation retargeting options are stored on the skeleton this way they should be preserved.












LEGACY // Unsupported

Make sure to use the unreal engine version specified to load the uasset files to prevent issues. Then migrate into target project. For manual setup check the blueprintue.com links.
Also note the issues / problems listed with each Utility before using!
Please turn on the Geometry Script (experimental) and Dataprep Editor plugins to ensure that the action utils work correctly.

How to install:
Place inside content folder. That's it. Should load automatically and be useable.


EUBP_SkeletonFix  https://blueprintue.com/blueprint/gvwkv37g/ UE 5.4 , Add missing IK Bones to Synty Skeletal Meshes using python command UE5SkeletonRenamer.py from https://github.com/toxrus/UEPythonUtils

EUBP_ScaleRotate   https://blueprintue.com/blueprint/wgtfg46g/ UE 5.3

EUBP_AssignSkeleton  https://blueprintue.com/blueprint/3iw2vz5b/ UE 5.3

EUBP_TransformSkeletalMesh https://blueprintue.com/blueprint/b4fxvyq_/ UE5.3 --Enum accepts cape, tail, backpack for now to fix corresponding synty asset root bones -> See also https://github.com/toxrus/UEPythonUtils -> CorrectBoneOffSet for needed python script
