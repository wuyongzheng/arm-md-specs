## D24.2.43 DACR32\_EL2, Domain Access Control Register

The DACR32\_EL2 characteristics are:

## Purpose

Allows access to the AArch32 DACR register from AArch64 state only. Its value has no effect on execution in AArch64 state.

## Configuration

If EL2 is not implemented but EL3 is implemented, and EL1 is capable of using AArch32, then this register is not RES0.

AArch64 System register DACR32\_EL2 bits [31:0] are architecturally mapped to AArch32 System register DACR[31:0].

This register is present only when FEAT\_AA32EL1 is implemented and FEAT\_AA64 is implemented. Otherwise, direct accesses to DACR32\_EL2 are UNDEFINED.

## Attributes

DACR32\_EL2 is a 64-bit register.

## Field descriptions

<!-- image -->

## Bits [63:32]

Reserved, RES0.

## D&lt;n&gt; , bits [2n+1:2n], for n = 15 to 0

Domain n access permission, where n = 0 to 15. Permitted values are:

| D<n>   | Meaning                                                                                  |
|--------|------------------------------------------------------------------------------------------|
| 0b00   | No access. Any access to the domain generates a Domain fault.                            |
| 0b01   | Client. Accesses are checked against the permission bits in the translation tables.      |
| 0b11   | Manager. Accesses are not checked against the permission bits in the translation tables. |

The value

0b10 is reserved.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Accessing DACR32\_EL2

Accesses to this register use the following encodings in the System register encoding space:

MRS &lt;Xt&gt;, DACR32\_EL2

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b100 | 0b0011 | 0b0000 | 0b000 |

if !(IsFeatureImplemented(FEAT\_AA32EL1) &amp;&amp; IsFeatureImplemented(FEAT\_AA64)) then UNDEFINED;

elsif !IsFeatureImplemented(FEAT\_AA32EL1) then

UNDEFINED;

elsif PSTATE.EL == EL0 then

UNDEFINED;

elsif PSTATE.EL == EL1 then

if EffectiveHCR\_EL2\_NVx() IN {'xx1'} then AArch64.SystemAccessTrap(EL2, 0x18);

else

UNDEFINED;

elsif PSTATE.EL == EL2 then

X[t, 64] = DACR32\_EL2;

elsif PSTATE.EL == EL3 then

X[t, 64] = DACR32\_EL2;

MSR DACR32\_EL2, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b100 | 0b0011 | 0b0000 | 0b000 |

if !(IsFeatureImplemented(FEAT\_AA32EL1) &amp;&amp; IsFeatureImplemented(FEAT\_AA64)) then

UNDEFINED;

elsif !IsFeatureImplemented(FEAT\_AA32EL1) then

UNDEFINED;

elsif PSTATE.EL == EL0 then

UNDEFINED;

elsif PSTATE.EL == EL1 then if EffectiveHCR\_EL2\_NVx() IN {'xx1'} then AArch64.SystemAccessTrap(EL2, 0x18);

else

UNDEFINED;

elsif PSTATE.EL == EL2 then

DACR32\_EL2 = X[t, 64];

elsif PSTATE.EL == EL3 then

DACR32\_EL2 = X[t, 64];