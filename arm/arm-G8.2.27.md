## G8.2.27 CLIDR, Cache Level ID Register

The CLIDR characteristics are:

## Purpose

Identifies the type of cache, or caches, that are implemented at each level and can be managed using the architected cache maintenance instructions that operate by set/way, up to a maximum of seven levels. Also identifies the Level of Coherence (LoC) and Level of Unification (LoU) for the cache hierarchy.

## Configuration

AArch32 System register CLIDR bits [31:0] are architecturally mapped to AArch64 System register CLIDR\_EL1[31:0].

This register is present only when FEAT\_AA32EL1 is implemented. Otherwise, direct accesses to CLIDR are UNDEFINED.

## Attributes

CLIDR is a 32-bit register.

## Field descriptions

| 31 30   | 29   | 26   | 24 23 21   | 20 18   | 17 15   | 14     | 12 11   | 8 6    | 5 3    | 2 0    |
|---------|------|------|------------|---------|---------|--------|---------|--------|--------|--------|
| ICB     | LoUU | LoC  | LoUIS      | Ctype7  | Ctype6  | Ctype5 | Ctype4  | Ctype3 | Ctype2 | Ctype1 |

## ICB, bits [31:30]

Inner cache boundary. This field indicates the boundary for caching Inner Cacheable memory regions.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| ICB   | Meaning                                        |
|-------|------------------------------------------------|
| 0b00  | Not disclosed by this mechanism.               |
| 0b01  | L1 cache is the highest Inner Cacheable level. |
| 0b10  | L2 cache is the highest Inner Cacheable level. |
| 0b11  | L3 cache is the highest Inner Cacheable level. |

Access to this field is RO.

## LoUU, bits [29:27]

Level of Unification Uniprocessor for the cache hierarchy.

For a description of the values of this field, see Terminology for Clean, Invalidate, and Clean and Invalidate instructions.

Note

This field does not describe the requirements for instruction cache invalidation. See CTR.DIC.

Note

When FEAT\_S2FWB is implemented, the architecture requires that this field is zero so that no levels of data cache need to be cleaned in order to manage coherency with instruction fetches.

This field has an IMPLEMENTATION DEFINED value.

Access to this field is RO.

## LoC, bits [26:24]

Level of Coherence for the cache hierarchy.

For a description of the values of this field, see Terminology for Clean, Invalidate, and Clean and Invalidate instructions.

This field has an IMPLEMENTATION DEFINED value.

Access to this field is RO.

## LoUIS, bits [23:21]

Level of Unification Inner Shareable for the cache hierarchy.

For a description of the values of this field, see Terminology for Clean, Invalidate, and Clean and Invalidate instructions.

Note

This field does not describe the requirements for instruction cache invalidation. See CTR.DIC.

Note

When FEAT\_S2FWB is implemented, the architecture requires that this field is zero so that no levels of data cache need to be cleaned in order to manage coherency with instruction fetches.

This field has an IMPLEMENTATION DEFINED value.

Access to this field is RO.

## Ctype&lt;n&gt; , bits [3(n-1)+2:3(n-1)], for n = 7 to 1

Cache Type fields. Indicate the type of cache that is implemented and can be managed using the architected cache maintenance instructions that operate by set/way at each level, from Level 1 up to a maximum of seven levels of cache hierarchy.

| Ctype<n>   | Meaning                               |
|------------|---------------------------------------|
| 0b000      | No cache.                             |
| 0b001      | Instruction cache only.               |
| 0b010      | Data cache only.                      |
| 0b011      | Separate instruction and data caches. |
| 0b100      | Unified cache.                        |

All other values are reserved.

If software reads the Cache Type fields from Ctype1 upwards, once it has seen a value of 0b000 , no caches that can be managed using the architected cache maintenance instructions that operate by set/way exist at further-out levels of the hierarchy. So, for example, if Ctype3 is the first Cache Type field with a value of 0b000 , the values of Ctype4 to Ctype7 must be ignored.

## Accessing CLIDR

Accesses to this register use the following encodings in the System register encoding space:

```
MRC{<c>}{<q>} <coproc>, {#}<opc1>, <Rt>, <CRn>, <CRm>{, {#}<opc2>}
```

| coproc   | opc1   | CRn    | CRm    | opc2   |
|----------|--------|--------|--------|--------|
| 0b1111   | 0b001  | 0b0000 | 0b0000 | 0b001  |

```
if !IsFeatureImplemented(FEAT_AA32EL1) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && HSTR_EL2.T0 == '1' ↪ → then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HSTR.T0 == '1' ↪ → then AArch32.TakeHypTrapException(0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && HCR_EL2.TID2 == ↪ → '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && ↪ → IsFeatureImplemented(FEAT_EVT) && HCR_EL2.TID4 == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HCR.TID2 == '1' ↪ → then AArch32.TakeHypTrapException(0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && ↪ → IsFeatureImplemented(FEAT_EVT) && HCR2.TID4 == '1' then AArch32.TakeHypTrapException(0x03); else R[t] = CLIDR; elsif PSTATE.EL == EL2 then R[t] = CLIDR; elsif PSTATE.EL == EL3 then R[t] = CLIDR;
```