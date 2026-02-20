## G8.2.119 NMRR, Normal Memory Remap Register

The NMRR characteristics are:

## Purpose

Provides additional mapping controls for memory regions that are mapped as Normal memory by their entry in the PRRR.

Used in conjunction with the PRRR.

## Configuration

MAIR1 and NMRR are the same register, with a different view depending on the value of TTBCR.EAE:

- When it is set to 0, the register is as described in NMRR.
- When it is set to 1, the register is as described in MAIR1.

When EL3 is not implemented or EL3 is using AArch64, AArch32 System register NMRR bits [31:0] are architecturally mapped to AArch64 System register MAIR\_EL1[63:32].

When EL3 is not implemented or EL3 is using AArch64, AArch32 System register NMRR bits [31:0] are architecturally mapped to AArch32 System register MAIR1[31:0].

When EL3 is using AArch32, AArch32 System register NMRR bits [31:0] are architecturally mapped to AArch32 System register MAIR1[31:0].

When EL3 is using AArch32, AArch32 System register NMRR bits [31:0] are architecturally mapped to AArch32 System register MAIR1[31:0].

This register is banked between NMRR and NMRR\_S and NMRR\_NS.

This register is present only when FEAT\_AA32EL1 is implemented. Otherwise, direct accesses to NMRR are UNDEFINED.

## Attributes

NMRRis a 32-bit register.

This register has the following instances:

- NMRR, when EL3 is not implemented or FEAT\_AA64 is implemented.
- NMRR\_S, when FEAT\_AA32EL3 is implemented.
- NMRR\_NS, when FEAT\_AA32EL3 is implemented.

## Field descriptions

When TTBCR.EAE == '0':

<!-- image -->

| 31 30 29 28   | 27 26   | 25 24   | 23 22   | 21 20   | 19 18   | 17 16   | 15 14   | 13 12   | 11 10   | 9 8   | 7 6   | 5 4   | 3 2   | 1 0   |
|---------------|---------|---------|---------|---------|---------|---------|---------|---------|---------|-------|-------|-------|-------|-------|
| OR7 OR6       | OR5     | OR4     | OR3     | OR2     | OR1     | OR0     | IR7     | IR6     | IR5     | IR4   | IR3   | IR2   | IR1   | IR0   |

## OR&lt;n&gt; , bits [2n+17:2n+16], for n = 7 to 0

Outer Cacheable property mapping for memory attributes n, if the region is mapped as Normal memory by the PRRR.TR&lt;n&gt; entry. n is the value of the TEX[0], C, and B bits concatenated.

| OR<n>   | Meaning                                     |
|---------|---------------------------------------------|
| 0b00    | Region is Non-cacheable.                    |
| 0b01    | Region is Write-Back, Write-Allocate.       |
| 0b10    | Region is Write-Through, no Write-Allocate. |
| 0b11    | Region is Write-Back, no Write-Allocate.    |

The meaning of the field with n = 6 is IMPLEMENTATION DEFINED and might differ from the meaning given here. This is because the meaning of the attribute combination {TEX[0] = 1, C = 1, B = 0} is IMPLEMENTATION DEFINED.

When FEAT\_XS is implemented, stage 1 Outer Write-Back Cacheable memory types have the XS attribute set to 0.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## IR&lt;n&gt; , bits [2n+1:2n], for n = 7 to 0

Inner Cacheable property mapping for memory attributes n, if the region is mapped as Normal memory by the PRRR.TR&lt;n&gt; entry. n is the value of the TEX[0], C, and B bits concatenated.

| IR<n>   | Meaning                                     |
|---------|---------------------------------------------|
| 0b00    | Region is Non-cacheable.                    |
| 0b01    | Region is Write-Back, Write-Allocate.       |
| 0b10    | Region is Write-Through, no Write-Allocate. |
| 0b11    | Region is Write-Back, no Write-Allocate.    |

The meaning of the field with n = 6 is IMPLEMENTATION DEFINED and might differ from the meaning given here. This is because the meaning of the attribute combination {TEX[0] = 1, C = 1, B = 0} is IMPLEMENTATION DEFINED.

