## D24.2.176 SCTLR\_EL2, System Control Register (EL2)

The SCTLR\_EL2 characteristics are:

## Purpose

Provides top-level control of the system, including its memory system, at EL2.

When the Effective value of HCR\_EL2.{E2H, TGE} is {1, 1}, these controls apply also to execution at EL0.

## Configuration

If EL2 is not implemented, this register is RES0 from EL3.

This register has no effect if EL2 is not enabled in the current Security state.

AArch64 System register SCTLR\_EL2 bits [31:0] are architecturally mapped to AArch32 System register HSCTLR[31:0].

This register is present only when FEAT\_AA64 is implemented. Otherwise, direct accesses to SCTLR\_EL2 are UNDEFINED.

## Attributes

SCTLR\_EL2 is a 64-bit register.

## Field descriptions

<!-- image -->

## TIDCP, bit [63]

## When FEAT\_TIDCP1 is implemented and ELIsInHost(EL2):

Trap IMPLEMENTATION DEFINED functionality. Traps EL0 accesses to the encodings reserved for IMPLEMENTATION DEFINED functionality to EL2.

| TIDCP   | Meaning                                                                                                   |
|---------|-----------------------------------------------------------------------------------------------------------|
| 0b0     | No instructions accessing the System register or System instruction spaces are trapped by this mechanism. |

| TIDCP   | Meaning                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
|---------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b1     | If HCR_EL2.TGE==0, no instructions accessing the System register or System instruction spaces are trapped by this mechanism. If HCR_EL2.TGE==1, instructions accessing the following System register or System instruction spaces are trapped to EL2 by this mechanism: • In AArch64 state, EL0 access to the encodings in the following reserved encoding spaces are trapped: • IMPLEMENTATION DEFINED System instructions, which are accessed using SYS and SYSL, with CRn == {11, 15}, and are reported using EC syndrome value 0x18 . • IMPLEMENTATION DEFINED System instructions, which are accessed using SYSP, with CRn == {11, 15}, and are reported using EC syndrome value 0x14 . • IMPLEMENTATION DEFINED System registers, which are accessed using MRSand MSRwith the S3_<op1>_<Cn>_<Cm>_<op2> register name, and are reported using EC syndrome value 0x18 . • IMPLEMENTATION DEFINED System registers, which are accessed usingMRRSandMSRR with the S3_<op1>_<Cn>_<Cm>_<op2> register name, and are reported using EC syndrome value 0x14 . • In AArch32 state, EL0 MCRand MRCaccesses to the following encodings are trapped and reported using EC syndrome value 0x03 : • All coproc==p15, CRn==c9, opc1 == {0-7}, CRm=={c0-c2, c5-c8}, opc2 == {0-7}. • All coproc==p15, CRn==c10, opc1 =={0-7}, CRm=={c0, c1, c4, c8}, opc2 == {0-7}. • All coproc==p15, CRn==c11, opc1=={0-7}, CRm=={c0-c8, c15}, opc2 == {0-7}. |

If HCR\_EL2.TGE == 0b0 , the field is IGNORED for all purposes other than direct reads and writes of the register.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## SPINTMASK, bit [62]

## When FEAT\_NMI is implemented:

SP Interrupt Mask enable. When SCTLR\_EL2.NMI is 1, controls whether PSTATE.SP acts as an interrupt mask, and controls the value of PSTATE.ALLINT on taking an exception to EL2.

| SPINTMASK   | Meaning                                                                                                                                                                                                        |
|-------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0         | Does not cause PSTATE.SP to mask interrupts. PSTATE.ALLINT is set to 1 on taking an exception to EL2.                                                                                                          |
| 0b1         | When PSTATE.SP is 1 and execution is at EL2, an IRQ or FIQ interrupt that is targeted to EL2 is masked regardless of any indication of Superpriority. PSTATE.ALLINT is set to 0 on taking an exception to EL2. |

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

NMI, bit [61]

## When FEAT\_NMI is implemented:

Non-maskable Interrupt enable.

| NMI   | Meaning                                                  |
|-------|----------------------------------------------------------|
| 0b0   | This control does not affect interrupt masking behavior. |
| 0b1   | This control enables all of the following:               |

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

EnTP2, bit [60]

## When FEAT\_SME is implemented and ELIsInHost(EL2):

Traps instructions executed at EL0 that access TPIDR2\_EL0 to EL2 when EL2 is implemented and enabled for the current Security state. The exception is reported using EC syndrome value 0x18 .

| EnTP2   | Meaning                                                                   |
|---------|---------------------------------------------------------------------------|
| 0b0     | This control causes execution of these instructions at EL0 to be trapped. |
| 0b1     | This control does not cause execution of any instructions to be trapped.  |

If HCR\_EL2.TGE == 0b0 , the field is IGNORED for all purposes other than direct reads and writes of the register.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

TCSO, bit [59]

## When FEAT\_MTE\_STORE\_ONLY is implemented:

Tag Checking Store Only.

| TCSO   | Meaning                                                                                   |
|--------|-------------------------------------------------------------------------------------------|
| 0b0    | This field has no effect on Tag checking.                                                 |
| 0b1    | Explicit Memory Read Effects generated by instructions executed in EL2 are Tag Unchecked. |

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## TCSO0, bit [58]

## When FEAT\_MTE\_STORE\_ONLY is implemented and ELIsInHost(EL2):

Tag Checking Store Only in EL0.

| TCSO0   | Meaning                                                                                   |
|---------|-------------------------------------------------------------------------------------------|
| 0b0     | This field has no effect on Tag checking.                                                 |
| 0b1     | Explicit Memory Read Effects generated by instructions executed in EL0 are Tag Unchecked. |

If HCR\_EL2.TGE == 0b0 , the field is IGNORED for all purposes other than direct reads and writes of the register.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## EPAN, bit [57]

## When FEAT\_PAN3 is implemented and ELIsInHost(EL2):

Enhanced Privileged Access Never. When PSTATE.PAN is 1, determines whether an EL2 data access to a page with EL0 instruction access permission generates a Permission fault as a result of the Privileged Access Never mechanism.

| EPAN   | Meaning                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
|--------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0    | No additional Permission faults are generated by this mechanism.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| 0b1    | An EL2 data access to a page with stage 1 EL0 data access permission or stage 1 EL0 instruction access permission generates a Permission fault. Any speculative data accesses that would generate a Permission fault as a result of PSTATE.PAN = 1 if the accesses were not speculative, will not cause an allocation into a cache. When executing at EL2, and the Effective value of HCR_EL2.{E2H, TGE} is {1, 1}, this does not prevent unprivileged speculative accesses generated from the EL0 hardware-defined context from causing allocation into a cache. |

