## C7.2.72 FCSEL

Floating-point conditional select (scalar)

This instruction allows the SIMD&amp;FP destination register to take the value from either one or the other of two SIMD&amp;FP source registers. If the condition passes, the first SIMD&amp;FP source register value is taken, otherwise the second SIMD&amp;FP source register value is taken.

Depending on the settings in the CPACR\_EL1, CPTR\_EL2, and CPTR\_EL3 registers, and the current Security state and Exception level, an attempt to execute the instruction might be trapped.

<!-- image -->

## Encoding for the Half-precision variant

```
(FEAT_FP16) Applies when (ftype
```

```
FCSEL <Hd>, <Hn>, <Hm>,
```

```
== 11) <cond>
```

## Encoding for the Single-precision variant

```
(FEAT_FP) Applies when (ftype == 00) FCSEL <Sd>, <Sn>, <Sm>, <cond>
```

## Encoding for the Double-precision variant

```
(FEAT_FP) Applies when (ftype == 01)
```

```
FCSEL <Dd>, <Dn>, <Dm>, <cond>
```

## Decode for all variants of this encoding

```
if !IsFeatureImplemented(FEAT_FP) then EndOfDecode(Decode_UNDEF); if ftype == '10' then EndOfDecode(Decode_UNDEF); if ftype == '11' && !IsFeatureImplemented(FEAT_FP16) then EndOfDecode(Decode_UNDEF); constant integer d = UInt(Rd); constant integer n = UInt(Rn); constant integer m = UInt(Rm); constant integer datasize = 8 << UInt(ftype EOR '10'); constant bits(4) condition = cond;
```

## Assembler Symbols

## &lt;Hd&gt;

Is the 16-bit name of the SIMD&amp;FP destination register, encoded in the 'Rd' field.

## &lt;Hn&gt;

Is the 16-bit name of the first SIMD&amp;FP source register, encoded in the 'Rn' field.

## &lt;Hm&gt;

Is the 16-bit name of the second SIMD&amp;FP source register, encoded in the 'Rm' field.

## &lt;cond&gt;

Is one of the standard conditions, encoded in the standard way, and encoded in 'cond':

|   cond | <cond>   |
|--------|----------|
|   0000 | EQ       |
|   0001 | NE       |
|   0010 | CS       |
|   0011 | CC       |
|   0100 | MI       |
|   0101 | PL       |
|   0110 | VS       |
|   0111 | VC       |
|   1000 | HI       |
|   1001 | LS       |
|   1010 | GE       |
|   1011 | LT       |
|   1100 | GT       |
|   1101 | LE       |
|   1110 | AL       |
|   1111 | NV       |

Is the 32-bit name of the SIMD&amp;FP destination register, encoded in the 'Rd' field.

- &lt;Sn&gt; Is the 32-bit name of the first SIMD&amp;FP source register, encoded in the 'Rn' field.

## &lt;Sm&gt;

Is the 32-bit name of the second SIMD&amp;FP source register, encoded in the 'Rm' field.

## &lt;Dd&gt;

## &lt;Dn&gt;

Is the 64-bit name of the first SIMD&amp;FP source register, encoded in the 'Rn' field.

## &lt;Dm&gt;

Is the 64-bit name of the second SIMD&amp;FP source register, encoded in the 'Rm' field.

## Operation

```
AArch64.CheckFPEnabled(); bits(datasize) result; constant boolean condition_holds = ConditionHolds(condition); result = if condition_holds then V[n, datasize] else V[m, datasize];
```

## &lt;Sd&gt;

Is the 64-bit name of the SIMD&amp;FP destination register, encoded in the 'Rd' field.

```
V[d, datasize] = result;
```

## Operational Information

This instruction is a data-independent-time instruction as described in About PSTATE.DIT.
