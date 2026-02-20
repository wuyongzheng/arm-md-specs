## G8.2.94 ID\_MMFR1, Memory Model Feature Register 1

The ID\_MMFR1 characteristics are:

## Purpose

Provides information about the implemented memory model and memory management support in AArch32 state.

For general information about the interpretation of the ID registers see 'Principles of the ID scheme for fields in ID registers'.

## Configuration

AArch32 System register ID\_MMFR1 bits [31:0] are architecturally mapped to AArch64 System register ID\_MMFR1\_EL1[31:0].

This register is present only when FEAT\_AA32EL1 is implemented. Otherwise, direct accesses to ID\_MMFR1 are UNDEFINED.

## Attributes

ID\_MMFR1 is a 32-bit register.

## Field descriptions

| 31    | 28 27    | 24 23   | 20 19   | 16 15   | 12 11   | 8 7     | 4 3   | 0       |
|-------|----------|---------|---------|---------|---------|---------|-------|---------|
| BPred | L1TstCln | L1Uni   | L1Hvd   | L1UniSW | L1HvdSW | L1UniVA |       | L1HvdVA |

## BPred, bits [31:28]

Branch Predictor. Indicates branch predictor management requirements.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| BPred   | Meaning                                                                                                                                                                                                                                                                                                                                             |
|---------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0000  | No branch predictor, or no MMUpresent. Implies a fixed MPUconfiguration.                                                                                                                                                                                                                                                                            |
| 0b0001  | Branch predictor requires flushing on: • Enabling or disabling a stage of address translation. • Writing new data to instruction locations. • Writing new mappings to the translation tables. • Changes to the TTBR0, TTBR1, or TTBCR registers. • Changes to the ContextID or ASID, or to the FCSE ProcessID if this is supported.                 |
| 0b0010  | Branch predictor requires flushing on: • Enabling or disabling a stage of address translation. • Writing new data to instruction locations. • Writing new mappings to the translation tables. • Any change to the TTBR0, TTBR1, or TTBCR registers without a change to the corresponding ContextID or ASID, or FCSE ProcessID if this is supported. |
| 0b0011  | Branch predictor requires flushing only on writing new data to instruction locations.                                                                                                                                                                                                                                                               |
| 0b0100  | For execution correctness, branch predictor requires no flushing at any time.                                                                                                                                                                                                                                                                       |

All other values are reserved.

In Armv8-A, the permitted values are 0b0010 , 0b0011 , or 0b0100 . For values other than 0b0000 and 0b0100 , the Arm Architecture Reference Manual, or the product documentation, might give more information about the required maintenance.

Access to this field is RO.

## L1TstCln, bits [27:24]

Level 1 cache Test and Clean. Indicates the supported Level 1 data cache test and clean operations, for Harvard or unified cache implementations.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| L1TstCln   | Meaning                                                                                          |
|------------|--------------------------------------------------------------------------------------------------|
| 0b0000     | None supported.                                                                                  |
| 0b0001     | Supported Level 1 data cache test and clean operations are:                                      |
| 0b0010     | • Test and clean data cache. As for 0b0001 , and adds: • Test, clean, and invalidate data cache. |

All other values are reserved.

In Armv8-A, the only permitted value is 0b0000 .

Access to this field is RO.

## L1Uni, bits [23:20]

Level 1 Unified cache. Indicates the supported entire Level 1 cache maintenance operations for a unified cache implementation.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| L1Uni   | Meaning                                                                                                                                                                                            |
|---------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0000  | None supported.                                                                                                                                                                                    |
| 0b0001  | Supported entire Level 1 cache operations are: • Invalidate cache, including branch predictor if appropriate. • Invalidate branch predictor, if appropriate.                                       |
| 0b0010  | As for 0b0001 , and adds: • Clean cache, using a recursive model that uses the cache dirty status bit. • Clean and invalidate cache, using a recursive model that uses the cache dirty status bit. |

All other values are reserved.

In Armv8-A, the only permitted value is 0b0000 .

Access to this field is RO.

## L1Hvd, bits [19:16]

Level 1 Harvard cache. Indicates the supported entire Level 1 cache maintenance operations for a Harvard cache implementation.

## The value of this field is an IMPLEMENTATION DEFINED choice of:

| L1Hvd   | Meaning                                                                                                                                                                                                      |
|---------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0000  | None supported.                                                                                                                                                                                              |
| 0b0001  | Supported entire Level 1 cache operations are: • Invalidate instruction cache, including branch predictor if appropriate. • Invalidate branch predictor, if appropriate.                                     |
| 0b0010  | As for 0b0001 , and adds: • Invalidate data cache. • Invalidate data cache and instruction cache, including branch predictor if appropriate.                                                                 |
| 0b0011  | As for 0b0010 , and adds: • Clean data cache, using a recursive model that uses the cache dirty status bit. • Clean and invalidate data cache, using a recursive model that uses the cache dirty status bit. |

