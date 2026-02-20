## D1.5 Process state, PSTATE

RSPCZF

Process state, or PSTATE, is an abstraction of process state information.

ILPKMT

All Arm instruction sets provide instructions that operate on elements of PSTATE.

IKXKMY

PSTATE includes all of the following:

- Fields that are meaningful only in AArch32 state.

- Fields that are meaningful only in AArch64 state.

- Fields that are meaningful in both Execution states.

IZHGST

PSTATE is defined in pseudocode as the PSTATE structure, of type ProcState .

## D1.5.1 PSTATE fields that are meaningful in AArch64 state

ILLLXL

PSTATE fields that are meaningful in AArch64 state are grouped into the following categories:

- Condition flags.
- Execution state controls.
- Exception mask bits.
- Access control bits.
- Timing control bits.
- Speculation control bits.

RPCDTX

The following PSTATE bits are meaningful in AArch64 state:

| PSTATE field name                        | PSTATE field group       | Required implemented feature   | Value when a Warm reset is asserted                                                                                                                      | Additional details                                                  |
|------------------------------------------|--------------------------|--------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------|
| N, Negative condition flag               | Condition flags          | -                              | -                                                                                                                                                        | -                                                                   |
| Z, Zero condition flag                   | Condition flags          | -                              | -                                                                                                                                                        | -                                                                   |
| C, Carry condition flag                  | Condition flags          | -                              | -                                                                                                                                                        | -                                                                   |
| V, Overflow condition flag               | Condition flags          | -                              | -                                                                                                                                                        | -                                                                   |
| SS, Software Step bit                    | Execution state controls | -                              | 0                                                                                                                                                        | -                                                                   |
| IL, Illegal Execution state bit          | Execution state controls | -                              | 0                                                                                                                                                        | -                                                                   |
| nRW, Current Execution state bit         | Execution state controls | -                              | 0                                                                                                                                                        | If the current Execution state is AArch64, the PSTATE.nRW bit is 0. |
| EL, Current Exception level field        | Execution state controls | -                              | When a Warm reset is asserted into an Exception level using AArch64, the PSTATE.EL field holds the encoding for the highest implemented Exception level. | -                                                                   |
| SP, Stack pointer register selection bit | Execution state controls | -                              | 1                                                                                                                                                        | -                                                                   |
| D, Debug exception mask bit              | Exception mask bits      | -                              | 1                                                                                                                                                        | -                                                                   |
| A, I, F Asynchronous exception mask bits | Exception mask bits      | -                              | 1                                                                                                                                                        | -                                                                   |

| PSTATE field name                            | PSTATE field group       | Required implemented feature   | Value when a Warm reset is asserted   | Additional details   |
|----------------------------------------------|--------------------------|--------------------------------|---------------------------------------|----------------------|
| ALLINT, All interrupt mask bit               | Exception mask bits      | FEAT_NMI                       | -                                     | -                    |
| PAN, Privileged Access Never state bit       | Access control bits      | FEAT_PAN                       | -                                     | -                    |
| UAO, User Access Override bit                | Access control bits      | FEAT_UAO                       | -                                     | -                    |
| TCO, Tag Check Override bit                  | Access control bits      | FEAT_MTE                       | -                                     | -                    |
| BTYPE, Branch target identification bit      | Access control bits      | FEAT_BTI                       | -                                     | -                    |
| DIT, Data Independent Timing bit             | Timing control bits      | FEAT_DIT                       | 0                                     | -                    |
| SSBS, Speculative Store Bypass Safe bit      | Speculation control bits | FEAT_SSBS                      | IMPLEMENTATION DEFINED                | -                    |
| PM, PMUexception mask                        | Exception mask bits      | FEAT_EBEP                      | -                                     | -                    |
| PPEND, PMUexception pending                  | Access control bits      | FEAT_SEBEP                     | -                                     | -                    |
| EXLOCK, GCS exception state lock             | Access control bits      | FEAT_GCS                       | 0                                     | -                    |
| SM, Enables Streaming SVE mode               | Execution state controls | FEAT_SME                       | 0                                     | -                    |
| ZA, Enables SMEZAstorage                     | Access control bits      | FEAT_SME                       | 0                                     | -                    |
| PACM. PACM instruction executed              | Execution state controls | FEAT_PAuth_LR                  | 0                                     | -                    |
| UINJ, Inject Undefined Instruction exception | Execution state controls | FEAT_UINJ                      | 0                                     | -                    |

## D1.5.1.1 Accessing PSTATE fields

RLYGBS

In AArch64 state, PSTATE fields are accessed using Special-purpose registers that are directly read using the MRS (register) instructions, and directly written using the MSR (register) instructions.

RDGPCL

If in AArch64 state, the following Special-purpose registers can access the PSTATE fields that hold AArch64 state:

| Special-purpose register   | PSTATE fields   |
|----------------------------|-----------------|
| NZCV                       | N, Z, C,V       |
| DAIF                       | D, A, I, F      |
| CurrentEL                  | EL              |
| SPSel                      | SP              |
| PAN                        | PAN             |
| UAO                        | UAO             |
| DIT                        | DIT             |
| SSBS                       | SSBS            |
| TCO                        | TCO             |
| ALLINT                     | ALLINT          |
| PM                         | PM              |

| Special-purpose register   | PSTATE fields   |
|----------------------------|-----------------|
| SVCR                       | SM,ZA           |

All other PSTATE fields do not have direct read and write access.

Software can use the MSR (immediate) instructions to directly write to PSTATE.{D, A, I, F, SP, PAN, UAO, DIT, SSBS,

TCO, ALLINT, PM, SM, ZA}.

## RLDXKJ The following PSTATE fields can be accessed at EL0:

- PSTATE.{N, Z, C, V, SSBS, DIT, TCO, SM, ZA}.
- If SCTLR\_EL1.UMA is 1, and the Effective value of HCR\_EL2.{E2H, TGE} is not {1, 1}, PSTATE.{D, A, I, F}.
- PSTATE.{SM, ZA} access instructions can be executed at EL0 or higher.
- All other PSTATE access instructions can be executed at EL1 or higher and are UNDEFINED at EL0.

Writes to the PSTATE fields have side-effects on various aspects of the PE operation. For side-effects caused by writes to a PSTATE field, all of the following are true:

- The side-effect is guaranteed not to be visible to earlier instructions in the Execution stream.
- The side-effect is guaranteed to be visible to later instructions in the Execution stream.

Other side-effects might occur but are not guaranteed.

RBRSMZ

RHXYGT