## G8.2.122 PRRR, Primary Region Remap Register

The PRRR characteristics are:

## Purpose

Controls the top-level mapping of the TEX[0], C, and B memory region attributes.

## Configuration

MAIR0 and PRRR are the same register, with a different view depending on the value of TTBCR.EAE:

- When it is set to 0, the register is as described in PRRR.
- When it is set to 1, the register is as described in MAIR0.

When EL3 is not implemented or EL3 is using AArch64, AArch32 System register PRRR bits [31:0] are architecturally mapped to AArch64 System register MAIR\_EL1[31:0].

When EL3 is not implemented or EL3 is using AArch64, AArch32 System register PRRR bits [31:0] are architecturally mapped to AArch32 System register MAIR0[31:0].

When EL3 is using AArch32, AArch32 System register PRRR bits [31:0] are architecturally mapped to AArch32 System register MAIR0[31:0].

When EL3 is using AArch32, AArch32 System register PRRR bits [31:0] are architecturally mapped to AArch32 System register MAIR0[31:0].

This register is banked between PRRR and PRRR\_S and PRRR\_NS.

This register is present only when FEAT\_AA32EL1 is implemented. Otherwise, direct accesses to PRRR are UNDEFINED.

## Attributes

PRRR is a 32-bit register.

This register has the following instances:

- PRRR, when EL3 is not implemented or FEAT\_AA64 is implemented.
- PRRR\_S, when FEAT\_AA32EL3 is implemented.
- PRRR\_NS, when FEAT\_AA32EL3 is implemented.

## Field descriptions

When TTBCR.EAE == '0':

<!-- image -->

## NOS&lt;n&gt; , bits [n+24], for n = 7 to 0

Not Outer Shareable. NOS&lt;n&gt; is the Outer Shareable property for memory attributes n, if the region is mapped as Normal memory that is not Inner Non-cacheable, Outer Non-cacheable, and the appropriate PRRR.{NS0, NS1} field identifies the region as shareable. n is the value of the concatenation of the {TEX[0], C, B} bits from the Translation table descriptor. The possible values of each NOS&lt;n&gt; field other than NOS6 are:

| NOS<n>   | Meaning                           |
|----------|-----------------------------------|
| 0b0      | Memory region is Outer Shareable. |
| 0b1      | Memory region is Inner Shareable. |

The value of this bit is ignored if the region is:

- Device memory
- Normal memory that is at least one of:
- Inner Non-cacheable, Outer Non-cacheable.
- Identified by the appropriate PRRR.{NS0, NS1} field as Non-shareable.

The meaning of the NOS6 field is IMPLEMENTATION DEFINED.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Bits [23:20]

Reserved, RES0.

## NS1, bit [19]

Mapping of S = 1 attribute for Normal memory regions. This field is used in determining the Shareability of a memory region that is mapped to Normal memory and both:

- Is not Inner Non-cacheable, Outer Non-cacheable.
- Has the S bit in the Translation table descriptor set to 1.

| NS1   | Meaning                                                                                                                                  |
|-------|------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0   | Region is Non-shareable.                                                                                                                 |
| 0b1   | Region is shareable. The value of the appropriate PRRR.NOS<n> field determines whether the region is Inner Shareable or Outer Shareable. |

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## NS0, bit [18]

Mapping of S = 0 attribute for Normal memory regions. This field is used in determining the Shareability of a memory region that is mapped to Normal memory and both:

- Is not Inner Non-cacheable, Outer Non-cacheable.
- Has the S bit in the Translation table descriptor set to 0.

| NS0   | Meaning                                                                                                                                  |
|-------|------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0   | Region is Non-shareable.                                                                                                                 |
| 0b1   | Region is shareable. The value of the appropriate PRRR.NOS<n> field determines whether the region is Inner Shareable or Outer Shareable. |

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## DS1, bit [17]

Mapping of S = 1 attribute for Device memory. From Armv8.0, all types of Device memory are Outer Shareable, and therefore this bit is RES1.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## DS0, bit [16]

Mapping of S = 0 attribute for Device memory. From Armv8.0, all types of Device memory are Outer Shareable, and therefore this bit is RES1.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## TR&lt;n&gt; , bits [2n+1:2n], for n = 7 to 0

