## F5.1.84 LDREXB

Load Register Exclusive Byte derives an address from a base register value, loads a byte from memory, zero-extends it to form a 32-bit word, writes it to a register and:

- If the address has the Shared Memory attribute, marks the physical address as exclusive access for the executing PE in a global monitor.
- Causes the executing PE to indicate an active exclusive access in the local monitor.

For more information about support for shared memory see Synchronization and semaphores. For information about memory accesses see Memory accesses.

It has encodings from the following instruction sets: A32 (A1) and T32 (T1).

A1

<!-- image -->

## Encoding

```
LDREXB{<c>}{<q>} <Rt>, [<Rn>]
```

## Decode for this encoding

```
constant integer t = UInt(Rt); constant integer n = UInt(Rn); if t == 15 || n == 15 then UNPREDICTABLE;
```

T1

<!-- image -->

## Encoding

```
LDREXB{<c>}{<q>} <Rt>, [<Rn>]
```

## Decode for this encoding

```
constant integer t = UInt(Rt); constant integer n = UInt(Rn); // Armv8-A removes UNPREDICTABLE for R13 if t == 15 || n == 15 then UNPREDICTABLE;
```

For more information about the CONSTRAINED UNPREDICTABLE behavior of this instruction, see Architectural Constraints on UNPREDICTABLE behaviors.

## Assembler Symbols

&lt;c&gt;

See Standard assembler syntax fields.

See Standard assembler syntax fields.

Is the general-purpose register to be transferred, encoded in the 'Rt' field.

&lt;q&gt;

&lt;Rt&gt;

&lt;Rn&gt;

Is the general-purpose base register, encoded in the 'Rn' field.

## Operation

```
if ConditionPassed() then AArch32.SetExclusiveMonitors(address,1);
```

```
EncodingSpecificOperations(); constant bits(32) address = R[n]; R[t] = ZeroExtend(MemA[address,1], 32);
```

## Operational Information

This instruction is a data-independent-time instruction as described in About the DIT bit.