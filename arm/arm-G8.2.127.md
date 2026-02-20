## G8.2.127 SCTLR, System Control Register

The SCTLR characteristics are:

## Purpose

Provides the top-level control of the system, including its memory system.

## Configuration

Some bits in the register are read-only. These bits relate to non-configurable features of an implementation, and are provided for compatibility with previous versions of the architecture.

AArch32 System register SCTLR bits [31:0] are architecturally mapped to AArch64 System register SCTLR\_EL1[31:0].

This register is banked between SCTLR and SCTLR\_S and SCTLR\_NS.

This register is present only when FEAT\_AA32EL1 is implemented. Otherwise, direct accesses to SCTLR are UNDEFINED.

## Attributes

SCTLR is a 32-bit register.

This register has the following instances:

- SCTLR, when EL3 is not implemented or FEAT\_AA64 is implemented.
- SCTLR\_S, when FEAT\_AA32EL3 is implemented.
- SCTLR\_NS, when FEAT\_AA32EL3 is implemented.

## Field descriptions

<!-- image -->

DSSBS, bit [31]

## When FEAT\_SSBS is implemented:

Default PSTATE.SSBS value on Exception Entry. The defined values are:

| DSSBS   | Meaning                                                                                    |
|---------|--------------------------------------------------------------------------------------------|
| 0b0     | PSTATE.SSBS is set to 0 on an exception to any mode in this security state except Hyp mode |
| 0b1     | PSTATE.SSBS is set to 1 on an exception to any mode in this security state except Hyp mode |

Note

When EL3 is implemented and is using AArch32, this bit is banked between the two Security states.

The reset behavior of this field is:

- On a Warm reset, this field resets to an IMPLEMENTATION DEFINED value.

## Otherwise:

Reserved, RES0.

## TE, bit [30]

T32 Exception Enable. This bit controls whether exceptions to an Exception level that is executing at PL1 are taken to A32 or T32 state:

| TE   | Meaning                                          |
|------|--------------------------------------------------|
| 0b0  | Exceptions, including reset, taken to A32 state. |
| 0b1  | Exceptions, including reset, taken to T32 state. |

The reset behavior of this field is:

- On a Warm reset, this field resets to an IMPLEMENTATION DEFINED value.

## AFE, bit [29]

Access Flag Enable. When using the Short-descriptor translation table format for the PL1&amp;0 translation regime, this bit enables use of the AP[0] bit in the translation descriptors as the Access flag, and restricts access permissions in the translation descriptors to the simplified model.

| AFE   | Meaning                                                                                                                                                     |
|-------|-------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0   | In the Translation table descriptors, AP[0] is an access permissions bit. The full range of access permissions is supported. No Access flag is implemented. |
| 0b1   | In the Translation table descriptors, AP[0] is the Access flag. Only the simplified model for access permissions is supported.                              |

When using the Long-descriptor translation table format, the VMSA behaves as if this bit is set to 1, regardless of the value of this bit.

The AFE bit is permitted to be cached in a TLB.

The reset behavior of this field is:

- On a Warm reset, this field resets to '0' .

## TRE, bit [28]

TEX remap enable. This bit enables remapping of the TEX[2:1] bits in the PL1&amp;0 translation regime for use as two translation table bits that can be managed by the operating system. Enabling this remapping also changes the scheme used to describe the memory region attributes in the VMSA.

| TRE   | Meaning                                                                                                                                                                                              |
|-------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0   | TEX remap disabled. TEX[2:0] are used, with the Cand Bbits, to describe the memory region attributes.                                                                                                |
| 0b1   | TEX remap enabled. TEX[2:1] are reassigned for use as bits managed by the operating system. The TEX[0], C, and Bbits are used to describe the memory region attributes, with the MMUremap registers. |

When the value of TTBCR.EAE is 1, this bit is RES1.

The TRE bit is permitted to be cached in a TLB.

The reset behavior of this field is:

- On a Warm reset, this field resets to '0' .

## Bits [27:26]

Reserved, RES0.

## EE, bit [25]

The value of the PSTATE.E bit on branch to an exception vector or coming out of reset, and the endianness of stage 1 translation table walks in the PL1&amp;0 translation regime.

