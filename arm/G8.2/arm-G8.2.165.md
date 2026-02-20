## G8.2.165 TTBCR, Translation Table Base Control Register

The TTBCR characteristics are:

## Purpose

The control register for stage 1 of the PL1&amp;0 translation regime. Its controls include:

- Where the VA range is split between addresses translated using TTBR0 and addresses translated using TTBR1.
- The translation table format used by this stage of translation.

From Armv8.2, when the value of TTBCR.{EAE, T2E} is {1, 1}, TTBCR is used with TTBCR2.

## Configuration

The current translation table format determines which format of the register is used.

Some RW fields of this register have defined reset values. These apply only if the PE resets into an Exception level that is using AArch32. If the PE resets into EL3 using AArch32, then:

- The EAE bit resets to 0 in both the Secure and the Non-secure instances of the register.
- Other reset values apply only to the Secure instance of the register.

AArch32 System register TTBCR bits [31:0] are architecturally mapped to AArch64 System register TCR\_EL1[31:0].

This register is banked between TTBCR and TTBCR\_S and TTBCR\_NS.

This register is present only when FEAT\_AA32EL1 is implemented. Otherwise, direct accesses to TTBCR are UNDEFINED.

## Attributes

TTBCR is a 32-bit register.

This register has the following instances:

- TTBCR, when EL3 is not implemented or FEAT\_AA64 is implemented.
- TTBCR\_S, when FEAT\_AA32EL3 is implemented.
- TTBCR\_NS, when FEAT\_AA32EL3 is implemented.

## Field descriptions

When TTBCR.EAE == '0':

<!-- image -->

## EAE, bit [31]

Extended Address Enable.

| EAE   | Meaning                                                                                  |
|-------|------------------------------------------------------------------------------------------|
| 0b0   | Use the VMSAv8-32 translation system with the Short-descriptor translation table format. |

The reset behavior of this field is:

- On a Warm reset, this field resets to '0' .

## Bits [30:6]

Reserved, RES0.

## PD1, bit [5]

Translation table walk disable for translations using TTBR1. This bit controls whether a translation table walk is performed on a TLB miss, for an address that is translated using TTBR1.

| PD1   | Meaning                                                                                                                      |
|-------|------------------------------------------------------------------------------------------------------------------------------|
| 0b0   | Perform translation table walks using TTBR1.                                                                                 |
| 0b1   | ATLBmiss on an address that is translated using TTBR1 generates a Translation fault. No translation table walk is performed. |

The reset behavior of this field is:

- On a Warm reset, this field resets to '0' .

## PD0, bit [4]

Translation table walk disable for translations using TTBR0. This bit controls whether a translation table walk is performed on a TLB miss for an address that is translated using TTBR0.

| PD0   | Meaning                                                                                                                      |
|-------|------------------------------------------------------------------------------------------------------------------------------|
| 0b0   | Perform translation table walks using TTBR0.                                                                                 |
| 0b1   | ATLBmiss on an address that is translated using TTBR0 generates a Translation fault. No translation table walk is performed. |

The reset behavior of this field is:

- On a Warm reset, this field resets to '0' .

## Bit [3]

Reserved, RES0.

## N, bits [2:0]

Indicate the width of the base address held in TTBR0. In TTBR0, the base address field is bits[31:14-N]. The value of N also determines:

- Whether TTBR0 or TTBR1 is used as the base address for translation table walks.
- The size of the translation table pointed to by TTBR0.

Ncan take any value from 0 to 7, that is, from 0b000 to 0b111 .

When N has its reset value of 0, the translation table base is compatible with Armv5 and Armv6.

The reset behavior of this field is:

- On a Warm reset, this field resets to '000' .

## When TTBCR.EAE == '1':

<!-- image -->

## EAE, bit [31]

Extended Address Enable.

| EAE   | Meaning                                                                                 |
|-------|-----------------------------------------------------------------------------------------|
| 0b1   | Use the VMSAv8-32 translation system with the Long-descriptor translation table format. |

The reset behavior of this field is:

- On a Warm reset, this field resets to '0' .

## IMPLEMENTATIONDEFINED, bit [30]

IMPLEMENTATION DEFINED.

The reset behavior of this field is:

- On a Warm reset, this field resets to '0' .

## SH1, bits [29:28]

Shareability attribute for memory associated with translation table walks using TTBR1.

| SH1   | Meaning          |
|-------|------------------|
| 0b00  | Non-shareable.   |
| 0b10  | Outer Shareable. |
| 0b11  | Inner Shareable. |

