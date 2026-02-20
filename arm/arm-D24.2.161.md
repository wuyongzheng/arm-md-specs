## D24.2.161 RNDR, Random Number

The RNDR characteristics are:

## Purpose

Random Number. Returns a 64-bit random number from an approved Random Bit Generator, where the Deterministic Random Bit Generator within the Random Bit Generator is reseeded from an approved entropy source at an IMPLEMENTATION DEFINED rate. See 'Properties of the generated random number'.

If the hardware returns a genuine random number, PSTATE.NZCV is set to 0b0000 .

If the instruction cannot return a genuine random number in a reasonable period of time, PSTATE.NZCV is set to 0b0100 and the data value returned is 0.

## Configuration

This register is present only when (FEAT\_RNG is implemented or FEAT\_RNG\_TRAP is implemented) and FEAT\_AA64 is implemented. Otherwise, direct accesses to RNDR are UNDEFINED.

## Attributes

RNDRis a 64-bit register.

## Field descriptions

<!-- image -->

| 63   | 32   |
|------|------|
|      | 0    |
| 31   |      |
| RNDR |      |

## RNDR, bits [63:0]

Random Number. Returns a 64-bit Random Number from an approved Random Bit Generator, where the Deterministic Random Bit Generator within the Random Bit Generator is reseeded from an approved entropy source at an IMPLEMENTATION DEFINED rate. See 'Properties of the generated random number'.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Accessing RNDR

Accesses to this register use the following encodings in the System register encoding space:

```
MRS <Xt>, RNDR
```

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b011 | 0b0010 | 0b0100 | 0b000 |

```
if !((IsFeatureImplemented(FEAT_RNG) || IsFeatureImplemented(FEAT_RNG_TRAP)) && ↪ → IsFeatureImplemented(FEAT_AA64)) then UNDEFINED; elsif PSTATE.EL == EL0 then if IsFeatureImplemented(FEAT_RNG_TRAP) && SCR_EL3.TRNDR == '1' then
```

```
if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif !IsFeatureImplemented(FEAT_RNG) then UNDEFINED; else X[t, 64] = RNDR; elsif PSTATE.EL == EL1 then if IsFeatureImplemented(FEAT_RNG_TRAP) && SCR_EL3.TRNDR == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif !IsFeatureImplemented(FEAT_RNG) then UNDEFINED; else X[t, 64] = RNDR; elsif PSTATE.EL == EL2 then if IsFeatureImplemented(FEAT_RNG_TRAP) && SCR_EL3.TRNDR == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif !IsFeatureImplemented(FEAT_RNG) then UNDEFINED; else X[t, 64] = RNDR; elsif PSTATE.EL == EL3 then if IsFeatureImplemented(FEAT_RNG_TRAP) && SCR_EL3.TRNDR == '1' then AArch64.SystemAccessTrap(EL3, 0x18); elsif !IsFeatureImplemented(FEAT_RNG) then UNDEFINED; else X[t, 64] = RNDR;
```