## G8.2.56 FPSID, Floating-Point System ID register

The FPSID characteristics are:

## Purpose

Provides top-level information about the floating-point implementation.

This register largely duplicates information held in the MIDR. Arm deprecates use of it.

## Configuration

Implemented only if the implementation includes the Advanced SIMD and floating-point functionality.

This register is present only when FEAT\_AA32EL1 is implemented. Otherwise, direct accesses to FPSID are UNDEFINED.

## Attributes

FPSID is a 32-bit register.

## Field descriptions

<!-- image -->

| 31          | 24 23 22   | 24 23 22        | 16 15   | 8 7     | 4 3      |
|-------------|------------|-----------------|---------|---------|----------|
| Implementer | SW         | Subarchitecture | PartNum | Variant | Revision |

## Implementer, bits [31:24]

Implementer codes are the same as those used for the MIDR.

For an implementation by Arm this field is 0x41 , the ASCII code for A.

This field has an IMPLEMENTATION DEFINED value.

Access to this field is RO.

## SW, bit [23]

Software bit.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| SW   | Meaning                                                                                   |
|------|-------------------------------------------------------------------------------------------|
| 0b0  | The implementation provides a hardware implementation of the floating-point instructions. |
| 0b1  | The implementation supports only software emulation of the floating-point instructions.   |

In Armv8-A, the only permitted value is 0b0 .

Access to this field is RO.

## Subarchitecture, bits [22:16]

Subarchitecture version number.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| Subarchitecture   | Meaning                                                                                                                                                                                                                                                                                                                                         |
|-------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0000000         | VFPv1 architecture with an IMPLEMENTATION DEFINED subarchitecture.                                                                                                                                                                                                                                                                              |
| 0b0000001         | VFPv2 architecture with Common VFP subarchitecture v1.                                                                                                                                                                                                                                                                                          |
| 0b0000010         | VFPv3 architecture, or later, with Common VFP subarchitecture v2. The VFP architecture version is indicated by the MVFR0and MVFR1registers.                                                                                                                                                                                                     |
| 0b0000011         | VFPv3 architecture, or later, with Null subarchitecture. The entire floating-point implementation is in hardware, and no software support code is required. The VFP architecture version is indicated by the MVFR0and MVFR1registers. This value can be used only by an implementation that does not support the trap enable bits in the FPSCR. |
| 0b0000100         | VFPv3 architecture, or later, with Common VFP subarchitecture v3, and support for trap enable bits in FPSCR. The VFP architecture version is indicated by theMVFR0andMVFR1 registers.                                                                                                                                                           |

For a subarchitecture designed by Arm the most significant bit of this field, register bit[22], is 0. Values with a most significant bit of 0 that are not listed here are reserved.

When the subarchitecture designer is not Arm, the most significant bit of this field, register bit[22], must be 1. Each implementer must maintain its own list of subarchitectures it has designed, starting at subarchitecture version number 0x40 .

In Armv8-A, the permitted values are 0b0000011 and 0b0000100 .

Access to this field is RO.

## PartNum, bits [15:8]

Part Number for the floating-point implementation, assigned by the implementer.

This field has an IMPLEMENTATION DEFINED value.

Access to this field is RO.

## Variant, bits [7:4]

Variant number. Typically, this field distinguishes between different production variants of a single product.

This field has an IMPLEMENTATION DEFINED value.

Access to this field is RO.

## Revision, bits [3:0]

Revision number for the floating-point implementation.

This field has an IMPLEMENTATION DEFINED value.

Access to this field is RO.

## Accessing FPSID

Accesses to this register use the following encodings in the System register encoding space:

VMRS{&lt;c&gt;}{&lt;q&gt;} &lt;Rt&gt;, &lt;spec\_reg&gt;

reg

0b0000

