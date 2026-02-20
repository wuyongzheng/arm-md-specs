## G8.2.126 SCR, Secure Configuration Register

The SCR characteristics are:

## Purpose

When EL3 is implemented and can use AArch32, defines the configuration of the current Security state. It specifies:

- The Security state, either Secure or Non-secure.
- What mode the PE branches to if an IRQ, FIQ, or External abort occurs.
- Whether the PSTATE.F or PSTATE.A bits can be modified when SCR.NS==1.

## Configuration

This register is present only when FEAT\_AA32EL3 is implemented. Otherwise, direct accesses to SCR are UNDEFINED.

## Attributes

SCR is a 32-bit register.

## Field descriptions

<!-- image -->

## Bits [31:16]

Reserved, RES0.

## TERR, bit [15]

## When FEAT\_RAS is implemented:

Trap Error record accesses. Generate a Monitor Trap exception on MRC, MCR, MRRC, or MCRR accesses to the following registers from modes other than Monitor mode, reported using EC syndrome values 0x03 and 0x04 :

ERRIDR, ERRSELR, ERXADDR, ERXADDR2, ERXCTLR, ERXCTLR2, ERXFR, ERXFR2, ERXMISC0, ERXMISC1, ERXMISC2, ERXMISC3, and ERXSTATUS. When FEAT\_RASv1p1 is implemented, ERXMISC4, ERXMISC5, ERXMISC6, ERXMISC7.

| TERR   | Meaning                                                                                                   |
|--------|-----------------------------------------------------------------------------------------------------------|
| 0b0    | This control does not cause any instructions to be trapped.                                               |
| 0b1    | Accesses to the specified registers from modes other than Monitor mode generate a Monitor Trap exception. |

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL3, this field resets to '0' .

TERR

RES0

## Otherwise:

Reserved, RES0.

## Bit [14]

Reserved, RES0.

## TWE, bit [13]

Traps WFE instructions to Monitor mode.

| TWE   | Meaning                                                                                                                                                                                                                                                                                                                                                                             |
|-------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0   | This control does not cause any instructions to be trapped.                                                                                                                                                                                                                                                                                                                         |
| 0b1   | Any attempt to execute a WFEinstruction in any mode other than Monitor mode is trapped to Monitor mode, if the instruction would otherwise have caused the PE to enter a low-power state and the attempted execution does not generate an exception that is taken to EL1 or EL2 by SCTLR.nTWE or HCR.TWE. Any exception that is taken to EL1 or to EL2 has priority over this trap. |

The attempted execution of a conditional WFE instruction is only trapped if the instruction passes its condition code check.

Note

Since a WFE or WFI can complete at any time, even without a Wakeup event, the traps on WFE of WFI are not guaranteed to be taken, even if the WFE or WFI is executed when there is no Wakeup event. The only guarantee is that if the instruction does not complete in finite time in the absence of a Wakeup event, the trap will be taken.

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL3, this field resets to '0' .

## TWI, bit [12]

Traps WFI instructions to Monitor mode.

| TWI   | Meaning                                                                                                                                                                                                                                                                                                                                                                              |
|-------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0   | This control does not cause any instructions to be trapped.                                                                                                                                                                                                                                                                                                                          |
| 0b1   | Any attempt to execute a WFI instruction in any mode other than Monitor mode is trapped to Monitor mode, if the instruction would otherwise have caused the PE to enter a low-power state and the attempted execution does not generate an exception that is taken to EL1 or EL2 by SCTLR.nTWI or HCR.TWI. Any exception that is taken to EL1 or to EL2 has priority over this trap. |

The attempted execution of a conditional WFI instruction is only trapped if the instruction passes its condition code check.

Note

Since a WFE or WFI can complete at any time, even without a Wakeup event, the traps on WFE of WFI are not guaranteed to be taken, even if the WFE or WFI is executed when there is no Wakeup event. The only guarantee is that if the instruction does not complete in finite time in the absence of a Wakeup event, the trap will be taken.

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL3, this field resets to '0' .

## Bits [11:10]

Reserved, RES0.

## SIF, bit [9]

Secure instruction fetch. When the PE is in Secure state, this bit disables instruction execution from Non-secure memory.

| SIF   | Meaning                                                                     |
|-------|-----------------------------------------------------------------------------|
| 0b0   | Secure state instruction execution from Non-secure memory is permitted.     |
| 0b1   | Secure state instruction execution from Non-secure memory is not permitted. |

This bit is permitted to be cached in a TLB.

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL3, this field resets to '0' .

## HCE, bit [8]

Hypervisor Call instruction enable. If EL2 is implemented, enables execution of HVC instructions at Non-secure EL1 and EL2.

| HCE   | Meaning                                                                                                                                                                                                                                          |
|-------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0   | HVCinstructions are: • UNDEFINED at Non-secure EL1. The Undefined Instruction exception is taken from PL1 to PL1. • UNPREDICTABLE at EL2. Behavior is one of the following: • The instruction is UNDEFINED. • The instruction executes as a NOP. |
| 0b1   | HVCinstructions are enabled at Non-secure EL1 and EL2.                                                                                                                                                                                           |

Note

HVCinstructions are always UNDEFINED at EL0 and in Secure state.

If EL2 is not implemented, this bit is RES0 and HVC is UNDEFINED.

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL3, this field resets to '0' .

## SCD, bit [7]

Secure Monitor Call disable. Disables SMC instructions.

| SCD   | Meaning                                                                                                                                                                                                                                                                                   |
|-------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0   | SMCinstructions are enabled.                                                                                                                                                                                                                                                              |
| 0b1   | In Non-secure state, SMCinstructions are UNDEFINED. The Undefined Instruction exception is taken from the current Exception level to the current Exception level. In Secure state, behavior is one of the following: • The instruction is UNDEFINED. • The instruction executes as a NOP. |