Other values are reserved. The effect of programming this field to a Reserved value is that behavior is CONSTRAINED UNPREDICTABLE.

The reset behavior of this field is:

- On a Warm reset, this field resets to '00' .

## ORGN1, bits [27:26]

Outer cacheability attribute for memory associated with translation table walks using TTBR1.

| ORGN1   | Meaning                                                                       |
|---------|-------------------------------------------------------------------------------|
| 0b00    | Normal memory, Outer Non-cacheable.                                           |
| 0b01    | Normal memory, Outer Write-Back Read-Allocate Write-Allocate Cacheable.       |
| 0b10    | Normal memory, Outer Write-Through Read-Allocate No Write-Allocate Cacheable. |
| 0b11    | Normal memory, Outer Write-Back Read-Allocate No Write-Allocate Cacheable.    |

The reset behavior of this field is:

- On a Warm reset, this field resets to '00' .

## IRGN1, bits [25:24]

Inner cacheability attribute for memory associated with translation table walks using TTBR1.

| IRGN1   | Meaning                                                                       |
|---------|-------------------------------------------------------------------------------|
| 0b00    | Normal memory, Inner Non-cacheable.                                           |
| 0b01    | Normal memory, Inner Write-Back Read-Allocate Write-Allocate Cacheable.       |
| 0b10    | Normal memory, Inner Write-Through Read-Allocate No Write-Allocate Cacheable. |
| 0b11    | Normal memory, Inner Write-Back Read-Allocate No Write-Allocate Cacheable.    |

The reset behavior of this field is:

- On a Warm reset, this field resets to '00' .

## EPD1, bit [23]

Translation table walk disable for translations using TTBR1. This bit controls whether a translation table walk is performed on a TLB miss, for an address that is translated using TTBR1.

| EPD1   | Meaning                                                                                                                      |
|--------|------------------------------------------------------------------------------------------------------------------------------|
| 0b0    | Perform translation table walks using TTBR1.                                                                                 |
| 0b1    | ATLBmiss on an address that is translated using TTBR1 generates a Translation fault. No translation table walk is performed. |

The reset behavior of this field is:

- On a Warm reset, this field resets to '0' .

## A1, bit [22]

Selects whether TTBR0 or TTBR1 defines the ASID.

| A1   | Meaning                      |
|------|------------------------------|
| 0b0  | TTBR0.ASID defines the ASID. |
| 0b1  | TTBR1.ASID defines the ASID. |

The reset behavior of this field is:

- On a Warm reset, this field resets to '0' .

## Bits [21:19]

Reserved, RES0.

## T1SZ, bits [18:16]

See 'Selecting between TTBR0 and TTBR1, VMSAv8-32 Long-descriptor translation table format' for how TTBCR.{T1SZ, T0SZ} determine the input address ranges and memory region sizes translated using TTBR0 and TTBR1.

The reset behavior of this field is:

- On a Warm reset, this field resets to '000' .

## Bits [15:14]

Reserved, RES0.

## SH0, bits [13:12]

Shareability attribute for memory associated with translation table walks using TTBR0.

| SH0   | Meaning         |
|-------|-----------------|
| 0b00  | Non-shareable   |
| 0b10  | Outer Shareable |
| 0b11  | Inner Shareable |

Other values are reserved. The effect of programming this field to a Reserved value is that behavior is CONSTRAINED UNPREDICTABLE.

The reset behavior of this field is:

- On a Warm reset, this field resets to '00' .

## ORGN0, bits [11:10]

Outer cacheability attribute for memory associated with translation table walks using TTBR0.

| ORGN0   | Meaning                                                                       |
|---------|-------------------------------------------------------------------------------|
| 0b00    | Normal memory, Outer Non-cacheable.                                           |
| 0b01    | Normal memory, Outer Write-Back Read-Allocate Write-Allocate Cacheable.       |
| 0b10    | Normal memory, Outer Write-Through Read-Allocate No Write-Allocate Cacheable. |

| 0b11   | Normal memory, Outer Write-Back Read-Allocate No Write-Allocate Cacheable.   |
|--------|------------------------------------------------------------------------------|

The reset behavior of this field is:

- On a Warm reset, this field resets to '00' .

## IRGN0, bits [9:8]

Inner cacheability attribute for memory associated with translation table walks using TTBR0.