```
if !IsFeatureImplemented(FEAT_AA32EL1) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA64EL3) && ↪ → !ELUsingAArch32(EL3) && CPTR_EL3.TFP == '1' then UNDEFINED; elsif (IsFeatureImplemented(FEAT_AA32EL3) && ELUsingAArch32(EL3) && SCR.NS == '1' && NSACR.cp10 == ↪ → '0') || CPACR.cp10 == '00' then UNDEFINED; elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && !ELIsInHost(EL2) ↪ → && CPTR_EL2.TFP == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x07); elsif ELIsInHost(EL2) && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && CPTR_EL2.FPEN ↪ → IN {'x0'} then AArch64.AArch32SystemAccessTrap(EL2, 0x07); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && ↪ → ((IsFeatureImplemented(FEAT_AA32EL3) && ELUsingAArch32(EL3) && SCR.NS == '1' && NSACR.cp10 == ↪ → '0') || HCPTR.TCP10 == '1') then AArch32.TakeHypTrapException(0x08); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && HCR_EL2.TID0 == ↪ → '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x08); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HCR.TID0 == '1' ↪ → then AArch32.TakeHypTrapException(0x08); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && CPTR_EL3.TFP == ↪ → '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.AArch32SystemAccessTrap(EL3, 0x07); else R[t] = FPSID; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA64EL3) && ↪ → !ELUsingAArch32(EL3) && CPTR_EL3.TFP == '1' then UNDEFINED; elsif EL2Enabled() && ((IsFeatureImplemented(FEAT_AA32EL3) && ELUsingAArch32(EL3) && SCR.NS == '1' ↪ → && NSACR.cp10 == '0') || HCPTR.TCP10 == '1') then AArch32.TakeHypTrapException(0x00); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && CPTR_EL3.TFP == ↪ → '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.AArch32SystemAccessTrap(EL3, 0x07); else R[t] = FPSID; elsif PSTATE.EL == EL3 then if CPACR.cp10 == '00' then UNDEFINED; else R[t] = FPSID;
```

VMSR{&lt;c&gt;}{&lt;q&gt;} &lt;spec\_reg&gt;, &lt;Rt&gt;

reg

0b0000

```
if !IsFeatureImplemented(FEAT_AA32EL1) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA64EL3) && ↪ → !ELUsingAArch32(EL3) && CPTR_EL3.TFP == '1' then UNDEFINED; elsif (IsFeatureImplemented(FEAT_AA32EL3) && ELUsingAArch32(EL3) && SCR.NS == '1' && NSACR.cp10 == ↪ → '0') || CPACR.cp10 == '00' then UNDEFINED; elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && !ELIsInHost(EL2) ↪ → && CPTR_EL2.TFP == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x07); elsif ELIsInHost(EL2) && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && CPTR_EL2.FPEN ↪ → IN {'x0'} then AArch64.AArch32SystemAccessTrap(EL2, 0x07); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && ↪ → ((IsFeatureImplemented(FEAT_AA32EL3) && ELUsingAArch32(EL3) && SCR.NS == '1' && NSACR.cp10 == ↪ → '0') || HCPTR.TCP10 == '1') then AArch32.TakeHypTrapException(0x08); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && HCR_EL2.TID0 == ↪ → '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x08); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HCR.TID0 == '1' ↪ → then AArch32.TakeHypTrapException(0x08); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && CPTR_EL3.TFP == ↪ → '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.AArch32SystemAccessTrap(EL3, 0x07); else return; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA64EL3) && ↪ → !ELUsingAArch32(EL3) && CPTR_EL3.TFP == '1' then UNDEFINED; elsif EL2Enabled() && ((IsFeatureImplemented(FEAT_AA32EL3) && ELUsingAArch32(EL3) && SCR.NS == '1' ↪ → && NSACR.cp10 == '0') || HCPTR.TCP10 == '1') then AArch32.TakeHypTrapException(0x00); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && CPTR_EL3.TFP == ↪ → '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.AArch32SystemAccessTrap(EL3, 0x07); else return; elsif PSTATE.EL == EL3 then if CPACR.cp10 == '00' then UNDEFINED; else return;
```