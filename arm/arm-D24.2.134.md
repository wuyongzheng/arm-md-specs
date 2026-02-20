## D24.2.134 MECID\_RL\_A\_EL3, Realm PA space Alternate MECID for EL3 stage 1 translation regime

The MECID\_RL\_A\_EL3 characteristics are:

## Purpose

Alternate MECID for EL3 accesses to the Realm physical address space, translated by TTBR0\_EL3.

## Configuration

This register is present only when FEAT\_MEC is implemented and FEAT\_AA64 is implemented. Otherwise, direct accesses to MECID\_RL\_A\_EL3 are UNDEFINED.

## Attributes

MECID\_RL\_A\_EL3 is a 64-bit register.

## Field descriptions

<!-- image -->

## Bits [63:16]

Reserved, RES0.

## MECID, bits [15:0]

If MECIDWidth is less than 16 bits, bits[15:MECIDWidth] are RES0.

Note

MECIDWidth is defined in MECIDR\_EL2.MECIDWidthm1.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Accessing MECID\_RL\_A\_EL3

Accesses to this register use the following encodings in the System register encoding space:

MRS &lt;Xt&gt;, MECID\_RL\_A\_EL3

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b110 | 0b1010 | 0b1010 | 0b001 |

```
if !(IsFeatureImplemented(FEAT_MEC) && IsFeatureImplemented(FEAT_AA64)) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then
```

UNDEFINED; elsif PSTATE.EL == EL2 then UNDEFINED; elsif PSTATE.EL == EL3 then X[t, 64] = MECID\_RL\_A\_EL3;

MSR MECID\_RL\_A\_EL3, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b110 | 0b1010 | 0b1010 | 0b001 |

```
if !(IsFeatureImplemented(FEAT_MEC) && IsFeatureImplemented(FEAT_AA64)) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then UNDEFINED; elsif PSTATE.EL == EL2 then UNDEFINED; elsif PSTATE.EL == EL3 then if IsFeatureImplemented(FEAT_FGWTE3) && FGWTE3_EL3.MECID_RL_A_EL3 == '1' AArch64.SystemAccessTrap(EL3, 0x18); else MECID_RL_A_EL3 = X[t, 64];
```

then