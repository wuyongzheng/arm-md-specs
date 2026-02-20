## F5.1.35 CMN (register-shifted register)

Compare Negative (register-shifted register) adds a register value and a register-shifted register value. It updates the condition flags based on the result, and discards the result.

<!-- image -->

## Encoding

```
CMN{<c>}{<q>} <Rn>, <Rm>, <type> <Rs>
```

## Decode for this encoding

```
constant integer n = UInt(Rn); constant integer m = UInt(Rm); constant integer s = UInt(Rs); constant SRType shift_t = DecodeRegShift(stype); if n == 15 || m == 15 || s == 15 then UNPREDICTABLE;
```

For more information about the CONSTRAINED UNPREDICTABLE behavior, see Architectural Constraints on UNPREDICTABLE behaviors.

## Assembler Symbols

&lt;c&gt;

See Standard assembler syntax fields.

See Standard assembler syntax fields.

&lt;q&gt;

## &lt;Rn&gt;

Is the first general-purpose source register, encoded in the 'Rn' field.

## &lt;Rm&gt;

Is the second general-purpose source register, encoded in the 'Rm' field.

## &lt;type&gt;

Is the type of shift to be applied to the second source register, encoded in 'stype':

|   stype | <type>   |
|---------|----------|
|      00 | LSL      |
|      01 | LSR      |
|      10 | ASR      |
|      11 | ROR      |

Is the third general-purpose source register holding a shift amount in its bottom 8 bits, encoded in the 'Rs' field.

<!-- image -->

&lt;Rs&gt;

## Operation

```
if ConditionPassed() then EncodingSpecificOperations(); constant integer shift_n = UInt(R[s]<7:0>); constant bits(32) shifted = Shift(R[m], shift_t, shift_n, PSTATE.C); bits(32) result; bits(4) nzcv; (result, nzcv) = AddWithCarry(R[n], shifted, '0'); PSTATE.<N,Z,C,V> = nzcv;
```

## Operational Information

This instruction is a data-independent-time instruction as described in About the DIT bit.