## Note

SMCinstructions are always UNDEFINED at PL0.

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL3, this field resets to '0' .

## nET, bit [6]

Not Early Termination. This bit disables early termination.

| nET   | Meaning                                                                                                                      |
|-------|------------------------------------------------------------------------------------------------------------------------------|
| 0b0   | Early termination permitted. Execution time of data operations can depend on the data values.                                |
| 0b1   | Disable early termination. The number of cycles required for data operations is forced to be independent of the data values. |

This IMPLEMENTATION DEFINED mechanism can disable data dependent timing optimizations from multiplies and data operations. It can provide system support against information leakage that might be exploited by timing correlation types of attack.

On implementations that do not support early termination or do not support disabling early termination, this bit is RES0.

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL3, this field resets to '0' .

## AW, bit [5]

When the value of SCR.EA is 1 and the value of HCR.AMO is 0, this bit controls whether PSTATE.A masks an External abort taken from Non-secure state.

| AW   | Meaning                                                                                                                                                       |
|------|---------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0  | External aborts taken from Non-secure state are not masked by PSTATE.A, and are taken to EL3. External aborts taken from Secure state are masked by PSTATE.A. |
| 0b1  | External aborts taken from either Security state are masked by PSTATE.A. When PSTATE.A is 0, the abort is taken to EL3.                                       |

When SCR.EA is 0 or HCR.AMO is 1, this bit has no effect.

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL3, this field resets to '0' .

## FW, bit [4]

When the value of SCR.FIQ is 1 and the value of HCR.FMO is 0, this bit controls whether PSTATE.F masks an FIQ interrupt taken from Non-secure state.

| FW   | Meaning                                                                                                                                  |
|------|------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0  | An FIQ taken from Non-secure state is not masked by PSTATE.F, and is taken to EL3. An FIQ taken from Secure state is masked by PSTATE.F. |
| 0b1  | An FIQ taken from either Security state is masked by PSTATE.F. When PSTATE.F is 0, the FIQ is taken to EL3.                              |

When SCR.FIQ is 0 or HCR.FMO is 1, this bit has no effect.

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL3, this field resets to '0' .

## EA, bit [3]

External Abort handler. This bit controls which mode takes External aborts and SError exceptions.

| EA   | Meaning                                |
|------|----------------------------------------|
| 0b0  | External aborts taken to Abort mode.   |
| 0b1  | External aborts taken to Monitor mode. |

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL3, this field resets to '0' .

## FIQ, bit [2]

FIQ handler. This bit controls which mode takes FIQ exceptions.

| FIQ   | Meaning                     |
|-------|-----------------------------|
| 0b0   | FIQs taken to FIQ mode.     |
| 0b1   | FIQs taken to Monitor mode. |

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL3, this field resets to '0' .

## IRQ, bit [1]

IRQ handler. This bit controls which mode takes IRQ exceptions.

| IRQ   | Meaning                     |
|-------|-----------------------------|
| 0b0   | IRQs taken to IRQ mode.     |
| 0b1   | IRQs taken to Monitor mode. |

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL3, this field resets to '0' .

## NS, bit [0]

Non-secure bit. Except when the PE is in Monitor mode, this bit determines the Security state of the PE:

| NS   | Meaning                    |
|------|----------------------------|
| 0b0  | PE is in Secure state.     |
| 0b1  | PE is in Non-secure state. |

If the HCR.TGE bit is set, an attempt to change from a Secure PL1 mode to a Non-secure EL1 mode by changing the SCR.NS bit from 0 to 1 results in the SCR.NS bit remaining as 0.

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL3, this field resets to '0' .

## Accessing SCR

Accesses to this register use the following encodings in the System register encoding space:

```
MRC{<c>}{<q>} <coproc>, {#}<opc1>, <Rt>, <CRn>, <CRm>{, {#}<opc2>}
```

| coproc   | opc1   | CRn    | CRm    | opc2   |
|----------|--------|--------|--------|--------|
| 0b1111   | 0b000  | 0b0001 | 0b0001 | 0b000  |

```
if !IsFeatureImplemented(FEAT_AA32EL3) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && HSTR_EL2.T1 == '1' ↪ → then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HSTR.T1 == '1' ↪ → then AArch32.TakeHypTrapException(0x03);
```

```
elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && ↪ → IsCurrentSecurityState(SS_Secure) then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && ↪ → IsCurrentSecurityState(SS_Secure) then AArch64.AArch32SystemAccessTrap(EL3, 0x03); else UNDEFINED; elsif PSTATE.EL == EL2 then UNDEFINED; elsif PSTATE.EL == EL3 then R[t] = SCR;
```

MCR{&lt;c&gt;}{&lt;q&gt;} &lt;coproc&gt;, {#}&lt;opc1&gt;, &lt;Rt&gt;, &lt;CRn&gt;, &lt;CRm&gt;{, {#}&lt;opc2&gt;}

| coproc   | opc1   | CRn    | CRm    | opc2   |
|----------|--------|--------|--------|--------|
| 0b1111   | 0b000  | 0b0001 | 0b0001 | 0b000  |

```
if !IsFeatureImplemented(FEAT_AA32EL3) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && HSTR_EL2.T1 == '1' ↪ → then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HSTR.T1 == '1' ↪ → then AArch32.TakeHypTrapException(0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && ↪ → IsCurrentSecurityState(SS_Secure) then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && ↪ → IsCurrentSecurityState(SS_Secure) then AArch64.AArch32SystemAccessTrap(EL3, 0x03); else UNDEFINED; elsif PSTATE.EL == EL2 then UNDEFINED; elsif PSTATE.EL == EL3 then SCR = R[t];
```