## D24.2.126 MAIR2\_EL3, Extended Memory Attribute Indirection Register (EL3)

The MAIR2\_EL3 characteristics are:

## Purpose

Provides the memory attribute encodings corresponding to the possible AttrIndx values in a VMSAv8-64 or VMSAv9-128 translation table entry for stage 1 translations at EL1.

## Configuration

This register is present only when FEAT\_AIE is implemented and FEAT\_AA64 is implemented. Otherwise, direct accesses to MAIR2\_EL3 are UNDEFINED.

## Attributes

MAIR2\_EL3 is a 64-bit register.

## Field descriptions

| 63    | 56    | 55 48 47   |       | 40 39   |       | 32   |
|-------|-------|------------|-------|---------|-------|------|
|       | Attr7 | Attr6      | Attr5 |         | Attr4 |      |
| 31    | 24 23 | 16 15      |       | 8 7     |       | 0    |
| Attr3 |       | Attr2      | Attr1 |         | Attr0 |      |

## Attr&lt;n&gt; , bits [8n+7:8n], for n = 7 to 0

Memory Attribute encoding.

When stage 1 Attributes Index Extension is enabled and AttrIndx[3] in a VMSAv8-64 or VMSAv9-128 translation table entry is 1, AttrIndx[2:0] gives the value of &lt;n&gt; in Attr&lt;n&gt;.

When stage 1 Attributes Index Extension is enabled and AttrIndx[3] in a VMSAv8-64 or VMSAv9-128 translation table entry is 0, see MAIR\_EL3.Attr

Attr is encoded as follows:

| Attr        |                                     | Meaning                                                                                                                                                                                                          |
|-------------|-------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0000 dd00 |                                     | Device memory. See encoding of 'dd' for the type of Device memory.                                                                                                                                               |
| 0b0000 dd01 |                                     | If FEAT_XS is implemented: Device memory with the XS attribute set to 0. See encoding of 'dd' for the type of Device memory. Otherwise, UNPREDICTABLE.                                                           |
| 0b0000 dd1x |                                     | UNPREDICTABLE.                                                                                                                                                                                                   |
| 0booooiiii  | where oooo != 0000 and iiii != 0000 | Normal memory. See encoding of 'oooo' and 'iiii' for the type of Normal memory.                                                                                                                                  |
| 0b01000000  |                                     | If FEAT_XS is implemented: Normal Inner Non-cacheable, Outer Non-cacheable memory with the XS attribute set to 0. Otherwise, UNPREDICTABLE.                                                                      |
| 0b10100000  |                                     | If FEAT_XS is implemented: Normal Inner Write-through Cacheable, Outer Write-through Cacheable, Read-Allocate, No-Write Allocate, Non-transient memory with the XS attribute set to 0. Otherwise, UNPREDICTABLE. |
| 0b11110000  |                                     | If FEAT_MTE2 is implemented: Tagged Normal Inner Write-Back, Outer Write-Back, Read-Allocate, Write-Allocate Non-transient memory. Otherwise, UNPREDICTABLE.                                                     |

| Attr       | Meaning                               |
|------------|---------------------------------------|
| 0bxxxx0000 | where xxxx != 0000 and UNPREDICTABLE. |

dd is encoded as follows:

oooo is encoded as follows:

| 'oooo'   |              | Meaning                                           |
|----------|--------------|---------------------------------------------------|
| 0b0000   |              | See encoding of Attr.                             |
| 0b00 RW  | where RW!=00 | Normal memory, Outer Write-Through Transient.     |
| 0b0100   |              | Normal memory, Outer Non-cacheable.               |
| 0b01 RW  | where RW!=00 | Normal memory, Outer Write-Back Transient.        |
| 0b10 RW  |              | Normal memory, Outer Write-Through Non-transient. |
| 0b11 RW  |              | Normal memory, Outer Write-Back Non-transient.    |

R encodes the Outer Read-Allocate policy and W encodes the Outer Write-Allocate policy.

iiii is encoded as follows:

| 'iiii'   |              | Meaning                                           |
|----------|--------------|---------------------------------------------------|
| 0b0000   |              | See encoding of Attr.                             |
| 0b00 RW  | where RW!=00 | Normal memory, Inner Write-Through Transient.     |
| 0b0100   |              | Normal memory, Inner Non-cacheable.               |
| 0b01 RW  | where RW!=00 | Normal memory, Inner Write-Back Transient.        |
| 0b10 RW  |              | Normal memory, Inner Write-Through Non-transient. |
| 0b11 RW  |              | Normal memory, Inner Write-Back Non-transient.    |

R encodes the Inner Read-Allocate policy and W encodes the Inner Write-Allocate policy.

In oooo and iiii , R and W are encoded as follows:

| 'dd'   | Meaning               |
|--------|-----------------------|
| 0b00   | Device-nGnRnE memory. |
| 0b01   | Device-nGnRE memory.  |
| 0b10   | Device-nGRE memory.   |
| 0b11   | Device-GRE memory.    |

then

| 'R' or 'W'   | Meaning      |
|--------------|--------------|
| 0b0          | No Allocate. |
| 0b1          | Allocate.    |

When FEAT\_XS is implemented, stage 1 Inner Write-Back Cacheable, Outer Write-Back Cacheable memory types have the XS attribute set to 0.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Accessing MAIR2\_EL3

Accesses to this register use the following encodings in the System register encoding space:

<!-- formula-not-decoded -->

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b110 | 0b1010 | 0b0001 | 0b001 |

if !(IsFeatureImplemented(FEAT\_AIE) &amp;&amp;

UNDEFINED;

elsif

PSTATE.EL == EL0

UNDEFINED;

elsif PSTATE.EL == EL1 then

UNDEFINED;

elsif PSTATE.EL == EL2 then

UNDEFINED;

elsif

PSTATE.EL == EL3

then

X[t, 64]

=

MAIR2\_EL3;

MSR MAIR2\_EL3, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b110 | 0b1010 | 0b0001 | 0b001 |

```
if !(IsFeatureImplemented(FEAT_AIE) && IsFeatureImplemented(FEAT_AA64)) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then UNDEFINED; elsif PSTATE.EL == EL2 then UNDEFINED; elsif PSTATE.EL == EL3 then if IsFeatureImplemented(FEAT_FGWTE3) && FGWTE3_EL3.MAIR2_EL3 == '1' then AArch64.SystemAccessTrap(EL3, 0x18); else MAIR2_EL3 = X[t, 64];
```

IsFeatureImplemented(FEAT\_AA64)) then