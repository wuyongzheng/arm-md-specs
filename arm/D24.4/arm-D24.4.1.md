## D24.4.1 TRBBASER\_EL1, Trace Buffer Base Address Register

The TRBBASER\_EL1 characteristics are:

## Purpose

Defines the base address for the trace buffer.

## Configuration

When FEAT\_TRBE\_EXT is implemented, AArch64 System register TRBBASER\_EL1 bits [63:0] are architecturally mapped to External register TRBBASER\_EL1[63:0].

This register is present only when FEAT\_TRBE is implemented. Otherwise, direct accesses to TRBBASER\_EL1 are UNDEFINED.

## Attributes

TRBBASER\_EL1 is a 64-bit register.

## Field descriptions

<!-- image -->

## BASE, bits [63:12]

Trace Buffer Base pointer address. (TRBBASER\_EL1.BASE « 12) is the address of the first byte in the trace buffer. Bits [11:0] of the Base pointer address are always zero. If the smallest implemented translation granule is not 4KB, then TRBBASER\_EL1[N-1:12] are RES0, where N is the IMPLEMENTATION DEFINED value Log2(smallest implemented translation granule).

The reset behavior of this field is:

- On a Cold reset, this field resets to an architecturally UNKNOWN value.

## Bits [11:0]

Reserved, RES0.

## Accessing TRBBASER\_EL1

The PE might ignore a write to TRBBASER\_EL1 if any of the following apply:

- TRBLIMITR\_EL1.E == 0b1 , and either FEAT\_TRBE\_EXT is not implemented or the Trace Buffer Unit is using Self-hosted mode.
- TRBLIMITR\_EL1.XE == 0b1 , FEAT\_TRBE\_EXT is implemented, and the Trace Buffer Unit is using External mode.

Accesses to this register use the following encodings in the System register encoding space:

MRS &lt;Xt&gt;, TRBBASER\_EL1

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b000 | 0b1001 | 0b1011 | 0b010 |

```
if !IsFeatureImplemented(FEAT_TRBE) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && CheckMDCR_EL3_NSTBTrap() then UNDEFINED; elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') && ↪ → HDFGRTR_EL2.TRBBASER_EL1 == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && MDCR_EL2.E2TB IN {'x0'} then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && CheckMDCR_EL3_NSTBTrap() then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else X[t, 64] = TRBBASER_EL1; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && CheckMDCR_EL3_NSTBTrap() then UNDEFINED; elsif HaveEL(EL3) && CheckMDCR_EL3_NSTBTrap() then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else X[t, 64] = TRBBASER_EL1; elsif PSTATE.EL == EL3 then if IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA == ↪ → '1' then Halt(DebugHalt_SoftwareAccess); else X[t, 64] = TRBBASER_EL1;
```

MSR TRBBASER\_EL1, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b000 | 0b1001 | 0b1011 | 0b010 |

```
if !IsFeatureImplemented(FEAT_TRBE) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && CheckMDCR_EL3_NSTBTrap() then UNDEFINED;
```

```
elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') && ↪ → HDFGWTR_EL2.TRBBASER_EL1 == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && MDCR_EL2.E2TB IN {'x0'} then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && CheckMDCR_EL3_NSTBTrap() then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else TRBBASER_EL1 = X[t, 64]; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && CheckMDCR_EL3_NSTBTrap() then UNDEFINED; elsif HaveEL(EL3) && CheckMDCR_EL3_NSTBTrap() then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA ↪ → == '1' then Halt(DebugHalt_SoftwareAccess); else TRBBASER_EL1 = X[t, 64]; elsif PSTATE.EL == EL3 then if IsFeatureImplemented(FEAT_TRBE_EXT) && OSLSR_EL1.OSLK == '0' && HaltingAllowed() && EDSCR2.TTA == ↪ → '1' then Halt(DebugHalt_SoftwareAccess); else TRBBASER_EL1 = X[t, 64];
```
