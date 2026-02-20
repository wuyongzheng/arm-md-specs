## G8.2.73 HSCTLR, Hyp System Control Register

The HSCTLR characteristics are:

## Purpose

Provides top-level control of the system operation in Hyp mode.

## Configuration

If EL2 is not implemented, this register is RES0 from EL3.

AArch32 System register HSCTLR bits [31:0] are architecturally mapped to AArch64 System register SCTLR\_EL2[31:0].

This register is present only when FEAT\_AA32EL2 is implemented. Otherwise, direct accesses to HSCTLR are UNDEFINED.

## Attributes

HSCTLR is a 32-bit register.

## Field descriptions

<!-- image -->

## DSSBS, bit [31]

## When FEAT\_SSBS is implemented:

Default PSTATE.SSBS value on Exception Entry. The defined values are:

| DSSBS   | Meaning                                              |
|---------|------------------------------------------------------|
| 0b0     | PSTATE.SSBS is set to 0 on an exception to Hyp mode. |
| 0b1     | PSTATE.SSBS is set to 1 on an exception to Hyp mode. |

The reset behavior of this field is:

- On a Warm reset, this field resets to an IMPLEMENTATION DEFINED value.

## Otherwise:

Reserved, RES0.

## TE, bit [30]

T32 Exception Enable. This bit controls whether exceptions to EL2 are taken to A32 or T32 state:

| TE   | Meaning                                          |
|------|--------------------------------------------------|
| 0b0  | Exceptions, including reset, taken to A32 state. |
| 0b1  | Exceptions, including reset, taken to T32 state. |

The reset behavior of this field is:

- On a Warm reset, this field resets to an IMPLEMENTATION DEFINED value.

## Bits [29:28]

Reserved, RES1.

## Bits [27:26]

Reserved, RES0.

## EE, bit [25]

## When FEAT\_MixedEnd is implemented:

The value of the PSTATE.E bit on entry to Hyp mode, the endianness of stage 1 translation table walks in the EL2 translation regime, and the endianness of stage 2 translation table walks in the PL1&amp;0 translation regime.

| EE   | Meaning                                                                                                                                                                                                             |
|------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0  | Little-endian. PSTATE.E is cleared to 0 on entry to Hyp mode. Stage 1 translation table walks in the EL2 translation regime, and stage 2 translation table walks in the PL1&0 translation regime are little-endian. |
| 0b1  | Big-endian. PSTATE.E is set to 1 on entry to Hyp mode. Stage 1 translation table walks in the EL2 translation regime, and stage 2 translation table walks in the PL1&0 translation regime are big-endian.           |

The reset behavior of this field is:

- On a Warm reset, this field resets to an IMPLEMENTATION DEFINED value.

## When FEAT\_BigEnd is implemented:

Explicit data accesses at EL1, and stage 1 translation table walks in the EL1&amp;0 translation regime are big-endian.

Reserved, RES1.

## Otherwise:

Explicit data accesses at EL1, and stage 1 translation table walks in the EL1&amp;0 translation regime are little-endian.

Reserved, RES0.

## Bit [24]

Reserved, RES0.

## Bits [23:22]

Reserved, RES1.

## Bits [21:20]

Reserved, RES0.

## WXN,bit [19]

Write permission implies XN (Execute-never). For the EL2 translation regime, this bit can force all memory regions that are writable to be treated as XN.

| WXN   | Meaning                                                                                                               |
|-------|-----------------------------------------------------------------------------------------------------------------------|
| 0b0   | This control has no effect on memory access permissions.                                                              |
| 0b1   | Any region that is writable in the EL2 translation regime is forced to XNfor accesses from software executing at EL2. |

This bit applies only when HSCTLR.M bit is set.

This bit is permitted to be cached in a TLB.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Bit [18]

Reserved, RES1.

## Bit [17]

Reserved, RES0.

## Bit [16]

Reserved, RES1.

## Bits [15:13]

Reserved, RES0.

## I, bit [12]

Instruction access Cacheability control, for accesses at EL2:

| I   | Meaning                                                                                                                                                                                                                                                                                             |
|-----|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0 | All instruction access to Normal memory from EL2 are Non-cacheable for all levels of instruction and unified cache. If the value of HSCTLR.M is 0, instruction accesses from stage 1 of the EL2 translation regime are to Normal, Outer Shareable, Inner Non-cacheable, Outer Non-cacheable memory. |
| 0b1 | All instruction access to Normal memory from EL2 can be cached at all levels of instruction and unified cache. If the value of HSCTLR.M is 0, instruction accesses from stage 1 of the EL2 translation regime are to Normal, Outer Shareable, Inner Write-Through, Outer Write-Through memory.      |

