## D24.2.62 HCR\_EL2, Hypervisor Configuration Register

The HCR\_EL2 characteristics are:

## Purpose

Provides configuration controls for virtualization, including defining whether various operations are trapped to EL2.

## Configuration

If EL2 is not implemented, this register is RES0 from EL3.

Unless otherwise stated, the bits in this register behave as if they are 0 for all purposes other than direct reads of the register if EL2 is not enabled in the current Security state.

AArch64 System register HCR\_EL2 bits [31:0] are architecturally mapped to AArch32 System register HCR[31:0].

AArch64 System register HCR\_EL2 bits [63:32] are architecturally mapped to AArch32 System register HCR2[31:0].

This register is present only when FEAT\_AA64 is implemented. Otherwise, direct accesses to HCR\_EL2 are UNDEFINED.

## Attributes

HCR\_EL2 is a 64-bit register.

## Field descriptions

<!-- image -->

## TWEDEL,bits [63:60]

## When FEAT\_TWED is implemented:

TWEDelay. A 4-bit unsigned number that, when HCR\_EL2.TWEDEn is 1, encodes the minimum delay in taking a trap of WFE* caused by HCR\_EL2.TWE as 2 (TWEDEL + 8) cycles.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

TWEDEn, bit [59]

## When FEAT\_TWED is implemented:

TWEDelay Enable. Enables a configurable delayed trap of the WFE* instruction caused by HCR\_EL2.TWE.

| TWEDEn   | Meaning                                                                                   |
|----------|-------------------------------------------------------------------------------------------|
| 0b0      | The delay for taking the trap is IMPLEMENTATION DEFINED.                                  |
| 0b1      | The delay for taking the trap is at least the number of cycles defined in HCR_EL2.TWEDEL. |

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## TID5, bit [58]

## When FEAT\_MTE2 is implemented:

Trap ID group 5. Traps the following register accesses to EL2, when EL2 is enabled in the current Security state:

## AArch64:

- GMID\_EL1.

| TID5   | Meaning                                                                |
|--------|------------------------------------------------------------------------|
| 0b0    | This control does not cause any instructions to be trapped.            |
| 0b1    | The specified EL1 accesses to ID group 5 registers are trapped to EL2. |

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## DCT, bit [57]

## When FEAT\_MTE2 is implemented:

Default Cacheability Tagging. When HCR\_EL2.DC is in effect, controls whether EL1&amp;0 stage 1 translations have the Tagged attribute.

| DCT   | Meaning                                                |
|-------|--------------------------------------------------------|
| 0b0   | Stage 1 translations do not have the Tagged attribute. |

| 0b1   | Stage 1 translations have the Tagged attribute.   |
|-------|---------------------------------------------------|

This bit is permitted to be cached in a TLB.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## ATA, bit [56]

## When FEAT\_MTE2 is implemented:

Memory tagging enable override:

- Overrides enabling of Memory tagging at EL1 and EL0.
- Accesses to the following registers at EL1 are trapped to EL2 and reported using EC syndrome value 0x18 :
- GCR\_EL1.
- RGSR\_EL1.
- TFSRE0\_EL1.
- TFSR\_EL1.
- Accesses with the register name TFSR\_EL2 that are not UNDEFINED.

| ATA   | Meaning                                                                                                                       |
|-------|-------------------------------------------------------------------------------------------------------------------------------|
| 0b0   | Disables the use of Memory tagging at EL1 and EL0. The specified registers are trapped to EL2.                                |
| 0b1   | This field has no effect on the use of Memory tagging at EL1 and EL0. The field does not trap the specified registers to EL2. |

The Effective value of this field is 1 when the Effective value of SCR\_EL3.ATA is 1 and any of the following are true:

- The Effective value of HCR\_EL2.{E2H, TGE} is {1, 1}.
- EL2 is not implemented or not enabled in the current Security state.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## TTLBOS, bit [55]

## When FEAT\_EVT is implemented:

Trap TLB maintenance instructions that operate on the Outer Shareable domain. Traps execution of those TLB maintenance instructions at EL1 using AArch64 to EL2, when EL2 is enabled in the current Security state. The following instructions are trapped and reported with EC syndrome value 0x18 :

- TLBI VMALLE1OS, TLBI VAE1OS, TLBI ASIDE1OS,TLBI VAAE1OS, TLBI VALE1OS, and TLBI VAALE1OS.
- If FEAT\_TLBIRANGE is implemented, TLBI RVAE1OS, TLBI RVAAE1OS,TLBI RVALE1OS, and TLBI RVAALE1OS.

- If FEAT\_XS is implemented, then the *OSNXS variants are also trapped.

| TTLBOS   | Meaning                                                     |
|----------|-------------------------------------------------------------|
| 0b0      | This control does not cause any instructions to be trapped. |
| 0b1      | Execution of the specified instructions are trapped to EL2. |

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## TTLBIS, bit [54]

## When FEAT\_EVT is implemented:

Trap TLB maintenance instructions that operate on the Inner Shareable domain. Traps execution of those TLB maintenance instructions at EL1 to EL2, when EL2 is enabled in the current Security state, as follows:

- If EL1 is using AArch64, then the following instructions are trapped to EL2 and reported with EC syndrome value 0x18 :
- TLBI VMALLE1IS, TLBI VAE1IS, TLBI ASIDE1IS, TLBI VAAE1IS, TLBI VALE1IS, TLBI VAALE1IS, TLBI RVAE1IS, TLBI RVAAE1IS, TLBI RVALE1IS, and TLBI RVAALE1IS.
- If EL1 is using AArch32, then the following instructions are trapped to EL2 and reported with EC syndrome value 0x03 :
- TLBIALLIS, TLBIMVAIS, TLBIASIDIS, TLBIMVAAIS, TLBIMVALIS, and TLBIMVAALIS.
- If FEAT\_XS is implemented, then the *ISNXS variants are also trapped.

| TTLBIS   | Meaning                                                     |
|----------|-------------------------------------------------------------|
| 0b0      | This control does not cause any instructions to be trapped. |
| 0b1      | Execution of the specified instructions are trapped to EL2. |

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## EnSCXT, bit [53]

## When FEAT\_CSV2\_2 is implemented or FEAT\_CSV2\_1p2 is implemented:

Enable Access to the SCXTNUM\_EL1 and SCXTNUM\_EL0 registers. The defined values are:

| EnSCXT   | Meaning                                                                                                                                                                                                                                                                                                                                                                                                                           |
|----------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0      | When EL2 is enabled in the current Security state, EL1 accesses to SCXTNUM_EL0 and SCXTNUM_EL1 are disabled, causing an exception to EL2, and the value of the registers to be treated as 0. When the Effective value of HCR_EL2.{E2H, TGE} is not {1, 1} and EL2 is enabled in the current Security state, EL0 access to SCXTNUM_EL0 is disabled, causing an exception to EL2, and the value of the register to be treated as 0. |
| 0b1      | This control does not cause accesses to SCXTNUM_EL0 or SCXTNUM_EL1 to be trapped.                                                                                                                                                                                                                                                                                                                                                 |

When the Effective value of HCR\_EL2.{E2H, TGE} is {1, 1} and the value of this field is 0, accesses at EL0 are not trapped by this control.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## TOCU, bit [52]

## When FEAT\_EVT is implemented:

Trap cache maintenance instructions that operate to the Point of Unification. Traps execution of those cache maintenance instructions at EL0 and EL1 to EL2, when EL2 is enabled in the current Security state, as follows:

- If EL0 is using AArch64, the value of SCTLR\_EL1.UCI is 1, and the Effective value of HCR\_EL2.{E2H, TGE} is not {1, 1}, then the following instructions at EL0 are trapped to EL2 and reported with EC syndrome value 0x18 :
- IC IVAU, and DC CVAU.
- If EL1 is using AArch64, then the following instructions at EL1 are trapped to EL2 and reported with EC syndrome value 0x18 :
- IC IVAU, IC IALLU, and DC CVAU.
- If EL1 is using AArch32, then the following instructions are trapped at EL1 to EL2 and reported with EC syndrome value 0x03 :
- ICIMVAU, ICIALLU, and DCCMVAU.

## Note

When SCTLR\_EL1.UCI is 0, the trap on execution of instructions at EL0 is higher priority than this control. An exception generated because an instruction is UNDEFINED at EL0 is higher priority than this trap to EL2. In addition:

- IC IALLUIS and IC IALLU are always UNDEFINED at EL0 using AArch64.
- ICIMVAU, ICIALLU, ICIALLUIS, and DCCMVAU are always UNDEFINED at EL0 using AArch32.

| TOCU   | Meaning                                                                                                                  |
|--------|--------------------------------------------------------------------------------------------------------------------------|
| 0b0    | This control does not cause any instructions to be trapped.                                                              |
| 0b1    | For each of the specified instructions, if the execution of the instruction can be trapped, accesses are trapped to EL2. |

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## AMVOFFEN,bit [51]

## When FEAT\_AMUv1p1 is implemented:

Activity Monitors Virtual Offsets Enable.

| AMVOFFEN   | Meaning                                                                                                       |
|------------|---------------------------------------------------------------------------------------------------------------|
| 0b0        | Virtualization of the Activity Monitors is disabled. Indirect reads of the virtual offset registers are zero. |
| 0b1        | Virtualization of the Activity Monitors is enabled.                                                           |

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## TICAB, bit [50]

## When FEAT\_EVT is implemented:

Trap ICIALLUIS and IC IALLUIS cache maintenance instructions. Traps execution of those cache maintenance instructions at EL1 to EL2, when EL2 is enabled in the current Security state, as follows:

- If EL1 is using AArch64, then the following instruction is trapped to EL2 and reported with EC syndrome value 0x18 :
- IC IALLUIS.
- If EL1 is using AArch32, then the following instruction is trapped to EL2 and reported with EC syndrome value 0x03 :
- ICIALLUIS.

| TICAB   | Meaning                                                                                                                   |
|---------|---------------------------------------------------------------------------------------------------------------------------|
| 0b0     | This control does not cause any instructions to be trapped.                                                               |
| 0b1     | For each of the specified instructions, if the execution of the instruction can be trapped, EL1 access is trapped to EL2. |

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## TID4, bit [49]

## When FEAT\_EVT is implemented:

Trap ID group 4. Traps the following register accesses to EL2, when EL2 is enabled in the current Security state:

