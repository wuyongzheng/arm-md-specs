## C6.2.352 SBCS

Subtract with carry, setting flags

This instruction subtracts a register value and the value of NOT (Carry flag) from a register value, and writes the result to the destination register. It updates the condition flags based on the result.

This instruction is used by the alias NGCS.

<!-- image -->

## Encoding for the 32-bit variant

Applies when (sf == 0)

```
SBCS <Wd>, <Wn>, <Wm>
```

## Encoding for the 64-bit variant

Applies when (sf == 1)

```
SBCS <Xd>, <Xn>, <Xm>
```

## Decode for all variants of this encoding

```
constant integer d = UInt(Rd); constant integer n = UInt(Rn); constant integer m = UInt(Rm); constant integer datasize = 32 <<
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

```
UInt(sf);
```

Is the 64-bit name of the general-purpose destination register, encoded in the 'Rd' field.

## Alias Conditions

## Operation

```
constant bits(datasize) operand1 = X[n, datasize]; constant bits(datasize) operand2 = NOT(X[m, datasize]); bits(datasize) result; bits(4) nzcv; (result, nzcv) = AddWithCarry(operand1, operand2, PSTATE.C); X[d, datasize] = result; PSTATE.<N,Z,C,V> = nzcv;
```

## Operational Information

This instruction is a data-independent-time instruction as described in About PSTATE.DIT.

| Alias   | Is preferred when   |
|---------|---------------------|
| NGCS    | Rn == '11111'       |
