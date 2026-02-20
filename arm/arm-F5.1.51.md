## F5.1.51 EOR, EORS (register-shifted register)

Bitwise Exclusive-OR (register-shifted register) performs a bitwise exclusive-OR of a register value and a register-shifted register value. It writes the result to the destination register, and can optionally update the condition flags based on the result.

<!-- image -->

## Encoding for the Flag setting variant

Applies when

```
EORS{<c>}{<q>} {<Rd>, }<Rn>, <Rm>, <shift>
```

```
(S == 1) <Rs>
```

## Encoding for the Not flag setting variant

```
Applies when (S == 0) EOR{<c>}{<q>} {<Rd>, }<Rn>, <Rm>, <shift> <Rs>
```

## Decode for all variants of this encoding

```
constant integer d = UInt(Rd); constant integer n = UInt(Rn); constant integer m = UInt(Rm); constant integer s = UInt(Rs); constant boolean setflags = (S == '1'); constant SRType shift_t = DecodeRegShift(stype); if d == 15 || n == 15 || m == 15 || s == 15 then
```

```
UNPREDICTABLE;
```

For more information about the CONSTRAINED UNPREDICTABLE behavior, see Architectural Constraints on UNPREDICTABLE behaviors.

## Assembler Symbols

&lt;c&gt;

See Standard assembler syntax fields.

See Standard assembler syntax fields.

Is the general-purpose destination register, encoded in the 'Rd' field.

&lt;q&gt;

&lt;Rd&gt;

&lt;Rn&gt;

Is the first general-purpose source register, encoded in the 'Rn' field.

&lt;Rm&gt;

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
if ConditionPassed() then EncodingSpecificOperations(); constant integer shift_n = UInt(R[s]<7:0>); bits(32) shifted; bit carry; (shifted, carry) = Shift_C(R[m], shift_t, shift_n, PSTATE.C); constant bits(32) result = R[n] EOR shifted; R[d] = result; if setflags then PSTATE.N = result<31>; PSTATE.Z = IsZeroBit(result); PSTATE.C = carry; // PSTATE.V unchanged
```

## Operational Information

This instruction is a data-independent-time instruction as described in About the DIT bit.