| EE   | Meaning                                                                                                                                                                   |
|------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0  | Little-endian. PSTATE.E is cleared to 0 on taking an exception or coming out of reset. Stage 1 translation table walks in the PL1&0 translation regime are little-endian. |
| 0b1  | Big-endian. PSTATE.E is set to 1 on taking an exception or coming out of reset. Stage 1 translation table walks in the PL1&0 translation regime are big-endian.           |

If an implementation does not provide Big-endian support for data accesses at Exception levels higher than EL0, this bit is RES0.

If an implementation does not provide Little-endian support for data accesses at Exception levels higher than EL0, this bit is RES1.

The reset behavior of this field is:

- On a Warm reset, this field resets to an IMPLEMENTATION DEFINED value.

## Bit [24]

Reserved, RES0.

## SPAN, bit [23]

## When FEAT\_PAN is implemented:

Set Privileged Access Never, on taking an exception to EL1 from either Secure or Non-secure state, or to EL3 from Secure state when EL3 is using AArch32.

| SPAN   | Meaning                                                                  |
|--------|--------------------------------------------------------------------------|
| 0b0    | PSTATE.PAN is set to 1 in the following situations:                      |
| 0b1    | The value of PSTATE.PAN is left unchanged on taking an exception to EL1. |

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES1.

## Bit [22]

Reserved, RES1.

## Bit [21]

Reserved, RES0.

## UWXN,bit [20]

Unprivileged write permission implies PL1 XN (Execute-never). This bit can force all memory regions that are writable at PL0 to be treated as XN for accesses from software executing at PL1.

| UWXN   | Meaning                                                                                     |
|--------|---------------------------------------------------------------------------------------------|
| 0b0    | This control has no effect on memory access permissions.                                    |
| 0b1    | Any region that is writable at PL0 forced to XNfor accesses from software executing at PL1. |

The UWXN bit is permitted to be cached in a TLB.

The reset behavior of this field is:

- On a Warm reset, this field resets to '0' .

## WXN,bit [19]

Write permission implies XN (Execute-never). For the PL1&amp;0 translation regime, this bit can force all memory regions that are writable to be treated as XN.

| WXN   | Meaning                                                                                                                        |
|-------|--------------------------------------------------------------------------------------------------------------------------------|
| 0b0   | This control has no effect on memory access permissions.                                                                       |
| 0b1   | Any region that is writable in the PL1&0 translation regime is forced to XNfor accesses from software executing at PL1 or PL0. |

This bit applies only when SCTLR.M bit is set.

The WXN bit is permitted to be cached in a TLB.

The reset behavior of this field is:

nTWE

0b0

0b1

- On a Warm reset, this field resets to '0' .

## nTWE, bit [18]

Traps EL0 execution of WFE instructions to Undefined mode.

Meaning

Any attempt to execute a WFE instruction at EL0 is trapped to Undefined mode, if the instruction would otherwise have caused the PE to enter a low-power state.

This control does not cause any instructions to be trapped.

The attempted execution of a conditional WFE instruction is only trapped if the instruction passes its condition code check.

Note

Since a WFE or WFI can complete at any time, even without a Wakeup event, the traps on WFE of WFI are not guaranteed to be taken, even if the WFE or WFI is executed when there is no Wakeup event. The only guarantee is that if the instruction does not complete in finite time in the absence of a Wakeup event, the trap will be taken.

The reset behavior of this field is:

- On a Warm reset, this field resets to '1' .

## Bit [17]

Reserved, RES0.

## nTWI, bit [16]

Traps EL0 execution of WFI instructions to Undefined mode.

| nTWI   | Meaning                                                                                                                                                         |
|--------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0    | Any attempt to execute a WFI instruction at EL0 is trapped to Undefined mode, if the instruction would otherwise have caused the PE to enter a low-power state. |
| 0b1    | This control does not cause any instructions to be trapped.                                                                                                     |

The attempted execution of a conditional WFI instruction is only trapped if the instruction passes its condition code check.

Note

Since a WFE or WFI can complete at any time, even without a Wakeup event, the traps on WFE of WFI are not guaranteed to be taken, even if the WFE or WFI is executed when there is no Wakeup event. The only guarantee is that if the instruction does not complete in finite time in the absence of a Wakeup event, the trap will be taken.

The reset behavior of this field is:

- On a Warm reset, this field resets to '1' .

## Bits [15:14]

Reserved, RES0.

## V, bit [13]

Vectors bit. This bit selects the base address of the exception vectors for exceptions taken to a PE mode other than Monitor mode or Hyp mode:

