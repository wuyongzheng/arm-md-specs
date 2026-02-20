## G8.2.36 CSSELR, Cache Size Selection Register

The CSSELR characteristics are:

## Purpose

Selects the current Cache Size ID Register, CCSIDR, by specifying the required cache level and the cache type, which is either instruction cache or data cache.

If FEAT\_CCIDX is implemented, CSSELR also selects the current CCSIDR2.

## Configuration

AArch32 System register CSSELR bits [31:0] are architecturally mapped to AArch64 System register CSSELR\_EL1[31:0].

This register is banked between CSSELR and CSSELR\_S and CSSELR\_NS.

This register is present only when FEAT\_AA32EL1 is implemented. Otherwise, direct accesses to CSSELR are UNDEFINED.

## Attributes

CSSELR is a 32-bit register.

This register has the following instances:

- CSSELR, when EL3 is not implemented or FEAT\_AA64 is implemented.
- CSSELR\_S, when FEAT\_AA32EL3 is implemented.
- CSSELR\_NS, when FEAT\_AA32EL3 is implemented.

## Field descriptions

<!-- image -->

| 31   | 4 3   | 1 0   |
|------|-------|-------|
|      | Level | InD   |

## Bits [31:4]

Reserved, RES0.

## Level, bits [3:1]

Cache level of required cache. Permitted values are:

| Level   | Meaning        |
|---------|----------------|
| 0b000   | Level 1 cache. |
| 0b001   | Level 2 cache. |
| 0b010   | Level 3 cache. |
| 0b011   | Level 4 cache. |
| 0b100   | Level 5 cache. |
| 0b101   | Level 6 cache. |
| 0b110   | Level 7 cache. |

All other values are reserved.

If CSSELR.{Level, InD} is programmed to a cache level that is not implemented, then the value for this field on a read of CSSELR is UNKNOWN.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## InD, bit [0]

Instruction not Data bit. Permitted values are:

| InD   | Meaning                |
|-------|------------------------|
| 0b0   | Data or unified cache. |
| 0b1   | Instruction cache.     |

If CSSELR.{Level, InD} is programmed to a cache level that is not implemented, then the value for this field on a read of CSSELR is UNKNOWN.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Accessing CSSELR

Accesses to this register use the following encodings in the System register encoding space:

```
MRC{<c>}{<q>} <coproc>, {#}<opc1>, <Rt>, <CRn>, <CRm>{, {#}<opc2>}
```

| coproc   | opc1   | CRn    | CRm    | opc2   |
|----------|--------|--------|--------|--------|
| 0b1111   | 0b010  | 0b0000 | 0b0000 | 0b000  |

```
if !IsFeatureImplemented(FEAT_AA32EL1) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && HSTR_EL2.T0 == '1' ↪ → then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HSTR.T0 == '1' ↪ → then AArch32.TakeHypTrapException(0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && HCR_EL2.TID2 == ↪ → '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && ↪ → IsFeatureImplemented(FEAT_EVT) && HCR_EL2.TID4 == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HCR.TID2 == '1' ↪ → then AArch32.TakeHypTrapException(0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && ↪ → IsFeatureImplemented(FEAT_EVT) && HCR2.TID4 == '1' then AArch32.TakeHypTrapException(0x03);
```

```
elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA32EL3) && ELUsingAArch32(EL3) then R[t] = CSSELR_NS; else R[t] = CSSELR; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && IsFeatureImplemented(FEAT_AA32EL3) && ELUsingAArch32(EL3) then R[t] = CSSELR_NS; else R[t] = CSSELR; elsif PSTATE.EL == EL3 then if SCR.NS == '0' then R[t] = CSSELR_S; else R[t] = CSSELR_NS;
```

MCR{&lt;c&gt;}{&lt;q&gt;} &lt;coproc&gt;, {#}&lt;opc1&gt;, &lt;Rt&gt;, &lt;CRn&gt;, &lt;CRm&gt;{, {#}&lt;opc2&gt;}

| coproc   | opc1   | CRn    | CRm    | opc2   |
|----------|--------|--------|--------|--------|
| 0b1111   | 0b010  | 0b0000 | 0b0000 | 0b000  |

```
if !IsFeatureImplemented(FEAT_AA32EL1) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && HSTR_EL2.T0 == '1' ↪ → then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HSTR.T0 == '1' ↪ → then AArch32.TakeHypTrapException(0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && HCR_EL2.TID2 == ↪ → '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && ↪ → IsFeatureImplemented(FEAT_EVT) && HCR_EL2.TID4 == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HCR.TID2 == '1' ↪ → then AArch32.TakeHypTrapException(0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && ↪ → IsFeatureImplemented(FEAT_EVT) && HCR2.TID4 == '1' then AArch32.TakeHypTrapException(0x03); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA32EL3) && ELUsingAArch32(EL3) then CSSELR_NS = R[t]; else CSSELR = R[t]; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && IsFeatureImplemented(FEAT_AA32EL3) && ELUsingAArch32(EL3) then CSSELR_NS = R[t]; else CSSELR = R[t]; elsif PSTATE.EL == EL3 then if SCR.NS == '0' then CSSELR_S = R[t]; else CSSELR_NS = R[t];
```