## C6.2.304 PACGA

Pointer Authentication Code, using generic key

This instruction computes the Pointer Authentication Code for a 64-bit value in the first source register, using a modifier in the second source register, and the generic key. The computed Pointer Authentication Code is written to the most significant 32 bits of the destination register, and the least significant 32 bits of the destination register are set to zero.

## Integer

(FEAT\_PAuth)

<!-- image -->

## Encoding

```
PACGA <Xd>, <Xn>,
```

```
<Xm|SP>
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_PAuth) then EndOfDecode(Decode_UNDEF); boolean source_is_sp = FALSE; constant integer d = UInt(Rd); constant integer n = UInt(Rn); constant integer m = UInt(Rm); if m == 31 then source_is_sp = TRUE;
```

## Assembler Symbols

&lt;Xd&gt;

Is the 64-bit name of the general-purpose destination register, encoded in the 'Rd' field.

&lt;Xn&gt;

Is the 64-bit name of the first general-purpose source register, encoded in the 'Rn' field.

## &lt;Xm|SP&gt;

Is the 64-bit name of the second general-purpose source register or stack pointer, encoded in the 'Rm' field.

## Operation

```
if source_is_sp then X[d, 64] = AddPACGA(X[n, 64], SP[64]); else X[d, 64] = AddPACGA(X[n, 64], X[m, 64]);
```
