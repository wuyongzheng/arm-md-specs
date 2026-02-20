## F5.1.271 UDIV

Unsigned Divide divides a 32-bit unsigned integer register value by a 32-bit unsigned integer register value, and writes the result to the destination register. The condition flags are not affected.

See Divide instructions for more information about this instruction.

It has encodings from the following instruction sets: A32 (A1) and T32 (T1).

A1

<!-- image -->

## Encoding

UDIV{&lt;c&gt;}{&lt;q&gt;}

{&lt;Rd&gt;, }&lt;Rn&gt;, &lt;Rm&gt;

## Decode for this encoding

```
constant integer d = UInt(Rd); constant integer n = UInt(Rn); constant integer m = UInt(Rm); constant integer a = UInt(Ra); if d == 15 || n == 15 || m == 15 || a != 15 then
```

```
UNPREDICTABLE; end
```

## CONSTRAINED UNPREDICTABLE behavior

If Ra != '1111' , then one of the following behaviors must occur:

- The instruction is UNDEFINED.
- The instruction executes as NOP .
- The instruction executes as described, with no change to its behavior and no additional side effects.
- The instruction performs a divide and the register specified by Ra becomes UNKNOWN.

T1

<!-- image -->

<!-- image -->

Listing F5-86

## Decode for this encoding

```
constant integer d = UInt(Rd); constant integer n = UInt(Rn); constant integer m = UInt(Rm); constant integer a = UInt(Ra); // Armv8-A removes UNPREDICTABLE for R13 if d == 15 || n == 15 || m == 15 || a != 15 then UNPREDICTABLE; end
```

## CONSTRAINED UNPREDICTABLE behavior

If Ra != '1111' , then one of the following behaviors must occur:

- The instruction is UNDEFINED.
- The instruction executes as NOP .
- The instruction executes as described, with no change to its behavior and no additional side effects.
- The instruction performs a divide and the register specified by Ra becomes UNKNOWN.

For more information about the CONSTRAINED UNPREDICTABLE behavior of this instruction, see Architectural Constraints on UNPREDICTABLE behaviors.

## Assembler Symbols

&lt;c&gt;

See Standard assembler syntax fields.

See Standard assembler syntax fields.

Is the general-purpose destination register, encoded in the 'Rd' field.

&lt;q&gt;

&lt;Rd&gt;

&lt;Rn&gt;

Is the first general-purpose source register holding the dividend, encoded in the 'Rn' field.

## &lt;Rm&gt;

Is the second general-purpose source register holding the divisor, encoded in the 'Rm' field.

## Operation

```
if ConditionPassed() then EncodingSpecificOperations(); constant integer dividend constant integer divisor integer result; if divisor == 0 then result = 0; else result = dividend DIVRM divisor; end R[d] = result<31:0>; end
```

```
= UInt(R[n]); = UInt(R[m]);
```

Listing F5-88