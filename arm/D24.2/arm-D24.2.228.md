## D24.2.228 ZCR\_EL3, SVE Control Register (EL3)

The ZCR\_EL3 characteristics are:

## Purpose

This register controls aspects of SVE visible at all Exception levels.

## Configuration

This register has no effect when FEAT\_SME is implemented and the PE is in Streaming SVE mode.

This register is present only when FEAT\_SVE is implemented. Otherwise, direct accesses to ZCR\_EL3 are UNDEFINED.

## Attributes

ZCR\_EL3 is a 64-bit register.

## Field descriptions

<!-- image -->

| 63      |        |    | 32   |     |
|---------|--------|----|------|-----|
| RES0 31 |        | 4  | 0    |     |
| RES0    | RAZ/WI |    |      | LEN |

## Bits [63:9]

Reserved, RES0.

## Bits [8:4]

Reserved, RAZ/WI.

## LEN, bits [3:0]

Requests an Effective Non-streaming SVE vector length at EL3 of (LEN+1)*128 bits.

The Non-streaming SVE vector length can be any power of two from 128 bits to 2048 bits inclusive. An implementation can support a subset of the architecturally permitted lengths. An implementation is required to support all lengths that are powers of two, from 128 bits up to its maximum implemented Non-streaming SVE vector length.

When FEAT\_SME is not implemented, or the PE is not in Streaming SVE mode, the Effective SVE vector length (VL) is equal to the Effective Non-streaming SVE vector length.

When FEAT\_SME is implemented and the PE is in Streaming SVE mode, VL is equal to the Effective Streaming SVE vector length. See SMCR\_EL3.

For all purposes other than returning the result of a direct read of ZCR\_EL3, the PE selects the highest supported Non-streaming SVE vector length that is less than or equal to the requested length.

An indirect read of ZCR\_EL3.LEN appears to occur in program order relative to a direct write of the same register, without the need for explicit synchronization.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Accessing ZCR\_EL3

Accesses to this register use the following encodings in the System register encoding space:

MRS &lt;Xt&gt;, ZCR\_EL3

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b110 | 0b0001 | 0b0010 | 0b000 |

```
if !IsFeatureImplemented(FEAT_SVE) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then UNDEFINED; elsif PSTATE.EL == EL2 then UNDEFINED; elsif PSTATE.EL == EL3 then if CPTR_EL3.EZ == '0' then AArch64.SystemAccessTrap(EL3, 0x19); else X[t, 64] = ZCR_EL3;
```

MSR ZCR\_EL3, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b110 | 0b0001 | 0b0010 | 0b000 |

```
if !IsFeatureImplemented(FEAT_SVE) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then UNDEFINED; elsif PSTATE.EL == EL2 then UNDEFINED; elsif PSTATE.EL == EL3 then if CPTR_EL3.EZ == '0' then AArch64.SystemAccessTrap(EL3, 0x19); else ZCR_EL3 = X[t, 64];
```