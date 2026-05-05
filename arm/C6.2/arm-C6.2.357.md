## C6.2.357 SETF8, SETF16

Evaluation of 8-bit or 16-bit flag values

This instruction sets the PSTATE.NZV flags based on the value in the specified general-purpose register. SETF8 treats the value as an 8-bit value. SETF16 treats the value as a 16-bit value.

The PSTATE.C flag is not affected by these instructions.

## Integer

(FEAT\_FlagM)

<!-- image -->

## Encoding for the SETF8 variant

```
Applies when (sz == 0) SETF8 <Wn>
```

## Encoding for the SETF16 variant

```
Applies when (sz ==
```

```
1) SETF16 <Wn>
```

## Decode for all variants of this encoding

```
if !IsFeatureImplemented(FEAT_FlagM) then constant integer size = 8 << UInt(sz); constant integer n = UInt(Rn);
```

## Assembler Symbols

## &lt;Wn&gt;

Is the 32-bit name of the general-purpose source register, encoded in the 'Rn' field.

## Operation

```
constant bits(32) reg = X[n, 32]; PSTATE.N = reg<size-1>; PSTATE.Z = if (reg<size-1:0> == Zeros(size)) then '1' else '0'; PSTATE.V = reg<size> EOR reg<size-1>; //PSTATE.C unchanged;
```

## Operational Information

This instruction is a data-independent-time instruction as described in About PSTATE.DIT.

```
EndOfDecode(Decode_UNDEF);
```
