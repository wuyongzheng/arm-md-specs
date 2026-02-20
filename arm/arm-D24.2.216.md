## D24.2.216 VBAR\_EL3, Vector Base Address Register (EL3)

The VBAR\_EL3 characteristics are:

## Purpose

Holds the vector base address for any exception that is taken to EL3.

## Configuration

This register is present only when EL3 is implemented and FEAT\_AA64 is implemented. Otherwise, direct accesses to VBAR\_EL3 are UNDEFINED.

## Attributes

VBAR\_EL3 is a 64-bit register.

## Field descriptions

<!-- image -->

## VBA, bits [63:11]

Vector Base Address. Base address of the exception vectors for exceptions taken to EL3.

Note

If the implementation supports FEAT\_LVA3, then:

- If tagged addresses are not being used, bits [63:56] of VBAR\_EL3 must be 0 or else the use of the vector address will result in a recursive exception.

## Otherwise:

If the implementation supports FEAT\_LVA, then:

- If tagged addresses are being used, bits [55:52] of VBAR\_EL3 must be 0 or else the use of the vector address will result in a recursive exception.
- If tagged addresses are not being used, bits [63:52] of VBAR\_EL3 must be 0 or else the use of the vector address will result in a recursive exception.

If the implementation does not support FEAT\_LVA, then:

- If tagged addresses are being used, bits [55:48] of VBAR\_EL3 must be 0 or else the use of the vector address will result in a recursive exception.
- If tagged addresses are not being used, bits [63:48] of VBAR\_EL3 must be 0 or else the use of the vector address will result in a recursive exception.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Bits [10:0]

Reserved, RES0.

## Accessing VBAR\_EL3

Accesses to this register use the following encodings in the System register encoding space:

<!-- formula-not-decoded -->

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b110 | 0b1100 | 0b0000 | 0b000 |

if !(HaveEL(EL3) &amp;&amp; IsFeatureImplemented(FEAT\_AA64)) then

```
UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then UNDEFINED; elsif PSTATE.EL == EL2 then UNDEFINED; elsif PSTATE.EL == EL3 then X[t, 64] = VBAR_EL3;
```

MSR VBAR\_EL3, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b110 | 0b1100 | 0b0000 | 0b000 |

```
if !(HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64)) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then UNDEFINED; elsif PSTATE.EL == EL2 then UNDEFINED; elsif PSTATE.EL == EL3 then if IsFeatureImplemented(FEAT_FGWTE3) && FGWTE3_EL3.VBAR_EL3 == '1' then AArch64.SystemAccessTrap(EL3, 0x18); else VBAR_EL3 = X[t, 64];
```