This bit has no effect on the PL1&amp;0 translation regime.

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Bit [11]

Reserved, RES1.

## Bits [10:9]

Reserved, RES0.

## SED, bit [8]

SETEND instruction disable. Disables SETEND instructions at EL2.

| SED   | Meaning                                         |
|-------|-------------------------------------------------|
| 0b0   | SETEND instruction execution is enabled at EL2. |
| 0b1   | SETEND instructions are UNDEFINED at EL2.       |

If the implementation does not support mixed-endian operation at EL2, this bit is RES1.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## ITD, bit [7]

IT Disable. Disables some uses of IT instructions at EL2.

| ITD   | Meaning                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|-------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0   | All IT instruction functionality is enabled at EL2.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| 0b1   | Any attempt at EL2 to execute any of the following is UNDEFINED: • All encodings of the IT instruction with hw1[3:0]!=1000. • All encodings of the subsequent instruction with the following values for hw1: • 0b11xxxxxxxxxxxxxx : All 32-bit instructions, and the 16-bit instructions B, UDF, SVC, LDM, and STM. • 0b1011xxxxxxxxxxxx : All instructions in 'Miscellaneous 16-bit instructions'. • 0b10100xxxxxxxxxxx : ADDRd, PC, #imm • 0b01001xxxxxxxxxxx : LDRRd, [PC, #imm] • 0b0100x1xxx1111xxx : ADDRdn, PC; CMPRn, PC; MOVRd,PC; BXPC; BLXPC. • 0b010001xx1xxxx111 : ADDPC, Rm; CMPPC, Rm; MOVPC,Rm. This pattern also covers unpredictable cases with BLXRn. These instructions are always UNDEFINED, regardless of whether they would pass or fail the condition code check that applies to them as a result of being in an IT block. It is IMPLEMENTATION DEFINED whether the IT instruction is treated as: • A16-bit instruction, that can only be followed by another 16-bit instruction. • The first half of a 32-bit instruction. This means that, for the situations that are UNDEFINED, either the second 16-bit instruction or the 32-bit instruction is UNDEFINED. An implementation might vary dynamically as to whether IT is treated as a 16-bit instruction or the first half of a 32-bit instruction. |

If an instruction in an active IT block that would be disabled by this field sets this field to 1, then behavior is CONSTRAINED UNPREDICTABLE. For more information, see 'Changes to an ITD control by an instruction in an IT block'.

ITD is optional, but if it is implemented in the HSCTLR, then it must also be implemented in the SCTLR\_EL1, SCTLR\_EL2, and SCTLR.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

When an implementation does not implement ITD, access to this field is RAZ/WI.

## Bit [6]

Reserved, RES0.

## CP15BEN, bit [5]

System instruction memory barrier enable. Enables accesses to the DMB, DSB, and ISB System instructions in the (coproc== 0b1111 ) encoding space from EL2:

| CP15BEN   | Meaning                                                                       |
|-----------|-------------------------------------------------------------------------------|
| 0b0       | EL2 execution of the CP15DMB, CP15DSB, and CP15ISB instructions is UNDEFINED. |
| 0b1       | EL2 execution of the CP15DMB, CP15DSB, and CP15ISB instructions is enabled.   |

CP15BEN is optional, but if it is implemented in the HSCTLR, then it must also be implemented in the SCTLR\_EL1, SCTLR\_EL2, and SCTLR.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

When an implementation does not implement CP15BEN, access to this field is RAO/WI.

## LSMAOE, bit [4]

## When FEAT\_LSMAOC is implemented:

Load Multiple and Store Multiple Atomicity and Ordering Enable.

| LSMAOE   | Meaning                                                                                                                                                                                               |
|----------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0      | For all memory accesses at EL2, T32 and A32 Load Multiple and Store Multiple can have an interrupt taken during the sequence memory accesses, and the memory accesses are not required to be ordered. |
| 0b1      | The ordering and interrupt behavior of T32 and A32 Load Multiple and Store Multiple at EL2 is as defined for Armv8.0.                                                                                 |

This bit is permitted to be cached in a TLB.

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '1' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES1.

## nTLSMD, bit [3]

## When FEAT\_LSMAOC is implemented:

No Trap Load Multiple and Store Multiple to Device-nGRE/Device-nGnRE/Device-nGnRnE memory.

