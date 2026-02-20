## D11.5 Stage 1 permission model

| G FJCSY   | FEAT_GCS provides EL1 with controls to govern the behavior of EL0 Guarded Control Stacks when operating in the EL1&0 translation regime, with little or no intervention from Exception levels higher than EL1.   |
|-----------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| G FHRKC   | FEAT_GCS provides EL2 with controls to govern the behavior of EL0 Guarded Control Stacks when operating in the EL2&0 translation regime, with little or no intervention from Exception levels higher than EL2.   |
| G RDKLS   | FEAT_GCS provides EL1 with controls to govern the behavior of EL1 Guarded Control Stacks, while allowing EL2 to opt-in to manage some aspects of EL1 Guarded Control Stacks to provide additional security.      |
| G PDKVN   | FEAT_GCS provides EL2 with controls to govern the behavior of EL2 Guarded Control Stacks.                                                                                                                        |
| G LJFBN   | FEAT_GCS provides EL3 with controls to govern the behavior of EL3 Guarded Control Stacks.                                                                                                                        |
| I CZTDM   | FEAT_S1PIE is required to be implemented if FEAT_GCS is implemented.                                                                                                                                             |

## D11.5.1 Stage 1 Base Permissions

- IMDFXL

The permissions encodings that permit Guarded Control Stack data access can only be configured when stage 1 translation uses the Indirect permission scheme.

- IBVLMP For translation regimes that apply to EL0 and a higher Exception level and where a Guarded Control Stack is being used for privileged execution, unprivileged data accesses do not write to such a Guarded Control Stack. For more information, see Stage 1 permissions.

IZZMLZ For translation regimes that apply to EL0 and a higher Exception level and where a Guarded Control Stack is being used for privileged execution but also accessible by any of unprivileged Data read accesses or unprivileged Instruction accesses, such a Guarded Control Stack is accessible by privileged Guarded Control Stack data access irrespective of the value of PSTATE.PAN. For more information, see Stage 1 permissions.

ILZXNK

For the purpose of permission checking, the DC IV AC instruction is considered to produce a privileged explicit data write access other than a Guarded Control Stack data access.

If the Point of Coherency is before any level of cache, it is IMPLEMENTATION DEFINED whether the DC IV AC instruction can generate a Permission fault.

- IFRYGL When FEAT\_CMOW is implemented and SCTLR\_EL1.UCI is 1 and SCTLR\_EL1.CMOW is 1, for the purpose of permission checking, the following instructions executed at EL0 are considered as producing an unprivileged explicit data write access other than a Guarded Control Stack data access:
- IC IVAU.
- DCCVAC.
- DCCIGVAC.
- DCCIGDVAC.

If the Point of Coherency is before any level of cache, it is IMPLEMENTATION DEFINED whether the above instructions can generate a Permission fault.

If the Point of Unification is before any level of data cache, it is IMPLEMENTATION DEFINED whether the above instructions can generate a Permission fault.

- SDBWHS EL0 Guarded Control Stack pages are expected to use:
- UnprivRead as 1, UnprivWrite as 0, UnprivExecute as 0 and UnprivGCS as 1 in S1UnprivBasePerm.
- PrivRead as 1, PrivWrite as 0 or 1, PrivExecute as 0 and PrivGCS as 0 in S1PrivBasePerm.

EL0 Guarded Control Stack pages are generally accessible from EL1, enabling management from EL1. If PrivWrite is 0, then EL1 software should use the GCSSTTR instruction to manage the EL0 Guarded Control Stack.

EL1 Guarded Control Stack pages are expected to use:

- UnprivRead as 0, UnprivWrite as 0, UnprivExecute as 0 and UnprivGCS as 0 in S1UnprivBasePerm.
- PrivRead as 1, PrivWrite as 0, PrivExecute as 0 and PrivGCS as 1 in S1PrivBasePerm.

SGRGDT

SYNDKX

SHKJXY

SMQRCG

Management of EL1 Guarded Control Stack pages is possible from EL1 by using the GCSSTR or GCSPUSHM instructions.

In a translation regime that applies to EL0 and a higher Exception level, the higher Exception level software cannot use unprivileged store instructions that perform non-Guarded Control Stack data access to manage the Guarded Control Stack pages of EL0. The higher Exception level software should use privileged store instructions or GCSSTTR instead.

In a translation regime that applies to EL0 and a higher Exception level, the higher Exception level software can make use of GCSSTR and GCSPUSHM instructions to manage the Guarded Control Stack pages of the higher Exception level. In a translation regime that applies to only one Exception level, software can make use of GCSSTR and GCSPUSHM instructions to manage the Guarded Control Stack pages of the current Exception level.

Note: The GCSPUSHM instruction executes as a NOP when the Guarded Control Stack is Disabled at the current Exception level. The GCSSTR instruction is functional even if the Guarded Control Stack is Disabled at the current Exception level.

When PSTATE.PAN is 1, in a translation regime that applies to EL0 and a higher Exception level, the higher Exception level software can use unprivileged load instructions that perform non-Guarded Control Stack data access to manage the Guarded Control Stack pages of EL0.

## Example:

```
;At EL0 BL ;produce a GCS store operation SVC #0x0 ;exception to EL1 and PSTATE.PAN is set to 0b1 MRS x0,GCSPR_EL0 GCSB DSYNC LDTR x1,[x0] ;read GCS contents of EL0
```

## D11.5.2 Security states

| I FYTRK   | AGuarded Control Stack data access generated in Secure state that is marked in the first stage of translation as being Non-secure generates a Permission fault.                                              |
|-----------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| I FDCRS   | AGuarded Control Stack data access generated in Secure state is allowed to access Non-secure memory as determined by Memory access control.                                                                  |
| I RSDVG   | When FEAT_RME is implemented, during execution at EL3, a Guarded Control Stack data access to physical memory other than the Root physical address space causes a stage 1 Permission fault.                  |
| I HGYTX   | If execution is using the Realm EL2 or Realm EL2&0 translation regime, a Guarded Control Stack data access to physical memory other than the Realm physical address space causes a stage 1 Permission fault. |
| I THLDW   | If execution is using the Realm EL1&0 translation regime, a Guarded Control Stack data access is allowed to access physical memory that is not from the Realm physical address space.                        |