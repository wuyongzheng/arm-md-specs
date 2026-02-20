## C9.2.280 SUNPK

Unpack and sign-extend multi-vector elements

This instruction unpacks elements from one or two source vectors and then sign-extends them to place in elements of twice their size within the two or four destination vectors.

This instruction is unpredicated.

It has encodings from 2 classes: Two registers and Four registers

```
Two registers
```

(FEAT\_SME2)

<!-- image -->

## Encoding

```
SUNPK { <Zd1>.<T>-<Zd2>.<T> }, <Zn>.<Tb>
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SME2) then EndOfDecode(Decode_UNDEF); if size == '00' then EndOfDecode(Decode_UNDEF); constant integer esize = 8 << UInt(size); constant integer n = UInt(Zn); constant integer d = UInt(Zd:'0'); constant integer nreg = 2; constant boolean unsigned = FALSE;
```

```
Four registers (FEAT_SME2)
```

<!-- image -->

## Encoding

```
SUNPK { <Zd1>.<T>-<Zd4>.<T> }, { <Zn1>.<Tb>-<Zn2>.<Tb> }
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SME2) then if size == '00' then EndOfDecode(Decode_UNDEF); constant integer esize = 8 << UInt(size); constant integer n = UInt(Zn:'0'); constant integer d = UInt(Zd:'00'); constant integer nreg = 4; constant boolean unsigned = FALSE;
```

```
EndOfDecode(Decode_UNDEF);
```

U

## Assembler Symbols

## &lt;Zd1&gt;

For the 'Two registers' variant: is the name of the first scalable vector register of the destination multi-vector group, encoded as 'Zd' times 2.

For the 'Four registers' variant: is the name of the first scalable vector register of the destination multi-vector group, encoded as 'Zd' times 4.

Is the size specifier, encoded in 'size':

## &lt;Zd2&gt;

Is the name of the second scalable vector register of the destination multi-vector group, encoded as 'Zd' times 2 plus 1.

## &lt;Zn&gt;

## &lt;Tb&gt;

## &lt;T&gt;

|   size | <T>      |
|--------|----------|
|     00 | RESERVED |
|     01 | H        |
|     10 | S        |
|     11 | D        |

Is the name of the source scalable vector register, encoded in the 'Zn' field.

Is the size specifier, encoded in 'size':

## &lt;Zd4&gt;

Is the name of the fourth scalable vector register of the destination multi-vector group, encoded as 'Zd' times 4 plus 3.

## &lt;Zn1&gt;

Is the name of the first scalable vector register of the source multi-vector group, encoded as 'Zn' times 2.

## &lt;Zn2&gt;

Is the name of the second scalable vector register of the source multi-vector group, encoded as 'Zn' times 2 plus 1.

|   size | <Tb>     |
|--------|----------|
|     00 | RESERVED |
|     01 | B        |
|     10 | H        |
|     11 | S        |

## Operation

```
CheckStreamingSVEEnabled(); constant integer VL = CurrentVL; constant integer elements = VL DIV esize; constant integer hsize = esize DIV 2; constant integer sreg = nreg DIV 2; array [0..3] of bits(VL) results; for r = 0 to sreg-1 constant bits(VL) operand = Z[n+r, VL]; for i = 0 to 1 for e = 0 to elements-1 constant bits(hsize) element = Elem[operand, i*elements + e, hsize]; Elem[results[2*r+i], e, esize] = Extend(element, esize, unsigned); for r = 0 to nreg-1 Z[d+r, VL] = results[r];
```

## Operational Information

This instruction is a data-independent-time instruction as described in About PSTATE.DIT.