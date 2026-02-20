## G8.2.65 HCR, Hyp Configuration Register

The HCR characteristics are:

## Purpose

Provides configuration controls for virtualization, including defining whether various Non-secure operations are trapped to Hyp mode.

## Configuration

If EL2 is not implemented, this register is RES0 from EL3.

AArch32 System register HCR bits [31:0] are architecturally mapped to AArch64 System register HCR\_EL2[31:0].

This register is present only when FEAT\_AA32EL2 is implemented. Otherwise, direct accesses to HCR are UNDEFINED.

## Attributes

HCRis a 32-bit register.

## Field descriptions

<!-- image -->

## Bit [31]

Reserved, RES0.

## TRVM, bit [30]

Trap Reads of Virtual Memory controls. Traps Non-secure EL1 reads of the virtual memory control registers to EL2, when EL2 is enabled in the current Security state.

MRCreads of the following registers are trapped and reported using EC syndrome value 0x03 and MRRC reads are trapped and reported using EC syndrome value 0x04 :

SCTLR, TTBR0, TTBR1, TTBCR, TTBCR2, DACR, DFSR, IFSR, DFAR, IFAR, ADFSR, AIFSR, PRRR, NMRR, MAIR0, MAIR1, AMAIR0, AMAIR1, CONTEXTIDR.

| TRVM   | Meaning                                                                                   |
|--------|-------------------------------------------------------------------------------------------|
| 0b0    | This control does not cause any instructions to be trapped.                               |
| 0b1    | Non-secure EL1 read accesses to the specified Virtual Memory controls are trapped to EL2. |

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL3 or the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## HCD, bit [29]

## When EL3 is not implemented:

HVCinstruction disable.

Disables Non-secure EL1 and EL2 execution of HVC instructions, when EL2 is enabled in the current Security state, reported using EC syndrome value 0x00 .

| HCD   | Meaning                                                                                                                                                               |
|-------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0   | HVCinstruction execution is enabled at EL2 and EL1.                                                                                                                   |
| 0b1   | HVCinstructions are UNDEFINED at EL2 and Non-secure EL1. The Undefined Instruction exception is taken to the Exception level at which the HVCinstruction is executed. |

Note

HVCinstructions are always UNDEFINED at EL0.

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL3 or the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## Bit [28]

Reserved, RES0.

## TGE, bit [27]

Trap General Exceptions, from Non-secure EL0.

| TGE   | Meaning                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|-------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0   | This control has no effect on execution at EL0.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| 0b1   | When EL2 is not enabled in the current Security state, this control has no effect on execution at EL0. When EL2 is enabled in the current Security state, then: • All exceptions that would be routed to EL1 are routed to EL2. • The SCTLR.M bit is treated as being 0 for all purposes other than returning the result of a direct read of SCTLR. • The HCR.{FMO, IMO, AMO}bits are treated as being 1 for all purposes other than returning the result of a direct read of HCR. • All virtual interrupts are disabled. • Any IMPLEMENTATION DEFINED mechanisms for signaling virtual interrupts are disabled. • An exception return to EL1 is treated as an illegal exception return. • Monitor mode execution of an MSRor CPS instruction that changes PSTATE.M to a Non-secure EL1 mode is an illegal change to PSTATE.M. For more information see 'Illegal changes to PSTATE.M'. |

Also, when HCR.TGE is 1:

- If EL3 is using AArch32, an attempt to change from a Secure PL1 mode to a Non-secure EL1 mode by changing SCR.NS from 0 to 1 results in SCR.NS remaining as 0.
- The HDCR.{TDRA, TDOSA, TDA, TDE} bits are ignored and treated as being 1 other than for the purpose of a direct read of HDCR.

## The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL3 or the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## TVM, bit [26]

Trap Virtual Memory controls. Traps Non-secure EL1 writes to the virtual memory control registers to EL2, when EL2 is enabled in the current Security state.

MCRwrites of the following registers are trapped and reported using EC syndrome value 0x03 and MCRR writes are trapped and reported using EC syndrome value 0x04 :

SCTLR, TTBR0, TTBR1, TTBCR, TTBCR2, DACR, DFSR, IFSR, DFAR, IFAR, ADFSR, AIFSR, PRRR, NMRR, MAIR0, MAIR1, AMAIR0, AMAIR1, CONTEXTIDR.

