## F5.1.62 LDAEXD

Load-Acquire Exclusive Doubleword loads a doubleword from memory, writes it to two registers and:

- If the address has the Shared Memory attribute, marks the physical address as exclusive access for the executing PE in a global monitor
- Causes the executing PE to indicate an active exclusive access in the local monitor.

The instruction also acts as a barrier instruction with the ordering requirements described in Load-Acquire, Store-Release.

For more information about support for shared memory see Synchronization and semaphores. For information about memory accesses see Memory accesses.

It has encodings from the following instruction sets: A32 (A1) and T32 (T1).

A1

<!-- image -->

## Encoding

```
LDAEXD{<c>}{<q>} <Rt>, <Rt2>, [<Rn>]
```

## Decode for this encoding

```
constant integer t = UInt(Rt); constant integer t2 = t + 1; constant integer n = UInt(Rn); if Rt<0> == '1' || t2 == 15 || n == 15 then
```

```
UNPREDICTABLE;
```

## CONSTRAINED UNPREDICTABLE behavior

If Rt&lt;0&gt; == '1' , then one of the following behaviors must occur:

- The instruction is UNDEFINED.
- The instruction executes as NOP .
- The instruction executes with the additional decode: t&lt;0&gt; = '0'.
- The instruction executes with the additional decode: t2 = t.
- The instruction executes as described, with no change to its behavior and no additional side effects.

If Rt == '1110' , then one of the following behaviors must occur:

- The instruction is UNDEFINED.
- The instruction executes as NOP .
- The instruction is handled as described in Using R15.

T1

<!-- image -->

## Encoding

```
LDAEXD{<c>}{<q>} <Rt>, <Rt2>, [<Rn>]
```

## Decode for this encoding

```
constant integer t = UInt(Rt); constant integer t2 = UInt(Rt2); constant integer n = UInt(Rn); if t == 15 || t2 == 15 || t == t2 || n == 15 then
```

```
UNPREDICTABLE;
```

## CONSTRAINED UNPREDICTABLE behavior

If t == t2 , then one of the following behaviors must occur:

- The instruction is UNDEFINED.
- The instruction executes as NOP .
- The load instruction executes but the destination register takes an UNKNOWN value.

For more information about the CONSTRAINED UNPREDICTABLE behavior of this instruction, see Architectural Constraints on UNPREDICTABLE behaviors.

## Assembler Symbols

<!-- image -->

See Standard assembler syntax fields.

See Standard assembler syntax fields.

For the 'A1' variant: is the first general-purpose register to be transferred, encoded in the 'Rt' field. &lt;Rt&gt; must be even-numbered and not R14.

For the 'T1' variant: is the first general-purpose register to be transferred, encoded in the 'Rt' field.

## &lt;Rt2&gt;

For the 'A1' variant: is the second general-purpose register to be transferred. &lt;Rt2&gt; must be &lt;R(t+1)&gt; .

For the 'T1' variant: is the second general-purpose register to be transferred, encoded in the 'Rt2' field.

Is the general-purpose base register, encoded in the 'Rn' field.

<!-- image -->

## &lt;Rt&gt;

<!-- image -->

&lt;Rn&gt;

## Operation

```
if ConditionPassed() then EncodingSpecificOperations(); constant bits(32) address = R[n]; AArch32.SetExclusiveMonitors(address, 8); constant bits(64) value = MemO[address, 8]; // Extract words from 64-bit loaded value such that R[t] is // loaded from address and R[t2] from address+4. R[t] = if BigEndian(AccessType_GPR) then value<63:32> else value<31:0>; R[t2] = if BigEndian(AccessType_GPR) then value<31:0> else value<63:32>;
```

## Operational Information

This instruction is a data-independent-time instruction as described in About the DIT bit.