Note

The value of HCR\_EL2.TGE does not change the effect of this field on privileged accesses.

This bit is permitted to be cached in a TLB.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## EnALS, bit [56]

## When FEAT\_LS64 is implemented and ELIsInHost(EL2):

Traps execution of an LD64B or ST64B instruction at EL0 to EL2.

| EnALS   | Meaning                                                              |
|---------|----------------------------------------------------------------------|
| 0b0     | Execution of an LD64B or ST64B instruction at EL0 is trapped to EL2. |
| 0b1     | This control does not cause any instructions to be trapped.          |

If HCR\_EL2.TGE == 0b0 , the field is IGNORED for all purposes other than direct reads and writes of the register.

Atrap of an LD64B or ST64B instruction is reported using EC syndrome value 0x0A , with an ISS code of 0x0000002 .

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## EnAS0, bit [55]

## When FEAT\_LS64\_ACCDATA is implemented and ELIsInHost(EL2):

Traps execution of an ST64BV0 instruction at EL0 to EL2.

| EnAS0   | Meaning                                                       |
|---------|---------------------------------------------------------------|
| 0b0     | Execution of an ST64BV0 instruction at EL0 is trapped to EL2. |
| 0b1     | This control does not cause any instructions to be trapped.   |

If HCR\_EL2.TGE == 0b0 , the field is IGNORED for all purposes other than direct reads and writes of the register.

Atrap of an ST64BV0 instruction is reported using EC syndrome value 0x0A , with an ISS code of 0x0000001 .

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## EnASR, bit [54]

## When FEAT\_LS64\_V is implemented and ELIsInHost(EL2):

Traps execution of an ST64BV instruction at EL0 to EL2.

| EnASR   | Meaning                                                      |
|---------|--------------------------------------------------------------|
| 0b0     | Execution of an ST64BV instruction at EL0 is trapped to EL2. |
| 0b1     | This control does not cause any instructions to be trapped.  |

If HCR\_EL2.TGE == 0b0 , the field is IGNORED for all purposes other than direct reads and writes of the register.

Atrap of an ST64BV instruction is reported using EC syndrome value 0x0A , with an ISS code of 0x0000000 .

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## Bits [53:50]

Reserved, RES0.

## TWEDEL,bits [49:46]

## When FEAT\_TWED is implemented and ELIsInHost(EL2):

TWEDelay. A 4-bit unsigned number that, when SCTLR\_EL2.TWEDEn is 1, encodes the minimum delay in taking a trap of WFE* caused by SCTLR\_EL2.nTWE as 2 (TWEDEL + 8) cycles.

If HCR\_EL2.TGE == 0b0 , the field is IGNORED for all purposes other than direct reads and writes of the register.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## TWEDEn, bit [45]

## When FEAT\_TWED is implemented and ELIsInHost(EL2):

TWEDelay Enable. Enables a configurable delayed trap of the WFE* instruction caused by SCTLR\_EL2.nTWE.

| TWEDEn   | Meaning                                                                                        |
|----------|------------------------------------------------------------------------------------------------|
| 0b0      | The delay for taking a WFE* trap is IMPLEMENTATION DEFINED.                                    |
| 0b1      | The delay for taking a WFE* trap is at least the number of cycles defined in SCTLR_EL2.TWEDEL. |

If HCR\_EL2.TGE == 0b0 , the field is IGNORED for all purposes other than direct reads and writes of the register.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## DSSBS, bit [44]

## When FEAT\_SSBS is implemented:

Default PSTATE.SSBS value on exception entry.

| DSSBS   | Meaning                                         |
|---------|-------------------------------------------------|
| 0b0     | PSTATE.SSBS is set to 0 on an exception to EL2. |
| 0b1     | PSTATE.SSBS is set to 1 on an exception to EL2. |

The reset behavior of this field is:

- On a Warm reset, this field resets to an IMPLEMENTATION DEFINED value.

## Otherwise:

Reserved, RES0.

## ATA, bit [43]

## When FEAT\_MTE2 is implemented:

Allocation Tag Access in EL2.

Controls use of Memory tagging in EL2.

| ATA   | Meaning                                   |
|-------|-------------------------------------------|
| 0b0   | Use of Memory tagging is disabled at EL2. |
| 0b1   | Use of Memory tagging is enabled at EL2.  |

If SCR\_EL3.ATA is 0, then the Effective value of this field is 0.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## ATA0, bit [42]

## When FEAT\_MTE2 is implemented and ELIsInHost(EL2):

Allocation Tag Access in EL0.

Controls use of Memory Tagging in EL0.

| ATA0   | Meaning                                   |
|--------|-------------------------------------------|
| 0b0    | Use of Memory tagging is disabled at EL0. |
| 0b1    | Use of Memory tagging is enabled at EL2.  |

If SCR\_EL3.ATA is 0, then the Effective value of this field is 0.

If HCR\_EL2.TGE is 0, the field is IGNORED for all purposes other than direct reads and writes of the register.

Note

Software may change this control bit on a context switch.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

TCF, bits [41:40]

## When FEAT\_MTE2 is implemented:

Tag Check Fault in EL2. Controls the effect of Tag Check Faults due to Loads and Stores in EL2.

| TCF   | Meaning                                                                                                | Applies when                       |
|-------|--------------------------------------------------------------------------------------------------------|------------------------------------|
| 0b00  | Tag Check Faults have no effect on the PE.                                                             |                                    |
| 0b01  | Tag Check Faults cause a synchronous exception.                                                        |                                    |
| 0b10  | Tag Check Faults are asynchronously accumulated.                                                       |                                    |
| 0b11  | Tag Check Faults cause a synchronous exception on reads, and are asynchronously accumulated on writes. | FEAT_MTE_ASYM_FAULT is implemented |

If FEAT\_MTE3 is not implemented, the value 0b11 is reserved.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

TCF0, bits [39:38]

## When FEAT\_MTE2 is implemented and ELIsInHost(EL2):

Tag Check Fault in EL0. Controls the effect of Tag Check Faults due to Loads and Stores in EL0.

| TCF0   | Meaning                                                                                                | Applies when                       |
|--------|--------------------------------------------------------------------------------------------------------|------------------------------------|
| 0b00   | Tag Check Faults have no effect on the PE.                                                             |                                    |
| 0b01   | Tag Check Faults cause a synchronous exception.                                                        |                                    |
| 0b10   | Tag Check Faults are asynchronously accumulated.                                                       |                                    |
| 0b11   | Tag Check Faults cause a synchronous exception on reads, and are asynchronously accumulated on writes. | FEAT_MTE_ASYM_FAULT is implemented |

