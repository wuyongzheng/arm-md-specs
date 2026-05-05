## D24.4.37 TRCIDR2, Trace ID Register 2

The TRCIDR2 characteristics are:

## Purpose

Returns the tracing capabilities of the trace unit.

## Configuration

AArch64 System register TRCIDR2 bits [31:0] are architecturally mapped to External register TRCIDR2[31:0].

This register is present only when FEAT\_ETE is implemented and System register access to the trace unit registers is implemented. Otherwise, direct accesses to TRCIDR2 are UNDEFINED.

## Attributes

TRCIDR2 is a 64-bit register.

## Field descriptions

<!-- image -->

## Bits [63:32]

Reserved, RES0.

## WFXMODE,bit [31]

Indicates whether WFI , WFIT , WFE , and WFET instructions are classified as P0 instructions:

The value of this field is an IMPLEMENTATION DEFINED choice of:

| WFXMODE   | Meaning                                                                         |
|-----------|---------------------------------------------------------------------------------|
| 0b0       | WFI , WFIT , WFE , and WFET instructions are not classified as P0 instructions. |
| 0b1       | WFI , WFIT , WFE , and WFET instructions are classified as P0 instructions.     |

Access to this field is RO.

## VMIDOPT, bits [30:29]

Indicates the options for Virtual context identifier selection.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| VMIDOPT   | Meaning                                                                            |
|-----------|------------------------------------------------------------------------------------|
| 0b00      | Virtual context identifier selection not supported. TRCCONFIGR.VMIDOPT is RES0.    |
| 0b01      | Virtual context identifier selection supported. TRCCONFIGR.VMIDOPT is implemented. |
| 0b10      | Virtual context identifier selection not supported. TRCCONFIGR.VMIDOPT is RES1.    |

All other values are reserved.

If TRCIDR2.VMIDSIZE == 0b00000 then this field is 0b00 .

If TRCIDR2.VMIDSIZE != 0b00000 then this field is 0b10 .

Access to this field is RO.

## CCSIZE, bits [28:25]

## When TRCIDR0.TRCCCI == '1':

Indicates the size of the cycle counter.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| CCSIZE   | Meaning                                 |
|----------|-----------------------------------------|
| 0b0000   | The cycle counter is 12 bits in length. |
| 0b0001   | The cycle counter is 13 bits in length. |
| 0b0010   | The cycle counter is 14 bits in length. |
| 0b0011   | The cycle counter is 15 bits in length. |
| 0b0100   | The cycle counter is 16 bits in length. |
| 0b0101   | The cycle counter is 17 bits in length. |
| 0b0110   | The cycle counter is 18 bits in length. |
| 0b0111   | The cycle counter is 19 bits in length. |
| 0b1000   | The cycle counter is 20 bits in length. |

All other values are reserved.

Access to this field is RO.

## Otherwise:

Reserved, RES0.

## DVSIZE, bits [24:20]

## When TRCIDR0.TRCDATA != '00':

Indicates the data value size in bytes. Data tracing is not implemented in ETE and this field is reserved for other trace architectures. Allocated in other trace architectures.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| DVSIZE   | Meaning                                                 |
|----------|---------------------------------------------------------|
| 0b00000  | Data value tracing not implemented.                     |
| 0b00100  | Data value tracing has a maximum of 32-bit data values. |
| 0b01000  | Data value tracing has a maximum of 64-bit data values. |

All other values are reserved.

Access to this field is RO.

## Otherwise:

Reserved, RES0.

DASIZE, bits [19:15]

## When TRCIDR0.TRCDATA != '00':

Indicates the data address size in bytes. Data tracing is not implemented in ETE and this field is reserved for other trace architectures. Allocated in other trace architectures.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| DASIZE   | Meaning                                                      |
|----------|--------------------------------------------------------------|
| 0b00000  | Data address tracing not implemented.                        |
| 0b00100  | Data address tracing has a maximum of 32-bit data addresses. |
| 0b01000  | Data address tracing has a maximum of 64-bit data addresses. |

All other values are reserved.

Access to this field is RO.

## Otherwise:

Reserved, RES0.

## VMIDSIZE, bits [14:10]

Indicates the trace unit Virtual context identifier size.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| VMIDSIZE   | Meaning                                              |
|------------|------------------------------------------------------|
| 0b00000    | Virtual context identifier tracing is not supported. |
| 0b00001    | 8-bit Virtual context identifier size.               |
| 0b00010    | 16-bit Virtual context identifier size.              |
| 0b00100    | 32-bit Virtual context identifier size.              |

All other values are reserved.

If the PE does not implement EL2 then this field is 0b00000 .

If the PE implements EL2 then this field is 0b00100 .

Access to this field is RO.

## CIDSIZE, bits [9:5]

Indicates the Context identifier size.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| CIDSIZE   | Meaning                                      |
|-----------|----------------------------------------------|
| 0b00000   | Context identifier tracing is not supported. |
| 0b00100   | 32-bit Context identifier size.              |

All other values are reserved.

This field reads as 0b00100 .

Access to this field is RO.

## IASIZE, bits [4:0]

Virtual instruction address size.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| IASIZE   | Meaning                                     |
|----------|---------------------------------------------|
| 0b00100  | Maximum of 32-bit instruction address size. |
| 0b01000  | Maximum of 64-bit instruction address size. |

All other values are reserved.

This field reads as 0b01000 .

Access to this field is RO.

## Accessing TRCIDR2

Accesses to this register use the following encodings in the System register encoding space:

MRS &lt;Xt&gt;, TRCIDR2

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b10  | 0b001 | 0b0000 | 0b1010 | 0b111 |

```
if !(IsFeatureImplemented(FEAT_ETE) && IsFeatureImplemented(FEAT_TRC_SR)) UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && CPTR_EL3.TTA == '1' then UNDEFINED; elsif CPACR_EL1.TTA == '1' then
```

then

```
AArch64.SystemAccessTrap(EL1, 0x18); elsif EL2Enabled() && CPTR_EL2.TTA == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') && ↪ → HDFGRTR_EL2.TRCID == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && CPTR_EL3.TTA == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else X[t, 64] = TRCIDR2; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && CPTR_EL3.TTA == '1' then UNDEFINED; elsif CPTR_EL2.TTA == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && CPTR_EL3.TTA == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else X[t, 64] = TRCIDR2; elsif PSTATE.EL == EL3 then if CPTR_EL3.TTA == '1' then AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else X[t, 64] = TRCIDR2;
```
