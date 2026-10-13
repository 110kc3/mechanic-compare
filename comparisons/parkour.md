# Parkour implementation comparison

Generated from [data/implementations.json](../data/implementations.json).

Source review: 2026-10-13. Runtime checks unperformed: 6 of 6. Navigation anchors do not establish portable functionality or fidelity.

<a id="faith-runner"></a>

## Faith Runner

Mirror’s Edge-style movement in a separate Rust crate, with a Bevy demonstration project. [readme](https://github.com/tnrjns/faith-runner/blob/9ddef190d73be4cbb7a2ae30bde67018cbe15eb9/README.md) [world](https://github.com/tnrjns/faith-runner/blob/9ddef190d73be4cbb7a2ae30bde67018cbe15eb9/crates/faith_move/src/world.rs)

Source context: **engine-independent**; languages: **Rust**; shape: **subsystem**.

Reviewed [9ddef190d73b](https://github.com/tnrjns/faith-runner/tree/9ddef190d73be4cbb7a2ae30bde67018cbe15eb9) on 2026-10-13. Runtime check: **not-run**.

### Reviewed mechanics

- **wall-run**: Controller wall-running state and wall probes. [controller](https://github.com/tnrjns/faith-runner/blob/9ddef190d73be4cbb7a2ae30bde67018cbe15eb9/crates/faith_move/src/controller.rs)
- **vault**: Vault state advances movement over or onto obstacles. [controller](https://github.com/tnrjns/faith-runner/blob/9ddef190d73be4cbb7a2ae30bde67018cbe15eb9/crates/faith_move/src/controller.rs)
- **slide**: Slide state controls movement while crouched at speed. [controller](https://github.com/tnrjns/faith-runner/blob/9ddef190d73be4cbb7a2ae30bde67018cbe15eb9/crates/faith_move/src/controller.rs)
- **ledge-grab**: Ledge hang and shimmy states are present. [controller](https://github.com/tnrjns/faith-runner/blob/9ddef190d73be4cbb7a2ae30bde67018cbe15eb9/crates/faith_move/src/controller.rs)

### Integration

The host supplies box sweep and overlap queries through World, feeds input and steps Controller; optional fixtures describe special traversal objects. These boundaries still need a host adapter. [world](https://github.com/tnrjns/faith-runner/blob/9ddef190d73be4cbb7a2ae30bde67018cbe15eb9/crates/faith_move/src/world.rs) [controller](https://github.com/tnrjns/faith-runner/blob/9ddef190d73be4cbb7a2ae30bde67018cbe15eb9/crates/faith_move/src/controller.rs)

### Requirements

- The movement crate depends on glam; the demonstration application uses Bevy. [crate](https://github.com/tnrjns/faith-runner/blob/9ddef190d73be4cbb7a2ae30bde67018cbe15eb9/crates/faith_move/Cargo.toml) [readme](https://github.com/tnrjns/faith-runner/blob/9ddef190d73be4cbb7a2ae30bde67018cbe15eb9/README.md)
- Original body, animation and sound loading uses the user’s Mirror’s Edge install; the README describes procedural arms when those files are unavailable. [readme](https://github.com/tnrjns/faith-runner/blob/9ddef190d73be4cbb7a2ae30bde67018cbe15eb9/README.md)

### Limitations

- Tuning distinguishes values attributed to original class defaults from guessed values; this is provenance in source comments, not independently measured fidelity. [tuning](https://github.com/tnrjns/faith-runner/blob/9ddef190d73be4cbb7a2ae30bde67018cbe15eb9/crates/faith_move/src/tuning.rs)
- Engine-independent source does not establish an existing adapter for every target engine. [world](https://github.com/tnrjns/faith-runner/blob/9ddef190d73be4cbb7a2ae30bde67018cbe15eb9/crates/faith_move/src/world.rs) [readme](https://github.com/tnrjns/faith-runner/blob/9ddef190d73be4cbb7a2ae30bde67018cbe15eb9/README.md)

### Declared terms

Status: **unknown**. No root license file was found during inspection of this revision; terms remain unresolved.

- No root license file found in the [reviewed repository tree](https://github.com/tnrjns/faith-runner/tree/9ddef190d73be4cbb7a2ae30bde67018cbe15eb9).

### Source navigation

| Evidence | Path | Symbols to inspect |
| --- | --- | --- |
| [readme](https://github.com/tnrjns/faith-runner/blob/9ddef190d73be4cbb7a2ae30bde67018cbe15eb9/README.md) | README.md | — |
| [crate](https://github.com/tnrjns/faith-runner/blob/9ddef190d73be4cbb7a2ae30bde67018cbe15eb9/crates/faith_move/Cargo.toml) | crates/faith_move/Cargo.toml | glam |
| [world](https://github.com/tnrjns/faith-runner/blob/9ddef190d73be4cbb7a2ae30bde67018cbe15eb9/crates/faith_move/src/world.rs) | crates/faith_move/src/world.rs | pub trait World, fn sweep, fn overlaps |
| [controller](https://github.com/tnrjns/faith-runner/blob/9ddef190d73be4cbb7a2ae30bde67018cbe15eb9/crates/faith_move/src/controller.rs) | crates/faith_move/src/controller.rs | pub struct Controller, pub fn step, fn wallrun, fn slide, fn hang, fn vault_step |
| [tuning](https://github.com/tnrjns/faith-runner/blob/9ddef190d73be4cbb7a2ae30bde67018cbe15eb9/crates/faith_move/src/tuning.rs) | crates/faith_move/src/tuning.rs | guess, ME: |

<a id="beatrun"></a>

## Beatrun Community Edition

A Garry’s Mod parkour gamemode with movement and camera behavior tied to host APIs. [readme](https://github.com/JonnyBro/beatrun/blob/d176729c9bdd2491208a9bd2e1aee0f4b715f25f/README.md) [wallrun](https://github.com/JonnyBro/beatrun/blob/d176729c9bdd2491208a9bd2e1aee0f4b715f25f/gamemodes/beatrun/gamemode/sh/WallrunME.lua)

Source context: **garrys-mod**; languages: **Lua**; shape: **gamemode**.

Reviewed [d176729c9bdd](https://github.com/JonnyBro/beatrun/tree/d176729c9bdd2491208a9bd2e1aee0f4b715f25f) on 2026-10-13. Runtime check: **not-run**.

### Reviewed mechanics

- **wall-run**: Purist wall-running checks and state update. [wallrun](https://github.com/JonnyBro/beatrun/blob/d176729c9bdd2491208a9bd2e1aee0f4b715f25f/gamemodes/beatrun/gamemode/sh/WallrunME.lua)
- **vault**: Vault variants and SetupMove hook. [vault](https://github.com/JonnyBro/beatrun/blob/d176729c9bdd2491208a9bd2e1aee0f4b715f25f/gamemodes/beatrun/gamemode/sh/Vaulting.lua)
- **wall-climb**: Climbing movement logic in the gamemode. [climb](https://github.com/JonnyBro/beatrun/blob/d176729c9bdd2491208a9bd2e1aee0f4b715f25f/gamemodes/beatrun/gamemode/sh/Climb.lua)

### Integration

Integrates through Garry’s Mod movement hooks, player state, traces and camera hooks. Reusing behavior in another engine requires translating those dependencies. [wallrun](https://github.com/JonnyBro/beatrun/blob/d176729c9bdd2491208a9bd2e1aee0f4b715f25f/gamemodes/beatrun/gamemode/sh/WallrunME.lua) [vault](https://github.com/JonnyBro/beatrun/blob/d176729c9bdd2491208a9bd2e1aee0f4b715f25f/gamemodes/beatrun/gamemode/sh/Vaulting.lua)

### Requirements

- The README installs the project as a Garry’s Mod gamemode. [readme](https://github.com/JonnyBro/beatrun/blob/d176729c9bdd2491208a9bd2e1aee0f4b715f25f/README.md)
- Wall-running calls player/movement methods and util.TraceLine. [wallrun](https://github.com/JonnyBro/beatrun/blob/d176729c9bdd2491208a9bd2e1aee0f4b715f25f/gamemodes/beatrun/gamemode/sh/WallrunME.lua)

### Limitations

- The source anchors are pieces of a full gamemode, not a standalone collision-and-input API. [wallrun](https://github.com/JonnyBro/beatrun/blob/d176729c9bdd2491208a9bd2e1aee0f4b715f25f/gamemodes/beatrun/gamemode/sh/WallrunME.lua) [vault](https://github.com/JonnyBro/beatrun/blob/d176729c9bdd2491208a9bd2e1aee0f4b715f25f/gamemodes/beatrun/gamemode/sh/Vaulting.lua)
- The reviewed snapshot contains a code license declaration; bundled asset provenance was not audited. [license](https://github.com/JonnyBro/beatrun/blob/d176729c9bdd2491208a9bd2e1aee0f4b715f25f/LICENSE) [readme](https://github.com/JonnyBro/beatrun/blob/d176729c9bdd2491208a9bd2e1aee0f4b715f25f/README.md)

### Declared terms

Status: **declared**. The root LICENSE declares WTFPL. This records the declaration only; it does not audit bundled asset terms.

- WTFPL. [license](https://github.com/JonnyBro/beatrun/blob/d176729c9bdd2491208a9bd2e1aee0f4b715f25f/LICENSE)

### Source navigation

| Evidence | Path | Symbols to inspect |
| --- | --- | --- |
| [readme](https://github.com/JonnyBro/beatrun/blob/d176729c9bdd2491208a9bd2e1aee0f4b715f25f/README.md) | README.md | — |
| [license](https://github.com/JonnyBro/beatrun/blob/d176729c9bdd2491208a9bd2e1aee0f4b715f25f/LICENSE) | LICENSE | — |
| [wallrun](https://github.com/JonnyBro/beatrun/blob/d176729c9bdd2491208a9bd2e1aee0f4b715f25f/gamemodes/beatrun/gamemode/sh/WallrunME.lua) | gamemodes/beatrun/gamemode/sh/WallrunME.lua | PuristWallrunningCheck, PuristWallrunningThink, util.TraceLine |
| [vault](https://github.com/JonnyBro/beatrun/blob/d176729c9bdd2491208a9bd2e1aee0f4b715f25f/gamemodes/beatrun/gamemode/sh/Vaulting.lua) | gamemodes/beatrun/gamemode/sh/Vaulting.lua | Vault1, BeatrunVaulting |
| [climb](https://github.com/JonnyBro/beatrun/blob/d176729c9bdd2491208a9bd2e1aee0f4b715f25f/gamemodes/beatrun/gamemode/sh/Climb.lua) | gamemodes/beatrun/gamemode/sh/Climb.lua | — |

<a id="noshot"></a>

## NOSHOT First Person Controller

A Godot C# movement project with dedicated wall-running, vertical wall-running and vault states. [readme](https://github.com/theRealUnd3rdog/Godot_Noshot_Controller/blob/15ac57ce0b7f1ab94c264fecd14e87732c8264fb/README.md) [wallrun](https://github.com/theRealUnd3rdog/Godot_Noshot_Controller/blob/15ac57ce0b7f1ab94c264fecd14e87732c8264fb/Scripts/PlayerMovementStates/PlayerWallrun.cs)

Source context: **godot**; languages: **C#**; shape: **controller-project**.

Reviewed [15ac57ce0b7f](https://github.com/theRealUnd3rdog/Godot_Noshot_Controller/tree/15ac57ce0b7f1ab94c264fecd14e87732c8264fb) on 2026-10-13. Runtime check: **not-run**.

### Reviewed mechanics

- **wall-run**: Wall-running state uses ray checks, friction and a jump exit. [wallrun](https://github.com/theRealUnd3rdog/Godot_Noshot_Controller/blob/15ac57ce0b7f1ab94c264fecd14e87732c8264fb/Scripts/PlayerMovementStates/PlayerWallrun.cs)
- **wall-climb**: Vertical wall-running state is present. [wallclimb](https://github.com/theRealUnd3rdog/Godot_Noshot_Controller/blob/15ac57ce0b7f1ab94c264fecd14e87732c8264fb/Scripts/PlayerMovementStates/PlayerVerticalWallrun.cs)
- **vault**: Vault state integrates with the movement state machine. [vault](https://github.com/theRealUnd3rdog/Godot_Noshot_Controller/blob/15ac57ce0b7f1ab94c264fecd14e87732c8264fb/Scripts/PlayerMovementStates/PlayerVault.cs)

### Integration

Use or adapt the Godot player scene, movement class and state machine; the wall-running state delegates collision queries and velocity to PlayerMovement. [wallrun](https://github.com/theRealUnd3rdog/Godot_Noshot_Controller/blob/15ac57ce0b7f1ab94c264fecd14e87732c8264fb/Scripts/PlayerMovementStates/PlayerWallrun.cs) [movement](https://github.com/theRealUnd3rdog/Godot_Noshot_Controller/blob/15ac57ce0b7f1ab94c264fecd14e87732c8264fb/Scripts/PlayerMovement.cs)

### Requirements

- The setup section requires Godot 4.3 Mono/.NET; the introduction mentions 4.2, so version claims should retain that distinction. [readme](https://github.com/theRealUnd3rdog/Godot_Noshot_Controller/blob/15ac57ce0b7f1ab94c264fecd14e87732c8264fb/README.md) [project](https://github.com/theRealUnd3rdog/Godot_Noshot_Controller/blob/15ac57ce0b7f1ab94c264fecd14e87732c8264fb/FirstGodotProject.csproj)
- Movement is written in C# and the README specifies Jolt physics. [readme](https://github.com/theRealUnd3rdog/Godot_Noshot_Controller/blob/15ac57ce0b7f1ab94c264fecd14e87732c8264fb/README.md) [wallrun](https://github.com/theRealUnd3rdog/Godot_Noshot_Controller/blob/15ac57ce0b7f1ab94c264fecd14e87732c8264fb/Scripts/PlayerMovementStates/PlayerWallrun.cs)

### Limitations

- This is not a native GDScript controller; a GDScript-only project would require an adaptation. [wallrun](https://github.com/theRealUnd3rdog/Godot_Noshot_Controller/blob/15ac57ce0b7f1ab94c264fecd14e87732c8264fb/Scripts/PlayerMovementStates/PlayerWallrun.cs) [project](https://github.com/theRealUnd3rdog/Godot_Noshot_Controller/blob/15ac57ce0b7f1ab94c264fecd14e87732c8264fb/FirstGodotProject.csproj)
- Scene/state-machine integration is required; source review did not establish a direct import into an existing player controller. [wallrun](https://github.com/theRealUnd3rdog/Godot_Noshot_Controller/blob/15ac57ce0b7f1ab94c264fecd14e87732c8264fb/Scripts/PlayerMovementStates/PlayerWallrun.cs) [movement](https://github.com/theRealUnd3rdog/Godot_Noshot_Controller/blob/15ac57ce0b7f1ab94c264fecd14e87732c8264fb/Scripts/PlayerMovement.cs)

### Declared terms

Status: **declared**. The root LICENSE declares MIT. The README separately describes project assets as CC0; this project has not audited asset provenance.

- MIT. [license](https://github.com/theRealUnd3rdog/Godot_Noshot_Controller/blob/15ac57ce0b7f1ab94c264fecd14e87732c8264fb/LICENSE)

### Source navigation

| Evidence | Path | Symbols to inspect |
| --- | --- | --- |
| [readme](https://github.com/theRealUnd3rdog/Godot_Noshot_Controller/blob/15ac57ce0b7f1ab94c264fecd14e87732c8264fb/README.md) | README.md | — |
| [license](https://github.com/theRealUnd3rdog/Godot_Noshot_Controller/blob/15ac57ce0b7f1ab94c264fecd14e87732c8264fb/LICENSE) | LICENSE | — |
| [project](https://github.com/theRealUnd3rdog/Godot_Noshot_Controller/blob/15ac57ce0b7f1ab94c264fecd14e87732c8264fb/FirstGodotProject.csproj) | FirstGodotProject.csproj | — |
| [wallrun](https://github.com/theRealUnd3rdog/Godot_Noshot_Controller/blob/15ac57ce0b7f1ab94c264fecd14e87732c8264fb/Scripts/PlayerMovementStates/PlayerWallrun.cs) | Scripts/PlayerMovementStates/PlayerWallrun.cs | PlayerWallrun, PhysicsUpdate, SendRayInDirection |
| [wallclimb](https://github.com/theRealUnd3rdog/Godot_Noshot_Controller/blob/15ac57ce0b7f1ab94c264fecd14e87732c8264fb/Scripts/PlayerMovementStates/PlayerVerticalWallrun.cs) | Scripts/PlayerMovementStates/PlayerVerticalWallrun.cs | PlayerVerticalWallrun |
| [vault](https://github.com/theRealUnd3rdog/Godot_Noshot_Controller/blob/15ac57ce0b7f1ab94c264fecd14e87732c8264fb/Scripts/PlayerMovementStates/PlayerVault.cs) | Scripts/PlayerMovementStates/PlayerVault.cs | PlayerVault |
| [movement](https://github.com/theRealUnd3rdog/Godot_Noshot_Controller/blob/15ac57ce0b7f1ab94c264fecd14e87732c8264fb/Scripts/PlayerMovement.cs) | Scripts/PlayerMovement.cs | PlayerMovement |

<a id="parks-edge"></a>

## Park’s Edge

A Minecraft movement mod whose README describes Mirror’s Edge-inspired controls. [readme](https://github.com/uLmElKa/Park-s-Edge/blob/7709f2bb130d9edd0b94b401e6604a8664b91988/README.md) [movement](https://github.com/uLmElKa/Park-s-Edge/blob/7709f2bb130d9edd0b94b401e6604a8664b91988/java/com/parkedge/client/MovementController.java)

Source context: **minecraft**; languages: **Java**; shape: **mod**.

Reviewed [7709f2bb130d](https://github.com/uLmElKa/Park-s-Edge/tree/7709f2bb130d9edd0b94b401e6604a8664b91988) on 2026-10-13. Runtime check: **not-run**.

### Reviewed mechanics

- **wall-run**: Client movement controller contains wall-running state. [movement](https://github.com/uLmElKa/Park-s-Edge/blob/7709f2bb130d9edd0b94b401e6604a8664b91988/java/com/parkedge/client/MovementController.java)
- **wall-climb**: The client controller contains climbing states; the README documents the controls. [movement](https://github.com/uLmElKa/Park-s-Edge/blob/7709f2bb130d9edd0b94b401e6604a8664b91988/java/com/parkedge/client/MovementController.java) [readme](https://github.com/uLmElKa/Park-s-Edge/blob/7709f2bb130d9edd0b94b401e6604a8664b91988/README.md)
- **vault**: tryStartVault handles a vault attempt. [movement](https://github.com/uLmElKa/Park-s-Edge/blob/7709f2bb130d9edd0b94b401e6604a8664b91988/java/com/parkedge/client/MovementController.java)
- **slide**: Client slide state has server-side pose messaging. [movement](https://github.com/uLmElKa/Park-s-Edge/blob/7709f2bb130d9edd0b94b401e6604a8664b91988/java/com/parkedge/client/MovementController.java) [server](https://github.com/uLmElKa/Park-s-Edge/blob/7709f2bb130d9edd0b94b401e6604a8664b91988/java/com/parkedge/network/ServerMovementHandler.java)

### Integration

Uses Minecraft player APIs, mixins and Architectury networking. The server handler receives movement actions; this is not evidence of validated multiplayer movement. [movement](https://github.com/uLmElKa/Park-s-Edge/blob/7709f2bb130d9edd0b94b401e6604a8664b91988/java/com/parkedge/client/MovementController.java) [server](https://github.com/uLmElKa/Park-s-Edge/blob/7709f2bb130d9edd0b94b401e6604a8664b91988/java/com/parkedge/network/ServerMovementHandler.java)

### Requirements

- The build properties target Minecraft 1.21.1 and list Fabric, NeoForge and Architectury versions. No loader build was tested here. [versions](https://github.com/uLmElKa/Park-s-Edge/blob/7709f2bb130d9edd0b94b401e6604a8664b91988/gradle.properties)
- Implementation depends on Minecraft client/server player classes. [movement](https://github.com/uLmElKa/Park-s-Edge/blob/7709f2bb130d9edd0b94b401e6604a8664b91988/java/com/parkedge/client/MovementController.java) [server](https://github.com/uLmElKa/Park-s-Edge/blob/7709f2bb130d9edd0b94b401e6604a8664b91988/java/com/parkedge/network/ServerMovementHandler.java)

### Limitations

- The author states compatibility and bugs are not established; the source was not run by this project. [readme](https://github.com/uLmElKa/Park-s-Edge/blob/7709f2bb130d9edd0b94b401e6604a8664b91988/README.md)
- Source manifest and public listing disagree on license declarations; do not silently choose one. [manifest](https://github.com/uLmElKa/Park-s-Edge/blob/7709f2bb130d9edd0b94b401e6604a8664b91988/fabric/src/main/resources/fabric.mod.json) [listing](https://www.curseforge.com/minecraft/mc-mods/parks-edge)

### Declared terms

Status: **conflicting**. Fabric manifest declares CC0-1.0; the CurseForge listing displayed MIT on the review date. No root license file was found. Clarification remains unresolved.

- CC0-1.0. [manifest](https://github.com/uLmElKa/Park-s-Edge/blob/7709f2bb130d9edd0b94b401e6604a8664b91988/fabric/src/main/resources/fabric.mod.json)
- MIT. [listing](https://www.curseforge.com/minecraft/mc-mods/parks-edge)

### Source navigation

| Evidence | Path | Symbols to inspect |
| --- | --- | --- |
| [readme](https://github.com/uLmElKa/Park-s-Edge/blob/7709f2bb130d9edd0b94b401e6604a8664b91988/README.md) | README.md | — |
| [movement](https://github.com/uLmElKa/Park-s-Edge/blob/7709f2bb130d9edd0b94b401e6604a8664b91988/java/com/parkedge/client/MovementController.java) | java/com/parkedge/client/MovementController.java | MovementController, tryStartVault, tick, wallRunActive |
| [server](https://github.com/uLmElKa/Park-s-Edge/blob/7709f2bb130d9edd0b94b401e6604a8664b91988/java/com/parkedge/network/ServerMovementHandler.java) | java/com/parkedge/network/ServerMovementHandler.java | ServerMovementHandler, register |
| [versions](https://github.com/uLmElKa/Park-s-Edge/blob/7709f2bb130d9edd0b94b401e6604a8664b91988/gradle.properties) | gradle.properties | minecraft_version = 1.21.1 |
| [manifest](https://github.com/uLmElKa/Park-s-Edge/blob/7709f2bb130d9edd0b94b401e6604a8664b91988/fabric/src/main/resources/fabric.mod.json) | fabric/src/main/resources/fabric.mod.json | CC0-1.0 |
| [listing](https://www.curseforge.com/minecraft/mc-mods/parks-edge) | External listing; dated observation | — |

<a id="still-alive"></a>

## Still Alive / Mirror’s Edge Unity port

A Unity port with converted move classes and project-level integration. [readme](https://github.com/Eideren/Mirror-s-Edge/blob/f34b689435293a0df446d8ee20a7cf9352364389/README.md) [wallrun](https://github.com/Eideren/Mirror-s-Edge/blob/f34b689435293a0df446d8ee20a7cf9352364389/Assets/Source/Integration/Converted/TdGame/TdMove_WallRun.cs)

Source context: **unity**; languages: **C#**; shape: **game-port**.

Reviewed [f34b68943529](https://github.com/Eideren/Mirror-s-Edge/tree/f34b689435293a0df446d8ee20a7cf9352364389) on 2026-10-13. Runtime check: **not-run**.

### Reviewed mechanics

- **wall-run**: Converted wall-running move class and state transitions. [wallrun](https://github.com/Eideren/Mirror-s-Edge/blob/f34b689435293a0df446d8ee20a7cf9352364389/Assets/Source/Integration/Converted/TdGame/TdMove_WallRun.cs)
- **vault**: Converted speed-vault move class and state transitions. [vault](https://github.com/Eideren/Mirror-s-Edge/blob/f34b689435293a0df446d8ee20a7cf9352364389/Assets/Source/Integration/Converted/TdGame/TdMove_SpeedVault.cs)

### Integration

Move classes depend on the converted TdGame pawn, physics, animation and integration types. This is a full port context, not an isolated Unity character-controller package. [wallrun](https://github.com/Eideren/Mirror-s-Edge/blob/f34b689435293a0df446d8ee20a7cf9352364389/Assets/Source/Integration/Converted/TdGame/TdMove_WallRun.cs) [vault](https://github.com/Eideren/Mirror-s-Edge/blob/f34b689435293a0df446d8ee20a7cf9352364389/Assets/Source/Integration/Converted/TdGame/TdMove_SpeedVault.cs)

### Requirements

- The README targets Unity 2022.3 and describes Git LFS requirements for cloning. [readme](https://github.com/Eideren/Mirror-s-Edge/blob/f34b689435293a0df446d8ee20a7cf9352364389/README.md) [version](https://github.com/Eideren/Mirror-s-Edge/blob/f34b689435293a0df446d8ee20a7cf9352364389/ProjectSettings/ProjectVersion.txt)
- Reviewed move classes rely on converted game framework types. [wallrun](https://github.com/Eideren/Mirror-s-Edge/blob/f34b689435293a0df446d8ee20a7cf9352364389/Assets/Source/Integration/Converted/TdGame/TdMove_WallRun.cs) [vault](https://github.com/Eideren/Mirror-s-Edge/blob/f34b689435293a0df446d8ee20a7cf9352364389/Assets/Source/Integration/Converted/TdGame/TdMove_SpeedVault.cs)

### Limitations

- The README lists outstanding character-controller bugs and frame-rate concerns. [readme](https://github.com/Eideren/Mirror-s-Edge/blob/f34b689435293a0df446d8ee20a7cf9352364389/README.md)
- A move class alone does not establish completeness of native behavior or successful integration into another Unity game. [wallrun](https://github.com/Eideren/Mirror-s-Edge/blob/f34b689435293a0df446d8ee20a7cf9352364389/Assets/Source/Integration/Converted/TdGame/TdMove_WallRun.cs) [vault](https://github.com/Eideren/Mirror-s-Edge/blob/f34b689435293a0df446d8ee20a7cf9352364389/Assets/Source/Integration/Converted/TdGame/TdMove_SpeedVault.cs)

### Declared terms

Status: **unknown**. No root license file was found during inspection of this revision; terms remain unresolved.

- No root license file found in the [reviewed repository tree](https://github.com/Eideren/Mirror-s-Edge/tree/f34b689435293a0df446d8ee20a7cf9352364389).

### Source navigation

| Evidence | Path | Symbols to inspect |
| --- | --- | --- |
| [readme](https://github.com/Eideren/Mirror-s-Edge/blob/f34b689435293a0df446d8ee20a7cf9352364389/README.md) | README.md | — |
| [version](https://github.com/Eideren/Mirror-s-Edge/blob/f34b689435293a0df446d8ee20a7cf9352364389/ProjectSettings/ProjectVersion.txt) | ProjectSettings/ProjectVersion.txt | — |
| [wallrun](https://github.com/Eideren/Mirror-s-Edge/blob/f34b689435293a0df446d8ee20a7cf9352364389/Assets/Source/Integration/Converted/TdGame/TdMove_WallRun.cs) | Assets/Source/Integration/Converted/TdGame/TdMove_WallRun.cs | TdMove_WallRun, CanDoMove, StartMove |
| [vault](https://github.com/Eideren/Mirror-s-Edge/blob/f34b689435293a0df446d8ee20a7cf9352364389/Assets/Source/Integration/Converted/TdGame/TdMove_SpeedVault.cs) | Assets/Source/Integration/Converted/TdGame/TdMove_SpeedVault.cs | TdMove_SpeedVault, CanDoMove, StartMove |

<a id="dani-fps"></a>

## Dani simple FPS movement

A small Rigidbody-based movement script used as a simpler baseline, without reviewed wall-running code. [readme](https://github.com/DaniDevy/FPS_Movement_Rigidbody/blob/e2688501e1309cc35f6d8f14c0c1bbc8146a86b9/README.md) [movement](https://github.com/DaniDevy/FPS_Movement_Rigidbody/blob/e2688501e1309cc35f6d8f14c0c1bbc8146a86b9/PlayerMovement.cs)

Source context: **unity**; languages: **C#**; shape: **movement-baseline**.

Reviewed [e2688501e130](https://github.com/DaniDevy/FPS_Movement_Rigidbody/tree/e2688501e1309cc35f6d8f14c0c1bbc8146a86b9) on 2026-10-13. Runtime check: **not-run**.

### Reviewed mechanics

- **jump**: Jump applies Rigidbody forces and enforces a jump cooldown. [movement](https://github.com/DaniDevy/FPS_Movement_Rigidbody/blob/e2688501e1309cc35f6d8f14c0c1bbc8146a86b9/PlayerMovement.cs)
- **slide**: StartCrouch adds a slide force; CounterMovement changes crouched braking. [movement](https://github.com/DaniDevy/FPS_Movement_Rigidbody/blob/e2688501e1309cc35f6d8f14c0c1bbc8146a86b9/PlayerMovement.cs)

### Integration

Attach and configure the Unity MonoBehaviour with a Rigidbody, transforms and input mappings. The script reads Unity input and collision callbacks directly. [movement](https://github.com/DaniDevy/FPS_Movement_Rigidbody/blob/e2688501e1309cc35f6d8f14c0c1bbc8146a86b9/PlayerMovement.cs)

### Requirements

- Unity C# and Rigidbody physics; setup instructions are linked as a tutorial from the README. [movement](https://github.com/DaniDevy/FPS_Movement_Rigidbody/blob/e2688501e1309cc35f6d8f14c0c1bbc8146a86b9/PlayerMovement.cs) [readme](https://github.com/DaniDevy/FPS_Movement_Rigidbody/blob/e2688501e1309cc35f6d8f14c0c1bbc8146a86b9/README.md)

### Limitations

- The inspected script implements jumping and crouch sliding; the seed does not identify a wall-running implementation here. [movement](https://github.com/DaniDevy/FPS_Movement_Rigidbody/blob/e2688501e1309cc35f6d8f14c0c1bbc8146a86b9/PlayerMovement.cs)
- Source is a basic movement reference, with no runtime observation of behavior in a current Unity version. [readme](https://github.com/DaniDevy/FPS_Movement_Rigidbody/blob/e2688501e1309cc35f6d8f14c0c1bbc8146a86b9/README.md) [movement](https://github.com/DaniDevy/FPS_Movement_Rigidbody/blob/e2688501e1309cc35f6d8f14c0c1bbc8146a86b9/PlayerMovement.cs)

### Declared terms

Status: **declared**. The root LICENSE declares MIT.

- MIT. [license](https://github.com/DaniDevy/FPS_Movement_Rigidbody/blob/e2688501e1309cc35f6d8f14c0c1bbc8146a86b9/LICENSE)

### Source navigation

| Evidence | Path | Symbols to inspect |
| --- | --- | --- |
| [readme](https://github.com/DaniDevy/FPS_Movement_Rigidbody/blob/e2688501e1309cc35f6d8f14c0c1bbc8146a86b9/README.md) | README.md | — |
| [license](https://github.com/DaniDevy/FPS_Movement_Rigidbody/blob/e2688501e1309cc35f6d8f14c0c1bbc8146a86b9/LICENSE) | LICENSE | — |
| [movement](https://github.com/DaniDevy/FPS_Movement_Rigidbody/blob/e2688501e1309cc35f6d8f14c0c1bbc8146a86b9/PlayerMovement.cs) | PlayerMovement.cs | PlayerMovement, Movement, Jump, StartCrouch, CounterMovement |
