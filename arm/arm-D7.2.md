## D7.2 Address space

The architecture is designed to support a wide range of applications with different memory requirements. It supports a range of physical address (PA) sizes, and provides associated control and identification mechanisms. For more information, see Implemented physical address size.

## D7.2.1 Virtual address space overflow

When a PE performs a Simple sequential execution of instructions, it calculates:

(address\_of\_current\_instruction) + (size\_of\_executed\_instruction)

This calculation is performed after each instruction to determine which instruction to execute next.

If the address calculation performed after executing an instruction overflows 0xFFFF\_FFFF\_FFFF\_FFFF , the program counter becomes UNKNOWN. Similarly, if the address calculation based on the program counter for the value of the link register or exception link register overflows 0xFFFF\_FFFF\_FFFF\_FFFF , then those registers also become UNKNOWN.

Note

Address tags are not propagated to the program counter, so the tag does not affect the address calculation.

Where an instruction accesses a sequential set of bytes that crosses the 0xFFFF\_FFFF\_FFFF\_FFFF boundary when tagged addresses are not used, or the 0xXXFF\_FFFF\_FFFF\_FFFF boundary when tagged addresses are used, then the virtual address accessed for the bytes above this boundary is UNKNOWN.

The UNKNOWN virtual address behavior also applies to the set of bytes addressed by SVE and SME predicated, contiguous loads and stores that cross the 0xFFFF\_FFFF\_FFFF\_FFFF boundary, even if all of the virtual addresses below the boundary correspond to Inactive elements. Conversely, for SVE gather loads and scatter stores, the UNKNOWN address behavior applies only to accesses corresponding to an individual Active element that crosses the boundary.

When tagged addresses are used, the value of the tag associated with the address also becomes UNKNOWN.

Note

The behaviors described in this section apply only for the upper bound of the upper V A range, in translation regimes that have two VA ranges. They do not apply for address calculations relating to the top of the lower V A range.