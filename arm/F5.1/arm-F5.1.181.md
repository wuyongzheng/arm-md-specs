## F5.1.181 SDIV

Signed Divide divides a 32-bit signed integer register value by a 32-bit signed integer register value, and writes the result to the destination register. The condition flags are not affected.

It has encodings from the following instruction sets: A32 (A1) and T32 (T1).

A1

<!-- image -->

## Encoding

SDIV{&lt;c&gt;}{&lt;q&gt;}

{&lt;Rd&gt;, }&lt;Rn&gt;, &lt;Rm&gt;

## Decode for this encoding

```
constant integer d = UInt(Rd); constant integer n = UInt(Rn); constant integer m = UInt(Rm); constant integer a = UInt(Ra);
```

```
if d == 15 || n == 15 || m == 15 || a != 15 then UNPREDICTABLE; end
```

## CONSTRAINED UNPREDICTABLE behavior

If Ra != '1111' , then one of the following behaviors must occur:

- The instruction is UNDEFINED.
- The instruction executes as NOP .
- The instruction executes as described, with no change to its behavior and no additional side effects.
- The instruction executes as described, and the register specified by Ra becomes UNKNOWN.

T1

<!-- image -->

## Encoding

SDIV{&lt;c&gt;}{&lt;q&gt;}

{&lt;Rd&gt;, }&lt;Rn&gt;, &lt;Rm&gt;

## Decode for this encoding

```
constant integer d = UInt(Rd); constant integer n = UInt(Rn); constant integer m = UInt(Rm); constant integer a = UInt(Ra); // Armv8-A removes UNPREDICTABLE for R13 if d == 15 || n == 15 || m == 15 || a != 15 then UNPREDICTABLE; end
```

Listing F5-66

Listing F5-67

## CONSTRAINED UNPREDICTABLE behavior

If Ra != '1111' , then one of the following behaviors must occur:

- The instruction is UNDEFINED.
- The instruction executes as NOP .
- The instruction executes as described, with no change to its behavior and no additional side effects.
- The instruction executes as described, and the register specified by Ra becomes UNKNOWN.

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

Overflow

If the signed integer division 0x80000000 / 0xFFFFFFFF is performed, the pseudocode produces the intermediate integer result +2 31 , that overflows the 32-bit signed integer range. No indication of this overflow case is produced, and the 32-bit result written to &lt;Rd&gt; must be the bottom 32 bits of the binary representation of +2 31 . So the result of the division is 0x80000000 .

## Operation

```
if ConditionPassed() then EncodingSpecificOperations(); constant integer dividend = SInt(R[n]); constant integer divisor = SInt(R[m]); integer result; if divisor == 0 then result = 0; elsif (dividend < 0) == (divisor < 0) then result = Abs(dividend) DIVRM Abs(divisor); // same signs - positive result else result = -(Abs(dividend) DIVRM Abs(divisor)); // different signs - negative result end R[d] = result<31:0>; end
```

Listing F5-68