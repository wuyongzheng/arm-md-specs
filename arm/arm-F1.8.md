## F1.8 Additional pseudocode support for instruction descriptions

Earlier sections of this chapter include pseudocode that describes features of the execution of T32 and A32 instructions, see:

- Pseudocode description of conditional execution.
- Pseudocode description of instruction-specified shifts and rotates

The following subsection gives additional pseudocode support functions for some of the instructions described in Alphabetical list of T32 and A32 base instruction set instructions. See also Pseudocode support for the banked register transfer instructions.

## F1.8.1 Pseudocode description of operations for System register access instructions

The AArch32.SysRegRead() function obtains the word for an MRC instruction from the System register.

The AArch32.SysRegRead64() function obtains the two words for an MRRC instruction from the System register.

Note

The relative significance of the two words returned is IMPLEMENTATION DEFINED, but all uses within this manual present the two words in the order (most significant, least significant).

The AArch32.SysRegWrite() procedure sends the word for an MCR instruction to the System register.

The AArch32.SysRegWrite64() procedure sends the two words for an MCRR instruction to the System register.

Note

The relative significance of word2 and word1 is IMPLEMENTATION DEFINED, but all uses within this manual treat word2 as more significant than word1 .

## F1.8.2 Pseudocode details of system calls

The AArch32.CallSupervisor() pseudocode function generates a Supervisor Call exception. Valid execution of the SVC instruction calls this function.

The AArch32.CallHypervisor() pseudocode function generates an HVC exception. Valid execution of the HVC instruction calls this function.