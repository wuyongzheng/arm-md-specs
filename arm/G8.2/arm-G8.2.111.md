## G8.2.111 MAIR0, Memory Attribute Indirection Register 0

The MAIR0 characteristics are:

## Purpose

Along with MAIR1, provides the memory attribute encodings corresponding to the possible AttrIndx values in a Long-descriptor format translation table entry for stage 1 translations.

AttrIndx[2] indicates the MAIR register to be used:

- When AttrIndx[2] is 0, MAIR0 is used.
- When AttrIndx[2] is 1, MAIR1 is used.

## Configuration

MAIR0 and PRRR are the same register, with a different view depending on the value of TTBCR.EAE:

- When it is set to 0, the register is as described in PRRR.
- When it is set to 1, the register is as described in MAIR0.

When EL3 is using AArch32, write access to MAIR0(S) is disabled when the CP15SDISABLE signal is asserted HIGH.

When EL3 is not implemented or EL3 is using AArch64, AArch32 System register MAIR0 bits [31:0] are architecturally mapped to AArch64 System register MAIR\_EL1[31:0].

When EL3 is not implemented or EL3 is using AArch64, AArch32 System register MAIR0 bits [31:0] are architecturally mapped to AArch32 System register PRRR[31:0].

When EL3 is using AArch32, AArch32 System register MAIR0 bits [31:0] are architecturally mapped to AArch32 System register PRRR[31:0].

When EL3 is using AArch32, AArch32 System register MAIR0 bits [31:0] are architecturally mapped to AArch32 System register PRRR[31:0].

This register is banked between MAIR0 and MAIR0\_S and MAIR0\_NS.

This register is present only when FEAT\_AA32EL1 is implemented. Otherwise, direct accesses to MAIR0 are UNDEFINED.

## Attributes

MAIR0 is a 32-bit register.

This register has the following instances:

- MAIR0, when EL3 is not implemented or FEAT\_AA64 is implemented.
- MAIR0\_S, when FEAT\_AA32EL3 is implemented.
- MAIR0\_NS, when FEAT\_AA32EL3 is implemented.

## Field descriptions

When TTBCR.EAE == '1':

<!-- image -->

## Attr&lt;n&gt; , bits [8n+7:8n], for n = 3 to 0

The memory attribute encoding for an AttrIndx[2:0] entry in a Long descriptor format translation table entry, where:

- AttrIndx[2:0] gives the value of &lt;n&gt; in Attr&lt;n&gt;.

- AttrIndx[2] defines which MAIR to access. Attr7 to Attr4 are in MAIR1, and Attr3 to Attr0 are in MAIR0.

Bits [7:4] are encoded as follows:

| Attr<n>[7:4]        | Meaning                                                                    |
|---------------------|----------------------------------------------------------------------------|
| 0b0000              | Device memory. See encoding of Attr<n>[3:0] for the type of Device memory. |
| 0b00 RW, RWnot 0b00 | Normal memory, Outer Write-Through Transient.                              |
| 0b0100              | Normal memory, Outer Non-cacheable.                                        |
| 0b01 RW, RWnot 0b00 | Normal memory, Outer Write-Back Transient.                                 |
| 0b10 RW             | Normal memory, Outer Write-Through Non-transient.                          |
| 0b11 RW             | Normal memory, Outer Write-Back Non-transient.                             |

R=Outer Read-Allocate policy, W = Outer Write-Allocate policy.

The meaning of bits [3:0] depends on the value of bits [7:4]:

| Attr<n>[3:0]        | Meaning when Attr<n>[7:4] is 0b0000   | Meaning when Attr<n>[7:4] is not 0b0000                      |
|---------------------|---------------------------------------|--------------------------------------------------------------|
| 0b0000              | Device-nGnRnE memory                  | UNPREDICTABLE                                                |
| 0b00 RW, RWnot 0b00 | UNPREDICTABLE                         | Normal memory, Inner Write-Through Transient                 |
| 0b0100              | Device-nGnRE memory                   | Normal memory, Inner Non-cacheable                           |
| 0b01 RW, RWnot 0b00 | UNPREDICTABLE                         | Normal memory, Inner Write-Back Transient                    |
| 0b1000              | Device-nGRE memory                    | Normal memory, Inner Write-Through Non-transient (RW= 0b00 ) |
| 0b10 RW, RWnot 0b00 | UNPREDICTABLE                         | Normal memory, Inner Write-Through Non-transient             |
| 0b1100              | Device-GRE memory                     | Normal memory, Inner Write-Back Non-transient (RW= 0b00 )    |
| 0b11 RW, RWnot 0b00 | UNPREDICTABLE                         | Normal memory, Inner Write-Back Non-transient                |