TR&lt;n&gt; is the primary TEX mapping for memory attributes n, and defines the mapped memory type for a region with attributes n. n is the value of the concatenation of the {TEX[0], C, B} bits from the Translation table descriptor. The possible values for each field other than TR6 are:

| TR<n>   | Meaning              |
|---------|----------------------|
| 0b00    | Device-nGnRnE memory |
| 0b01    | Device-nGnRE memory  |
| 0b10    | Normal memory        |

The value 0b11 is reserved. The effect of programming a field to 0b11 is CONSTRAINED UNPREDICTABLE.

The meaning of the TR6 field is IMPLEMENTATION DEFINED.

When FEAT\_XS is implemented, stage 1 Inner Write-Back Cacheable, Outer Write-Back Cacheable memory types have the XS attribute set to 0.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Accessing PRRR

Accesses to this register use the following encodings in the System register encoding space:

```
MRC{<c>}{<q>} <coproc>, {#}<opc1>, <Rt>, <CRn>, <CRm>{, {#}<opc2>}
```

| coproc   | opc1   | CRn    | CRm    | opc2   |
|----------|--------|--------|--------|--------|
| 0b1111   | 0b000  | 0b1010 | 0b0010 | 0b000  |

```
if !IsFeatureImplemented(FEAT_AA32EL1) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then
```

```
if EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && HSTR_EL2.T10 == '1' ↪ → then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HSTR.T10 == '1' ↪ → then AArch32.TakeHypTrapException(0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && HCR_EL2.TRVM == ↪ → '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HCR.TRVM == '1' ↪ → then AArch32.TakeHypTrapException(0x03); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA32EL3) && ELUsingAArch32(EL3) then if TTBCR.EAE == '1' then R[t] = MAIR0_NS; else R[t] = PRRR_NS; else if TTBCR.EAE == '1' then R[t] = MAIR0; else R[t] = PRRR; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && IsFeatureImplemented(FEAT_AA32EL3) && ELUsingAArch32(EL3) then if TTBCR.EAE == '1' then R[t] = MAIR0_NS; else R[t] = PRRR_NS; else if TTBCR.EAE == '1' then R[t] = MAIR0; else R[t] = PRRR; elsif PSTATE.EL == EL3 then if TTBCR.EAE == '1' then if SCR.NS == '0' then R[t] = MAIR0_S; else R[t] = MAIR0_NS; else if SCR.NS == '0' then R[t] = PRRR_S; else R[t] = PRRR_NS;
```

MCR{&lt;c&gt;}{&lt;q&gt;} &lt;coproc&gt;, {#}&lt;opc1&gt;, &lt;Rt&gt;, &lt;CRn&gt;, &lt;CRm&gt;{, {#}&lt;opc2&gt;}

| coproc   | opc1   | CRn    | CRm    | opc2   |
|----------|--------|--------|--------|--------|
| 0b1111   | 0b000  | 0b1010 | 0b0010 | 0b000  |

```
if !IsFeatureImplemented(FEAT_AA32EL1) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && HSTR_EL2.T10 == '1' ↪ → then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HSTR.T10 == '1' ↪ → then
```

```
AArch32.TakeHypTrapException(0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && HCR_EL2.TVM == ↪ → '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HCR.TVM == '1' ↪ → then AArch32.TakeHypTrapException(0x03); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA32EL3) && ELUsingAArch32(EL3) then if TTBCR.EAE == '1' then MAIR0_NS = R[t]; else PRRR_NS = R[t]; else if TTBCR.EAE == '1' then MAIR0 = R[t]; else PRRR = R[t]; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && IsFeatureImplemented(FEAT_AA32EL3) && ELUsingAArch32(EL3) then if TTBCR.EAE == '1' then MAIR0_NS = R[t]; else PRRR_NS = R[t]; else if TTBCR.EAE == '1' then MAIR0 = R[t]; else PRRR = R[t]; elsif PSTATE.EL == EL3 then if SCR.NS == '0' && CP15SDISABLE == HIGH then UNDEFINED; elsif SCR.NS == '0' && CP15SDISABLE2 == HIGH then UNDEFINED; else if TTBCR.EAE == '1' then if SCR.NS == '0' then MAIR0_S = R[t]; else MAIR0_NS = R[t]; else if SCR.NS == '0' then PRRR_S = R[t]; else PRRR_NS = R[t];
```