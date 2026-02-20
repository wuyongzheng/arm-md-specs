## D11.10 Detecting when FEAT\_GCS is enabled

| G LCMSZ   | FEAT_GCS provides support for a common software supporting the Guarded Control Stack to run with minimal overheads on a PE that does not implement FEAT_GCS.                                                                                                                                                                                                                                                                                        |
|-----------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| G VTQRM   | FEAT_GCS provides support for a common software supporting the Guarded Control Stack to run on a PE which implements FEAT_GCS when the Guarded Control Stack is disabled for this software. This software runs with minimal additional overheads due to the Guarded Control Stack support.                                                                                                                                                          |
| I KZSCH   | Software might need to interact with the Guarded Control Stack at various points, in particular to manage the contents including removing entries from the GCS using the GCSPOPM instruction. FEAT_CHK provides a low-overhead mechanism to detect whether FEAT_GCS is enabled at the current Exception level, to allow such software to avoid running such code when FEAT_GCS is disabled. For more information about FEAT_CHK, see Check Feature. |

## Chapter D12 The Generic Timer in AArch64 state

This chapter describes the implementation of the Arm Generic Timer. It includes an overview of the AArch64 System register interface to an Arm Generic Timer.

It contains the following sections:

- About the Generic Timer.
- The AArch64 view of the Generic Timer.

The Generic Timer in AArch32 state describes the AArch32 view of the Generic Timer, and System Level Implementation of the Generic Timer describes the system level implementation of the Generic Timer.