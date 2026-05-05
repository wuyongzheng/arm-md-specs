## C7.2.236 LUTI2

Lookup table read with 2-bit indices

This instruction copies indexed 8-bit or 16-bit elements from the table vector to the destination vector using packed 2-bit indices from a segment of the source vector. A segment corresponds to a portion of the source vector that is consumed in order to fill the destination vector. The segment is selected by the vector segment index.

## Advanced SIMD

(FEAT\_AdvSIMD &amp;&amp; FEAT\_LUT)

<!-- image -->

## Encoding for the Byte variant

Applies when (op2 == 10 &amp;&amp; op ==

```
1)
```

```
LUTI2 <Vd>.16B, { <Vn>.16B },
```

```
<Vm>[<index>]
```

## Encoding for the Halfword variant

```
Applies when (op2 == 11) LUTI2 <Vd>.8H, { <Vn>.8H },
```

```
<Vm>[<index>]
```

## Decode for all variants of this encoding

```
if !IsFeatureImplemented(FEAT_AdvSIMD) || !IsFeatureImplemented(FEAT_LUT) EndOfDecode(Decode_UNDEF); if op2 == '10' && op == '0' then EndOfDecode(Decode_UNDEF); constant integer d = UInt(Rd); constant integer n = UInt(Rn); constant integer m = UInt(Rm); constant integer isize = 2; constant integer esize = if op2 == '10' then 8 else 16; constant integer part = if op2 == '10' then UInt(len) else UInt(len:op);
```

## Assembler Symbols

## &lt;Vd&gt;

Is the name of the SIMD&amp;FP destination register, encoded in the 'Rd' field.

## &lt;Vn&gt;

Is the name of the SIMD&amp;FP table register, encoded in the 'Rn' field.

## &lt;Vm&gt;

Is the name of the SIMD&amp;FP source register, encoded in the 'Rm' field.

## &lt;index&gt;

For the 'Byte' variant: is the vector segment index, in the range 0 to 3, encoded in the 'len' field.

For the 'Halfword' variant: is the vector segment index, in the range 0 to 7, encoded in the 'len:op' fields.

```
then
```

## Operation

```
AArch64.CheckFPAdvSIMDEnabled(); constant integer elements = 128 DIV esize; constant integer ibase = elements * part; constant bits(128) indices = V[m, 128]; constant bits(128) table = V[n, 128]; bits(128) result; for e = 0 to elements-1 constant integer index = UInt(Elem[indices, ibase + Elem[result, e, esize] = Elem[table, index, esize]; V[d, 128] = result;
```

## Operational Information

This instruction is a data-independent-time instruction as described in About PSTATE.DIT.

```
e, isize]);
```