AArch64:

- EL1 reads of CCSIDR\_EL1, CCSIDR2\_EL1, CLIDR\_EL1, and CSSELR\_EL1.
- EL1 writes to CSSELR\_EL1.

## AArch32:

- EL1 reads of CCSIDR, CCSIDR2, CLIDR, and CSSELR.
- EL1 writes to CSSELR.

| TID4   | Meaning                                                                |
|--------|------------------------------------------------------------------------|
| 0b0    | This control does not cause any instructions to be trapped.            |
| 0b1    | The specified EL1 accesses to ID group 4 registers are trapped to EL2. |

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## GPF, bit [48]

## When FEAT\_RME is implemented:

Controls the reporting of Granule protection faults at EL0 and EL1.

| GPF   | Meaning                                                                                                |
|-------|--------------------------------------------------------------------------------------------------------|
| 0b0   | This control does not cause exceptions to be routed from EL0 and EL1 to EL2.                           |
| 0b1   | Instruction Abort exceptions and Data Abort exceptions due to GPFs from EL0 and EL1 are routed to EL2. |

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## FIEN, bit [47]

## When FEAT\_RASv1p1 is implemented:

Fault Injection Enable. Unless this bit is set to 1, accesses to the ERXPFGCDN\_EL1, ERXPFGCTL\_EL1, and ERXPFGF\_EL1 registers from EL1 generate a Trap exception to EL2, when EL2 is enabled in the current Security state, reported using EC syndrome value 0x18 .

| FIEN   | Meaning                                                                                                             |
|--------|---------------------------------------------------------------------------------------------------------------------|
| 0b0    | Accesses to the specified registers from EL1 are trapped to EL2, when EL2 is enabled in the current Security state. |

| FIEN   | Meaning                                                     |
|--------|-------------------------------------------------------------|
| 0b1    | This control does not cause any instructions to be trapped. |

If EL2 is disabled in the current Security state, the Effective value of HCR\_EL2.FIEN is 1.

If ERRIDR\_EL1.NUM is zero, meaning no error records are implemented, or no error record accessible using System registers is owned by a node that implements the RAS Common Fault Injection Model Extension, then this bit might be RES0.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## FWB, bit [46]

## When FEAT\_S2FWB is implemented:

Forced Write-Back. Defines the combined cacheability attributes in a 2 stage translation regime.

| FWB   | Meaning                                                                                                                                                                                                                                                 |
|-------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0   | When this bit is 0, then the combination of stage 1 and stage 2 translations on memory type and cacheability attributes are as described in the Armv8.0 architecture. For more information, see 'Combining stage 1 and stage 2 memory type attributes'. |
| 0b1   | When this bit is 1, then the encoding of the stage 2 memory type and cacheability attributes in bits[5:2] of the stage 2 Page or Block descriptors are as described in 'Stage 2 memory type and Cacheability attributes when FEAT_S2FWB is enabled'.    |

In Secure state, this bit applies to both the Secure stage 2 translation and the Non-secure stage 2 translation.

This bit is permitted to be cached in a TLB.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## NV2, bit [45]

## When FEAT\_NV2 is implemented:

Nested Virtualization. Changes the behaviors of HCR\_EL2.{NV1, NV} to provide a mechanism for hardware to transform reads and writes from System registers into reads and writes from memory.

| NV2   | Meaning                                                                                                                   |
|-------|---------------------------------------------------------------------------------------------------------------------------|
| 0b0   | This bit has no effect on the behavior of HCR_EL2.{NV1, NV}. The behavior of HCR_EL2.{NV1, NV} is as defined for FEAT_NV. |

| NV2   | Meaning                                                                                                                                                                                                                                                                           |
|-------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b1   | Redefines behavior of HCR_EL2{NV1, NV} to enable: • Transformation of read/writes to registers into read/writes to memory. • Redirection of EL2 registers to EL1 registers. Any exception taken from EL1 and taken to EL1 causes SPSR_EL1.M[3:2] to be set to 0b10 and not 0b01 . |

When the Effective value of HCR\_EL2.NV is 0, the Effective value of this field is 0 and this field is treated as 0 for all purposes other than direct reads and writes of this field.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## AT, bit [44]

## When FEAT\_NV is implemented:

Address Translation. EL1 execution of the following address translation instructions is trapped to EL2, when EL2 is enabled in the current Security state, reported using EC syndrome value 0x18 :

- AT S1E0R, AT S1E0W, AT S1E1R, AT S1E1W, AT S1E1RP, and AT S1E1WP.
- If FEAT\_ATS1A is implemented, AT S1E1A.

| AT   | Meaning                                                        |
|------|----------------------------------------------------------------|
| 0b0  | This control does not cause any instructions to be trapped.    |
| 0b1  | EL1 execution of the specified instructions is trapped to EL2. |

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## NV1, bit [43]

## When FEAT\_NV2 is implemented:

Nested Virtualization.

| NV1   | Meaning                                                                                                                                                                                                                                                                                   |
|-------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0   | If the Effective value of HCR_EL2.{NV2, NV} is {1, 1}, accesses executed from EL1 to implemented EL12, EL02, or EL2 registers are transformed to loads and stores. If the Effective value of HCR_EL2.{NV2, NV} is not {1, 1}, this control does not cause any instructions to be trapped. |

| NV1   | Meaning                                                                                                                                                                                                                                                                                                                                                                                                                      |
|-------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b1   | If the Effective value of HCR_EL2.NV2 is 1, accesses executed from EL1 to implemented EL2 registers are transformed to loads and stores. If the Effective value of HCR_EL2.NV2 is 0, EL1 accesses to VBAR_EL1, ELR_EL1, SPSR_EL1, and, when FEAT_CSV2_2 or FEAT_CSV2_1p2 is implemented, SCXTNUM_EL1, are trapped to EL2, when EL2 is enabled in the current Security state, and are reported using EC syndrome value 0x18 . |

If the Effective value of HCR\_EL2.NV2 is 1, the Effective value of HCR\_EL2.NV1 defines which EL1 register accesses are transformed to loads and stores.

The trapping of EL1 registers caused by other control bits has priority over the transformation of these accesses.

If a register is specified that is not implemented by an implementation, then access to that register are UNDEFINED.

For the list of registers affected, see 'Enhanced support for nested virtualization'.

If the Effective value of HCR\_EL2.{NV1, NV} is {0, 1}, any exception taken from EL1, and taken to EL1, causes the SPSR\_EL1.M[3:2] to be set to 0b10 , and not 0b01 .

If the Effective value of HCR\_EL2.{NV1, NV} is {1, 1}, then:

- The EL1 translation table Block and Page descriptors:
- Bit[54] holds the PXN instead of the UXN.
- The Effective value of UXN is 0.
- Bit[53] is RES0.
- Bit[6] is treated as 0 regardless of the actual value.
- If Hierarchical Permissions are enabled, the EL1 translation table Table descriptors are as follows:
- Bit[61] is treated as 0 regardless of the actual value.
- Bit[60] holds the PXNTable instead of the UXNTable.
- Bit[59] is RES0.
- When executing at EL1, the Effective value of PSTATE.PAN is 0 for all purposes except reading the value of the bit.
- When executing at EL1, the Effective value of PSTATE.UAO is 1 for all purposes except reading the value of the bit.

If the Effective value of HCR\_EL2.{NV1, NV} are {1, 0}, then the behavior is a CONSTRAINED UNPREDICTABLE choice of:

- Behaving as if the Effective value of HCR\_EL2.{NV1, NV} is {1, 1} for all purposes other than reading back the value of the HCR\_EL2.NV bit.
- Behaving as if the Effective value of HCR\_EL2.{NV1, NV} is {0, 0} for all purposes other than reading back the value of the HCR\_EL2.NV1 bit.
- Behaving with regard to the Effective value of HCR\_EL2.{NV1, NV} behavior as defined in the rest of this description.

This bit is permitted to be cached in a TLB.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## When FEAT\_NV is implemented:

Nested Virtualization. EL1 accesses to certain registers are trapped to EL2, when EL2 is enabled in the current Security state.

| NV1   | Meaning                                                                                                                                                                                                                                 |
|-------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0   | This control does not cause any instructions to be trapped.                                                                                                                                                                             |
| 0b1   | EL1 accesses to VBAR_EL1, ELR_EL1, SPSR_EL1, and, when FEAT_CSV2_2 or FEAT_CSV2_1p2 is implemented, SCXTNUM_EL1, are trapped to EL2, when EL2 is enabled in the current Security state, and are reported using EC syndrome value 0x18 . |

If the Effective value of HCR\_EL2.{NV1, NV} is {0, 1}, then the following effects also apply:

- Any exception taken from EL1, and taken to EL1, causes the SPSR\_EL1.M[3:2] to be set to 0b10 , and not 0b01 .

If the Effective value of HCR\_EL2.{NV1, NV} is {1, 1}, then the following effects also apply:

- The EL1 translation table Block and Page descriptors:
- Bit[54] holds the PXN instead of the UXN.
- The Effective value of UXN is 0.
- Bit[53] is RES0.
- Bit[6] is treated as 0 regardless of the actual value.
- If Hierarchical Permissions are enabled, the EL1 translation table Table descriptors are as follows:
- Bit[61] is treated as 0 regardless of the actual value.
- Bit[60] holds the PXNTable instead of the UXNTable.
- Bit[59] is RES0.
- When executing at EL1, the Effective value of PSTATE.PAN is 0 for all purposes except reading the value of the bit.
- When executing at EL1, the Effective value of PSTATE.UAO is 1 for all purposes except reading the value of the bit.

If the Effective value of HCR\_EL2.{NV1, NV} is {1, 0}, then the behavior is a CONSTRAINED UNPREDICTABLE choice of:

- Behaving as if the Effective value of HCR\_EL2.{NV1, NV} is {1, 1} for all purposes other than reading back the value of the HCR\_EL2.NV bit.
- Behaving as if the Effective value of HCR\_EL2.{NV1, NV} is {0, 0} for all purposes other than reading back the value of the HCR\_EL2.NV1 bit.
- Behaving with regard to the Effective value of HCR\_EL2.{NV1, NV} behavior as defined in the rest of this description.

This bit is permitted to be cached in a TLB.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## NV, bit [42]

## When FEAT\_NV2 is implemented:

