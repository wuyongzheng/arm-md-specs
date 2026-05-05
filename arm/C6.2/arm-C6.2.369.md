## C6.2.369 SMAX (immediate)

Signed maximum (immediate)

This instruction determines the signed maximum of the source register value and immediate, and writes the result to the destination register.

## Integer

(FEAT\_CSSC)

<!-- image -->

## Encoding for the 32-bit variant

```
Applies when (sf == 0) SMAX <Wd>, <Wn>, #<simm>
```

## Encoding for the 64-bit variant

Applies when

```
(sf == 1) SMAX <Xd>, <Xn>, #<simm>
```

## Decode for all variants of this encoding

```
EndOfDecode(Decode_UNDEF);
```

```
if !IsFeatureImplemented(FEAT_CSSC) then constant integer d = UInt(Rd); constant integer n = UInt(Rn); constant integer datasize = 32 << UInt(sf); constant integer imm = SInt(imm8);
```

## Assembler Symbols

## &lt;Wd&gt;

Is the 32-bit name of the general-purpose destination register, encoded in the 'Rd' field.

## &lt;Wn&gt;

Is the 32-bit name of the general-purpose source register, encoded in the 'Rn' field.

## &lt;simm&gt;

Is a signed immediate, in the range -128 to 127, encoded in the 'imm8' field.

## &lt;Xd&gt;

## &lt;Xn&gt;

Is the 64-bit name of the general-purpose source register, encoded in the 'Rn' field.

## Operation

```
constant bits(datasize) operand1 = X[n, datasize]; constant integer result = Max(SInt(operand1), imm); X[d, datasize] = result<datasize-1:0>;
```

Is the 64-bit name of the general-purpose destination register, encoded in the 'Rd' field.

## Operational Information

This instruction is a data-independent-time instruction as described in About PSTATE.DIT.