| TVM   | Meaning                                                                                             |
|-------|-----------------------------------------------------------------------------------------------------|
| 0b0   | This control does not cause any instructions to be trapped.                                         |
| 0b1   | Non-secure EL1 write accesses to the specified virtual memory control registers are trapped to EL2. |

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL3 or the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## TTLB, bit [25]

Trap TLB maintenance instructions. Traps Non-secure EL1 execution of a TLBI instruction to EL2, when EL2 is enabled in the current Security state.

MCRand MRC accesses to the following system instructions are trapped and reported using EC syndrome value 0x03 :

TLBIALLIS, TLBIMVAIS, TLBIASIDIS, TLBIMVAAIS, TLBIMVALIS, TLBIMVAALIS, ITLBIALL, ITLBIMVA, ITLBIASID, DTLBIALL, DTLBIMVA, DTLBIASID, TLBIALL, TLBIMVA, TLBIASID, TLBIMVAA, TLBIMVAL, TLBIMVAAL

| TTLB   | Meaning                                                                                   |
|--------|-------------------------------------------------------------------------------------------|
| 0b0    | This control does not cause any instructions to be trapped.                               |
| 0b1    | Non-secure EL1 accesses to the specified TLB maintenance instructions are trapped to EL2. |

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL3 or the highest implemented Exception level is EL2, this field resets to '0' .

## TPU, bit [24]

Trap cache maintenance instructions that operate to the Point of Unification. Traps Non-secure EL1 execution of those cache maintenance instructions to EL2, when EL2 is enabled in the current Security state.

MRCand MCR accesses of the following system instructions are trapped and reported using EC syndrome value 0x03 :

- ICIMVAU, ICIALLU, ICIALLUIS, DCCMVAU.

Note

An Undefined Instruction exception generated at EL0 is higher priority than this trap to EL2, and these instructions are always UNDEFINED at EL0.

| TPU   | Meaning                                                                                     |
|-------|---------------------------------------------------------------------------------------------|
| 0b0   | This control does not cause any instructions to be trapped.                                 |
| 0b1   | Non-secure EL1 execution of the specified cache maintenance instructions is trapped to EL2. |

If the Point of Unification is before any level of data cache, it is IMPLEMENTATION DEFINED whether the execution of any data or unified cache clean by V A to the Point of Unification instruction can be trapped when the value of this control is 1.

If the Point of Unification is before any level of instruction cache, it is IMPLEMENTATION DEFINED whether the execution of any instruction cache invalidate to the Point of Unification instruction can be trapped when the value of this control is 1.

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL3 or the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## TPC, bit [23]

Trap data or unified cache maintenance instructions that operate to the Point of Coherency. Traps Non-secure EL1 execution of those cache maintenance instructions to EL2, when EL2 is enabled in the current Security state.

MRCand MCR accesses of the following system instructions are trapped and reported using EC syndrome value 0x03 :

- DCIMVAC, DCCIMVAC, DCCMVAC.

Note

An Undefined Instruction exception generated at EL0 is higher priority than this trap to EL2, and these instructions are always UNDEFINED at EL0.

| TPC   | Meaning                                                                                     |
|-------|---------------------------------------------------------------------------------------------|
| 0b0   | This control does not cause any instructions to be trapped.                                 |
| 0b1   | Non-secure EL1 execution of the specified cache maintenance instructions is trapped to EL2. |

- Otherwise, this field resets to an architecturally UNKNOWN value.

If the Point of Coherency is before any level of data cache, it is IMPLEMENTATION DEFINED whether the execution of any data or unified cache clean, invalidate, or clean and invalidate instruction that operates by V A to the point of coherency can be trapped when the value of this control is 1.

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL3 or the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## TSW, bit [22]

Trap data or unified cache maintenance instructions that operate by Set/Way. Traps Non-secure EL1 execution of those cache maintenance instructions by set/way to EL2, when EL2 is enabled in the current Security state.

MRCand MCR accesses of the following system instructions are trapped and reported using EC syndrome value 0x03 :

- DCISW, DCCSW, DCCISW.

Note

An Undefined Instruction exception generated at EL0 is higher priority than this trap to EL2, and these instructions are always UNDEFINED at EL0.

| TSW   | Meaning                                                                                     |
|-------|---------------------------------------------------------------------------------------------|
| 0b0   | This control does not cause any instructions to be trapped.                                 |
| 0b1   | Non-secure EL1 execution of the specified cache maintenance instructions is trapped to EL2. |

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL3 or the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## TAC, bit [21]

Trap Auxiliary Control Registers. Traps Non-secure EL1 accesses to the Auxiliary Control Registers to EL2, when EL2 is enabled in the current Security state, from both Execution states.