| V   | Meaning                                                                                          |
|-----|--------------------------------------------------------------------------------------------------|
| 0b0 | Normal exception vectors. Base address is held in VBAR.                                          |
| 0b1 | High exception vectors (Hivecs), base address 0xFFFF0000 . This base address cannot be remapped. |

The reset behavior of this field is:

- On a Warm reset, this field resets to an IMPLEMENTATION DEFINED value.

## I, bit [12]

Instruction access Cacheability control, for accesses at EL1 and EL0:

| I   | Meaning                                                                                                                                                                                                                                                                                                      |
|-----|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0 | All instruction access to Normal memory from PL1 and PL0 are Non-cacheable for all levels of instruction and unified cache. If the value of SCTLR.M is 0, instruction accesses from stage 1 of the PL1&0 translation regime are to Normal, Outer Shareable, Inner Non-cacheable, Outer Non-cacheable memory. |
| 0b1 | All instruction access to Normal memory from PL1 and PL0 can be cached at all levels of instruction and unified cache. If the value of SCTLR.M is 0, instruction accesses from stage 1 of the PL1&0 translation regime are to Normal, Outer Shareable, Inner Write-Through, Outer Write-Through memory.      |

Instruction accesses to Normal memory from EL1 and EL0 are Cacheable regardless of the value of the SCTLR.I bit if either:

- EL2 is using AArch32 and the value of HCR.DC is 1.
- EL2 is using AArch64 and the value of HCR\_EL2.DC is 1.

The reset behavior of this field is:

- On a Warm reset, this field resets to '0' .

## Bit [11]

Reserved, RES1.

## EnRCTX, bit [10]

## When FEAT\_SPECRES is implemented:

Enable EL0 access to the following System instructions:

- CFPRCTX.
- DVPRCTX.
- CPPRCTX.
- If FEAT\_SPECRES2 is implemented, COSPRCTX.

| EnRCTX   | Meaning                                                                                  |
|----------|------------------------------------------------------------------------------------------|
| 0b0      | EL0 access to these instructions is disabled, and these instructions are trapped to EL1. |
| 0b1      | EL0 access to these instructions is enabled.                                             |

Note

When EL3 is implemented and is using AArch32, this bit is banked between the two Security states.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## Bit [9]

Reserved, RES0.

## SED, bit [8]

SETEND instruction disable. Disables SETEND instructions at PL0 and PL1.

| SED   | Meaning                                                 |
|-------|---------------------------------------------------------|
| 0b0   | SETEND instruction execution is enabled at PL0 and PL1. |
| 0b1   | SETEND instructions are UNDEFINED at PL0 and PL1.       |

If the implementation does not support mixed-endian operation at any Exception level, this bit is RES1.

The reset behavior of this field is:

- On a Warm reset, this field resets to '0' .

## ITD, bit [7]

IT Disable. Disables some uses of IT instructions at PL1 and PL0.

| ITD   | Meaning                                                     |
|-------|-------------------------------------------------------------|
| 0b0   | All IT instruction functionality is enabled at PL1 and PL0. |

| ITD   | Meaning                                                                 |
|-------|-------------------------------------------------------------------------|
| 0b1   | Any attempt at PL1 or PL0 to execute any of the following is UNDEFINED: |