When FEAT\_XS is implemented, stage 1 Inner Write-Back Cacheable memory types have the XS attribute set to 0.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Accessing NMRR

Accesses to this register use the following encodings in the System register encoding space:

MRC{&lt;c&gt;}{&lt;q&gt;} &lt;coproc&gt;, {#}&lt;opc1&gt;, &lt;Rt&gt;, &lt;CRn&gt;, &lt;CRm&gt;{, {#}&lt;opc2&gt;}

| coproc   | opc1   | CRn    | CRm    | opc2   |
|----------|--------|--------|--------|--------|
| 0b1111   | 0b000  | 0b1010 | 0b0010 | 0b001  |

```
if !IsFeatureImplemented(FEAT_AA32EL1) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED;
```

```
elsif PSTATE.EL == EL1 then if EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && HSTR_EL2.T10 == '1' ↪ → then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HSTR.T10 == '1' ↪ → then AArch32.TakeHypTrapException(0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && HCR_EL2.TRVM == ↪ → '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HCR.TRVM == '1' ↪ → then AArch32.TakeHypTrapException(0x03); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA32EL3) && ELUsingAArch32(EL3) then if TTBCR.EAE == '1' then R[t] = MAIR1_NS; else R[t] = NMRR_NS; else if TTBCR.EAE == '1' then R[t] = MAIR1; else R[t] = NMRR; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && IsFeatureImplemented(FEAT_AA32EL3) && ELUsingAArch32(EL3) then if TTBCR.EAE == '1' then R[t] = MAIR1_NS; else R[t] = NMRR_NS; else if TTBCR.EAE == '1' then R[t] = MAIR1; else R[t] = NMRR; elsif PSTATE.EL == EL3 then if TTBCR.EAE == '1' then if SCR.NS == '0' then R[t] = MAIR1_S; else R[t] = MAIR1_NS; else if SCR.NS == '0' then R[t] = NMRR_S; else R[t] = NMRR_NS;
```

MCR{&lt;c&gt;}{&lt;q&gt;} &lt;coproc&gt;, {#}&lt;opc1&gt;, &lt;Rt&gt;, &lt;CRn&gt;, &lt;CRm&gt;{, {#}&lt;opc2&gt;}

| coproc   | opc1   | CRn    | CRm    | opc2   |
|----------|--------|--------|--------|--------|
| 0b1111   | 0b000  | 0b1010 | 0b0010 | 0b001  |

```
if !IsFeatureImplemented(FEAT_AA32EL1) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && HSTR_EL2.T10 == '1' ↪ → then AArch64.AArch32SystemAccessTrap(EL2, 0x03);
```

```
elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HSTR.T10 == '1' ↪ → then AArch32.TakeHypTrapException(0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && HCR_EL2.TVM == ↪ → '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HCR.TVM == '1' ↪ → then AArch32.TakeHypTrapException(0x03); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA32EL3) && ELUsingAArch32(EL3) then if TTBCR.EAE == '1' then MAIR1_NS = R[t]; else NMRR_NS = R[t]; else if TTBCR.EAE == '1' then MAIR1 = R[t]; else NMRR = R[t]; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && IsFeatureImplemented(FEAT_AA32EL3) && ELUsingAArch32(EL3) then if TTBCR.EAE == '1' then MAIR1_NS = R[t]; else NMRR_NS = R[t]; else if TTBCR.EAE == '1' then MAIR1 = R[t]; else NMRR = R[t]; elsif PSTATE.EL == EL3 then if SCR.NS == '0' && CP15SDISABLE == HIGH then UNDEFINED; elsif SCR.NS == '0' && CP15SDISABLE2 == HIGH then UNDEFINED; else if TTBCR.EAE == '1' then if SCR.NS == '0' then MAIR1_S = R[t]; else MAIR1_NS = R[t]; else if SCR.NS == '0' then NMRR_S = R[t]; else NMRR_NS = R[t];
```