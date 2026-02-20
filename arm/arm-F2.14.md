## F2.14 Floating-point data-processing instructions

Table F2-31 summarizes the data-processing instructions in the floating-point instruction set. In this table, floating-point register means a register in the SIMD and floating-point register file. The BFloat16 floating-point instructions are provided by FEAT\_AA32BF16.

For details of the floating-point arithmetic used by floating-point instructions, see Floating-point support.

Table F2-31 Floating-point data-processing instructions

| Instruction                                                                                                   | See                                                          |
|---------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------|
| BFloat16 convert from single-precision to BFloat16 format writing to bottom half of single-precision register | VCVTB(BFloat16)                                              |
| BFloat16 convert from single-precision to BFloat16 format writing to top half of single-precision register    | VCVTT(BFloat16)                                              |
| Convert between double-precision and single-precision                                                         | VCVT(between double-precision and single-precision)          |
| Convert between floating-point and fixed-point                                                                | VCVT(between floating-point and fixed-point, floating-point) |
| Convert between half-precision and single-precision, writing to bottom half of single-precision register      | VCVTB                                                        |
| Convert between half-precision and single-precision, writing to top half of single-precision register         | VCVTT                                                        |
| Convert from floating-point to integer                                                                        | VCVT(floating-point to integer, floating-point)              |
| Convert from floating-point to integer using FPSCR rounding mode                                              | VCVTR                                                        |
| Convert from integer to floating-point                                                                        | VCVT(integer to floating-point, floating-point)              |
| Floating-point Javascript convert to signed fixed-point, rounding toward zero                                 | VJCVT                                                        |
| Copy from one floating-point register to another                                                              | VMOV(register)                                               |
| Divide                                                                                                        | VDIV                                                         |
| Move immediate value to a floating-point register                                                             | VMOV(immediate)                                              |
| Square Root                                                                                                   | VSQRT                                                        |
| Vector Absolute value                                                                                         | VABS                                                         |
| Vector Add                                                                                                    | VADD(floating-point)                                         |
| Vector Compare with exceptions disabled                                                                       | VCMPE                                                        |
| Vector Compare with exceptions enabled                                                                        | VCMP                                                         |
| Vector Fused Multiply Accumulate                                                                              | VFMA                                                         |
| Vector Fused Multiply Subtract                                                                                | VFMS                                                         |
| Vector Fused Negate Multiply Accumulate                                                                       | VFNMA                                                        |
| Vector Fused Negate Multiply Subtract                                                                         | VFNMS                                                        |
| Vector Multiply                                                                                               | VMUL(floating-point)                                         |
| Vector Multiply Accumulate                                                                                    | VMLA(floating-point)                                         |
| Vector Multiply Subtract                                                                                      | VMLS(floating-point)                                         |
| Vector Negate Multiply                                                                                        | VNMUL                                                        |
| Vector Negate Multiply Accumulate                                                                             | VNMLA                                                        |
| Vector Negate Multiply Subtract                                                                               | VNMLS                                                        |

| Instruction                              | See                  |
|------------------------------------------|----------------------|
| Vector Negate, by inverting the sign bit | VNEG                 |
| Vector Subtract                          | VSUB(floating-point) |

## Chapter F3 T32 Instruction Set Encoding

This chapter describes the encoding of the T32 instruction set. It contains the following sections:

- T32 instruction set encoding.
- About the T32 Advanced SIMD and floating-point instructions and their encoding.

## In this chapter:

- In the decode tables, an entry of x for a field value means the value of the field does not affect the decoding.
- In the decode diagrams, a shaded field indicates that the bits in that field are not used in that level of decode.