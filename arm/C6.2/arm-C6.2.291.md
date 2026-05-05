## C6.2.291 MSUBPT

## Multiply-subtract checked pointer

This instruction multiplies two register values, subtracts the product from a third register value, and writes the result to the destination register. The intermediate product is treated as the offset.

If the operation would have generated a result where the most significant 8 bits of the result register differ from the most significant 8 bits of the base register, then the result is modified such that it is likely to be non-canonical when used as an address.

If the intermediate product cannot be correctly represented as a 64-bit two's complement value, then the result is modified such that it is likely to be non-canonical when used as an address.

## Integer

(FEAT\_CPA)

<!-- image -->

## Encoding

```
MSUBPT <Xd>, <Xn>, <Xm>, <Xa>
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_CPA) then EndOfDecode(Decode_UNDEF);
```

```
constant integer d = UInt(Rd); constant integer n = UInt(Rn); constant integer m = UInt(Rm); constant integer a = UInt(Ra);
```

## Assembler Symbols

## &lt;Xd&gt;

Is the 64-bit name of the general-purpose destination register, encoded in the 'Rd' field.

## &lt;Xn&gt;

Is the 64-bit name of the first general-purpose source register holding the multiplicand, encoded in the 'Rn' field.

## &lt;Xm&gt;

Is the 64-bit name of the second general-purpose source register holding the multiplier, encoded in the 'Rm' field.

## &lt;Xa&gt;

Is the 64-bit name of the third general-purpose source register holding the minuend, encoded in the 'Ra' field.

## Operation

```
constant bits(64) operand1 = X[n, 64]; constant bits(64) operand2 = X[m, 64]; constant bits(64) operand3 = X[a, 64]; bits(64) result; constant integer product = SInt(operand1) *
```

```
SInt(operand2);
```

```
// Signed and unsigned twos complement arithmetic are equivalent if only a // fixed number of bits are considered. result = operand3 - product<63:0>; constant boolean overflow = (product != SInt(product<63:0>)); result = PointerMultiplyAddCheck(result, operand3, overflow); X[d, 64] = result;
```
