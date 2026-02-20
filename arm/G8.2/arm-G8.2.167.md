## G8.2.167 TTBR0, Translation Table Base Register 0

The TTBR0 characteristics are:

## Purpose

Holds the base address of the translation table for the initial lookup for stage 1 of the translation of an address from the lower VA range in the PL1&amp;0 translation regime, and other information for this translation regime.

## Configuration

TTBR0 is a 64-bit register that can also be accessed as a 32-bit value. If it is accessed as a 32-bit register, accesses read and write bits [31:0] and do not modify bits [63:32].

TTBCR.EAE determines which TTBR0 format is used:

- TTBCR.EAE == 0b0 : 32-bit format is used. TTBR0[63:32] are ignored.
- TTBCR.EAE == 0b1 : 64-bit format is used.

When EL3 is using AArch32, write access to TTBR0(S) is disabled when the CP15SDISABLE signal is asserted HIGH.

Used in conjunction with the TTBCR. When the 64-bit TTBR0 format is used, cacheability and shareability information is held in the TTBCR, not in TTBR0.

AArch32 System register TTBR0 bits [63:0] are architecturally mapped to AArch64 System register TTBR0\_EL1[63:0].

This register is banked between TTBR0 and TTBR0\_S and TTBR0\_NS.

This register is present only when FEAT\_AA32EL1 is implemented. Otherwise, direct accesses to TTBR0 are UNDEFINED.

## Attributes

TTBR0 is a 64-bit register.

This register has the following instances:

- TTBR0, when EL3 is not implemented or FEAT\_AA64 is implemented.
- TTBR0\_S, when FEAT\_AA32EL3 is implemented.
- TTBR0\_NS, when FEAT\_AA32EL3 is implemented.

## Field descriptions

When TTBCR.EAE == '0':

<!-- image -->

Bits [63:32]

Reserved, RES0.

## TTB0, bits [31:7]

Translation table base address, bits[31:x], where x is 14-(TTBCR.N). Register bits [x-1:7] are RES0, with the additional requirement that if these bits are not all zero, this is a misaligned translation table base address, with effects that are CONSTRAINED UNPREDICTABLE, and must be one of the following:

- Register bits [x-1:7] are treated as if all the bits are zero. The value read back from these bits is either the value written or zero.
- The result of the calculation of an address for a translation table walk using this register can be corrupted in those bits that are nonzero.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## IRGN, bits [0, 6]

Inner region bits. Bits [0,6] of this register together indicate the Inner Cacheability attributes for the memory associated with the translation table walks. The possible values of IRGN[1:0] are:

| IRGN   | Meaning                                                      |
|--------|--------------------------------------------------------------|
| 0b00   | Normal memory, Inner Non-cacheable.                          |
| 0b01   | Normal memory, Inner Write-Back Write-Allocate Cacheable.    |
| 0b10   | Normal memory, Inner Write-Through Cacheable.                |
| 0b11   | Normal memory, Inner Write-Back no Write-Allocate Cacheable. |

## Note

The encoding of the IRGN bits is counter-intuitive, with register bit[6] being IRGN[0] and register bit[0] being IRGN[1]. This encoding is chosen to give a consistent encoding of memory region types and to ensure that software written for ARMv7 without the Multiprocessing Extensions can run unmodified on an implementation that includes the functionality introduced by the ARMv7 Multiprocessing Extensions.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## NOS, bit [5]

Not Outer Shareable. When the value of TTBR0.S is 1, indicates whether the memory associated with a translation table walk is Inner Shareable or Outer Shareable:

| NOS   | Meaning                    |
|-------|----------------------------|
| 0b0   | Memory is Outer Shareable. |
| 0b1   | Memory is Inner Shareable. |

This bit is ignored when the value of TTBR0.S is 0.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## RGN, bits [4:3]

Region bits. Indicates the Outer cacheability attributes for the memory associated with the translation table walks:

| RGN   | Meaning                                                      |
|-------|--------------------------------------------------------------|
| 0b00  | Normal memory, Outer Non-cacheable.                          |
| 0b01  | Normal memory, Outer Write-Back Write-Allocate Cacheable.    |
| 0b10  | Normal memory, Outer Write-Through Cacheable.                |
| 0b11  | Normal memory, Outer Write-Back no Write-Allocate Cacheable. |

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## IMP, bit [2]

The effect of this bit is IMPLEMENTATION DEFINED. If the translation table implementation does not include any IMPLEMENTATION DEFINED features this bit is RES0.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## S, bit [1]