- All encodings of the IT instruction with hw1[3:0]!=1000.
- All encodings of the subsequent instruction with the following values for hw1:
- 0b11xxxxxxxxxxxxxx : All 32-bit instructions, and the 16-bit instructions B, UDF, SVC, LDM, and STM.
- 0b1011xxxxxxxxxxxx : All instructions in 'Miscellaneous 16-bit instructions'.
- 0b10100xxxxxxxxxxx : ADDRd, PC, #imm
- 0b01001xxxxxxxxxxx : LDRRd, [PC, #imm]
- 0b0100x1xxx1111xxx : ADDRdn, PC; CMP Rn, PC; MOV Rd, PC; BX PC; BLX PC.
- 0b010001xx1xxxx111 : ADDPC, Rm; CMP PC, Rm; MOV PC, Rm. This pattern also covers unpredictable cases with BLX Rn.

These instructions are always UNDEFINED, regardless of whether they would pass or fail the condition code check that applies to them as a result of being in an IT block.

It is IMPLEMENTATION DEFINED whether the IT instruction is treated as:

- A16-bit instruction, that can only be followed by another 16-bit instruction.
- The first half of a 32-bit instruction.

This means that, for the situations that are UNDEFINED, either the second 16-bit instruction or the 32-bit instruction is UNDEFINED.

An implementation might vary dynamically as to whether IT is treated as a 16-bit instruction or the first half of a 32-bit instruction.

If an instruction in an active IT block that would be disabled by this field sets this field to 1, then behavior is CONSTRAINED UNPREDICTABLE. For more information see 'Changes to an ITD control by an instruction in an IT block'.

ITD is optional, but if it is implemented in the SCTLR, then it must also be implemented in the SCTLR\_EL1, SCTLR\_EL2, and HSCTLR.

The reset behavior of this field is:

- On a Warm reset, this field resets to '0' .

When an implementation does not implement ITD, access to this field is RAZ/WI.

## UNK, bit [6]

Writes to this bit are IGNORED. Reads of this bit return an UNKNOWN value.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## CP15BEN, bit [5]

System instruction memory barrier enable. Enables accesses to the DMB, DSB, and ISB System instructions in the (coproc== 0b1111 ) encoding space from PL1 and PL0:

| CP15BEN   | Meaning                                                                               |
|-----------|---------------------------------------------------------------------------------------|
| 0b0       | PL0 and PL1 execution of the CP15DMB, CP15DSB, and CP15ISB instructions is UNDEFINED. |
| 0b1       | PL0 and PL1 execution of the CP15DMB, CP15DSB, and CP15ISB instructions is enabled.   |

CP15BEN is optional, but if it is implemented in the SCTLR, then it must also be implemented in the SCTLR\_EL1, SCTLR\_EL2, and HSCTLR.

The reset behavior of this field is:

- On a Warm reset, this field resets to '1' .

When an implementation does not implement CP15BEN, access to this field is RAO/WI.

## LSMAOE, bit [4]

## When FEAT\_LSMAOC is implemented:

Load Multiple and Store Multiple Atomicity and Ordering Enable.

| LSMAOE   | Meaning                                                                                                                                                                                                      |
|----------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0      | For all memory accesses at EL1 or EL0, T32 and A32 Load Multiple and Store Multiple can have an interrupt taken during the sequence memory accesses, and the memory accesses are not required to be ordered. |
| 0b1      | The ordering and interrupt behavior of T32 and A32 Load Multiple and Store Multiple at EL1 or EL0 is as defined for Armv8.0.                                                                                 |

This bit is permitted to be cached in a TLB.

The reset behavior of this field is:

- On a Warm reset, this field resets to '1' .

## Otherwise:

Reserved, RES1.

## nTLSMD, bit [3]

## When FEAT\_LSMAOC is implemented:

No Trap Load Multiple and Store Multiple to Device-nGRE/Device-nGnRE/Device-nGnRnE memory.

| nTLSMD   | Meaning                                                                                                                                                                                                           |
|----------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0      | All memory accesses by T32 and A32 Load Multiple and Store Multiple at EL1 or EL0 that are marked at stage 1 as Device-nGRE/Device-nGnRE/Device-nGnRnE memory are trapped and generate a stage 1 Alignment fault. |
| 0b1      | All memory accesses by T32 and A32 Load Multiple and Store Multiple at EL1 or EL0 that are marked at stage 1 as Device-nGRE/Device-nGnRE/Device-nGnRnE memory are not trapped.                                    |

This bit is permitted to be cached in a TLB.

The reset behavior of this field is:

- On a Warm reset, this field resets to '1' .

## Otherwise:

Reserved, RES1.

## C, bit [2]

Cacheability control, for data accesses at EL1 and EL0:

| C   | Meaning                                                                                                                                                                  |
|-----|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0 | All data access to Normal memory from PL1 and PL0, and all accesses to the PL1&0 stage 1 translation tables, are Non-cacheable for all levels of data and unified cache. |
| 0b1 | All data access to Normal memory from PL1 and PL0, and all accesses to the PL1&0 stage 1 translation tables, can be cached at all levels of data and unified cache.      |

The PE ignores SCTLR.C, and data accesses to Normal memory from EL1 and EL0 are Cacheable, if either:

- EL2 is using AArch32 and the value of HCR.DC is 1.
- EL2 is using AArch64 and the value of HCR\_EL2.DC is 1.

The reset behavior of this field is:

- On a Warm reset, this field resets to '0' .

## A, bit [1]

Alignment check enable. This is the enable bit for Alignment fault checking at PL1 and PL0:

| A   | Meaning                                                                                                                                                                                                                                                                                                                                    |
|-----|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0 | Alignment fault checking disabled when executing at PL1 or PL0. Instructions that load or store one or more registers, other than load/store exclusive and load-acquire/store-release, do not check that the address being accessed is aligned to the size of the data element(s) being accessed.                                          |
| 0b1 | Alignment fault checking enabled when executing at PL1 or PL0. All instructions that load or store one or more registers have an alignment check that the address being accessed is aligned to the size of the data element(s) being accessed. If this check fails it causes an Alignment fault, which is taken as a Data Abort exception. |

Load/store exclusive and load-acquire/store-release instructions have an alignment check regardless of the value of the A bit.

The reset behavior of this field is:

- On a Warm reset, this field resets to '0' .

## M, bit [0]

MMUenable for EL1 and EL0 stage 1 address translation. Possible values of this bit are:

| M   | Meaning                                                                                                                            |
|-----|------------------------------------------------------------------------------------------------------------------------------------|
| 0b0 | EL1 and EL0 stage 1 address translation disabled. See the SCTLR.I field for the behavior of instruction accesses to Normal memory. |
| 0b1 | EL1 and EL0 stage 1 address translation enabled.                                                                                   |

The PE behaves as if the value of the SCTLR.M field is 0 for all purposes other than returning the value of a direct read of the field if either:

- EL2 is using AArch32 and the value of HCR.{DC, TGE} is not {0, 0}.

- EL2 is using AArch64 and the value of HCR\_EL2.{DC, TGE} is not {0, 0}.

The reset behavior of this field is:

- On a Warm reset, this field resets to '0' .

## Accessing SCTLR

Accesses to this register use the following encodings in the System register encoding space:

```
MRC{<c>}{<q>} <coproc>, {#}<opc1>, <Rt>, <CRn>, <CRm>{, {#}<opc2>}
```

| coproc   | opc1   | CRn    | CRm    | opc2   |
|----------|--------|--------|--------|--------|
| 0b1111   | 0b000  | 0b0001 | 0b0000 | 0b000  |

```
if !IsFeatureImplemented(FEAT_AA32EL1) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && HSTR_EL2.T1 == '1' ↪ → then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HSTR.T1 == '1' ↪ → then AArch32.TakeHypTrapException(0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && HCR_EL2.TRVM == ↪ → '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HCR.TRVM == '1' ↪ → then AArch32.TakeHypTrapException(0x03); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA32EL3) && ELUsingAArch32(EL3) then R[t] = SCTLR_NS; else R[t] = SCTLR; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && IsFeatureImplemented(FEAT_AA32EL3) && ELUsingAArch32(EL3) then R[t] = SCTLR_NS; else R[t] = SCTLR; elsif PSTATE.EL == EL3 then if SCR.NS == '0' then R[t] = SCTLR_S; else R[t] = SCTLR_NS;
```

```
MCR{<c>}{<q>} <coproc>, {#}<opc1>, <Rt>, <CRn>, <CRm>{, {#}<opc2>}
```

| coproc   | opc1   | CRn    | CRm    | opc2   |
|----------|--------|--------|--------|--------|
| 0b1111   | 0b000  | 0b0001 | 0b0000 | 0b000  |

```
if !IsFeatureImplemented(FEAT_AA32EL1) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && HSTR_EL2.T1 == '1' ↪ → then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HSTR.T1 == '1' ↪ → then AArch32.TakeHypTrapException(0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && HCR_EL2.TVM == ↪ → '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HCR.TVM == '1' ↪ → then AArch32.TakeHypTrapException(0x03); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA32EL3) && ELUsingAArch32(EL3) then SCTLR_NS = R[t]; else SCTLR = R[t]; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && IsFeatureImplemented(FEAT_AA32EL3) && ELUsingAArch32(EL3) then SCTLR_NS = R[t]; else SCTLR = R[t]; elsif PSTATE.EL == EL3 then if SCR.NS == '0' && CP15SDISABLE == HIGH then UNDEFINED; elsif SCR.NS == '0' && CP15SDISABLE2 == HIGH then UNDEFINED; else if SCR.NS == '0' then SCTLR_S = R[t]; else SCTLR_NS = R[t];
```