## C7.2.237 LUTI4

Lookup table read with 4-bit indices

This instruction copies indexed 8-bit or 16-bit elements from the one or two table vectors to the destination vector using packed 4-bit indices from a segment of the source vector. A segment corresponds to a portion of the source vector that is consumed in order to fill the destination vector. The segment is selected by the vector segment index.

## Advanced SIMD

(FEAT\_AdvSIMD &amp;&amp; FEAT\_LUT)

<!-- image -->

## Encoding for the Byte variant

Applies when (len == x1 &amp;&amp; op ==

```
0)
```

```
LUTI4 <Vd>.16B, { <Vn>.16B },
```

```
<Vm>[<index>]
```

## Encoding for the Halfword variant

```
Applies when (op == 1)
```

```
LUTI4 <Vd>.8H, { <Vn1>.8H, <Vn2>.8H },
```

## Decode for all variants of this encoding

```
if !IsFeatureImplemented(FEAT_AdvSIMD) || !IsFeatureImplemented(FEAT_LUT) EndOfDecode(Decode_UNDEF); if len<0> == '0' && op == '0' then EndOfDecode(Decode_UNDEF); constant integer d = UInt(Rd); constant integer n = UInt(Rn); constant integer m = UInt(Rm); constant integer isize = 4; constant integer esize = 8 << UInt(op); constant integer ntblr = 1 << UInt(op); constant integer part = if op == '0' then UInt(len<1>) else UInt(len);
```

## Assembler Symbols

&lt;Vd&gt;

Is the name of the SIMD&amp;FP destination register, encoded in the 'Rd' field.

&lt;Vn&gt;

Is the name of the SIMD&amp;FP table register, encoded in the 'Rn' field.

## &lt;Vm&gt;

Is the name of the SIMD&amp;FP source register, encoded in the 'Rm' field.

## &lt;index&gt;

For the 'Byte' variant: is the vector segment index, in the range 0 to 1, encoded in the 'len&lt;1&gt;' field.

For the 'Halfword' variant: is the vector segment index, in the range 0 to 3, encoded in the 'len' field.

```
<Vm>[<index>]
```

```
then
```

## &lt;Vn1&gt;

Is the name of the first SIMD&amp;FP table register, encoded in the 'Rn' field.

&lt;Vn2&gt;

Is the name of the second SIMD&amp;FP table register, encoded as 'Rn' plus 1 modulo 32.

## Operation

```
AArch64.CheckFPAdvSIMDEnabled(); constant integer elements = 128 DIV esize; constant integer ibase = elements * part; constant bits(128) indices = V[m, 128]; constant bits(128) table1 = V[n+0, 128]; constant bits(128) table2 = if ntblr == 2 then V[(n+1) MOD 32, 128] else Zeros(128); bits(128) result; bits(esize) res; for e = 0 to elements-1 constant integer index = UInt(Elem[indices, ibase + e, isize]); if index < elements then res = Elem[table1, index, esize]; else assert ntblr == 2; res = Elem[table2, index -elements, esize]; Elem[result, e, esize] = res; V[d, 128] = result;
```

## Operational Information

This instruction is a data-independent-time instruction as described in About PSTATE.DIT.