| IRGN0   | Meaning                                                                       |
|---------|-------------------------------------------------------------------------------|
| 0b00    | Normal memory, Inner Non-cacheable.                                           |
| 0b01    | Normal memory, Inner Write-Back Read-Allocate Write-Allocate Cacheable.       |
| 0b10    | Normal memory, Inner Write-Through Read-Allocate No Write-Allocate Cacheable. |
| 0b11    | Normal memory, Inner Write-Back Read-Allocate No Write-Allocate Cacheable.    |

The reset behavior of this field is:

- On a Warm reset, this field resets to '00' .

## EPD0, bit [7]

Translation table walk disable for translations using TTBR0. This bit controls whether a translation table walk is performed on a TLB miss, for an address that is translated using TTBR0.

| EPD0   | Meaning                                                                                                                      |
|--------|------------------------------------------------------------------------------------------------------------------------------|
| 0b0    | Perform translation table walks using TTBR0.                                                                                 |
| 0b1    | ATLBmiss on an address that is translated using TTBR0 generates a Translation fault. No translation table walk is performed. |

The reset behavior of this field is:

- On a Warm reset, this field resets to '0' .

## T2E, bit [6]

## When FEAT\_AA32HPD is implemented:

TTBCR2 Enable.

| T2E   | Meaning                                                                                                                  |
|-------|--------------------------------------------------------------------------------------------------------------------------|
| 0b0   | TTBCR2 is disabled. The contents of TTBCR2 are treated as 0 for all purposes other than reading or writing the register. |
| 0b1   | TTBCR2 is enabled.                                                                                                       |

If TTBCR.EAE==0, then the behavior is as if the bit is 0.

## Otherwise:

Reserved, RES0.

## Bits [5:3]

Reserved, RES0.

## T0SZ, bits [2:0]

See 'Selecting between TTBR0 and TTBR1, VMSAv8-32 Long-descriptor translation table format' for how TTBCR.{T1SZ, T0SZ} determine the input address ranges and memory region sizes translated using TTBR0 and TTBR1.

The reset behavior of this field is:

- On a Warm reset, this field resets to '000' .

## Accessing TTBCR

Accesses to this register use the following encodings in the System register encoding space:

```
MRC{<c>}{<q>} <coproc>, {#}<opc1>, <Rt>, <CRn>, <CRm>{, {#}<opc2>}
```

| coproc   | opc1   | CRn    | CRm    | opc2   |
|----------|--------|--------|--------|--------|
| 0b1111   | 0b000  | 0b0010 | 0b0000 | 0b010  |

```
if !IsFeatureImplemented(FEAT_AA32EL1) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && HSTR_EL2.T2 == '1' ↪ → then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HSTR.T2 == '1' ↪ → then AArch32.TakeHypTrapException(0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && HCR_EL2.TRVM == ↪ → '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HCR.TRVM == '1' ↪ → then AArch32.TakeHypTrapException(0x03); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA32EL3) && ELUsingAArch32(EL3) then R[t] = TTBCR_NS; else R[t] = TTBCR; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && IsFeatureImplemented(FEAT_AA32EL3) && ELUsingAArch32(EL3) then R[t] = TTBCR_NS; else R[t] = TTBCR; elsif PSTATE.EL == EL3 then if SCR.NS == '0' then R[t] = TTBCR_S; else R[t] = TTBCR_NS;
```

| coproc   | opc1   | CRn    | CRm    | opc2   |
|----------|--------|--------|--------|--------|
| 0b1111   | 0b000  | 0b0010 | 0b0000 | 0b010  |

```
if !IsFeatureImplemented(FEAT_AA32EL1) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && HSTR_EL2.T2 == '1' ↪ → then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HSTR.T2 == '1' ↪ → then AArch32.TakeHypTrapException(0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && HCR_EL2.TVM == ↪ → '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HCR.TVM == '1' ↪ → then AArch32.TakeHypTrapException(0x03); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA32EL3) && ELUsingAArch32(EL3) then TTBCR_NS = R[t]; else TTBCR = R[t]; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && IsFeatureImplemented(FEAT_AA32EL3) && ELUsingAArch32(EL3) then TTBCR_NS = R[t]; else TTBCR = R[t]; elsif PSTATE.EL == EL3 then if SCR.NS == '0' && CP15SDISABLE == HIGH then UNDEFINED; elsif SCR.NS == '0' && CP15SDISABLE2 == HIGH then UNDEFINED; else if SCR.NS == '0' then TTBCR_S = R[t]; else TTBCR_NS = R[t];
```