If HCR\_EL2.TGE == 0b0 , the field is IGNORED for all purposes other than direct reads and writes of the register.

If FEAT\_MTE3 is not implemented, the value 0b11 is reserved.

Note

Software may change this control bit on a context switch.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## ITFSB, bit [37]

## When FEAT\_MTE\_ASYNC is implemented:

When synchronous exceptions are not being generated by Tag Check Faults, this field controls whether on exception entry into EL2, all Tag Check Faults due to instructions executed before exception entry, that are reported asynchronously, are synchronized into TFSRE0\_EL1, TFSR\_EL1, and TFSR\_EL2 registers.

| ITFSB   | Meaning                                                |
|---------|--------------------------------------------------------|
| 0b0     | Tag Check Faults are not synchronized on entry to EL2. |
| 0b1     | Tag Check Faults are synchronized on entry to EL2.     |

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## BT, bit [36]

## When FEAT\_BTI is implemented:

Indicates the Branch Type compatibility of the implicit BTI behavior for the following instructions at EL2:

- PACIASP .
- PACIBSP .
- If FEAT\_PAuth\_LR is implemented, PACIASPPC .
- If FEAT\_PAuth\_LR is implemented, PACIBSPPC .

When the Effective value of HCR\_EL2.{E2H, TGE} is {1, 1}, this bit is named BT1.

| BT   | Meaning                                                                                                                                                   |
|------|-----------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0  | When the PE is executing at EL2, when the specified instructions have an implicit BTI behavior, they are compatible with the same BTYPE values as BTI.jc. |
| 0b1  | When the PE is executing at EL2, when the specified instructions have an implicit BTI behavior, they are compatible with the same BTYPE values as BTI.c.  |

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## BT0, bit [35]

## When FEAT\_BTI is implemented and ELIsInHost(EL2):

Indicates the Branch Type compatibility of the implicit BTI behavior for the following instructions at EL0:

- PACIASP .
- PACIBSP .
- If FEAT\_PAuth\_LR is implemented, PACIASPPC .
- If FEAT\_PAuth\_LR is implemented, PACIBSPPC .

| BT0   | Meaning                                                                                                                                                   |
|-------|-----------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0   | When the PE is executing at EL0, when the specified instructions have an implicit BTI behavior, they are compatible with the same BTYPE values as BTI.jc. |
| 0b1   | When the PE is executing at EL0, when the specified instructions have an implicit BTI behavior, they are compatible with the same BTYPE values as BTI.c.  |

If HCR\_EL2.TGE == 0b0 , the field is IGNORED for all purposes other than direct reads and writes of the register.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## EnFPM, bit [34]

## When FEAT\_FPMR is implemented and ELIsInHost(EL0):

Enables direct and indirect accesses to FPMR from EL0.

When accesses to FPMR are disabled by this control:

- Direct accesses to FPMR from EL0 are trapped to EL2 and reported using EC syndrome value 0x18 .
- Execution of FP8 data-processing instructions that indirectly access FPMR is UNDEFINED at EL0.

| EnFPM   | Meaning                                                     |
|---------|-------------------------------------------------------------|
| 0b0     | Direct and indirect accesses to FPMRare disabled at EL0.    |
| 0b1     | This control does not cause any instructions to be trapped. |

Traps are not taken if there is a higher priority exception generated by the access.

If EL2 is not implemented or is disabled in the current Security state, the Effective value of this field is 0b1 .

When HCR\_EL2.TGE is 0, this field is IGNORED for all purposes other than direct reads and writes of the register.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## MSCEn, bit [33]

## When FEAT\_MOPS is implemented and ELIsInHost(EL2):

Memory Copy and Memory Set instructions Enable. Enables execution of the Memory Copy and Memory Set instructions at EL0.

| MSCEn   | Meaning                                                                       |
|---------|-------------------------------------------------------------------------------|
| 0b0     | Execution of the Memory Copy and Memory Set instructions is UNDEFINED at EL0. |
| 0b1     | This control does not cause any instructions to be UNDEFINED.                 |

If HCR\_EL2.TGE == 0b0 , the field is IGNORED for all purposes other than direct reads and writes of the register.

When FEAT\_MOPS is implemented and the Effective value of HCR\_EL2.{E2H, TGE} is not {1, 1}, the Effective value of this bit is 0b1 .

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## CMOW,bit [32]

## When FEAT\_CMOWis implemented and ELIsInHost(EL2):

Controls the required permissions for the following cache maintenance instructions executed at EL0:

- Any DC instruction that operates by V A and performs a clean and invalidate operation.
- Any IC instruction that operates by V A.

| CMOW   | Meaning                                                                                                                                  |
|--------|------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0    | This control does not cause any instruction to generate a stage 1 Permission fault.                                                      |
| 0b1    | For these instructions, when executed at EL0, the absence of stage 1 unprivileged write permission generates a stage 1 permission fault. |

If HCR\_EL2.TGE == 0b0 , the field is IGNORED for all purposes other than direct reads and writes of the register.

For more information, see:

- Stage 1 permissions.
- Implications of enabling the dirty state management mechanism.

This bit is permitted to be cached in a TLB.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## EnIA, bit [31]

## When FEAT\_PAuth is implemented:

Controls enabling of pointer authentication of instruction addresses, using the APIAKey\_EL1 key, at EL2 and at EL0 in the EL2&amp;0 translation regime.

| EnIA   | Meaning                                                                                                                                       |
|--------|-----------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0    | Pointer authentication of instruction addresses at EL2 and at EL0 in the EL2&0 translation regime, using the APIAKey_EL1 key, is not enabled. |
| 0b1    | Pointer authentication of instruction addresses at EL2 and at EL0 in the EL2&0 translation regime, using the APIAKey_EL1 key, is enabled.     |

## Note

This field controls the behavior of the AddPACIA and AuthIA pseudocode functions. When pointer authentication is enabled, AddPACIA returns a copy of a pointer to which a pointer authentication code has been added, and AuthIA returns an authenticated copy of a pointer. When pointer authentication is disabled, both of these functions are NOP.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## EnIB, bit [30]

## When FEAT\_PAuth is implemented:

Controls enabling of pointer authentication of instruction addresses, using the APIBKey\_EL1 key, at EL2 and at EL0 in the EL2&amp;0 translation regime.