Nested Virtualization.

When the Effective value of HCR\_EL2.NV2 is 1, redefines register accesses so that:

- Instructions accessing the Special purpose registers SPSR\_EL2 and ELR\_EL2 instead access SPSR\_EL1 and ELR\_EL1 respectively.
- Instructions accessing the System registers ESR\_EL2 and FAR\_EL2 instead access ESR\_EL1 and FAR\_EL1.

When the Effective value of HCR\_EL2.NV2 is 0, traps functionality that is permitted at EL2 and would be UNDEFINED at EL1 if this field was 0, when EL2 is enabled in the current Security state. This applies to the following operations:

- EL1 accesses to Special-purpose registers that are not UNDEFINED at EL2.
- EL1 accesses to System registers that are not UNDEFINED at EL2.
- Execution of EL1 or EL2 translation regime address translation and TLB maintenance instructions for EL2 and above.

| NV   | Meaning                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0  | When this bit is set to 0, then the PE behaves as if the Effective value of HCR_EL2.NV2 is 0 for all purposes other than reading this register. This control does not cause any instructions to be trapped. When the Effective value of HCR_EL2.NV2 is 1, no FEAT_NV2 functionality is implemented.                                                                                                                                                                                                                    |
| 0b1  | When the Effective value of HCR_EL2.NV2 is 0, EL1 accesses to the specified registers or the execution of the specified instructions are trapped to EL2, when EL2 is enabled in the current Security state. EL1 read accesses to the CurrentEL register return a value of 0x2 . When the Effective value of HCR_EL2.NV2 is 1, this control redefines EL1 register accesses so that instructions accessing SPSR_EL2, ELR_EL2, ESR_EL2, and FAR_EL2 instead access SPSR_EL1, ELR_EL1, ESR_EL1, and FAR_EL1 respectively. |

When the Effective value of HCR\_EL2.NV2 is 0, then:

- The System or Special-purpose registers for which accesses are trapped and reported using EC syndrome value 0x18 are as follows:
- Registers accessed using MRS or MSR with a name ending in \_EL2, except the following:
- SP\_EL2.
- If FEAT\_MEC is implemented, MECID\_A0\_EL2, MECID\_A1\_EL2, MECID\_P0\_EL2, MECID\_P1\_EL2, MECIDR\_EL2, VMECID\_A\_EL2, and VMECID\_P\_EL2.
- Registers accessed using MRS or MSR with a name ending in \_EL12.
- Registers accessed using MRS or MSR with a name ending in \_EL02.
- Special-purpose registers SPSR\_irq, SPSR\_abt, SPSR\_und, and SPSR\_fiq, accessed using MRS or MSR.
- Special-purpose register SP\_EL1 accessed using the dedicated MRS or MSR instruction.
- The instructions for which the execution is trapped and reported using EC syndrome value 0x18 are as follows:
- EL2 translation regime Address Translation instructions and TLB maintenance instructions.
- EL1 translation regime Address Translation instructions and TLB maintenance instructions that are accessible only from EL2 and EL3.
- The instructions for which the execution is trapped as follows:
- SMCin an implementation that does not include EL3 and when HCR\_EL2.TSC is 1. HCR\_EL2.TSC bit is not RES0 in this case. This is reported using EC syndrome value 0x17 .
- The ERET, ERETAA, and ERETAB instructions, reported using EC syndrome value 0x1A .

## Note

The priority of this trap is higher than the priority of the HCR\_EL2.API trap. If both of these bits are set so that EL1 execution of an ERETAA or ERETAB instruction is trapped to EL2, then the syndrome reported is 0x1A .

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## When FEAT\_NV is implemented:

Nested Virtualization. Traps functionality that is permitted at EL2 and would be UNDEFINED at EL1 if this field was 0, when EL2 is enabled in the current Security state. This applies to the following operations:

- EL1 accesses to Special-purpose registers that are not UNDEFINED at EL2.
- EL1 accesses to System registers that are not UNDEFINED at EL2.
- Execution of EL1 or EL2 translation regime address translation and TLB maintenance instructions for EL2 and above.

| NV   | Meaning                                                                                                                                                                                                                           |
|------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0  | This control does not cause any instructions to be trapped.                                                                                                                                                                       |
| 0b1  | EL1 accesses to the specified registers or the execution of the specified instructions are trapped to EL2, when EL2 is enabled in the current Security state. EL1 read accesses to the CurrentEL register return a value of 0x2 . |

The System or Special-purpose registers for which accesses are trapped and reported using EC syndrome value 0x18 are as follows:

- Registers accessed using MRS or MSR with a name ending in \_EL2, except the following:
- SP\_EL2.
- If FEAT\_MEC is implemented, MECID\_A0\_EL2, MECID\_A1\_EL2, MECID\_P0\_EL2, MECID\_P1\_EL2, MECIDR\_EL2, VMECID\_A\_EL2, and VMECID\_P\_EL2.
- Registers accessed using MRS or MSR with a name ending in \_EL12.
- Registers accessed using MRS or MSR with a name ending in \_EL02.
- Special-purpose registers SPSR\_irq, SPSR\_abt, SPSR\_und, and SPSR\_fiq, accessed using MRS or MSR.
- Special-purpose register SP\_EL1 accessed using the dedicated MRS or MSR instruction.

The instructions for which the execution is trapped and reported using EC syndrome value 0x18 are as follows:

- EL2 translation regime Address Translation instructions and TLB maintenance instructions.
- EL1 translation regime Address Translation instructions and TLB maintenance instructions that are accessible only from EL2 and EL3.

The execution of the ERET, ERETAA, and ERETAB instructions are trapped and reported using EC syndrome value 0x1A .

Note

The priority of this trap is higher than the priority of the HCR\_EL2.API trap. If both of these bits are set so that EL1 execution of an ERETAA or ERETAB instruction is trapped to EL2, then the syndrome reported is 0x1A .

The execution of the SMC instructions in an implementation that does not include EL3 and when HCR\_EL2.TSC is 1 are trapped and reported using EC syndrome value 0x17 . HCR\_EL2.TSC bit is not RES0 in this case.

This bit is permitted to be cached in a TLB.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## API, bit [41]

## When FEAT\_PAuth is implemented:

Controls the use of instructions related to Pointer Authentication:

- PACGA.
- AUTDA, AUTDB, AUTDZA, AUTDZB, AUTIA, AUTIA1716, AUTIASP, AUTIAZ, AUTIB, AUTIB1716, AUTIBSP, AUTIBZ, AUTIZA, AUTIZB.
- PACDA, PACDB, PACDZA, PACDZB, PACIA, PACIA1716, PACIASP, PACIAZ, PACIB, PACIB1716, PACIBSP, PACIBZ, PACIZA, PACIZB.
- RETAA, RETAB, BRAA, BRAB, BLRAA, BLRAB, BRAAZ, BRABZ, BLRAAZ, BLRABZ.

- ERETAA, ERETAB, LDRAA, and LDRAB.
- When FEAT\_PAuth\_LR is implemented, AUTIASPPC, AUTIASPPCR, AUTIA171615, AUTIBSPPC, AUTIBSPPCR, AUTIB171615, PACIASPPC, PACNBIASPPC, PACIA171615, PACIBSPPC, PACNBIBSPPC, PACIB171615, RETAASPPC, RETAASPPCR, RETABSPPC, RETABSPPCR.

This field is ignored if the instruction is disabled as a result of the SCTLR\_ELx.{EnIB, EnIA, EnDA, EnDB} fields.

| API   | Meaning                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|-------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0   | The instructions related to Pointer Authentication are trapped to EL2 and reported using EC syndrome value 0x09 , when EL2 is enabled in the current Security state and the instructions are enabled for the EL1&0 translation regime, from: • When the Effective value of HCR_EL2.{E2H, TGE} is not {1, 1}, EL0. • EL1. If the Effective value of HCR_EL2.NV is 1, the HCR_EL2.NV trap takes precedence over the HCR_EL2.API trap for the ERETAA and ERETAB instructions. If EL2 is implemented and enabled in the current Security state and the Effective value of HFGITR_EL2.ERET is 1, execution at EL1 using AArch64 of ERETAA or ERETAB instructions is reported with EC syndrome value 0x1A with its associated ISS field, as the fine-grained trap has higher priority than the trap enabled by HCR_EL2.API == 0. |
| 0b1   | This control does not cause any instructions to be trapped.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |

If FEAT\_PAuth is implemented but EL2 is not implemented or is disabled in the current Security state, the system behaves as if this bit is 1.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## APK, bit [40]

## When FEAT\_PAuth is implemented:

Trap registers holding 'key' values for Pointer Authentication. Traps accesses to the following registers from EL1 to EL2, when EL2 is enabled in the current Security state, reported using EC syndrome value 0x18 :

- APIAKeyLo\_EL1, APIAKeyHi\_EL1, APIBKeyLo\_EL1, APIBKeyHi\_EL1, APDAKeyLo\_EL1, APDAKeyHi\_EL1, APDBKeyLo\_EL1, APDBKeyHi\_EL1, APGAKeyLo\_EL1, and APGAKeyHi\_EL1.

| APK   | Meaning                                                                                                                                                 |
|-------|---------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0   | Access to the registers holding 'key' values for pointer authentication from EL1 are trapped to EL2, when EL2 is enabled in the current Security state. |
| 0b1   | This control does not cause any instructions to be trapped.                                                                                             |

Note

If FEAT\_PAuth is implemented but EL2 is not implemented or is disabled in the current Security state, the system behaves as if this bit is 1.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## Bits [39:38]

Reserved, RES0.

## TEA, bit [37]

## When FEAT\_RAS is implemented:

Route synchronous External abort exceptions to EL2.

| TEA   | Meaning                                                                                                                                                                                |
|-------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0   | Synchronous External abort exceptions are unaffected by this mechanism. That is, synchronous External abort exceptions are not taken to EL2 unless routed to EL2 by another control.   |
| 0b1   | When executing at Exception levels below EL2, and EL2 is enabled in the current Security state, synchronous External abort exceptions are taken to EL2, unless they are routed to EL3. |

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## TERR, bit [36]

## When FEAT\_RAS is implemented:

Trap accesses of Error Record registers. Enables a trap to EL2 on accesses of Error Record registers.