| nTLSMD   | Meaning                                                                                                                                                                                                    |
|----------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0      | All memory accesses by T32 and A32 Load Multiple and Store Multiple at EL2 that are marked at stage 1 as Device-nGRE/Device-nGnRE/Device-nGnRnE memory are trapped and generate a stage 1 Alignment fault. |
| 0b1      | All memory accesses by T32 and A32 Load Multiple and Store Multiple at EL2 that are marked at stage 1 as Device-nGRE/Device-nGnRE/Device-nGnRnE memory are not trapped.                                    |

This bit is permitted to be cached in a TLB.

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '1' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES1.

## C, bit [2]

Cacheability control, for data accesses at EL2:

| C   | Meaning                                                                                                                                                |
|-----|--------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0 | All data access to Normal memory from EL2, and all accesses to the EL2 translation tables, are Non-cacheable for all levels of data and unified cache. |
| 0b1 | All data access to Normal memory from EL2, and all accesses to the EL2 translation tables, can be cached at all levels of data and unified cache.      |

This bit has no effect on the PL1&amp;0 translation regime.

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## A, bit [1]

Alignment check enable. This is the enable bit for Alignment fault checking at EL2:

| A   | Meaning                                                                                                                                                                                                                                                                                                                                           |
|-----|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0 | Alignment fault checking disabled when executing at EL2. Instructions that load or store one or more registers, other than load/store exclusive and load-acquire/store-release, do not check that the address being accessed is aligned to the size of the data element or data elements being accessed.                                          |
| 0b1 | Alignment fault checking enabled when executing at EL2. All instructions that load or store one or more registers have an alignment check that the address being accessed is aligned to the size of the data element or data elements being accessed. If this check fails it causes an Alignment fault, which is taken as a Data Abort exception. |

Load/store exclusive and load-acquire/store-release instructions have an alignment check regardless of the value of the A bit.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## M, bit [0]

MMUenable for EL2 stage 1 address translation. Possible values of this bit are:

| M   | Meaning                                                                                                                     |
|-----|-----------------------------------------------------------------------------------------------------------------------------|
| 0b0 | EL2 stage 1 address translation disabled. See the HSCTLR.I field for the behavior of instruction accesses to Normal memory. |
| 0b1 | EL2 stage 1 address translation enabled.                                                                                    |

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Accessing HSCTLR

Accesses to this register use the following encodings in the System register encoding space:

```
MRC{<c>}{<q>} <coproc>, {#}<opc1>, <Rt>, <CRn>, <CRm>{, {#}<opc2>}
```

| coproc   | opc1   | CRn    | CRm    | opc2   |
|----------|--------|--------|--------|--------|
| 0b1111   | 0b100  | 0b0001 | 0b0000 | 0b000  |

```
if !IsFeatureImplemented(FEAT_AA32EL2) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && HSTR_EL2.T1 == '1' ↪ → then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HSTR.T1 == '1' ↪ → then AArch32.TakeHypTrapException(0x03);
```

else

```
UNDEFINED; elsif PSTATE.EL == EL2 then R[t] = HSCTLR; elsif PSTATE.EL == EL3 then if SCR.NS == '0' then UNDEFINED; else R[t] = HSCTLR;
```

MCR{&lt;c&gt;}{&lt;q&gt;} &lt;coproc&gt;, {#}&lt;opc1&gt;, &lt;Rt&gt;, &lt;CRn&gt;, &lt;CRm&gt;{, {#}&lt;opc2&gt;}

| coproc   | opc1   | CRn    | CRm    | opc2   |
|----------|--------|--------|--------|--------|
| 0b1111   | 0b100  | 0b0001 | 0b0000 | 0b000  |

if !IsFeatureImplemented(FEAT\_AA32EL2) then

UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EL2Enabled() &amp;&amp; IsFeatureImplemented(FEAT\_AA64EL2) &amp;&amp; !ELUsingAArch32(EL2) &amp;&amp; HSTR\_EL2.T1 == '1' ↪ → then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() &amp;&amp; IsFeatureImplemented(FEAT\_AA32EL2) &amp;&amp; ELUsingAArch32(EL2) &amp;&amp; HSTR.T1 == '1' ↪ → then AArch32.TakeHypTrapException(0x03); else UNDEFINED; elsif PSTATE.EL == EL2 then HSCTLR = R[t]; elsif PSTATE.EL == EL3 then if SCR.NS == '0' then UNDEFINED; else HSCTLR = R[t];