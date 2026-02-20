## F1.5 Memory accesses

Commonly, the following addressing modes are permitted for memory access instructions:

## Offset addressing

The offset value is applied to an address obtained from the base register. The result is used as the address for the memory access. The value of the base register is unchanged.

The assembly language syntax for this mode is:

[&lt;Rn&gt;, &lt;offset&gt;]

## Pre-indexed addressing

The offset value is applied to an address obtained from the base register. The result is used as the address for the memory access, and written back into the base register.

The assembly language syntax for this mode is:

[&lt;Rn&gt;, &lt;offset&gt;]!

## Post-indexed addressing

The address obtained from the base register is used, unchanged, as the address for the memory access. The offset value is applied to the address, and written back into the base register

The assembly language syntax for this mode is:

[&lt;Rn&gt;], &lt;offset&gt;

In each case, &lt;Rn&gt; is the base register. &lt;offset&gt; can be:

- An immediate constant, such as &lt;imm8&gt; or &lt;imm12&gt; .
- An index register, &lt;Rm&gt;.
- Ashifted index register, such as &lt;Rm&gt;, LSL #&lt;shift&gt; .

For information about unaligned access, endianness, and exclusive access, see:

- Alignment support.
- Endian support.
- Synchronization and semaphores.