## D24.2.183 SCXTNUM\_EL3, EL3 Read/Write Software Context Number

The SCXTNUM\_EL3 characteristics are:

## Purpose

Provides a number that can be used to separate out different context numbers with the EL3 exception level, for the purpose of protecting against side-channels using branch prediction and similar resources.

## Configuration

This register is present only when (HaveEL(EL3) &amp;&amp; (IsFeatureImplemented(FEAT\_CSV2\_2) || IsFeatureImplemented(FEAT\_CSV2\_1p2))) &amp;&amp; IsFeatureImplemented(FEAT\_AA64). Otherwise, direct accesses to SCXTNUM\_EL3 are UNDEFINED.

## Attributes

SCXTNUM\_EL3 is a 64-bit register.

## Field descriptions

| 63                      | 32   |
|-------------------------|------|
| Software Context Number |      |
| 31                      | 0    |
| Software Context Number |      |

## SCXTNUM,bits [63:0]

Software Context Number. A number to identify the context within the EL3 exception level.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Accessing SCXTNUM\_EL3

Accesses to this register use the following encodings in the System register encoding space:

```
MRS <Xt>, SCXTNUM_EL3
```

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b110 | 0b1101 | 0b0000 | 0b111 |

```
if !(HaveEL(EL3) && (IsFeatureImplemented(FEAT_CSV2_2) || IsFeatureImplemented(FEAT_CSV2_1p2)) && ↪ → IsFeatureImplemented(FEAT_AA64)) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then UNDEFINED; elsif PSTATE.EL == EL2 then UNDEFINED; elsif PSTATE.EL == EL3 then X[t, 64] = SCXTNUM_EL3;
```

MSR SCXTNUM\_EL3, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b110 | 0b1101 | 0b0000 | 0b111 |

```
if !(HaveEL(EL3) && (IsFeatureImplemented(FEAT_CSV2_2) || IsFeatureImplemented(FEAT_CSV2_1p2)) && ↪ → IsFeatureImplemented(FEAT_AA64)) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then UNDEFINED; elsif PSTATE.EL == EL2 then UNDEFINED; elsif PSTATE.EL == EL3 then SCXTNUM_EL3 = X[t, 64];
```