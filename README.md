Asset / Actor Action Utilities
Inspired by the work of Simon Blakeney at https://dev.epicgames.com/community/learning/tutorials/1x0V/unreal-engine-automate-with-33-scripted-action-utilities.

UEUtils53 is a sample project for unreal engine 5.3 containing various Asset Action Utilities and the associated python scripts.
Beta release (current and upcoming features)
SkeletalMesh Actions:
  - Add new Bone to parent Bone (implemented, untested)
  - Batch create static meshes from skeletal meshes with optional offset to set the pivot to the last corrected bone instead of the root of the original skeletal mesh (implemented, tested with Synty Polygon Mechs)
  - Synty Unreal Engine 4 Mannequin Gen1->Gen2 Transform correction (implemented, untested, Skeletal meshes need to have the same skeleton/ bone names)
  - Synty Skeleton Unifier (implemented, tested across various packs. Might not support the knights pack characters)
  - Generic Skeleton Unifier (Work In Progress)







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