| EnIB   | Meaning                                                                                                                                       |
|--------|-----------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0    | Pointer authentication of instruction addresses at EL2 and at EL0 in the EL2&0 translation regime, using the APIBKey_EL1 key, is not enabled. |
| 0b1    | Pointer authentication of instruction addresses at EL2 and at EL0 in the EL2&0 translation regime, using the APIBKey_EL1 key, is enabled.     |

## Note

This field controls the behavior of the AddPACIB and AuthIB pseudocode functions. When pointer authentication is enabled, AddPACIB returns a copy of a pointer to which a pointer authentication code has been added, and AuthIB returns an authenticated copy of a pointer. When pointer authentication is disabled, both of these functions are NOP.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## LSMAOE, bit [29]

## When FEAT\_LSMAOC is implemented and ELIsInHost(EL2):

Load Multiple and Store Multiple Atomicity and Ordering Enable.

| LSMAOE   | Meaning                                                                                                                                                                                               |
|----------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0      | For all memory accesses at EL0, T32 and A32 Load Multiple and Store Multiple can have an interrupt taken during the sequence memory accesses, and the memory accesses are not required to be ordered. |
| 0b1      | The ordering and interrupt behavior of T32 and A32 Load Multiple and Store Multiple at EL0 is as defined for Armv8.0.                                                                                 |

If HCR\_EL2.TGE == 0b0 , the field is IGNORED for all purposes other than direct reads and writes of the register.

This bit is permitted to be cached in a TLB.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES1.

## nTLSMD, bit [28]

## When FEAT\_LSMAOC is implemented and ELIsInHost(EL2):

No Trap Load Multiple and Store Multiple to Device-nGRE/Device-nGnRE/Device-nGnRnE memory.

| nTLSMD   | Meaning                                                                                                                                                                                                    |
|----------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0      | All memory accesses by T32 and A32 Load Multiple and Store Multiple at EL0 that are marked at stage 1 as Device-nGRE/Device-nGnRE/Device-nGnRnE memory are trapped and generate a stage 1 Alignment fault. |
| 0b1      | All memory accesses by T32 and A32 Load Multiple and Store Multiple at EL0 that are marked at stage 1 as Device-nGRE/Device-nGnRE/Device-nGnRnE memory are not trapped.                                    |

If HCR\_EL2.TGE == 0b0 , the field is IGNORED for all purposes other than direct reads and writes of the register.

This bit is permitted to be cached in a TLB.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES1.

## EnDA, bit [27]

## When FEAT\_PAuth is implemented:

Controls enabling of pointer authentication of data addresses, using the APDAKey\_EL1 key, at EL2 and at EL0 in the EL2&amp;0 translation regime.

| EnDA   | Meaning                                                                                                                                |
|--------|----------------------------------------------------------------------------------------------------------------------------------------|
| 0b0    | Pointer authentication of data addresses at EL2 and at EL0 in the EL2&0 translation regime, using the APDAKey_EL1 key, is not enabled. |
| 0b1    | Pointer authentication of data addresses at EL2 and at EL0 in the EL2&0 translation regime, using the APDAKey_EL1 key, is enabled.     |

## Note

This field controls the behavior of the AddPACDA and AuthDA pseudocode functions. When pointer authentication is enabled, AddPACDA returns a copy of a pointer to which a pointer authentication code has been added, and AuthDA returns an authenticated copy of a pointer. When pointer authentication is disabled, both of these functions are NOP.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## UCI, bit [26]

## When ELIsInHost(EL2):

Traps execution of cache maintenance instructions at EL0 to EL2, from AArch64 state only, reported using EC syndrome value 0x18 , as follows:

- DCCVAU, DC CIVAC, DC CVAC, and IC IVAU.

- If FEAT\_MTE is implemented, DC CIGVAC, DC CIGDVAC, DC CGVAC, and DC CGDVAC.
- If FEAT\_DPB is implemented, DC CVAP.
- If FEAT\_DPB and FEAT\_MTE are implemented, DC CGVAP and DC CGDVAP.
- If FEAT\_DPB2 is implemented, DC CVADP.
- If FEAT\_DPB2 and FEAT\_MTE are implemented, DC CGVADP and DC CGDVADP.
- If FEAT\_OCCMO is implemented, DC CIVAOC, DC CIGDVAOC, DC CVAOC and DC CGDVAOC.

| UCI   | Meaning                                                                                                                                    |
|-------|--------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0   | For each of the specified instructions, if the execution of the instruction can be trapped, access at EL0 using AArch64 is trapped to EL2. |
| 0b1   | This control does not cause any instructions to be trapped.                                                                                |

If HCR\_EL2.TGE == 0b0 , the field is IGNORED for all purposes other than direct reads and writes of the register.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## EE, bit [25]

## When FEAT\_MixedEnd is implemented:

Endianness of data accesses at EL2, stage 1 translation table walks in the EL2 or EL2&amp;0 translation regime, and stage 2 translation table walks in the EL1&amp;0 translation regime.

| EE   | Meaning                                                                                                                                                                                       |
|------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0  | Explicit data accesses at EL2, stage 1 translation table walks in the EL2 or EL2&0 translation regime, and stage 2 translation table walks in the EL1&0 translation regime are little-endian. |
| 0b1  | Explicit data accesses at EL2, stage 1 translation table walks in the EL2 or EL2&0 translation regime, and stage 2 translation table walks in the EL1&0 translation regime are big-endian.    |

The EE bit is permitted to be cached in a TLB.

The reset behavior of this field is:

- On a Warm reset, this field resets to an IMPLEMENTATION DEFINED value.

## When FEAT\_BigEnd is implemented:

Explicit data accesses at EL1, and stage 1 translation table walks in the EL1&amp;0 translation regime are big-endian.

Reserved, RES1.

## Otherwise:

Explicit data accesses at EL1, and stage 1 translation table walks in the EL1&amp;0 translation regime are little-endian.

Reserved, RES0.

## E0E, bit [24]

## When ELIsInHost(EL2) and FEAT\_MixedEndEL0 is implemented:

Endianness of data accesses at EL0.

| E0E   | Meaning                                          |
|-------|--------------------------------------------------|
| 0b0   | Explicit data accesses at EL0 are little-endian. |
| 0b1   | Explicit data accesses at EL0 are big-endian.    |

If HCR\_EL2.TGE == 0b0 , the field is IGNORED for all purposes other than direct reads and writes of the register.

This bit has no effect on the endianness of Explicit Memory Effects generated by unprivileged memory access instructions executed at EL2.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## When FEAT\_BigEndEL0 is implemented:

Explicit data accesses at EL0 are big-endian.

