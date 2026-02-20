## D24.2.162 RNDRRS, Random Number Full Entropy

The RNDRRS characteristics are:

## Purpose

Random Number with fresh full entropy. Returns a 64-bit random number from an approved Random Bit Generator, using either a Non-deterministic Random Bit Generator or one where the Deterministic Random Bit Generator is reseeded, where possible, from an approved entropy source before the return of the random number. See 'Properties of the generated random number'.

If the hardware returns a genuine random number, PSTATE.NZCV is set to 0b0000 .

If the instruction cannot return a genuine random number in a reasonable period of time, PSTATE.NZCV is set to 0b0100 and the data value returned is 0.

When FEAT\_RNG\_TRAP is implemented and SCR\_EL3.TRNDR is 1, reads of this register are trapped to EL3.

## Configuration

This register is present only when (FEAT\_RNG is implemented or FEAT\_RNG\_TRAP is implemented) and FEAT\_AA64 is implemented. Otherwise, direct accesses to RNDRRS are UNDEFINED.

## Attributes

RNDRRSis a 64-bit register.

## Field descriptions

<!-- image -->

| 63     | 32     |        |
|--------|--------|--------|
| RNDRRS | RNDRRS | RNDRRS |
| 31     | 0      |        |
| RNDRRS | RNDRRS | RNDRRS |

## RNDRRS, bits [63:0]

Random Number with fresh full entropy. Returns a 64-bit random number from an approved Random Bit Generator, using either a Non-deterministic Random Bit Generator or one where the Deterministic Random Bit Generator is reseeded, where possible, from an approved entropy source before the return of the random number. See 'Properties of the generated random number'.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Accessing RNDRRS

Accesses to this register use the following encodings in the System register encoding space:

MRS &lt;Xt&gt;, RNDRRS

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b011 | 0b0010 | 0b0100 | 0b001 |

```
if !((IsFeatureImplemented(FEAT_RNG) || IsFeatureImplemented(FEAT_RNG_TRAP)) && ↪ → IsFeatureImplemented(FEAT_AA64)) then UNDEFINED; elsif PSTATE.EL == EL0 then if IsFeatureImplemented(FEAT_RNG_TRAP) && SCR_EL3.TRNDR == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif !IsFeatureImplemented(FEAT_RNG) then UNDEFINED; else X[t, 64] = RNDRRS; elsif PSTATE.EL == EL1 then if IsFeatureImplemented(FEAT_RNG_TRAP) && SCR_EL3.TRNDR == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif !IsFeatureImplemented(FEAT_RNG) then UNDEFINED; else X[t, 64] = RNDRRS; elsif PSTATE.EL == EL2 then if IsFeatureImplemented(FEAT_RNG_TRAP) && SCR_EL3.TRNDR == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif !IsFeatureImplemented(FEAT_RNG) then UNDEFINED; else X[t, 64] = RNDRRS; elsif PSTATE.EL == EL3 then if IsFeatureImplemented(FEAT_RNG_TRAP) && SCR_EL3.TRNDR == '1' then AArch64.SystemAccessTrap(EL3, 0x18); elsif !IsFeatureImplemented(FEAT_RNG) then UNDEFINED; else X[t, 64] = RNDRRS;
```