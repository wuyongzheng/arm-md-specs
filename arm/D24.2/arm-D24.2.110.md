## D24.2.110 ID\_MMFR2\_EL1, AArch32 Memory Model Feature Register 2

The ID\_MMFR2\_EL1 characteristics are:

## Purpose

Provides information about the implemented memory model and memory management support in AArch32 state.

For general information about the interpretation of the ID registers see 'Principles of the ID scheme for fields in ID registers'.

## Configuration

AArch64 System register ID\_MMFR2\_EL1 bits [31:0] are architecturally mapped to AArch32 System register ID\_MMFR2[31:0].

This register is present only when FEAT\_AA64 is implemented. Otherwise, direct accesses to ID\_MMFR2\_EL1 are UNDEFINED.

## Attributes

ID\_MMFR2\_EL1 is a 64-bit register.

## Field descriptions

When FEAT\_AA32 is implemented:

<!-- image -->

| 63   |          |          |         |        |        |          |     |         | 32      |
|------|----------|----------|---------|--------|--------|----------|-----|---------|---------|
|      |          |          |         | RES0   |        |          |     |         |         |
| 31   | 28 27    | 24 23    |         | 16     | 15     | 11       | 8 7 |         | 0       |
|      | HWAccFlg | WFIStall | MemBarr | UniTLB | HvdTLB | L1HvdRng |     | L1HvdBG | L1HvdFG |

## Bits [63:32]

Reserved, RES0.

## HWAccFlg, bits [31:28]

Hardware Access Flag. In earlier versions of the Arm Architecture, this field indicates support for a Hardware Access flag, as part of the VMSAv7 implementation.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| HWAccFlg   | Meaning                                              |
|------------|------------------------------------------------------|
| 0b0000     | Not supported.                                       |
| 0b0001     | Support for VMSAv7 Access flag, updated in hardware. |

All other values are reserved.

From Armv8.0, 0b0001 is not permitted.

Access to this field is RO.

## WFIStall, bits [27:24]

Wait For Interrupt Stall. Indicates the support for Wait For Interrupt (WFI) stalling.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| WFIStall   | Meaning                   |
|------------|---------------------------|
| 0b0000     | Not supported.            |
| 0b0001     | Support for WFI stalling. |

All other values are reserved.

Access to this field is RO.

## MemBarr, bits [23:20]

Memory Barrier. Indicates the supported memory barrier System instructions in the (coproc== 0b1111 ) encoding space:

The value of this field is an IMPLEMENTATION DEFINED choice of:

| MemBarr   | Meaning                                                                                             |
|-----------|-----------------------------------------------------------------------------------------------------|
| 0b0000    | None supported.                                                                                     |
| 0b0001    | Supported memory barrier System instructions are: • Data Synchronization Barrier (DSB).             |
| 0b0010    | As for 0b0001 , and adds: • Instruction Synchronization Barrier (ISB). • Data Memory Barrier (DMB). |

All other values are reserved.

From Armv8.0, the values 0b000 and 0b0001 are not permitted.

Arm deprecates the use of these operations. ID\_ISAR4.Barrier\_instrs indicates the level of support for the preferred barrier instructions.

Access to this field is RO.

## UniTLB, bits [19:16]

Unified TLB. Indicates the supported TLB maintenance operations, for a unified TLB implementation.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| UniTLB   | Meaning        |
|----------|----------------|
| 0b0000   | Not supported. |

| UniTLB   | Meaning                                                                                                                                                              |
|----------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0001   | Supported unified TLB maintenance operations are: • Invalidate all entries in the TLB. • Invalidate TLB entry by VA.                                                 |
| 0b0010   | As for 0b0001 , and adds: • Invalidate TLB entries by ASID match.                                                                                                    |
| 0b0011   | As for 0b0010 , and adds: • Invalidate instruction TLB and data TLB entries by VA All ASID. This is a shared unified TLB operation.                                  |
| 0b0100   | As for 0b0011 , and adds: • Invalidate Hyp mode unified TLB entry by VA. • Invalidate entire Non-secure PL1&0 unified TLB. • Invalidate entire Hyp mode unified TLB. |
| 0b0101   | As for 0b0100 , and adds the following operations: TLBIMVALIS, TLBIMVAALIS, TLBIMVALHIS, TLBIMVAL, TLBIMVAAL, TLBIMVALH.                                             |
| 0b0110   | As for 0b0101 , and adds the following operations: TLBIIPAS2IS, TLBIIPAS2LIS, TLBIIPAS2, TLBIIPAS2L.                                                                 |

