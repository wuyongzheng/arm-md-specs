## G8.2.96 ID\_MMFR3, Memory Model Feature Register 3

The ID\_MMFR3 characteristics are:

## Purpose

Provides information about the implemented memory model and memory management support in AArch32 state.

For general information about the interpretation of the ID registers see 'Principles of the ID scheme for fields in ID registers'.

## Configuration

AArch32 System register ID\_MMFR3 bits [31:0] are architecturally mapped to AArch64 System register ID\_MMFR3\_EL1[31:0].

This register is present only when FEAT\_AA32EL1 is implemented. Otherwise, direct accesses to ID\_MMFR3 are UNDEFINED.

## Attributes

ID\_MMFR3 is a 32-bit register.

## Field descriptions

| 31       | 28 27   | 24 23   | 20 19   | 16 15     | 12 11   | 8 7      | 4 3   | 0        |
|----------|---------|---------|---------|-----------|---------|----------|-------|----------|
| Supersec | CMemSz  | CohWalk | PAN     | MaintBcst | BPMaint | CMaintSW |       | CMaintVA |

## Supersec, bits [31:28]

Supersections. On a VMSA implementation, indicates whether Supersections are supported.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| Supersec   | Meaning                      |
|------------|------------------------------|
| 0b0000     | Supersections supported.     |
| 0b1111     | Supersections not supported. |

All other values are reserved.

In Armv8-A, the permitted values are 0b0000 and 0b1111 .

Access to this field is RO.

## CMemSz, bits [27:24]

Cached Memory Size. Indicates the physical memory size supported by the caches.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| CMemSz   | Meaning                                                                  |
|----------|--------------------------------------------------------------------------|
| 0b0000   | 4GB, corresponding to a 32-bit physical address range.                   |
| 0b0001   | 64GB, corresponding to a 36-bit physical address range.                  |
| 0b0010   | 1TB or more, corresponding to a 40-bit or larger physical address range. |

All other values are reserved.

In Armv8-A, the permitted values are 0b0000 , 0b0001 , and 0b0010 .

Access to this field is RO.

## CohWalk, bits [23:20]

Coherent Walk. Indicates whether Translation table updates require a clean to the Point of Unification.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| CohWalk   | Meaning                                                                                                                                          |
|-----------|--------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0000    | Updates to the translation tables require a clean to the Point of Unification to ensure visibility by subsequent translation table walks.        |
| 0b0001    | Updates to the translation tables do not require a clean to the Point of Unification to ensure visibility by subsequent translation table walks. |

All other values are reserved.

In Armv8-A, the only permitted value is 0b0001 .

Access to this field is RO.

## PAN, bits [19:16]

Privileged Access Never. Indicates support for the PAN bit in CPSR, SPSR, and DSPSR in AArch32 state.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| PAN    | Meaning                                                         |
|--------|-----------------------------------------------------------------|
| 0b0000 | PAN not supported.                                              |
| 0b0001 | PAN supported.                                                  |
| 0b0010 | PAN supported and ATS1CPRP and ATS1CPWP instructions supported. |

All other values are reserved.

FEAT\_PAN implements the functionality identified by the value 0b0001 .

FEAT\_PAN2 implements the functionality added by the value 0b0010 .

From Armv8.1, the value 0b0000 is not permitted.

From Armv8.2, the value 0b0001 is not permitted.

Access to this field is RO.

## MaintBcst, bits [15:12]

Maintenance Broadcast. Indicates whether Cache, TLB, and branch predictor operations are broadcast.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| MaintBcst   | Meaning                                                                                                                                                              |
|-------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0000      | Cache, TLB, and branch predictor operations only affect local structures.                                                                                            |
| 0b0001      | Cache and branch predictor operations affect structures according to shareability and defined behavior of instructions. TLB operations only affect local structures. |
| 0b0010      | Cache, TLB, and branch predictor operations affect structures according to shareability and defined behavior of instructions.                                        |

All other values are reserved.

In Armv8-A, the only permitted value is 0b0010 .

Access to this field is RO.

## BPMaint, bits [11:8]

Branch Predictor Maintenance. Indicates the supported branch predictor maintenance operations in an implementation with hierarchical cache maintenance operations.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| BPMaint   | Meaning                                                                                    |
|-----------|--------------------------------------------------------------------------------------------|
| 0b0000    | None supported.                                                                            |
| 0b0001    | Supported branch predictor maintenance operations are: • Invalidate all branch predictors. |
| 0b0010    | As for 0b0001 , and adds: • Invalidate branch predictors by VA.                            |

All other values are reserved.

In Armv8-A, the only permitted value is 0b0010 .

Access to this field is RO.

## CMaintSW, bits [7:4]

Cache Maintenance by Set/Way. Indicates the supported cache maintenance operations by set/way, in an implementation with hierarchical caches.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| CMaintSW   | Meaning                                                               |
|------------|-----------------------------------------------------------------------|
| 0b0000     | None supported.                                                       |
| 0b0001     | Supported hierarchical cache maintenance instructions by set/way are: |

All other values are reserved.

In Armv8-A, the only permitted value is 0b0001 .

In a unified cache implementation, the data cache maintenance operations apply to the unified caches.

Access to this field is RO.

## CMaintVA, bits [3:0]

Cache Maintenance by Virtual Address. Indicates the supported cache maintenance operations by V A, in an implementation with hierarchical caches.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| CMaintVA   | Meaning                                                                                                                                                                             |
|------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0000     | None supported.                                                                                                                                                                     |
| 0b0001     | Supported hierarchical cache maintenance operations by VA are:                                                                                                                      |
|            | • Invalidate data cache by VA. • Clean data cache by VA. • Clean and invalidate data cache by VA. • Invalidate instruction cache by VA. • Invalidate all instruction cache entries. |

All other values are reserved.

In Armv8-A, the only permitted value is 0b0001 .

In a unified cache implementation, data cache maintenance operations apply to the unified caches, and the instruction cache maintenance instructions are not implemented.

Access to this field is RO.

## Accessing ID\_MMFR3

Accesses to this register use the following encodings in the System register encoding space:

MRC{&lt;c&gt;}{&lt;q&gt;} &lt;coproc&gt;, {#}&lt;opc1&gt;, &lt;Rt&gt;, &lt;CRn&gt;, &lt;CRm&gt;{, {#}&lt;opc2&gt;}

| coproc   | opc1   | CRn    | CRm    | opc2   |
|----------|--------|--------|--------|--------|
| 0b1111   | 0b000  | 0b0000 | 0b0001 | 0b111  |

```
if !IsFeatureImplemented(FEAT_AA32EL1) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && HSTR_EL2.T0 == '1' ↪ → then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HSTR.T0 == '1' ↪ → then AArch32.TakeHypTrapException(0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && HCR_EL2.TID3 == ↪ → '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HCR.TID3 == '1' ↪ → then AArch32.TakeHypTrapException(0x03); else R[t] = ID_MMFR3; elsif PSTATE.EL == EL2 then R[t] = ID_MMFR3; elsif PSTATE.EL == EL3 then R[t] = ID_MMFR3;
```