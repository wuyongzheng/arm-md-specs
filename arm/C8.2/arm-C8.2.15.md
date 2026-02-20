## C8.2.15 ADR

Compute vector address

This instruction optionally sign-extends or zero-extends the least significant 32 bits of each element from a vector of offsets or indices in the second source vector, and scales each index by 2, 4, or 8. The scaled indices are then added to a vector of base addresses from the first source vector, and the resulting addresses are placed in the destination vector. This instruction is unpredicated.

This instruction is illegal when executed in Streaming SVE mode, unless FEAT\_SME\_FA64 is implemented and enabled.

It has encodings from 3 classes: Packed offsets, Unpacked 32-bit signed offsets, and Unpacked 32-bit unsigned offsets

## Packed offsets

(FEAT\_SVE)

<!-- image -->

## Encoding

```
ADR <Zd>.<T>, [<Zn>.<T>, <Zm>.<T>{, <mod> <amount>}]
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SVE) then EndOfDecode(Decode_UNDEF); constant integer esize = 32 << UInt(sz); constant integer n = UInt(Zn); constant integer m = UInt(Zm); constant integer d = UInt(Zd); constant integer osize = esize; constant boolean unsigned = TRUE; constant integer mbytes = 1 << UInt(msz);
```

## Unpacked 32-bit signed offsets

(FEAT\_SVE)

<!-- image -->

## Encoding

```
ADR <Zd>.D, [<Zn>.D, <Zm>.D, SXTW{<amount>}]
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SVE) then EndOfDecode(Decode_UNDEF);
```

```
constant integer esize = 64; constant integer n = UInt(Zn); constant integer m = UInt(Zm); constant integer d = UInt(Zd); constant integer osize = 32; constant boolean unsigned = FALSE; constant integer mbytes = 1 << UInt(msz);
```

## Unpacked 32-bit unsigned offsets

(FEAT\_SVE)

<!-- image -->

## Encoding

```
ADR <Zd>.D, [<Zn>.D, <Zm>.D, UXTW{<amount>}]
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SVE) then EndOfDecode(Decode_UNDEF); constant integer esize = 64; constant integer n = UInt(Zn); constant integer m = UInt(Zm); constant integer d = UInt(Zd); constant integer osize = 32; constant boolean unsigned = TRUE; constant integer mbytes = 1 << UInt(msz);
```

## Assembler Symbols

&lt;Zd&gt;

Is the name of the destination scalable vector register, encoded in the 'Zd' field.

Is the size specifier, encoded in 'sz':

<!-- image -->

## &lt;Zn&gt;

|   sz | <T>   |
|------|-------|
|    0 | S     |
|    1 | D     |

Is the name of the base scalable vector register, encoded in the 'Zn' field.

## &lt;Zm&gt;

Is the name of the offset scalable vector register, encoded in the 'Zm' field.

## &lt;mod&gt;

Is the index extend and shift specifier, encoded in 'msz':

## &lt;amount&gt;

Is the index shift amount, encoded in 'msz':

## Operation

```
CheckNonStreamingSVEEnabled(); constant integer VL = CurrentVL; constant integer elements = VL DIV esize; constant bits(VL) base = Z[n, VL]; constant bits(VL) offs = Z[m, VL]; bits(VL) result; for e = 0 to elements-1 constant bits(esize) addr = Elem[base, e, esize]; constant bits(osize) offselt = Elem[offs, e, esize]<osize-1:0>; constant integer offset = if unsigned then UInt(offselt) else SInt(offselt); Elem[result, e, esize] = addr + (offset * mbytes); Z[d, VL] = result;
```

## Operational Information

This instruction is a data-independent-time instruction as described in About PSTATE.DIT.

| msz   | <mod>    |
|-------|----------|
| 00    | [absent] |
| x1    | LSL      |
| 10    | LSL      |

|   msz | <amount>   |
|-------|------------|
|    00 | [absent]   |
|    01 | #1         |
|    10 | #2         |
|    11 | #3         |