MRCand MCR accesses of the following registers are trapped and reported using EC syndrome value 0x03 :

ACTLR and, if implemented, ACTLR2.

| TAC   | Meaning                                                                |
|-------|------------------------------------------------------------------------|
| 0b0   | This control does not cause any instructions to be trapped.            |
| 0b1   | Non-secure EL1 accesses to the specified registers are trapped to EL2. |

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL3 or the highest implemented Exception level is EL2, this field resets to '0' .

## TSC, bit [19]

Trap SMC instructions. Traps Non-secure EL1 execution of SMC instructions to Hyp mode.

| TSC   | Meaning                                                                                                                |
|-------|------------------------------------------------------------------------------------------------------------------------|
| 0b0   | This control does not cause any instructions to be trapped.                                                            |
| 0b1   | Any attempt to execute an SMCinstruction at Non-secure EL1 is trapped to Hyp mode, regardless of the value of SCR.SCD. |

The Armv8-A architecture permits, but does not require, this trap to apply to conditional SMC instructions that fail their condition code check, in the same way as with traps on other conditional instructions.

## Note

- This trap is implemented only if the implementation includes EL3.
- SMCinstructions are always UNDEFINED at PL0.
- This bit traps execution of the SMC instruction, reported using EC syndrome value 0x13 . It is not a routing control for the SMC exception. Hyp Trap exceptions and SMC exceptions have different preferred return addresses.

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL3 or the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## TIDCP, bit [20]

Trap IMPLEMENTATION DEFINED functionality. Traps Non-secure EL1 accesses to the encodings for IMPLEMENTATION DEFINED System Registers to EL2, when EL2 is enabled in the current Security state.

MRCand MCR accesses of the following encodings are trapped and reported using EC syndrome value 0x03 :

- All coproc==p15, CRn==c9, Opcode1 = {0-7}, CRm == {c0-c2, c5-c8}, opcode2 == {0-7}.
- All coproc==p15, CRn==c10, Opcode1 =={0-7}, CRm == {c0, c1, c4, c8}, opcode2 == {0-7}.
- All coproc==p15, CRn==c11, Opcode1=={0-7}, CRm == {c0-c8, c15}, opcode2 == {0-7}.

| TIDCP   | Meaning                                                                                                                         |
|---------|---------------------------------------------------------------------------------------------------------------------------------|
| 0b0     | This control does not cause any instructions to be trapped.                                                                     |
| 0b1     | Non-secure EL1 accesses to the specified System register encodings for IMPLEMENTATION DEFINED functionality are trapped to EL2. |

When HCR.TIDCP is set to 1, it is IMPLEMENTATION DEFINED whether any of this functionality accessed from Non-secure EL0 is trapped to EL2. Otherwise, it is UNDEFINED and the PE takes an Undefined Instruction exception to Non-secure Undefined mode.

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL3 or the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

- Otherwise, this field resets to an architecturally UNKNOWN value.

## TID3, bit [18]

Trap ID group 3. Traps Non-secure EL1 reads of the following registers to EL2, when EL2 is enabled in the current Security state as follows:

- VMRSaccess to MVFR0, MVFR1, and MVFR2, reported using EC syndrome value 0x08 , unless access is also trapped by HCPTR which takes priority.
- MRCaccess to the following registers are reported using EC syndrome value 0x03 :
- ID\_PFR0, ID\_PFR1, ID\_PFR2, ID\_DFR0, ID\_AFR0, ID\_MMFR0, ID\_MMFR1, ID\_MMFR2, ID\_MMFR3, ID\_ISAR0, ID\_ISAR1, ID\_ISAR2, ID\_ISAR3, ID\_ISAR4, and ID\_ISAR5.
- If FEAT\_FGT is implemented:
- ID\_MMFR4 and ID\_MMFR5 are trapped to EL2.
- ID\_ISAR6 is trapped to EL2.
- ID\_DFR1 is trapped to EL2.
- This field traps all MRC accesses to registers in the following range that are not already mentioned in this field description: coproc == p15, opc1 == 0, CRn == c0, CRm == {c2-c7}, opc2 == {0-7}.
- If FEAT\_FGT is not implemented:
- ID\_MMFR4 and ID\_MMFR5 are trapped to EL2, unless implemented as RAZ, when it is IMPLEMENTATION DEFINED whether accesses to ID\_MMFR4 or ID\_MMFR5 are trapped.
- ID\_ISAR6 is trapped to EL2, unless implemented as RAZ, when it is IMPLEMENTATION DEFINED whether accesses to ID\_ISAR6 are trapped to EL2.
- ID\_DFR1 is trapped to EL2, unless implemented as RAZ, when it is IMPLEMENTATION DEFINED whether accesses to ID\_DFR1 are trapped to EL2.
- Otherwise, it is IMPLEMENTATION DEFINED whether this bit traps MRC accesses to registers not already mentioned, with coproc == p15, opc1 == 0, CRn == c0, CRm == {c2-c7}, opc2 == {0-7}.