Shareable. Indicates whether the memory associated with the translation table walks is Shareable:

| S   | Meaning                                                                                                      |
|-----|--------------------------------------------------------------------------------------------------------------|
| 0b0 | Memory is Non-shareable.                                                                                     |
| 0b1 | Memory is Shareable. The TTBR0.NOS field indicates whether the memory is Inner Shareable or Outer Shareable. |

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## When TTBCR.EAE == '1':

<!-- image -->

## Bits [63:56]

Reserved, RES0.

## ASID, bits [55:48]

An ASID for the translation table base address. The TTBCR.A1 field selects either TTBR0.ASID or TTBR1.ASID.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## BADDR, bits [47:1]

Translation table base address, bits[47:x], Bits [x-1:1] are RES0, with the additional requirement that if bits[x-1:3] are not all zero, this is a misaligned translation table base address, with effects that are CONSTRAINED UNPREDICTABLE, and must be one of the following:

- Register bits [x-1:3] are treated as if all the bits are zero. The value read back from these bits is either the value written or zero.
- The result of the calculation of an address for a translation table walk using this register can be corrupted in those bits that are nonzero.

x is determined from the value of TTBCR.T0SZ as follows:

- If TTBCR.T0SZ is 0 or 1, x = 5 - TTBCR.T0SZ.
- If TTBCR.T0SZ is greater than 1, x = 14 - TTBCR.T0SZ.

If bits[47:40] of the translation table base address are not zero, an Address size fault is generated.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## CnP, bit [0]

## When FEAT\_TTCNP is implemented:

Common not Private. When TTBCR.EAE ==1, this bit indicates whether each entry that is pointed to by TTBR0 is a member of a common set that can be used by every PE in the Inner Shareable domain for which the value of TTBR0.CnP is 1.

| CnP   | Meaning                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
|-------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0   | The translation table entries pointed to by this instance of TTBR0, for the current ASID, are permitted to differ from corresponding entries for this instance of TTBR0 for other PEs in the Inner Shareable domain. This is not affected by: • The value of TTBR0.CnP on those other PEs. • The value of TTBCR.EAE on those other PEs. • The value of the current ASID or, for the Non-secure instance of TTBR0, the value of the current VMID.                                                                              |
| 0b1   | The translation table entries pointed to by this instance of TTBR0 are the same as the translation table entries for every other PE in the Inner Shareable domain for which the value of TTBR0.CnP is 1 for this instance of TTBR0 and all of the following apply: • The translation table entries are pointed to by this instance of TTBR0. • The value of the applicable TTBCR.EAE field is 1. • The ASID is the same as the current ASID. • For the Non-secure instance of TTBR0, the VMIDis the same as the current VMID. |

When a TLB combines entries from stage 1 translation and stage 2 translation into a single entry, that entry can only be shared between different PEs if the value of the CnP bit is 1 for both stage 1 and stage 2.

Note

If the value of the TTBR0.CnP bit is 1 on multiple PEs in the same Inner Shareable domain and those TTBR0s do not point to the same translation table entries when the other conditions specified for the case when the value of CnP is 1 apply, then the results of translations are CONSTRAINED UNPREDICTABLE, see 'CONSTRAINED UNPREDICTABLE behaviors due to caching of control or data values'.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## Accessing TTBR0

Accesses to this register use the following encodings in the System register encoding space:

