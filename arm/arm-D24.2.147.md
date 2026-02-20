## D24.2.147 PIR\_EL3, Permission Indirection Register 3 (EL3)

The PIR\_EL3 characteristics are:

## Purpose

Stage 1 Permission Indirection Register for privileged access of the EL3 translation regime.

## Configuration

This register is present only when FEAT\_S1PIE is implemented and FEAT\_AA64 is implemented. Otherwise, direct accesses to PIR\_EL3 are UNDEFINED.

## Attributes

PIR\_EL3 is a 64-bit register.

## Field descriptions

<!-- image -->

| 63     | 60 59   | 56 55   | 52 51   | 48 47   | 44 43   | 39    | 36 35   | 32    |
|--------|---------|---------|---------|---------|---------|-------|---------|-------|
| Perm15 | Perm14  | Perm13  | Perm12  | Perm11  | Perm10  | Perm9 | Perm8   |       |
| 31     | 28 27   | 24 23   | 20 19   | 16 15   | 12 11   | 7     | 4 3     | 0     |
| Perm7  | Perm6   | Perm5   | Perm4   | Perm3   | Perm2   | Perm1 |         | Perm0 |

## Perm&lt;m&gt; , bits [4m+3:4m], for m = 15 to 0

Represents stage 1 Base Permissions.

| Perm<m>   | Meaning                                                        |
|-----------|----------------------------------------------------------------|
| 0b0000    | No access. Overlay applied.                                    |
| 0b0001    | Read. Overlay applied.                                         |
| 0b0010    | Execute. Overlay applied.                                      |
| 0b0011    | Read and Execute. Overlay applied.                             |
| 0b0100    | Reserved - treated as No access. Overlay applied.              |
| 0b0101    | Read and Write. Overlay applied.                               |
| 0b0110    | Read, Write, and Execute. Overlay applied. WXNcontrol applied. |
| 0b0111    | Read, Write, and Execute. Overlay applied.                     |
| 0b1000    | Read. Overlay not applied.                                     |
| 0b1001    | Read, GCS Read, and GCS Write. Overlay not applied.            |
| 0b1010    | Read and Execute. Overlay not applied.                         |
| 0b1011    | Reserved - treated as No access. Overlay not applied.          |
| 0b1100    | Read and Write. Overlay not applied.                           |
| 0b1101    | Reserved - treated as No access. Overlay not applied.          |
| 0b1110    | Read, Write, and Execute. Overlay not applied.                 |

0b1111

This field is permitted to be cached in a TLB.

When stage 1 Indirect Permission mechanism is disabled, this register is ignored.

Unless otherwise specified, the WXN control is not applied.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Accessing PIR\_EL3

Accesses to this register use the following encodings in the System register encoding space:

<!-- formula-not-decoded -->

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b110 | 0b1010 | 0b0010 | 0b011 |

if !(IsFeatureImplemented(FEAT\_S1PIE) &amp;&amp;

UNDEFINED;

elsif

PSTATE.EL == EL0

UNDEFINED;

elsif

PSTATE.EL == EL1

UNDEFINED;

elsif

PSTATE.EL == EL2

UNDEFINED;

elsif

PSTATE.EL == EL3

X[t, 64]

=

PIR\_EL3;

MSR PIR\_EL3, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b110 | 0b1010 | 0b0010 | 0b011 |

```
if !(IsFeatureImplemented(FEAT_S1PIE) && IsFeatureImplemented(FEAT_AA64)) UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then UNDEFINED; elsif PSTATE.EL == EL2 then UNDEFINED; elsif PSTATE.EL == EL3 then if IsFeatureImplemented(FEAT_FGWTE3) && FGWTE3_EL3.PIR_EL3 == '1' then AArch64.SystemAccessTrap(EL3, 0x18); else PIR_EL3 = X[t, 64];
```

```
then
```

IsFeatureImplemented(FEAT\_AA64))

then then

then then

then