| TID3   | Meaning                                                                                |
|--------|----------------------------------------------------------------------------------------|
| 0b0    | This control does not cause any instructions to be trapped.                            |
| 0b1    | The specified Non-secure EL1 read accesses to ID group 3 registers are trapped to EL2. |

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL3 or the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## TID2, bit [17]

Trap ID group 2. Traps the following register MRC and MCR accesses to EL2, reported using EC syndrome value 0x03 , when EL2 is enabled in the current Security state:

- Non-secure EL1 and EL0 reads of the CTR, CCSIDR, CCSIDR2, CLIDR, and CSSELR.
- Non-secure EL1 and EL0 writes to the CSSELR.

| TID2   | Meaning                                                                                   |
|--------|-------------------------------------------------------------------------------------------|
| 0b0    | This control does not cause any instructions to be trapped.                               |
| 0b1    | The specified Non-secure EL1 and EL0 accesses to ID group 2 registers are trapped to EL2. |

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL3 or the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## TID1, bit [16]

Trap ID group 1. Traps Non-secure EL1 MRC reads of the following registers to EL2, reported using EC syndrome value 0x03 , when EL2 is enabled in the current Security state:

TCMTR, TLBTR, REVIDR, AIDR.

| TID1   | Meaning                                                                                |
|--------|----------------------------------------------------------------------------------------|
| 0b0    | This control does not cause any instructions to be trapped.                            |
| 0b1    | The specified Non-secure EL1 read accesses to ID group 1 registers are trapped to EL2. |

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL3 or the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## TID0, bit [15]

Trap ID group 0. Traps the following register accesses to EL2, when EL2 is enabled in the current Security state:

- Non-secure EL1 VMRS reads of FPSID reported using EC syndrome value 0x08 .
- Non-secure EL0 and EL1 MCR and MRC accesses of JIDR reported using EC syndrome value 0x05 .

## Note

- It is IMPLEMENTATION DEFINED whether the JIDR is RAZ or UNDEFINED at EL0. If it is UNDEFINED at EL0 then the Undefined Instruction exception takes precedence over this trap.
- The FPSID is not accessible at EL0.
- Writes to the FPSID are ignored, and not trapped by this control.

| TID0   | Meaning                                                                                |
|--------|----------------------------------------------------------------------------------------|
| 0b0    | This control does not cause any instructions to be trapped.                            |
| 0b1    | The specified Non-secure EL1 read accesses to ID group 0 registers are trapped to EL2. |

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL3 or the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## TWE, bit [14]

Traps Non-secure EL0 and EL1 execution of WFE instructions to EL2, reported using EC syndrome value 0x01 , when EL2 is enabled in the current Security state.

| TWE   | Meaning                                                                                                                                                                                                   |
|-------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0   | This control does not cause any instructions to be trapped.                                                                                                                                               |
| 0b1   | Any attempt to execute a WFEinstruction at Non-secure EL0 or EL1 is trapped to EL2, if the instruction would otherwise have caused the PE to enter a low-power state and it is not trapped by SCTLR.nTWE. |

The attempted execution of a conditional WFE instruction is only trapped if the instruction passes its condition code check.

Note

Since a WFE can complete at any time, even without a Wakeup event, the traps on WFE are not guaranteed to be taken, even if the WFE is executed when there is no Wakeup event. The only guarantee is that if the instruction does not complete in finite time in the absence of a Wakeup event, the trap will be taken.

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL3 or the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## TWI, bit [13]

Traps Non-secure EL0 and EL1 execution of WFI instructions to EL2, reported using EC syndrome value 0x01 , when EL2 is enabled in the current Security state.

| TWI   | Meaning                                                                                                                                                                                                    |
|-------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0   | This control does not cause any instructions to be trapped.                                                                                                                                                |
| 0b1   | Any attempt to execute a WFI instruction at Non-secure EL0 or EL1 is trapped to EL2, if the instruction would otherwise have caused the PE to enter a low-power state and it is not trapped by SCTLR.nTWI. |

