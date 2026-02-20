## D24.2.153 POR\_EL3, Permission Overlay Register 3 (EL3)

The POR\_EL3 characteristics are:

## Purpose

Stage 1 Permission Overlay Register for privileged access of the EL3 translation regime.

## Configuration

This register is present only when FEAT\_S1POE is implemented and FEAT\_AA64 is implemented. Otherwise, direct accesses to POR\_EL3 are UNDEFINED.

## Attributes

POR\_EL3 is a 64-bit register.

## Field descriptions

<!-- image -->

| 63     | 60 59   | 56 55   | 52 51   | 48 47   | 44 43   | 40 39   |       | 36 35   | 32   |
|--------|---------|---------|---------|---------|---------|---------|-------|---------|------|
| Perm15 | Perm14  | Perm13  | Perm12  | Perm11  | Perm10  |         | Perm9 | Perm8   |      |
| 31     | 28 27   | 24 23   | 20 19   | 16 15   | 12 11   | 8 7     |       | 4 3     | 0    |
| Perm7  | Perm6   | Perm5   | Perm4   |         | Perm3   | Perm2   | Perm1 | Perm0   |      |

## Perm&lt;m&gt; , bits [4m+3:4m], for m = 15 to 0

Perm Represents stage 1 Overlay Permissions.

| Perm<m>   | Meaning                         |
|-----------|---------------------------------|
| 0b0000    | No access.                      |
| 0b0001    | Read.                           |
| 0b0010    | Execute.                        |
| 0b0011    | Read, Execute.                  |
| 0b0100    | Write.                          |
| 0b0101    | Write, Read.                    |
| 0b0110    | Write, Execute.                 |
| 0b0111    | Read, Write, Execute.           |
| 0b1xxx    | Reserved - treated as No access |

If FEAT\_D128 is implemented and VMSAv9-128 is in use, then fields Perm[8] to Perm[15] are used for POIndex values 8 to 15.

Otherwise, the fields Perm[8] to Perm[15] are RES0.

This field is not permitted to be cached in a TLB.

When stage 1 Overlay mechanism is disabled, this register is ignored.

The reset behavior of this field is:

· On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Accessing POR\_EL3

Accesses to this register use the following encodings in the System register encoding space:

MRS &lt;Xt&gt;, POR\_EL3

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b110 | 0b1010 | 0b0010 | 0b100 |

if !(IsFeatureImplemented(FEAT\_S1POE) &amp;&amp; IsFeatureImplemented(FEAT\_AA64)) then UNDEFINED;

elsif PSTATE.EL == EL0 then

UNDEFINED;

elsif PSTATE.EL == EL1 then

UNDEFINED;

elsif PSTATE.EL == EL2 then

UNDEFINED;

elsif PSTATE.EL == EL3 then

X[t, 64] = POR\_EL3;

MSR POR\_EL3, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b110 | 0b1010 | 0b0010 | 0b100 |

if !(IsFeatureImplemented(FEAT\_S1POE) &amp;&amp; IsFeatureImplemented(FEAT\_AA64)) then

UNDEFINED;

elsif PSTATE.EL == EL0 then UNDEFINED;

elsif PSTATE.EL == EL1 then

UNDEFINED;

elsif PSTATE.EL == EL2 then

UNDEFINED;

elsif PSTATE.EL == EL3 then

POR\_EL3 = X[t, 64];