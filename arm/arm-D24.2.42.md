## D24.2.42 CTR\_EL0, Cache Type Register

The CTR\_EL0 characteristics are:

## Purpose

Provides information about the architecture of the caches.

## Configuration

AArch64 System register CTR\_EL0 bits [31:0] are architecturally mapped to AArch32 System register CTR[31:0].

This register is present only when FEAT\_AA64 is implemented. Otherwise, direct accesses to CTR\_EL0 are UNDEFINED.

## Attributes

CTR\_EL0 is a 64-bit register.

## Field descriptions

<!-- image -->

## Bits [63:38]

Reserved, RES0.

## TminLine, bits [37:32]

## When FEAT\_MTE2 is implemented:

Tag minimum Line. Log2 of the number of words covered by Allocation Tags in the smallest cache line of all caches which can contain Allocation tags that are controlled by the PE.

## Note

- For an implementation with cache lines containing 64 bytes of data and 4 Allocation Tags, this will be log2(64/4) = 4.
- For an implementation with Allocations Tags in separate cache lines of 128 Allocation Tags per line, this will be log2(128*16/4) = 9.

This field has an IMPLEMENTATION DEFINED value.

Access to this field is RO.

## Otherwise:

Reserved, RES0.

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

Note

If CTR\_EL0.DIC is 1, instruction cache maintenance is not required after overwriting instructions, including for different V A aliases of the affected Locations, regardless of the value of CTR\_EL0.L1Ip.

Access to this field is RO.

## IDC, bit [28]

Data cache clean requirements for instruction to data coherence. The meaning of this bit is:

The value of this field is an IMPLEMENTATION DEFINED choice of:

| IDC   | Meaning                                                                                                                                                                               |
|-------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0   | Data cache clean to the Point of Unification is required for instruction to data coherence, unless CLIDR_EL1.LoC == 0b000 or (CLIDR_EL1.LoUIS == 0b000 and CLIDR_EL1.LoUU == 0b000 ). |
| 0b1   | Data cache clean to the Point of Unification is not required for instruction to data coherence.                                                                                       |

If CTR\_EL0.DIC is 1 then the value reported in this field must also be 1.

The Effective value of IDC is 1 if any of the following are true:

- CTR\_EL0.IDC == 1.
- CLIDR\_EL1.LoC == 0b000 .
- CLIDR\_EL1.LoUIS == 0b000 and CLIDR\_EL1.LoUU == 0b000 .

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

From Armv8.0, the value 0b01 is reserved.

Access to this field is RO.

## Bits [13:4]

Reserved, RES0.

## IminLine, bits [3:0]

Log2 of the number of words in the smallest cache line of all the instruction caches that are controlled by the PE.

This field has an IMPLEMENTATION DEFINED value.

Access to this field is RO.

## Accessing CTR\_EL0

Accesses to this register use the following encodings in the System register encoding space:

MRS &lt;Xt&gt;, CTR\_EL0

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b011 | 0b0000 | 0b0000 | 0b001 |

```
if !IsFeatureImplemented(FEAT_AA64) then UnimplementedIDRegister(); elsif PSTATE.EL == EL0 then if !ELIsInHost(EL0) && SCTLR_EL1.UCT == '0' then if EL2Enabled() && HCR_EL2.TGE == '1' then AArch64.SystemAccessTrap(EL2, 0x18); else AArch64.SystemAccessTrap(EL1, 0x18); elsif EL2Enabled() && !ELIsInHost(EL0) && HCR_EL2.TID2 == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && !ELIsInHost(EL0) && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || ↪ → SCR_EL3.FGTEn == '1') && HFGRTR_EL2.CTR_EL0 == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif ELIsInHost(EL0) && SCTLR_EL2.UCT == '0' then AArch64.SystemAccessTrap(EL2, 0x18); else X[t, 64] = CTR_EL0; elsif PSTATE.EL == EL1 then if EL2Enabled() && HCR_EL2.TID2 == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') && ↪ → HFGRTR_EL2.CTR_EL0 == '1' then AArch64.SystemAccessTrap(EL2, 0x18); else X[t, 64] = CTR_EL0; elsif PSTATE.EL == EL2 then X[t, 64] = CTR_EL0; elsif PSTATE.EL == EL3 then X[t, 64] = CTR_EL0;
```