The attempted execution of a conditional WFI instruction is only trapped if the instruction passes its condition code check.

Note

Since a WFI can complete at any time, even without a Wakeup event, the traps on WFI are not guaranteed to be taken, even if the WFI is executed when there is no Wakeup event. The only guarantee is that if the instruction does not complete in finite time in the absence of a Wakeup event, the trap will be taken.

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL3 or the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## DC, bit [12]

Default Cacheability.

| DC   | Meaning                                                                |
|------|------------------------------------------------------------------------|
| 0b0  | This control has no effect on the Non-secure EL1&0 translation regime. |
| 0b1  | In Non-secure state:                                                   |

This field has no effect on the EL2 and EL3 translation regimes.

This bit is permitted to be cached in a TLB.

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL3 or the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## BSU, bits [11:10]

Barrier Shareability upgrade. This field determines the minimum shareability domain that is applied to any barrier instruction executed from Non-secure EL1 or Non-secure EL0:

| BSU   | Meaning          |
|-------|------------------|
| 0b00  | No effect.       |
| 0b01  | Inner Shareable. |
| 0b10  | Outer Shareable. |
| 0b11  | Full system.     |

This value is combined with the specified level of the barrier held in its instruction, using the same principles as combining the shareability attributes from two stages of address translation.

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL3 or the highest implemented Exception level is EL2, this field resets to '00' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## FB, bit [9]

Force broadcast. Causes the following instructions to be broadcast within the Inner Shareable domain when executed from Non-secure EL1:

BPIALL, TLBIALL, TLBIMVA, TLBIASID, DTLBIALL, DTLBIMVA, DTLBIASID, ITLBIALL, ITLBIMVA, ITLBIASID, TLBIMVAA, ICIALLU, TLBIMVAL, TLBIMVAAL.

| FB   | Meaning                                                                                                                                           |
|------|---------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0  | This field has no effect on the operation of the specified instructions.                                                                          |
| 0b1  | When one of the specified instruction is executed at Non-secure EL1, the instruction is broadcast within the Inner Shareable shareability domain. |

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL3 or the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## VA, bit [8]

Virtual SError exception.

| VA   | Meaning                                                          |
|------|------------------------------------------------------------------|
| 0b0  | This mechanism is not making a virtual SError exception pending. |
| 0b1  | Avirtual SError exception is pending because of this mechanism.  |

The virtual SError exception is enabled only when the value of HCR.{TGE, AMO} is {0, 1}.

The Guest OS cannot distinguish the virtual exception from the corresponding physical exception.

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL3 or the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## VI, bit [7]

Virtual IRQ exception.

| VI   | Meaning                                             |
|------|-----------------------------------------------------|
| 0b0  | This mechanism is not making a virtual IRQ pending. |
| 0b1  | Avirtual IRQ is pending because of this mechanism.  |

The virtual IRQ is enabled only when the value of HCR.{TGE, IMO} is {0, 1}.

The Guest OS cannot distinguish the virtual exception from the corresponding physical exception.

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL3 or the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

VF, bit [6]

Virtual FIQ exception.

| VF   | Meaning                                             |
|------|-----------------------------------------------------|
| 0b0  | This mechanism is not making a virtual FIQ pending. |
| 0b1  | Avirtual FIQ is pending because of this mechanism.  |

The virtual FIQ is enabled only when the value of HCR.{TGE, FMO} is {0, 1}.

The Guest OS cannot distinguish the virtual exception from the corresponding physical exception.

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL3 or the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## AMO,bit [5]

SError exception Mask Override. When this bit is set to 1, it overrides the effect of PSTATE.A, and enables virtual exception signaling by the V A bit.

If the value of HCR.TGE is 0, then virtual SError exceptions are enabled in Non-secure state.

If the value of HCR.TGE is 1, then in Non-secure state the HCR.AMO bit behaves as 1 for all purposes other than a direct read of the value of the bit.

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL3 or the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## IMO, bit [4]

IRQ Mask Override. When this bit is set to 1, it overrides the effect of PSTATE.I, and enables virtual exception signaling by the VI bit.

If the value of HCR.TGE is 0, then Virtual IRQ interrupts are enabled in the Non-secure state.

If the value of HCR.TGE is 1, then in Non-secure state the HCR.IMO bit behaves as 1 for all purposes other than a direct read of the value of the bit.

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL3 or the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## FMO, bit [3]