All other values are reserved.

In Armv8-A, the only permitted value is 0b0110 .

Access to this field is RO.

## HvdTLB, bits [15:12]

If the Unified TLB field (UniTLB, bits [19:16]) is not 0000, then the meaning of this field is IMPLEMENTATION DEFINED. Arm deprecates the use of this field by software.

This field has an IMPLEMENTATION DEFINED value.

Access to this field is RO.

## L1HvdRng, bits [11:8]

Level 1 Harvard cache Range. Indicates the supported Level 1 cache maintenance range operations, for a Harvard cache implementation.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| L1HvdRng   | Meaning                                                                                                                                                         |
|------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0000     | Not supported.                                                                                                                                                  |
| 0b0001     | Supported Level 1 Harvard cache maintenance range operations are:                                                                                               |
|            | • Invalidate data cache range by VA. • Invalidate instruction cache range by VA. • Clean data cache range by VA. • Clean and invalidate data cache range by VA. |

All other values are reserved.

From Armv8.0, the value 0b0001 is not permitted.

Access to this field is RO.

## L1HvdBG, bits [7:4]

Level 1 Harvard cache Background fetch. Indicates the supported Level 1 cache background fetch operations, for a Harvard cache implementation. When supported, background fetch operations are non-blocking operations.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| L1HvdBG   | Meaning                                                                |
|-----------|------------------------------------------------------------------------|
| 0b0000    | Not supported.                                                         |
| 0b0001    | Supported Level 1 Harvard cache background fetch operations are:       |
|           | • Fetch instruction cache range by VA. • Fetch data cache range by VA. |

All other values are reserved.

From Armv8.0, the value 0b0001 is not permitted.

Access to this field is RO.

## L1HvdFG, bits [3:0]

Level 1 Harvard cache Foreground fetch. Indicates the supported Level 1 cache foreground fetch operations, for a Harvard cache implementation. When supported, foreground fetch operations are blocking operations.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| L1HvdFG   | Meaning                                                                |
|-----------|------------------------------------------------------------------------|
| 0b0000    | Not supported.                                                         |
| 0b0001    | Supported Level 1 Harvard cache foreground fetch operations are:       |
|           | • Fetch instruction cache range by VA. • Fetch data cache range by VA. |

All other values are reserved.

From Armv8.0, the value 0b0001 is not permitted.

Access to this field is RO.

## Otherwise:

<!-- image -->

| 63      | 32   |
|---------|------|
| UNKNOWN | 0    |
| 31      |      |

## Bits [63:0]

Reserved, UNKNOWN.

## Accessing ID\_MMFR2\_EL1

Accesses to this register use the following encodings in the System register encoding space:

```
MRS <Xt>, ID_MMFR2_EL1
```

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b000 | 0b0000 | 0b0001 | 0b110 |

```
if !IsFeatureImplemented(FEAT_AA64) then UnimplementedIDRegister(); elsif PSTATE.EL == EL0 then if IsFeatureImplemented(FEAT_IDST) then if EL2Enabled() && HCR_EL2.TGE == '1' then AArch64.SystemAccessTrap(EL2, 0x18); else AArch64.SystemAccessTrap(EL1, 0x18); else UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_IDTE3) && SCR_EL3.TID3 == '1' ↪ → then UNDEFINED; elsif EL2Enabled() && HCR_EL2.TID3 == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_IDTE3) && SCR_EL3.TID3 == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = ID_MMFR2_EL1; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_IDTE3) && SCR_EL3.TID3 == '1' ↪ → then UNDEFINED; elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_IDTE3) && SCR_EL3.TID3 == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = ID_MMFR2_EL1; elsif PSTATE.EL == EL3 then X[t, 64] = ID_MMFR2_EL1;
```