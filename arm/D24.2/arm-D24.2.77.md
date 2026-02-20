## D24.2.77 HSTR\_EL2, Hypervisor System Trap Register

The HSTR\_EL2 characteristics are:

## Purpose

Controls trapping to EL2 of EL1 or lower AArch32 accesses to the System register in the coproc == 0b1111 encoding space, by the CRn value used to access the register using MCR or MRC instruction. When the register is accessible using an MCRR or MRRC instruction, this is the CRm value used to access the register.

## Configuration

If EL2 is not implemented, this register is RES0 from EL3.

This register has no effect if EL2 is not enabled in the current Security state.

AArch64 System register HSTR\_EL2 bits [31:0] are architecturally mapped to AArch32 System register HSTR[31:0].

This register is present only when FEAT\_AA64 is implemented. Otherwise, direct accesses to HSTR\_EL2 are UNDEFINED.

## Attributes

HSTR\_EL2 is a 64-bit register.

## Field descriptions

When FEAT\_AA32 is implemented:

<!-- image -->

## Bits [63:16, 14, 4]

Reserved, RES0.

## T&lt;n&gt; , bits [n], for n = 15 to 15, 13 to 5, 3 to 0

The remaining fields control whether EL0 and EL1 accesses, using MCR, MRC, MCRR, and MRRC instructions, to the System registers in the coproc == 0b1111 encoding space, are trapped to EL2 as follows:

- MCRor MRC accesses to these registers that are trapped to EL2 are reported using EC syndrome value 0x03 , unless the access is UNDEFINED.
- MCRRor MRRC accesses to these registers that are trapped to EL2 are reported using EC syndrome value 0x04 , unless the access is UNDEFINED.

| T<n>   | Meaning                                                                |
|--------|------------------------------------------------------------------------|
| 0b0    | This control has no effect on EL0 or EL1 accesses to System registers. |

| T<n>   | Meaning                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|--------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b1    | System registers in the coproc == 0b1111 encoding space and CRn == <n> or CRm == <n> where T<n> is the name of this field, are trapped as follows: • An EL1 MCRor MRCaccess is trapped to EL2. • An EL0 MCRor MRCaccess is trapped to EL2, if the access is not UNDEFINED when the value of this field is 0. • An EL1 MCRRor MRRCaccess is trapped to EL2. • An EL0 MCRRor MRRCaccess is trapped to EL2, if the access is not UNDEFINED when the value of this field is 0. It is IMPLEMENTATION DEFINED whether an EL0 access using AArch32 is trapped to EL2, or is UNDEFINED. If the access is UNDEFINED, and generates an exception that is taken to EL1 or EL2 using AArch64, this is reported with EC syndrome value 0x00 . Note Armexpects that trapping to EL2 of EL0 accesses to these registers is unusual and used only when the hypervisor must virtualize EL0 operation. Arm recommends that, whenever possible, EL0 accesses to these registers behave as they would if the implementation did not include EL2. This means that, if the architecture does not support the EL0 access, then the register access instruction is treated as UNDEFINED and generates an exception that is taken to EL1. |

For example, when HSTR\_EL2.T7 is 1, for instructions executed at EL1:

- An MCR or MRC instruction with coproc set to 0b1111 and &lt;CRn&gt; set to c7 is trapped to EL2.
- An MCRR or MRRC instruction with coproc set to 0b1111 and &lt;CRm&gt; set to c7 is trapped to EL2.

When the Effective value of HCR\_EL2.{E2H, TGE} is {1, 1}, this field behaves as 0 for all purposes other than a direct read of the value of this bit.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

<!-- image -->

| 63   | 32   |
|------|------|
|      | 0    |
| 31   |      |
| RES0 |      |

## Bits [63:0]

Reserved, RES0.

## Accessing HSTR\_EL2

Accesses to this register use the following encodings in the System register encoding space:

MRS &lt;Xt&gt;, HSTR\_EL2

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b100 | 0b0001 | 0b0001 | 0b011 |

{'xx1'} then

```
if PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EffectiveHCR_EL2_NVx() IN {'1x1'} then X[t, 64] = NVMem[0x080]; elsif EffectiveHCR_EL2_NVx() IN AArch64.SystemAccessTrap(EL2, 0x18); else UNDEFINED; elsif PSTATE.EL == EL2 then X[t, 64] = HSTR_EL2; elsif PSTATE.EL == EL3 then X[t, 64] = HSTR_EL2;
```

MSR HSTR\_EL2, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b100 | 0b0001 | 0b0001 | 0b011 |

```
if PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EffectiveHCR_EL2_NVx() IN {'1x1'} then NVMem[0x080] = X[t, 64]; elsif EffectiveHCR_EL2_NVx() IN {'xx1'} then AArch64.SystemAccessTrap(EL2, 0x18); else UNDEFINED; elsif PSTATE.EL == EL2 then HSTR_EL2 = X[t, 64]; elsif PSTATE.EL == EL3 then HSTR_EL2 = X[t, 64];
```