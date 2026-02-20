## F5.1.261 TEQ (register-shifted register)

Test Equivalence (register-shifted register) performs a bitwise exclusive-OR operation on a register value and a register-shifted register value. It updates the condition flags based on the result, and discards the result.

<!-- image -->

## Encoding

```
TEQ{<c>}{<q>} <Rn>, <Rm>, <type> <Rs>
```

## Decode for this encoding

```
constant integer n = UInt(Rn); constant integer m = UInt(Rm); constant integer s = UInt(Rs); constant SRType shift_t = DecodeRegShift(stype); if n == 15 || m == 15 || s == 15 then
```

```
UNPREDICTABLE;
```

For more information about the CONSTRAINED UNPREDICTABLE behavior of this instruction, see Architectural Constraints on UNPREDICTABLE behaviors.

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
if ConditionPassed() then EncodingSpecificOperations(); constant integer shift_n = UInt(R[s]<7:0>); bits(32) shifted; bit carry; (shifted, carry) = Shift_C(R[m], shift_t, shift_n, constant bits(32) result = R[n] EOR shifted; PSTATE.N = result<31>; PSTATE.Z = IsZeroBit(result); PSTATE.C = carry; // PSTATE.V unchanged
```

## Operational Information

This instruction is a data-independent-time instruction as described in About the DIT bit.

```
PSTATE.C);
```