MRC{&lt;c&gt;}{&lt;q&gt;} &lt;coproc&gt;, {#}&lt;opc1&gt;, &lt;Rt&gt;, &lt;CRn&gt;, &lt;CRm&gt;{, {#}&lt;opc2&gt;}

| coproc   | opc1   | CRn    | CRm    | opc2   |
|----------|--------|--------|--------|--------|
| 0b1111   | 0b000  | 0b0010 | 0b0000 | 0b000  |

```
if !IsFeatureImplemented(FEAT_AA32EL1) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && HSTR_EL2.T2 == '1' ↪ → then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HSTR.T2 == '1' ↪ → then AArch32.TakeHypTrapException(0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && HCR_EL2.TRVM == ↪ → '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HCR.TRVM == '1' ↪ → then AArch32.TakeHypTrapException(0x03); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA32EL3) && ELUsingAArch32(EL3) then R[t] = TTBR0_NS<31:0>; else R[t] = TTBR0<31:0>; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && IsFeatureImplemented(FEAT_AA32EL3) && ELUsingAArch32(EL3) then R[t] = TTBR0_NS<31:0>; else R[t] = TTBR0<31:0>; elsif PSTATE.EL == EL3 then if SCR.NS == '0' then R[t] = TTBR0_S<31:0>; else R[t] = TTBR0_NS<31:0>;
```

MCR{&lt;c&gt;}{&lt;q&gt;} &lt;coproc&gt;, {#}&lt;opc1&gt;, &lt;Rt&gt;, &lt;CRn&gt;, &lt;CRm&gt;{, {#}&lt;opc2&gt;}

| coproc   | opc1   | CRn    | CRm    | opc2   |
|----------|--------|--------|--------|--------|
| 0b1111   | 0b000  | 0b0010 | 0b0000 | 0b000  |

```
if !IsFeatureImplemented(FEAT_AA32EL1) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && HSTR_EL2.T2 == '1' ↪ → then AArch64.AArch32SystemAccessTrap(EL2, 0x03);
```

```
elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HSTR.T2 == '1' ↪ → then AArch32.TakeHypTrapException(0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && HCR_EL2.TVM == ↪ → '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HCR.TVM == '1' ↪ → then AArch32.TakeHypTrapException(0x03); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA32EL3) && ELUsingAArch32(EL3) then TTBR0_NS<31:0> = R[t]; else TTBR0<31:0> = R[t]; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && IsFeatureImplemented(FEAT_AA32EL3) && ELUsingAArch32(EL3) then TTBR0_NS<31:0> = R[t]; else TTBR0<31:0> = R[t]; elsif PSTATE.EL == EL3 then if SCR.NS == '0' && CP15SDISABLE == HIGH then UNDEFINED; else if SCR.NS == '0' then TTBR0_S<31:0> = R[t]; else TTBR0_NS<31:0> = R[t];
```

MRRC{&lt;c&gt;}{&lt;q&gt;} &lt;coproc&gt;, {#}&lt;opc1&gt;, &lt;Rt&gt;, &lt;Rt2&gt;, &lt;CRm&gt;

| coproc   | CRm    | opc1   |
|----------|--------|--------|
| 0b1111   | 0b0010 | 0b0000 |

```
if !IsFeatureImplemented(FEAT_AA32EL1) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && HSTR_EL2.T2 == '1' ↪ → then AArch64.AArch32SystemAccessTrap(EL2, 0x04); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HSTR.T2 == '1' ↪ → then AArch32.TakeHypTrapException(0x04); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && HCR_EL2.TRVM == ↪ → '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x04); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HCR.TRVM == '1' ↪ → then AArch32.TakeHypTrapException(0x04); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA32EL3) && ELUsingAArch32(EL3) then R[t, t2] = TTBR0_NS; else R[t, t2] = TTBR0; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && IsFeatureImplemented(FEAT_AA32EL3) && ELUsingAArch32(EL3) then R[t, t2] = TTBR0_NS; else R[t, t2] = TTBR0; elsif PSTATE.EL == EL3 then if SCR.NS == '0' then
```

```
R[t, t2] = TTBR0_S; else R[t, t2] = TTBR0_NS;
```

MCRR{&lt;c&gt;}{&lt;q&gt;} &lt;coproc&gt;, {#}&lt;opc1&gt;, &lt;Rt&gt;, &lt;Rt2&gt;, &lt;CRm&gt;

| coproc   | CRm    | opc1   |
|----------|--------|--------|
| 0b1111   | 0b0010 | 0b0000 |

```
if !IsFeatureImplemented(FEAT_AA32EL1) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && HSTR_EL2.T2 == '1' ↪ → then AArch64.AArch32SystemAccessTrap(EL2, 0x04); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HSTR.T2 == '1' ↪ → then AArch32.TakeHypTrapException(0x04); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && HCR_EL2.TVM == ↪ → '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x04); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HCR.TVM == '1' ↪ → then AArch32.TakeHypTrapException(0x04); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA32EL3) && ELUsingAArch32(EL3) then TTBR0_NS = R[t, t2]; else TTBR0 = R[t, t2]; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && IsFeatureImplemented(FEAT_AA32EL3) && ELUsingAArch32(EL3) then TTBR0_NS = R[t, t2]; else TTBR0 = R[t, t2]; elsif PSTATE.EL == EL3 then if SCR.NS == '0' && CP15SDISABLE == HIGH then UNDEFINED; else if SCR.NS == '0' then TTBR0_S = R[t, t2]; else TTBR0_NS = R[t, t2];
```