Reserved, RES1.

## Otherwise:

Explicit data accesses at EL0 are little-endian.

Reserved, RES0.

## SPAN, bit [23]

## When ELIsInHost(EL2):

Set Privileged Access Never, on taking an exception to EL2.

| SPAN   | Meaning                                                                  |
|--------|--------------------------------------------------------------------------|
| 0b0    | PSTATE.PAN is set to 1 on taking an exception to EL2.                    |
| 0b1    | The value of PSTATE.PAN is left unchanged on taking an exception to EL2. |

If HCR\_EL2.TGE == 0b0 , the field is IGNORED for all purposes other than direct reads and writes of the register.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES1.

## EIS, bit [22]

## When FEAT\_ExS is implemented:

Exception entry is a context synchronization event.

| EIS   | Meaning                                                                   |
|-------|---------------------------------------------------------------------------|
| 0b0   | The taking of an exception to EL2 is not a context synchronization event. |
| 0b1   | The taking of an exception to EL2 is a context synchronization event.     |

## If SCTLR\_EL2.EIS is set to 0b0 :

- Indirect writes to ESR\_EL2, FAR\_EL2, SPSR\_EL2, ELR\_EL2, and HPFAR\_EL2 are synchronized on exception entry to EL2, so that a direct read of the register after exception entry sees the indirectly written value caused by the exception entry.
- Memory transactions, including instruction fetches, from an Exception level always use the translation resources associated with that translation regime.
- Exception Catch debug events are synchronous debug events.
- DCPS* and DRPS instructions are context synchronization events.
- Some exception entries reported are not considered IFBEs per the memory model.

The following are not affected by the value of SCTLR\_EL2.EIS:

- Changes to the PSTATE information on entry to EL2.
- Behavior of accessing the banked copies of the stack pointer using the SP register name for loads, stores, and data processing instructions.
- The memory model requirement for exception entry to generate an Instruction Fetch Barrier Effect for some exception entries. See Basic definitions for the list of exception entries.
- Exit from Debug state.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES1.

## IESB, bit [21]

## When FEAT\_IESB is implemented:

Implicit Error Synchronization event enable.

| IESB   | Meaning                                           |
|--------|---------------------------------------------------|
| 0b0    | Disabled.                                         |
| 0b1    | An implicit error synchronization event is added: |

If FEAT\_DoubleFault2 is implemented, the PE is in Non-debug state, and the Effective value of SCTLR2\_EL2.NMEA is 1, then SCTLR\_EL2.IESB is ignored and the PE behaves as if SCTLR\_EL2.IESB is 1 for all purposes other than direct read of the register.

When the PE is in Debug state, the effect of this field is CONSTRAINED UNPREDICTABLE, and its Effective value might be 0 or 1 regardless of the value of the field. If the Effective value of the field is 1, then an implicit error synchronization event is added after each DCPSx instruction taken to EL2 and before each DRPS instruction executed at EL2, in addition to the other cases where it is added.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## TSCXT, bit [20]

## When (FEAT\_CSV2\_2 is implemented or FEAT\_CSV2\_1p2 is implemented) and ELIsInHost(EL2):

Trap EL0 Access to the SCXTNUM\_EL0 register, when EL0 is using AArch64.

| TSCXT   | Meaning                                                                                                        |
|---------|----------------------------------------------------------------------------------------------------------------|
| 0b0     | EL0 access to SCXTNUM_EL0 is not disabled by this mechanism.                                                   |
| 0b1     | EL0 access to SCXTNUM_EL0 is disabled, causing an exception to EL2, and the SCXTNUM_EL0 value is treated as 0. |

If HCR\_EL2.TGE == 0b0 , the field is IGNORED for all purposes other than direct reads and writes of the register.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

When FEAT\_CSV2\_2 is not implemented, FEAT\_CSV2\_1p2 is not implemented, and ELIsInHost(EL0):

Reserved, RES1.

## Otherwise:

Reserved, RES0.

## WXN,bit [19]

Write permission implies XN (Execute-never). For the EL2 or EL2&amp;0 translation regime, this bit can restrict execute permissions on writeable pages.

| WXN   | Meaning                                                                                                                                                                                        |
|-------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0   | This control has no effect on memory access permissions.                                                                                                                                       |
| 0b1   | In the EL2 or EL2&0 translation regime, any region of memory that is writeable at EL2 is XNat EL2. In the EL2&0 translation regime, any region of memory that is writeable at EL0 is XNat EL0. |

This bit applies only when SCTLR\_EL2.M bit is set.

The WXN bit is permitted to be cached in a TLB.

This field is RES0 if TCR2\_EL2.PIE is 1.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

nTWE, bit [18]

## When ELIsInHost(EL2):

Traps execution of WFE instructions at EL0 to EL2, from both Execution states.

When FEAT\_WFxT is implemented, this trap also applies to the WFET instruction.

| nTWE   | Meaning                                                                                                                                             |
|--------|-----------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0    | Any attempt to execute a WFEinstruction at EL0 is trapped to EL2, if the instruction would otherwise have caused the PE to enter a low-power state. |
| 0b1    | This control does not cause any instructions to be trapped.                                                                                         |

If HCR\_EL2.TGE == 0b0 , the field is IGNORED for all purposes other than direct reads and writes of the register.

In AArch32 state, the attempted execution of a conditional WFE instruction is only trapped if the instruction passes its condition code check.

Note

Since a WFE or WFI can complete at any time, even without a Wakeup event, the traps on WFE of WFI are not guaranteed to be taken, even if the WFE or WFI is executed when there is no Wakeup event. The only guarantee is that if the instruction does not complete in finite time in the absence of a Wakeup event, the trap will be taken.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES1.

## Bit [17]

Reserved, RES0.

## nTWI, bit [16]

## When ELIsInHost(EL2):

Traps execution of WFI instructions at EL0 to EL2, from both Execution states.

When FEAT\_WFxT is implemented, this trap also applies to the WFIT instruction.

| nTWI   | Meaning                                                                                                                                           |
|--------|---------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0    | Any attempt to execute a WFI instruction at EL0 is trapped EL2, if the instruction would otherwise have caused the PE to enter a low-power state. |
| 0b1    | This control does not cause any instructions to be trapped.                                                                                       |

If HCR\_EL2.TGE == 0b0 , the field is IGNORED for all purposes other than direct reads and writes of the register.

In AArch32 state, the attempted execution of a conditional WFI instruction is only trapped if the instruction passes its condition code check.

Note