| TERR   | Meaning                                                                                                                                   |
|--------|-------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0    | Accesses of the specified Error Record registers are not trapped by this mechanism.                                                       |
| 0b1    | Accesses of the specified Error Record registers at EL1 are trapped to EL2, unless the instruction generates a higher priority exception. |

In AArch64 state, the instructions affected by this control are:

- MRS and MSR accesses to ERRSELR\_EL1, ERXADDR\_EL1, ERXCTLR\_EL1, ERXMISC0\_EL1, ERXMISC1\_EL1, and ERXSTATUS\_EL1.
- MRS accesses to ERRIDR\_EL1 and ERXFR\_EL1.
- If FEAT\_RASv1p1 is implemented, MRS and MSR accesses to ERXMISC2\_EL1 and ERXMISC3\_EL1.
- If FEAT\_RASv2 is implemented, MRS accesses to ERXGSR\_EL1.

In AArch32 state, the instructions affected by this control are:

- accesses to ERRSELR, ERXADDR, ERXADDR2, ERXCTLR, ERXCTLR2,
- MRC and MCR ERXMISC0, ERXMISC1, ERXMISC2, ERXMISC3, and ERXSTATUS.
- MRC accesses to ERRIDR, ERXFR, and ERXFR2.

- If FEAT\_RASv1p1 is implemented, MRC and MCR accesses to ERXMISC4, ERXMISC5, ERXMISC6, and ERXMISC7.

Unless the instruction generates a higher priority exception, trapped instructions generate an exception to EL2.

Trapped AArch64 instructions are reported using EC syndrome value 0x18 .

Trapped AArch32 instructions are reported using EC syndrome value 0x03 .

Accessing this field has the following behavior:

- This field is permitted to be RES0 if all of the following are true:
- ERRSELR\_EL1 and all ERX* registers are implemented as UNDEFINED or RAZ/WI.
- ERRIDR\_EL1.NUM is zero.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## TLOR, bit [35]

## When FEAT\_LOR is implemented:

Trap LOR registers. Traps Non-secure and Realm EL1 accesses to LORSA\_EL1, LOREA\_EL1, LORN\_EL1, LORC\_EL1, and LORID\_EL1 registers to EL2.

| TLOR   | Meaning                                                                   |
|--------|---------------------------------------------------------------------------|
| 0b0    | This control does not cause any instructions to be trapped.               |
| 0b1    | Non-secure and Realm EL1 accesses to the LORregisters are trapped to EL2. |

When HCR\_EL2.TGE is 1, the PE ignores the value of this field for all purposes other than a direct read of this field.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## E2H, bit [34]

## When FEAT\_VHE is implemented:

EL2 Host. Enables a configuration where a Host Operating System is running in EL2, and the Host Operating System's applications are running in EL0.

| E2H   | Meaning                                                                |
|-------|------------------------------------------------------------------------|
| 0b0   | The facilities to support a Host Operating System at EL2 are disabled. |
| 0b1   | The facilities to support a Host Operating System at EL2 are enabled.  |

For information on the behavior of this bit see 'Behavior of HCR\_EL2.E2H'.

When FEAT\_E2H0 is not implemented, this field is RES1 and behaves as if it is 1 for all purposes other than a direct read.

This bit is permitted to be cached in a TLB.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## ID, bit [33]

Stage 2 Instruction access cacheability disable. For the EL1&amp;0 translation regime, when EL2 is enabled in the current Security state and HCR\_EL2.VM==1, this control forces all stage 2 translations for instruction accesses to Normal memory to be Non-cacheable.

| ID   | Meaning                                                                                        |
|------|------------------------------------------------------------------------------------------------|
| 0b0  | This control has no effect on stage 2 of the EL1&0 translation regime.                         |
| 0b1  | Forces all stage 2 translations for instruction accesses to Normal memory to be Non-cacheable. |

This bit has no effect on the EL2, EL2&amp;0, or EL3 translation regimes.

When the Effective value of HCR\_EL2.{E2H, TGE} is {1, 1}, the PE ignores the value of this field for all purposes other than a direct read of this field.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## CD, bit [32]

Stage 2 Data access cacheability disable. For the EL1&amp;0 translation regime, when EL2 is enabled in the current Security state and HCR\_EL2.VM==1, this control forces all stage 2 translations for data accesses and translation table walks to Normal memory to be Non-cacheable.

| CD   | Meaning                                                                                                              |
|------|----------------------------------------------------------------------------------------------------------------------|
| 0b0  | This control has no effect on stage 2 of the EL1&0 translation regime for data accesses and translation table walks. |
| 0b1  | Forces all stage 2 translations for data accesses and translation table walks to Normal memory to be Non-cacheable.  |

This bit has no effect on the EL2, EL2&amp;0, or EL3 translation regimes.

When the Effective value of HCR\_EL2.{E2H, TGE} is {1, 1}, the PE ignores the value of this field for all purposes other than a direct read of this field.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

RW, bit [31]

## When FEAT\_AA32EL1 is implemented:

Execution state control for lower Exception levels:

| RW   | Meaning                                                                                                                                     |
|------|---------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0  | Lower levels are all AArch32.                                                                                                               |
| 0b1  | The Execution state for EL1 is AArch64. The Execution state for EL0 is determined by the current value of PSTATE.nRW when executing at EL0. |

In an implementation that includes EL3, when EL2 is not enabled in Secure state, the PE behaves as if this bit has the same value as the SCR\_EL3.RW bit for all purposes other than a direct read or write access of HCR\_EL2.

The RW bit is permitted to be cached in a TLB.

When the Effective value of HCR\_EL2.{E2H, TGE} is {1, 1}, the Effective value of this field is 1.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RAO/WI.

## TRVM, bit [30]

Trap Reads of Virtual Memory controls. Traps reads of the virtual memory control registers to EL2, when EL2 is enabled in the current Security state, as follows:

- If EL1 is using AArch64, EL1 accesses to the following registers are trapped to EL2 and reported using EC syndrome value 0x18 for MRS and 0x14 for MRRS :
- SCTLR\_EL1, TTBR0\_EL1, TTBR1\_EL1, TCR\_EL1, ESR\_EL1, FAR\_EL1, AFSR0\_EL1, AFSR1\_EL1, MAIR\_EL1, AMAIR\_EL1, and CONTEXTIDR\_EL1.
- If FEAT\_AIE is implemented, MAIR2\_EL1 and AMAIR2\_EL1.
- If FEAT\_S1PIE is implemented, PIRE0\_EL1 and PIR\_EL1.
- If FEAT\_S1POE is implemented, POR\_EL0 and POR\_EL1.
- If FEAT\_S2POE is implemented, S2POR\_EL1.
- If FEAT\_TCR2 is implemented, TCR2\_EL1.
- If FEAT\_SCTLR2 is implemented, SCTLR2\_EL1.
- If the Effective value of HCR\_EL2.{E2H, TGE} is not {1, 1}, and EL0 is using AArch64, EL0 accesses to the following registers are trapped to EL2 and reported using EC syndrome value 0x18 for MRS :
- If FEAT\_S1POE is implemented, POR\_EL0.
- If EL1 is using AArch32, EL1 accesses using MRC to the following registers are trapped to EL2 and reported using EC syndrome value 0x03 , accesses using MRRC are trapped to EL2 and reported using EC syndrome value 0x04 :
- SCTLR, TTBR0, TTBR1, TTBCR, TTBCR2, DACR, DFSR, IFSR, DFAR, IFAR, ADFSR, AIFSR, PRRR, NMRR, MAIR0, MAIR1, AMAIR0, AMAIR1, and CONTEXTIDR.

| TRVM   | Meaning                                                                                                                                |
|--------|----------------------------------------------------------------------------------------------------------------------------------------|
| 0b0    | This control does not cause any instructions to be trapped.                                                                            |
| 0b1    | Read accesses to the specified Virtual Memory control registers are trapped to EL2, when EL2 is enabled in the current Security state. |

When the Effective value of HCR\_EL2.{E2H, TGE} is {1, 1}, the PE ignores the value of this field for all purposes other than a direct read of this field.

## Note

EL2 provides a second stage of address translation, that a hypervisor can use to remap the address map defined by a Guest OS. In addition, a hypervisor can trap attempts by a Guest OS to write to the registers that control the memory system. A hypervisor might use this trap as part of its virtualization of memory management.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## HCD, bit [29]

## When EL3 is not implemented:

HVCinstruction disable. Disables EL1 and EL2 execution of HVC instructions, from both Execution states, when EL2 is enabled in the current Security state, reported using EC syndrome value 0x00 .

| HCD   | Meaning                                                                                                                                        |
|-------|------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0   | HVCinstruction execution is enabled at EL2 and EL1.                                                                                            |
| 0b1   | HVCinstructions are UNDEFINED at EL2 and EL1. Any resulting exception is taken to the Exception level at which the HVCinstruction is executed. |

Note

HVCinstructions are always UNDEFINED at EL0.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## TDZ, bit [28]

Traps EL0 and EL1 execution of the following instructions to EL2, when EL2 is enabled in the current Security state, from AArch64 state only, reported using EC syndrome value 0x18 :

- DCZVA.
- If FEAT\_MTE is implemented, DC GVA and DC GZVA.

| TDZ   | Meaning                                                                                                                                                                                                                                                                                                                              |
|-------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0   | This control does not cause any instructions to be trapped.                                                                                                                                                                                                                                                                          |
| 0b1   | In AArch64 state, any attempt to execute an instruction this trap applies to at EL1, or at EL0 when the instruction is not UNDEFINED at EL0, is trapped to EL2 when EL2 is enabled in the current Security state. Reading the DCZID_EL0 returns a value that indicates that the instructions this trap applies to are not supported. |

When the Effective value of HCR\_EL2.{E2H, TGE} is {1, 1}, the Effective value of this field is 0.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## TGE, bit [27]

Trap General Exceptions, from EL0.

