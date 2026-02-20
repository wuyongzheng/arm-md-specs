## C7.1 About the A64 Advanced SIMD and floating-point instructions

Alphabetical list of A64 Advanced SIMD and floating-point instructions gives full descriptions of the A64 instructions that are in the following instruction groups:

- Loads and store instructions associated with the SIMD and floating-point registers.
- Data processing instructions with SIMD and floating-point registers.

A64 instruction set encoding in the A64 Instruction Encodings chapter provides an overview of the instruction encodings as part of an instruction class within a functional group.

The rest of this section is a general description of the SIMD and floating-point instructions. It contains the following subsections:

- Register size.
- Output element control.
- Data types.
- Condition flags and related instructions.

## C7.1.1 Register size

A64 provides a comprehensive set of packed Single Instruction Multiple Data (SIMD) and scalar operations using data held in the 32 entry 128-bit wide SIMD and floating-point register file.

Each SIMD and floating-point register can be used to hold:

- Asingle scalar value of the floating-point or integer type.
- A64-bit wide vector containing one or more elements.
- A128-bit wide vector containing two or more elements.

Where the entire 128-bit wide register is not fully utilized, the vector or scalar quantity is held in the least significant bits of the register, with the most significant bits being cleared to zero on a write, see Advanced SIMD vector formats.

The following instructions can insert data into individual elements within a SIMD and floating-pointer register without clearing the remaining bits to zero:

- Insert vector element from another vector element or general-purpose register, INS .
- Load structure into a single lane, for example LD3 .
- All second-part narrowing operations, for example SHRN2 .

## C7.1.2 Output element control

When FEAT\_AFP is implemented, the FPCR.NEP bit controls how output elements are determined for the scalar Advanced SIMD instructions for elements other than the lowest element of the vector.

If FPCR.NEP == 1, the following instructions determine output elements as follows:

- The 3-input floating-point scalar versions of FMLA (by element) and FMLS (by element) take output elements other than the lowest element from the &lt;Hd&gt;, &lt;Sd&gt;, or &lt;Dd&gt; register.
- The 3-input floating-point FMADD, FMSUB, FNMADD, and FNMSUB instructions take output elements other than the lowest element from the &lt;Ha&gt;, &lt;Sa&gt;, or &lt;Da&gt; register.
- The 2-input floating-point scalar versions of FCMGE (register), FCMGT (register), FCMEQ (register), FACGE, FACGT, take output elements other than the lowest element from the &lt;Hm&gt;, &lt;Sm&gt;, or &lt;Dm&gt; register.
- The 2-input floating-point scalar versions of FMULX, FRECPS, FRSQRTS, FABD, FMUL (by element), FMUL(scalar), FDIV (scalar), FADD (scalar), FSUB (scalar), FMAX (scalar), FMIN (scalar), FMAXNM (scalar), FMINNM (scalar), FNMUL (scalar), take output elements other than the lowest element from the &lt;Hn&gt;, &lt;Sn&gt;, or &lt;Dn&gt; register.

- For 1-input floating-point scalar versions of the instructions FCVTNS (vector), FCVTMS (vector), FCVTAS (vector), FCVTPS (vector), SCVTF (vector, integer), UCVTF (vector, integer) FCVTZS (vector, integer), FCVTZU (vector, integer), FCVTNU (vector), FCVTMU (vector), FCVTAU (vector), FCVTPU (vector), SCVTF (vector, fixed-point), UCVTF (vector, fixed-point), FCVTZS (vector, fixed-point), FCVTZU (vector, fixed-point), SCVTF (scalar, integer), UCVTF (scalar, integer), SCVTF (scalar, fixed-point), UCVTF (scalar, fixed-point), BFCVT, FCVT, FCVTXN , FRECPE, FRECPX, FRSQRTE, FABS (scalar), FNEG (scalar), FSQRT (scalar), FRINTN (scalar), FRINTP (scalar), FRINTM (scalar), FRINTZ (scalar), FRINTA (scalar), FRINTI (scalar), FRINTX (scalar), FRINT32Z (scalar), FRINT32X (scalar), FRINT64Z (scalar), FRINT64X (scalar), take output elements other than the lowest element from the &lt;Hd&gt;, &lt;Sd&gt;, or &lt;Dd&gt; register.

## C7.1.3 Data types

The A64 instruction set provides support for arithmetic, conversion, and bitwise operations on:

- Half-precision, single-precision, and double-precision floating-points.
- Signed and unsigned integers.
- Polynomials over {0, 1}.
- When FEAT\_FCMA is implemented, complex numbers.

For all AArch64 floating-point operations, including SIMD operations, the rounding mode and exception trap handling are controlled by the FPCR.

Note

- AArch32 Advanced SIMD operations always use Arm standard floating-point arithmetic, regardless of the rounding mode specified by the AArch64 FPCR or the AArch32 FPSCR.
- In AArch64 state, floating-point multiply-add operations are always performed as fused operations, but AArch32 state provides both fused and chained multiply-add instructions.

In addition to operations that consume and produce values of the same width and type, the A64 instruction set supports SIMD and scalar operations that produce a wider or narrower vector result:

- Where a SIMD operation narrows a 128-bit vector to a 64-bit vector, the A64 instruction set provides a second-part operation, for example SHRN2 , that can pack the result of a second operation into the upper part of the same destination register.
- Where a SIMD operation widens a 64-bit vector to a 128-bit vector, the A64 instruction set provides a second-part operation, for example SMLAL2 , that can extract the source from the upper 64 bits of the source registers.

All SIMD operations that could produce side-effects that are not limited to the destination SIMD and floating-point register, for example a potential update of FPSR.Q or FPSR.IDC, have a dedicated scalar variant to support the use of SIMD with loops requiring specialized head or tail handling, or both.

## C7.1.4 Condition flags and related instructions

The A64 instruction set provides support for flag setting and conditional operations on the SIMD and floating-point register file:

- Floating-point FCSEL and FCCMP instructions are equivalent to the integer CSEL and CCMP instructions.
- Floating-point FCMP , FCMPE , FCCMP , and FCCMP instructions set the PSTATE.{N, Z, C, V} flags based on the result of the floating-point comparison.
- Floating-point FJCVTZS instruction sets the PSTATE.Z flag if the result of the conversion, when converted back to a double-precision floating-point number, gives precisely the same value as the original. Other PSTATE flags are cleared by this instruction.
- Floating-point and integer instructions provide a means of producing either a scalar or a vector mask based on a comparison in a SIMD and floating-point register, for example FCMEQ .

Note

FCMP and FCMPE differ from the A32/T32 VCMP and VCMPE instructions, which use the dedicated FPSCR.NZCV field for the result. A64 instructions store the result of an FCMP or FCMPE operation in the PSTATE.{N, Z, C, V} field. If FEAT\_FlagM2 is implemented, base instructions XAFLAG and AXFLAG convert between the PSTATE condition flag format used by the FCMP instruction and an alternative format. See Table C6-1.