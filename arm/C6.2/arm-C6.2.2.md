## C6.2.2 ADC

## Add with carry

This instruction adds two register values and the Carry flag value, and writes the result to the destination register.

<!-- image -->

## Encoding for the 32-bit variant

Applies when (sf ==

```
ADC
```

```
0) <Wd>, <Wn>, <Wm>
```

## Encoding for the 64-bit variant

Applies when (sf == 1)

```
ADC
```

```
<Xd>, <Xn>, <Xm>
```

## Decode for all variants of this encoding

```
constant integer d = UInt(Rd); constant integer n = UInt(Rn); constant integer m = UInt(Rm); constant integer datasize = 32 << UInt(sf);
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
constant bits(datasize) operand1 = X[n, datasize]; constant bits(datasize) operand2 = X[m, datasize]; bits(datasize) result; (result, -) = AddWithCarry(operand1, operand2, PSTATE.C); X[d, datasize] = result;
```

## Operational Information

This instruction is a data-independent-time instruction as described in About PSTATE.DIT.
