## C6.2.302 PACDA, PACDZA

Pointer Authentication Code for data address, using key A

This instruction computes and inserts a Pointer Authentication Code for a data address, using a modifier and key A.

The address is in the general-purpose register that is specified by &lt;Xd&gt; .

The modifier is:

- In the general-purpose register or stack pointer that is specified by &lt;Xn|SP&gt; for PACDA .
- The value zero, for PACDZA .

## Integer

(FEAT\_PAuth)

<!-- image -->

## Encoding for the PACDA variant

```
(Z == 0)
```

```
Applies when PACDA <Xd>, <Xn|SP>
```

## Encoding for the PACDZA variant

```
Applies when (Z == 1 && Rn == 11111)
```

PACDZA

&lt;Xd&gt;

## Decode for all variants of this encoding

```
EndOfDecode(Decode_UNDEF);
```

```
if !IsFeatureImplemented(FEAT_PAuth) then boolean source_is_sp = FALSE; constant integer d = UInt(Rd); constant integer n = UInt(Rn); if Z == '0' then // PACDA if n == 31 then source_is_sp = TRUE; else // PACDZA if n != 31 then EndOfDecode(Decode_UNDEF);
```

## Assembler Symbols

## &lt;Xd&gt;

Is the 64-bit name of the general-purpose destination register, encoded in the 'Rd' field.

## &lt;Xn|SP&gt;

Is the 64-bit name of the general-purpose source register or stack pointer, encoded in the 'Rn' field.

## Operation

```
if source_is_sp then X[d, 64] = AddPACDA(X[d, 64], SP[64]); else X[d, 64] = AddPACDA(X[d, 64], X[n, 64]);
```