All other values are reserved.

In Armv8-A, the only permitted value is 0b0000 .

Access to this field is RO.

## L1UniSW, bits [15:12]

Level 1 Unified cache by Set/Way. Indicates the supported Level 1 cache line maintenance operations by set/way, for a unified cache implementation.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| L1UniSW   | Meaning                                                                                                    |
|-----------|------------------------------------------------------------------------------------------------------------|
| 0b0000    | None supported.                                                                                            |
| 0b0001    | Supported Level 1 unified cache line maintenance operations by set/way are: • Clean cache line by set/way. |
| 0b0010    | As for 0b0001 , and adds: • Clean and invalidate cache line by set/way.                                    |
| 0b0011    | As for 0b0010 , and adds: • Invalidate cache line by set/way.                                              |

All other values are reserved.

In Armv8-A, the only permitted value is 0b0000 .

Access to this field is RO.

## L1HvdSW, bits [11:8]

Level 1 Harvard cache by Set/Way. Indicates the supported Level 1 cache line maintenance operations by set/way, for a Harvard cache implementation.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| L1HvdSW   | Meaning                                                                                                                                                            |
|-----------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0000    | None supported.                                                                                                                                                    |
| 0b0001    | Supported Level 1 Harvard cache line maintenance operations by set/way are: • Clean data cache line by set/way. • Clean and invalidate data cache line by set/way. |
| 0b0010    | As for 0b0001 , and adds: • Invalidate data cache line by set/way.                                                                                                 |
| 0b0011    | As for 0b0010 , and adds: • Invalidate instruction cache line by set/way.                                                                                          |

All other values are reserved.

In Armv8-A, the only permitted value is 0b0000 .

Access to this field is RO.

## L1UniVA, bits [7:4]

Level 1 Unified cache by Virtual Address. Indicates the supported Level 1 cache line maintenance operations by VA, for a unified cache implementation.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| L1UniVA   | Meaning                                                                                                                                                                  |
|-----------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0000    | None supported.                                                                                                                                                          |
| 0b0001    | Supported Level 1 unified cache line maintenance operations by VA are: • Clean cache line by VA. • Invalidate cache line by VA. • Clean and invalidate cache line by VA. |
| 0b0010    | As for 0b0001 , and adds: • Invalidate branch predictor by VA, if branch predictor is implemented.                                                                       |

All other values are reserved.

In Armv8-A, the only permitted value is 0b0000 .

Access to this field is RO.

## L1HvdVA, bits [3:0]

Level 1 Harvard cache by Virtual Address. Indicates the supported Level 1 cache line maintenance operations by VA, for a Harvard cache implementation.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| L1HvdVA   | Meaning                                                                                                                                                                                                                       |
|-----------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0000    | None supported.                                                                                                                                                                                                               |
| 0b0001    | Supported Level 1 Harvard cache line maintenance operations by VA are: • Clean data cache line by VA. • Invalidate data cache line by VA. • Clean and invalidate data cache line by VA. • Clean instruction cache line by VA. |
| 0b0010    | As for 0b0001 , and adds: • Invalidate branch predictor by VA, if branch predictor is implemented.                                                                                                                            |

All other values are reserved.

In Armv8-A, the only permitted value is 0b0000 .

Access to this field is RO.

## Accessing ID\_MMFR1

Accesses to this register use the following encodings in the System register encoding space:

```
MRC{<c>}{<q>} <coproc>, {#}<opc1>, <Rt>, <CRn>, <CRm>{, {#}<opc2>}
```

| coproc   | opc1   | CRn    | CRm    | opc2   |
|----------|--------|--------|--------|--------|
| 0b1111   | 0b000  | 0b0000 | 0b0001 | 0b101  |

```
if !IsFeatureImplemented(FEAT_AA32EL1) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && HSTR_EL2.T0 == '1' ↪ → then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HSTR.T0 == '1' ↪ → then AArch32.TakeHypTrapException(0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && HCR_EL2.TID3 == ↪ → '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HCR.TID3 == '1' ↪ → then AArch32.TakeHypTrapException(0x03); else R[t] = ID_MMFR1; elsif PSTATE.EL == EL2 then R[t] = ID_MMFR1; elsif PSTATE.EL == EL3 then R[t] = ID_MMFR1;
```