R=Inner Read-Allocate policy, W = Inner Write-Allocate policy.

The R and W bits in some Attr&lt;n&gt; fields have the following meanings:

| R or W   | Meaning     |
|----------|-------------|
| 0b0      | No Allocate |
| 0b1      | Allocate    |

When FEAT\_XS is implemented, stage 1 Inner Write-Back Cacheable, Outer Write-Back Cacheable memory types have the XS attribute set to 0.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Accessing MAIR0

Accesses to this register use the following encodings in the System register encoding space:

MRC{&lt;c&gt;}{&lt;q&gt;} &lt;coproc&gt;, {#}&lt;opc1&gt;, &lt;Rt&gt;, &lt;CRn&gt;, &lt;CRm&gt;{, {#}&lt;opc2&gt;}

| coproc   | opc1   | CRn    | CRm    | opc2   |
|----------|--------|--------|--------|--------|
| 0b1111   | 0b000  | 0b1010 | 0b0010 | 0b000  |

```
if !IsFeatureImplemented(FEAT_AA32EL1) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && HSTR_EL2.T10 == '1' ↪ → then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HSTR.T10 == '1' ↪ → then AArch32.TakeHypTrapException(0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && HCR_EL2.TRVM == ↪ → '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HCR.TRVM == '1' ↪ → then AArch32.TakeHypTrapException(0x03); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA32EL3) && ELUsingAArch32(EL3) then if TTBCR.EAE == '1' then R[t] = MAIR0_NS; else R[t] = PRRR_NS; else if TTBCR.EAE == '1' then R[t] = MAIR0; else R[t] = PRRR; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && IsFeatureImplemented(FEAT_AA32EL3) && ELUsingAArch32(EL3) then if TTBCR.EAE == '1' then R[t] = MAIR0_NS; else R[t] = PRRR_NS; else if TTBCR.EAE == '1' then R[t] = MAIR0; else R[t] = PRRR; elsif PSTATE.EL == EL3 then if TTBCR.EAE == '1' then if SCR.NS == '0' then R[t] = MAIR0_S; else R[t] = MAIR0_NS; else if SCR.NS == '0' then R[t] = PRRR_S; else R[t] = PRRR_NS;
```

| coproc   | opc1   | CRn    | CRm    | opc2   |
|----------|--------|--------|--------|--------|
| 0b1111   | 0b000  | 0b1010 | 0b0010 | 0b000  |

```
if !IsFeatureImplemented(FEAT_AA32EL1) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && HSTR_EL2.T10 == '1' ↪ → then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HSTR.T10 == '1' ↪ → then AArch32.TakeHypTrapException(0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && HCR_EL2.TVM == ↪ → '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HCR.TVM == '1' ↪ → then AArch32.TakeHypTrapException(0x03); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA32EL3) && ELUsingAArch32(EL3) then if TTBCR.EAE == '1' then MAIR0_NS = R[t]; else PRRR_NS = R[t]; else if TTBCR.EAE == '1' then MAIR0 = R[t]; else PRRR = R[t]; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && IsFeatureImplemented(FEAT_AA32EL3) && ELUsingAArch32(EL3) then if TTBCR.EAE == '1' then MAIR0_NS = R[t]; else PRRR_NS = R[t]; else if TTBCR.EAE == '1' then MAIR0 = R[t]; else PRRR = R[t]; elsif PSTATE.EL == EL3 then if SCR.NS == '0' && CP15SDISABLE == HIGH then UNDEFINED; elsif SCR.NS == '0' && CP15SDISABLE2 == HIGH then UNDEFINED; else if TTBCR.EAE == '1' then if SCR.NS == '0' then MAIR0_S = R[t]; else MAIR0_NS = R[t]; else if SCR.NS == '0' then PRRR_S = R[t]; else PRRR_NS = R[t];
```