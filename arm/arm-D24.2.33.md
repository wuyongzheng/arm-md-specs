## D24.2.33 CLIDR\_EL1, Cache Level ID Register

The CLIDR\_EL1 characteristics are:

## Purpose

Identifies the type of cache, or caches, that are implemented at each level and can be managed using the architected cache maintenance instructions that operate by set/way, up to a maximum of seven levels. Also identifies the Level of Coherence (LoC) and Level of Unification (LoU) for the cache hierarchy.

## Configuration

AArch64 System register CLIDR\_EL1 bits [31:0] are architecturally mapped to AArch32 System register CLIDR[31:0].

This register is present only when FEAT\_AA64 is implemented. Otherwise, direct accesses to CLIDR\_EL1 are UNDEFINED.

## Attributes

CLIDR\_EL1 is a 64-bit register.

## Field descriptions

<!-- image -->

## Bits [63:47]

Reserved, RES0.

Ttype&lt;n&gt; , bits [2(n-1)+34:2(n-1)+33], for n = 7 to 1

## When FEAT\_MTE2 is implemented:

Tag cache type. Indicate the type of cache that is implemented and can be managed using the architected cache maintenance instructions that operate by set/way at each level, from Level 1 up to a maximum of seven levels of cache hierarchy.

| Ttype<n>   | Meaning                                                                            |
|------------|------------------------------------------------------------------------------------|
| 0b00       | No Tag Cache.                                                                      |
| 0b01       | Separate Allocation Tag Cache.                                                     |
| 0b10       | Unified Allocation Tag and Data cache, Allocation Tags and Data in unified lines.  |
| 0b11       | Unified Allocation Tag and Data cache, Allocation Tags and Data in separate lines. |

## Otherwise:

Reserved, RES0.

## ICB, bits [32:30]

Inner cache boundary. This field indicates the boundary for caching Inner Cacheable memory regions.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| ICB   | Meaning                                        |
|-------|------------------------------------------------|
| 0b000 | Not disclosed by this mechanism.               |
| 0b001 | L1 cache is the highest Inner Cacheable level. |
| 0b010 | L2 cache is the highest Inner Cacheable level. |
| 0b011 | L3 cache is the highest Inner Cacheable level. |
| 0b100 | L4 cache is the highest Inner Cacheable level. |
| 0b101 | L5 cache is the highest Inner Cacheable level. |
| 0b110 | L6 cache is the highest Inner Cacheable level. |
| 0b111 | L7 cache is the highest Inner Cacheable level. |

Access to this field is RO.

## LoUU, bits [29:27]

Level of Unification Uniprocessor for the cache hierarchy.

For a description of the values of this field, see Terminology for Clean, Invalidate, and Clean and Invalidate instructions.

Note

This field does not describe the requirements for instruction cache invalidation. See CTR\_EL0.DIC.

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

This field does not describe the requirements for instruction cache invalidation. See CTR\_EL0.DIC.

Note

When FEAT\_S2FWB is implemented, the architecture requires that this field is zero so that no levels of data cache need to be cleaned in order to manage coherency with instruction fetches.

This field has an IMPLEMENTATION DEFINED value.

Access to this field is RO.

## Ctype&lt;n&gt; , bits [3(n-1)+2:3(n-1)], for n = 7 to 1

Cache Type fields. Indicate the type of cache that is implemented and can be managed using the architected cache maintenance instructions that operate by set/way at each level, from Level 1 up to a maximum of seven levels of cache hierarchy. Possible values of each field are:

| Ctype<n>   | Meaning                               |
|------------|---------------------------------------|
| 0b000      | No cache.                             |
| 0b001      | Instruction cache only.               |
| 0b010      | Data cache only.                      |
| 0b011      | Separate instruction and data caches. |
| 0b100      | Unified cache.                        |

All other values are reserved.

If software reads the Cache Type fields from Ctype1 upwards, once it has seen a value of 0b000 , no caches that can be managed using the architected cache maintenance instructions that operate by set/way exist at further-out levels of the hierarchy. So, for example, if Ctype3 is the first Cache Type field with a value of 0b000 , the values of Ctype4 to Ctype7 must be ignored.

## Accessing CLIDR\_EL1

Accesses to this register use the following encodings in the System register encoding space:

MRS &lt;Xt&gt;, CLIDR\_EL1

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b001 | 0b0000 | 0b0000 | 0b001 |

```
if !IsFeatureImplemented(FEAT_AA64) then UnimplementedIDRegister(); elsif PSTATE.EL == EL0 then if IsFeatureImplemented(FEAT_IDST) then if EL2Enabled() && HCR_EL2.TGE == '1' then AArch64.SystemAccessTrap(EL2, 0x18); else AArch64.SystemAccessTrap(EL1, 0x18); else UNDEFINED; elsif PSTATE.EL == EL1 then if EL2Enabled() && HCR_EL2.TID2 == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && IsFeatureImplemented(FEAT_EVT) && HCR_EL2.TID4 == '1' then AArch64.SystemAccessTrap(EL2, 0x18);
```

```
elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') && ↪ → HFGRTR_EL2.CLIDR_EL1 == '1' then AArch64.SystemAccessTrap(EL2, 0x18); else X[t, 64] = CLIDR_EL1; elsif PSTATE.EL == EL2 then X[t, 64] = CLIDR_EL1; elsif PSTATE.EL == EL3 then X[t, 64] = CLIDR_EL1;
```