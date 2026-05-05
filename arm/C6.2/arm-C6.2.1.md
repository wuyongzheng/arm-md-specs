## C6.2.1 ABS

Absolute value

This instruction computes the absolute value of the signed integer value in the source register, and writes the result to the destination register.

## Integer

(FEAT\_CSSC)

<!-- image -->

## Encoding for the 32-bit variant

Applies when (sf == 0)

```
ABS <Wd>, <Wn>
```

## Encoding for the 64-bit variant

Applies when (sf == 1)

```
ABS <Xd>, <Xn>
```

## Decode for all variants of this encoding

```
EndOfDecode(Decode_UNDEF);
```

```
if !IsFeatureImplemented(FEAT_CSSC) then constant integer datasize = 32 << UInt(sf); constant integer d = UInt(Rd); constant integer n = UInt(Rn);
```

## Assembler Symbols

## &lt;Wd&gt;

Is the 32-bit name of the general-purpose destination register, encoded in the 'Rd' field.

## &lt;Wn&gt;

Is the 32-bit name of the general-purpose source register, encoded in the 'Rn' field.

## &lt;Xd&gt;

## &lt;Xn&gt;

Is the 64-bit name of the general-purpose source register, encoded in the 'Rn' field.

## Operation

```
constant bits(datasize) operand1 = constant integer result = Abs(SInt(operand1)); X[d, datasize] = result<datasize-1:0>;
```

## Operational Information

This instruction is a data-independent-time instruction as described in About PSTATE.DIT.

Is the 64-bit name of the general-purpose destination register, encoded in the 'Rd' field.

```
X[n, datasize];
```