Since a WFE or WFI can complete at any time, even without a Wakeup event, the traps on WFE of WFI are not guaranteed to be taken, even if the WFE or WFI is executed when there is no Wakeup event. The only guarantee is that if the instruction does not complete in finite time in the absence of a Wakeup event, the trap will be taken.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES1.

## UCT, bit [15]

## When ELIsInHost(EL2):

Traps EL0 accesses to the CTR\_EL0 to EL2, from AArch64 state only.

| UCT   | Meaning                                                            |
|-------|--------------------------------------------------------------------|
| 0b0   | Accesses to the CTR_EL0 from EL0 using AArch64 are trapped to EL2. |
| 0b1   | This control does not cause any instructions to be trapped.        |

If HCR\_EL2.TGE == 0b0 , the field is IGNORED for all purposes other than direct reads and writes of the register.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## DZE, bit [14]

## When ELIsInHost(EL2):

Traps execution of DC ZVA instructions at EL0 to EL2, from AArch64 state only.

If FEAT\_MTE is implemented, this trap also applies to DC GVA and DC GZVA.

| DZE   | Meaning                                                                                                                                                                                                                         |
|-------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0   | Any attempt to execute an instruction that this trap applies to at EL0 using AArch64 is trapped to EL2. Reading DCZID_EL0.DZP from EL0 returns 1, indicating that the instructions that this trap applies to are not supported. |
| 0b1   | This control does not cause any instructions to be trapped.                                                                                                                                                                     |

If HCR\_EL2.TGE == 0b0 , the field is IGNORED for all purposes other than direct reads and writes of the register.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## EnDB, bit [13]

## When FEAT\_PAuth is implemented:

Controls enabling of pointer authentication of data addresses, using the APDBKey\_EL1 key, at EL2 and at EL0 in the EL2&amp;0 translation regime.

| EnDB   | Meaning                                                                                                                                |
|--------|----------------------------------------------------------------------------------------------------------------------------------------|
| 0b0    | Pointer authentication of data addresses at EL2 and at EL0 in the EL2&0 translation regime, using the APDBKey_EL1 key, is not enabled. |
| 0b1    | Pointer authentication of data addresses at EL2 and at EL0 in the EL2&0 translation regime, using the APDBKey_EL1 key, is enabled.     |

## Note

This field controls the behavior of the AddPACDB and AuthDB pseudocode functions. When pointer authentication is enabled, AddPACDB returns a copy of a pointer to which a pointer authentication code has been added, and AuthDB returns an authenticated copy of a pointer. When pointer authentication is disabled, both of these functions are NOP.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## I, bit [12]

Instruction access Cacheability control, for accesses at EL2 and, when the Effective value of HCR\_EL2.{E2H, TGE} is {1, 1}, EL0.

| I   | Meaning                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|-----|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0 | All instruction accesses to Normal memory from EL2 are Non-cacheable for all levels of instruction and unified cache. When the Effective value of HCR_EL2.{E2H, TGE} is {1, 1}, all instruction accesses to Normal memory from EL0 are Non-cacheable for all levels of instruction and unified cache. If SCTLR_EL2.M is 0, instruction accesses from stage 1 of the EL2 or EL2&0 translation regime are to Normal, Outer Shareable, Inner Non-cacheable, Outer Non-cacheable memory. |
| 0b1 | This control has no effect on the Cacheability of instruction access to Normal memory from EL2 and, when the Effective value of HCR_EL2.{E2H, TGE} is {1, 1}, instruction access to Normal memory from EL0. If the value of SCTLR_EL2.M is 0, instruction accesses from stage 1 of the EL2 or EL2&0 translation regime are to Normal, Outer Shareable, Inner Write-Through, Outer Write-Through memory.                                                                              |

This bit has no effect on the EL3 translation regime.

When EL2 is disabled in the current Security state or the Effective value of HCR\_EL2.{E2H, TGE} is not {1, 1}, this bit has no effect on the EL1&amp;0 translation regime.

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## EOS, bit [11]

## When FEAT\_ExS is implemented:

Exception exit is a context synchronization event.

| EOS   | Meaning                                                              |
|-------|----------------------------------------------------------------------|
| 0b0   | An exception return from EL2 is not a context synchronization event. |
| 0b1   | An exception return from EL2 is a context synchronization event.     |

## If SCTLR\_EL2.EOS is set to 0b0 :

- Memory transactions, including instruction fetches, from an Exception level always use the translation resources associated with that translation regime.
- Exception Catch debug events are synchronous debug events.
- DCPS* and DRPS instructions are context synchronization events.

The following are not affected by the value of SCTLR\_EL2.EOS:

- The indirect write of the PSTATE and PC values from SPSR\_EL2 and ELR\_EL2 on exception return is synchronized.
- Behavior of accessing the banked copies of the stack pointer using the SP register name for loads, stores, and data processing instructions.
- Exit from Debug state.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES1.

## EnRCTX, bit [10]

## When FEAT\_SPECRES is implemented and ELIsInHost(EL2):

Enable EL0 access to the following System instructions:

- CFPRCTX, DVPRCTX and CPPRCTX instructions.
- If FEAT\_SPECRES2 is implemented, COSPRCTX.
- CFP RCTX, DVP RCTX and CPP RCTX instructions.
- If FEAT\_SPECRES2 is implemented, COSP RCTX.

| EnRCTX   | Meaning                                                                                  |
|----------|------------------------------------------------------------------------------------------|
| 0b0      | EL0 access to these instructions is disabled, and these instructions are trapped to EL2. |
| 0b1      | EL0 access to these instructions is enabled.                                             |

If HCR\_EL2.TGE == 0b0 , the field is IGNORED for all purposes other than direct reads and writes of the register.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## Bit [9]

Reserved, RES0.

## SED, bit [8]

## When FEAT\_AA32EL0 is implemented and ELIsInHost(EL2):

SETEND instruction disable. Disables SETEND instructions at EL0 using AArch32.

| SED   | Meaning                                                       |
|-------|---------------------------------------------------------------|
| 0b0   | SETEND instruction execution is enabled at EL0 using AArch32. |
| 0b1   | SETEND instructions are UNDEFINED at EL0 using AArch32.       |

If HCR\_EL2.TGE == 0b0 , the field is IGNORED for all purposes other than direct reads and writes of the register.

If the implementation does not support mixed-endian operation at any Exception level, this bit is RES1.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## When FEAT\_AA32EL0 is not implemented and ELIsInHost(EL2):

If HCR\_EL2.TGE == 0b0 , the field is IGNORED for all purposes other than direct reads and writes of the register.

