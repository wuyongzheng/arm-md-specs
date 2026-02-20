## D24.2.31 CCSIDR2\_EL1, Current Cache Size ID Register 2

The CCSIDR2\_EL1 characteristics are:

## Purpose

Provides the information about the architecture of the currently selected cache from bits[63:32] of CCSIDR\_EL1.

## Configuration

In an implementation which does not support AArch32 at EL1, it is IMPLEMENTATION DEFINED whether reading this register gives an UNKNOWN value or is UNDEFINED.

The implementation includes one CCSIDR2\_EL1 for each cache that it can access. CSSELR\_EL1 selects which Cache Size ID Register is accessible.

AArch64 System register CCSIDR2\_EL1 bits [31:0] are architecturally mapped to AArch32 System register CCSIDR2[31:0].

This register is present only when FEAT\_CCIDX is implemented and FEAT\_AA64 is implemented. Otherwise, direct accesses to CCSIDR2\_EL1 are UNDEFINED.

## Attributes

CCSIDR2\_EL1 is a 64-bit register.

## Field descriptions

<!-- image -->

## Bits [63:24]

Reserved, RES0.

## NumSets, bits [23:0]

(Number of sets in cache) - 1, therefore a value of 0 indicates 1 set in the cache. The number of sets does not have to be a power of 2.

## Accessing CCSIDR2\_EL1

If CSSELR\_EL1.{TnD, Level, InD} is programmed to a cache level that is not implemented, then on a read of the CCSIDR2\_EL1 the behavior is CONSTRAINED UNPREDICTABLE, and can be one of the following:

- The CCSIDR2\_EL1 read is treated as NOP.
- The CCSIDR2\_EL1 read is UNDEFINED. If FEAT\_IDST is implemented, this is permitted to be reported with EC syndrome value 0x18 .
- The CCSIDR2\_EL1 read returns an UNKNOWN value.

Accesses to this register use the following encodings in the System register encoding space:

MRS &lt;Xt&gt;, CCSIDR2\_EL1

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b001 | 0b0000 | 0b0000 | 0b010 |

```
if !(IsFeatureImplemented(FEAT_CCIDX) && IsFeatureImplemented(FEAT_AA64)) then UnimplementedIDRegister(); elsif PSTATE.EL == EL0 then if IsFeatureImplemented(FEAT_IDST) then if EL2Enabled() && HCR_EL2.TGE == '1' then AArch64.SystemAccessTrap(EL2, 0x18); else AArch64.SystemAccessTrap(EL1, 0x18); else UNDEFINED; elsif PSTATE.EL == EL1 then if EL2Enabled() && HCR_EL2.TID2 == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && IsFeatureImplemented(FEAT_EVT) && HCR_EL2.TID4 == '1' then AArch64.SystemAccessTrap(EL2, 0x18); else X[t, 64] = CCSIDR2_EL1; elsif PSTATE.EL == EL2 then X[t, 64] = CCSIDR2_EL1; elsif PSTATE.EL == EL3 then X[t, 64] = CCSIDR2_EL1;
```