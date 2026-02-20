## C8.2.504 PFALSE

Set all predicate elements to false

This instruction sets all elements in the destination predicate to false.

For programmer convenience, an assembler must also accept predicate-as-counter register name for the destination predicate register.

## SVE

(FEAT\_SVE || FEAT\_SME)

<!-- image -->

## Encoding

```
PFALSE <Pd>.B
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SVE) && !IsFeatureImplemented(FEAT_SME) then
```

```
EndOfDecode(Decode_UNDEF); constant integer d = UInt(Pd);
```

## Assembler Symbols

&lt;Pd&gt;

Is the name of the destination scalable predicate register, encoded in the 'Pd' field.

## Operation

```
CheckSVEEnabled(); constant integer VL = CurrentVL; constant integer PL = VL DIV 8; P[d, PL] = Zeros(PL);
```