## D24.2.58 HACDBSBR\_EL2, Hardware Accelerator for Cleaning Dirty State Base Register

The HACDBSBR\_EL2 characteristics are:

## Purpose

Control register for HACDBS structure.

## Configuration

This register is present only when FEAT\_HACDBS is implemented and FEAT\_AA64 is implemented. Otherwise, direct accesses to HACDBSBR\_EL2 are UNDEFINED.

## Attributes

HACDBSBR\_EL2 is a 64-bit register.

## Field descriptions

<!-- image -->

## Bits [63:56]

Reserved, RES0.

## BADDR, bits [55:12]

HACDBSbase address, bits [55:12].

- Bits [55:12] of the base address are the value of this field.
- Bits [11:0] of the base address are 0.

Bits of this field above the implemented physical address size, indicated in ID\_AA64MMFR0\_EL1.PARange, are RES0.

Based on the value of the SZ field of this register, for encodings of the SZ field greater than 4KB, bits [(SZ+12-1):12] of this field are RES0 such that the base address of the HACDBS is aligned to its size.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## EN, bit [11]

Enable use of HACDBS.

If SCR\_EL3.HACDBSEn is set to 0, then this field behaves as 0 for all purposes other than a direct read of the value of this bit.

| EN   | Meaning                                                    |
|------|------------------------------------------------------------|
| 0b0  | Hardware accelerator for cleaning Dirty state is disabled. |
| 0b1  | Hardware accelerator for cleaning Dirty state is enabled.  |

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Bits [10:4]

Reserved, RES0.

## SZ, bits [3:0]

Size of the HACDBS.

All other values are reserved.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Accessing HACDBSBR\_EL2

Accesses to this register use the following encodings in the System register encoding space:

MRS &lt;Xt&gt;, HACDBSBR\_EL2

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b100 | 0b0010 | 0b0011 | 0b100 |

```
if !(IsFeatureImplemented(FEAT_HACDBS) && IsFeatureImplemented(FEAT_AA64)) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EffectiveHCR_EL2_NVx() IN {'1x1'} then X[t, 64] = NVMem[0x2F0]; elsif EffectiveHCR_EL2_NVx() IN {'xx1'} then AArch64.SystemAccessTrap(EL2, 0x18); else UNDEFINED; elsif PSTATE.EL == EL2 then
```

| SZ     | Meaning   |
|--------|-----------|
| 0b0000 | 4KB       |
| 0b0001 | 8KB       |
| 0b0010 | 16KB      |
| 0b0011 | 32KB      |
| 0b0100 | 64KB      |
| 0b0101 | 128KB     |
| 0b0110 | 256KB     |
| 0b0111 | 512KB     |
| 0b1000 | 1MB       |
| 0b1001 | 2MB       |

```
if HaveEL(EL3) && EL3SDDUndefPriority() && SCR_EL3.HACDBSEn == '0' then UNDEFINED; elsif HaveEL(EL3) && SCR_EL3.HACDBSEn == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = HACDBSBR_EL2; elsif PSTATE.EL == EL3 then X[t, 64] = HACDBSBR_EL2;
```

MSR HACDBSBR\_EL2, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b100 | 0b0010 | 0b0011 | 0b100 |

```
if !(IsFeatureImplemented(FEAT_HACDBS) && IsFeatureImplemented(FEAT_AA64)) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EffectiveHCR_EL2_NVx() IN {'1x1'} then NVMem[0x2F0] = X[t, 64]; elsif EffectiveHCR_EL2_NVx() IN {'xx1'} then AArch64.SystemAccessTrap(EL2, 0x18); else UNDEFINED; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && SCR_EL3.HACDBSEn == '0' then UNDEFINED; elsif HaveEL(EL3) && SCR_EL3.HACDBSEn == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else HACDBSBR_EL2 = X[t, 64]; elsif PSTATE.EL == EL3 then HACDBSBR_EL2 = X[t, 64];
```