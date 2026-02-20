## D24.2.135 MECIDR\_EL2, MEC Identification Register

The MECIDR\_EL2 characteristics are:

## Purpose

MECidentification register.

## Configuration

If EL2 is not implemented, this register is RES0 from EL3.

This register is present only when FEAT\_MEC is implemented and FEAT\_AA64 is implemented. Otherwise, direct accesses to MECIDR\_EL2 are UNDEFINED.

## Attributes

MECIDR\_EL2 is a 64-bit register.

## Field descriptions

<!-- image -->

| 63   | 32           |
|------|--------------|
| RES0 |              |
| 31   | 4 3 0        |
| RES0 | MECIDWidthm1 |

## Bits [63:4]

Reserved, RES0.

## MECIDWidthm1, bits [3:0]

MECID width minus 1.

The value of this field plus 1 is the MECID width in bits, that this PE supports.

This field has an IMPLEMENTATION DEFINED value.

For example, the value 0b1111 indicates that this PE supports a MECID width of 16 bits, and provides 2 16 possible MECID values.

MECIDWidth is defined as MECIDR\_EL2.MECIDWidthm1 + 1.

Access to this field is RO.

## Accessing MECIDR\_EL2

For accesses from EL2 and EL3, this register is RO.

Accesses to this register use the following encodings in the System register encoding space:

MRS &lt;Xt&gt;, MECIDR\_EL2

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b100 | 0b1010 | 0b1000 | 0b111 |

```
if !(IsFeatureImplemented(FEAT_MEC) && UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then UNDEFINED; elsif PSTATE.EL == EL2 then X[t, 64] = MECIDR_EL2; elsif PSTATE.EL == EL3 then X[t, 64] = MECIDR_EL2;
```

```
IsFeatureImplemented(FEAT_AA64)) then
```