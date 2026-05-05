## C6.2.491 UMAX (immediate)

Unsigned maximum (immediate)

This instruction determines the unsigned maximum of the source register value and immediate, and writes the result to the destination register.

## Integer

(FEAT\_CSSC)

<!-- image -->

## Encoding for the 32-bit variant

```
Applies when (sf == 0) UMAX <Wd>, <Wn>, #<uimm>
```

## Encoding for the 64-bit variant

Applies when

```
(sf == 1) UMAX <Xd>, <Xn>, #<uimm>
```

## Decode for all variants of this encoding

```
EndOfDecode(Decode_UNDEF);
```

```
if !IsFeatureImplemented(FEAT_CSSC) then constant integer d = UInt(Rd); constant integer n = UInt(Rn); constant integer datasize = 32 << UInt(sf); constant integer imm = UInt(imm8);
```

## Assembler Symbols

## &lt;Wd&gt;

Is the 32-bit name of the general-purpose destination register, encoded in the 'Rd' field.

## &lt;Wn&gt;

Is the 32-bit name of the general-purpose source register, encoded in the 'Rn' field.

## &lt;uimm&gt;

Is an unsigned immediate, in the range 0 to 255, encoded in the 'imm8' field.

## &lt;Xd&gt;

## &lt;Xn&gt;

Is the 64-bit name of the general-purpose source register, encoded in the 'Rn' field.

## Operation

```
constant bits(datasize) operand1 = X[n, datasize]; constant integer result = Max(UInt(operand1), imm); X[d, datasize] = result<datasize-1:0>;
```

Is the 64-bit name of the general-purpose destination register, encoded in the 'Rd' field.

## Operational Information

This instruction is a data-independent-time instruction as described in About PSTATE.DIT.
