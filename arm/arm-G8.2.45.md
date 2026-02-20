## G8.2.45 DCISW, Data Cache line Invalidate by Set/Way

The DCISW characteristics are:

## Purpose

Invalidate data or unified cache line by set/way.

## Configuration

AArch32 System instruction DCISW bits [31:0] performs the same function as bits [31:0].

This system instruction is present only when FEAT\_AA32EL1 is implemented. Otherwise, direct accesses to DCISW are UNDEFINED.

## Attributes

DCISW is a 32-bit System instruction.

## Field descriptions

<!-- image -->

## SetWay, bits [31:4]

Contains two fields:

- Way, bits[31:32-A], the number of the way to operate on.
- Set, bits[B-1:L], the number of the set to operate on.

Bits[L-1:4] are RES0.

A=Log2(ASSOCIATIVITY), L = Log2(LINELEN), B = (L + S), S = Log2(NSETS).

ASSOCIATIVITY, LINELEN (line length, in bytes), and NSETS (number of sets) have their usual meanings and are the values for the cache level being operated on. The values of A and S are rounded up to the next integer.

## Level, bits [3:1]

Cache level to operate on, minus 1. For example, this field is 0 for operations on L1 cache, or 1 for operations on L2 cache.

## Bit [0]

Reserved, RES0.

## Executing DCISW

If this instruction is executed with a set, way or level argument that is larger than the value supported by the implementation then the behavior is CONSTRAINED UNPREDICTABLE and one of the following occurs:

- The instruction is UNDEFINED
- The instruction performs cache maintenance on one of:
- No cache lines.
- Asingle arbitrary cache line.
- Multiple arbitrary cache lines.

Accesses to this instruction use the following encodings in the System instruction encoding space:

MCR{&lt;c&gt;}{&lt;q&gt;} &lt;coproc&gt;, {#}&lt;opc1&gt;, &lt;Rt&gt;, &lt;CRn&gt;, &lt;CRm&gt;{, {#}&lt;opc2&gt;}

| coproc   | opc1   | CRn    | CRm    | opc2   |
|----------|--------|--------|--------|--------|
| 0b1111   | 0b000  | 0b0111 | 0b0110 | 0b010  |

```
if !IsFeatureImplemented(FEAT_AA32EL1) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && HSTR_EL2.T7 == '1' ↪ → then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HSTR.T7 == '1' ↪ → then AArch32.TakeHypTrapException(0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && HCR_EL2.TSW == ↪ → '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HCR.TSW == '1' ↪ → then AArch32.TakeHypTrapException(0x03); else AArch32.DC(R[t], CacheOp_Invalidate, CacheOpScope_SetWay); elsif PSTATE.EL == EL2 then AArch32.DC(R[t], CacheOp_Invalidate, CacheOpScope_SetWay); elsif PSTATE.EL == EL3 then AArch32.DC(R[t], CacheOp_Invalidate, CacheOpScope_SetWay);
```