Access to this field is RES1.

## Otherwise:

Reserved, RES0.

## ITD, bit [7]

## When FEAT\_AA32EL0 is implemented and ELIsInHost(EL2):

IT Disable. Disables some uses of IT instructions at EL0 using AArch32.

| ITD   | Meaning                                                           |
|-------|-------------------------------------------------------------------|
| 0b0   | All IT instruction functionality is enabled at EL0 using AArch32. |

| ITD   | Meaning                                                                        |
|-------|--------------------------------------------------------------------------------|
| 0b1   | Any attempt at EL0 using AArch32 to execute any of the following is UNDEFINED: |

- All encodings of the IT instruction with hw1[3:0]!=1000.
- All encodings of the subsequent instruction with the following values for hw1:
- 0b11xxxxxxxxxxxxxx : All 32-bit instructions, and the 16-bit instructions B, UDF, SVC, LDM, and STM.
- 0b1011xxxxxxxxxxxx : All instructions in 'Miscellaneous 16-bit instructions'.
- 0b10100xxxxxxxxxxx : ADDRd, PC, #imm
- 0b01001xxxxxxxxxxx : LDRRd, [PC, #imm]
- 0b0100x1xxx1111xxx : ADDRdn, PC; CMP Rn, PC; MOV Rd, PC; BX PC; BLX PC.
- 0b010001xx1xxxx111 : ADDPC, Rm; CMP PC, Rm; MOV PC, Rm. This pattern also covers UNPREDICTABLE cases with BLX Rn.

These instructions are always UNDEFINED, regardless of whether they would pass or fail the condition code check that applies to them as a result of being in an IT block.

It is IMPLEMENTATION DEFINED whether the IT instruction is treated as:

- A16-bit instruction, that can only be followed by another 16-bit instruction.
- The first half of a 32-bit instruction.

This means that, for the situations that are UNDEFINED, either the second 16-bit instruction or the 32-bit instruction is UNDEFINED.

An implementation might vary dynamically whether IT is treated as a 16-bit instruction or the first half of a 32-bit instruction.

If HCR\_EL2.TGE == 0b0 , the field is IGNORED for all purposes other than direct reads and writes of the register.

If an instruction in an active IT block that would be disabled by this field sets this field to 1, then behavior is CONSTRAINED UNPREDICTABLE. For more information see 'Changes to an ITD control by an instruction in an IT block'.

ITD is optional, but if it is implemented in the SCTLR\_EL2, then it must also be implemented in the SCTLR\_EL1, HSCTLR, and SCTLR.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

When an implementation does not implement ITD, access to this field is RAZ/WI.

## When FEAT\_AA32EL0 is not implemented and ELIsInHost(EL2):

Reserved, RES1.

## Otherwise:

Reserved, RES0.

## nAA, bit [6]

## When FEAT\_LSE2 is implemented:

Non-aligned access. This bit controls generation of Alignment faults under certain conditions at EL2, and, when the Effective value of HCR\_EL2.{E2H, TGE} is {1, 1}, EL0.

The following instructions generate an Alignment fault if all bytes being accessed are not within a single naturally aligned 16-byte quantity, for access:

- LDAPR, LDAPRH, LDAPUR, LDAPURH, LDAPURSH, LDAPURSW, LDAR, LDARH, LDLAR, LDLARH.
- STLLR, STLLRH, STLR, STLRH, STLUR, and STLURH.
- If FEAT\_LRCPC3 is implemented, the post index versions of LDAPR and the pre index versions of STLR.
- If FEAT\_LRCPC3 and Advanced SIMD and floating-point instructions are implemented, LDAPUR (SIMD&amp;FP), LDAP1 (SIMD&amp;FP), STLUR (SIMD&amp;FP), and STL1 (SIMD&amp;FP).

If FEAT\_LRCPC3 is implemented, the following instructions generate an Alignment fault if all bytes being accessed for a single register are not within a single naturally aligned 16-byte quantity, for access:

- LDIAPP, STILP.

| nAA   | Meaning                                                                              |
|-------|--------------------------------------------------------------------------------------|
| 0b0   | Unaligned accesses by the specified instructions generate an Alignment fault.        |
| 0b1   | Unaligned accesses by the specified instructions do not generate an Alignment fault. |

For a load-acquire instruction that does not have acquire semantics as the result of the destination register, or registers, being ZR, it is IMPLEMENTATION SPECIFIC whether this field behaves as 1 or the programmed value.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## CP15BEN, bit [5]

## When FEAT\_AA32EL0 is implemented and ELIsInHost(EL2):

System instruction memory barrier enable. Enables accesses to the DMB, DSB, and ISB System instructions in the (coproc== 0b1111 ) encoding space from EL0:

| CP15BEN   | Meaning                                                                                          |
|-----------|--------------------------------------------------------------------------------------------------|
| 0b0       | EL0 using AArch32: EL0 execution of the CP15DMB, CP15DSB, and CP15ISB instructions is UNDEFINED. |
| 0b1       | EL0 using AArch32: EL0 execution of the CP15DMB, CP15DSB, and CP15ISB instructions is enabled.   |

If HCR\_EL2.TGE == 0b0 , the field is IGNORED for all purposes other than direct reads and writes of the register.

CP15BEN is optional, but if it is implemented in the SCTLR\_EL2, then it must also be implemented in the SCTLR\_EL1, HSCTLR, and SCTLR.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## When FEAT\_AA32EL0 is not implemented and ELIsInHost(EL2):

Access to this field is RES0.

## Otherwise:

Reserved, RES1.

## SA0, bit [4]

## When ELIsInHost(EL2):

SP Alignment check enable for EL0. When set to 1, if a load or store instruction executed at EL0 uses the SP as the base address and the SP is not aligned to a 16-byte boundary, then an SP alignment fault exception is generated. For more information, see 'SP alignment checking'.

A, bit [1]

If HCR\_EL2.TGE == 0b0 , the field is IGNORED for all purposes other than direct reads and writes of the register.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES1.

## SA, bit [3]

SP Alignment check enable. When set to 1, if a load or store instruction executed at EL2 uses the SP as the base address and the SP is not aligned to a 16-byte boundary, then an SP alignment fault exception is generated. For more information, see 'SP alignment checking'.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## C, bit [2]

Data access Cacheability control, for accesses at EL2 and, when the Effective value of HCR\_EL2.{E2H, TGE} is {1, 1}, EL0

| C   | Meaning                                                                                                                                                                                                                                                                                                                                                                                                     |
|-----|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0 | The following are Non-cacheable for all levels of data and unified cache: • Data accesses to Normal memory from EL2. • When the Effective value of HCR_EL2.{E2H, TGE} is not {1, 1}, Normal memory accesses to the EL2 translation tables. • When the Effective value of HCR_EL2.{E2H, TGE} is {1, 1}: • Data accesses to Normal memory from EL0. • Normal memory accesses to the EL2&0 translation tables. |
| 0b1 | This control has no effect on the Cacheability of: • Data access to Normal memory from EL2. • When the Effective value of HCR_EL2.{E2H, TGE} is not {1, 1}, Normal memory accesses to the EL2 translation tables. • When the Effective value of HCR_EL2.{E2H, TGE} is {1, 1}: • Data accesses to Normal memory from EL0. • Normal memory accesses to the EL2&0 translation tables.                          |

This bit has no effect on the EL3 translation regime.

When EL2 is disabled in the current Security state or the Effective value of HCR\_EL2.{E2H, TGE} is not {1, 1}, this bit has no effect on the EL1&amp;0 translation regime.

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

Alignment check enable. This is the enable bit for Alignment fault checking at EL2 and, when the Effective value of HCR\_EL2.{E2H, TGE} is {1, 1}, EL0.

| A   | Meaning                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|-----|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0 | Alignment fault checking is disabled when executing at EL2. When the Effective value of HCR_EL2.{E2H, TGE} is {1, 1}, alignment fault checking disabled when executing at EL0. Alignment checks on some instructions are not disabled by this control. For more information, see 'Alignment of data accesses'.                                                                                                                                           |
| 0b1 | Alignment fault checking is enabled when executing at EL2. When the Effective value of HCR_EL2.{E2H, TGE} is {1, 1}, alignment fault checking enabled when executing at EL0. All instructions that load or store one or more registers have an alignment check that the address being accessed is aligned to the size of the data element(s) being accessed. If this check fails it causes an Alignment fault, which is taken as a Data Abort exception. |

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## M, bit [0]

MMUenable for EL2 or EL2&amp;0 stage 1 address translation.

| M   | Meaning                                                                                                                                                                                                                                                                                            |
|-----|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0 | When the Effective value of HCR_EL2.{E2H, TGE} is not {1, 1}, EL2 stage 1 address translation disabled. When the Effective value of HCR_EL2.{E2H, TGE} is {1, 1}, EL2&0 stage 1 address translation disabled. See the SCTLR_EL2.I field for the behavior of instruction accesses to Normal memory. |
| 0b1 | When the Effective value of HCR_EL2.{E2H, TGE} is not {1, 1}, EL2 stage 1 address translation enabled. When the Effective value of HCR_EL2.{E2H, TGE} is {1, 1}, EL2&0 stage 1 address translation enabled.                                                                                        |

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Accessing SCTLR\_EL2

When the Effective value of HCR\_EL2.E2H is 1, without explicit synchronization, accesses from EL2 using the accessor name SCTLR\_EL2 or SCTLR\_EL1 are not guaranteed to be ordered with respect to accesses using the other accessor name.

If FEAT\_SRMASK is implemented, accesses to SCTLR\_EL2 are masked by SCTLRMASK\_EL2.

Accesses to this register use the following encodings in the System register encoding space:

MRS &lt;Xt&gt;, SCTLR\_EL2

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b100 | 0b0001 | 0b0000 | 0b000 |

```
if !IsFeatureImplemented(FEAT_AA64) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EffectiveHCR_EL2_NVx() IN {'xx1'} then AArch64.SystemAccessTrap(EL2, 0x18); else UNDEFINED; elsif PSTATE.EL == EL2 then X[t, 64] = SCTLR_EL2; elsif PSTATE.EL == EL3 then X[t, 64] = SCTLR_EL2;
```

MSR SCTLR\_EL2, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b100 | 0b0001 | 0b0000 | 0b000 |

```
if !IsFeatureImplemented(FEAT_AA64) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EffectiveHCR_EL2_NVx() IN {'xx1'} then AArch64.SystemAccessTrap(EL2, 0x18); else UNDEFINED; elsif PSTATE.EL == EL2 then if IsFeatureImplemented(FEAT_SRMASK) then SCTLR_EL2 = (X[t, 64] AND NOT EffectiveSCTLRMASK_EL2()) OR (SCTLR_EL2 AND ↪ → EffectiveSCTLRMASK_EL2()); else SCTLR_EL2 = X[t, 64]; elsif PSTATE.EL == EL3 then SCTLR_EL2 = X[t, 64];
```

When FEAT\_VHE is implemented MRS &lt;Xt&gt;, SCTLR\_EL1

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b000 | 0b0001 | 0b0000 | 0b000 |

```
if !IsFeatureImplemented(FEAT_AA64) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EL2Enabled() && HCR_EL2.TRVM == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') ↪ → && HFGRTR_EL2.SCTLR_EL1 == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EffectiveHCR_EL2_NVx() IN {'111'} then X[t, 64] = NVMem[0x110]; else X[t, 64] = SCTLR_EL1; elsif PSTATE.EL == EL2 then if ELIsInHost(EL2) then X[t, 64] = SCTLR_EL2; else X[t, 64] = SCTLR_EL1; elsif PSTATE.EL == EL3 then X[t, 64] = SCTLR_EL1;
```

When FEAT\_VHE is implemented MSR SCTLR\_EL1, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b000 | 0b0001 | 0b0000 | 0b000 |

```
if !IsFeatureImplemented(FEAT_AA64) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EL2Enabled() && HCR_EL2.TVM == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') ↪ → && HFGWTR_EL2.SCTLR_EL1 == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EffectiveHCR_EL2_NVx() IN {'111'} then NVMem[0x110] = X[t, 64]; else if IsFeatureImplemented(FEAT_SRMASK) then SCTLR_EL1 = (X[t, 64] AND NOT EffectiveSCTLRMASK_EL1()) OR (SCTLR_EL1 AND ↪ → EffectiveSCTLRMASK_EL1()); else SCTLR_EL1 = X[t, 64]; elsif PSTATE.EL == EL2 then if ELIsInHost(EL2) then if IsFeatureImplemented(FEAT_SRMASK) then SCTLR_EL2 = (X[t, 64] AND NOT EffectiveSCTLRMASK_EL2()) OR (SCTLR_EL2 AND ↪ → EffectiveSCTLRMASK_EL2()); else SCTLR_EL2 = X[t, 64]; else SCTLR_EL1 = X[t, 64]; elsif PSTATE.EL == EL3 then SCTLR_EL1 = X[t, 64];
```