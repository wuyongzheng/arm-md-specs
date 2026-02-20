## D24.2.20 APAS, Associate PA space

The APAS characteristics are:

## Purpose

Associate a location with a specified PA space, for locations that are protected by a memory-side PAS filter.

## Configuration

This system instruction is present only when FEAT\_RME\_GPC3 is implemented and FEAT\_AA64 is implemented. Otherwise, direct accesses to APAS are UNDEFINED.

## Attributes

APAS is a 64-bit System instruction.

## Field descriptions

<!-- image -->

## NS, bit [63]

Together with the NSE field, selects the target physical address space.

| NSE   | NS   | Meaning                                                       |
|-------|------|---------------------------------------------------------------|
| 0b0   | 0b0  | When Secure state is implemented, Secure. Otherwise reserved. |
| 0b0   | 0b1  | Non-secure.                                                   |
| 0b1   | 0b0  | Root.                                                         |
| 0b1   | 0b1  | Realm.                                                        |

## NSE, bit [62]

Together with the NS field, selects the target physical address space.

For a description of the values derived by evaluating NS and NSE together, see .NS.

## Bits [61:56]

Reserved, RES0.

## PA, bits [55:6]

Bits [55:6] of the Physical Address.

Bits of Xt corresponding to physical address bits above the implemented physical address size indicated in ID\_AA64MMFR0\_EL1.PARange are RES0. For example, if 44 bits of PA space are implemented, then Xt[55:44] are RES0.

## Bits [5:3]

Reserved, RES0.

## TargetAttributes, bits [2:0]

The Target Attributes field is encoded as follows:

| TargetAttributes   | Meaning                   |
|--------------------|---------------------------|
| 0b000              | Default behavior applies. |
| 0b001 .. 0b111     | IMPLEMENTATION DEFINED.   |

## Executing APAS

This instruction is not subject to any translation, permission checks, or granule protection checks.

This system instruction is an alias of the SYS instruction.

Accesses to this instruction use the following encodings in the System instruction encoding space:

APAS &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b01  | 0b110 | 0b0111 | 0b0000 | 0b000 |

```
if !(IsFeatureImplemented(FEAT_RME_GPC3) && IsFeatureImplemented(FEAT_AA64)) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then UNDEFINED; elsif PSTATE.EL == EL2 then UNDEFINED; elsif PSTATE.EL == EL3 then AArch64.APAS(X[t, 64]);
```