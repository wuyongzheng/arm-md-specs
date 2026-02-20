## F5.1.83 LDREX

Load Register Exclusive calculates an address from a base register value and an immediate offset, loads a word from memory, writes it to a register and:

- If the address has the Shared Memory attribute, marks the physical address as exclusive access for the executing PE in a global monitor.
- Causes the executing PE to indicate an active exclusive access in the local monitor.

For more information about support for shared memory see Synchronization and semaphores. For information about memory accesses see Memory accesses.

It has encodings from the following instruction sets: A32 (A1) and T32 (T1).

A1

<!-- image -->

## Encoding

```
LDREX{<c>}{<q>} <Rt>, [<Rn> {, {#}<imm>}]
```

## Decode for this encoding

```
constant integer t = UInt(Rt); constant integer n = UInt(Rn); constant bits(32) imm32 = Zeros(32); // Zero offset if t == 15 || n == 15 then UNPREDICTABLE;
```

T1

<!-- image -->

## Encoding

```
LDREX{<c>}{<q>} <Rt>, [<Rn> {, #<imm>}]
```

## Decode for this encoding

```
constant integer t = UInt(Rt); constant integer n = UInt(Rn); constant bits(32) imm32 = ZeroExtend(imm8:'00', 32); // Armv8-A removes UNPREDICTABLE for R13 if t == 15 || n == 15 then UNPREDICTABLE;
```

For more information about the CONSTRAINED UNPREDICTABLE behavior of this instruction, see Architectural Constraints on UNPREDICTABLE behaviors.

## Assembler Symbols

&lt;c&gt;

See Standard assembler syntax fields.

See Standard assembler syntax fields.

Is the general-purpose register to be transferred, encoded in the 'Rt' field.

&lt;q&gt;

## &lt;Rt&gt;

## &lt;Rn&gt;

Is the general-purpose base register, encoded in the 'Rn' field.

## &lt;imm&gt;

For the 'A1' variant: the immediate offset added to the value of &lt;Rn&gt; to calculate the address. &lt;imm&gt; can only be 0 or omitted.

For the 'T1' variant: the immediate offset added to the value of &lt;Rn&gt; to calculate the address. &lt;imm&gt; can be omitted, meaning an offset of 0. Values are multiples of 4 in the range 0-1020.

## Operation

```
if ConditionPassed() then EncodingSpecificOperations(); constant bits(32) address = R[n] + imm32; AArch32.SetExclusiveMonitors(address,4); R[t] = MemA[address,4];
```

## Operational Information

This instruction is a data-independent-time instruction as described in About the DIT bit.