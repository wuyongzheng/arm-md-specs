## C6.2.492 UMAX (register)

Unsigned maximum (register)

This instruction determines the unsigned maximum of the two source register values and writes the result to the destination register.

## Integer

(FEAT\_CSSC)

<!-- image -->

## Encoding for the 32-bit variant

Applies when (sf == 0)

```
UMAX <Wd>, <Wn>, <Wm>
```

## Encoding for the 64-bit variant

Applies when (sf == 1)

```
UMAX
```

```
<Xd>, <Xn>, <Xm>
```

## Decode for all variants of this encoding

```
EndOfDecode(Decode_UNDEF);
```

```
if !IsFeatureImplemented(FEAT_CSSC) then constant integer d = UInt(Rd); constant integer n = UInt(Rn); constant integer m = UInt(Rm); constant integer datasize = 32 << UInt(sf);
```

## Assembler Symbols

## &lt;Wd&gt;

Is the 32-bit name of the general-purpose destination register, encoded in the 'Rd' field.

## &lt;Wn&gt;

Is the 32-bit name of the first general-purpose source register, encoded in the 'Rn' field.

## &lt;Wm&gt;

Is the 32-bit name of the second general-purpose source register, encoded in the 'Rm' field.

## &lt;Xd&gt;

## &lt;Xn&gt;

Is the 64-bit name of the first general-purpose source register, encoded in the 'Rn' field.

## &lt;Xm&gt;

Is the 64-bit name of the second general-purpose source register, encoded in the 'Rm' field.

Is the 64-bit name of the general-purpose destination register, encoded in the 'Rd' field.

## Operation

```
constant bits(datasize) operand1 = X[n, datasize]; constant bits(datasize) operand2 = X[m, datasize]; constant integer result = X[d, datasize] = result<datasize-1:0>;
```

## Operational Information

This instruction is a data-independent-time instruction as described in About PSTATE.DIT.

```
Max(UInt(operand1), UInt(operand2));
```
