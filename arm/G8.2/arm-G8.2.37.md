## G8.2.37 CTR, Cache Type Register

The CTR characteristics are:

## Purpose

Provides information about the architecture of the caches.

## Configuration

AArch32 System register CTR bits [31:0] are architecturally mapped to AArch64 System register CTR\_EL0[31:0].

This register is present only when FEAT\_AA32EL1 is implemented. Otherwise, direct accesses to CTR are UNDEFINED.

## Attributes

CTR is a 32-bit register.

## Field descriptions

<!-- image -->

## Bit [31]

Reserved, RES1.

## Bit [30]

Reserved, RES0.

## DIC, bit [29]

Instruction cache invalidation requirements for data to instruction coherence.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| DIC   | Meaning                                                                                                       |
|-------|---------------------------------------------------------------------------------------------------------------|
| 0b0   | Instruction cache invalidation to the Point of Unification is required for data to instruction coherence.     |
| 0b1   | Instruction cache invalidation to the Point of Unification is not required for data to instruction coherence. |

All PEs in the same Inner Shareable shareability domain must have a common value of this field.

Access to this field is RO.

## IDC, bit [28]

Data cache clean requirements for instruction to data coherence. The meaning of this bit is:

The value of this field is an IMPLEMENTATION DEFINED choice of:

| IDC   | Meaning                                                                                                                                                                   |
|-------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0   | Data cache clean to the Point of Unification is required for instruction to data coherence, unless CLIDR.LoC == 0b000 or (CLIDR.LoUIS == 0b000 and CLIDR.LoUU == 0b000 ). |
| 0b1   | Data cache clean to the Point of Unification is not required for instruction to data coherence.                                                                           |

If CTR.DIC is 1, then the value reported in this field must be 1.

The Effective value of IDC is 1 if any of the following are true:

- CTR.IDC == 1.
- CLIDR.LoC == 0b000 .
- CLIDR.LoUIS == 0b000 and CLIDR.LoUU == 0b000 .

All PEs in the same Inner Shareable shareability domain must have a common Effective value of IDC.

Access to this field is RO.

## CWG,bits [27:24]

Cache writeback granule. Log2 of the number of words of the maximum size of memory that can be overwritten as a result of the eviction of a cache entry that has had a memory location in it modified.

Avalue of 0b0000 indicates that this register does not provide Cache writeback granule information and either:

- The architectural maximum of 512 words (2KB) must be assumed.
- The Cache writeback granule can be determined from maximum cache line size encoded in the Cache Size ID Registers.

Values greater than 0b1001 are reserved.

Arm recommends that an implementation that does not support cache write-back implements this field as 0b0001 . This applies, for example, to an implementation that supports only write-through caches.

This field has an IMPLEMENTATION DEFINED value.

Access to this field is RO.

## ERG, bits [23:20]

Exclusives reservation granule. Log2 of the number of words of the maximum size of the reservation granule that has been implemented for the Load-Exclusive and Store-Exclusive instructions.

The use of the value 0b0000 is deprecated.

The value 0b0001 and values greater than 0b1001 are reserved.

This field has an IMPLEMENTATION DEFINED value.

Access to this field is RO.

## DminLine, bits [19:16]

Log2 of the number of words in the smallest cache line of all the data caches and unified caches that are controlled by the PE.

This field has an IMPLEMENTATION DEFINED value.

Access to this field is RO.

## L1Ip, bits [15:14]

Level 1 instruction cache policy. Indicates the indexing and tagging policy for the L1 instruction cache.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| L1Ip   | Meaning                                          |
|--------|--------------------------------------------------|
| 0b00   | Reserved.                                        |
| 0b01   | ASID-tagged Virtual Index, Virtual Tag (AIVIVT). |
| 0b10   | Virtual Index, Physical Tag (VIPT).              |
| 0b11   | Physical Index, Physical Tag (PIPT).             |

From Armv8.0, the value 0b01 is not permitted.

Access to this field is RO.

## Bits [13:4]

Reserved, RES0.

## IminLine, bits [3:0]

Log2 of the number of words in the smallest cache line of all the instruction caches that are controlled by the PE.

This field has an IMPLEMENTATION DEFINED value.

Access to this field is RO.

## Accessing CTR

Accesses to this register use the following encodings in the System register encoding space:

```
MRC{<c>}{<q>} <coproc>, {#}<opc1>, <Rt>, <CRn>, <CRm>{, {#}<opc2>}
```

| coproc   | opc1   | CRn    | CRm    | opc2   |
|----------|--------|--------|--------|--------|
| 0b1111   | 0b000  | 0b0000 | 0b0000 | 0b001  |

```
if !IsFeatureImplemented(FEAT_AA32EL1) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && HSTR_EL2.T0 == '1' ↪ → then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HSTR.T0 == '1' ↪ → then AArch32.TakeHypTrapException(0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && HCR_EL2.TID2 == ↪ → '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HCR.TID2 == '1' ↪ → then AArch32.TakeHypTrapException(0x03); else R[t] = CTR; elsif PSTATE.EL == EL2 then R[t] = CTR; elsif PSTATE.EL == EL3 then R[t] = CTR;
```