FIQ Mask Override. When this bit is set to 1, it overrides the effect of PSTATE.F, and enables virtual exception signaling by the VF bit.

If the value of HCR.TGE is 0, then Virtual FIQ interrupts are enabled in the Non-secure state.

If the value of HCR.TGE is 1, then in Non-secure state the HCR.FMO bit behaves as 1 for all purposes other than a direct read of the value of the bit.

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL3 or the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## PTW, bit [2]

Protected Table Walk. In the Non-secure PL1&amp;0 translation regime, a translation table access made as part of a stage 1 translation table walk is subject to a stage 2 translation. The combining of the memory type attributes from the two stages of translation means the access might be made to a type of Device memory. If this occurs then the value of this bit determines the behavior:

| PTW   | Meaning                                                                                                                |
|-------|------------------------------------------------------------------------------------------------------------------------|
| 0b0   | The translation table walk occurs as if it is to Normal Non-cacheable memory. This means it can be made speculatively. |
| 0b1   | The memory access generates a stage 2 Permission fault.                                                                |

This bit is permitted to be cached in a TLB.

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL3 or the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## SWIO, bit [1]

Set/Way Invalidation Override. Causes Non-secure EL1 execution of the data cache invalidate by set/way instructions to perform a data cache clean and invalidate by set/way.

| SWIO   | Meaning                                                                                             |
|--------|-----------------------------------------------------------------------------------------------------|
| 0b0    | This control has no effect on the operation of data cache invalidate by set/way instructions.       |
| 0b1    | Data cache invalidate by set/way instructions perform a data cache clean and invalidate by set/way. |

When this bit is set to 1, DCISW performs the same invalidation as a DCCISW instruction.

As a result of changes to the behavior of DCISW, this bit is redundant in Armv8. This bit can be implemented as RES1.

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL3 or the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## VM, bit [0]

Virtualization enable. Enables stage 2 address translation for the Non-secure EL1&amp;0 translation regime.

| VM   | Meaning                                                |
|------|--------------------------------------------------------|
| 0b0  | Non-secure EL1&0 stage 2 address translation disabled. |
| 0b1  | Non-secure EL1&0 stage 2 address translation enabled.  |

If the HCR.DC bit is set to 1, then the behavior of the PE when executing in a Non-secure mode other than Hyp mode is consistent with HCR.VM being 1, regardless of the actual value of HCR.VM, other than the value returned by an explicit read of HCR.VM.

When the value of this bit is 1, data cache invalidate instructions executed at Non-secure EL1 perform a data cache clean and invalidate. For the invalidate by set/way instruction this behavior applies regardless of the value of the HCR.SWIO bit.

This bit is permitted to be cached in a TLB.

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL3 or the highest implemented Exception level is EL2, this field resets to '0' .
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Accessing HCR

Accesses to this register use the following encodings in the System register encoding space:

```
MRC{<c>}{<q>} <coproc>, {#}<opc1>, <Rt>, <CRn>, <CRm>{, {#}<opc2>}
```

| coproc   | opc1   | CRn    | CRm    | opc2   |
|----------|--------|--------|--------|--------|
| 0b1111   | 0b100  | 0b0001 | 0b0001 | 0b000  |

```
if !IsFeatureImplemented(FEAT_AA32EL2) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && HSTR_EL2.T1 == '1' ↪ → then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HSTR.T1 == '1' ↪ → then AArch32.TakeHypTrapException(0x03); else UNDEFINED; elsif PSTATE.EL == EL2 then R[t] = HCR; elsif PSTATE.EL == EL3 then if SCR.NS == '0' then UNDEFINED; else R[t] = HCR;
```

MCR{&lt;c&gt;}{&lt;q&gt;} &lt;coproc&gt;, {#}&lt;opc1&gt;, &lt;Rt&gt;, &lt;CRn&gt;, &lt;CRm&gt;{, {#}&lt;opc2&gt;}

| coproc   | opc1   | CRn    | CRm    | opc2   |
|----------|--------|--------|--------|--------|
| 0b1111   | 0b100  | 0b0001 | 0b0001 | 0b000  |

```
if !IsFeatureImplemented(FEAT_AA32EL2) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && HSTR_EL2.T1 == '1' ↪ → then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HSTR.T1 == '1' ↪ → then AArch32.TakeHypTrapException(0x03); else UNDEFINED; elsif PSTATE.EL == EL2 then HCR = R[t]; elsif PSTATE.EL == EL3 then if SCR.NS == '0' then UNDEFINED; else HCR = R[t];
```