| TGE   | Meaning                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|-------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0   | This control has no effect on execution at EL0.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| 0b1   | When EL2 is not enabled in the current Security state, this control has no effect on execution at EL0. When EL2 is enabled in the current Security state, in all cases: • All exceptions that would be routed to EL1 are routed to EL2. • If EL1 is using AArch64, the SCTLR_EL1.M field is treated as being 0 for all purposes other than returning the result of a direct read of SCTLR_EL1. • If EL1 is using AArch32, the SCTLR.M field is treated as being 0 for all purposes other than returning the result of a direct read of SCTLR. • All virtual interrupts and virtual exceptions are disabled. • Any IMPLEMENTATION DEFINED mechanisms for signaling virtual interrupts are disabled. • An exception return to EL1 is treated as an illegal exception return. • The MDCR_EL2.{TDRA, TDOSA, TDA, TDE} fields are treated as being 1 for all purposes other than returning the result of a direct read of MDCR_EL2. In addition, when EL2 is enabled in the current Security state, if: • The Effective value of HCR_EL2.E2H is not 1, the Effective values of the HCR_EL2.{FMO, IMO, AMO}fields are 1. • The Effective value of HCR_EL2.E2H is 1, the Effective values of the HCR_EL2.{FMO, IMO, AMO}fields are 0. For further information on the behavior of this bit when the Effective value of E2H is 1, see 'Behavior of |

HCR\_EL2.TGE must not be cached in a TLB.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## TVM, bit [26]

Trap Virtual Memory controls. Traps writes to the virtual memory control registers to EL2, when EL2 is enabled in the current Security state, as follows:

- If EL1 is using AArch64, the following registers are trapped to EL2 and reported using EC syndrome value 0x18 for MSR and 0x14 for MSRR :
- SCTLR\_EL1, TTBR0\_EL1, TTBR1\_EL1, TCR\_EL1, ESR\_EL1, FAR\_EL1, AFSR0\_EL1, AFSR1\_EL1, MAIR\_EL1, AMAIR\_EL1, and CONTEXTIDR\_EL1.
- If FEAT\_AIE is implemented, MAIR2\_EL1 and AMAIR2\_EL1.
- If FEAT\_S1PIE is implemented, PIRE0\_EL1 and PIR\_EL1.
- If FEAT\_S1POE is implemented, POR\_EL0 and POR\_EL1.
- If FEAT\_S2POE is implemented, S2POR\_EL1.
- If FEAT\_TCR2 is implemented, TCR2\_EL1.
- If FEAT\_SCTLR2 is implemented, SCTLR2\_EL1.
- If the Effective value of HCR\_EL2.{E2H, TGE} is not {1, 1}, and EL0 is using AArch64, EL0 accesses to the following registers are trapped to EL2 and reported using EC syndrome value 0x18 for MSR :
- If FEAT\_S1POE is implemented, POR\_EL0.
- If EL1 is using AArch32, EL1 accesses using MCR to the following registers are trapped to EL2 and reported using EC syndrome value 0x03 , accesses using MCRR are trapped to EL2 and reported using EC syndrome value 0x04 :
- SCTLR, TTBR0, TTBR1, TTBCR, TTBCR2, DACR, DFSR, IFSR, DFAR, IFAR, ADFSR, AIFSR, PRRR, NMRR, MAIR0, MAIR1, AMAIR0, AMAIR1, and CONTEXTIDR.

| TVM   | Meaning                                                                                                                                 |
|-------|-----------------------------------------------------------------------------------------------------------------------------------------|
| 0b0   | This control does not cause any instructions to be trapped.                                                                             |
| 0b1   | Write accesses to the specified Virtual Memory control registers are trapped to EL2, when EL2 is enabled in the current Security state. |

When the Effective value of HCR\_EL2.{E2H, TGE} is {1, 1}, the PE ignores the value of this field for all purposes other than a direct read of this field.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## TTLB, bit [25]

Trap TLB maintenance instructions. Traps execution of TLB maintenance instructions at EL1 to EL2, when EL2 is enabled in the current Security state, as follows:

- If EL1 is using AArch64, then the following instructions are trapped to EL2 and reported using EC syndrome value 0x18 :
- TLBI VMALLE1, TLBI VAE1, TLBI ASIDE1, TLBI VAAE1, TLBI VALE1, and TLBI VAALE1.
- TLBI VMALLE1IS, TLBI VAE1IS, TLBI ASIDE1IS, TLBI VAAE1IS, TLBI VALE1IS, and TLBI VAALE1IS.
- If FEAT\_TLBIOS is implemented, TLBI VMALLE1OS, TLBI VAE1OS, TLBI ASIDE1OS, TLBI VAAE1OS, TLBI VALE1OS, and TLBI VAALE1OS.
- If FEAT\_TLBIRANGE is implemented, TLBI RVAE1, TLBI RVAAE1, TLBI RVALE1, TLBI RVAALE1, TLBI RVAE1IS, TLBI RVAAE1IS, TLBI RVALE1IS, and TLBI RVAALE1IS.
- If FEAT\_TLBIOS and FEAT\_TLBIRANGE are implemented, TLBI RVAE1OS, TLBI RVAAE1OS, TLBI RVALE1OS, and TLBI RVAALE1OS.
- If EL1 is using AArch32, then the following instructions are trapped to EL2 and reported using EC syndrome value 0x03 :
- TLBIALLIS, TLBIMVAIS, TLBIASIDIS, TLBIMVAAIS, TLBIMVALIS, and TLBIMVAALIS.
- TLBIALL, TLBIMVA, TLBIASID, TLBIMVAA, TLBIMVAL, and TLBIMVAAL
- ITLBIALL, ITLBIMVA, and ITLBIASID.
- DTLBIALL, DTLBIMVA, and DTLBIASID.

| TTLB   | Meaning                                                                                                                            |
|--------|------------------------------------------------------------------------------------------------------------------------------------|
| 0b0    | This control does not cause any instructions to be trapped.                                                                        |
| 0b1    | EL1 execution of the specified TLB maintenance instructions are trapped to EL2, when EL2 is enabled in the current Security state. |

When HCR\_EL2.TGE is 1, the PE ignores the value of this field for all purposes other than a direct read of this field.

| Note                                                   |
|--------------------------------------------------------|
| The TLB maintenance instructions are UNDEFINED at EL0. |

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## TPU, bit [24]

Trap cache maintenance instructions that operate to the Point of Unification. Traps execution of those cache maintenance instructions at EL0 and EL1 to EL2, when EL2 is enabled in the current Security state, as follows:

- If EL0 is using AArch64 and the value of SCTLR\_EL1.UCI is 1, then the following instructions at EL0 are trapped to EL2 and reported with EC syndrome value 0x18 :
- IC IVAU and DC CVAU.
- If EL1 is using AArch64, then the following instructions at EL1 are trapped to EL2 and reported with EC syndrome value 0x18 :
- IC IVAU, IC IALLU, IC IALLUIS, and DC CVAU.
- If EL1 is using AArch32, then the following instructions are trapped to EL2 and reported with EC syndrome value 0x03 :
- ICIMVAU, ICIALLU, ICIALLUIS, and DCCMVAU.

Note

When SCTLR\_EL1.UCI is 0, the trap on execution of instructions at EL0 is higher priority than this control. An exception generated because an instruction is UNDEFINED at EL0 is higher priority than this trap to EL2. In addition:

- IC IALLUIS and IC IALLU are always UNDEFINED at EL0 using AArch64.
- ICIMVAU, ICIALLU, ICIALLUIS, and DCCMVAU are always UNDEFINED at EL0 using AArch32.

| TPU   | Meaning                                                                                                                                                                  |
|-------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0   | This control does not cause any instructions to be trapped.                                                                                                              |
| 0b1   | For each of the specified instructions, if the execution of the instruction can be trapped, access is trapped to EL2, when EL2 is enabled in the current Security state. |

When the Effective value of HCR\_EL2.{E2H, TGE} is {1, 1}, the Effective value of this field is 0.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## TPCP, bit [23]

Trap data or unified cache maintenance instructions that operate to the Point of Coherency, Persistence, or Physical Storage. When EL2 is enabled in the current Security state, traps execution of cache maintenance instructions at EL0 and EL1 to EL2 as follows:

- If EL0 is using AArch64 and the value of SCTLR\_EL1.UCI is 1, then the following instructions at EL0 are trapped to EL2 and reported using EC syndrome value 0x18 :
- DCCIVAC and DC CVAC.
- If FEAT\_MTE is implemented, DC CIGVAC, DC CIGDVAC, DC CGVAC, and DC CGDVAC.
- If FEAT\_DPB is implemented, DC CVAP.
- If FEAT\_DPB and FEAT\_MTE are implemented, DC CGVAP and DC CGDVAP.
- If FEAT\_DPB2 is implemented, DC CVADP.
- If FEAT\_DPB2 and FEAT\_MTE are implemented, DC CGVADP and DC CGDVADP.
- If FEAT\_OCCMO is implemented, DC CIVAOC, DC CIGDVAOC, DC CVAOC and DC CGDVAOC.
- If EL1 is using AArch64, then the following instructions at EL1 are trapped to EL2 and reported using EC syndrome value 0x18 :
- DCIVAC, DC CIVAC and DC CVAC.
- If FEAT\_MTE is implemented, DC CIGVAC, DC CIGDVAC, DC IGVAC, DC IGDVAC, DC CGVAC, and DC CGDVAC.
- If FEAT\_DPB is implemented, DC CVAP.
- If FEAT\_DPB and FEAT\_MTE are implemented, DC CGVAP and DC CGDVAP.
- If FEAT\_DPB2 is implemented, DC CVADP.
- If FEAT\_DPB2 and FEAT\_MTE are implemented, DC CGVADP and DC CGDVADP.
- If FEAT\_PoPS is implemented, DC CIVAPS.
- If FEAT\_PoPS and FEAT\_MTE2 are implemented, DC CIGDVAPS.
- If FEAT\_OCCMO is implemented, DC CIVAOC, DC CIGDVAOC, DC CVAOC and DC CGDVAOC.
- If EL1 is using AArch32, then the following instructions at EL1 are trapped to EL2 and reported using EC syndrome value 0x03 :
- DCIMVAC, DCCIMVAC, and DCCMVAC.

Note

This field was previously named TPC.

When SCTLR\_EL1.UCI is 0, the trap on execution of instructions at EL0 is higher priority than this control. An exception generated because an instruction is UNDEFINED at EL0 is higher priority than this trap to EL2. In addition:

- AArch64 instructions which invalidate by VA to the Point of Coherency or Physical Storage are always UNDEFINED at EL0 using AArch64.
- DCIMVAC, DCCIMVAC, and DCCMVAC are always UNDEFINED at EL0 using AArch32.

