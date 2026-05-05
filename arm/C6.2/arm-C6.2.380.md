## C6.2.380 SSBB

Speculative store bypass barrier

This instruction is a memory barrier that prevents speculative loads from bypassing earlier stores to the same virtual address under certain conditions. For more information and details of the semantics, see Speculative Store Bypass Barrier (SSBB).

This is an alias of DSB. This means:

- The encodings in this description are named to match the encodings of DSB.
- The description of DSB gives the operational pseudocode, any CONSTRAINED UNPREDICTABLE behavior, and any operational information for this instruction.

<!-- image -->

## Encoding

| SSBB             |
|------------------|
| is equivalent to |
| DSB #0           |

and is always the preferred disassembly.

## Operation

The description of DSB gives the operational pseudocode for this instruction.
