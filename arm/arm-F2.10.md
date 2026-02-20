## F2.10 System register access instructions

The System register encoding space is indexed using the parameters { coproc , opc1 , CRn , CRm , opc2 }, see The AArch32 System register interface. This encoding space provides System registers and System instructions. The only permitted values of coproc are 0b1110 and 0b1111 , and the following instructions give access to this encoding space:

- Instructions that transfer data between general-purpose registers and System registers. See:
- -MCR.
- -MCRR.
- -MRC.
- -MRRC.
- Instructions that load or store from memory to a System register. See:
- -LDC(immediate).
- -LDC(literal).
- -STC.

Note

The System register encoding space with coproc == 0b101x is redefined to provide some of the Advanced SIMD and floating-point functionality. That is, to:

- Initiate a floating-point data-processing operation, see Floating-point data-processing instructions.
- Transfer data between general-purpose registers and the Advanced SIMD and floating-point registers, see Advanced SIMD and floating-point register transfer instructions.
- Load or store data to the Advanced SIMD and floating-point registers, see Advanced SIMD and floating-point load/store instructions.

System register access instructions are part of the instruction stream executed by the PE, and therefore any System register access instruction that cannot be executed by the implementation causes an Undefined Instruction exception. In the A-profile and the R-profile architectures, the instruction encodings in the System register access instruction encoding space are unallocated, and generate Undefined Instruction exceptions, except for:

- The instructions summarized in this section that access the coproc == 0b111x encoding space.
- The instructions in the coproc == 0b101x encoding space that are redefined to provide Advanced SIMD and floating-point functionality, as summarized in the Note in this section.