| TPCP   | Meaning                                                                                                                                                              |
|--------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0    | This control does not cause any instructions to be trapped.                                                                                                          |
| 0b1    | For each of the specified instructions, if the execution of the instruction can be trapped, it is trapped to EL2, when EL2 is enabled in the current Security state. |

When the Effective value of HCR\_EL2.{E2H, TGE} is {1, 1}, the Effective value of this field is 0.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## TSW, bit [22]

Trap data or unified cache maintenance instructions that operate by Set/Way. Traps execution of those cache maintenance instructions at EL1 to EL2, when EL2 is enabled in the current Security state, as follows:

- If EL1 is using AArch64, then the following instructions are trapped to EL2 and reported with EC syndrome value 0x18 :
- DCISW, DC CSW, and DC CISW.
- If FEAT\_MTE2 is implemented, DC IGSW, DC IGDSW, DC CGSW, DC CGDW, DC CIGSW, and DCCIGDSW.
- If EL1 is using AArch32, then the following instructions are trapped to EL2 and reported with EC syndrome value 0x03 :
- DCISW, DCCSW, and DCCISW.

Note

An exception generated because an instruction is UNDEFINED at EL0 is higher priority than this trap to EL2, and these instructions are always UNDEFINED at EL0.

| TSW   | Meaning                                                                                                       |
|-------|---------------------------------------------------------------------------------------------------------------|
| 0b0   | This control does not cause any instructions to be trapped.                                                   |
| 0b1   | Execution of the specified instructions is trapped to EL2, when EL2 is enabled in the current Security state. |

When HCR\_EL2.TGE is 1, the PE ignores the value of this field for all purposes other than a direct read of this field.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## TACR, bit [21]

Trap Auxiliary Control Registers. Traps EL1 accesses to the Auxiliary Control Registers to EL2, when EL2 is enabled in the current Security state, as follows:

- If EL1 is using AArch64, accesses to ACTLR\_EL1 to EL2, are trapped to EL2 and reported using EC syndrome value 0x18 .
- If EL1 is using AArch32, accesses to ACTLR and, if implemented, ACTLR2 are trapped to EL2 and reported using EC syndrome value 0x03 .

| TACR   | Meaning                                                                                                        |
|--------|----------------------------------------------------------------------------------------------------------------|
| 0b0    | This control does not cause any instructions to be trapped.                                                    |
| 0b1    | EL1 accesses to the specified registers are trapped to EL2, when EL2 is enabled in the current Security state. |

When HCR\_EL2.TGE is 1, the PE ignores the value of this field for all purposes other than a direct read of this field.

Note

ACTLR\_EL1 is not accessible at EL0.

ACTLR and ACTLR2 are not accessible at EL0.

The Auxiliary Control Registers are IMPLEMENTATION DEFINED registers that might implement global control bits for the PE.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## TIDCP, bit [20]

Trap IMPLEMENTATION DEFINED functionality. Traps EL1 accesses to the encodings reserved for IMPLEMENTATION DEFINED functionality to EL2, when EL2 is enabled in the current Security state as follows:

- In AArch64 state, EL0 access to the encodings in the following reserved encoding spaces are trapped:
- IMPLEMENTATION DEFINED System instructions, which are accessed using SYS and SYSL, with CRn == {11, 15}, and are reported using EC syndrome value 0x18 .
- IMPLEMENTATION DEFINED System instructions, which are accessed using SYSP, with CRn == {11, 15}, and are reported using EC syndrome value 0x14 .
- IMPLEMENTATION DEFINED System registers, which are accessed using MRS and MSR with the S3\_&lt;op1&gt;\_&lt;Cn&gt;\_&lt;Cm&gt;\_&lt;op2&gt; register name, and are reported using EC syndrome 0x18 .
- IMPLEMENTATION DEFINED System registers, which are accessed using MRRS and MSRR with the S3\_&lt;op1&gt;\_&lt;Cn&gt;\_&lt;Cm&gt;\_&lt;op2&gt; register name, and are reported using EC syndrome 0x14 .
- In AArch32 state, MCR and MRC access to instructions with the following encodings are trapped and reported using EC syndrome value 0x03 :
- All coproc==p15, CRn==c9, opc1 == {0-7}, CRm == {c0-c2, c5-c8}, opc2 == {0-7}.
- All coproc==p15, CRn==c10, opc1 =={0-7}, CRm == {c0, c1, c4, c8}, opc2 == {0-7}.
- All coproc==p15, CRn==c11, opc1=={0-7}, CRm == {c0-c8, c15}, opc2 == {0-7}.

When this functionality is accessed from EL0:

- If FEAT\_TIDCP1 is implemented and the Effective value of SCTLR\_EL1.TIDCP is 1, any accesses from EL0 are trapped to EL1.
- Otherwise, if FEAT\_TIDCP1 is implemented and the Effective value of SCTLR\_EL2.TIDCP is 1, any accesses from EL0 are trapped to EL2.
- Otherwise:
- If HCR\_EL2.TIDCP is 1, it is IMPLEMENTATION DEFINED whether any accesses from EL0 are trapped to EL2.
- If HCR\_EL2.TIDCP is 0, any accesses from EL0 are UNDEFINED and generate an exception that is taken to EL1 or EL2.

| TIDCP   | Meaning                                                                                                                                                                          |
|---------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0     | This control does not cause any instructions to be trapped.                                                                                                                      |
| 0b1     | EL1 accesses to or execution of the specified encodings reserved for IMPLEMENTATION DEFINED functionality are trapped to EL2, when EL2 is enabled in the current Security state. |

An implementation can also include IMPLEMENTATION DEFINED registers that provide additional controls, to give finer-grained control of the trapping of IMPLEMENTATION DEFINED features.

Note

The trapping of accesses to these registers from EL1 is higher priority than an exception resulting from the register access being UNDEFINED.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## TSC, bit [19]

Trap SMC instructions. Traps EL1 execution of SMC instructions to EL2, when EL2 is enabled in the current Security state.

If execution is in AArch64 state, the trap is reported using EC syndrome value 0x17 .

If execution is in AArch32 state, the trap is reported using EC syndrome value 0x13 .

Note

HCR\_EL2.TSC traps execution of the SMC instruction. It is not a routing control for the SMC exception. Trap exceptions and SMC exceptions have different preferred return addresses.

| TSC   | Meaning                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|-------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0   | This control does not cause any instructions to be trapped.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| 0b1   | If EL3 is implemented, then any attempt to execute an SMC instruction at EL1 is trapped to EL2, when EL2 is enabled in the current Security state, regardless of the value of SCR_EL3.SMD. If EL3 is not implemented and the Effective value of HCR_EL2.NV is 1, then any attempt to execute an SMCinstruction at EL1 using AArch64 is trapped to EL2. If EL3 is not implemented and the Effective value of HCR_EL2.NV is 0, then it is IMPLEMENTATION DEFINED whether: • Any attempt to execute an SMCinstruction at EL1 is trapped to EL2, when EL2 is enabled in the current Security state. • Any attempt to execute an SMCinstruction is UNDEFINED. |

In AArch32 state, the Armv8-A architecture permits, but does not require, this trap to apply to conditional SMC instructions that fail their condition code check, in the same way as with traps on other conditional instructions.

SMC instructions are UNDEFINED at EL0.

If EL3 is not implemented, and the Effective value of HCR\_EL2.NV is 0, then it is IMPLEMENTATION DEFINED whether this bit is:

- RES0.
- Implemented with the functionality as described in HCR\_EL2.TSC.

When HCR\_EL2.TGE is 1, the PE ignores the value of this field for all purposes other than a direct read of this field.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## TID3, bit [18]

Trap ID group 3. Traps EL1 reads of group 3 ID registers to EL2, when EL2 is enabled in the current Security state, as follows:

## In AArch64 state:

- Reads of the following registers are trapped to EL2, reported using EC syndrome value 0x18 :
- ID\_PFR0\_EL1, ID\_PFR1\_EL1, ID\_DFR0\_EL1, ID\_AFR0\_EL1, ID\_MMFR0\_EL1, ID\_MMFR1\_EL1, ID\_MMFR2\_EL1, ID\_MMFR3\_EL1, ID\_ISAR0\_EL1, ID\_ISAR1\_EL1, ID\_ISAR2\_EL1, ID\_ISAR3\_EL1, ID\_ISAR4\_EL1, ID\_ISAR5\_EL1, MVFR0\_EL1, MVFR1\_EL1, and MVFR2\_EL1.
- ID\_AA64PFR0\_EL1, ID\_AA64PFR1\_EL1, ID\_AA64DFR0\_EL1, ID\_AA64DFR1\_EL1, ID\_AA64ISAR0\_EL1, ID\_AA64ISAR1\_EL1, ID\_AA64MMFR0\_EL1, ID\_AA64MMFR1\_EL1, ID\_AA64AFR0\_EL1, and ID\_AA64AFR1\_EL1.
- If FEAT\_FGT is implemented, reads of the following registers are trapped to EL2. If FEAT\_FGT is not implemented, reads of the following registers are trapped to EL2, unless the registers are implemented as RAZ, when it is IMPLEMENTATION DEFINED whether accesses are trapped to EL2.
- ID\_PFR2\_EL1, ID\_MMFR4\_EL1 and ID\_MMFR5\_EL1.
- ID\_AA64MMFR3\_EL1.
- ID\_AA64MMFR4\_EL1.
- ID\_AA64PFR2\_EL1.
- ID\_AA64MMFR2\_EL1 and ID\_ISAR6\_EL1.
- ID\_DFR1\_EL1.
- ID\_AA64ZFR0\_EL1.
- ID\_AA64SMFR0\_EL1.
- ID\_AA64ISAR2\_EL1.
- If FEAT\_FGT is implemented, this field traps all MRS accesses to registers in the following range that are not already mentioned in this field description: op0 == 3, op1 == 0, CRn == 0, CRm == {2-7}, op2 == {0-7}. If FEAT\_FGT is not implemented, it is IMPLEMENTATION DEFINED whether this field traps accesses to registers in the range.

## In AArch32 state:

