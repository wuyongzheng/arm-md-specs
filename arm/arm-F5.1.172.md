## F5.1.172 RSC, RSCS (register-shifted register)

Reverse Subtract (register-shifted register) subtracts a register value and the value of NOT (Carry flag) from a register-shifted register value, and writes the result to the destination register. It can optionally update the condition flags based on the result.

<!-- image -->

## Encoding for the Flag setting variant

```
Applies when (S == 1) RSCS{<c>}{<q>} {<Rd>, }<Rn>, <Rm>, <shift> <Rs>
```

## Encoding for the Not flag setting variant

```
Applies when
```

```
RSC{<c>}{<q>} {<Rd>, }<Rn>, <Rm>, <shift>
```

```
(S == 0) <Rs>
```

## Decode for all variants of this encoding

```
constant integer d = UInt(Rd); constant integer n = UInt(Rn); constant integer m = UInt(Rm); constant integer s = UInt(Rs); constant boolean setflags = (S == '1'); constant SRType shift_t = DecodeRegShift(stype); if d == 15 || n == 15 || m == 15 || s == 15 then
```

```
UNPREDICTABLE;
```

For more information about the CONSTRAINED UNPREDICTABLE behavior of this instruction, see Architectural Constraints on UNPREDICTABLE behaviors.

## Assembler Symbols

&lt;c&gt;

See Standard assembler syntax fields.

See Standard assembler syntax fields.

Is the general-purpose destination register, encoded in the 'Rd' field.

&lt;q&gt;

## &lt;Rd&gt;

&lt;Rn&gt;

Is the first general-purpose source register, encoded in the 'Rn' field.

## &lt;Rm&gt;

Is the second general-purpose source register, encoded in the 'Rm' field.

## &lt;shift&gt;

Is the type of shift to be applied to the second source register, encoded in 'stype':

|   stype | <shift>   |
|---------|-----------|
|      00 | LSL       |
|      01 | LSR       |
|      10 | ASR       |
|      11 | ROR       |

<!-- image -->

Is the third general-purpose source register holding a shift amount in its bottom 8 bits, encoded in the 'Rs' field.

## Operation

```
if ConditionPassed() then EncodingSpecificOperations(); constant integer shift_n = UInt(R[s]<7:0>); constant bits(32) shifted = Shift(R[m], shift_t, shift_n, PSTATE.C); bits(32) result; bits(4) nzcv; (result, nzcv) = AddWithCarry(NOT(R[n]), shifted, PSTATE.C); R[d] = result; if setflags then PSTATE.<N,Z,C,V> = nzcv;
```

## Operational Information

This instruction is a data-independent-time instruction as described in About the DIT bit.