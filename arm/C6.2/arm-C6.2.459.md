## C6.2.459 SUBP

Subtract pointer

This instruction subtracts the 56-bit address held in the second source register from the 56-bit address held in the first source register, sign-extends the result to 64 bits, and writes the result to the destination register.

## Integer

(FEAT\_MTE)

<!-- image -->

## Encoding

```
SUBP <Xd>, <Xn|SP>, <Xm|SP>
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_MTE) then EndOfDecode(Decode_UNDEF);
```

```
constant integer d = UInt(Rd); constant integer n = UInt(Rn); constant integer m = UInt(Rm);
```

## Assembler Symbols

## &lt;Xd&gt;

Is the 64-bit name of the general-purpose destination register, encoded in the 'Rd' field.

## &lt;Xn|SP&gt;

Is the 64-bit name of the first source general-purpose register or stack pointer, encoded in the 'Rn' field.

## &lt;Xm|SP&gt;

Is the 64-bit name of the second general-purpose source register or stack pointer, encoded in the 'Rm' field.

## Operation

```
bits(64) operand1 = if n == 31 then SP[64] else X[n, 64]; bits(64) operand2 = if m == 31 then SP[64] else X[m, 64]; operand1 = SignExtend(operand1<55:0>, 64); operand2 = NOT(SignExtend(operand2<55:0>, 64)); bits(64) result; (result, -) = AddWithCarry(operand1, operand2, '1'); X[d, 64] = result;
```