- VMRSaccess to MVFR0, MVFR1, and MVFR2, are trapped to EL2, reported using EC syndrome value 0x08 , unless access is also trapped by HCPTR which takes priority.
- MRCaccess to the following registers are trapped to EL2, reported using EC syndrome value 0x03 :
- ID\_PFR0, ID\_PFR1, ID\_PFR2, ID\_DFR0, ID\_AFR0, ID\_MMFR0, ID\_MMFR1, ID\_MMFR2, ID\_MMFR3, ID\_ISAR0, ID\_ISAR1, ID\_ISAR2, ID\_ISAR3, ID\_ISAR4, and ID\_ISAR5.
- If FEAT\_FGT is implemented:
- ID\_MMFR4 and ID\_MMFR5.
- ID\_ISAR6.
- ID\_DFR1.
- This field traps all MRC accesses to encodings in the following range that are not already mentioned in this field description: coproc == p15, opc1 == 0, CRn == c0, CRm == {c2-c7}, opc2 == {0-7}.
- If FEAT\_FGT is not implemented:
- ID\_MMFR4 and ID\_MMFR5 are trapped to EL2, unless implemented as RAZ, when it is IMPLEMENTATION DEFINED whether accesses to ID\_MMFR4 or ID\_MMFR5 are trapped.
- ID\_ISAR6 is trapped to EL2, unless implemented as RAZ, when it is IMPLEMENTATION DEFINED whether accesses to ID\_ISAR6 are trapped to EL2.
- ID\_DFR1 is trapped to EL2, unless implemented as RAZ, when it is IMPLEMENTATION DEFINED whether accesses to ID\_DFR1 are trapped to EL2.
- Otherwise, it is IMPLEMENTATION DEFINED whether this bit traps all MRC accesses to registers in the following range not already mentioned in this field description with coproc == p15, opc1 == 0, CRn == c0, CRm == {c2-c7}, opc2 == {0-7}.

| TID3   | Meaning                                                                                                                        |
|--------|--------------------------------------------------------------------------------------------------------------------------------|
| 0b0    | This control does not cause any instructions to be trapped.                                                                    |
| 0b1    | The specified EL1 read accesses to ID group 3 registers are trapped to EL2, when EL2 is enabled in the current Security state. |

When HCR\_EL2.TGE is 1, the PE ignores the value of this field for all purposes other than a direct read of this field.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## TID2, bit [17]

Trap ID group 2. Traps the following register accesses to EL2, when EL2 is enabled in the current Security state, as follows:

- If EL1 is using AArch64, reads of CTR\_EL0, CCSIDR\_EL1, CCSIDR2\_EL1, CLIDR\_EL1, and CSSELR\_EL1 are trapped to EL2, reported using EC syndrome value 0x18 .
- If EL0 is using AArch64 and the value of SCTLR\_EL1.UCT is not 0, reads of CTR\_EL0 are trapped to EL2, reported using EC syndrome value 0x18 . If the value of SCTLR\_EL1.UCT is 0, then EL0 reads of CTR\_EL0 are trapped to EL1 and the resulting exception takes precedence over this trap.
- If EL1 is using AArch64, writes to CSSELR\_EL1 are trapped to EL2, reported using EC syndrome value 0x18 .
- If EL1 is using AArch32, reads of CTR, CCSIDR, CCSIDR2, CLIDR, and CSSELR are trapped to EL2, reported using EC syndrome value 0x03 .
- If EL1 is using AArch32, writes to CSSELR are trapped to EL2, reported using EC syndrome value 0x03 .

| TID2   | Meaning                                                                                                                           |
|--------|-----------------------------------------------------------------------------------------------------------------------------------|
| 0b0    | This control does not cause any instructions to be trapped.                                                                       |
| 0b1    | The specified EL1 and EL0 accesses to ID group 2 registers are trapped to EL2, when EL2 is enabled in the current Security state. |

When the Effective value of HCR\_EL2.{E2H, TGE} is {1, 1}, the Effective value of this field is 0.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## TID1, bit [16]

Trap ID group 1. Traps EL1 reads of the following registers to EL2, when EL2 is enabled in the current Security state as follows:

- In AArch64 state, accesses of REVIDR\_EL1, AIDR\_EL1, and SMIDR\_EL1, reported using EC syndrome value 0x18 .
- In AArch32 state, accesses of TCMTR, TLBTR, REVIDR, and AIDR, reported using EC syndrome value 0x03 .

| TID1   | Meaning                                                     |
|--------|-------------------------------------------------------------|
| 0b0    | This control does not cause any instructions to be trapped. |

| TID1   | Meaning                                                                                                                        |
|--------|--------------------------------------------------------------------------------------------------------------------------------|
| 0b1    | The specified EL1 read accesses to ID group 1 registers are trapped to EL2, when EL2 is enabled in the current Security state. |

When HCR\_EL2.TGE is 1, the PE ignores the value of this field for all purposes other than a direct read of this field.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## TID0, bit [15]

## When FEAT\_AA32 is implemented:

Trap ID group 0. Traps the following register accesses to EL2:

- EL1 reads of the JIDR, reported using EC syndrome value 0x05 .
- If the JIDR is RAZ from EL0, EL0 reads of the JIDR, reported using EC syndrome value 0x05 .
- EL1 accesses using VMRS of the FPSID, reported using EC syndrome value 0x08 .

## Note

- It is IMPLEMENTATION DEFINED whether the JIDR is RAZ or UNDEFINED at EL0. If it is UNDEFINED at EL0, then any resulting exception takes precedence over this trap.
- The FPSID is not accessible at EL0 using AArch32.
- Writes to the FPSID are ignored, and not trapped by this control.

| TID0   | Meaning                                                                                                                        |
|--------|--------------------------------------------------------------------------------------------------------------------------------|
| 0b0    | This control does not cause any instructions to be trapped.                                                                    |
| 0b1    | The specified EL1 read accesses to ID group 0 registers are trapped to EL2, when EL2 is enabled in the current Security state. |

When the Effective value of HCR\_EL2.{E2H, TGE} is {1, 1}, the Effective value of this field is 0.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## TWE, bit [14]

Traps EL0 and EL1 execution of WFE instructions to EL2, when EL2 is enabled in the current Security state, from both Execution states, reported using EC syndrome value 0x01 .

When FEAT\_WFxT is implemented, this trap also applies to the WFET instruction.

| TWE   | Meaning                                                     |
|-------|-------------------------------------------------------------|
| 0b0   | This control does not cause any instructions to be trapped. |

| TWE   | Meaning                                                                                                                                                                                                                                                             |
|-------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b1   | Any attempt to execute a WFEinstruction at EL0 or EL1 is trapped to EL2, when EL2 is enabled in the current Security state, if the instruction would otherwise have caused the PE to enter a low-power state and it is not trapped by SCTLR.nTWE or SCTLR_EL1.nTWE. |

In AArch32 state, the attempted execution of a conditional WFE instruction is trapped only if the instruction passes its condition code check.

Note

Since a WFE can complete at any time, even without a Wakeup event, the traps on WFE are not guaranteed to be taken, even if the WFE is executed when there is no Wakeup event. The only guarantee is that if the instruction does not complete in finite time in the absence of a Wakeup event, the trap will be taken.

When the Effective value of HCR\_EL2.{E2H, TGE} is {1, 1}, the Effective value of this field is 0.

For more information about when WFE instructions can cause the PE to enter a low-power state, see 'Wait for Event mechanism and Send event'.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## TWI, bit [13]

Traps EL0 and EL1 execution of WFI instructions to EL2, when EL2 is enabled in the current Security state, from both Execution states, reported using EC syndrome value 0x01 .

When FEAT\_WFxT is implemented, this trap also applies to the WFIT instruction.

| TWI   | Meaning                                                                                                                                                                                                                                                              |
|-------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0   | This control does not cause any instructions to be trapped.                                                                                                                                                                                                          |
| 0b1   | Any attempt to execute a WFI instruction at EL0 or EL1 is trapped to EL2, when EL2 is enabled in the current Security state, if the instruction would otherwise have caused the PE to enter a low-power state and it is not trapped by SCTLR.nTWI or SCTLR_EL1.nTWI. |

In AArch32 state, the attempted execution of a conditional WFI instruction is trapped only if the instruction passes its condition code check.

Note

Since a WFI can complete at any time, even without a Wakeup event, the traps on WFI are not guaranteed to be taken, even if the WFI is executed when there is no Wakeup event. The only guarantee is that if the instruction does not complete in finite time in the absence of a Wakeup event, the trap will be taken.

When the Effective value of HCR\_EL2.{E2H, TGE} is {1, 1}, the Effective value of this field is 0.

For more information about when WFI instructions can cause the PE to enter a low-power state, see 'Wait for Interrupt'.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## DC, bit [12]

Default Cacheability.

| DC   | Meaning                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0  | This control has no effect on the EL1&0 translation regime.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| 0b1  | In any Security state: • When EL1 is using AArch64, the PE behaves as if the value of the SCTLR_EL1.M field is 0 for all purposes other than returning the value of a direct read of SCTLR_EL1. • When EL1 is using AArch32, the PE behaves as if the value of the SCTLR.M field is 0 for all purposes other than returning the value of a direct read of SCTLR. • The PE behaves as if the value of the HCR_EL2.VM field is 1 for all purposes other than returning the value of a direct read of HCR_EL2. • The memory type produced by stage 1 of the EL10 translation regime is Normal Non-Shareable, Inner Write-Back Read-Allocate Write-Allocate, Outer Write-Back Read-Allocate Write-Allocate. |

This field has no effect on the EL2, EL2&amp;0, and EL3 translation regimes.

This bit is permitted to be cached in a TLB.

When the Effective value of HCR\_EL2.{E2H, TGE} is {1, 1}, the Effective value of this field is 0.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## BSU, bits [11:10]

Barrier Shareability upgrade. This field determines the minimum shareability domain that is applied to any barrier instruction executed from EL1 or EL0:

| BSU   | Meaning          |
|-------|------------------|
| 0b00  | No effect.       |
| 0b01  | Inner Shareable. |
| 0b10  | Outer Shareable. |
| 0b11  | Full system.     |

This value is combined with the specified level of the barrier held in its instruction, using the same principles as combining the shareability attributes from two stages of address translation.

When the Effective value of HCR\_EL2.{E2H, TGE} is {1, 1}, the Effective value of this field is 0.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## FB, bit [9]

Force broadcast. Causes the following Non-shareable invalidate instructions to be broadcast within the Inner Shareable domain when executed from EL1:

