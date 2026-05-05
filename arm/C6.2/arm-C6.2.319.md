## C6.2.319 PSSBB

Physical speculative store bypass barrier

This instruction is a memory barrier that prevents speculative loads from bypassing earlier stores to the same physical address under certain conditions. For more information and details of the semantics, see Physical Speculative Store Bypass Barrier (PSSBB).

This is an alias of DSB. This means:

- The encodings in this description are named to match the encodings of DSB.
- The description of DSB gives the operational pseudocode, any CONSTRAINED UNPREDICTABLE behavior, and any operational information for this instruction.

<!-- image -->

## Encoding

| PSSBB            |
|------------------|
| is equivalent to |
| DSB #4           |

and is always the preferred disassembly.

## Operation

The description of DSB gives the operational pseudocode for this instruction.