- In AArch32 state: BPIALL, TLBIALL, TLBIMVA, TLBIASID, DTLBIALL, DTLBIMVA, DTLBIASID, ITLBIALL, ITLBIMVA, ITLBIASID, TLBIMVAA, ICIALLU, TLBIMVAL, and TLBIMVAAL.
- In AArch64 state:
- All TLBI instructions that are executable at EL1 and do not specify IS or OS.
- All TLBIP instructions that are executable at EL1 and do not specify IS or OS.
- IC IALLU .

For more information, see 'A64 System instructions for TLB maintenance'.

| FB   | Meaning                                                                                                                                             |
|------|-----------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0  | The specified instructions are not affected by this control.                                                                                        |
| 0b1  | When one of the specified Non-shareable instructions is executed at EL1, the operation is broadcast within the Inner Shareable shareability domain. |

When HCR\_EL2.TGE is 1, the PE ignores the value of this field for all purposes other than a direct read of this field.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## VSE, bit [8]

Virtual SError exception.

| VSE   | Meaning                                                          |
|-------|------------------------------------------------------------------|
| 0b0   | This mechanism is not making a virtual SError exception pending. |
| 0b1   | Avirtual SError exception is pending because of this mechanism.  |

The virtual SError exception is enabled only when HCR\_EL2.TGE is 0 and either HCR\_EL2.AMO is 1 or FEAT\_DoubleFault2 is implemented and the Effective value of HCRX\_EL2.TMEA is 1.

When FEAT\_E3DSE is implemented, virtual SError exceptions pended by this field have priority over delegated SError exceptions pended by SCR\_EL3.DSE.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## VI, bit [7]

Virtual IRQ Interrupt.

| VI   | Meaning                                             |
|------|-----------------------------------------------------|
| 0b0  | This mechanism is not making a virtual IRQ pending. |
| 0b1  | Avirtual IRQ is pending because of this mechanism.  |

The virtual IRQ is enabled only when the value of HCR\_EL2.{TGE, IMO} is {0, 1}.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## VF, bit [6]

Virtual FIQ Interrupt.

| VF   | Meaning                                             |
|------|-----------------------------------------------------|
| 0b0  | This mechanism is not making a virtual FIQ pending. |
| 0b1  | Avirtual FIQ is pending because of this mechanism.  |

The virtual FIQ is enabled only when the value of HCR\_EL2.{TGE, FMO} is {0, 1}.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## AMO,bit [5]

Physical SError exception routing.

| AMO   | Meaning                                                                                                                                                                                                                                                                                                                                                                   |
|-------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0   | When executing at Exception levels below EL3 and the Effective value of HCR_EL2.TGE is 0: • The routing of physical SError exceptions is unaffected by this mechanism. • If FEAT_E3DSE is implemented, then delegated SError exceptions enabled by SCR_EL3.DSE are not taken to EL2. • Virtual SError exceptions are not enabled by this mechanism.                       |
| 0b1   | When executing at Exception levels below EL3, EL2 is enabled in the current Security state, and the Effective value of HCR_EL2.TGE is 0: • Physical SError exceptions are taken to EL2, unless they are routed to EL3. • If FEAT_E3DSE is implemented, then delegated SError exceptions enabled by SCR_EL3.DSE are taken to EL2. • Virtual SError exceptions are enabled. |

When executing at EL3, the value of HCR\_EL2.AMO has no impact on the behavior of the PE.

When executing at Exception levels below EL3, and EL2 is not enabled in the current Security state, the Effective value of HCR\_EL2.AMO is 0.

When the Effective value of HCR\_EL2.TGE is 1, regardless of the value of the AMO bit, all of the following are true:

- Physical SError exceptions target EL2 unless they are routed to EL3.
- If FEAT\_E3DSE is implemented, delegated SError exceptions target EL2.
- Virtual SError exceptions are disabled.

When executing at EL2 and the Effective value of HCR\_EL2.{E2H, TGE} is {1, 0}, it is IMPLEMENTATION DEFINED whether the Effective value of HCR\_EL2.AMO is 1 or the value programmed.

For more information, see 'Asynchronous exception routing'.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## IMO, bit [4]

Physical IRQ Routing.

| IMO   | Meaning                                                                                                                                                                                                                                                   |
|-------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0   | When executing at Exception levels below EL3 and the Effective value of HCR_EL2.TGE is 0: • Physical IRQ interrupts are not taken to EL2. • Virtual IRQ interrupts are disabled.                                                                          |
| 0b1   | When executing at Exception levels below EL3, EL2 is enabled in the current Security state, and the Effective value of HCR_EL2.TGE is 0: • Physical IRQ exceptions are taken to EL2, unless they are routed to EL3. • Virtual IRQ interrupts are enabled. |

When executing at EL3, the Effective value of HCR\_EL2.IMO has no impact on the behavior of the PE.

When executing at Exception levels below EL3, and EL2 is not enabled in the current Security state, the Effective value of HCR\_EL2.IMO is 0.

When the Effective value of HCR\_EL2.TGE is 1, regardless of the value of the IMO bit, all of the following are true:

- Physical IRQ Interrupts target EL2 unless they are routed to EL3.
- Virtual IRQ interrupts are disabled.

When executing at EL2 and the Effective value of HCR\_EL2.{E2H, TGE} is {1, 0}, it is IMPLEMENTATION DEFINED whether the Effective value of HCR\_EL2.IMO is 1 or the value programmed.

For more information, see 'Asynchronous exception routing'.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## FMO, bit [3]

Physical FIQ Routing.

| FMO   | Meaning                                                                                                                                                                                                                                                   |
|-------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0   | When executing at Exception levels below EL3 and the Effective value of HCR_EL2.TGE is 0: • Physical FIQ interrupts are not taken to EL2. • Virtual FIQ interrupts are disabled.                                                                          |
| 0b1   | When executing at Exception levels below EL3, EL2 is enabled in the current Security state, and the Effective value of HCR_EL2.TGE is 0: • Physical FIQ exceptions are taken to EL2, unless they are routed to EL3. • Virtual FIQ interrupts are enabled. |

When executing at EL3, the Effective value of HCR\_EL2.FMO has no impact on the behavior of the PE.

When executing at Exception levels below EL3, and EL2 is not enabled in the current Security state, the Effective value of HCR\_EL2.FMO is 0.

When the Effective value of HCR\_EL2.TGE is 1, regardless of the value of the FMO bit, all of the following are true:

- Physical FIQ Interrupts target EL2 unless they are routed to EL3.
- Virtual FIQ interrupts are disabled.

When executing at EL2 and the Effective value of HCR\_EL2.{E2H, TGE} is {1, 0}, it is IMPLEMENTATION DEFINED whether the Effective value of HCR\_EL2.FMO is 1 or the value programmed.

For more information, see 'Asynchronous exception routing'.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## PTW, bit [2]

Protected Table Walk. In the EL1&amp;0 translation regime, a translation table access made as part of a stage 1 translation table walk is subject to a stage 2 translation. The combining of the memory type attributes from the two stages of translation means the access might be made to a type of Device memory. If this occurs, then the value of this bit determines the behavior:

| PTW   | Meaning                                                                                                                |
|-------|------------------------------------------------------------------------------------------------------------------------|
| 0b0   | The translation table walk occurs as if it is to Normal Non-cacheable memory. This means it can be made speculatively. |
| 0b1   | The memory access generates a stage 2 Permission fault.                                                                |

This bit is permitted to be cached in a TLB.

When HCR\_EL2.TGE is 1, the PE ignores the value of this field for all purposes other than a direct read of this field.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## SWIO, bit [1]

Set/Way Invalidation Override. Causes EL1 execution of the data cache invalidate by set/way instructions to perform a data cache clean and invalidate by set/way:

| SWIO   | Meaning                                                                                             |
|--------|-----------------------------------------------------------------------------------------------------|
| 0b0    | This control has no effect on the operation of data cache invalidate by set/way instructions.       |
| 0b1    | Data cache invalidate by set/way instructions perform a data cache clean and invalidate by set/way. |

When the value of this bit is 1:

AArch32: DCISW performs the same invalidation as a DCCISW instruction.

AArch64: DC ISW performs the same invalidation as a DC CISW instruction.

This bit can be implemented as RES1.

When HCR\_EL2.TGE is 1, the PE ignores the value of this field for all purposes other than a direct read of this field.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## VM, bit [0]

Virtualization enable. Enables stage 2 address translation for the EL1&amp;0 translation regime, when EL2 is enabled in the current Security state.

| VM   | Meaning                                     |
|------|---------------------------------------------|
| 0b0  | EL1&0 stage 2 address translation disabled. |
| 0b1  | EL1&0 stage 2 address translation enabled.  |

When the value of this bit is 1, data cache invalidate instructions executed at EL1 perform a data cache clean and invalidate. For the invalidate by set/way instruction this behavior applies regardless of the value of the HCR\_EL2.SWIO bit.

This bit is permitted to be cached in a TLB.

When the Effective value of HCR\_EL2.{E2H, TGE} is {1, 1}, the Effective value of this field is 0.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Accessing HCR\_EL2

Accesses to this register use the following encodings in the System register encoding space:

MRS &lt;Xt&gt;, HCR\_EL2

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b100 | 0b0001 | 0b0001 | 0b000 |

```
if !IsFeatureImplemented(FEAT_AA64) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EffectiveHCR_EL2_NVx() IN {'1x1'} then X[t, 64] = NVMem[0x078]; elsif EffectiveHCR_EL2_NVx() IN {'xx1'} then AArch64.SystemAccessTrap(EL2, 0x18); else UNDEFINED; elsif PSTATE.EL == EL2 then X[t, 64] = HCR_EL2; elsif PSTATE.EL == EL3 then X[t, 64] = HCR_EL2;
```

MSR HCR\_EL2, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b100 | 0b0001 | 0b0001 | 0b000 |

```
if !IsFeatureImplemented(FEAT_AA64) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EffectiveHCR_EL2_NVx() IN {'1x1'} then
```

```
NVMem[0x078] = X[t, 64]; elsif EffectiveHCR_EL2_NVx() IN {'xx1'} then AArch64.SystemAccessTrap(EL2, 0x18); else UNDEFINED; elsif PSTATE.EL == EL2 then HCR_EL2 = X[t, 64]; elsif PSTATE.EL == EL3 then HCR_EL2 = X[t, 64];
```