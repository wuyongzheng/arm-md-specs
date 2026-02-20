## C4.1 A64 instruction set encoding

| 31 30   | 29 28   | 25 24   |
|---------|---------|---------|
| op0     | op1     |         |

| op0   | op1   | Instruction details                                       |
|-------|-------|-----------------------------------------------------------|
| 0     | 0000  | Reserved                                                  |
| 1     | 0000  | SMEencodings                                              |
| x     | 0010  | SVE encodings                                             |
| x     | 00x1  | UNALLOCATED                                               |
| x     | 100x  | Data Processing - Immediate                               |
| x     | 101x  | Branches, Exception Generating and System instructions    |
| x     | x101  | Data Processing - Register                                |
| x     | x111  | Data Processing - Scalar Floating-Point and Advanced SIMD |
| x     | x1x0  | Loads and Stores                                          |

## Reserved

## SME encodings

## Reserved

The encodings in this section are decoded from A64 instruction set encoding.

<!-- image -->

|   31 | 30   | 29 28   | 25 24   |
|------|------|---------|---------|
|    0 | op0  | 0 0 0 0 | op1     |

| op0   | op1          | Instruction details   |
|-------|--------------|-----------------------|
| 00    | 000000000    | UDF                   |
| 00    | != 000000000 | UNALLOCATED           |
| != 00 | xxxxxxxxx    | UNALLOCATED           |

## SMEencodings

The encodings in this section are decoded from A64 instruction set encoding.

<!-- image -->

|   31 | 30 29   | 25 24   | 10 9 6 5   |
|------|---------|---------|------------|
|    1 | op0     | 0 op1   | op2        |

| op0   | op1             | op2    | Instruction details                                 |
|-------|-----------------|--------|-----------------------------------------------------|
| 00    | x00xxxxx0x00000 | 0xx0xx | SME2 Quarter Tile Outer Product - 16-bit and 32-bit |
| 00    | x00xxxxx0x00000 | 1xx0xx | UNALLOCATED                                         |
| 00    | x00xxxxx0x00001 | xxx0xx | UNALLOCATED                                         |
| 00    | x00xxxxx0x0001x | xxx0xx | UNALLOCATED                                         |
| 00    | x00xxxxx0x001xx | xxx0xx | UNALLOCATED                                         |
| 00    | x00xxxxx0x01xxx | xxx0xx | UNALLOCATED                                         |
| 00    | x00xxxxx1x0xxxx | xxx0xx | UNALLOCATED                                         |
| 00    | x01xxxxxxx0xxxx | xxx0xx | SME2 Sparse Outer Product                           |
| 00    | x0xxxxxxxx0xxxx | xxx1xx | UNALLOCATED                                         |
| 00    | x0xxxxxxxx1xxxx | xxxxxx | UNALLOCATED                                         |
| 00    | x10xxxxxxxxxxxx | xx00xx | SMEFPOuter Product - 32 bit                         |
| 00    | x10xxxxxxxxxxxx | xx10xx | SME2 Outer Product - Misc                           |
| 01    | 00xxxxxxxxxxxxx | xxxxxx | SME2 Multi-vector - Memory (Contiguous)             |
| 01    | 10xxxxxxxxxxxxx | xxxxxx | SME2 Multi-vector - Memory (Strided)                |
| 01    | x10xxxxxxxxxxxx | xxx0xx | SMEInteger Outer Product - 32 bit                   |
| 0x    | x10xxxxxxxxxxxx | xxx1xx | UNALLOCATED                                         |
| 0x    | x11xxxxx0000000 | 0x1xxx | SME2 Quarter Tile Outer Product - 64-bit            |
| 0x    | x11xxxxx0000000 | 1x1xxx | UNALLOCATED                                         |
| 0x    | x11xxxxx0000001 | xx1xxx | UNALLOCATED                                         |
| 0x    | x11xxxxx000001x | xx1xxx | UNALLOCATED                                         |
| 0x    | x11xxxxx00001xx | xx1xxx | UNALLOCATED                                         |
| 0x    | x11xxxxx0001xxx | xx1xxx | UNALLOCATED                                         |
| 0x    | x11xxxxx001xxxx | xx1xxx | UNALLOCATED                                         |
| 0x    | x11xxxxx01xxxxx | xx1xxx | UNALLOCATED                                         |
| 0x    | x11xxxxx1xxxxxx | xx1xxx | UNALLOCATED                                         |
| 0x    | x11xxxxxxxxxxxx | xx0xxx | SMEOuter Product - 64 bit                           |
| 10    | 0000010xxxxxxxx | xxxxxx | SMEzero array                                       |
| 10    | 0000011xxxxxxxx | xxxxxx | SME2 Multiple Zero                                  |
| 10    | 0010010xxxxxxxx | xxxxxx | SME2 zero lookup table                              |
| 10    | 0010011xxxxxxxx | xxxxxx | SME2 Move Lookup Table                              |
| 10    | 00x011xxxxxxxxx | xxxxxx | UNALLOCATED                                         |
| 10    | 010011xxxxxxxxx | xxxxxx | SME2 Expand Lookup Table (Non- contiguous)          |

|   op0 | op1             | op2    | Instruction details                                                           |
|-------|-----------------|--------|-------------------------------------------------------------------------------|
|    10 | 011011xxxxxxxxx | xxxxxx | UNALLOCATED                                                                   |
|    10 | 01x001xxxxxxxxx | xxxxxx | SME2Expand Lookup Table (Contiguous)                                          |
|    10 | 0xx000x0xxxxxxx | x0xxxx | SMEMove into Array                                                            |
|    10 | 0xx000x0xxxxxxx | x1xxxx | UNALLOCATED                                                                   |
|    10 | 0xx000x1xxxxxxx | xxxxxx | SMEMove from Array                                                            |
|    10 | 0xx010xxxxxxxxx | xx0xxx | SMEAddVector to Array                                                         |
|    10 | 0xx010xxxxxxxxx | xx1xxx | UNALLOCATED                                                                   |
|    10 | 0xx1xxxxxxxxxxx | xxxxxx | UNALLOCATED                                                                   |
|    10 | 10x10xxxx0xxxxx | xxxxxx | SME2 Multi-vector - Multiple and Single Array Vectors (Two registers)         |
|    10 | 10x11xxxx0xxxxx | xxxxxx | SME2 Multi-vector - Multiple and Single Array Vectors (Four registers)        |
|    10 | 11x1xxxx00xxxxx | xxxxxx | SME2 Multi-vector - Multiple Array Vectors (Two registers)                    |
|    10 | 11x1xxxx10xxxxx | xxxxxx | SME2 Multi-vector - Multiple Array Vectors (Four registers)                   |
|    10 | 1xx00xxxxxxxxxx | xxxxxx | SME2 Multi-vector - Indexed (One register)                                    |
|    10 | 1xx01xxxx0xxxxx | xxxxxx | SME2 Multi-vector - Indexed (Two registers)                                   |
|    10 | 1xx01xxxx1xxxxx | xxxxxx | SME2 Multi-vector - Indexed (Four registers)                                  |
|    10 | 1xx10xxxx10100x | xxxxxx | SME2 Multi-vector - Multiple and Single SVE Destructive (Two registers)       |
|    10 | 1xx10xxxx10101x | xxxx0x | SME2 Multi-vector - Multiple and Single SVE Destructive (Four registers)      |
|    10 | 1xx10xxxx10101x | xxxx1x | UNALLOCATED                                                                   |
|    10 | 1xx11xxxx1010xx | xxxxxx | UNALLOCATED                                                                   |
|    10 | 1xx1xxx00101110 | xxxx0x | SME2 Multi-vector - Multiple Vectors SVE Destructive (Four registers)         |
|    10 | 1xx1xxx00101111 | xxxx0x | SME2 Multi-vector - Multiple Vectors SVE Saturating Multiply (Four registers) |
|    10 | 1xx1xxx0010111x | xxxx1x | UNALLOCATED                                                                   |
|    10 | 1xx1xxx1010111x | xxxxxx | UNALLOCATED                                                                   |
|    10 | 1xx1xxxx0101100 | xxxxxx | SME2 Multi-vector - Multiple Vectors SVE Destructive (Two registers)          |
|    10 | 1xx1xxxx0101101 | xxxxxx | SME2 Multi-vector - Multiple Vectors SVE Saturating Multiply (Two registers)  |
|    10 | 1xx1xxxx01111xx | xxxxxx | UNALLOCATED                                                                   |
|    10 | 1xx1xxxx11x11xx | xxxxxx | UNALLOCATED                                                                   |
|    10 | 1xx1xxxxx100xxx | xxxxxx | SME2 Multi-vector - SVE Select                                                |
|    10 | 1xx1xxxxx110xxx | xxxxxx | SME2 Multi-vector - SVE Constructive Binary                                   |
|    10 | 1xx1xxxxx111000 | xxxxxx | SME2 Multi-vector - SVE Constructive Unary                                    |

|   op0 | op1             | op2    | Instruction details                           |
|-------|-----------------|--------|-----------------------------------------------|
|    10 | 1xx1xxxxx111001 | 0xxxx0 | SME2 Multi-vector - FP Multiply               |
|    10 | 1xx1xxxxx111001 | 0xxxx1 | UNALLOCATED                                   |
|    10 | 1xx1xxxxx111001 | 1xxxxx | UNALLOCATED                                   |
|    10 | 1xx1xxxxx111010 | 0xxxx0 | SME2 Multiple and Single Vector - FP multiply |
|    10 | 1xx1xxxxx111010 | 0xxxx1 | UNALLOCATED                                   |
|    10 | 1xx1xxxxx111010 | 1xxxxx | UNALLOCATED                                   |
|    10 | 1xx1xxxxx111011 | xxxxxx | UNALLOCATED                                   |
|    11 | xxxxxxxxxxxxxxx | xxxxxx | SMEMemory                                     |

## SME2 Quarter Tile Outer Product - 16-bit and 32-bit

SME2 Quarter Tile Outer Product - 16-bit and 32-bit

The encodings in this section are decoded from SME encodings.

<!-- image -->

| 31    | 25 24 23 22 21 20             | 17 16 15 14 10 9 6 5 4 3 2 1   |
|-------|-------------------------------|--------------------------------|
| 1 0 0 | 0 op0 0 0 op1 0 op2 0 0 0 0 0 | 0 op3 0 op4                    |

| op0   | op1   |   op2 | op3   | op4   | Instruction details                               |
|-------|-------|-------|-------|-------|---------------------------------------------------|
| 0     | 0     |     0 | x0    | x     | SME2 FP32 non-widening quarter tile outer product |
| 0     | 0     |     0 | x1    | 0     | UNALLOCATED                                       |
| 0     | 1     |     0 | 00    | x     | SME2 FP8 to FP32 quarter tile outer product       |
| 0     | 1     |     0 | 01    | 0     | SME2 FP8 to FP16 quarter tile outer product       |
| 0     | 1     |     0 | 10    | 1     | UNALLOCATED                                       |
| 0     | 1     |     0 | 1x    | 0     | UNALLOCATED                                       |
| 1     | 0     |     0 | x0    | x     | SME2 BF16 to FP32 quarter tile outer product      |
| 1     | 0     |     0 | x1    | 0     | SME2 FP16 non-widening quarter tile outer product |
| 1     | 1     |     0 | x0    | x     | SME2 FP16 to FP32 quarter tile outer product      |
| 1     | 1     |     0 | x1    | 0     | SME2 BF16 non-widening quarter tile outer product |
| x     | 0     |     1 | x1    | x     | SME2 Int16 to Int32 quarter tile outer product    |
| x     | 1     |     1 | x1    | x     | UNALLOCATED                                       |
| x     | x     |     0 | x1    | 1     | UNALLOCATED                                       |
| x     | x     |     1 | x0    | x     | SME2 Int8 to Int32 quarter tile outer product     |

## SME2 FP32 non-widening quarter tile outer product

The encodings in this section are decoded from SME2 Quarter Tile Outer Product - 16-bit and 32-bit.

<!-- image -->

| 31   | 25 24 23 22 21 20 19 17 16 15 14 10   |
|------|---------------------------------------|
| 1 0  | 0 0 0 0 0 M Zm 0 0 0 0 0 0 0          |

|   M |   N |   S | Instruction Details                                          |    |                 | Feature       |
|-----|-----|-----|--------------------------------------------------------------|----|-----------------|---------------|
|   0 |   0 |   0 | FMOP4A (non-widening) precision, single vectors              | -  | Single-         | FEAT_SME_MOP4 |
|   0 |   0 |   1 | FMOP4S (non-widening) precision, single vectors              | -  | Single-         | FEAT_SME_MOP4 |
|   0 |   1 |   0 | FMOP4A (non-widening) precision, multiple and single vectors | -  | Single-         | FEAT_SME_MOP4 |
|   0 |   1 |   1 | FMOP4S (non-widening) precision, multiple and single         | -  | Single- vectors | FEAT_SME_MOP4 |
|   1 |   0 |   0 | FMOP4A (non-widening) precision, single and multiple vectors | -  | Single-         | FEAT_SME_MOP4 |
|   1 |   0 |   1 | FMOP4S (non-widening) precision, single and multiple vectors | -  | Single-         | FEAT_SME_MOP4 |
|   1 |   1 |   0 | FMOP4A (non-widening) precision, multiple vectors            | -  | Single-         | FEAT_SME_MOP4 |
|   1 |   1 |   1 | FMOP4S (non-widening) precision, multiple vectors            | -  | Single-         | FEAT_SME_MOP4 |

## SME2 FP8 to FP32 quarter tile outer product

The encodings in this section are decoded from SME2 Quarter Tile Outer Product - 16-bit and 32-bit.

| 31   | 25 24 23 22 21 20 19 17 16 15 14 10 9   |
|------|-----------------------------------------|
| 1 0  | 0 0 0 0 1 M Zm 0 0 0 0 0 0 0 N          |

|   M |   N | Instruction Details                                    | Feature                        |
|-----|-----|--------------------------------------------------------|--------------------------------|
|   0 |   0 | FMOP4A (widening, 4-way) - Single vectors              | FEAT_SME_MOP4 &&FEAT_SME_F8F32 |
|   0 |   1 | FMOP4A (widening, 4-way) - Multiple and single vectors | FEAT_SME_MOP4 &&FEAT_SME_F8F32 |

|   M |   N | Instruction Details                                  | Feature                        |
|-----|-----|------------------------------------------------------|--------------------------------|
|   1 |   0 | FMOP4A(widening, 4-way) -Single and multiple vectors | FEAT_SME_MOP4 &&FEAT_SME_F8F32 |
|   1 |   1 | FMOP4A (widening, 4-way) - Multiple vectors          | FEAT_SME_MOP4 &&FEAT_SME_F8F32 |

## SME2 FP8 to FP16 quarter tile outer product

The encodings in this section are decoded from SME2 Quarter Tile Outer Product - 16-bit and 32-bit.

<!-- image -->

|   31 | 25 24   | 20 19 17 16 15 14   | 23   |   22 |   21 |    |    |    |         | 10 9   | 6   |   5 |     | 4 3   | 2 1 0   |
|------|---------|---------------------|------|------|------|----|----|----|---------|--------|-----|-----|-----|-------|---------|
|    1 | 0 0 0 0 | 0 0 0               | 0 0  |    0 |    1 | M  | Zm |  0 | 0 0 0 0 | 0 N    | Zn  |   0 | 0 1 | 0 0   | ZA      |

|   M |   N | Instruction Details                                                | Feature                        |
|-----|-----|--------------------------------------------------------------------|--------------------------------|
|   0 |   0 | FMOP4A (widening, 2-way, FP8 to FP16) -Single vectors              | FEAT_SME_MOP4 &&FEAT_SME_F8F16 |
|   0 |   1 | FMOP4A (widening, 2-way, FP8 to FP16) -Multiple and single vectors | FEAT_SME_MOP4 &&FEAT_SME_F8F16 |
|   1 |   0 | FMOP4A (widening, 2-way, FP8 to FP16) -Single and multiple vectors | FEAT_SME_MOP4 &&FEAT_SME_F8F16 |
|   1 |   1 | FMOP4A (widening, 2-way, FP8 to FP16) -Multiple vectors            | FEAT_SME_MOP4 &&FEAT_SME_F8F16 |

## SME2 BF16 to FP32 quarter tile outer product

The encodings in this section are decoded from SME2 Quarter Tile Outer Product - 16-bit and 32-bit.

<!-- image -->

| 31   | 25 24 23 22 21 20 19 17 16 15 14   |
|------|------------------------------------|
| 1 0  | 0 1 0 0 0 M Zm 0 0 0 0 0 0         |

|   M |   N | S Instruction Details                              | Feature       |
|-----|-----|----------------------------------------------------|---------------|
|   0 |   0 | 0 BFMOP4A (widening) -Single vectors               | FEAT_SME_MOP4 |
|   0 |   0 | 1 BFMOP4S (widening) -Single vectors               | FEAT_SME_MOP4 |
|   0 |   1 | 0 BFMOP4A (widening) - Multiple and single vectors | FEAT_SME_MOP4 |
|   0 |   1 | 1 BFMOP4S (widening) - Multiple and single vectors | FEAT_SME_MOP4 |

|   M |   N | S                                                  | Instruction Details Feature   |
|-----|-----|----------------------------------------------------|-------------------------------|
|   1 |   0 | 0 BFMOP4A (widening) - Single and multiple vectors | FEAT_SME_MOP4                 |
|   1 |   0 | 1 BFMOP4S (widening) - Single and multiple vectors | FEAT_SME_MOP4                 |
|   1 |   1 | 0 BFMOP4A(widening) -Multiple vectors              | FEAT_SME_MOP4                 |
|   1 |   1 | 1 BFMOP4S (widening) -Multiple vectors             | FEAT_SME_MOP4                 |

## SME2 FP16 non-widening quarter tile outer product

The encodings in this section are decoded from SME2 Quarter Tile Outer Product - 16-bit and 32-bit.

<!-- image -->

| 31   | 25        | 24   |   23 |   22 21 | 20   | 19   | 16 15   |   14 |     | 10 9   | 8   |   6 5 | 4   | 3   |   2 1 | 0   |
|------|-----------|------|------|---------|------|------|---------|------|-----|--------|-----|-------|-----|-----|-------|-----|
| 1 0  | 0 0 0 0 0 | 1 0  |    0 |       0 | M    | Zm   | 0 0 0   |    0 | 0 0 | 0 N    | Zn  |     0 | S   | 1 0 |     0 | ZA  |

|   M |   N |   S | Instruction Details                                                  | Feature                         |
|-----|-----|-----|----------------------------------------------------------------------|---------------------------------|
|   0 |   0 |   0 | FMOP4A (non-widening) - Half- precision, single vectors              | FEAT_SME_MOP4 &&FEAT_SME_F16F16 |
|   0 |   0 |   1 | FMOP4S (non-widening) - Half- precision, single vectors              | FEAT_SME_MOP4 &&FEAT_SME_F16F16 |
|   0 |   1 |   0 | FMOP4A (non-widening) - Half- precision, multiple and single vectors | FEAT_SME_MOP4 &&FEAT_SME_F16F16 |
|   0 |   1 |   1 | FMOP4S (non-widening) - Half- precision, multiple and single vectors | FEAT_SME_MOP4 &&FEAT_SME_F16F16 |
|   1 |   0 |   0 | FMOP4A (non-widening) - Half- precision, single and multiple vectors | FEAT_SME_MOP4 &&FEAT_SME_F16F16 |
|   1 |   0 |   1 | FMOP4S (non-widening) - Half- precision, single and multiple vectors | FEAT_SME_MOP4 &&FEAT_SME_F16F16 |
|   1 |   1 |   0 | FMOP4A (non-widening) - Half- precision, multiple vectors            | FEAT_SME_MOP4 &&FEAT_SME_F16F16 |
|   1 |   1 |   1 | FMOP4S (non-widening) - Half- precision, multiple vectors            | FEAT_SME_MOP4 &&FEAT_SME_F16F16 |

## SME2 FP16 to FP32 quarter tile outer product

The encodings in this section are decoded from SME2 Quarter Tile Outer Product - 16-bit and 32-bit.

<!-- image -->

| 31   | 25 24 23 22 21 20 19 17 16 15 14 10 9 8 6 5 4 3 2   |
|------|-----------------------------------------------------|
| 1 0  | 0 1 0 0 1 M Zm 0 0 0 0 0 0 0 N Zn 0 S 0 0           |

|   M |   N |   S | Instruction Details                                                 | Feature       |
|-----|-----|-----|---------------------------------------------------------------------|---------------|
|   0 |   0 |   0 | FMOP4A (widening, 2-way, FP16 to FP32) -Single vectors              | FEAT_SME_MOP4 |
|   0 |   0 |   1 | FMOP4S (widening) -Single vectors                                   | FEAT_SME_MOP4 |
|   0 |   1 |   0 | FMOP4A (widening, 2-way, FP16 to FP32) -Multiple and single vectors | FEAT_SME_MOP4 |
|   0 |   1 |   1 | FMOP4S (widening) - Multiple and single vectors                     | FEAT_SME_MOP4 |
|   1 |   0 |   0 | FMOP4A (widening, 2-way, FP16 to FP32) -Single and multiple vectors | FEAT_SME_MOP4 |
|   1 |   0 |   1 | FMOP4S (widening) - Single and multiple vectors                     | FEAT_SME_MOP4 |
|   1 |   1 |   0 | FMOP4A (widening, 2-way, FP16 to FP32) -Multiple vectors            | FEAT_SME_MOP4 |
|   1 |   1 |   1 | FMOP4S (widening) -Multiple vectors                                 | FEAT_SME_MOP4 |

## SME2 BF16 non-widening quarter tile outer product

The encodings in this section are decoded from SME2 Quarter Tile Outer Product - 16-bit and 32-bit.

<!-- image -->

| 31   | 25 24 23 22 21 20 19 17 16 15 14   |
|------|------------------------------------|
| 1 0  | 0 1 0 0 1 M Zm 0 0 0 0 0           |

|   M |   N | S                                                      | Instruction Details Feature            |
|-----|-----|--------------------------------------------------------|----------------------------------------|
|   0 |   0 | 0 BFMOP4A (non-widening) - vectors                     | Single FEAT_SME_MOP4 &&FEAT_SME_B16B16 |
|   0 |   0 | 1 BFMOP4S (non-widening) - Single vectors              | FEAT_SME_MOP4 &&FEAT_SME_B16B16        |
|   0 |   1 | 0 BFMOP4A (non-widening) - Multiple and single vectors | FEAT_SME_MOP4 &&FEAT_SME_B16B16        |
|   0 |   1 | 1 BFMOP4S (non-widening) - Multiple and single vectors | FEAT_SME_MOP4 &&FEAT_SME_B16B16        |
|   1 |   0 | 0 BFMOP4A (non-widening) -Single and multiple vectors  | FEAT_SME_MOP4 &&FEAT_SME_B16B16        |
|   1 |   0 | 1 BFMOP4S (non-widening) - Single and multiple vectors | FEAT_SME_MOP4 &&FEAT_SME_B16B16        |
|   1 |   1 | 0 BFMOP4A (non-widening) - Multiple vectors            | FEAT_SME_MOP4 &&FEAT_SME_B16B16        |
|   1 |   1 | 1 BFMOP4S (non-widening) - Multiple vectors            | FEAT_SME_MOP4 &&FEAT_SME_B16B16        |

## SME2 Int16 to Int32 quarter tile outer product

The encodings in this section are decoded from SME2 Quarter Tile Outer Product - 16-bit and 32-bit.

<!-- image -->

| 31   | 25 24 23 22 21 20 19 17 16 15 14   |
|------|------------------------------------|
| 1 0  | 0 u0 0 0 0 M Zm 0 1 0 0            |

|   u0 |   M |   N |   S | Instruction Details                          | Feature       |
|------|-----|-----|-----|----------------------------------------------|---------------|
|    0 |   0 |   0 |   0 | SMOP4A (2-way) -Single vectors               | FEAT_SME_MOP4 |
|    0 |   0 |   0 |   1 | SMOP4S (2-way) -Single vectors               | FEAT_SME_MOP4 |
|    0 |   0 |   1 |   0 | SMOP4A (2-way) -Multiple and single vectors  | FEAT_SME_MOP4 |
|    0 |   0 |   1 |   1 | SMOP4S (2-way) - Multiple and single vectors | FEAT_SME_MOP4 |
|    0 |   1 |   0 |   0 | SMOP4A (2-way) -Single and multiple vectors  | FEAT_SME_MOP4 |
|    0 |   1 |   0 |   1 | SMOP4S (2-way) - Single and multiple vectors | FEAT_SME_MOP4 |
|    0 |   1 |   1 |   0 | SMOP4A (2-way) -Multiple vectors             | FEAT_SME_MOP4 |
|    0 |   1 |   1 |   1 | SMOP4S (2-way) -Multiple vectors             | FEAT_SME_MOP4 |
|    1 |   0 |   0 |   0 | UMOP4A(2-way) -Single vectors                | FEAT_SME_MOP4 |
|    1 |   0 |   0 |   1 | UMOP4S (2-way) -Single vectors               | FEAT_SME_MOP4 |
|    1 |   0 |   1 |   0 | UMOP4A (2-way) -Multiple and single vectors  | FEAT_SME_MOP4 |
|    1 |   0 |   1 |   1 | UMOP4S (2-way) -Multiple and single vectors  | FEAT_SME_MOP4 |
|    1 |   1 |   0 |   0 | UMOP4A (2-way) -Single and multiple vectors  | FEAT_SME_MOP4 |
|    1 |   1 |   0 |   1 | UMOP4S (2-way) -Single and multiple vectors  | FEAT_SME_MOP4 |
|    1 |   1 |   1 |   0 | UMOP4A(2-way) -Multiple vectors              | FEAT_SME_MOP4 |
|    1 |   1 |   1 |   1 | UMOP4S (2-way) -Multiple vectors             | FEAT_SME_MOP4 |

## SME2 Int8 to Int32 quarter tile outer product

The encodings in this section are decoded from SME2 Quarter Tile Outer Product - 16-bit and 32-bit.

<!-- image -->

| 31   | 25 24 23 22 21 20 19 17 16 15 14 10   |
|------|---------------------------------------|
| 1 0  | 0 u0 0 0 u1 M Zm 0 1 0 0 0 0 0        |

|   u0 |   u1 |   M |   N |   S | Instruction Details                                  | Feature       |
|------|------|-----|-----|-----|------------------------------------------------------|---------------|
|    0 |    0 |   0 |   0 |   0 | SMOP4A(4-way) -32-bit, single vectors                | FEAT_SME_MOP4 |
|    0 |    0 |   0 |   0 |   1 | SMOP4S (4-way) -32-bit, single vectors               | FEAT_SME_MOP4 |
|    0 |    0 |   0 |   1 |   0 | SMOP4A (4-way) -32-bit, multiple and single vectors  | FEAT_SME_MOP4 |
|    0 |    0 |   0 |   1 |   1 | SMOP4S (4-way) -32-bit, multiple and single vectors  | FEAT_SME_MOP4 |
|    0 |    0 |   1 |   0 |   0 | SMOP4A (4-way) - 32-bit, single and multiple vectors | FEAT_SME_MOP4 |
|    0 |    0 |   1 |   0 |   1 | SMOP4S (4-way) - 32-bit, single and multiple vectors | FEAT_SME_MOP4 |
|    0 |    0 |   1 |   1 |   0 | SMOP4A (4-way) - 32-bit, multiple vectors            | FEAT_SME_MOP4 |
|    0 |    0 |   1 |   1 |   1 | SMOP4S (4-way) - 32-bit, multiple vectors            | FEAT_SME_MOP4 |
|    0 |    1 |   0 |   0 |   0 | SUMOP4A-32-bit, single vectors                       | FEAT_SME_MOP4 |
|    0 |    1 |   0 |   0 |   1 | SUMOP4S -32-bit, single vectors                      | FEAT_SME_MOP4 |
|    0 |    1 |   0 |   1 |   0 | SUMOP4A -32-bit, multiple and single vectors         | FEAT_SME_MOP4 |
|    0 |    1 |   0 |   1 |   1 | SUMOP4S - 32-bit, multiple and single vectors        | FEAT_SME_MOP4 |
|    0 |    1 |   1 |   0 |   0 | SUMOP4A -32-bit, single and multiple vectors         | FEAT_SME_MOP4 |
|    0 |    1 |   1 |   0 |   1 | SUMOP4S - 32-bit, single and multiple vectors        | FEAT_SME_MOP4 |
|    0 |    1 |   1 |   1 |   0 | SUMOP4A-32-bit, multiple vectors                     | FEAT_SME_MOP4 |
|    0 |    1 |   1 |   1 |   1 | SUMOP4S -32-bit, multiple vectors                    | FEAT_SME_MOP4 |
|    1 |    0 |   0 |   0 |   0 | USMOP4A-32-bit, single vectors                       | FEAT_SME_MOP4 |
|    1 |    0 |   0 |   0 |   1 | USMOP4S -32-bit, single vectors                      | FEAT_SME_MOP4 |
|    1 |    0 |   0 |   1 |   0 | USMOP4A -32-bit, multiple and single vectors         | FEAT_SME_MOP4 |
|    1 |    0 |   0 |   1 |   1 | USMOP4S - 32-bit, multiple and single vectors        | FEAT_SME_MOP4 |
|    1 |    0 |   1 |   0 |   0 | USMOP4A -32-bit, single and multiple vectors         | FEAT_SME_MOP4 |
|    1 |    0 |   1 |   0 |   1 | USMOP4S - 32-bit, single and multiple vectors        | FEAT_SME_MOP4 |
|    1 |    0 |   1 |   1 |   0 | USMOP4A-32-bit, multiple vectors                     | FEAT_SME_MOP4 |
|    1 |    0 |   1 |   1 |   1 | USMOP4S -32-bit, multiple vectors                    | FEAT_SME_MOP4 |
|    1 |    1 |   0 |   0 |   0 | UMOP4A (4-way) - 32-bit, single vectors              | FEAT_SME_MOP4 |
|    1 |    1 |   0 |   0 |   1 | UMOP4S(4-way) -32-bit, single vectors                | FEAT_SME_MOP4 |
|    1 |    1 |   0 |   1 |   0 | UMOP4A (4-way) -32-bit, multiple and single vectors  | FEAT_SME_MOP4 |
|    1 |    1 |   0 |   1 |   1 | UMOP4S (4-way) -32-bit, multiple and single vectors  | FEAT_SME_MOP4 |

|   u0 |   u1 |   M |   N |   S | Instruction Details                                  | Feature       |
|------|------|-----|-----|-----|------------------------------------------------------|---------------|
|    1 |    1 |   1 |   0 |   0 | UMOP4A (4-way) - 32-bit, single and multiple vectors | FEAT_SME_MOP4 |
|    1 |    1 |   1 |   0 |   1 | UMOP4S (4-way) - 32-bit, single and multiple vectors | FEAT_SME_MOP4 |
|    1 |    1 |   1 |   1 |   0 | UMOP4A (4-way) - 32-bit, multiple vectors            | FEAT_SME_MOP4 |
|    1 |    1 |   1 |   1 |   1 | UMOP4S (4-way) - 32-bit, multiple vectors            | FEAT_SME_MOP4 |

## SME2 Sparse Outer Product

SME2 Sparse Outer Product

The encodings in this section are decoded from SME encodings.

<!-- image -->

| 31    | 16 15 14 13 12   | 4 3 2 1 0   |
|-------|------------------|-------------|
| 1 0 0 | op2 0 op3        | op4 0 op5   |

| op0   | op1   | op2   |   op3 | op4   | op5   | Instruction details                       | Feature                         |
|-------|-------|-------|-------|-------|-------|-------------------------------------------|---------------------------------|
| 0     | 0     | 0     |     0 | 0     | x     | FTMOPA (non-widening) - Single- precision | FEAT_SME_TMOP                   |
| 0     | 0     | 0     |     0 | 1     | 0     | UNALLOCATED                               | -                               |
| 0     | 1     | 0     |     0 | 0     | x     | FTMOPA (widening, 4-way)                  | FEAT_SME_TMOP &&FEAT_SME_F8F32  |
| 0     | 1     | 0     |     0 | 1     | 0     | FTMOPA(widening, 2-way, FP8 to FP16)      | FEAT_SME_TMOP &&FEAT_SME_F8F16  |
| 1     | 0     | 0     |     0 | 0     | x     | BFTMOPA (widening)                        | FEAT_SME_TMOP                   |
| 1     | 0     | 0     |     0 | 1     | 0     | FTMOPA (non-widening) - Half- precision   | FEAT_SME_TMOP &&FEAT_SME_F16F16 |
| 1     | 1     | 0     |     0 | 0     | x     | FTMOPA (widening, 2-way, FP16 to FP32)    | FEAT_SME_TMOP                   |
| 1     | 1     | 0     |     0 | 1     | 0     | BFTMOPA (non-widening)                    | FEAT_SME_TMOP &&FEAT_SME_B16B16 |
| x     | 0     | 1     |     0 | 1     | x     | SME2 Int16 to Int32 sparse outer product  | -                               |
| x     | 1     | 1     |     0 | 1     | x     | UNALLOCATED                               | -                               |
| x     | x     | 0     |     0 | 1     | 1     | UNALLOCATED                               | -                               |
| x     | x     | 1     |     0 | 0     | x     | SMEInt8 to Int32 sparse outer product     | -                               |
| x     | x     | x     |     1 | x     | x     | UNALLOCATED                               | -                               |

## SME2 Int16 to Int32 sparse outer product

The encodings in this section are decoded from SME2 Sparse Outer Product.

<!-- image -->

|   31 | 25 24 23 22 21 20   | 16 15 14 13 12 11 10 9 6 5 4 3   |
|------|---------------------|----------------------------------|
|    1 | 0 u0 0 1 0 Zm 1     | 0 0 K Zk Zn i2 1                 |

## SME Int8 to Int32 sparse outer product

The encodings in this section are decoded from SME2 Sparse Outer Product.

<!-- image -->

| 31    | 25 24 23 22 21 20 16 15 14 13 12 11 10 9 6 5 4 3 2   |
|-------|------------------------------------------------------|
| 1 0 0 | 0 u0 0 1 u1 Zm 1 0 0 K Zk Zn i2 0 0                  |

|   u0 |   u1 | Instruction Details   | Feature       |
|------|------|-----------------------|---------------|
|    0 |    0 | STMOPA (4-way)        | FEAT_SME_TMOP |
|    0 |    1 | SUTMOPA               | FEAT_SME_TMOP |
|    1 |    0 | USTMOPA               | FEAT_SME_TMOP |
|    1 |    1 | UTMOPA(4-way)         | FEAT_SME_TMOP |

## SME FP Outer Product - 32 bit

SMEFPOuter Product - 32 bit

The encodings in this section are decoded from SME encodings.

<!-- image -->

| 31                        | 25 24 23 22 21 20 5 4 3 2   |
|---------------------------|-----------------------------|
| 1 0 0 0 0 0 0 op0 1 0 op1 | op2 0 0                     |

|   op0 |   op1 | op2   | Instruction details            | Feature        |
|-------|-------|-------|--------------------------------|----------------|
|     0 |     0 | x     | SMEFP32 outer product          | -              |
|     0 |     1 | 0     | FMOPA(widening, 4-way)         | FEAT_SME_F8F32 |
|     0 |     1 | 1     | UNALLOCATED                    | -              |
|     1 |     0 | x     | SMEBF16 widening outer product | -              |
|     1 |     1 | x     | SMEFP16 widening outer product | -              |

|   u0 | Instruction Details   | Feature       |
|------|-----------------------|---------------|
|    0 | STMOPA (2-way)        | FEAT_SME_TMOP |
|    1 | UTMOPA(2-way)         | FEAT_SME_TMOP |

## SME FP32 outer product

The encodings in this section are decoded from SME FP Outer Product - 32 bit.

<!-- image -->

| 31   | 25 24 23 22 21 20   | 16 15   | 13 12   | 10 9   | 5 4   | 3   | 2 1 0   |
|------|---------------------|---------|---------|--------|-------|-----|---------|
| 1 0  | 0 0 0 0 0 0 1 0 0   | Zm      | Pm      | Pn     | S     | 0 0 | ZAda    |

|   S | Instruction Details   | Feature   |
|-----|-----------------------|-----------|
|   0 | FMOPA(non-widening)   | FEAT_SME  |
|   1 | FMOPS (non-widening)  | FEAT_SME  |

## SME BF16 widening outer product

The encodings in this section are decoded from SME FP Outer Product - 32 bit.

<!-- image -->

| 31   | 25 24   | 23 22 13   |   10 | 5 4   |   21 20 | 16 15   | 12   | 9   | 3   | 2   | 1 0   |
|------|---------|------------|------|-------|---------|---------|------|-----|-----|-----|-------|
| 1 0  | 0 0 0 0 | 0 1        |    1 | 0 Zn  |       0 | Zm      | Pm   | Pn  | S   | 0 0 | ZAda  |

|   S | Instruction Details   | Feature   |
|-----|-----------------------|-----------|
|   0 | BFMOPA(widening)      | FEAT_SME  |
|   1 | BFMOPS (widening)     | FEAT_SME  |

## SME FP16 widening outer product

The encodings in this section are decoded from SME FP Outer Product - 32 bit.

<!-- image -->

| 31   | 25 24 23 22 21 20   | 13 12 10 9 5 4 3 2 1 0   |
|------|---------------------|--------------------------|
| 1 0  | 0 1 1 0 1 Zm        | Pm Pn Zn S 0 0 ZAda      |

|   S | Instruction Details                  | Feature   |
|-----|--------------------------------------|-----------|
|   0 | FMOPA(widening, 2-way, FP16 to FP32) | FEAT_SME  |
|   1 | FMOPS (widening)                     | FEAT_SME  |

## SME2 Outer Product - Misc

SME2 Outer Product - Misc

The encodings in this section are decoded from SME encodings.

| 31 25 24 23 22 21         | 5 4 3 2 1 0   |
|---------------------------|---------------|
| 1 0 0 0 0 0 0 op0 1 0 op1 | op2 1 0 op3   |

|   op0 | op1   | op2   | op3   | Instruction details                  | Feature        |
|-------|-------|-------|-------|--------------------------------------|----------------|
|     0 | 0     | x     | x     | SME2 32-bit binary outer product     | -              |
|     0 | 1     | 0     | 0     | FMOPA(widening, 2-way, FP8 to FP16)  | FEAT_SME_F8F16 |
|     0 | 1     | 1     | 0     | UNALLOCATED                          | -              |
|     0 | 1     | x     | 1     | UNALLOCATED                          | -              |
|     1 | 0     | x     | 0     | SME2 FP16 non-widening outer product | -              |
|     1 | 1     | x     | 0     | SME2 BF16 non-widening outer product | -              |
|     1 | x     | x     | 1     | UNALLOCATED                          | -              |

## SME2 32-bit binary outer product

The encodings in this section are decoded from SME2 Outer Product - Misc.

<!-- image -->

| 31    | 25 24 23 22 21 20   | 16 15 13 12 10 9 5 4 3 2 1 0   |
|-------|---------------------|--------------------------------|
| 1 0 0 | 0 0 1 0 0 Zm        | Pm Pn Zn S 1 0 ZAda            |

|   S | Instruction Details   | Feature   |
|-----|-----------------------|-----------|
|   0 | BMOPA                 | FEAT_SME2 |
|   1 | BMOPS                 | FEAT_SME2 |

## SME2 FP16 non-widening outer product

The encodings in this section are decoded from SME2 Outer Product - Misc.

<!-- image -->

## SME2 BF16 non-widening outer product

The encodings in this section are decoded from SME2 Outer Product - Misc.

<!-- image -->

|   S | Instruction Details   | Feature         |
|-----|-----------------------|-----------------|
|   0 | BFMOPA(non-widening)  | FEAT_SME_B16B16 |
|   1 | BFMOPS (non-widening) | FEAT_SME_B16B16 |

## SME2 Multi-vector - Memory (Contiguous)

SME2 Multi-vector - Memory (Contiguous)

The encodings in this section are decoded from SME encodings.

<!-- image -->

| 31    | 23 22   | 20   | 16 15   | 1 0   |
|-------|---------|------|---------|-------|
| 1 0 1 | 0 0 0 0 | op0  | op1     | op2   |

| op0   |   op1 | op2   | Instruction details                                                   |
|-------|-------|-------|-----------------------------------------------------------------------|
| 00x   |     0 | x     | SME2 multi-vec contiguous load (scalar plus scalar, two registers)    |
| 00x   |     1 | 0     | SME2 multi-vec contiguous load (scalar plus scalar, four registers)   |
| 01x   |     0 | x     | SME2 multi-vec contiguous store (scalar plus scalar, two registers)   |
| 01x   |     1 | 0     | SME2 multi-vec contiguous store (scalar plus scalar, four registers)  |
| 0x1   |     1 | 1     | UNALLOCATED                                                           |
| 100   |     0 | x     | SME2 multi-vec contiguous load (scalar plus immediate, two registers) |

|   S | Instruction Details   | Feature         |
|-----|-----------------------|-----------------|
|   0 | FMOPA(non-widening)   | FEAT_SME_F16F16 |
|   1 | FMOPS (non-widening)  | FEAT_SME_F16F16 |

| op0   | op1   | op2   | Instruction details                                                     |
|-------|-------|-------|-------------------------------------------------------------------------|
| 100   | 1     | 0     | SME2 multi-vec contiguous load (scalar plus immediate, four registers)  |
| 110   | 0     | x     | SME2 multi-vec contiguous store (scalar plus immediate, two registers)  |
| 110   | 1     | 0     | SME2 multi-vec contiguous store (scalar plus immediate, four registers) |
| 1x1   | x     | x     | UNALLOCATED                                                             |
| xx0   | 1     | 1     | UNALLOCATED                                                             |

## SME2 multi-vec contiguous load (scalar plus scalar, two registers)

The encodings in this section are decoded from SME2 Multi-vector - Memory (Contiguous).

<!-- image -->

| 31                    | 21 20   | 16 15 14 13 12 10 9 5 4 1 0   |
|-----------------------|---------|-------------------------------|
| 1 0 1 0 0 0 0 0 0 0 0 | Rm      | 0 msz PNg Rn Zt N             |

|   msz |   N | Instruction Details                                | Feature                            |
|-------|-----|----------------------------------------------------|------------------------------------|
|    00 |   0 | LD1B (scalar plus scalar, consecutive registers)   | FEAT_SME2 &#124;&#124; FEAT_SVE2p1 |
|    00 |   1 | LDNT1B (scalar plus scalar, consecutive registers) | FEAT_SME2 &#124;&#124; FEAT_SVE2p1 |
|    01 |   0 | LD1H (scalar plus scalar, consecutive registers)   | FEAT_SME2 &#124;&#124; FEAT_SVE2p1 |
|    01 |   1 | LDNT1H (scalar plus scalar, consecutive registers) | FEAT_SME2 &#124;&#124; FEAT_SVE2p1 |
|    10 |   0 | LD1W (scalar plus scalar, consecutive registers)   | FEAT_SME2 &#124;&#124; FEAT_SVE2p1 |
|    10 |   1 | LDNT1W (scalar plus scalar, consecutive registers) | FEAT_SME2 &#124;&#124; FEAT_SVE2p1 |
|    11 |   0 | LD1D (scalar plus scalar, consecutive registers)   | FEAT_SME2 &#124;&#124; FEAT_SVE2p1 |
|    11 |   1 | LDNT1D (scalar plus scalar, consecutive registers) | FEAT_SME2 &#124;&#124; FEAT_SVE2p1 |

## SME2 multi-vec contiguous load (scalar plus scalar, four registers)

The encodings in this section are decoded from SME2 Multi-vector - Memory (Contiguous).

<!-- image -->

| 31                    | 21 20   | 16 15 14 13 12 10 9 5 4 2 1   |
|-----------------------|---------|-------------------------------|
| 1 0 1 0 0 0 0 0 0 0 0 | Rm 1    | msz PNg Rn Zt 0               |

|   msz |   N | Instruction Details                                | Feature                            |
|-------|-----|----------------------------------------------------|------------------------------------|
|    00 |   0 | LD1B (scalar plus scalar, consecutive registers)   | FEAT_SME2 &#124;&#124; FEAT_SVE2p1 |
|    00 |   1 | LDNT1B (scalar plus scalar, consecutive registers) | FEAT_SME2 &#124;&#124; FEAT_SVE2p1 |
|    01 |   0 | LD1H (scalar plus scalar, consecutive registers)   | FEAT_SME2 &#124;&#124; FEAT_SVE2p1 |
|    01 |   1 | LDNT1H (scalar plus scalar, consecutive registers) | FEAT_SME2 &#124;&#124; FEAT_SVE2p1 |
|    10 |   0 | LD1W (scalar plus scalar, consecutive registers)   | FEAT_SME2 &#124;&#124; FEAT_SVE2p1 |
|    10 |   1 | LDNT1W (scalar plus scalar, consecutive registers) | FEAT_SME2 &#124;&#124; FEAT_SVE2p1 |
|    11 |   0 | LD1D (scalar plus scalar, consecutive registers)   | FEAT_SME2 &#124;&#124; FEAT_SVE2p1 |
|    11 |   1 | LDNT1D (scalar plus scalar, consecutive registers) | FEAT_SME2 &#124;&#124; FEAT_SVE2p1 |

## SME2 multi-vec contiguous store (scalar plus scalar, two registers)

The encodings in this section are decoded from SME2 Multi-vector - Memory (Contiguous).

<!-- image -->

|   msz |   N | Instruction Details                                | Feature                            |
|-------|-----|----------------------------------------------------|------------------------------------|
|    00 |   0 | ST1B (scalar plus scalar, consecutive registers)   | FEAT_SME2 &#124;&#124; FEAT_SVE2p1 |
|    00 |   1 | STNT1B (scalar plus scalar, consecutive registers) | FEAT_SME2 &#124;&#124; FEAT_SVE2p1 |
|    01 |   0 | ST1H (scalar plus scalar, consecutive registers)   | FEAT_SME2 &#124;&#124; FEAT_SVE2p1 |
|    01 |   1 | STNT1H (scalar plus scalar, consecutive registers) | FEAT_SME2 &#124;&#124; FEAT_SVE2p1 |
|    10 |   0 | ST1W (scalar plus scalar, consecutive registers)   | FEAT_SME2 &#124;&#124; FEAT_SVE2p1 |
|    10 |   1 | STNT1W (scalar plus scalar, consecutive registers) | FEAT_SME2 &#124;&#124; FEAT_SVE2p1 |
|    11 |   0 | ST1D (scalar plus scalar, consecutive registers)   | FEAT_SME2 &#124;&#124; FEAT_SVE2p1 |
|    11 |   1 | STNT1D (scalar plus scalar, consecutive registers) | FEAT_SME2 &#124;&#124; FEAT_SVE2p1 |

## SME2 multi-vec contiguous store (scalar plus scalar, four registers)

The encodings in this section are decoded from SME2 Multi-vector - Memory (Contiguous).

<!-- image -->

|   msz |   N | Instruction Details                                | Feature                            |
|-------|-----|----------------------------------------------------|------------------------------------|
|    00 |   0 | ST1B (scalar plus scalar, consecutive registers)   | FEAT_SME2 &#124;&#124; FEAT_SVE2p1 |
|    00 |   1 | STNT1B (scalar plus scalar, consecutive registers) | FEAT_SME2 &#124;&#124; FEAT_SVE2p1 |
|    01 |   0 | ST1H (scalar plus scalar, consecutive registers)   | FEAT_SME2 &#124;&#124; FEAT_SVE2p1 |
|    01 |   1 | STNT1H (scalar plus scalar, consecutive registers) | FEAT_SME2 &#124;&#124; FEAT_SVE2p1 |
|    10 |   0 | ST1W (scalar plus scalar, consecutive registers)   | FEAT_SME2 &#124;&#124; FEAT_SVE2p1 |
|    10 |   1 | STNT1W (scalar plus scalar, consecutive registers) | FEAT_SME2 &#124;&#124; FEAT_SVE2p1 |
|    11 |   0 | ST1D (scalar plus scalar, consecutive registers)   | FEAT_SME2 &#124;&#124; FEAT_SVE2p1 |
|    11 |   1 | STNT1D (scalar plus scalar, consecutive registers) | FEAT_SME2 &#124;&#124; FEAT_SVE2p1 |

SME2 multi-vec contiguous load (scalar plus immediate, two registers)

The encodings in this section are decoded from SME2 Multi-vector - Memory (Contiguous).

<!-- image -->

| 31    | 23 22 20 19    | 16 15 14 13 12 10 9 5 4 1 0   |
|-------|----------------|-------------------------------|
| 1 0 1 | 0 1 0 0 imm4 0 | msz PNg Rn Zt N               |

|   msz |   N | Instruction Details                                   | Feature                            |
|-------|-----|-------------------------------------------------------|------------------------------------|
|    00 |   0 | LD1B (scalar plus immediate, consecutive registers)   | FEAT_SME2 &#124;&#124; FEAT_SVE2p1 |
|    00 |   1 | LDNT1B (scalar plus immediate, consecutive registers) | FEAT_SME2 &#124;&#124; FEAT_SVE2p1 |

|   msz |   N | Instruction Details                                   | Feature                            |
|-------|-----|-------------------------------------------------------|------------------------------------|
|    01 |   0 | LD1H (scalar plus immediate, consecutive registers)   | FEAT_SME2 &#124;&#124; FEAT_SVE2p1 |
|    01 |   1 | LDNT1H (scalar plus immediate, consecutive registers) | FEAT_SME2 &#124;&#124; FEAT_SVE2p1 |
|    10 |   0 | LD1W(scalar plus immediate, consecutive registers)    | FEAT_SME2 &#124;&#124; FEAT_SVE2p1 |
|    10 |   1 | LDNT1W (scalar plus immediate, consecutive registers) | FEAT_SME2 &#124;&#124; FEAT_SVE2p1 |
|    11 |   0 | LD1D (scalar plus immediate, consecutive registers)   | FEAT_SME2 &#124;&#124; FEAT_SVE2p1 |
|    11 |   1 | LDNT1D (scalar plus immediate, consecutive registers) | FEAT_SME2 &#124;&#124; FEAT_SVE2p1 |

SME2 multi-vec contiguous load (scalar plus immediate, four registers)

The encodings in this section are decoded from SME2 Multi-vector - Memory (Contiguous).

<!-- image -->

| 31    | 23 22 20 19        | 16 15 14 13 12 10 9 5 4 2 1   |
|-------|--------------------|-------------------------------|
| 1 0 1 | 0 1 0 0 imm4 1 msz | PNg Rn Zt 0                   |

|   msz |   N | Instruction Details                                   | Feature                            |
|-------|-----|-------------------------------------------------------|------------------------------------|
|    00 |   0 | LD1B (scalar plus immediate, consecutive registers)   | FEAT_SME2 &#124;&#124; FEAT_SVE2p1 |
|    00 |   1 | LDNT1B (scalar plus immediate, consecutive registers) | FEAT_SME2 &#124;&#124; FEAT_SVE2p1 |
|    01 |   0 | LD1H (scalar plus immediate, consecutive registers)   | FEAT_SME2 &#124;&#124; FEAT_SVE2p1 |
|    01 |   1 | LDNT1H (scalar plus immediate, consecutive registers) | FEAT_SME2 &#124;&#124; FEAT_SVE2p1 |
|    10 |   0 | LD1W(scalar plus immediate, consecutive registers)    | FEAT_SME2 &#124;&#124; FEAT_SVE2p1 |
|    10 |   1 | LDNT1W (scalar plus immediate, consecutive registers) | FEAT_SME2 &#124;&#124; FEAT_SVE2p1 |
|    11 |   0 | LD1D (scalar plus immediate, consecutive registers)   | FEAT_SME2 &#124;&#124; FEAT_SVE2p1 |
|    11 |   1 | LDNT1D (scalar plus immediate, consecutive registers) | FEAT_SME2 &#124;&#124; FEAT_SVE2p1 |

SME2 multi-vec contiguous store (scalar plus immediate, two registers)

The encodings in this section are decoded from SME2 Multi-vector - Memory (Contiguous).

<!-- image -->

|   msz |   N | Instruction Details                                   | Feature                            |
|-------|-----|-------------------------------------------------------|------------------------------------|
|    00 |   0 | ST1B (scalar plus immediate, consecutive registers)   | FEAT_SME2 &#124;&#124; FEAT_SVE2p1 |
|    00 |   1 | STNT1B (scalar plus immediate, consecutive registers) | FEAT_SME2 &#124;&#124; FEAT_SVE2p1 |
|    01 |   0 | ST1H (scalar plus immediate, consecutive registers)   | FEAT_SME2 &#124;&#124; FEAT_SVE2p1 |
|    01 |   1 | STNT1H (scalar plus immediate, consecutive registers) | FEAT_SME2 &#124;&#124; FEAT_SVE2p1 |
|    10 |   0 | ST1W (scalar plus immediate, consecutive registers)   | FEAT_SME2 &#124;&#124; FEAT_SVE2p1 |
|    10 |   1 | STNT1W (scalar plus immediate, consecutive registers) | FEAT_SME2 &#124;&#124; FEAT_SVE2p1 |
|    11 |   0 | ST1D (scalar plus immediate, consecutive registers)   | FEAT_SME2 &#124;&#124; FEAT_SVE2p1 |
|    11 |   1 | STNT1D (scalar plus immediate, consecutive registers) | FEAT_SME2 &#124;&#124; FEAT_SVE2p1 |

## SME2 multi-vec contiguous store (scalar plus immediate, four registers)

The encodings in this section are decoded from SME2 Multi-vector - Memory (Contiguous).

<!-- image -->

| 31   | 23 22 20 19   | 16 15 14 13 10 9   | 12 5 4 2 1 0   |
|------|---------------|--------------------|----------------|
| 1 0  | 0 1 1 0 imm4  | 1 msz PNg Rn       | Zt 0 N         |

|   msz |   N | Instruction Details                                   | Feature                            |
|-------|-----|-------------------------------------------------------|------------------------------------|
|    00 |   0 | ST1B (scalar plus immediate, consecutive registers)   | FEAT_SME2 &#124;&#124; FEAT_SVE2p1 |
|    00 |   1 | STNT1B (scalar plus immediate, consecutive registers) | FEAT_SME2 &#124;&#124; FEAT_SVE2p1 |
|    01 |   0 | ST1H (scalar plus immediate, consecutive registers)   | FEAT_SME2 &#124;&#124; FEAT_SVE2p1 |
|    01 |   1 | STNT1H (scalar plus immediate, consecutive registers) | FEAT_SME2 &#124;&#124; FEAT_SVE2p1 |
|    10 |   0 | ST1W (scalar plus immediate, consecutive registers)   | FEAT_SME2 &#124;&#124; FEAT_SVE2p1 |

|   msz |   N | Instruction Details                                   | Feature                            |
|-------|-----|-------------------------------------------------------|------------------------------------|
|    10 |   1 | STNT1W (scalar plus immediate, consecutive registers) | FEAT_SME2 &#124;&#124; FEAT_SVE2p1 |
|    11 |   0 | ST1D (scalar plus immediate, consecutive registers)   | FEAT_SME2 &#124;&#124; FEAT_SVE2p1 |
|    11 |   1 | STNT1D (scalar plus immediate, consecutive registers) | FEAT_SME2 &#124;&#124; FEAT_SVE2p1 |

## SME2 Multi-vector - Memory (Strided)

SME2 Multi-vector - Memory (Strided)

The encodings in this section are decoded from SME encodings.

<!-- image -->

| 31      | 23 22 20 19 16 15 14 3 2   |
|---------|----------------------------|
| 1 0 1 0 | 0 op0 op1 op2              |

| op0   | op1   | op2   | Instruction details                                                   |       |
|-------|-------|-------|-----------------------------------------------------------------------|-------|
| 00x   | 0     | x     | SME2 multi-vec non-contiguous (scalar plus scalar, two registers)     | load  |
| 00x   | 1     | 0     | SME2 multi-vec non-contiguous (scalar plus scalar, four registers)    | load  |
| 01x   | 0     | x     | SME2 multi-vec non-contiguous (scalar plus scalar, two registers)     | store |
| 01x   | 1     | 0     | SME2 multi-vec non-contiguous (scalar plus scalar, four registers)    | store |
| 0x1   | 1     | 1     | UNALLOCATED                                                           |       |
| 100   | 0     | x     | SME2 multi-vec non-contiguous (scalar plus immediate, two registers)  | load  |
| 100   | 1     | 0     | SME2 multi-vec non-contiguous (scalar plus immediate, four registers) | load  |
| 110   | 0     | x     | SME2 multi-vec non-contiguous (scalar plus immediate, two registers)  | store |
| 110   | 1     | 0     | SME2 multi-vec non-contiguous (scalar plus immediate, four registers) | store |
| 1x1   | x     | x     | UNALLOCATED                                                           |       |
| xx0   | 1     | 1     | UNALLOCATED                                                           |       |

SME2 multi-vec non-contiguous load (scalar plus scalar, two registers)

The encodings in this section are decoded from SME2 Multi-vector - Memory (Strided).

<!-- image -->

|   msz |   N | Instruction Details                            | Feature   |
|-------|-----|------------------------------------------------|-----------|
|    00 |   0 | LD1B (scalar plus scalar, strided registers)   | FEAT_SME2 |
|    00 |   1 | LDNT1B (scalar plus scalar, strided registers) | FEAT_SME2 |
|    01 |   0 | LD1H(scalar plus scalar, strided registers)    | FEAT_SME2 |
|    01 |   1 | LDNT1H (scalar plus scalar, strided registers) | FEAT_SME2 |
|    10 |   0 | LD1W(scalar plus scalar, strided registers)    | FEAT_SME2 |
|    10 |   1 | LDNT1W (scalar plus scalar, strided registers) | FEAT_SME2 |
|    11 |   0 | LD1D(scalar plus scalar, strided registers)    | FEAT_SME2 |
|    11 |   1 | LDNT1D (scalar plus scalar, strided registers) | FEAT_SME2 |

## SME2 multi-vec non-contiguous load (scalar plus scalar, four registers)

The encodings in this section are decoded from SME2 Multi-vector - Memory (Strided).

<!-- image -->

| 31                    | 21 20   | 16 15 14 13 12 10 9 5 4 3   |
|-----------------------|---------|-----------------------------|
| 1 0 1 0 0 0 0 1 0 0 0 | Rm 1    | msz PNg Rn T N              |

|   msz |   N | Instruction Details                            | Feature   |
|-------|-----|------------------------------------------------|-----------|
|    00 |   0 | LD1B (scalar plus scalar, strided registers)   | FEAT_SME2 |
|    00 |   1 | LDNT1B (scalar plus scalar, strided registers) | FEAT_SME2 |
|    01 |   0 | LD1H(scalar plus scalar, strided registers)    | FEAT_SME2 |
|    01 |   1 | LDNT1H (scalar plus scalar, strided registers) | FEAT_SME2 |
|    10 |   0 | LD1W(scalar plus scalar, strided registers)    | FEAT_SME2 |
|    10 |   1 | LDNT1W (scalar plus scalar, strided registers) | FEAT_SME2 |
|    11 |   0 | LD1D(scalar plus scalar, strided registers)    | FEAT_SME2 |
|    11 |   1 | LDNT1D (scalar plus scalar, strided registers) | FEAT_SME2 |

## SME2 multi-vec non-contiguous store (scalar plus scalar, two registers)

The encodings in this section are decoded from SME2 Multi-vector - Memory (Strided).

<!-- image -->

| 31                    | 21 20   | 16 15 14 13 12 10 9   |
|-----------------------|---------|-----------------------|
| 1 0 1 0 0 0 0 1 0 0 1 | Rm 0    | msz PNg Rn            |

|   msz |   N | Instruction Details                            | Feature   |
|-------|-----|------------------------------------------------|-----------|
|    00 |   0 | ST1B (scalar plus scalar, strided registers)   | FEAT_SME2 |
|    00 |   1 | STNT1B (scalar plus scalar, strided registers) | FEAT_SME2 |
|    01 |   0 | ST1H (scalar plus scalar, strided registers)   | FEAT_SME2 |
|    01 |   1 | STNT1H (scalar plus scalar, strided registers) | FEAT_SME2 |
|    10 |   0 | ST1W (scalar plus scalar, strided registers)   | FEAT_SME2 |
|    10 |   1 | STNT1W (scalar plus scalar, strided registers) | FEAT_SME2 |
|    11 |   0 | ST1D (scalar plus scalar, strided registers)   | FEAT_SME2 |
|    11 |   1 | STNT1D (scalar plus scalar, strided registers) | FEAT_SME2 |

SME2 multi-vec non-contiguous store (scalar plus scalar, four registers)

The encodings in this section are decoded from SME2 Multi-vector - Memory (Strided).

<!-- image -->

|   msz |   N | Instruction Details                            | Feature   |
|-------|-----|------------------------------------------------|-----------|
|    00 |   0 | ST1B (scalar plus scalar, strided registers)   | FEAT_SME2 |
|    00 |   1 | STNT1B (scalar plus scalar, strided registers) | FEAT_SME2 |
|    01 |   0 | ST1H (scalar plus scalar, strided registers)   | FEAT_SME2 |
|    01 |   1 | STNT1H (scalar plus scalar, strided registers) | FEAT_SME2 |
|    10 |   0 | ST1W (scalar plus scalar, strided registers)   | FEAT_SME2 |
|    10 |   1 | STNT1W (scalar plus scalar, strided registers) | FEAT_SME2 |

|   msz | N Instruction Details                            | Feature   |
|-------|--------------------------------------------------|-----------|
|    11 | 0 ST1D (scalar plus scalar, strided registers)   | FEAT_SME2 |
|    11 | 1 STNT1D (scalar plus scalar, strided registers) | FEAT_SME2 |

## SME2 multi-vec non-contiguous load (scalar plus immediate, two registers)

The encodings in this section are decoded from SME2 Multi-vector - Memory (Strided).

<!-- image -->

| 31   | 23 22 20          | 16 15 14   | 13 12   | 10   | 5 4   | 3   | 2   | 0   |
|------|-------------------|------------|---------|------|-------|-----|-----|-----|
| 1 0  | 0 0 0 0 1 0 1 0 0 |            | 0 msz   |      | Rn    | T   | N   | Zt  |

|   msz |   N | Instruction Details                               | Feature   |
|-------|-----|---------------------------------------------------|-----------|
|    00 |   0 | LD1B (scalar plus immediate, strided registers)   | FEAT_SME2 |
|    00 |   1 | LDNT1B (scalar plus immediate, strided registers) | FEAT_SME2 |
|    01 |   0 | LD1H (scalar plus immediate, strided registers)   | FEAT_SME2 |
|    01 |   1 | LDNT1H (scalar plus immediate, strided registers) | FEAT_SME2 |
|    10 |   0 | LD1W (scalar plus immediate, strided registers)   | FEAT_SME2 |
|    10 |   1 | LDNT1W (scalar plus immediate, strided registers) | FEAT_SME2 |
|    11 |   0 | LD1D (scalar plus immediate, strided registers)   | FEAT_SME2 |
|    11 |   1 | LDNT1D (scalar plus immediate, strided registers) | FEAT_SME2 |

## SME2 multi-vec non-contiguous load (scalar plus immediate, four registers)

The encodings in this section are decoded from SME2 Multi-vector - Memory (Strided).

<!-- image -->

| 31      | 23 22 20 19        | 16 15 14 13 12 10 9 5 4 3 2   |
|---------|--------------------|-------------------------------|
| 1 0 1 0 | 0 1 0 0 imm4 1 msz | PNg Rn T N 0                  |

|   msz |   N | Instruction Details                               | Feature   |
|-------|-----|---------------------------------------------------|-----------|
|    00 |   0 | LD1B (scalar plus immediate, strided registers)   | FEAT_SME2 |
|    00 |   1 | LDNT1B (scalar plus immediate, strided registers) | FEAT_SME2 |
|    01 |   0 | LD1H (scalar plus immediate, strided registers)   | FEAT_SME2 |
|    01 |   1 | LDNT1H (scalar plus immediate, strided registers) | FEAT_SME2 |
|    10 |   0 | LD1W (scalar plus immediate, strided registers)   | FEAT_SME2 |
|    10 |   1 | LDNT1W (scalar plus immediate, strided registers) | FEAT_SME2 |
|    11 |   0 | LD1D (scalar plus immediate, strided registers)   | FEAT_SME2 |
|    11 |   1 | LDNT1D (scalar plus immediate, strided registers) | FEAT_SME2 |

SME2 multi-vec non-contiguous store (scalar plus immediate, two registers)

The encodings in this section are decoded from SME2 Multi-vector - Memory (Strided).

<!-- image -->

| 31   | 23 22 20 19       | 16 15 14 13   | 10   | 5   | 4 3   | 2   | 0   |
|------|-------------------|---------------|------|-----|-------|-----|-----|
| 1 0  | 0 0 0 0 1 0 1 1 0 | imm4 0 msz    | PNg  | Rn  | T     | N   | Zt  |

|   msz |   N | Instruction Details                               | Feature   |
|-------|-----|---------------------------------------------------|-----------|
|    00 |   0 | ST1B (scalar plus immediate, strided registers)   | FEAT_SME2 |
|    00 |   1 | STNT1B (scalar plus immediate, strided registers) | FEAT_SME2 |
|    01 |   0 | ST1H (scalar plus immediate, strided registers)   | FEAT_SME2 |
|    01 |   1 | STNT1H (scalar plus immediate, strided registers) | FEAT_SME2 |
|    10 |   0 | ST1W (scalar plus immediate, strided registers)   | FEAT_SME2 |
|    10 |   1 | STNT1W (scalar plus immediate, strided registers) | FEAT_SME2 |
|    11 |   0 | ST1D (scalar plus immediate, strided registers)   | FEAT_SME2 |
|    11 |   1 | STNT1D (scalar plus immediate, strided registers) | FEAT_SME2 |

## SME2 multi-vec non-contiguous store (scalar plus immediate, four registers)

The encodings in this section are decoded from SME2 Multi-vector - Memory (Strided).

<!-- image -->

| 31    | 23 22 20 19   | 16 15 14 13 12 10 9 5 4 3 2 1   |
|-------|---------------|---------------------------------|
| 1 0 1 | 0 1 1 0 imm4  | 1 msz PNg Rn T N 0 Zt           |

|   msz |   N | Instruction Details                               | Feature   |
|-------|-----|---------------------------------------------------|-----------|
|    00 |   0 | ST1B (scalar plus immediate, strided registers)   | FEAT_SME2 |
|    00 |   1 | STNT1B (scalar plus immediate, strided registers) | FEAT_SME2 |
|    01 |   0 | ST1H (scalar plus immediate, strided registers)   | FEAT_SME2 |
|    01 |   1 | STNT1H (scalar plus immediate, strided registers) | FEAT_SME2 |
|    10 |   0 | ST1W (scalar plus immediate, strided registers)   | FEAT_SME2 |
|    10 |   1 | STNT1W (scalar plus immediate, strided registers) | FEAT_SME2 |
|    11 |   0 | ST1D (scalar plus immediate, strided registers)   | FEAT_SME2 |
|    11 |   1 | STNT1D (scalar plus immediate, strided registers) | FEAT_SME2 |

## SME Integer Outer Product - 32 bit

SMEInteger Outer Product - 32 bit

The encodings in this section are decoded from SME encodings.

| 31              | 25 24 23 22 21 20 4 3 2   |
|-----------------|---------------------------|
| 1 0 1 0 0 0 0 1 | 0 op0 op1 0               |

| op0   |   op1 | Instruction details              |
|-------|-------|----------------------------------|
| 0     |     1 | SME2 Int16 two-way outer product |
| 1     |     1 | UNALLOCATED                      |
| x     |     0 | SMEInt8 outer product            |

## SME2 Int16 two-way outer product

The encodings in this section are decoded from SME Integer Outer Product - 32 bit.

<!-- image -->

|   31 | 25 24 23 22 21 20    | 16 15   | 13 12   | 10 9   | 5 4   | 3 2   | 1 0   |
|------|----------------------|---------|---------|--------|-------|-------|-------|
|    1 | 0 1 0 0 0 0 u0 1 0 0 | Zm      | Pm      | Pn     | S     | 1 0   | ZAda  |

|   u0 | S Instruction   | Details Feature   |
|------|-----------------|-------------------|
|    0 | 0 SMOPA(2-way)  | FEAT_SME2         |
|    0 | 1 SMOPS (2-way) | FEAT_SME2         |
|    1 | 0 UMOPA(2-way)  | FEAT_SME2         |
|    1 | 1 UMOPS(2-way)  | FEAT_SME2         |

## SME Int8 outer product

The encodings in this section are decoded from SME Integer Outer Product - 32 bit.

<!-- image -->

|   u0 |   u1 |   S | Instruction Details   | Feature   |
|------|------|-----|-----------------------|-----------|
|    0 |    0 |   0 | SMOPA(4-way)          | FEAT_SME  |
|    0 |    0 |   1 | SMOPS (4-way)         | FEAT_SME  |
|    0 |    1 |   0 | SUMOPA(4-way)         | FEAT_SME  |
|    0 |    1 |   1 | SUMOPS                | FEAT_SME  |
|    1 |    0 |   0 | USMOPA(4-way)         | FEAT_SME  |
|    1 |    0 |   1 | USMOPS                | FEAT_SME  |
|    1 |    1 |   0 | UMOPA(4-way)          | FEAT_SME  |
|    1 |    1 |   1 | UMOPS(4-way)          | FEAT_SME  |

## SME2 Quarter Tile Outer Product - 64-bit

SME2 Quarter Tile Outer Product - 64-bit

The encodings in this section are decoded from SME encodings.

<!-- image -->

| 31 30   | 17 16         | 10 9 6 5 4 3   |
|---------|---------------|----------------|
| 1 0     | 0 0 0 0 0 0 0 | 0 1            |

## SME2 FP64 non-widening quarter tile outer product

The encodings in this section are decoded from SME2 Quarter Tile Outer Product - 64-bit.

<!-- image -->

| 31 30 29   | 28    | 25 24   |   23 |   22 |   21 | 20 19   | 17   | 16   | 10        | 9   | 8   | 6   |   5 | 4   |   3 | 0    |
|------------|-------|---------|------|------|------|---------|------|------|-----------|-----|-----|-----|-----|-----|-----|------|
| 1 0 0      | 0 0 0 | 0 0     |    1 |    1 |    0 | M       | Zm   | 0 0  | 0 0 0 0 0 | N   |     | Zn  |   0 | S   |   1 | ZAda |

|   M |   N |   S | Instruction Details                                                    | Feature                         |
|-----|-----|-----|------------------------------------------------------------------------|---------------------------------|
|   0 |   0 |   0 | FMOP4A (non-widening) - Double- precision, single vectors              | FEAT_SME_MOP4 &&FEAT_SME_F64F64 |
|   0 |   0 |   1 | FMOP4S (non-widening) - Double- precision, single vectors              | FEAT_SME_MOP4 &&FEAT_SME_F64F64 |
|   0 |   1 |   0 | FMOP4A (non-widening) - Double- precision, multiple and single vectors | FEAT_SME_MOP4 &&FEAT_SME_F64F64 |
|   0 |   1 |   1 | FMOP4S (non-widening) - Double- precision, multiple and single vectors | FEAT_SME_MOP4 &&FEAT_SME_F64F64 |
|   1 |   0 |   0 | FMOP4A (non-widening) - Double- precision, single and multiple vectors | FEAT_SME_MOP4 &&FEAT_SME_F64F64 |
|   1 |   0 |   1 | FMOP4S (non-widening) - Double- precision, single and multiple vectors | FEAT_SME_MOP4 &&FEAT_SME_F64F64 |
|   1 |   1 |   0 | FMOP4A (non-widening) - Double- precision, multiple vectors            | FEAT_SME_MOP4 &&FEAT_SME_F64F64 |
|   1 |   1 |   1 | FMOP4S (non-widening) - Double- precision, multiple vectors            | FEAT_SME_MOP4 &&FEAT_SME_F64F64 |

## SME2 Int16 to Int64 quarter tile outer product

The encodings in this section are decoded from SME2 Quarter Tile Outer Product - 64-bit.

<!-- image -->

|   31 | 29 28   | 25 24   |    |   23 | 22   | 21 20   | 19   |    | 17 16         | 10 9   | 8   | 6 5   |    | 4   |   3 | 0    |
|------|---------|---------|----|------|------|---------|------|----|---------------|--------|-----|-------|----|-----|-----|------|
|    1 | 1 0 0 0 | 0 u0    |  1 |    1 | u1   | M       |      | Zm | 0 0 0 0 0 0 0 | N      |     | Zn    |  0 | S   |   1 | ZAda |

|   op0 | op1   | op2   | Instruction details                               |
|-------|-------|-------|---------------------------------------------------|
|     0 | 0     | 0     | SME2 FP64 non-widening quarter tile outer product |
|     0 | 0     | 1     | UNALLOCATED                                       |
|     0 | 1     | x     | UNALLOCATED                                       |
|     1 | x     | x     | SME2 Int16 to Int64 quarter tile outer product    |

|   u0 |   u1 |   M |   N |   S | Instruction Details                                  | Feature                         |
|------|------|-----|-----|-----|------------------------------------------------------|---------------------------------|
|    0 |    0 |   0 |   0 |   0 | SMOP4A(4-way) -64-bit, single vectors                | FEAT_SME_MOP4 &&FEAT_SME_I16I64 |
|    0 |    0 |   0 |   0 |   1 | SMOP4S (4-way) -64-bit, single vectors               | FEAT_SME_MOP4 &&FEAT_SME_I16I64 |
|    0 |    0 |   0 |   1 |   0 | SMOP4A (4-way) -64-bit, multiple and single vectors  | FEAT_SME_MOP4 &&FEAT_SME_I16I64 |
|    0 |    0 |   0 |   1 |   1 | SMOP4S (4-way) -64-bit, multiple and single vectors  | FEAT_SME_MOP4 &&FEAT_SME_I16I64 |
|    0 |    0 |   1 |   0 |   0 | SMOP4A (4-way) - 64-bit, single and multiple vectors | FEAT_SME_MOP4 &&FEAT_SME_I16I64 |
|    0 |    0 |   1 |   0 |   1 | SMOP4S (4-way) - 64-bit, single and multiple vectors | FEAT_SME_MOP4 &&FEAT_SME_I16I64 |
|    0 |    0 |   1 |   1 |   0 | SMOP4A (4-way) - 64-bit, multiple vectors            | FEAT_SME_MOP4 &&FEAT_SME_I16I64 |
|    0 |    0 |   1 |   1 |   1 | SMOP4S (4-way) - 64-bit, multiple vectors            | FEAT_SME_MOP4 &&FEAT_SME_I16I64 |
|    0 |    1 |   0 |   0 |   0 | SUMOP4A -64-bit, single vectors                      | FEAT_SME_MOP4 &&FEAT_SME_I16I64 |
|    0 |    1 |   0 |   0 |   1 | SUMOP4S -64-bit, single vectors                      | FEAT_SME_MOP4 &&FEAT_SME_I16I64 |
|    0 |    1 |   0 |   1 |   0 | SUMOP4A -64-bit, multiple and single vectors         | FEAT_SME_MOP4 &&FEAT_SME_I16I64 |
|    0 |    1 |   0 |   1 |   1 | SUMOP4S - 64-bit, multiple and single vectors        | FEAT_SME_MOP4 &&FEAT_SME_I16I64 |
|    0 |    1 |   1 |   0 |   0 | SUMOP4A -64-bit, single and multiple vectors         | FEAT_SME_MOP4 &&FEAT_SME_I16I64 |
|    0 |    1 |   1 |   0 |   1 | SUMOP4S - 64-bit, single and multiple vectors        | FEAT_SME_MOP4 &&FEAT_SME_I16I64 |
|    0 |    1 |   1 |   1 |   0 | SUMOP4A -64-bit, multiple vectors                    | FEAT_SME_MOP4 &&FEAT_SME_I16I64 |
|    0 |    1 |   1 |   1 |   1 | SUMOP4S -64-bit, multiple vectors                    | FEAT_SME_MOP4 &&FEAT_SME_I16I64 |
|    1 |    0 |   0 |   0 |   0 | USMOP4A -64-bit, single vectors                      | FEAT_SME_MOP4 &&FEAT_SME_I16I64 |
|    1 |    0 |   0 |   0 |   1 | USMOP4S -64-bit, single vectors                      | FEAT_SME_MOP4 &&FEAT_SME_I16I64 |
|    1 |    0 |   0 |   1 |   0 | USMOP4A -64-bit, multiple and single vectors         | FEAT_SME_MOP4 &&FEAT_SME_I16I64 |
|    1 |    0 |   0 |   1 |   1 | USMOP4S - 64-bit, multiple and single vectors        | FEAT_SME_MOP4 &&FEAT_SME_I16I64 |
|    1 |    0 |   1 |   0 |   0 | USMOP4A -64-bit, single and multiple vectors         | FEAT_SME_MOP4 &&FEAT_SME_I16I64 |
|    1 |    0 |   1 |   0 |   1 | USMOP4S - 64-bit, single and multiple vectors        | FEAT_SME_MOP4 &&FEAT_SME_I16I64 |
|    1 |    0 |   1 |   1 |   0 | USMOP4A -64-bit, multiple vectors                    | FEAT_SME_MOP4 &&FEAT_SME_I16I64 |
|    1 |    0 |   1 |   1 |   1 | USMOP4S -64-bit, multiple vectors                    | FEAT_SME_MOP4 &&FEAT_SME_I16I64 |
|    1 |    1 |   0 |   0 |   0 | UMOP4A (4-way) - 64-bit, single vectors              | FEAT_SME_MOP4 &&FEAT_SME_I16I64 |
|    1 |    1 |   0 |   0 |   1 | UMOP4S(4-way) -64-bit, single vectors                | FEAT_SME_MOP4 &&FEAT_SME_I16I64 |
|    1 |    1 |   0 |   1 |   0 | UMOP4A (4-way) -64-bit, multiple and single vectors  | FEAT_SME_MOP4 &&FEAT_SME_I16I64 |

|   u0 |   u1 |   M |   N | S   | Instruction Details                                   | Feature                         |
|------|------|-----|-----|-----|-------------------------------------------------------|---------------------------------|
|    1 |    1 |   0 |   1 |     | 1 UMOP4S (4-way) -64-bit, multiple and single vectors | FEAT_SME_MOP4 &&FEAT_SME_I16I64 |
|    1 |    1 |   1 |   0 | 0   | UMOP4A (4-way) - 64-bit, single and multiple vectors  | FEAT_SME_MOP4 &&FEAT_SME_I16I64 |
|    1 |    1 |   1 |   0 | 1   | UMOP4S (4-way) - 64-bit, single and multiple vectors  | FEAT_SME_MOP4 &&FEAT_SME_I16I64 |
|    1 |    1 |   1 |   1 |     | 0 UMOP4A (4-way) - 64-bit, multiple vectors           | FEAT_SME_MOP4 &&FEAT_SME_I16I64 |
|    1 |    1 |   1 |   1 | 1   | UMOP4S (4-way) - 64-bit, multiple vectors             | FEAT_SME_MOP4 &&FEAT_SME_I16I64 |

## SME Outer Product - 64 bit

SMEOuter Product - 64 bit

The encodings in this section are decoded from SME encodings.

| 31 30   | 29 28 25 24 23 22   |   4 3 2 |
|---------|---------------------|---------|
| 1 0     | op0 0 0 0 0 op1 1 1 |       0 |

|   op0 | op1   | op2   | Instruction details    |
|-------|-------|-------|------------------------|
|     0 | 0     | 0     | SMEFP64 outer product  |
|     0 | 0     | 1     | UNALLOCATED            |
|     0 | 1     | x     | UNALLOCATED            |
|     1 | x     | x     | SMEInt16 outer product |

## SME FP64 outer product

The encodings in this section are decoded from SME Outer Product - 64 bit.

<!-- image -->

| 31 30 29 28       | 25 24 23 22 21 20   | 16 15 13 12 10 9 5 4   |
|-------------------|---------------------|------------------------|
| 1 0 0 0 0 0 0 0 1 | 1 0 Zm              | Pm Pn Zn S             |

|   S | Instruction Details   | Feature         |
|-----|-----------------------|-----------------|
|   0 | FMOPA(non-widening)   | FEAT_SME_F64F64 |
|   1 | FMOPS (non-widening)  | FEAT_SME_F64F64 |

## SME Int16 outer product

The encodings in this section are decoded from SME Outer Product - 64 bit.

<!-- image -->

|   31 30 | 29 28   | 16 15   | 25 24 23 22 20 12   |   10 9 | 13 5 4   | 21   | 3     |    |    |    | 0    |
|---------|---------|---------|---------------------|--------|----------|------|-------|----|----|----|------|
|       1 | 0 1     |         | 0 0 0 0 u0          |      1 | 1 Pm     | u1   | Zm Pn | Zn | S  |  0 | ZAda |

|   u0 |   u1 |   S | Instruction Details   | Feature         |
|------|------|-----|-----------------------|-----------------|
|    0 |    0 |   0 | SMOPA(4-way)          | FEAT_SME_I16I64 |
|    0 |    0 |   1 | SMOPS (4-way)         | FEAT_SME_I16I64 |
|    0 |    1 |   0 | SUMOPA(4-way)         | FEAT_SME_I16I64 |
|    0 |    1 |   1 | SUMOPS                | FEAT_SME_I16I64 |
|    1 |    0 |   0 | USMOPA(4-way)         | FEAT_SME_I16I64 |
|    1 |    0 |   1 | USMOPS                | FEAT_SME_I16I64 |
|    1 |    1 |   0 | UMOPA(4-way)          | FEAT_SME_I16I64 |
|    1 |    1 |   1 | UMOPS(4-way)          | FEAT_SME_I16I64 |

## SME zero array

SMEzero array

The encodings in this section are decoded from SME encodings.

<!-- image -->

| 31                          | 18 17   |
|-----------------------------|---------|
| 1 1 0 0 0 0 0 0 0 0 0 0 1 0 | op0     |

| op0           | Instruction details   | Feature   |
|---------------|-----------------------|-----------|
| 0000000000    | ZERO (tiles)          | FEAT_SME  |
| != 0000000000 | UNALLOCATED           | -         |

## SME2 Multiple Zero

SME2 Multiple Zero

The encodings in this section are decoded from SME encodings.

<!-- image -->

| 31                        | 13 12 3 2   |
|---------------------------|-------------|
| 1 1 0 0 0 0 0 0 0 0 0 0 1 | op0         |

## SME multiple vectors zero array

The encodings in this section are decoded from SME2 Multiple Zero.

<!-- image -->

| 31                        | 18 17 15 14 13 12 3 2             |
|---------------------------|-----------------------------------|
| 1 1 0 0 0 0 0 0 0 0 0 0 1 | 1 opc Rv 0 0 0 0 0 0 0 0 0 0 opc2 |

| opc   | opc2   | Instruction Details                           | Feature     |
|-------|--------|-----------------------------------------------|-------------|
| x1x   | 1xx    | UNALLOCATED                                   | -           |
| 000   | xxx    | ZERO (single-vector) - Two ZA single- vectors | FEAT_SME2p1 |
| 001   | xxx    | ZERO (double-vector) -OneZAdouble- vector     | FEAT_SME2p1 |
| 010   | 0xx    | ZERO(double-vector) -TwoZAdouble- vectors     | FEAT_SME2p1 |
| 011   | 0xx    | ZERO(double-vector) -FourZAdouble- vectors    | FEAT_SME2p1 |
| 100   | xxx    | ZERO (single-vector) -Four ZA single- vectors | FEAT_SME2p1 |
| 101   | 0xx    | ZERO (quad-vector) - One ZA quad- vector      | FEAT_SME2p1 |
| 101   | 1xx    | UNALLOCATED                                   | -           |
| 11x   | 01x    | UNALLOCATED                                   | -           |
| 110   | 00x    | ZERO (quad-vector) - Two ZA quad- vectors     | FEAT_SME2p1 |
| 111   | 00x    | ZERO (quad-vector) - Four ZA quad- vectors    | FEAT_SME2p1 |

## SME2 zero lookup table

The encodings in this section are decoded from SME encodings.

<!-- image -->

| 31 18                       | 4 3   |
|-----------------------------|-------|
| 1 1 0 0 0 0 0 0 0 1 0 0 1 0 | opc   |

| op0           | Instruction details            |
|---------------|--------------------------------|
| 0000000000    | SMEmultiple vectors zero array |
| != 0000000000 | UNALLOCATED                    |

| op0               | opc     | Instruction Details   | Feature   |
|-------------------|---------|-----------------------|-----------|
| 00000000000000    | 0001    | ZERO (table)          | FEAT_SME2 |
| 00000000000000    | != 0001 | UNALLOCATED           | -         |
| != 00000000000000 | xxxx    | UNALLOCATED           | -         |

## SME2 Move Lookup Table

SME2 Move Lookup Table

The encodings in this section are decoded from SME encodings.

<!-- image -->

| 31   | 18        | 17 16 15 14   |
|------|-----------|---------------|
| 1 1  | 1 op0 op1 | op2           |

| op0   | op1   | op2   | Instruction details              |
|-------|-------|-------|----------------------------------|
| 0     | 00    | x     | SME2 move from lookup table      |
| 0     | 10    | x     | UNALLOCATED                      |
| 1     | 00    | x     | SME2 move into lookup table      |
| 1     | 10    | 0     | SME2 move vector to lookup table |
| 1     | 10    | 1     | UNALLOCATED                      |
| x     | x1    | x     | UNALLOCATED                      |

## SME2 move from lookup table

The encodings in this section are decoded from SME2 Move Lookup Table.

<!-- image -->

| opc        | Instruction Details   | Feature   |
|------------|-----------------------|-----------|
| 0011111    | MOVT(table to scalar) | FEAT_SME2 |
| != 0011111 | UNALLOCATED           | -         |

## SME2 move into lookup table

The encodings in this section are decoded from SME2 Move Lookup Table.

<!-- image -->

| 31    | 18 17 16 15 14 12 11 5 4   |
|-------|----------------------------|
| 1 1 0 | 1 1 0 0 imm3 opc Rt        |

| opc        | Instruction Details   | Feature   |
|------------|-----------------------|-----------|
| 0011111    | MOVT(scalar to table) | FEAT_SME2 |
| != 0011111 | UNALLOCATED           | -         |

## SME2 move vector to lookup table

The encodings in this section are decoded from SME2 Move Lookup Table.

<!-- image -->

| 31    | 17 16 15 14 13 12 11 5 4   |
|-------|----------------------------|
| 1 1 0 | 1 1 0 0 off2 opc Zt        |

| opc        | Instruction Details   | Feature        |
|------------|-----------------------|----------------|
| 0011111    | MOVT(vector to table) | FEAT_SME_LUTv2 |
| != 0011111 | UNALLOCATED           | -              |

## SME2 Expand Lookup Table (Non-contiguous)

SME2 Expand Lookup Table (Non-contiguous)

The encodings in this section are decoded from SME encodings.

<!-- image -->

| 31                    | 19 18   | 16 15 14 13 6 5   |
|-----------------------|---------|-------------------|
| 1 1 0 0 0 0 0 0 1 0 0 | 1 op0   | op1 op2           |

| op0   | op1   | op2   |   op3 | Instruction details                                                                        |
|-------|-------|-------|-------|--------------------------------------------------------------------------------------------|
| 011   | 00    | 0     |    00 | SME2 lookup table two source registers expand to four non-contiguous destination registers |
| 011   | 00    | 1     |    00 | UNALLOCATED                                                                                |
| xxx   | 10    | x     |    00 | SME2 lookup table expand four non- contiguous registers                                    |
| xxx   | x0    | x     |    01 | UNALLOCATED                                                                                |

| op0    | op1   | op2   | op3   | Instruction details                                    |
|--------|-------|-------|-------|--------------------------------------------------------|
| xxx    | x1    | x     | 0x    | SME2 lookup table expand two non- contiguous registers |
| xxx    | xx    | x     | 1x    | UNALLOCATED                                            |
| != 011 | 00    | x     | 00    | UNALLOCATED                                            |

## SME2 lookup table two source registers expand to four non-contiguous destination registers

The encodings in this section are decoded from SME2 Expand Lookup Table (Non-contiguous).

<!-- image -->

| 31    | 19 18 16 15 14 13 12 11 10 9 6 5 4 3 2 1   |
|-------|--------------------------------------------|
| 1 1 0 | 1 1 0 1 1 0 0 size opc Zn 0 D 0 0          |

| opc   | Instruction Details           | Feature                      |
|-------|-------------------------------|------------------------------|
| 00    | LUTI4 (four registers, 8-bit) | FEAT_SME2p1 &&FEAT_SME_LUTv2 |
| != 00 | UNALLOCATED                   | -                            |

## SME2 lookup table expand four non-contiguous registers

The encodings in this section are decoded from SME2 Expand Lookup Table (Non-contiguous).

<!-- image -->

| 31                        | 19 18   | 16 15 14 13 12 11 10 9 5 4 3 2 1   |
|---------------------------|---------|------------------------------------|
| 1 1 0 0 0 0 0 0 1 0 0 1 1 | opc 1 0 | size opc2 Zn D 0 0 Zd              |

| opc   | opc2   | Instruction Details                       | Feature     |
|-------|--------|-------------------------------------------|-------------|
| xxx   | != 00  | UNALLOCATED                               | -           |
| 00x   | 00     | UNALLOCATED                               | -           |
| 01x   | 00     | LUTI4 (four registers, 16-bit and 32-bit) | FEAT_SME2p1 |
| 1xx   | 00     | LUTI2 (four registers)                    | FEAT_SME2p1 |

## SME2 lookup table expand two non-contiguous registers

The encodings in this section are decoded from SME2 Expand Lookup Table (Non-contiguous).

<!-- image -->

| opc   | opc2   | Instruction Details   | Feature     |
|-------|--------|-----------------------|-------------|
| xxxx  | != 00  | UNALLOCATED           | -           |
| 00xx  | 00     | UNALLOCATED           | -           |
| 01xx  | 00     | LUTI4 (two registers) | FEAT_SME2p1 |
| 1xxx  | 00     | LUTI2 (two registers) | FEAT_SME2p1 |

## SME2 Expand Lookup Table (Contiguous)

SME2 Expand Lookup Table (Contiguous)

The encodings in this section are decoded from SME encodings.

<!-- image -->

| 31   | 23 22 21    | 19 18   | 6 5 4 2 1   |
|------|-------------|---------|-------------|
| 1 1  | 1 op0 0 0 1 | op1     | op2 op3     |

|   op0 | op1   | op2   | op3   | Instruction details                                                                    |
|-------|-------|-------|-------|----------------------------------------------------------------------------------------|
|     0 | 00x00 | x     | 00    | UNALLOCATED                                                                            |
|     0 | 01000 | x     | 00    | UNALLOCATED                                                                            |
|     0 | 01100 | 0     | 00    | SME2 lookup table two source registers expand to four contiguous destination registers |
|     0 | 01100 | 1     | 00    | UNALLOCATED                                                                            |
|     0 | 1xx00 | x     | 00    | UNALLOCATED                                                                            |
|     0 | xxx10 | x     | 00    | SME2lookuptableexpandfour contiguous registers                                         |
|     0 | xxxx0 | x     | 10    | UNALLOCATED                                                                            |
|     0 | xxxx1 | x     | x0    | SME2lookup table expand two contiguous registers                                       |
|     0 | xxxxx | x     | x1    | UNALLOCATED                                                                            |
|     1 | xxxxx | x     | xx    | SME2 lookup table expand one register                                                  |

## SME2 lookup table two source registers expand to four contiguous destination registers

The encodings in this section are decoded from SME2 Expand Lookup Table (Contiguous).

<!-- image -->

| opc   | Instruction Details           | Feature        |
|-------|-------------------------------|----------------|
| 00    | LUTI4 (four registers, 8-bit) | FEAT_SME_LUTv2 |
| != 00 | UNALLOCATED                   | -              |

## SME2 lookup table expand four contiguous registers

The encodings in this section are decoded from SME2 Expand Lookup Table (Contiguous).

<!-- image -->

| 31   | 23 22 21 16     | 19 18 11 10    | 15 14 13 12 9 5 4 2 1 0   |
|------|-----------------|----------------|---------------------------|
| 1 1  | 1 0 0 0 1 opc 1 | 0 size opc2 Zd | Zn 0 0                    |

| opc   | opc2   | Instruction Details                       | Feature   |
|-------|--------|-------------------------------------------|-----------|
| xxx   | != 00  | UNALLOCATED                               | -         |
| 00x   | 00     | UNALLOCATED                               | -         |
| 01x   | 00     | LUTI4 (four registers, 16-bit and 32-bit) | FEAT_SME2 |
| 1xx   | 00     | LUTI2 (four registers)                    | FEAT_SME2 |

## SME2 lookup table expand two contiguous registers

The encodings in this section are decoded from SME2 Expand Lookup Table (Contiguous).

<!-- image -->

| opc   | opc2   | Instruction Details   | Feature   |
|-------|--------|-----------------------|-----------|
| xxxx  | != 00  | UNALLOCATED           | -         |
| 00xx  | 00     | UNALLOCATED           | -         |
| 01xx  | 00     | LUTI4 (two registers) | FEAT_SME2 |
| 1xxx  | 00     | LUTI2 (two registers) | FEAT_SME2 |

## SME2 lookup table expand one register

The encodings in this section are decoded from SME2 Expand Lookup Table (Contiguous).

<!-- image -->

| 31   | 23 22 21          | 19 18   | 14 13 12 11 10   |      | 5 4   |    |
|------|-------------------|---------|------------------|------|-------|----|
| 1 1  | 0 0 0 0 0 1 1 0 0 | 1 opc   | size             | opc2 | Zn    | Zd |

| opc   | opc2   | Instruction Details   | Feature   |
|-------|--------|-----------------------|-----------|
| xxxxx | != 00  | UNALLOCATED           | -         |
| 00xxx | 00     | UNALLOCATED           | -         |
| 01xxx | 00     | LUTI4 (single)        | FEAT_SME2 |
| 1xxxx | 00     | LUTI2 (single)        | FEAT_SME2 |

## SME Move into Array

SMEMove into Array

The encodings in this section are decoded from SME encodings.

<!-- image -->

| 31        | 24 23 22 21 19 18 17 16 15 14 13 12 10 9 7 6 5 4   |
|-----------|----------------------------------------------------|
| 1 1 0 0 0 | 0 op0 0 0 0 op1 0 op2 op3 op4 0                    |

| op0   |   op1 | op2   | op3   | op4   | op5   | Instruction details                      | Feature   |
|-------|-------|-------|-------|-------|-------|------------------------------------------|-----------|
| 00    |     1 | 00    | 010   | x0    | 0     | MOVA(vector to array, two registers)     | FEAT_SME2 |
| 00    |     1 | 00    | 011   | 00    | 0     | MOVA(vector to array, four registers)    | FEAT_SME2 |
| 00    |     1 | 00    | 011   | 10    | 0     | UNALLOCATED                              | -         |
| 00    |     1 | 01    | 01x   | x0    | 0     | UNALLOCATED                              | -         |
| xx    |     0 | xx    | xxx   | xx    | x     | SMEmove vector to array                  | -         |
| xx    |     1 | 0x    | 000   | x0    | 0     | SME2 move vector to tile, two registers  | -         |
| xx    |     1 | 0x    | 001   | 00    | 0     | SME2 move vector to tile, four registers | -         |
| xx    |     1 | 0x    | 001   | 10    | 0     | UNALLOCATED                              | -         |
| xx    |     1 | 0x    | 0xx   | x0    | 1     | UNALLOCATED                              | -         |
| xx    |     1 | 0x    | 0xx   | x1    | x     | UNALLOCATED                              | -         |
| xx    |     1 | 0x    | 1xx   | xx    | x     | UNALLOCATED                              | -         |
| xx    |     1 | 1x    | xxx   | xx    | x     | UNALLOCATED                              | -         |
| != 00 |     1 | 0x    | 01x   | x0    | 0     | UNALLOCATED                              | -         |

## SME move vector to array

The encodings in this section are decoded from SME Move into Array.

<!-- image -->

| 31      | 24 23 22         | 21 14 13 12   | 19 18 17 16 15 10 9 5 4 3   |
|---------|------------------|---------------|-----------------------------|
| 1 1 0 0 | 0 size 0 0 0 0 0 | Q V Rs 0      | Pg Zn opc                   |

| size   |   Q | Instruction Details                   | Feature   |
|--------|-----|---------------------------------------|-----------|
| 00     |   0 | MOVA(vector to tile, single) -8-bit   | FEAT_SME  |
| 01     |   0 | MOVA(vector to tile, single) -16-bit  | FEAT_SME  |
| 10     |   0 | MOVA(vector to tile, single) -32-bit  | FEAT_SME  |
| 11     |   0 | MOVA(vector to tile, single) -64-bit  | FEAT_SME  |
| 11     |   1 | MOVA(vector to tile, single) -128-bit | FEAT_SME  |
| != 11  |   1 | UNALLOCATED                           | -         |

## SME2 move vector to tile, two registers

The encodings in this section are decoded from SME Move into Array.

<!-- image -->

| 31    | 24 23 22 21 19 18 17 16 15 14 13 12 10 9 6 5 4 3 2   |
|-------|------------------------------------------------------|
| 1 1 0 | 0 size 0 0 0 1 0 0 V Rs 0 0 0 Zn 0 0 0 opc           |

|   size | Instruction Details                          | Feature   |
|--------|----------------------------------------------|-----------|
|     00 | MOVA (vector to tile, two registers) -8- bit | FEAT_SME2 |
|     01 | MOVA(vector to tile, two registers)-16- bit  | FEAT_SME2 |
|     10 | MOVA(vector to tile, two registers)-32- bit  | FEAT_SME2 |
|     11 | MOVA(vector to tile, two registers)-64- bit  | FEAT_SME2 |

## SME2 move vector to tile, four registers

The encodings in this section are decoded from SME Move into Array.

<!-- image -->

## SME Move from Array

SMEMove from Array

The encodings in this section are decoded from SME encodings.

<!-- image -->

| 31          | 24 23 22 21 19 18 17 16 15 14 13 12 10 9 8 7 2 1   |
|-------------|----------------------------------------------------|
| 1 1 0 0 0 0 | 0 op0 0 0 0 op1 1 op2 op3 op4 op5                  |

| op0   |   op1 | op2   | op3    | op4   | op5   | Instruction details                              | Feature     |
|-------|-------|-------|--------|-------|-------|--------------------------------------------------|-------------|
| 00    |     1 | 00    | 010    | 00    | x0    | MOVA(array to vector, two registers)             | FEAT_SME2   |
| 00    |     1 | 00    | 010    | 10    | x0    | MOVAZ(array to vector, two registers)            | FEAT_SME2p1 |
| 00    |     1 | 00    | 011    | 00    | 00    | MOVA(array to vector, four registers)            | FEAT_SME2   |
| 00    |     1 | 00    | 011    | 10    | 00    | MOVAZ(array to vector, four registers)           | FEAT_SME2p1 |
| 00    |     1 | 00    | 011    | x0    | 10    | UNALLOCATED                                      | -           |
| 00    |     1 | 01    | 01x    | x0    | x0    | UNALLOCATED                                      | -           |
| xx    |     0 | xx    | 000    | 1x    | xx    | SMEzeroing move array to vector                  | -           |
| xx    |     0 | xx    | xxx    | 0x    | xx    | SMEmove array to vector                          | -           |
| xx    |     0 | xx    | != 000 | 1x    | xx    | UNALLOCATED                                      | -           |
| xx    |     1 | 0x    | 000    | 00    | x0    | SME2 move tile to vector, two registers          | -           |
| xx    |     1 | 0x    | 000    | 10    | x0    | SME2 zeroing move tile to vector, two registers  | -           |
| xx    |     1 | 0x    | 001    | 00    | 00    | SME2 move tile to vector, four registers         | -           |
| xx    |     1 | 0x    | 001    | 10    | 00    | SME2 zeroing move tile to vector, four registers | -           |
| xx    |     1 | 0x    | 001    | x0    | 10    | UNALLOCATED                                      | -           |
| xx    |     1 | 0x    | 0xx    | x0    | x1    | UNALLOCATED                                      | -           |
| xx    |     1 | 0x    | 0xx    | x1    | xx    | UNALLOCATED                                      | -           |
| xx    |     1 | 0x    | 1xx    | xx    | xx    | UNALLOCATED                                      | -           |
| xx    |     1 | 1x    | xxx    | xx    | xx    | UNALLOCATED                                      | -           |

| size   | opc   | Instruction Details                           | Feature   |
|--------|-------|-----------------------------------------------|-----------|
| 00     | 0xx   | MOVA (vector to tile, four registers) -8- bit | FEAT_SME2 |
| 01     | 0xx   | MOVA(vector to tile, four registers)-16- bit  | FEAT_SME2 |
| 10     | 0xx   | MOVA(vector to tile, four registers)-32- bit  | FEAT_SME2 |
| 11     | xxx   | MOVA(vector to tile, four registers)-64- bit  | FEAT_SME2 |
| != 11  | 1xx   | UNALLOCATED                                   | -         |

| op0   |   op1 | op2   | op3   | op4   | op5   | Instruction details   | Feature   |
|-------|-------|-------|-------|-------|-------|-----------------------|-----------|
| != 00 |     1 | 0x    | 01x   | x0    | x0    | UNALLOCATED           | -         |

## SME zeroing move array to vector

The encodings in this section are decoded from SME Move from Array.

<!-- image -->

| 31   | 24 23 22 21    | 19 18 17 13 12     | 16 15 14 10 9 8 5 4   |
|------|----------------|--------------------|-----------------------|
| 1 1  | 0 size 0 0 0 0 | 1 Q V Rs 0 0 1 opc | 0 Zd                  |

| size   |   Q | Instruction Details                    | Feature     |
|--------|-----|----------------------------------------|-------------|
| 00     |   0 | MOVAZ(tile to vector, single) -8-bit   | FEAT_SME2p1 |
| 01     |   0 | MOVAZ(tile to vector, single) -16-bit  | FEAT_SME2p1 |
| 10     |   0 | MOVAZ(tile to vector, single) -32-bit  | FEAT_SME2p1 |
| 11     |   0 | MOVAZ(tile to vector, single) -64-bit  | FEAT_SME2p1 |
| 11     |   1 | MOVAZ(tile to vector, single) -128-bit | FEAT_SME2p1 |
| != 11  |   1 | UNALLOCATED                            | -           |

## SME move array to vector

The encodings in this section are decoded from SME Move from Array.

<!-- image -->

| 31   | 24 23 22 21 19 18 17 16 15 14 13 12 10 9 8 5 4   |
|------|--------------------------------------------------|
| 1 1  | 0 size 0 0 0 0 1 Q V Rs Pg 0 opc Zd              |

| size   |   Q | Instruction Details                   | Feature   |
|--------|-----|---------------------------------------|-----------|
| 00     |   0 | MOVA(tile to vector, single) -8-bit   | FEAT_SME  |
| 01     |   0 | MOVA(tile to vector, single) -16-bit  | FEAT_SME  |
| 10     |   0 | MOVA(tile to vector, single) -32-bit  | FEAT_SME  |
| 11     |   0 | MOVA(tile to vector, single) -64-bit  | FEAT_SME  |
| 11     |   1 | MOVA(tile to vector, single) -128-bit | FEAT_SME  |
| != 11  |   1 | UNALLOCATED                           | -         |

## SME2 move tile to vector, two registers

The encodings in this section are decoded from SME Move from Array.

<!-- image -->

| 31   | 24 23 22 21        | 19 18 15 14 13 12 10   | 17 16 9 8 7 5 4 1 0   |
|------|--------------------|------------------------|-----------------------|
| 1 1  | 0 size 0 0 0 1 1 0 | V Rs 0 0 0 Zd          | 0 0 opc 0             |

|   size | Instruction Details                          | Feature   |
|--------|----------------------------------------------|-----------|
|     00 | MOVA (tile to vector, two registers) -8- bit | FEAT_SME2 |
|     01 | MOVA(tile to vector, two registers)-16- bit  | FEAT_SME2 |
|     10 | MOVA(tile to vector, two registers)-32- bit  | FEAT_SME2 |
|     11 | MOVA(tile to vector, two registers)-64- bit  | FEAT_SME2 |

## SME2 zeroing move tile to vector, two registers

The encodings in this section are decoded from SME Move from Array.

<!-- image -->

| 31    | 24 23 22 21 19 18 17 16 15 14 13 12 10 9 8 7 5 4 1 0   |
|-------|--------------------------------------------------------|
| 1 1 0 | 0 size 0 0 0 1 1 0 V Rs 0 0 0 1 0 opc Zd 0             |

|   size | Instruction Details                            | Feature     |
|--------|------------------------------------------------|-------------|
|     00 | MOVAZ (tile to vector, two registers) - 8-bit  | FEAT_SME2p1 |
|     01 | MOVAZ (tile to vector, two registers) - 16-bit | FEAT_SME2p1 |
|     10 | MOVAZ (tile to vector, two registers) - 32-bit | FEAT_SME2p1 |
|     11 | MOVAZ (tile to vector, two registers) - 64-bit | FEAT_SME2p1 |

## SME2 move tile to vector, four registers

The encodings in this section are decoded from SME Move from Array.

<!-- image -->

## SME Add Vector to Array

SMEAddVector to Array

The encodings in this section are decoded from SME encodings.

<!-- image -->

| 31 24 23 22 21 19 18 17       | 5 4 3 2   |
|-------------------------------|-----------|
| 1 1 0 0 0 0 0 0 op0 0 1 0 op1 | op2 0     |

| size   | opc   | Instruction Details                           | Feature   |
|--------|-------|-----------------------------------------------|-----------|
| 00     | 0xx   | MOVA (tile to vector, four registers) -8- bit | FEAT_SME2 |
| 01     | 0xx   | MOVA(tile to vector, four registers)-16- bit  | FEAT_SME2 |
| 10     | 0xx   | MOVA(tile to vector, four registers)-32- bit  | FEAT_SME2 |
| 11     | xxx   | MOVA(tile to vector, four registers)-64- bit  | FEAT_SME2 |
| != 11  | 1xx   | UNALLOCATED                                   | -         |

## SME2 zeroing move tile to vector, four registers

The encodings in this section are decoded from SME Move from Array.

<!-- image -->

| 31    | 24 23 22 21        | 19 18 17 14 13 12 10   | 16 15 9 8 7 5 4 2 1 0   |
|-------|--------------------|------------------------|-------------------------|
| 1 1 0 | 0 size 0 0 0 1 1 0 | V Rs 0 0 1 Zd          | 1 0 opc 0 0             |

| size   | opc   | Instruction Details                            | Feature     |
|--------|-------|------------------------------------------------|-------------|
| 00     | 0xx   | MOVAZ (tile to vector, four registers)- 8-bit  | FEAT_SME2p1 |
| 01     | 0xx   | MOVAZ (tile to vector, four registers)- 16-bit | FEAT_SME2p1 |
| 10     | 0xx   | MOVAZ (tile to vector, four registers)- 32-bit | FEAT_SME2p1 |
| 11     | xxx   | MOVAZ (tile to vector, four registers)- 64-bit | FEAT_SME2p1 |
| != 11  | 1xx   | UNALLOCATED                                    | -           |

## SME add vector to array

The encodings in this section are decoded from SME Add Vector to Array.

<!-- image -->

|   31 | 24 23 22 21 19     | 18 17 16 15 13 12   | 10 9   | 5 4   |   3 | 2    |
|------|--------------------|---------------------|--------|-------|-----|------|
|    1 | 1 0 0 0 0 0 0 1 op | 0 1 0 0 0 V Pm      | Pn     | Zn 0  |   0 | opc2 |

|   op | V   | opc2   | Instruction Details   | Feature         |
|------|-----|--------|-----------------------|-----------------|
|    0 | x   | 1xx    | UNALLOCATED           | -               |
|    0 | 0   | 0xx    | ADDHA-32-bit          | FEAT_SME        |
|    0 | 1   | 0xx    | ADDVA-32-bit          | FEAT_SME        |
|    1 | 0   | xxx    | ADDHA-64-bit          | FEAT_SME_I16I64 |
|    1 | 1   | xxx    | ADDVA-64-bit          | FEAT_SME_I16I64 |

## SME2 Multi-vector - Multiple and Single Array Vectors (Two registers)

SME2 Multi-vector - Multiple and Single Array Vectors (Two registers)

The encodings in this section are decoded from SME encodings.

<!-- image -->

|   op0 |   op1 | op2    | op3   | Instruction details                                      | Feature        |
|-------|-------|--------|-------|----------------------------------------------------------|----------------|
|     0 |   000 | 000    | 1     | FMLALL (multiple and single vector) - Two ZAquad-vectors | FEAT_SME_F8F32 |
|     0 |   000 | != 000 | 1     | UNALLOCATED                                              | -              |
|     0 |   010 | xxx    | x     | SME2 single-multi long FMA two sources                   | -              |
|     0 |   011 | xxx    | x     | SME2 multiple and single vector long FMAone source       | -              |
|     0 |   100 | xxx    | x     | SME2 single-multi FP dot product two registers           | -              |

|   op0 | op1   | op2   | Instruction details    |
|-------|-------|-------|------------------------|
|     0 | xx    | x     | UNALLOCATED            |
|     1 | 00    | 0     | SMEadd vector to array |
|     1 | 00    | 1     | UNALLOCATED            |
|     1 | != 00 | x     | UNALLOCATED            |

| op0   |   op1 | op2   | op3   | Instruction details                                     | Feature   |
|-------|-------|-------|-------|---------------------------------------------------------|-----------|
| 0     |   101 | x1x   | x     | SME2 single-multi mixed dot product two registers       | -         |
| 1     |   000 | xxx   | 1     | UNALLOCATED                                             | -         |
| 1     |   010 | xxx   | x     | SME2 single-multi long MLAtwo sources                   | -         |
| 1     |   011 | xxx   | x     | SME2 multiple and single vector long MLAone source      | -         |
| 1     |   100 | xxx   | x     | UNALLOCATED                                             | -         |
| 1     |   101 | x1x   | x     | SME2 single-multi two-way dot product two registers     | -         |
| x     |   000 | xxx   | 0     | SME2 single-multi long long MLA two sources             | -         |
| x     |   001 | xxx   | x     | SME2 multiple and single vector long long FMAone source | -         |
| x     |   101 | x0x   | x     | SME2 single-multi four-way dot product two registers    | -         |
| x     |   110 | 0xx   | x     | SME2single-multi ternary FPtworegisters                 | -         |
| x     |   110 | 1xx   | x     | SME2single-multi ternary int two registers              | -         |
| x     |   111 | 0xx   | x     | SME2 single-multi ternary FP16 two registers            | -         |
| x     |   111 | 1xx   | x     | UNALLOCATED                                             | -         |

## SME2 single-multi long FMA two sources

The encodings in this section are decoded from SME2 Multi-vector - Multiple and Single Array Vectors (Two registers).

<!-- image -->

| 31      | 23 22 21 20 19 16 15 14 13 12 10 9 5 4 3 2 1 0   |
|---------|--------------------------------------------------|
| 1 1 0 0 | 0 0 1 0 Zm 0 Rv 0 1 0 Zn op S o2 off2            |

|   op | S   |   o2 | Instruction Details                              | Feature        |
|------|-----|------|--------------------------------------------------|----------------|
|    0 | 0   |    0 | FMLAL (multiple and single vector, FP16 to FP32) | FEAT_SME2      |
|    0 | 0   |    1 | FMLAL(multiple and single vector, FP8to FP16)    | FEAT_SME_F8F16 |
|    0 | 1   |    0 | FMLSL (multiple and single vector)               | FEAT_SME2      |
|    0 | 1   |    1 | UNALLOCATED                                      | -              |
|    1 | x   |    1 | UNALLOCATED                                      | -              |
|    1 | 0   |    0 | BFMLAL(multiple and single vector)               | FEAT_SME2      |
|    1 | 1   |    0 | BFMLSL (multiple and single vector)              | FEAT_SME2      |

## SME2 multiple and single vector long FMA one source

The encodings in this section are decoded from SME2 Multi-vector - Multiple and Single Array Vectors (Two registers).

<!-- image -->

| 31   | 23 22 21 20 19    | 16 15 14 13 12 10 9 5 4 3 2   |
|------|-------------------|-------------------------------|
| 1 1  | 0 0 1 0 Zm 0 Rv 0 | 1 1 Zn op S off3              |

|   op | S Instruction Details                              | Feature   |
|------|----------------------------------------------------|-----------|
|    0 | 0 FMLAL (multiple and single vector, FP16 to FP32) | FEAT_SME2 |
|    0 | 1 FMLSL (multiple and single vector)               | FEAT_SME2 |
|    1 | 0 BFMLAL(multiple and single vector)               | FEAT_SME2 |
|    1 | 1 BFMLSL (multiple and single vector)              | FEAT_SME2 |

## SME2 single-multi FP dot product two registers

The encodings in this section are decoded from SME2 Multi-vector - Multiple and Single Array Vectors (Two registers).

<!-- image -->

|   opc | Instruction Details                                    | Feature        |
|-------|--------------------------------------------------------|----------------|
|    00 | FDOT (2-way, multiple and single vector, FP16 to FP32) | FEAT_SME2      |
|    01 | FDOT (2-way, multiple and single vector, FP8 to FP16)  | FEAT_SME_F8F16 |
|    10 | BFDOT (multiple and single vector)                     | FEAT_SME2      |
|    11 | FDOT (4-way, multiple and single vector)               | FEAT_SME_F8F32 |

## SME2 single-multi mixed dot product two registers

The encodings in this section are decoded from SME2 Multi-vector - Multiple and Single Array Vectors (Two registers).

<!-- image -->

## SME2 single-multi long MLA two sources

The encodings in this section are decoded from SME2 Multi-vector - Multiple and Single Array Vectors (Two registers).

<!-- image -->

| 31    | 23 22 21 20 19   | 16 15 14 13 12 10 9 5 4 3 2   |
|-------|------------------|-------------------------------|
| 1 1 0 | 0 1 1 0 Zm 0 Rv  | 0 1 0 Zn U S op               |

| U   | S op   | Instruction Details                | Feature   |
|-----|--------|------------------------------------|-----------|
| x   | x 1    | UNALLOCATED                        | -         |
| 0   | 0 0    | SMLAL(multiple and single vector)  | FEAT_SME2 |
| 0   | 1 0    | SMLSL (multiple and single vector) | FEAT_SME2 |
| 1   | 0 0    | UMLAL(multiple and single vector)  | FEAT_SME2 |
| 1   | 1 0    | UMLSL(multiple and single vector)  | FEAT_SME2 |

## SME2 multiple and single vector long MLA one source

The encodings in this section are decoded from SME2 Multi-vector - Multiple and Single Array Vectors (Two registers).

<!-- image -->

| 31    | 23 22 21 20 19   | 16 15 14 13 12 10 9 5 4 3 2   |
|-------|------------------|-------------------------------|
| 1 1 0 | 0 1 1 0 Zm 0 Rv  | 0 1 1 Zn U S off3             |

|   U |   S | Instruction Details                | Feature   |
|-----|-----|------------------------------------|-----------|
|   0 |   0 | SMLAL(multiple and single vector)  | FEAT_SME2 |
|   0 |   1 | SMLSL (multiple and single vector) | FEAT_SME2 |
|   1 |   0 | UMLAL(multiple and single vector)  | FEAT_SME2 |
|   1 |   1 | UMLSL(multiple and single vector)  | FEAT_SME2 |

|   U | Instruction Details                       | Feature   |
|-----|-------------------------------------------|-----------|
|   0 | USDOT (4-way, multiple and single vector) | FEAT_SME2 |
|   1 | SUDOT (4-way, multiple and single vector) | FEAT_SME2 |

## SME2 single-multi two-way dot product two registers

The encodings in this section are decoded from SME2 Multi-vector - Multiple and Single Array Vectors (Two registers).

<!-- image -->

| 31   | 23 22 21 20 19   | 16 15 14 13 12 10 9 5 4 3 2   |
|------|------------------|-------------------------------|
| 1 1  | 0 1 1 0 Zm 0 Rv  | 1 0 1 Zn U 1 off3             |

|   U | Instruction Details                      | Feature   |
|-----|------------------------------------------|-----------|
|   0 | SDOT (2-way, multiple and single vector) | FEAT_SME2 |
|   1 | UDOT(2-way, multiple and single vector)  | FEAT_SME2 |

## SME2 single-multi long long MLA two sources

The encodings in this section are decoded from SME2 Multi-vector - Multiple and Single Array Vectors (Two registers).

<!-- image -->

| sz   | U   | S   |   op | Instruction Details                 | Feature   |
|------|-----|-----|------|-------------------------------------|-----------|
| x    | 0   | 0   |    0 | SMLALL(multiple and single vector)  | FEAT_SME2 |
| x    | 0   | 1   |    0 | SMLSLL (multiple and single vector) | FEAT_SME2 |
| x    | 1   | 0   |    0 | UMLALL(multiple and single vector)  | FEAT_SME2 |
| x    | 1   | 1   |    0 | UMLSLL(multiple and single vector)  | FEAT_SME2 |
| 0    | x   | 1   |    1 | UNALLOCATED                         | -         |
| 0    | 0   | 0   |    1 | USMLALL(multiple and single vector) | FEAT_SME2 |
| 0    | 1   | 0   |    1 | SUMLALL(multiple and single vector) | FEAT_SME2 |
| 1    | x   | x   |    1 | UNALLOCATED                         | -         |

## SME2 multiple and single vector long long FMA one source

The encodings in this section are decoded from SME2 Multi-vector - Multiple and Single Array Vectors (Two registers).

<!-- image -->

| 31   | 23 22 21 20 19   | 16 15 14 13 12 10 9 5 4   |
|------|------------------|---------------------------|
| 1 1  | 0 sz 1 0 Zm 0    | Rv 0 0 1 Zn U             |

| sz   | U   | S   |   op | Instruction Details                 | Feature   |
|------|-----|-----|------|-------------------------------------|-----------|
| x    | 0   | 0   |    0 | SMLALL(multiple and single vector)  | FEAT_SME2 |
| x    | 0   | 1   |    0 | SMLSLL (multiple and single vector) | FEAT_SME2 |
| x    | 1   | 0   |    0 | UMLALL(multiple and single vector)  | FEAT_SME2 |
| x    | 1   | 1   |    0 | UMLSLL(multiple and single vector)  | FEAT_SME2 |
| 0    | 0   | 0   |    1 | USMLALL(multiple and single vector) | FEAT_SME2 |
| 0    | 0   | 1   |    1 | UNALLOCATED                         | -         |
| 0    | 1   | x   |    1 | UNALLOCATED                         | -         |
| 1    | x   | x   |    1 | UNALLOCATED                         | -         |

## SME2 single-multi four-way dot product two registers

The encodings in this section are decoded from SME2 Multi-vector - Multiple and Single Array Vectors (Two registers).

<!-- image -->

| 31   | 23 22 21 20 19 16    | 15 14 13 12 10 9 5 4 3 2   |
|------|----------------------|----------------------------|
| 1 1  | 0 sz 1 0 Zm 0 Rv 1 0 | 1 Zn U 0 off3              |

|   U | Instruction Details                      | Feature   |
|-----|------------------------------------------|-----------|
|   0 | SDOT (4-way, multiple and single vector) | FEAT_SME2 |
|   1 | UDOT(4-way, multiple and single vector)  | FEAT_SME2 |

## SME2 single-multi ternary FP two registers

The encodings in this section are decoded from SME2 Multi-vector - Multiple and Single Array Vectors (Two registers).

<!-- image -->

| 31    | 23 22 21 20 19     | 16 15 14 13 12 10 9 5 4 3 2   |
|-------|--------------------|-------------------------------|
| 1 1 0 | 0 sz 1 0 Zm 0 Rv 1 | 1 0 Zn 0 S off3               |

|   S | Instruction Details               | Feature   |
|-----|-----------------------------------|-----------|
|   0 | FMLA(multiple and single vector)  | FEAT_SME2 |
|   1 | FMLS (multiple and single vector) | FEAT_SME2 |

## SME2 single-multi ternary int two registers

The encodings in this section are decoded from SME2 Multi-vector - Multiple and Single Array Vectors (Two registers).

<!-- image -->

| 31   | 23 22 21 20 19     | 16 15 14 13 12 10 9 5 4 3 2   |
|------|--------------------|-------------------------------|
| 1 1  | 0 sz 1 0 Zm 0 Rv 1 | 1 0 Zn 1 S off3               |

|   S | Instruction Details                        | Feature   |
|-----|--------------------------------------------|-----------|
|   0 | ADD(to array, multiple and single vector)  | FEAT_SME2 |
|   1 | SUB (to array, multiple and single vector) | FEAT_SME2 |

## SME2 single-multi ternary FP16 two registers

The encodings in this section are decoded from SME2 Multi-vector - Multiple and Single Array Vectors (Two registers).

<!-- image -->

| 31    | 23 22 21 20 19   | 16 15 14 13 12 10 9 5 4 3 2   |
|-------|------------------|-------------------------------|
| 1 1 0 | 0 sz 1 0 Zm 0 Rv | 1 1 1 Zn 0 S off3             |

|   sz |   S | Instruction Details                | Feature         |
|------|-----|------------------------------------|-----------------|
|    0 |   0 | FMLA(multiple and single vector)   | FEAT_SME_F16F16 |
|    0 |   1 | FMLS (multiple and single vector)  | FEAT_SME_F16F16 |
|    1 |   0 | BFMLA(multiple and single vector)  | FEAT_SME_B16B16 |
|    1 |   1 | BFMLS (multiple and single vector) | FEAT_SME_B16B16 |

## SME2 Multi-vector - Multiple and Single Array Vectors (Four registers)

SME2 Multi-vector - Multiple and Single Array Vectors (Four registers)

The encodings in this section are decoded from SME encodings.

<!-- image -->

| 31 23 22 21 20            |   16 15 14 13 | 12 10 9 5 4 2 1   |
|---------------------------|---------------|-------------------|
| 1 1 0 0 0 0 0 1 0 op0 1 1 |             0 | op1 op2 op3       |

|   op0 |   op1 |   op2 |   op3 | Instruction details                                       | Feature        |
|-------|-------|-------|-------|-----------------------------------------------------------|----------------|
|     0 |   000 |   000 |     1 | FMLALL (multiple and single vector) - Four ZAquad-vectors | FEAT_SME_F8F32 |

| op0   | op1   | op2    | op3   | Instruction details                                               | Feature        |
|-------|-------|--------|-------|-------------------------------------------------------------------|----------------|
| 0     | 000   | != 000 | 1     | UNALLOCATED                                                       | -              |
| 0     | 001   | 000    | x     | FMLALL (multiple and single vector) - One ZAquad-vector           | FEAT_SME_F8F32 |
| 0     | 001   | 001    | x     | UNALLOCATED                                                       | -              |
| 0     | 010   | xxx    | x     | SME2single-multi long FMAfour sources                             | -              |
| 0     | 011   | 00x    | x     | FMLAL(multiple and single vector, FP8to FP16) -OneZAdouble-vector | FEAT_SME_F8F16 |
| 0     | 0x1   | 01x    | x     | UNALLOCATED                                                       | -              |
| 0     | 0x1   | 1xx    | x     | UNALLOCATED                                                       | -              |
| 0     | 100   | xxx    | x     | SME2 single-multi FP dot product four registers                   | -              |
| 0     | 101   | x1x    | x     | SME2 single-multi mixed dot product four registers                | -              |
| 1     | 000   | xxx    | 1     | UNALLOCATED                                                       | -              |
| 1     | 010   | xxx    | x     | SME2single-multi long MLAfour sources                             | -              |
| 1     | 0x1   | xxx    | x     | UNALLOCATED                                                       | -              |
| 1     | 100   | xxx    | x     | UNALLOCATED                                                       | -              |
| 1     | 101   | x1x    | x     | SME2 single-multi two-way dot product four registers              | -              |
| x     | 000   | xxx    | 0     | SME2 single-multi long long MLA four sources                      | -              |
| x     | 101   | x0x    | x     | SME2 single-multi four-way dot product four registers             | -              |
| x     | 110   | 0xx    | x     | SME2 single-multi ternary FP four registers                       | -              |
| x     | 110   | 1xx    | x     | SME2 single-multi ternary int four registers                      | -              |
| x     | 111   | 0xx    | x     | SME2 single-multi ternary FP16 four registers                     | -              |
| x     | 111   | 1xx    | x     | UNALLOCATED                                                       | -              |

## SME2 single-multi long FMA four sources

The encodings in this section are decoded from SME2 Multi-vector - Multiple and Single Array Vectors (Four registers).

<!-- image -->

| 31    | 23 22 21 20 19 16 15 14 13 12 10 9 5 4 3 2 1 0   |
|-------|--------------------------------------------------|
| 1 1 0 | 0 0 1 1 Zm 0 Rv 0 1 0 Zn op S o2 off2            |

|   op | S   |   o2 | Instruction Details                              | Feature        |
|------|-----|------|--------------------------------------------------|----------------|
|    0 | 0   |    0 | FMLAL (multiple and single vector, FP16 to FP32) | FEAT_SME2      |
|    0 | 0   |    1 | FMLAL(multiple and single vector, FP8to FP16)    | FEAT_SME_F8F16 |
|    0 | 1   |    0 | FMLSL (multiple and single vector)               | FEAT_SME2      |
|    0 | 1   |    1 | UNALLOCATED                                      | -              |
|    1 | x   |    1 | UNALLOCATED                                      | -              |
|    1 | 0   |    0 | BFMLAL(multiple and single vector)               | FEAT_SME2      |
|    1 | 1   |    0 | BFMLSL (multiple and single vector)              | FEAT_SME2      |

## SME2 single-multi FP dot product four registers

The encodings in this section are decoded from SME2 Multi-vector - Multiple and Single Array Vectors (Four registers).

<!-- image -->

| 31    | 23 22 21 20 19        | 16 15 14 13 12 10 9 5 4 3 2   |
|-------|-----------------------|-------------------------------|
| 1 1 0 | 0 0 1 1 Zm 0 Rv 1 0 0 | Zn opc off3                   |

|   opc | Instruction Details                                    | Feature        |
|-------|--------------------------------------------------------|----------------|
|    00 | FDOT (2-way, multiple and single vector, FP16 to FP32) | FEAT_SME2      |
|    01 | FDOT (2-way, multiple and single vector, FP8 to FP16)  | FEAT_SME_F8F16 |
|    10 | BFDOT (multiple and single vector)                     | FEAT_SME2      |
|    11 | FDOT (4-way, multiple and single vector)               | FEAT_SME_F8F32 |

## SME2 single-multi mixed dot product four registers

The encodings in this section are decoded from SME2 Multi-vector - Multiple and Single Array Vectors (Four registers).

<!-- image -->

<!-- image -->

|   U | Instruction Details Feature                 |
|-----|---------------------------------------------|
|   0 | USDOT (4-way, multiple and single FEAT_SME2 |

## SME2 single-multi long MLA four sources

The encodings in this section are decoded from SME2 Multi-vector - Multiple and Single Array Vectors (Four registers).

<!-- image -->

| 31    | 23 22 21 20 19   | 16 15 14 13 12 10 9 5 4 3 2 1 0   |
|-------|------------------|-----------------------------------|
| 1 1 0 | 0 1 1 1 Zm 0 Rv  | 0 1 0 Zn U S op off2              |

| U   | S op   | Instruction Details                | Feature   |
|-----|--------|------------------------------------|-----------|
| x   | x 1    | UNALLOCATED                        | -         |
| 0   | 0 0    | SMLAL(multiple and single vector)  | FEAT_SME2 |
| 0   | 1 0    | SMLSL (multiple and single vector) | FEAT_SME2 |
| 1   | 0 0    | UMLAL(multiple and single vector)  | FEAT_SME2 |
| 1   | 1 0    | UMLSL(multiple and single vector)  | FEAT_SME2 |

## SME2 single-multi two-way dot product four registers

The encodings in this section are decoded from SME2 Multi-vector - Multiple and Single Array Vectors (Four registers).

<!-- image -->

|   U | Instruction Details                      | Feature   |
|-----|------------------------------------------|-----------|
|   0 | SDOT (2-way, multiple and single vector) | FEAT_SME2 |
|   1 | UDOT(2-way, multiple and single vector)  | FEAT_SME2 |

## SME2 single-multi long long MLA four sources

The encodings in this section are decoded from SME2 Multi-vector - Multiple and Single Array Vectors (Four registers).

<!-- image -->

| U               | Instruction Details Feature           |
|-----------------|---------------------------------------|
| 1 SUDOT vector) | (4-way, multiple and single FEAT_SME2 |

| sz   | U   | S   |   op | Instruction Details                 | Feature   |
|------|-----|-----|------|-------------------------------------|-----------|
| x    | 0   | 0   |    0 | SMLALL(multiple and single vector)  | FEAT_SME2 |
| x    | 0   | 1   |    0 | SMLSLL (multiple and single vector) | FEAT_SME2 |
| x    | 1   | 0   |    0 | UMLALL(multiple and single vector)  | FEAT_SME2 |
| x    | 1   | 1   |    0 | UMLSLL(multiple and single vector)  | FEAT_SME2 |
| 0    | x   | 1   |    1 | UNALLOCATED                         | -         |
| 0    | 0   | 0   |    1 | USMLALL(multiple and single vector) | FEAT_SME2 |
| 0    | 1   | 0   |    1 | SUMLALL(multiple and single vector) | FEAT_SME2 |
| 1    | x   | x   |    1 | UNALLOCATED                         | -         |

## SME2 single-multi four-way dot product four registers

The encodings in this section are decoded from SME2 Multi-vector - Multiple and Single Array Vectors (Four registers).

<!-- image -->

| 31      | 23 22 21 20 19 16 15 14 13 12 10 9 5 4 3 2   |
|---------|----------------------------------------------|
| 1 1 0 0 | 0 sz 1 1 Zm 0 Rv 1 0 1 Zn U 0 off3           |

|   U | Instruction Details                      | Feature   |
|-----|------------------------------------------|-----------|
|   0 | SDOT (4-way, multiple and single vector) | FEAT_SME2 |
|   1 | UDOT(4-way, multiple and single vector)  | FEAT_SME2 |

## SME2 single-multi ternary FP four registers

The encodings in this section are decoded from SME2 Multi-vector - Multiple and Single Array Vectors (Four registers).

<!-- image -->

| 31    | 23 22 21 20 19   | 16 15 14 13 12 10 9 5 4 3   |
|-------|------------------|-----------------------------|
| 1 1 0 | 0 sz 1 1 Zm 0 Rv | 1 1 0 Zn 0 S                |

|   S | Instruction Details               | Feature   |
|-----|-----------------------------------|-----------|
|   0 | FMLA(multiple and single vector)  | FEAT_SME2 |
|   1 | FMLS (multiple and single vector) | FEAT_SME2 |

## SME2 single-multi ternary int four registers

The encodings in this section are decoded from SME2 Multi-vector - Multiple and Single Array Vectors (Four registers).

<!-- image -->

| 31   | 23 22 21 20 19       | 16 15 14 13 12 10 9 5 4 3 2   |
|------|----------------------|-------------------------------|
| 1 1  | 0 sz 1 1 Zm 0 Rv 1 1 | 0 Zn 1 S off3                 |

|   S | Instruction Details                        | Feature   |
|-----|--------------------------------------------|-----------|
|   0 | ADD(to array, multiple and single vector)  | FEAT_SME2 |
|   1 | SUB (to array, multiple and single vector) | FEAT_SME2 |

## SME2 single-multi ternary FP16 four registers

The encodings in this section are decoded from SME2 Multi-vector - Multiple and Single Array Vectors (Four registers).

<!-- image -->

| 31   | 23 22 21 20 19   | 16 15 14 13 12 10 9 5 4 3 2   |
|------|------------------|-------------------------------|
| 1 1  | 0 sz 1 1 Zm 0 Rv | 1 1 1 Zn 0 S off3             |

|   sz |   S | Instruction Details                | Feature         |
|------|-----|------------------------------------|-----------------|
|    0 |   0 | FMLA(multiple and single vector)   | FEAT_SME_F16F16 |
|    0 |   1 | FMLS (multiple and single vector)  | FEAT_SME_F16F16 |
|    1 |   0 | BFMLA(multiple and single vector)  | FEAT_SME_B16B16 |
|    1 |   1 | BFMLS (multiple and single vector) | FEAT_SME_B16B16 |

## SME2 Multi-vector - Multiple Array Vectors (Two registers)

SME2 Multi-vector - Multiple Array Vectors (Two registers)

The encodings in this section are decoded from SME encodings.

<!-- image -->

<!-- image -->

|   op0 | op1   | op2   |   op3 |   op4 |   op5 |   op6 | Instruction details                             | Feature        |
|-------|-------|-------|-------|-------|-------|-------|-------------------------------------------------|----------------|
|     0 | xx    | xx    |   000 |     1 |   000 |     0 | FMLALL (multiple vectors) - Two ZA quad-vectors | FEAT_SME_F8F32 |

| op0   | op1   | op2   | op3   | op4   | op5   | op6   | Instruction details                                        | Feature        |
|-------|-------|-------|-------|-------|-------|-------|------------------------------------------------------------|----------------|
| 0     | xx    | xx    | 000   | 1     | 001   | 0     | UNALLOCATED                                                | -              |
| 0     | xx    | xx    | 000   | 1     | 10x   | 0     | UNALLOCATED                                                | -              |
| 0     | xx    | xx    | 000   | 1     | x0x   | 1     | UNALLOCATED                                                | -              |
| 0     | xx    | xx    | 010   | 0     | xx0   | x     | SME2 multiple vectors long FMA two sources                 | -              |
| 0     | xx    | xx    | 010   | 1     | 000   | x     | FMLAL (multiple vectors, FP8 to FP16) -TwoZAdouble-vectors | FEAT_SME_F8F16 |
| 0     | xx    | xx    | 010   | 1     | 100   | x     | UNALLOCATED                                                | -              |
| 0     | xx    | xx    | 010   | 1     | x01   | x     | UNALLOCATED                                                | -              |
| 0     | xx    | xx    | 0x1   | 1     | xxx   | x     | UNALLOCATED                                                | -              |
| 0     | xx    | xx    | 100   | x     | x0x   | x     | SME2 multiple vectors FP dot product two registers         | -              |
| 0     | xx    | xx    | 101   | 0     | 01x   | x     | USDOT (4-way, multiple vectors) -Two ZAsingle-vectors      | FEAT_SME2      |
| 0     | xx    | xx    | 101   | 0     | 11x   | x     | UNALLOCATED                                                | -              |
| 0     | xx    | xx    | 110   | 1     | x0x   | x     | UNALLOCATED                                                | -              |
| 0     | xx    | xx    | 1x1   | 1     | xxx   | x     | UNALLOCATED                                                | -              |
| 0     | xx    | xx    | xx0   | 1     | x1x   | x     | UNALLOCATED                                                | -              |
| 1     | xx    | xx    | 010   | 0     | xx0   | x     | SME2 multiple vectors long MLA two sources                 | -              |
| 1     | xx    | xx    | 100   | 0     | x0x   | x     | UNALLOCATED                                                | -              |
| 1     | xx    | xx    | 101   | 0     | x1x   | x     | SME2 multiple vectors two-way dot product two registers    | -              |
| 1     | xx    | xx    | xxx   | 1     | xxx   | x     | UNALLOCATED                                                | -              |
| x     | 00    | 00    | 111   | 0     | 0xx   | x     | SME2 multiple vectors binary FP two registers              | -              |
| x     | 00    | 00    | 111   | 0     | 1xx   | x     | SME2 multiple vectors binary int two registers             | -              |
| x     | 00    | 10    | 111   | 0     | 0xx   | x     | SME2 multiple vectors binary FP16 two registers            | -              |
| x     | 00    | 10    | 111   | 0     | 1xx   | x     | UNALLOCATED                                                | -              |
| x     | 00    | x1    | 111   | 0     | xxx   | x     | UNALLOCATED                                                | -              |
| x     | xx    | xx    | 000   | 0     | xxx   | 0     | SME2 multiple vectors long long MLA two sources            | -              |
| x     | xx    | xx    | 000   | 0     | xxx   | 1     | UNALLOCATED                                                | -              |
| x     | xx    | xx    | 010   | 0     | xx1   | x     | UNALLOCATED                                                | -              |
| x     | xx    | xx    | 0x1   | 0     | xxx   | x     | UNALLOCATED                                                | -              |
| x     | xx    | xx    | 100   | 0     | x1x   | x     | SME2 multiple vectors ternary FP16 two registers           | -              |
| x     | xx    | xx    | 101   | 0     | x0x   | x     | SME2 multiple vectors four-way dot product two registers   | -              |
| x     | xx    | xx    | 110   | 0     | 0xx   | x     | SME2 multiple vectors ternary FP two registers             | -              |
| x     | xx    | xx    | 110   | 0     | 1xx   | x     | SME2 multiple vectors ternary int two registers            | -              |
| x     | != 00 | xx    | 111   | 0     | xxx   | x     | UNALLOCATED                                                | -              |

## SME2 multiple vectors long FMA two sources

The encodings in this section are decoded from SME2 Multi-vector - Multiple Array Vectors (Two registers).

<!-- image -->

| 31   | 17 16 15 14 13 12 10 9   |
|------|--------------------------|
| 1 1  | Zm 0 0 Rv 0 1 0 Zn       |

|   op | S Instruction Details                   | Feature   |
|------|-----------------------------------------|-----------|
|    0 | 0 FMLAL(multiple vectors, FP16 to FP32) | FEAT_SME2 |
|    0 | 1 FMLSL (multiple vectors)              | FEAT_SME2 |
|    1 | 0 BFMLAL(multiple vectors)              | FEAT_SME2 |
|    1 | 1 BFMLSL (multiple vectors)             | FEAT_SME2 |

## SME2 multiple vectors FP dot product two registers

The encodings in this section are decoded from SME2 Multi-vector - Multiple Array Vectors (Two registers).

<!-- image -->

|   opc | Instruction Details                          | Feature        |
|-------|----------------------------------------------|----------------|
|    00 | FDOT (2-way, multiple vectors, FP16 to FP32) | FEAT_SME2      |
|    01 | BFDOT (multiple vectors)                     | FEAT_SME2      |
|    10 | FDOT (2-way, multiple vectors, FP8 to FP16)  | FEAT_SME_F8F16 |
|    11 | FDOT (4-way, multiple vectors)               | FEAT_SME_F8F32 |

## SME2 multiple vectors long MLA two sources

The encodings in this section are decoded from SME2 Multi-vector - Multiple Array Vectors (Two registers).

<!-- image -->

## SME2 multiple vectors binary FP two registers

The encodings in this section are decoded from SME2 Multi-vector - Multiple Array Vectors (Two registers).

<!-- image -->

| 31    | 23 22 21 20 19 18 17 16 15 14 13 12 10 9 6 5 4 3 2   |
|-------|------------------------------------------------------|
| 1 1 0 | 1 sz 1 0 0 0 0 0 0 Rv 1 1 1 Zm 0 0 S off3            |

|   S | Instruction Details   | Feature   |
|-----|-----------------------|-----------|
|   0 | FADD                  | FEAT_SME2 |
|   1 | FSUB                  | FEAT_SME2 |

|   U |   S | Instruction Details      | Feature   |
|-----|-----|--------------------------|-----------|
|   0 |   0 | SMLAL(multiple vectors)  | FEAT_SME2 |
|   0 |   1 | SMLSL (multiple vectors) | FEAT_SME2 |
|   1 |   0 | UMLAL(multiple vectors)  | FEAT_SME2 |
|   1 |   1 | UMLSL(multiple vectors)  | FEAT_SME2 |

## SME2 multiple vectors two-way dot product two registers

The encodings in this section are decoded from SME2 Multi-vector - Multiple Array Vectors (Two registers).

<!-- image -->

| 31    | 20 17 16 15 14 13 12 10 9 6 5 4   |
|-------|-----------------------------------|
| 1 1 0 | Zm 0 0 Rv 1 0 1 Zn 0 U            |

|   U | Instruction Details            | Feature   |
|-----|--------------------------------|-----------|
|   0 | SDOT (2-way, multiple vectors) | FEAT_SME2 |
|   1 | UDOT(2-way, multiple vectors)  | FEAT_SME2 |

## SME2 multiple vectors binary int two registers

The encodings in this section are decoded from SME2 Multi-vector - Multiple Array Vectors (Two registers).

<!-- image -->

| 31   | 23 22 21 20 19 18 17 16 15 14 13 12 10 9 6 5 4 3   |
|------|----------------------------------------------------|
| 1 1  | 1 sz 1 0 0 0 0 0 0 Rv 1 1 1 Zm 0 1 S               |

|   S | Instruction Details                        | Feature   |
|-----|--------------------------------------------|-----------|
|   0 | ADD(to array, array and multiple vectors)  | FEAT_SME2 |
|   1 | SUB (to array, array and multiple vectors) | FEAT_SME2 |

## SME2 multiple vectors binary FP16 two registers

The encodings in this section are decoded from SME2 Multi-vector - Multiple Array Vectors (Two registers).

<!-- image -->

| 31    | 23 22 21 20 19 18 17 16 15 14 13 12 10 9 6 5 4 3   |
|-------|----------------------------------------------------|
| 1 1 0 | 1 sz 1 0 0 1 0 0 0 Rv 1 1 1 Zm 0 0 S               |

|   sz |   S | Instruction Details   | Feature                                     |
|------|-----|-----------------------|---------------------------------------------|
|    0 |   0 | FADD                  | FEAT_SME_F16F16 &#124;&#124; FEAT_SME_F8F16 |
|    0 |   1 | FSUB                  | FEAT_SME_F16F16 &#124;&#124; FEAT_SME_F8F16 |
|    1 |   0 | BFADD                 | FEAT_SME_B16B16                             |
|    1 |   1 | BFSUB                 | FEAT_SME_B16B16                             |

## SME2 multiple vectors long long MLA two sources

The encodings in this section are decoded from SME2 Multi-vector - Multiple Array Vectors (Two registers).

<!-- image -->

| sz   |   U |   S |   op | Instruction Details       | Feature   |
|------|-----|-----|------|---------------------------|-----------|
| x    |   0 |   0 |    0 | SMLALL(multiple vectors)  | FEAT_SME2 |
| x    |   0 |   1 |    0 | SMLSLL (multiple vectors) | FEAT_SME2 |

| sz   | U   | S   |   op | Instruction Details       | Feature   |
|------|-----|-----|------|---------------------------|-----------|
| x    | 1   | 0   |    0 | UMLALL(multiple vectors)  | FEAT_SME2 |
| x    | 1   | 1   |    0 | UMLSLL(multiple vectors)  | FEAT_SME2 |
| 0    | 0   | 0   |    1 | USMLALL(multiple vectors) | FEAT_SME2 |
| 0    | 0   | 1   |    1 | UNALLOCATED               | -         |
| 0    | 1   | x   |    1 | UNALLOCATED               | -         |
| 1    | x   | x   |    1 | UNALLOCATED               | -         |

## SME2 multiple vectors ternary FP16 two registers

The encodings in this section are decoded from SME2 Multi-vector - Multiple Array Vectors (Two registers).

<!-- image -->

| 31    | 23 22 21 20 17 16 15 14 13 12 10 9 6 5 4 3 2   |
|-------|------------------------------------------------|
| 1 1 0 | 1 sz 1 Zm 0 0 Rv 1 0 0 Zn 0 S 1 off3           |

|   sz | S               | Instruction Details      | Feature         |
|------|-----------------|--------------------------|-----------------|
|    0 | 0 FMLA(multiple | vectors)                 | FEAT_SME_F16F16 |
|    0 | 1               | FMLS (multiple vectors)  | FEAT_SME_F16F16 |
|    1 | 0               | BFMLA(multiple vectors)  | FEAT_SME_B16B16 |
|    1 | 1               | BFMLS (multiple vectors) | FEAT_SME_B16B16 |

## SME2 multiple vectors four-way dot product two registers

The encodings in this section are decoded from SME2 Multi-vector - Multiple Array Vectors (Two registers).

<!-- image -->

|   U | Instruction Details            | Feature   |
|-----|--------------------------------|-----------|
|   0 | SDOT (4-way, multiple vectors) | FEAT_SME2 |
|   1 | UDOT(4-way, multiple vectors)  | FEAT_SME2 |

## SME2 multiple vectors ternary FP two registers

The encodings in this section are decoded from SME2 Multi-vector - Multiple Array Vectors (Two registers).

<!-- image -->

| 31   | 23 22 21 20 17 16 15 14 13 12 10 9 6 5 4 3   |
|------|----------------------------------------------|
| 1 1  | 1 sz 1 Zm 0 0 Rv 1 1 0 Zn 0 0 S              |

|   S | Instruction Details     | Feature   |
|-----|-------------------------|-----------|
|   0 | FMLA(multiple vectors)  | FEAT_SME2 |
|   1 | FMLS (multiple vectors) | FEAT_SME2 |

## SME2 multiple vectors ternary int two registers

The encodings in this section are decoded from SME2 Multi-vector - Multiple Array Vectors (Two registers).

<!-- image -->

| 31    | 20 17 16 15 14 13 12 10 9 6 5 4 3   |
|-------|-------------------------------------|
| 1 1 0 | Zm 0 0 Rv 1 1 0 Zn 0 1 S            |

|   S | Instruction Details              | Feature   |
|-----|----------------------------------|-----------|
|   0 | ADD(to array, multiple vectors)  | FEAT_SME2 |
|   1 | SUB (to array, multiple vectors) | FEAT_SME2 |

## SME2 Multi-vector - Multiple Array Vectors (Four registers)

SME2 Multi-vector - Multiple Array Vectors (Four registers)

The encodings in this section are decoded from SME encodings.

<!-- image -->

|   op0 | op1   | op2   |   op3 |   op4 | op5   |   op6 | Instruction details                              | Feature        |
|-------|-------|-------|-------|-------|-------|-------|--------------------------------------------------|----------------|
|     0 | xx    | x0    |   000 |    01 | 000   |     0 | FMLALL (multiple vectors) - Four ZA quad-vectors | FEAT_SME_F8F32 |
|     0 | xx    | x0    |   000 |    01 | 001   |     0 | UNALLOCATED                                      | -              |
|     0 | xx    | x0    |   000 |    01 | 10x   |     0 | UNALLOCATED                                      | -              |

| op0   | op1   | op2   | op3   | op4   | op5   | op6   | Instruction details                                          | Feature        |
|-------|-------|-------|-------|-------|-------|-------|--------------------------------------------------------------|----------------|
| 0     | xx    | x0    | 000   | 01    | x0x   | 1     | UNALLOCATED                                                  | -              |
| 0     | xx    | x0    | 010   | 00    | xx0   | x     | SME2 multiple vectors long FMA four sources                  | -              |
| 0     | xx    | x0    | 010   | 01    | 000   | x     | FMLAL (multiple vectors, FP8 to FP16) -Four ZAdouble-vectors | FEAT_SME_F8F16 |
| 0     | xx    | x0    | 010   | 01    | 100   | x     | UNALLOCATED                                                  | -              |
| 0     | xx    | x0    | 010   | 01    | x01   | x     | UNALLOCATED                                                  | -              |
| 0     | xx    | x0    | 0x1   | 01    | xxx   | x     | UNALLOCATED                                                  | -              |
| 0     | xx    | x0    | 100   | 0x    | x0x   | x     | SME2multiple vectors FP dot product four registers           | -              |
| 0     | xx    | x0    | 101   | 00    | 01x   | x     | USDOT (4-way, multiple vectors) -Four ZAsingle-vectors       | FEAT_SME2      |
| 0     | xx    | x0    | 101   | 00    | 11x   | x     | UNALLOCATED                                                  | -              |
| 0     | xx    | x0    | 110   | 01    | x0x   | x     | UNALLOCATED                                                  | -              |
| 0     | xx    | x0    | 1x1   | 01    | xxx   | x     | UNALLOCATED                                                  | -              |
| 0     | xx    | x0    | xx0   | 01    | x1x   | x     | UNALLOCATED                                                  | -              |
| 1     | xx    | x0    | 010   | 00    | xx0   | x     | SME2 multiple vectors long MLA four sources                  | -              |
| 1     | xx    | x0    | 100   | 00    | x0x   | x     | UNALLOCATED                                                  | -              |
| 1     | xx    | x0    | 101   | 00    | x1x   | x     | SME2 multiple vectors two-way dot product four registers     | -              |
| 1     | xx    | x0    | xxx   | 01    | xxx   | x     | UNALLOCATED                                                  | -              |
| x     | 00    | 00    | 111   | 00    | 0xx   | x     | SME2 multiple vectors binary FP four registers               | -              |
| x     | 00    | 00    | 111   | 00    | 1xx   | x     | SME2 multiple vectors binary int four registers              | -              |
| x     | 00    | 10    | 111   | 00    | 0xx   | x     | SME2 multiple vectors binary FP16 four registers             | -              |
| x     | 00    | 10    | 111   | 00    | 1xx   | x     | UNALLOCATED                                                  | -              |
| x     | xx    | x0    | 000   | 00    | xxx   | 0     | SME2 multiple vectors long long MLA four sources             | -              |
| x     | xx    | x0    | 000   | 00    | xxx   | 1     | UNALLOCATED                                                  | -              |
| x     | xx    | x0    | 010   | 00    | xx1   | x     | UNALLOCATED                                                  | -              |
| x     | xx    | x0    | 0x1   | 00    | xxx   | x     | UNALLOCATED                                                  | -              |
| x     | xx    | x0    | 100   | 00    | x1x   | x     | SME2 multiple vectors ternary FP16 four registers            | -              |
| x     | xx    | x0    | 101   | 00    | x0x   | x     | SME2 multiple vectors four-way dot product four registers    | -              |
| x     | xx    | x0    | 110   | 00    | 0xx   | x     | SME2 multiple vectors ternary FP four registers              | -              |
| x     | xx    | x0    | 110   | 00    | 1xx   | x     | SME2 multiple vectors ternary int four registers             | -              |
| x     | xx    | x0    | xxx   | 1x    | xxx   | x     | UNALLOCATED                                                  | -              |
| x     | xx    | x1    | xxx   | xx    | xxx   | x     | UNALLOCATED                                                  | -              |
| x     | != 00 | x0    | 111   | 00    | xxx   | x     | UNALLOCATED                                                  | -              |

## SME2 multiple vectors long FMA four sources

The encodings in this section are decoded from SME2 Multi-vector - Multiple Array Vectors (Four registers).

<!-- image -->

|   31 |     | 23 22   |       |   21 |   20 | 18   | 17   |   15 | 14 13   | 12   | 10 9   | 7   | 6 5 4   | 3   |     | 2 1   | 0    |
|------|-----|---------|-------|------|------|------|------|------|---------|------|--------|-----|---------|-----|-----|-------|------|
|    1 | 1 0 | 0 0 0   | 0 1 1 |    0 |    1 | Zm   | 0 1  |    0 | Rv 0    | 1 0  |        | Zn  | 0 0     | op  | S 0 |       | off2 |

|   op | S Instruction Details                   | Feature   |
|------|-----------------------------------------|-----------|
|    0 | 0 FMLAL(multiple vectors, FP16 to FP32) | FEAT_SME2 |
|    0 | 1 FMLSL (multiple vectors)              | FEAT_SME2 |
|    1 | 0 BFMLAL(multiple vectors)              | FEAT_SME2 |
|    1 | 1 BFMLSL (multiple vectors)             | FEAT_SME2 |

## SME2 multiple vectors FP dot product four registers

The encodings in this section are decoded from SME2 Multi-vector - Multiple Array Vectors (Four registers).

<!-- image -->

|   opc | Instruction Details                          | Feature        |
|-------|----------------------------------------------|----------------|
|    00 | FDOT (2-way, multiple vectors, FP16 to FP32) | FEAT_SME2      |
|    01 | BFDOT (multiple vectors)                     | FEAT_SME2      |
|    10 | FDOT (2-way, multiple vectors, FP8 to FP16)  | FEAT_SME_F8F16 |
|    11 | FDOT (4-way, multiple vectors)               | FEAT_SME_F8F32 |

## SME2 multiple vectors long MLA four sources

The encodings in this section are decoded from SME2 Multi-vector - Multiple Array Vectors (Four registers).

<!-- image -->

## SME2 multiple vectors binary FP four registers

The encodings in this section are decoded from SME2 Multi-vector - Multiple Array Vectors (Four registers).

<!-- image -->

| 31    | 23 22 21 20 19 18 17 16 15 14 13 12 10 9 7 6 5 4 3 2   |
|-------|--------------------------------------------------------|
| 1 1 0 | 1 sz 1 0 0 0 0 1 0 Rv 1 1 1 Zm 0 0 0 S off3            |

|   S | Instruction Details   | Feature   |
|-----|-----------------------|-----------|
|   0 | FADD                  | FEAT_SME2 |
|   1 | FSUB                  | FEAT_SME2 |

|   U |   S | Instruction Details      | Feature   |
|-----|-----|--------------------------|-----------|
|   0 |   0 | SMLAL(multiple vectors)  | FEAT_SME2 |
|   0 |   1 | SMLSL (multiple vectors) | FEAT_SME2 |
|   1 |   0 | UMLAL(multiple vectors)  | FEAT_SME2 |
|   1 |   1 | UMLSL(multiple vectors)  | FEAT_SME2 |

## SME2 multiple vectors two-way dot product four registers

The encodings in this section are decoded from SME2 Multi-vector - Multiple Array Vectors (Four registers).

<!-- image -->

| 31   | 23 22 21 20 18 17 15 14 13 12 10   |
|------|------------------------------------|
| 1 1  | 1 1 1 Zm 0 1 0 Rv 1 0 1            |

|   U | Instruction Details            | Feature   |
|-----|--------------------------------|-----------|
|   0 | SDOT (2-way, multiple vectors) | FEAT_SME2 |
|   1 | UDOT(2-way, multiple vectors)  | FEAT_SME2 |

## SME2 multiple vectors binary int four registers

The encodings in this section are decoded from SME2 Multi-vector - Multiple Array Vectors (Four registers).

<!-- image -->

| 31   | 23 22 21 20 19 18 17 16 15 14 13 12 10 9 7 6 5 4 3 2   |
|------|--------------------------------------------------------|
| 1 1  | 1 sz 1 0 0 0 0 1 0 Rv 1 1 1 Zm 0 0 1 S off3            |

|   S | Instruction Details                        | Feature   |
|-----|--------------------------------------------|-----------|
|   0 | ADD(to array, array and multiple vectors)  | FEAT_SME2 |
|   1 | SUB (to array, array and multiple vectors) | FEAT_SME2 |

## SME2 multiple vectors binary FP16 four registers

The encodings in this section are decoded from SME2 Multi-vector - Multiple Array Vectors (Four registers).

<!-- image -->

| 31    | 23 22 21 20 19 18 17 16 15 14 13 12 10 9 7 6 5 4 3 2   |
|-------|--------------------------------------------------------|
| 1 1 0 | 1 sz 1 0 0 1 0 1 0 Rv 1 1 1 Zm 0 0 0 S off3            |

|   sz |   S | Instruction Details   | Feature                                     |
|------|-----|-----------------------|---------------------------------------------|
|    0 |   0 | FADD                  | FEAT_SME_F16F16 &#124;&#124; FEAT_SME_F8F16 |
|    0 |   1 | FSUB                  | FEAT_SME_F16F16 &#124;&#124; FEAT_SME_F8F16 |
|    1 |   0 | BFADD                 | FEAT_SME_B16B16                             |
|    1 |   1 | BFSUB                 | FEAT_SME_B16B16                             |

## SME2 multiple vectors long long MLA four sources

The encodings in this section are decoded from SME2 Multi-vector - Multiple Array Vectors (Four registers).

<!-- image -->

| sz   |   U |   S |   op | Instruction Details       | Feature   |
|------|-----|-----|------|---------------------------|-----------|
| x    |   0 |   0 |    0 | SMLALL(multiple vectors)  | FEAT_SME2 |
| x    |   0 |   1 |    0 | SMLSLL (multiple vectors) | FEAT_SME2 |

| sz   | U   | S   |   op | Instruction Details       | Feature   |
|------|-----|-----|------|---------------------------|-----------|
| x    | 1   | 0   |    0 | UMLALL(multiple vectors)  | FEAT_SME2 |
| x    | 1   | 1   |    0 | UMLSLL(multiple vectors)  | FEAT_SME2 |
| 0    | 0   | 0   |    1 | USMLALL(multiple vectors) | FEAT_SME2 |
| 0    | 0   | 1   |    1 | UNALLOCATED               | -         |
| 0    | 1   | x   |    1 | UNALLOCATED               | -         |
| 1    | x   | x   |    1 | UNALLOCATED               | -         |

## SME2 multiple vectors ternary FP16 four registers

The encodings in this section are decoded from SME2 Multi-vector - Multiple Array Vectors (Four registers).

<!-- image -->

| 31    | 23 22 21 20 18 17 15 14 13 12 10   |
|-------|------------------------------------|
| 1 1 0 | 1 sz 1 Zm 0 1 0 Rv 1 0 0           |

|   sz | S               | Instruction Details      | Feature         |
|------|-----------------|--------------------------|-----------------|
|    0 | 0 FMLA(multiple | vectors)                 | FEAT_SME_F16F16 |
|    0 | 1               | FMLS (multiple vectors)  | FEAT_SME_F16F16 |
|    1 | 0               | BFMLA(multiple vectors)  | FEAT_SME_B16B16 |
|    1 | 1               | BFMLS (multiple vectors) | FEAT_SME_B16B16 |

## SME2 multiple vectors four-way dot product four registers

The encodings in this section are decoded from SME2 Multi-vector - Multiple Array Vectors (Four registers).

<!-- image -->

|   U | Instruction Details            | Feature   |
|-----|--------------------------------|-----------|
|   0 | SDOT (4-way, multiple vectors) | FEAT_SME2 |
|   1 | UDOT(4-way, multiple vectors)  | FEAT_SME2 |

## SME2 multiple vectors ternary FP four registers

The encodings in this section are decoded from SME2 Multi-vector - Multiple Array Vectors (Four registers).

<!-- image -->

| 31   | 23 22 21 20 18 17 15 14 13 12 10 9 7 6 5 4 3 2   |
|------|--------------------------------------------------|
| 1 1  | 1 sz 1 Zm 0 1 0 Rv 1 1 0 Zn 0 0 0 S off3         |

|   S | Instruction Details     | Feature   |
|-----|-------------------------|-----------|
|   0 | FMLA(multiple vectors)  | FEAT_SME2 |
|   1 | FMLS (multiple vectors) | FEAT_SME2 |

## SME2 multiple vectors ternary int four registers

The encodings in this section are decoded from SME2 Multi-vector - Multiple Array Vectors (Four registers).

<!-- image -->

| 31   |       | 23 22   | 21   |    | 20   | 17   |   15 | 14 13   | 12   |   10 | 9   | 7 6   |   5 | 4   | 3   | 0    |
|------|-------|---------|------|----|------|------|------|---------|------|------|-----|-------|-----|-----|-----|------|
| 1 1  | 0 0 0 | 0 1 1   | sz   |  1 | Zm   | 0 1  |    0 | Rv      | 1 1  |    0 | Zn  | 0 0   |   1 |     | S   | off3 |

|   S | Instruction Details              | Feature   |
|-----|----------------------------------|-----------|
|   0 | ADD(to array, multiple vectors)  | FEAT_SME2 |
|   1 | SUB (to array, multiple vectors) | FEAT_SME2 |

## SME2 Multi-vector - Indexed (One register)

SME2 Multi-vector - Indexed (One register)

The encodings in this section are decoded from SME encodings.

<!-- image -->

|   op0 | op1   | op2    | Instruction details                                    | Feature        |
|-------|-------|--------|--------------------------------------------------------|----------------|
|    00 | x     | xxx    | SME2 multi-vec indexed long long MLA one source 32-bit | -              |
|    01 | x     | 000    | FMLALL(multiple and indexed vector)- One ZAquad-vector | FEAT_SME_F8F32 |
|    01 | x     | != 000 | UNALLOCATED                                            | -              |

|   op0 |   op1 | op2   | Instruction details                                                 | Feature        |
|-------|-------|-------|---------------------------------------------------------------------|----------------|
|    10 |     0 | xx0   | SME2 multi-vec indexed long long MLA one source 64-bit              | -              |
|    10 |     0 | xx1   | UNALLOCATED                                                         | -              |
|    10 |     1 | xxx   | SME2 multi-vec indexed long FMA one source                          | -              |
|    11 |     0 | 0xx   | FMLAL(multiple and indexed vector, FP8 to FP16) -OneZAdouble-vector | FEAT_SME_F8F16 |
|    11 |     0 | 1xx   | UNALLOCATED                                                         | -              |
|    11 |     1 | xxx   | SME2 multi-vec indexed long MLA one source                          | -              |

## SME2 multi-vec indexed long long MLA one source 32-bit

The encodings in this section are decoded from SME2 Multi-vector - Indexed (One register).

<!-- image -->

| 31    | 24 23 22 21 20 19   | 16 15 14 13 12 10 9 5 4 3 2 1 0   |
|-------|---------------------|-----------------------------------|
| 1 1 0 | 1 0 0 0 0 Zm i4h Rv | i4l Zn U S op off2                |

| U   | S op   | Instruction Details                  | Feature   |
|-----|--------|--------------------------------------|-----------|
| x   | 1 1    | UNALLOCATED                          | -         |
| 0   | 0 0    | SMLALL(multiple and indexed vector)  | FEAT_SME2 |
| 0   | 0 1    | USMLALL(multiple and indexed vector) | FEAT_SME2 |
| 0   | 1 0    | SMLSLL (multiple and indexed vector) | FEAT_SME2 |
| 1   | 0 0    | UMLALL(multiple and indexed vector)  | FEAT_SME2 |
| 1   | 0 1    | SUMLALL(multiple and indexed vector) | FEAT_SME2 |
| 1   | 1 0    | UMLSLL(multiple and indexed vector)  | FEAT_SME2 |

## SME2 multi-vec indexed long long MLA one source 64-bit

The encodings in this section are decoded from SME2 Multi-vector - Indexed (One register).

<!-- image -->

| 31   | 24 23 22 21 20 19   | 16 15 14 13 12 11 10 9 5 4 3 2   |
|------|---------------------|----------------------------------|
| 1 1  | 1 1 0 0 0 Zm i3h Rv | 0 i3l Zn U S 0                   |

|   U |   S | Instruction Details                 | Feature                     |
|-----|-----|-------------------------------------|-----------------------------|
|   0 |   0 | SMLALL(multiple and indexed vector) | FEAT_SME2 &&FEAT_SME_I16I64 |

|   U |   S | Instruction Details                  | Feature                     |
|-----|-----|--------------------------------------|-----------------------------|
|   0 |   1 | SMLSLL (multiple and indexed vector) | FEAT_SME2 &&FEAT_SME_I16I64 |
|   1 |   0 | UMLALL(multiple and indexed vector)  | FEAT_SME2 &&FEAT_SME_I16I64 |
|   1 |   1 | UMLSLL(multiple and indexed vector)  | FEAT_SME2 &&FEAT_SME_I16I64 |

## SME2 multi-vec indexed long FMA one source

The encodings in this section are decoded from SME2 Multi-vector - Indexed (One register).

<!-- image -->

| 31      | 24 23 22 21 20 19 16 15 14 13 12 11 10 9 5 4   |
|---------|------------------------------------------------|
| 1 1 0 0 | 1 1 0 0 0 Zm i3h Rv 1 i3l Zn op                |

|   op | S Instruction Details                               | Feature   |
|------|-----------------------------------------------------|-----------|
|    0 | 0 FMLAL (multiple and indexed vector, FP16 to FP32) | FEAT_SME2 |
|    0 | 1 FMLSL (multiple and indexed vector)               | FEAT_SME2 |
|    1 | 0 BFMLAL(multiple and indexed vector)               | FEAT_SME2 |
|    1 | 1 BFMLSL (multiple and indexed vector)              | FEAT_SME2 |

## SME2 multi-vec indexed long MLA one source

The encodings in this section are decoded from SME2 Multi-vector - Indexed (One register).

<!-- image -->

|   U |   S | Instruction Details                 | Feature   |
|-----|-----|-------------------------------------|-----------|
|   0 |   0 | SMLAL(multiple and indexed vector)  | FEAT_SME2 |
|   0 |   1 | SMLSL (multiple and indexed vector) | FEAT_SME2 |
|   1 |   0 | UMLAL(multiple and indexed vector)  | FEAT_SME2 |
|   1 |   1 | UMLSL(multiple and indexed vector)  | FEAT_SME2 |

## SME2 Multi-vector - Indexed (Two registers)

SME2 Multi-vector - Indexed (Two registers)

The encodings in this section are decoded from SME encodings.

<!-- image -->

| 31   | 24 23 22 21 20 19 16 15   |
|------|---------------------------|

|   op0 | op1   | op2   | op3   | Instruction details                                                                       | Feature        |
|-------|-------|-------|-------|-------------------------------------------------------------------------------------------|----------------|
|    00 | 0x    | x     | xx    | SME2 multi-vec indexed long long MLA two sources 32-bit                                   | -              |
|    00 | 1x    | x     | xx    | SME2 multi-vec ternary indexed two registers 16-bit                                       | -              |
|    01 | xx    | x     | xx    | SME2 multi-vec ternary indexed two registers 32-bit                                       | -              |
|    10 | 00    | 0     | xx    | SME2 multi-vec indexed long long MLA two sources 64-bit                                   | -              |
|    10 | 01    | 0     | xx    | UNALLOCATED                                                                               | -              |
|    10 | 0x    | 1     | 00    | FMLALL(multiple and indexed vector)- Two ZAquad-vectors                                   | FEAT_SME_F8F32 |
|    10 | 0x    | 1     | != 00 | UNALLOCATED                                                                               | -              |
|    10 | 1x    | 0     | xx    | SME2 multi-vec indexed long FMA two sources                                               | -              |
|    10 | 1x    | 1     | 0x    | UNALLOCATED                                                                               | -              |
|    10 | 1x    | 1     | 1x    | FMLAL(multiple and indexed vector, FP8 to FP16) -TwoZAdouble-vectors                      | FEAT_SME_F8F16 |
|    11 | 00    | 0     | xx    | SME2 multi-vec ternary indexed two registers 64-bit                                       | -              |
|    11 | 01    | 0     | xx    | SME2 multi-vec indexed FP8 two-way vertical dot product to single-precision two registers | -              |
|    11 | 1x    | 0     | xx    | SME2 multi-vec indexed long MLA two sources                                               | -              |
|    11 | xx    | 1     | 0x    | SME2 multi-vec indexed FP8 two-way dot product to FP16 two registers                      | -              |
|    11 | xx    | 1     | 1x    | UNALLOCATED                                                                               | -              |

## SME2 multi-vec indexed long long MLA two sources 32-bit

The encodings in this section are decoded from SME2 Multi-vector - Indexed (Two registers).

<!-- image -->

| 31      | 24 23 22 21 20 19 16 15 14 13 12 11 10 9 6 5 4 3 2   |
|---------|------------------------------------------------------|
| 1 1 0 0 | 1 0 0 0 1 Zm 0 Rv 0 i4h Zn op U S i4l                |

|   op | U   |   S | Instruction Details                  | Feature   |
|------|-----|-----|--------------------------------------|-----------|
|    0 | 0   |   0 | SMLALL(multiple and indexed vector)  | FEAT_SME2 |
|    0 | 0   |   1 | SMLSLL (multiple and indexed vector) | FEAT_SME2 |
|    0 | 1   |   0 | UMLALL(multiple and indexed vector)  | FEAT_SME2 |
|    0 | 1   |   1 | UMLSLL(multiple and indexed vector)  | FEAT_SME2 |
|    1 | x   |   1 | UNALLOCATED                          | -         |
|    1 | 0   |   0 | USMLALL(multiple and indexed vector) | FEAT_SME2 |
|    1 | 1   |   0 | SUMLALL(multiple and indexed vector) | FEAT_SME2 |

## SME2 multi-vec ternary indexed two registers 16-bit

The encodings in this section are decoded from SME2 Multi-vector - Indexed (Two registers).

<!-- image -->

|   op |   S | Instruction Details                 | Feature         |
|------|-----|-------------------------------------|-----------------|
|    0 |   0 | FMLA(multiple and indexed vector)   | FEAT_SME_F16F16 |
|    0 |   1 | FMLS (multiple and indexed vector)  | FEAT_SME_F16F16 |
|    1 |   0 | BFMLA(multiple and indexed vector)  | FEAT_SME_B16B16 |
|    1 |   1 | BFMLS (multiple and indexed vector) | FEAT_SME_B16B16 |

## SME2 multi-vec ternary indexed two registers 32-bit

The encodings in this section are decoded from SME2 Multi-vector - Indexed (Two registers).

<!-- image -->

| 31    | 24 23 22 21 20 19    | 16 15 14 13 12 11 10 9 6 5 3 2   |
|-------|----------------------|----------------------------------|
| 1 1 0 | 1 0 1 0 1 Zm 0 Rv op | i2 Zn opc2 off3                  |

|   op |   opc2 | Instruction Details                | Feature   |
|------|--------|------------------------------------|-----------|
|    0 |    000 | FMLA(multiple and indexed vector)  | FEAT_SME2 |
|    0 |    001 | FVDOT(FP16 to FP32)                | FEAT_SME2 |
|    0 |    010 | FMLS (multiple and indexed vector) | FEAT_SME2 |
|    0 |    011 | BFVDOT                             | FEAT_SME2 |
|    0 |    100 | SVDOT(2-way)                       | FEAT_SME2 |

|   op |   opc2 | Instruction Details                                     | Feature        |
|------|--------|---------------------------------------------------------|----------------|
|    0 |    101 | UNALLOCATED                                             | -              |
|    0 |    110 | UVDOT(2-way)                                            | FEAT_SME2      |
|    0 |    111 | FDOT (4-way, multiple and indexed vector)               | FEAT_SME_F8F32 |
|    1 |    000 | SDOT (2-way, multiple and indexed vector)               | FEAT_SME2      |
|    1 |    001 | FDOT (2-way, multiple and indexed vector, FP16 to FP32) | FEAT_SME2      |
|    1 |    010 | UDOT (2-way, multiple and indexed vector)               | FEAT_SME2      |
|    1 |    011 | BFDOT (multiple and indexed vector)                     | FEAT_SME2      |
|    1 |    100 | SDOT (4-way, multiple and indexed vector)               | FEAT_SME2      |
|    1 |    101 | USDOT (4-way, multiple and indexed vector)              | FEAT_SME2      |
|    1 |    110 | UDOT (4-way, multiple and indexed vector)               | FEAT_SME2      |
|    1 |    111 | SUDOT (4-way, multiple and indexed vector)              | FEAT_SME2      |

## SME2 multi-vec indexed long long MLA two sources 64-bit

The encodings in this section are decoded from SME2 Multi-vector - Indexed (Two registers).

<!-- image -->

| 31    | 24 23 22 21 20 19   | 16 15 14 13 12 11 10 9   |
|-------|---------------------|--------------------------|
| 1 1 0 | 1 1 0 0 1 Zm 0 Rv   | 0 0 i3h Zn               |

|   U |   S | Instruction Details                  | Feature                     |
|-----|-----|--------------------------------------|-----------------------------|
|   0 |   0 | SMLALL(multiple and indexed vector)  | FEAT_SME2 &&FEAT_SME_I16I64 |
|   0 |   1 | SMLSLL (multiple and indexed vector) | FEAT_SME2 &&FEAT_SME_I16I64 |
|   1 |   0 | UMLALL(multiple and indexed vector)  | FEAT_SME2 &&FEAT_SME_I16I64 |
|   1 |   1 | UMLSLL(multiple and indexed vector)  | FEAT_SME2 &&FEAT_SME_I16I64 |

## SME2 multi-vec indexed long FMA two sources

The encodings in this section are decoded from SME2 Multi-vector - Indexed (Two registers).

<!-- image -->

| 31    | 24 23 22 21 20 19   | 16 15 14 13 12 11 10 9 6 5 4 3 2   |
|-------|---------------------|------------------------------------|
| 1 1 0 | 1 1 0 0 1 Zm 0      | Rv 1 i3h Zn 0 op S i3l             |

|   op | S Instruction Details                               | Feature   |
|------|-----------------------------------------------------|-----------|
|    0 | 0 FMLAL (multiple and indexed vector, FP16 to FP32) | FEAT_SME2 |
|    0 | 1 FMLSL (multiple and indexed vector)               | FEAT_SME2 |
|    1 | 0 BFMLAL(multiple and indexed vector)               | FEAT_SME2 |
|    1 | 1 BFMLSL (multiple and indexed vector)              | FEAT_SME2 |

## SME2 multi-vec ternary indexed two registers 64-bit

The encodings in this section are decoded from SME2 Multi-vector - Indexed (Two registers).

<!-- image -->

| 31   | 24 23 22 21 20 19        | 16 15 14 13 12 11 10 9 6 5 4 3 2   |
|------|--------------------------|------------------------------------|
| 1 1  | 1 1 1 0 1 Zm 0 Rv 0 0 i1 | Zn 0 opc off3                      |

|   opc | Instruction Details                       | Feature                     |
|-------|-------------------------------------------|-----------------------------|
|    00 | FMLA(multiple and indexed vector)         | FEAT_SME2 &&FEAT_SME_F64F64 |
|    01 | SDOT (4-way, multiple and indexed vector) | FEAT_SME2 &&FEAT_SME_I16I64 |
|    10 | FMLS (multiple and indexed vector)        | FEAT_SME2 &&FEAT_SME_F64F64 |
|    11 | UDOT (4-way, multiple and indexed vector) | FEAT_SME2 &&FEAT_SME_I16I64 |

SME2 multi-vec indexed FP8 two-way vertical dot product to single-precision two registers

The encodings in this section are decoded from SME2 Multi-vector - Indexed (Two registers).

<!-- image -->

|   T | Instruction Details   | Feature        |
|-----|-----------------------|----------------|
|   0 | FVDOTB                | FEAT_SME_F8F32 |
|   1 | FVDOTT                | FEAT_SME_F8F32 |

## SME2 multi-vec indexed long MLA two sources

The encodings in this section are decoded from SME2 Multi-vector - Indexed (Two registers).

<!-- image -->

| 31    | 24 23 22 21 20 19   | 16 15 14 13 12 11 10 9 6 5 4 3   |
|-------|---------------------|----------------------------------|
| 1 1 0 | 1 1 1 0 1 Zm 0 Rv   | 1 i3h Zn 0 U S                   |

|   U |   S | Instruction Details                 | Feature   |
|-----|-----|-------------------------------------|-----------|
|   0 |   0 | SMLAL(multiple and indexed vector)  | FEAT_SME2 |
|   0 |   1 | SMLSL (multiple and indexed vector) | FEAT_SME2 |
|   1 |   0 | UMLAL(multiple and indexed vector)  | FEAT_SME2 |
|   1 |   1 | UMLSL(multiple and indexed vector)  | FEAT_SME2 |

## SME2 multi-vec indexed FP8 two-way dot product to FP16 two registers

The encodings in this section are decoded from SME2 Multi-vector - Indexed (Two registers).

<!-- image -->

|   op | Instruction Details                                    | Feature        |
|------|--------------------------------------------------------|----------------|
|    0 | FDOT (2-way, multiple and indexed vector, FP8 to FP16) | FEAT_SME_F8F16 |
|    1 | FVDOT(FP8 to FP16)                                     | FEAT_SME_F8F16 |

## SME2 Multi-vector - Indexed (Four registers)

SME2 Multi-vector - Indexed (Four registers)

The encodings in this section are decoded from SME encodings.

<!-- image -->

| 31   | 24 23 22 21 20 19   | 16 15 14 13 12 11 10 7 6 4   |
|------|---------------------|------------------------------|

| op0   | op1   | op2   | op3   | Instruction details                                                              | Feature        |
|-------|-------|-------|-------|----------------------------------------------------------------------------------|----------------|
| 00    | 0x    | 0xx   | x     | SME2 multi-vec indexed long long MLA four sources 32-bit                         | -              |
| 00    | 0x    | 100   | 0     | FMLALL(multiple and indexed vector)- Four ZAquad-vectors                         | FEAT_SME_F8F32 |
| 00    | 0x    | 100   | 1     | UNALLOCATED                                                                      | -              |
| 00    | 1x    | 0xx   | x     | SME2 multi-vec ternary indexed four registers 16-bit                             | -              |
| 00    | 1x    | 100   | x     | FDOT (2-way, multiple and indexed vector, FP8 to FP16) - Four ZA single- vectors | FEAT_SME_F8F16 |
| 00    | xx    | 101   | x     | UNALLOCATED                                                                      | -              |
| 00    | xx    | 11x   | x     | UNALLOCATED                                                                      | -              |
| 01    | xx    | 0xx   | x     | SME2 multi-vec ternary indexed four registers 32-bit                             | -              |
| 10    | 00    | 00x   | x     | SME2 multi-vec indexed long long MLA four sources 64-bit                         | -              |
| 10    | 01    | 00x   | x     | UNALLOCATED                                                                      | -              |
| 10    | 0x    | 01x   | x     | UNALLOCATED                                                                      | -              |
| 10    | 1x    | 00x   | x     | SME2 multi-vec indexed long FMA four sources                                     | -              |
| 10    | 1x    | 010   | x     | FMLAL(multiple and indexed vector, FP8 to FP16) -Four ZAdouble-vectors           | FEAT_SME_F8F16 |
| 10    | 1x    | 011   | x     | UNALLOCATED                                                                      | -              |
| 11    | 0x    | 00x   | x     | SME2 multi-vec ternary indexed four registers 64-bit                             | -              |
| 11    | 1x    | 00x   | x     | SME2 multi-vec indexed long MLA four sources                                     | -              |
| 11    | xx    | 01x   | x     | UNALLOCATED                                                                      | -              |
| != 00 | xx    | 1xx   | x     | UNALLOCATED                                                                      | -              |

## SME2 multi-vec indexed long long MLA four sources 32-bit

The encodings in this section are decoded from SME2 Multi-vector - Indexed (Four registers).

<!-- image -->

| 31   | 23 22 21 20 19 16 15 14   |
|------|---------------------------|

|   op |   U |   S | Instruction Details                  | Feature   |
|------|-----|-----|--------------------------------------|-----------|
|    0 |   0 |   0 | SMLALL(multiple and indexed vector)  | FEAT_SME2 |
|    0 |   0 |   1 | SMLSLL (multiple and indexed vector) | FEAT_SME2 |
|    0 |   1 |   0 | UMLALL(multiple and indexed vector)  | FEAT_SME2 |
|    0 |   1 |   1 | UMLSLL(multiple and indexed vector)  | FEAT_SME2 |

|   op | U   | S                                      | Instruction Details Feature   |
|------|-----|----------------------------------------|-------------------------------|
|    1 | x   | 1 UNALLOCATED                          | -                             |
|    1 | 0   | 0 USMLALL(multiple and indexed vector) | FEAT_SME2                     |
|    1 | 1   | 0 SUMLALL(multiple and indexed vector) | FEAT_SME2                     |

## SME2 multi-vec ternary indexed four registers 16-bit

The encodings in this section are decoded from SME2 Multi-vector - Indexed (Four registers).

<!-- image -->

| 31    | 22 21 20 19 16 15 14 13 12 11 10 9 7 6 5 4 3 2   |
|-------|--------------------------------------------------|
| 1 1 0 | 0 0 1 Zm 1 Rv 1 i3h Zn 0 op S i3l off3           |

|   op |   S | Instruction Details                 | Feature         |
|------|-----|-------------------------------------|-----------------|
|    0 |   0 | FMLA(multiple and indexed vector)   | FEAT_SME_F16F16 |
|    0 |   1 | FMLS (multiple and indexed vector)  | FEAT_SME_F16F16 |
|    1 |   0 | BFMLA(multiple and indexed vector)  | FEAT_SME_B16B16 |
|    1 |   1 | BFMLS (multiple and indexed vector) | FEAT_SME_B16B16 |

## SME2 multi-vec ternary indexed four registers 32-bit

The encodings in this section are decoded from SME2 Multi-vector - Indexed (Four registers).

<!-- image -->

|   op |   opc2 | Instruction Details                       | Feature        |
|------|--------|-------------------------------------------|----------------|
|    0 |    000 | FMLA(multiple and indexed vector)         | FEAT_SME2      |
|    0 |    001 | FDOT (4-way, multiple and indexed vector) | FEAT_SME_F8F32 |
|    0 |    010 | FMLS (multiple and indexed vector)        | FEAT_SME2      |
|    0 |    011 | UNALLOCATED                               | -              |
|    0 |    100 | SVDOT(4-way)                              | FEAT_SME2      |
|    0 |    101 | USVDOT                                    | FEAT_SME2      |
|    0 |    110 | UVDOT(4-way)                              | FEAT_SME2      |
|    0 |    111 | SUVDOT                                    | FEAT_SME2      |

|   op |   opc2 | Instruction Details                 | Instruction Details                 | Instruction Details                 | Instruction Details                 | Feature   |
|------|--------|-------------------------------------|-------------------------------------|-------------------------------------|-------------------------------------|-----------|
|    1 |    000 | SDOT vector)                        | (2-way, multiple                    | and                                 | indexed                             | FEAT_SME2 |
|    1 |    001 | FDOT vector,                        | (2-way, multiple FP16 to FP32)      | and                                 | indexed                             | FEAT_SME2 |
|    1 |    010 | UDOT vector)                        | (2-way, multiple                    | and                                 | indexed                             | FEAT_SME2 |
|    1 |    011 | BFDOT (multiple and indexed vector) | BFDOT (multiple and indexed vector) | BFDOT (multiple and indexed vector) | BFDOT (multiple and indexed vector) | FEAT_SME2 |
|    1 |    100 | SDOT vector)                        | (4-way, multiple                    | and                                 | indexed                             | FEAT_SME2 |
|    1 |    101 | USDOT vector)                       | (4-way, multiple                    | and                                 | indexed                             | FEAT_SME2 |
|    1 |    110 | UDOT vector)                        | (4-way, multiple                    | and                                 | indexed                             | FEAT_SME2 |
|    1 |    111 | SUDOT vector)                       | (4-way, multiple                    | and                                 | indexed                             | FEAT_SME2 |

## SME2 multi-vec indexed long long MLA four sources 64-bit

The encodings in this section are decoded from SME2 Multi-vector - Indexed (Four registers).

<!-- image -->

| 31   | 24 23 22 21 20 19   | 16 15 14 13 12 11 10 9 7 6 5 4 3 2   |
|------|---------------------|--------------------------------------|
| 1 1  | 1 1 0 0 1 Zm 1 Rv   | 0 0 i3h Zn 0 0 U S                   |

|   U |   S | Instruction Details                  | Feature                     |
|-----|-----|--------------------------------------|-----------------------------|
|   0 |   0 | SMLALL(multiple and indexed vector)  | FEAT_SME2 &&FEAT_SME_I16I64 |
|   0 |   1 | SMLSLL (multiple and indexed vector) | FEAT_SME2 &&FEAT_SME_I16I64 |
|   1 |   0 | UMLALL(multiple and indexed vector)  | FEAT_SME2 &&FEAT_SME_I16I64 |
|   1 |   1 | UMLSLL(multiple and indexed vector)  | FEAT_SME2 &&FEAT_SME_I16I64 |

## SME2 multi-vec indexed long FMA four sources

The encodings in this section are decoded from SME2 Multi-vector - Indexed (Four registers).

<!-- image -->

|   op | S Instruction Details                               | Feature   |
|------|-----------------------------------------------------|-----------|
|    0 | 0 FMLAL (multiple and indexed vector, FP16 to FP32) | FEAT_SME2 |
|    0 | 1 FMLSL (multiple and indexed vector)               | FEAT_SME2 |
|    1 | 0 BFMLAL(multiple and indexed vector)               | FEAT_SME2 |
|    1 | 1 BFMLSL (multiple and indexed vector)              | FEAT_SME2 |

## SME2 multi-vec ternary indexed four registers 64-bit

The encodings in this section are decoded from SME2 Multi-vector - Indexed (Four registers).

<!-- image -->

| 31   | 24 23 22 21 20 19      | 16 15 14 13 12 11 10 9 7 6 5 4 3 2   |
|------|------------------------|--------------------------------------|
| 1 1  | 1 1 1 0 1 Zm 1 Rv 0 op | i1 Zn 0 0 opc2                       |

|   op | opc2   | Instruction Details                       | Feature                     |
|------|--------|-------------------------------------------|-----------------------------|
|    0 | 00     | FMLA(multiple and indexed vector)         | FEAT_SME2 &&FEAT_SME_F64F64 |
|    0 | 01     | SDOT (4-way, multiple and indexed vector) | FEAT_SME2 &&FEAT_SME_I16I64 |
|    0 | 10     | FMLS (multiple and indexed vector)        | FEAT_SME2 &&FEAT_SME_F64F64 |
|    0 | 11     | UDOT (4-way, multiple and indexed vector) | FEAT_SME2 &&FEAT_SME_I16I64 |
|    1 | x0     | UNALLOCATED                               | -                           |
|    1 | 01     | SVDOT(4-way)                              | FEAT_SME2 &&FEAT_SME_I16I64 |
|    1 | 11     | UVDOT(4-way)                              | FEAT_SME2 &&FEAT_SME_I16I64 |

## SME2 multi-vec indexed long MLA four sources

The encodings in this section are decoded from SME2 Multi-vector - Indexed (Four registers).

<!-- image -->

| 31      | 24 23 22 21 20 19   | 16 15 14 13 12 11 10 9 7 6 5 4 3 2   |
|---------|---------------------|--------------------------------------|
| 1 1 0 0 | 1 1 1 0 1 Zm 1      | Rv 1 i3h Zn 0 0 U S i3l              |

|   U |   S | Instruction Details                 | Feature   |
|-----|-----|-------------------------------------|-----------|
|   0 |   0 | SMLAL(multiple and indexed vector)  | FEAT_SME2 |
|   0 |   1 | SMLSL (multiple and indexed vector) | FEAT_SME2 |
|   1 |   0 | UMLAL(multiple and indexed vector)  | FEAT_SME2 |

## SME2 single-multi int min/max two registers

The encodings in this section are decoded from SME2 Multi-vector - Multiple and Single SVE Destructive (Two registers).

<!-- image -->

|   U | S                                    | Instruction Details Feature   |
|-----|--------------------------------------|-------------------------------|
|   1 | 1 UMLSL(multiple and indexed vector) | FEAT_SME2                     |

## SME2 Multi-vector - Multiple and Single SVE Destructive (Two registers)

SME2 Multi-vector - Multiple and Single SVE Destructive (Two registers)

The encodings in this section are decoded from SME encodings.

<!-- image -->

| op0   | op1   | op2    | Instruction details                                                      |
|-------|-------|--------|--------------------------------------------------------------------------|
| 0     | 00    | 00x    | SME2 single-multi int min/max two registers                              |
| 0     | 00    | 101    | UNALLOCATED                                                              |
| 0     | 01    | 00x    | SME2 single-multi FP min/max two registers                               |
| 0     | 01    | 100    | SME2 multiple and single vector FSCALE two registers                     |
| 0     | 01    | 101    | UNALLOCATED                                                              |
| 0     | 0x    | x1x    | UNALLOCATED                                                              |
| 0     | 10    | xxx    | SME2 single-multi shift two registers                                    |
| 0     | 11    | 000    | SME2 single-multi add two registers                                      |
| 0     | 11    | != 000 | UNALLOCATED                                                              |
| 1     | 00    | 000    | SME2 single-multi signed saturating doubling multiply high two registers |
| 1     | 00    | x10    | UNALLOCATED                                                              |
| 1     | 00    | xx1    | UNALLOCATED                                                              |
| 1     | != 00 | xxx    | UNALLOCATED                                                              |
| x     | 00    | 100    | UNALLOCATED                                                              |

## SME2 single-multi FP min/max two registers

The encodings in this section are decoded from SME2 Multi-vector - Multiple and Single SVE Destructive (Two registers).

<!-- image -->

| size   |   op |   o2 | Instruction Details                 | Feature                     |
|--------|------|------|-------------------------------------|-----------------------------|
| 00     |    0 |    0 | BFMAX(multiple and single vector)   | FEAT_SME2 &&FEAT_SVE_B16B16 |
| 00     |    0 |    1 | BFMIN (multiple and single vector)  | FEAT_SME2 &&FEAT_SVE_B16B16 |
| 00     |    1 |    0 | BFMAXNM(multiple and single vector) | FEAT_SME2 &&FEAT_SVE_B16B16 |
| 00     |    1 |    1 | BFMINNM(multiple and single vector) | FEAT_SME2 &&FEAT_SVE_B16B16 |
| != 00  |    0 |    0 | FMAX(multiple and single vector)    | FEAT_SME2                   |
| != 00  |    0 |    1 | FMIN (multiple and single vector)   | FEAT_SME2                   |
| != 00  |    1 |    0 | FMAXNM(multiple and single vector)  | FEAT_SME2                   |
| != 00  |    1 |    1 | FMINNM(multiple and single vector)  | FEAT_SME2                   |

## SME2 multiple and single vector FSCALE two registers

The encodings in this section are decoded from SME2 Multi-vector - Multiple and Single SVE Destructive (Two registers).

<!-- image -->

| size   |   op | Instruction Details                  | Feature                      |
|--------|------|--------------------------------------|------------------------------|
| xx     |    1 | UNALLOCATED                          | -                            |
| 00     |    0 | BFSCALE (multiple and single vector) | FEAT_SME2 &&FEAT_SVE_BFSCALE |
| != 00  |    0 | FSCALE (multiple and single vector)  | FEAT_SME2 &&FEAT_FP8         |

|   op |   U | Instruction Details               | Feature   |
|------|-----|-----------------------------------|-----------|
|    0 |   0 | SMAX(multiple and single vector)  | FEAT_SME2 |
|    0 |   1 | UMAX(multiple and single vector)  | FEAT_SME2 |
|    1 |   0 | SMIN (multiple and single vector) | FEAT_SME2 |
|    1 |   1 | UMIN(multiple and single vector)  | FEAT_SME2 |

## SME2 single-multi shift two registers

The encodings in this section are decoded from SME2 Multi-vector - Multiple and Single SVE Destructive (Two registers).

<!-- image -->

| opc    | U   | Instruction Details                | Feature   |
|--------|-----|------------------------------------|-----------|
| 001    | 0   | SRSHL (multiple and single vector) | FEAT_SME2 |
| 001    | 1   | URSHL (multiple and single vector) | FEAT_SME2 |
| != 001 | x   | UNALLOCATED                        | -         |

## SME2 single-multi add two registers

The encodings in this section are decoded from SME2 Multi-vector - Multiple and Single SVE Destructive (Two registers).

<!-- image -->

| 31    | 24 23 22 21 16 15         | 20 19 11 10 9 8 7 5 4 1 0   |
|-------|---------------------------|-----------------------------|
| 1 1 0 | 1 size 1 0 Zm 1 0 1 0 Zdn | 0 0 1 1 0 0 0 op            |

|   op | Instruction Details              | Feature   |
|------|----------------------------------|-----------|
|    0 | ADD(to vector, multiple vectors) | FEAT_SME2 |
|    1 | UNALLOCATED                      | -         |

## SME2 single-multi signed saturating doubling multiply high two registers

The encodings in this section are decoded from SME2 Multi-vector - Multiple and Single SVE Destructive (Two registers).

<!-- image -->

## SME2 single-multi int min/max four registers

The encodings in this section are decoded from SME2 Multi-vector - Multiple and Single SVE Destructive (Four registers).

<!-- image -->

|   op | Instruction Details                 | Feature   |
|------|-------------------------------------|-----------|
|    0 | SQDMULH(multiple and single vector) | FEAT_SME2 |
|    1 | UNALLOCATED                         | -         |

## SME2 Multi-vector - Multiple and Single SVE Destructive (Four registers)

SME2 Multi-vector - Multiple and Single SVE Destructive (Four registers)

The encodings in this section are decoded from SME encodings.

<!-- image -->

| 31      | 24 23 22 21 20 19   | 16 15 11 10 9 8 7 5 4 2 1   |
|---------|---------------------|-----------------------------|
| 1 1 0 0 | 1 1 0               | 1 0 1 0 1 op0 op1 op2 0     |

| op0   | op1   | op2    | Instruction details                                                       |
|-------|-------|--------|---------------------------------------------------------------------------|
| 0     | 00    | 00x    | SME2 single-multi int min/max four registers                              |
| 0     | 00    | 101    | UNALLOCATED                                                               |
| 0     | 01    | 00x    | SME2 single-multi FP min/max four registers                               |
| 0     | 01    | 100    | SME2 multiple and single vector FSCALE four registers                     |
| 0     | 01    | 101    | UNALLOCATED                                                               |
| 0     | 0x    | x1x    | UNALLOCATED                                                               |
| 0     | 10    | xxx    | SME2 single-multi shift four registers                                    |
| 0     | 11    | 000    | SME2 single-multi add four registers                                      |
| 0     | 11    | != 000 | UNALLOCATED                                                               |
| 1     | 00    | 000    | SME2 single-multi signed saturating doubling multiply high four registers |
| 1     | 00    | x10    | UNALLOCATED                                                               |
| 1     | 00    | xx1    | UNALLOCATED                                                               |
| 1     | != 00 | xxx    | UNALLOCATED                                                               |
| x     | 00    | 100    | UNALLOCATED                                                               |

## SME2 single-multi FP min/max four registers

The encodings in this section are decoded from SME2 Multi-vector - Multiple and Single SVE Destructive (Four registers).

<!-- image -->

| size   |   op |   o2 | Instruction Details                 | Feature                     |
|--------|------|------|-------------------------------------|-----------------------------|
| 00     |    0 |    0 | BFMAX(multiple and single vector)   | FEAT_SME2 &&FEAT_SVE_B16B16 |
| 00     |    0 |    1 | BFMIN (multiple and single vector)  | FEAT_SME2 &&FEAT_SVE_B16B16 |
| 00     |    1 |    0 | BFMAXNM(multiple and single vector) | FEAT_SME2 &&FEAT_SVE_B16B16 |
| 00     |    1 |    1 | BFMINNM(multiple and single vector) | FEAT_SME2 &&FEAT_SVE_B16B16 |
| != 00  |    0 |    0 | FMAX(multiple and single vector)    | FEAT_SME2                   |
| != 00  |    0 |    1 | FMIN (multiple and single vector)   | FEAT_SME2                   |
| != 00  |    1 |    0 | FMAXNM(multiple and single vector)  | FEAT_SME2                   |
| != 00  |    1 |    1 | FMINNM(multiple and single vector)  | FEAT_SME2                   |

## SME2 multiple and single vector FSCALE four registers

The encodings in this section are decoded from SME2 Multi-vector - Multiple and Single SVE Destructive (Four registers).

<!-- image -->

| size   |   op | Instruction Details                  | Feature                      |
|--------|------|--------------------------------------|------------------------------|
| xx     |    1 | UNALLOCATED                          | -                            |
| 00     |    0 | BFSCALE (multiple and single vector) | FEAT_SME2 &&FEAT_SVE_BFSCALE |
| != 00  |    0 | FSCALE (multiple and single vector)  | FEAT_SME2 &&FEAT_FP8         |

|   op |   U | Instruction Details               | Feature   |
|------|-----|-----------------------------------|-----------|
|    0 |   0 | SMAX(multiple and single vector)  | FEAT_SME2 |
|    0 |   1 | UMAX(multiple and single vector)  | FEAT_SME2 |
|    1 |   0 | SMIN (multiple and single vector) | FEAT_SME2 |
|    1 |   1 | UMIN(multiple and single vector)  | FEAT_SME2 |

## SME2 single-multi shift four registers

The encodings in this section are decoded from SME2 Multi-vector - Multiple and Single SVE Destructive (Four registers).

<!-- image -->

| 31    | 24 23 22 21 20 19 16 15 11 10 9 8 7 5 4 2 1 0   |
|-------|-------------------------------------------------|
| 1 1 0 | 1 size 1 0 Zm 1 0 1 0 1 0 1 0 opc Zdn 0 U       |

| opc    | U   | Instruction Details                | Feature   |
|--------|-----|------------------------------------|-----------|
| 001    | 0   | SRSHL (multiple and single vector) | FEAT_SME2 |
| 001    | 1   | URSHL (multiple and single vector) | FEAT_SME2 |
| != 001 | x   | UNALLOCATED                        | -         |

## SME2 single-multi add four registers

The encodings in this section are decoded from SME2 Multi-vector - Multiple and Single SVE Destructive (Four registers).

<!-- image -->

| 31    | 24 23 22 21 20 19 16 15 11 10 9 8 7 5 4 2 1 0   |
|-------|-------------------------------------------------|
| 1 1 0 | 1 size 1 0 Zm 1 0 1 0 1 0 1 1 0 0 0 Zdn 0 op    |

|   op | Instruction Details              | Feature   |
|------|----------------------------------|-----------|
|    0 | ADD(to vector, multiple vectors) | FEAT_SME2 |
|    1 | UNALLOCATED                      | -         |

## SME2 single-multi signed saturating doubling multiply high four registers

The encodings in this section are decoded from SME2 Multi-vector - Multiple and Single SVE Destructive (Four registers).

<!-- image -->

| 31   | 24 23 22 21 20 19 16 15 11 10 9 8 7 5 4 2 1   |
|------|-----------------------------------------------|
| 1 1  | 1 size 1 0 Zm 1 0 1 0 1 1 0 0 0 0 0 Zdn 0     |

## SME2 multiple vectors int min/max four registers

The encodings in this section are decoded from SME2 Multi-vector - Multiple Vectors SVE Destructive (Four registers).

<!-- image -->

| 31   | 24 23 22 21 20 18 17 10 9 7 6 5 4 2 1       |
|------|---------------------------------------------|
| 1 1  | 1 size 1 Zm 0 0 1 0 1 1 1 0 0 0 0 opc Zdn 0 |

| opc   | U   | Instruction Details     | Feature   |
|-------|-----|-------------------------|-----------|
| 00    | 0   | SMAX(multiple vectors)  | FEAT_SME2 |
| 00    | 1   | UMAX(multiple vectors)  | FEAT_SME2 |
| 01    | 0   | SMIN (multiple vectors) | FEAT_SME2 |
| 01    | 1   | UMIN(multiple vectors)  | FEAT_SME2 |
| 1x    | x   | UNALLOCATED             | -         |

|   op | Instruction Details                 | Feature   |
|------|-------------------------------------|-----------|
|    0 | SQDMULH(multiple and single vector) | FEAT_SME2 |
|    1 | UNALLOCATED                         | -         |

## SME2 Multi-vector - Multiple Vectors SVE Destructive (Four registers)

SME2 Multi-vector - Multiple Vectors SVE Destructive (Four registers)

The encodings in this section are decoded from SME encodings.

<!-- image -->

|   31 | 25 24       | 10 9      | 23   |   22 21 | 20   | 18 17 7 6 2 1   |
|------|-------------|-----------|------|---------|------|-----------------|
|    1 | 1 0 0 0 0 0 | 1 0 0 1 0 |      |       1 |      | 1 1 1 0 op0 0   |

| op0   | Instruction details                              |
|-------|--------------------------------------------------|
| 000   | SME2 multiple vectors int min/max four registers |
| 001   | UNALLOCATED                                      |
| 010   | SME2 multiple vectors FP min/max four registers  |
| 011   | SME2 multiple vectors FSCALE four registers      |
| 10x   | SME2 multiple vectors shift four registers       |
| 11x   | UNALLOCATED                                      |

## SME2 multiple vectors FP min/max four registers

The encodings in this section are decoded from SME2 Multi-vector - Multiple Vectors SVE Destructive (Four registers).

<!-- image -->

| 31   | 24 23 22 21 20 18 17 10 9 7 6 5 4 2 1 0        |
|------|------------------------------------------------|
| 1 1  | 1 size 1 Zm 0 0 1 0 1 1 1 0 0 1 0 opc Zdn 0 o2 |

| size   |   opc | o2   | Instruction Details       | Feature                     |
|--------|-------|------|---------------------------|-----------------------------|
| xx     |    10 | 0    | FAMAX                     | FEAT_SME2&&FEAT_FAMINMAX    |
| xx     |    10 | 1    | FAMIN                     | FEAT_SME2&&FEAT_FAMINMAX    |
| xx     |    11 | x    | UNALLOCATED               | -                           |
| 00     |    00 | 0    | BFMAX(multiple vectors)   | FEAT_SME2 &&FEAT_SVE_B16B16 |
| 00     |    00 | 1    | BFMIN (multiple vectors)  | FEAT_SME2 &&FEAT_SVE_B16B16 |
| 00     |    01 | 0    | BFMAXNM(multiple vectors) | FEAT_SME2 &&FEAT_SVE_B16B16 |
| 00     |    01 | 1    | BFMINNM(multiple vectors) | FEAT_SME2 &&FEAT_SVE_B16B16 |
| != 00  |    00 | 0    | FMAX(multiple vectors)    | FEAT_SME2                   |
| != 00  |    00 | 1    | FMIN (multiple vectors)   | FEAT_SME2                   |
| != 00  |    01 | 0    | FMAXNM(multiple vectors)  | FEAT_SME2                   |
| != 00  |    01 | 1    | FMINNM(multiple vectors)  | FEAT_SME2                   |

## SME2 multiple vectors FSCALE four registers

The encodings in this section are decoded from SME2 Multi-vector - Multiple Vectors SVE Destructive (Four registers).

<!-- image -->

| 31   | 24 23 22 21 20 18 17 10 9 7 6 5 4 2 1 0        |
|------|------------------------------------------------|
| 1 1  | 1 size 1 Zm 0 0 1 0 1 1 1 0 0 1 1 opc Zdn 0 o2 |

| size   | opc   | o2   | Instruction Details        | Feature                      |
|--------|-------|------|----------------------------|------------------------------|
| xx     | 00    | 1    | UNALLOCATED                | -                            |
| xx     | != 00 | x    | UNALLOCATED                | -                            |
| 00     | 00    | 0    | BFSCALE (multiple vectors) | FEAT_SME2 &&FEAT_SVE_BFSCALE |
| != 00  | 00    | 0    | FSCALE (multiple vectors)  | FEAT_SME2 &&FEAT_FP8         |

## SME2 multiple vectors shift four registers

The encodings in this section are decoded from SME2 Multi-vector - Multiple Vectors SVE Destructive (Four registers).

<!-- image -->

| 31   | 24 23 22 21 20 18 17 8 7 5 4 2 1 0          |
|------|---------------------------------------------|
| 1 1  | 1 size 1 Zm 0 0 1 0 1 1 1 0 1 0 opc Zdn 0 U |

| opc    | U   | Instruction Details      | Feature   |
|--------|-----|--------------------------|-----------|
| 001    | 0   | SRSHL (multiple vectors) | FEAT_SME2 |
| 001    | 1   | URSHL (multiple vectors) | FEAT_SME2 |
| != 001 | x   | UNALLOCATED              | -         |

## SME2 Multi-vector - Multiple Vectors SVE Saturating Multiply (Four registers)

SME2 Multi-vector - Multiple Vectors SVE Saturating Multiply (Four registers)

The encodings in this section are decoded from SME encodings.

<!-- image -->

| op0      | Instruction details                                                       |
|----------|---------------------------------------------------------------------------|
| 00000    | SME2 multi-vector signed saturating doubling multiply high four registers |
| != 00000 | UNALLOCATED                                                               |

## SME2 multi-vector signed saturating doubling multiply high four registers

The encodings in this section are decoded from SME2 Multi-vector - Multiple Vectors SVE Saturating Multiply (Four registers).

<!-- image -->

|   op | Instruction Details       | Feature   |
|------|---------------------------|-----------|
|    0 | SQDMULH(multiple vectors) | FEAT_SME2 |

## SME2 multiple vectors int min/max two registers

The encodings in this section are decoded from SME2 Multi-vector - Multiple Vectors SVE Destructive (Two registers).

<!-- image -->

| opc   | U   | Instruction Details     | Feature   |
|-------|-----|-------------------------|-----------|
| 00    | 0   | SMAX(multiple vectors)  | FEAT_SME2 |
| 00    | 1   | UMAX(multiple vectors)  | FEAT_SME2 |
| 01    | 0   | SMIN (multiple vectors) | FEAT_SME2 |
| 01    | 1   | UMIN(multiple vectors)  | FEAT_SME2 |
| 1x    | x   | UNALLOCATED             | -         |

|   op | Instruction Details   | Feature   |
|------|-----------------------|-----------|
|    1 | UNALLOCATED           | -         |

## SME2 Multi-vector - Multiple Vectors SVE Destructive (Two registers)

SME2 Multi-vector - Multiple Vectors SVE Destructive (Two registers)

The encodings in this section are decoded from SME encodings.

<!-- image -->

| op0   | Instruction details                             |
|-------|-------------------------------------------------|
| 000   | SME2 multiple vectors int min/max two registers |
| 001   | UNALLOCATED                                     |
| 010   | SME2 multiple vectors FP min/max two registers  |
| 011   | SME2 multiple vectors FSCALE two registers      |
| 10x   | SME2 multiple vectors shift two registers       |
| 11x   | UNALLOCATED                                     |

## SME2 multiple vectors FP min/max two registers

The encodings in this section are decoded from SME2 Multi-vector - Multiple Vectors SVE Destructive (Two registers).

<!-- image -->

| 31   | 24 23 22 21 20 17 16 10 9 7 6 5 4 1 0      |
|------|--------------------------------------------|
| 1 1  | 1 size 1 Zm 0 1 0 1 1 0 0 0 1 0 opc Zdn o2 |

| size   |   opc | o2   | Instruction Details       | Feature                     |
|--------|-------|------|---------------------------|-----------------------------|
| xx     |    10 | 0    | FAMAX                     | FEAT_SME2&&FEAT_FAMINMAX    |
| xx     |    10 | 1    | FAMIN                     | FEAT_SME2&&FEAT_FAMINMAX    |
| xx     |    11 | x    | UNALLOCATED               | -                           |
| 00     |    00 | 0    | BFMAX(multiple vectors)   | FEAT_SME2 &&FEAT_SVE_B16B16 |
| 00     |    00 | 1    | BFMIN (multiple vectors)  | FEAT_SME2 &&FEAT_SVE_B16B16 |
| 00     |    01 | 0    | BFMAXNM(multiple vectors) | FEAT_SME2 &&FEAT_SVE_B16B16 |
| 00     |    01 | 1    | BFMINNM(multiple vectors) | FEAT_SME2 &&FEAT_SVE_B16B16 |
| != 00  |    00 | 0    | FMAX(multiple vectors)    | FEAT_SME2                   |
| != 00  |    00 | 1    | FMIN (multiple vectors)   | FEAT_SME2                   |
| != 00  |    01 | 0    | FMAXNM(multiple vectors)  | FEAT_SME2                   |
| != 00  |    01 | 1    | FMINNM(multiple vectors)  | FEAT_SME2                   |

## SME2 multiple vectors FSCALE two registers

The encodings in this section are decoded from SME2 Multi-vector - Multiple Vectors SVE Destructive (Two registers).

<!-- image -->

| 31   | 24 23 22 21 20 17 16 10 9 7 6 5 4 1 0      |
|------|--------------------------------------------|
| 1 1  | 1 size 1 Zm 0 1 0 1 1 0 0 0 1 1 opc Zdn o2 |

| size   | opc   | o2   | Instruction Details        | Feature                      |
|--------|-------|------|----------------------------|------------------------------|
| xx     | 00    | 1    | UNALLOCATED                | -                            |
| xx     | != 00 | x    | UNALLOCATED                | -                            |
| 00     | 00    | 0    | BFSCALE (multiple vectors) | FEAT_SME2 &&FEAT_SVE_BFSCALE |
| != 00  | 00    | 0    | FSCALE (multiple vectors)  | FEAT_SME2 &&FEAT_FP8         |

## SME2 multiple vectors shift two registers

The encodings in this section are decoded from SME2 Multi-vector - Multiple Vectors SVE Destructive (Two registers).

<!-- image -->

| 31   | 24 23 22 21 20 17 16 8 7 5 4 1 0        |
|------|-----------------------------------------|
| 1 1  | 1 size 1 Zm 0 1 0 1 1 0 0 1 0 opc Zdn U |

| opc    | U   | Instruction Details      | Feature   |
|--------|-----|--------------------------|-----------|
| 001    | 0   | SRSHL (multiple vectors) | FEAT_SME2 |
| 001    | 1   | URSHL (multiple vectors) | FEAT_SME2 |
| != 001 | x   | UNALLOCATED              | -         |

## SME2 Multi-vector - Multiple Vectors SVE Saturating Multiply (Two registers)

SME2 Multi-vector - Multiple Vectors SVE Saturating Multiply (Two registers)

The encodings in this section are decoded from SME encodings.

<!-- image -->

| op0      | Instruction details                                                      |
|----------|--------------------------------------------------------------------------|
| 00000    | SME2 multi-vector signed saturating doubling multiply high two registers |
| != 00000 | UNALLOCATED                                                              |

## SME2 multi-vector signed saturating doubling multiply high two registers

The encodings in this section are decoded from SME2 Multi-vector - Multiple Vectors SVE Saturating Multiply (Two registers).

<!-- image -->

|   op | Instruction Details       | Feature   |
|------|---------------------------|-----------|
|    0 | SQDMULH(multiple vectors) | FEAT_SME2 |

## SME2 Multi-vector - SVE Select

SME2 Multi-vector - SVE Select

The encodings in this section are decoded from SME encodings.

<!-- image -->

| 31              | 24 23 22 21 20 18 17 16 15 13 12 7 6 5 4 2 1   |
|-----------------|------------------------------------------------|
| 1 1 0 0 0 0 0 1 | 1 op0 1 0 0 op1 op2                            |

| op0   | op1   | op2   | Instruction details   | Feature   |
|-------|-------|-------|-----------------------|-----------|
| 01    | 00    | 00    | SEL -Four registers   | FEAT_SME2 |
| 01    | 00    | 10    | UNALLOCATED           | -         |
| 01    | 10    | x0    | UNALLOCATED           | -         |
| 11    | x0    | x0    | UNALLOCATED           | -         |
| x0    | x0    | x0    | SEL -Tworegisters     | FEAT_SME2 |
| xx    | x0    | x1    | UNALLOCATED           | -         |
| xx    | x1    | xx    | UNALLOCATED           | -         |

## SME2 Multi-vector - SVE Constructive Binary

SME2 Multi-vector - SVE Constructive Binary

The encodings in this section are decoded from SME encodings.

<!-- image -->

| 31      | 24 23 22 21 20   | 16 15 13 12 10 9 2 1   |
|---------|------------------|------------------------|
| 1 1 0 0 | 1 op0 1 1 1 0    | op1 op2                |

| op0   |   op1 | op2   | Instruction details                                        |
|-------|-------|-------|------------------------------------------------------------|
| 00    |   101 | x     | SME2 multi-vec quadwords ZIP two registers                 |
| 01    |   101 | x     | UNALLOCATED                                                |
| 10    |   101 | x     | UNALLOCATED                                                |
| 11    |   101 | x     | SME2 multi-vec saturating shift right narrow two registers |
| xx    |   000 | x     | SME2 multi-vec FCLAMPtwo registers                         |
| xx    |   001 | x     | SME2 multi-vec CLAMPtwo registers                          |
| xx    |   010 | 0     | SME2 multi-vec FCLAMPfour registers                        |

|   op | Instruction Details   | Feature   |
|------|-----------------------|-----------|
|    1 | UNALLOCATED           | -         |

## SME2 multi-vec quadwords ZIP two registers

The encodings in this section are decoded from SME2 Multi-vector - SVE Constructive Binary.

<!-- image -->

| 31   | 24 23 22 21 20   | 16 15 13 12 10 9 5 4   |
|------|------------------|------------------------|
| 1 1  | 1 0 0 1 Zm 1 1   | 0 1 0 1 Zn Zd          |

|   op | Instruction Details   | Feature   |
|------|-----------------------|-----------|
|    0 | ZIP (two registers)   | FEAT_SME2 |
|    1 | UZP (two registers)   | FEAT_SME2 |

## SME2 multi-vec saturating shift right narrow two registers

The encodings in this section are decoded from SME2 Multi-vector - SVE Constructive Binary.

<!-- image -->

|   op |   U | Instruction Details     | Feature   |
|------|-----|-------------------------|-----------|
|    0 |   0 | SQRSHR (two registers)  | FEAT_SME2 |
|    0 |   1 | UQRSHR(two registers)   | FEAT_SME2 |
|    1 |   0 | SQRSHRU (two registers) | FEAT_SME2 |
|    1 |   1 | UNALLOCATED             | -         |

| op0   | op1   | op2   | Instruction details                                         |
|-------|-------|-------|-------------------------------------------------------------|
| xx    | 011   | 0     | SME2 multi-vec CLAMPfour registers                          |
| xx    | 01x   | 1     | UNALLOCATED                                                 |
| xx    | 100   | x     | SME2 multi-vec ZIP two registers                            |
| xx    | 11x   | x     | SME2 multi-vec saturating shift right narrow four registers |

## SME2 multi-vec FCLAMP two registers

The encodings in this section are decoded from SME2 Multi-vector - SVE Constructive Binary.

<!-- image -->

| size   |   op | Instruction Details   | Feature                     |
|--------|------|-----------------------|-----------------------------|
| xx     |    1 | UNALLOCATED           | -                           |
| 00     |    0 | BFCLAMP               | FEAT_SME2 &&FEAT_SVE_B16B16 |
| != 00  |    0 | FCLAMP                | FEAT_SME2                   |

## SME2 multi-vec CLAMP two registers

The encodings in this section are decoded from SME2 Multi-vector - SVE Constructive Binary.

<!-- image -->

|   U | Instruction Details   | Feature   |
|-----|-----------------------|-----------|
|   0 | SCLAMP                | FEAT_SME2 |
|   1 | UCLAMP                | FEAT_SME2 |

## SME2 multi-vec FCLAMP four registers

The encodings in this section are decoded from SME2 Multi-vector - SVE Constructive Binary.

<!-- image -->

| size   |   op | Instruction Details   | Feature                     |
|--------|------|-----------------------|-----------------------------|
| xx     |    1 | UNALLOCATED           | -                           |
| 00     |    0 | BFCLAMP               | FEAT_SME2 &&FEAT_SVE_B16B16 |
| != 00  |    0 | FCLAMP                | FEAT_SME2                   |

## SME2 multi-vec CLAMP four registers

The encodings in this section are decoded from SME2 Multi-vector - SVE Constructive Binary.

<!-- image -->

| 31   | 24 23 22 21 20 16 15 13 12 10 9 5 4   |
|------|---------------------------------------|
| 1 1  | 1 size 1 Zm 1 1 0 0 1 1 Zn Zd         |

|   U | Instruction Details   | Feature   |
|-----|-----------------------|-----------|
|   0 | SCLAMP                | FEAT_SME2 |
|   1 | UCLAMP                | FEAT_SME2 |

## SME2 multi-vec ZIP two registers

The encodings in this section are decoded from SME2 Multi-vector - SVE Constructive Binary.

<!-- image -->

|   op | Instruction Details   | Feature   |
|------|-----------------------|-----------|
|    0 | ZIP (two registers)   | FEAT_SME2 |
|    1 | UZP (two registers)   | FEAT_SME2 |

## SME2 multi-vec saturating shift right narrow four registers

The encodings in this section are decoded from SME2 Multi-vector - SVE Constructive Binary.

<!-- image -->

| N   |   op |   U | Instruction Details      | Feature   |
|-----|------|-----|--------------------------|-----------|
| x   |    1 |   1 | UNALLOCATED              | -         |
| 0   |    0 |   0 | SQRSHR (four registers)  | FEAT_SME2 |
| 0   |    0 |   1 | UQRSHR(four registers)   | FEAT_SME2 |
| 0   |    1 |   0 | SQRSHRU (four registers) | FEAT_SME2 |

|   N |   op |   U | Instruction Details   | Feature   |
|-----|------|-----|-----------------------|-----------|
|   1 |    0 |   0 | SQRSHRN               | FEAT_SME2 |
|   1 |    0 |   1 | UQRSHRN               | FEAT_SME2 |
|   1 |    1 |   0 | SQRSHRUN              | FEAT_SME2 |

## SME2 Multi-vector - SVE Constructive Unary

SME2 Multi-vector - SVE Constructive Unary

The encodings in this section are decoded from SME encodings.

<!-- image -->

| op0   | op1   |   op2 | op3   | op4   | Instruction details                             |
|-------|-------|-------|-------|-------|-------------------------------------------------|
| 00    | 000   |    01 | xx    | x0    | SME2 multi-vec FP to int convert two registers  |
| 00    | 000   |    10 | xx    | x0    | SME2 multi-vec int to FP two registers          |
| 00    | 100   |    01 | 0x    | 00    | SME2 multi-vec FP to int convert four registers |
| 00    | 100   |    10 | 0x    | 00    | SME2 multi-vec int to FP four registers         |
| 00    | 101   |    00 | 0x    | xx    | SME2 multi-vec FP8 down convert four registers  |
| 00    | 101   |    11 | 00    | x0    | SME2 multi-vec quadwords ZIP four registers     |
| 01    | 000   |    01 | xx    | x0    | UNALLOCATED                                     |
| 01    | 001   |    11 | xx    | xx    | UNALLOCATED                                     |
| 01    | 101   |    00 | 0x    | 1x    | UNALLOCATED                                     |
| 01    | 10x   |    00 | 0x    | 0x    | UNALLOCATED                                     |
| 0x    | 000   |    00 | xx    | xx    | SME2 multi-vec FP down convert two registers    |
| 0x    | 000   |    11 | xx    | xx    | SME2 multi-vec int down convert two registers   |
| 0x    | 001   |    00 | x0    | xx    | SME2 multi-vec FP8 down convert two registers   |
| 0x    | 001   |    00 | x1    | xx    | UNALLOCATED                                     |
| 10    | 000   |    00 | xx    | xx    | SME2 multi-vec convert two registers            |
| 10    | 001   |    00 | 1x    | xx    | UNALLOCATED                                     |
| 10    | x01   |    00 | 0x    | xx    | UNALLOCATED                                     |
| 11    | 00x   |    00 | xx    | xx    | UNALLOCATED                                     |
| 11    | 101   |    00 | 0x    | 1x    | UNALLOCATED                                     |
| 11    | 10x   |    00 | 0x    | 0x    | UNALLOCATED                                     |
| 1x    | 000   |    11 | xx    | x1    | UNALLOCATED                                     |

| op0   | op1   | op2   | op3   | op4   | Instruction details                            |
|-------|-------|-------|-------|-------|------------------------------------------------|
| 1x    | 000   | x1    | xx    | x0    | UNALLOCATED                                    |
| x0    | 100   | 00    | 0x    | 0x    | UNALLOCATED                                    |
| xx    | 000   | 01    | xx    | x1    | UNALLOCATED                                    |
| xx    | 000   | 10    | xx    | x1    | UNALLOCATED                                    |
| xx    | 001   | 01    | xx    | xx    | SME2 multi-vec unpack two registers            |
| xx    | 001   | 10    | xx    | xx    | SME2 multi-vec FP8 up convert two registers    |
| xx    | 01x   | xx    | x0    | x0    | SME2 multi-vec FRINT two registers             |
| xx    | 100   | 01    | 0x    | 01    | UNALLOCATED                                    |
| xx    | 100   | 01    | 1x    | xx    | UNALLOCATED                                    |
| xx    | 100   | 10    | 0x    | 01    | UNALLOCATED                                    |
| xx    | 100   | 11    | xx    | xx    | SME2 multi-vec int down convert four registers |
| xx    | 100   | != 11 | 0x    | 1x    | UNALLOCATED                                    |
| xx    | 101   | 01    | x0    | 0x    | SME2 multi-vec unpack four registers           |
| xx    | 101   | 01    | x0    | 1x    | UNALLOCATED                                    |
| xx    | 101   | 01    | x1    | xx    | UNALLOCATED                                    |
| xx    | 101   | 10    | 00    | x0    | SME2 multi-vec ZIP four registers              |
| xx    | 101   | 11    | 1x    | xx    | UNALLOCATED                                    |
| xx    | 101   | 1x    | 00    | x1    | UNALLOCATED                                    |
| xx    | 101   | 1x    | 01    | xx    | UNALLOCATED                                    |
| xx    | 10x   | x0    | 1x    | xx    | UNALLOCATED                                    |
| xx    | 11x   | xx    | 00    | 00    | SME2 multi-vec FRINT four registers            |
| xx    | 11x   | xx    | 00    | 10    | UNALLOCATED                                    |
| xx    | 11x   | xx    | 10    | x0    | UNALLOCATED                                    |
| xx    | x1x   | xx    | x0    | x1    | UNALLOCATED                                    |
| xx    | x1x   | xx    | x1    | xx    | UNALLOCATED                                    |
| != 00 | 000   | 10    | xx    | x0    | UNALLOCATED                                    |
| != 00 | 100   | 01    | 0x    | 00    | UNALLOCATED                                    |
| != 00 | 100   | 10    | 0x    | 00    | UNALLOCATED                                    |
| != 00 | 101   | 11    | 00    | x0    | UNALLOCATED                                    |
| != 01 | 001   | 11    | xx    | xx    | UNALLOCATED                                    |

## SME2 multi-vec FP to int convert two registers

The encodings in this section are decoded from SME2 Multi-vector - SVE Constructive Unary.

<!-- image -->

## SME2 multi-vec int to FP two registers

The encodings in this section are decoded from SME2 Multi-vector - SVE Constructive Unary.

<!-- image -->

| 31 24 23 22 21 20         | 10 9   | 6 5   | 4   |   1 0 |
|---------------------------|--------|-------|-----|-------|
| 1 1 0 0 0 0 0 1 0 0 1 0 0 | 0 Zn   | U     | Zd  |     0 |

|   U | Instruction Details   | Feature   |
|-----|-----------------------|-----------|
|   0 | SCVTF                 | FEAT_SME2 |
|   1 | UCVTF                 | FEAT_SME2 |

## SME2 multi-vec FP to int convert four registers

The encodings in this section are decoded from SME2 Multi-vector - SVE Constructive Unary.

<!-- image -->

|   31 | 24 23 22 21 20 18 17 16 15   | 10 9 7 6 5 4   |
|------|------------------------------|----------------|
|    1 | 1 0 0 1 1 0 0 0 1 1 1 1 0 0  | 0 Zn 0 U Zd    |

|   U | Instruction Details   | Feature   |
|-----|-----------------------|-----------|
|   0 | FCVTZS                | FEAT_SME2 |
|   1 | FCVTZU                | FEAT_SME2 |

## SME2 multi-vec int to FP four registers

The encodings in this section are decoded from SME2 Multi-vector - SVE Constructive Unary.

<!-- image -->

| 31   | 24 23 22 21 20 18 17 16 15       | 10 9 7 6 5 4   |
|------|----------------------------------|----------------|
| 1 1  | 1 0 0 1 1 0 0 1 0 1 1 1 0 0 0 Zn | 0 U Zd         |

|   U | Instruction Details   | Feature   |
|-----|-----------------------|-----------|
|   0 | FCVTZS                | FEAT_SME2 |
|   1 | FCVTZU                | FEAT_SME2 |

## SME2 multi-vec FP8 down convert four registers

The encodings in this section are decoded from SME2 Multi-vector - SVE Constructive Unary.

<!-- image -->

| 31   | 24 23 22 21 20 18 17 16 15           | 10 9 7 6 5 4   |
|------|--------------------------------------|----------------|
| 1 1  | 0 0 1 0 0 1 1 0 1 0 0 1 1 1 0 0 0 Zn | 0 N Zd         |

|   N | Instruction Details           | Feature              |
|-----|-------------------------------|----------------------|
|   0 | FCVT (narrowing, FP32 to FP8) | FEAT_SME2 &&FEAT_FP8 |
|   1 | FCVTN (FP32 to FP8)           | FEAT_SME2 &&FEAT_FP8 |

## SME2 multi-vec quadwords ZIP four registers

The encodings in this section are decoded from SME2 Multi-vector - SVE Constructive Unary.

<!-- image -->

|   31 | 24 23 22 21 20 18 17 16 15   | 10 9 7 6 5 4 2 1 0   |
|------|------------------------------|----------------------|
|    1 | 1 0 0 1 1 0 1 1 1 1 1 1 0    | 0 Zn 0 0 Zd op 0     |

|   op | Instruction Details   | Feature   |
|------|-----------------------|-----------|
|    0 | ZIP (four registers)  | FEAT_SME2 |
|    1 | UZP (four registers)  | FEAT_SME2 |

## SME2 multi-vec FP down convert two registers

The encodings in this section are decoded from SME2 Multi-vector - SVE Constructive Unary.

<!-- image -->

|   U | Instruction Details   | Feature   |
|-----|-----------------------|-----------|
|   0 | SCVTF                 | FEAT_SME2 |
|   1 | UCVTF                 | FEAT_SME2 |

|   op |   N | Instruction Details                  | Feature   |
|------|-----|--------------------------------------|-----------|
|    0 |   0 | FCVT (narrowing, FP32 to FP16)       | FEAT_SME2 |
|    0 |   1 | FCVTN (FP32 to FP16)                 | FEAT_SME2 |
|    1 |   0 | BFCVT (single-precision to BFloat16) | FEAT_SME2 |
|    1 |   1 | BFCVTN                               | FEAT_SME2 |

## SME2 multi-vec int down convert two registers

The encodings in this section are decoded from SME2 Multi-vector - SVE Constructive Unary.

<!-- image -->

| 31    | 23 22 21 20 18 17 16 15 10 9 6 5   |
|-------|------------------------------------|
| 1 1 0 | 0 op 1 0 0 0 1 1 1 1 1 0 0 0 Zn U  |

|   op |   U | Instruction Details   | Feature   |
|------|-----|-----------------------|-----------|
|    0 |   0 | SQCVT (two registers) | FEAT_SME2 |
|    0 |   1 | UQCVT(two registers)  | FEAT_SME2 |
|    1 |   0 | SQCVTU(two registers) | FEAT_SME2 |
|    1 |   1 | UNALLOCATED           | -         |

## SME2 multi-vec FP8 down convert two registers

The encodings in this section are decoded from SME2 Multi-vector - SVE Constructive Unary.

<!-- image -->

|   op | Instruction Details                      | Feature              |
|------|------------------------------------------|----------------------|
|    0 | FCVT (narrowing, FP16 to FP8)            | FEAT_SME2 &&FEAT_FP8 |
|    1 | BFCVT (BFloat16 to 8-bit floating-point) | FEAT_SME2 &&FEAT_FP8 |

## SME2 multi-vec convert two registers

The encodings in this section are decoded from SME2 Multi-vector - SVE Constructive Unary.

<!-- image -->

| 31   | 24 23 22 21 20 18 17 16 15    | 10 9   | 5 4 1 0   |
|------|-------------------------------|--------|-----------|
| 1 1  | 1 1 0 1 0 0 0 0 0 1 1 1 0 0 0 | Zn Zd  | L         |

|   L | Instruction Details   | Feature         |
|-----|-----------------------|-----------------|
|   0 | FCVT (widening)       | FEAT_SME_F16F16 |
|   1 | FCVTL                 | FEAT_SME_F16F16 |

## SME2 multi-vec unpack two registers

The encodings in this section are decoded from SME2 Multi-vector - SVE Constructive Unary.

<!-- image -->

|   U | Instruction Details   | Feature   |
|-----|-----------------------|-----------|
|   0 | SUNPK                 | FEAT_SME2 |
|   1 | UUNPK                 | FEAT_SME2 |

## SME2 multi-vec FP8 up convert two registers

The encodings in this section are decoded from SME2 Multi-vector - SVE Constructive Unary.

<!-- image -->

|   opc |   L | Instruction Details     | Feature              |
|-------|-----|-------------------------|----------------------|
|    00 |   0 | F1CVT,F2CVT-F1CVT       | FEAT_SME2 &&FEAT_FP8 |
|    00 |   1 | F1CVTL,F2CVTL-F1CVTL    | FEAT_SME2 &&FEAT_FP8 |
|    01 |   0 | BF1CVT,BF2CVT-BF1CVT    | FEAT_SME2 &&FEAT_FP8 |
|    01 |   1 | BF1CVTL,BF2CVTL-BF1CVTL | FEAT_SME2 &&FEAT_FP8 |

|   opc |   L | Instruction Details     | Feature              |
|-------|-----|-------------------------|----------------------|
|    10 |   0 | F1CVT,F2CVT-F2CVT       | FEAT_SME2 &&FEAT_FP8 |
|    10 |   1 | F1CVTL,F2CVTL-F2CVTL    | FEAT_SME2 &&FEAT_FP8 |
|    11 |   0 | BF1CVT,BF2CVT-BF2CVT    | FEAT_SME2 &&FEAT_FP8 |
|    11 |   1 | BF1CVTL,BF2CVTL-BF2CVTL | FEAT_SME2 &&FEAT_FP8 |

## SME2 multi-vec FRINT two registers

The encodings in this section are decoded from SME2 Multi-vector - SVE Constructive Unary.

<!-- image -->

| size   | opc   | Instruction Details   | Feature   |
|--------|-------|-----------------------|-----------|
| 10     | 000   | FRINTN                | FEAT_SME2 |
| 10     | 001   | FRINTP                | FEAT_SME2 |
| 10     | 010   | FRINTM                | FEAT_SME2 |
| 10     | 011   | UNALLOCATED           | -         |
| 10     | 100   | FRINTA                | FEAT_SME2 |
| 10     | 101   | UNALLOCATED           | -         |
| 10     | 11x   | UNALLOCATED           | -         |
| != 10  | xxx   | UNALLOCATED           | -         |

## SME2 multi-vec int down convert four registers

The encodings in this section are decoded from SME2 Multi-vector - SVE Constructive Unary.

<!-- image -->

|   op |   N |   U | Instruction Details    | Feature   |
|------|-----|-----|------------------------|-----------|
|    0 |   0 |   0 | SQCVT (four registers) | FEAT_SME2 |
|    0 |   0 |   1 | UQCVT(four registers)  | FEAT_SME2 |
|    0 |   1 |   0 | SQCVTN                 | FEAT_SME2 |
|    0 |   1 |   1 | UQCVTN                 | FEAT_SME2 |

## SME2 multi-vec unpack four registers

The encodings in this section are decoded from SME2 Multi-vector - SVE Constructive Unary.

<!-- image -->

| 31   | 24 23 22 21 20 18 17 16 15        | 10 9 6 5 4 2 1   |
|------|-----------------------------------|------------------|
| 1 1  | 1 size 1 1 0 1 0 1 1 1 1 0 0 0 Zn | 0 Zd 0           |

|   U | Instruction Details   | Feature   |
|-----|-----------------------|-----------|
|   0 | SUNPK                 | FEAT_SME2 |
|   1 | UUNPK                 | FEAT_SME2 |

## SME2 multi-vec ZIP four registers

The encodings in this section are decoded from SME2 Multi-vector - SVE Constructive Unary.

<!-- image -->

| 31   | 24 23 22 21 20 18 17 16 15        | 10 9 7 6 5 4 2 1   |
|------|-----------------------------------|--------------------|
| 1 1  | 1 size 1 1 0 1 1 0 1 1 1 0 0 0 Zn | 0 0 Zd op          |

|   op | Instruction Details   | Feature   |
|------|-----------------------|-----------|
|    0 | ZIP (four registers)  | FEAT_SME2 |
|    1 | UZP (four registers)  | FEAT_SME2 |

## SME2 multi-vec FRINT four registers

The encodings in this section are decoded from SME2 Multi-vector - SVE Constructive Unary.

<!-- image -->

|   op | N   |   U | Instruction Details    | Feature   |
|------|-----|-----|------------------------|-----------|
|    1 | x   |   1 | UNALLOCATED            | -         |
|    1 | 0   |   0 | SQCVTU(four registers) | FEAT_SME2 |
|    1 | 1   |   0 | SQCVTUN                | FEAT_SME2 |

## SME2 Multi-vector - FP Multiply

SME2 Multi-vector - FP Multiply

The encodings in this section are decoded from SME encodings.

<!-- image -->

| 31          | 24 23 22 21 20 18 17 16 15 10 9 7 6 5 4 2 1 0   |
|-------------|-------------------------------------------------|
| 1 1 0 0 0 0 | 1 1 op0 1 1 1 0 0 1 op1 0 op2 0                 |

| op0   | op1   | op2   | Instruction details                         |
|-------|-------|-------|---------------------------------------------|
| 01    | 0     | 0     | SME2 multi-vec FP multiply (four registers) |
| 01    | 0     | 1     | UNALLOCATED                                 |
| 01    | 1     | x     | UNALLOCATED                                 |
| 11    | x     | x     | UNALLOCATED                                 |
| x0    | x     | x     | SME2 multi-vec FP multiply (two registers)  |

| size   | opc   | Instruction Details   | Feature   |
|--------|-------|-----------------------|-----------|
| 10     | 000   | FRINTN                | FEAT_SME2 |
| 10     | 001   | FRINTP                | FEAT_SME2 |
| 10     | 010   | FRINTM                | FEAT_SME2 |
| 10     | 011   | UNALLOCATED           | -         |
| 10     | 100   | FRINTA                | FEAT_SME2 |
| 10     | 101   | UNALLOCATED           | -         |
| 10     | 11x   | UNALLOCATED           | -         |
| != 10  | xxx   | UNALLOCATED           | -         |

## SME2 multi-vec FP multiply (four registers)

The encodings in this section are decoded from SME2 Multi-vector - FP Multiply.

<!-- image -->

| size   | Instruction Details     | Feature                      |
|--------|-------------------------|------------------------------|
| 00     | BFMUL(multiple vectors) | FEAT_SME2 &&FEAT_SVE_BFSCALE |
| != 00  | FMUL(multiple vectors)  | FEAT_SME2p2                  |

## SME2 multi-vec FP multiply (two registers)

The encodings in this section are decoded from SME2 Multi-vector - FP Multiply.

<!-- image -->

| 31   | 24 23 22 21 20 17 16 10 9 6 5 4 1 0   |
|------|---------------------------------------|
| 1 1  | 1 size 1 Zm 0 1 1 1 0 0 1 Zn 0 Zd 0   |

| size   | Instruction Details     | Feature                      |
|--------|-------------------------|------------------------------|
| 00     | BFMUL(multiple vectors) | FEAT_SME2 &&FEAT_SVE_BFSCALE |
| != 00  | FMUL(multiple vectors)  | FEAT_SME2p2                  |

## SME2 Multiple and Single Vector - FP multiply

SME2 Multiple and Single Vector - FP multiply

The encodings in this section are decoded from SME encodings.

<!-- image -->

| 31          | 24 23 22 21 20 17 16 15 10 9 7 6 5 4 2 1 0   |
|-------------|----------------------------------------------|
| 1 1 0 0 0 0 | 1 1 op0 1 1 1 0 1 0 op1 0 op2 0              |

|   op0 | op1   | op2   | Instruction details                                          |
|-------|-------|-------|--------------------------------------------------------------|
|     0 | x     | x     | SME2 multiple and single vector FP multiply (two registers)  |
|     1 | 0     | 0     | SME2 multiple and single vector FP multiply (four registers) |
|     1 | 0     | 1     | UNALLOCATED                                                  |
|     1 | 1     | x     | UNALLOCATED                                                  |

## SME2 multiple and single vector FP multiply (two registers)

The encodings in this section are decoded from SME2 Multiple and Single Vector - FP multiply.

<!-- image -->

|   31 | 17 16 15 10 9 6 5 4   |
|------|-----------------------|
|    1 | 0 1 1 1 0 1 0 Zn 0 Zd |

## SME Memory

SMEMemory

The encodings in this section are decoded from SME encodings.

<!-- image -->

| 31        | 25 24   | 21 20   | 16 15 14   | 10   | 5   | 2   | 1 0   |
|-----------|---------|---------|------------|------|-----|-----|-------|
| 1 1 1 0 0 | 0 op0   | op1     | op2        | op3  | op4 |     |       |

| op0   | op1      | op2   | op3   | op4   | Instruction details              | Feature   |
|-------|----------|-------|-------|-------|----------------------------------|-----------|
| 0xx0  | xxxxx    | x     | xxxxx | 0xx   | SMEload array vector (elements)  | -         |
| 0xx1  | xxxxx    | x     | xxxxx | 0xx   | SMEstore array vector (elements) | -         |
| 100x  | 00000    | 0     | xx000 | 0xx   | SMEsave and restore array        | -         |
| 100x  | xxxxx    | 1     | 00000 | 000   | SME2 lookup table load/store     | -         |
| 100x  | xxxxx    | 1     | 00000 | 001   | UNALLOCATED                      | -         |
| 100x  | xxxxx    | 1     | 00000 | 01x   | UNALLOCATED                      | -         |
| 100x  | xxxxx    | 1     | 01000 | 0xx   | UNALLOCATED                      | -         |
| 100x  | xxxxx    | 1     | 1x000 | 0xx   | UNALLOCATED                      | -         |
| 100x  | xxxxx    | x     | xx001 | 0xx   | UNALLOCATED                      | -         |
| 100x  | xxxxx    | x     | xx01x | 0xx   | UNALLOCATED                      | -         |
| 100x  | xxxxx    | x     | xx1xx | 0xx   | UNALLOCATED                      | -         |
| 100x  | != 00000 | 0     | xx000 | 0xx   | UNALLOCATED                      | -         |

| size   | Instruction Details               | Feature                      |
|--------|-----------------------------------|------------------------------|
| 00     | BFMUL(multiple and single vector) | FEAT_SME2 &&FEAT_SVE_BFSCALE |
| != 00  | FMUL(multiple and single vector)  | FEAT_SME2p2                  |

## SME2 multiple and single vector FP multiply (four registers)

The encodings in this section are decoded from SME2 Multiple and Single Vector - FP multiply.

<!-- image -->

| 31   | 20 17 16 15 10 9 7 6 5   |
|------|--------------------------|
| 1 1  | Zm 1 1 1 1 0 1 0 Zn 0 0  |

| size   | Instruction Details               | Feature                      |
|--------|-----------------------------------|------------------------------|
| 00     | BFMUL(multiple and single vector) | FEAT_SME2 &&FEAT_SVE_BFSCALE |
| != 00  | FMUL(multiple and single vector)  | FEAT_SME2p2                  |

| op0   | op1   | op2   | op3   | op4   | Instruction details   | Feature   |
|-------|-------|-------|-------|-------|-----------------------|-----------|
| 101x  | xxxxx | x     | xxxxx | 0xx   | UNALLOCATED           | -         |
| 110x  | xxxxx | x     | xxxxx | 0xx   | UNALLOCATED           | -         |
| 1110  | xxxxx | x     | xxxxx | 0xx   | LD1Q                  | FEAT_SME  |
| 1111  | xxxxx | x     | xxxxx | 0xx   | ST1Q                  | FEAT_SME  |
| xxxx  | xxxxx | x     | xxxxx | 1xx   | UNALLOCATED           | -         |

## SME load array vector (elements)

The encodings in this section are decoded from SME Memory.

<!-- image -->

| 31    | 24 23 22 21 20   | 16 15 14 13   | 12 10 9 5 4 3   |
|-------|------------------|---------------|-----------------|
| 1 1 1 | 0 msz 0          | V Rs Pg       | Rn 0 opc        |

|   msz | Instruction Details                   | Feature   |
|-------|---------------------------------------|-----------|
|    00 | LD1B (scalar plus scalar, tile slice) | FEAT_SME  |
|    01 | LD1H (scalar plus scalar, tile slice) | FEAT_SME  |
|    10 | LD1W(scalar plus scalar, tile slice)  | FEAT_SME  |
|    11 | LD1D (scalar plus scalar, tile slice) | FEAT_SME  |

## SME store array vector (elements)

The encodings in this section are decoded from SME Memory.

<!-- image -->

| 31          | 24 23 22 21 20   |    |   4 | 16 15 14 13 12 10 9 5 3   |
|-------------|------------------|----|-----|---------------------------|
| 1 1 1 0 0 0 | 0 msz            |  1 |   0 | V Rs Pg Rn opc            |

|   msz | Instruction Details                   | Feature   |
|-------|---------------------------------------|-----------|
|    00 | ST1B (scalar plus scalar, tile slice) | FEAT_SME  |
|    01 | ST1H (scalar plus scalar, tile slice) | FEAT_SME  |
|    10 | ST1W (scalar plus scalar, tile slice) | FEAT_SME  |
|    11 | ST1D (scalar plus scalar, tile slice) | FEAT_SME  |

## SVE encodings

## SME save and restore array

The encodings in this section are decoded from SME Memory.

<!-- image -->

| 31   | 21 20                   | 16 15 14 13 12 10 9 5 4 3   |
|------|-------------------------|-----------------------------|
| 1 1  | op 0 0 0 0 0 0 Rv 0 0 0 | Rn 0 imm4                   |

|   op | Instruction Details   | Feature   |
|------|-----------------------|-----------|
|    0 | LDR(array vector)     | FEAT_SME  |
|    1 | STR (array vector)    | FEAT_SME  |

## SME2 lookup table load/store

The encodings in this section are decoded from SME Memory.

<!-- image -->

| opc    | opc2   | Instruction Details   | Feature   |
|--------|--------|-----------------------|-----------|
| x0xxxx | xx     | UNALLOCATED           | -         |
| x10xxx | xx     | UNALLOCATED           | -         |
| x110xx | xx     | UNALLOCATED           | -         |
| x1110x | xx     | UNALLOCATED           | -         |
| x11110 | xx     | UNALLOCATED           | -         |
| x11111 | != 00  | UNALLOCATED           | -         |
| 011111 | 00     | LDR(table)            | FEAT_SME2 |
| 111111 | 00     | STR (table)           | FEAT_SME2 |

## SVE encodings

The encodings in this section are decoded from A64 instruction set encoding.

<!-- image -->

|   op0 | op1      | op2    | op3   | Instruction details                                | Feature   |
|-------|----------|--------|-------|----------------------------------------------------|-----------|
|   000 | 0xx0xxxx | 000xxx | x     | SVE Integer Binary Arithmetic - Predicated         | -         |
|   000 | 0xx0xxxx | 001xxx | x     | SVE Integer Reduction                              | -         |
|   000 | 0xx0xxxx | 100xxx | x     | SVE Bitwise Shift - Predicated                     | -         |
|   000 | 0xx0xxxx | 101xxx | x     | SVEInteger Unary Arithmetic - Predicated           | -         |
|   000 | 0xx0xxxx | x1xxxx | x     | SVE Integer Multiply-Add - Predicated              | -         |
|   000 | 0xx1xxxx | 001xxx | x     | SVE Bitwise Logical - Unpredicated                 | -         |
|   000 | 0xx1xxxx | 0100xx | x     | SVE Index Generation                               | -         |
|   000 | 0xx1xxxx | 0101xx | x     | SVE Stack Allocation                               | -         |
|   000 | 0xx1xxxx | 011xxx | x     | SVE2 Integer Arithmetic - Unpredicated             | -         |
|   000 | 0xx1xxxx | 100xxx | x     | SVE Bitwise Shift - Unpredicated                   | -         |
|   000 | 0xx1xxxx | 1011xx | x     | SVE Integer Misc - Unpredicated                    | -         |
|   000 | 0xx1xxxx | 11xxxx | x     | SVE Element Count                                  | -         |
|   000 | 10x1xxxx | 000xxx | x     | SVE Permute Vector - Extract                       | -         |
|   000 | 11x1xxxx | 000xxx | x     | SVE Permute Vector - Segments                      | -         |
|   000 | 1xx00xxx | xxxxxx | x     | SVE Bitwise Immediate                              | -         |
|   000 | 1xx01xxx | xxxxxx | x     | SVE Integer Wide Immediate - Predicated            | -         |
|   000 | 1xx1xxxx | 001001 | x     | SVE Permute Vector - One Source Quadwords          | -         |
|   000 | 1xx1xxxx | 001110 | x     | SVE Permute Vector - Unpredicated                  | -         |
|   000 | 1xx1xxxx | 001111 | x     | UNALLOCATED                                        | -         |
|   000 | 1xx1xxxx | 010xxx | x     | SVE Permute Predicate                              | -         |
|   000 | 1xx1xxxx | 10xxxx | x     | SVE Permute Vector - Predicated                    | -         |
|   001 | 0xx0xxxx | xxxxxx | x     | SVE Integer Compare - Vectors                      | -         |
|   001 | 1xx00xxx | 11xxxx | x     | SVE Propagate Break                                | -         |
|   001 | 1xx01xxx | 01xxxx | x     | SVE Partition Break                                | -         |
|   001 | 1xx01xxx | 11xxxx | x     | SVE Predicate Misc                                 | -         |
|   001 | 1xx100xx | 10xxxx | x     | SVE Predicate Count                                | -         |
|   001 | 1xx101xx | 1000xx | x     | SVE Inc/Dec by Predicate Count                     | -         |
|   001 | 1xx101xx | 1001xx | x     | SVE Write FFR                                      | -         |
|   001 | 1xx101xx | 101xxx | x     | UNALLOCATED                                        | -         |
|   001 | 1xx11xxx | 10xxxx | x     | UNALLOCATED                                        | -         |
|   001 | 1xx1xxxx | 00xxxx | x     | SVE Integer Compare - Scalars                      | -         |
|   001 | 1xx1xxxx | 01xxxx | 1     | SVE Scalar Integer Compare - Predicate- as-counter | -         |
|   001 | 1xx1xxxx | 11xxxx | x     | SVE Integer Wide Immediate - Unpredicated          | -         |
|   010 | 0x10xxxx | 11001x | x     | UNALLOCATED                                        | -         |
|   010 | 0xx0xxxx | 0xxxxx | x     | SVE Integer Multiply-Add - Unpredicated            | -         |

|   op0 | op1      | op2    | op3   | Instruction details                                       | Feature   |
|-------|----------|--------|-------|-----------------------------------------------------------|-----------|
|   010 | 0xx0xxxx | 10xxxx | x     | SVE2 Integer - Predicated                                 | -         |
|   010 | 0xx0xxxx | 1101x1 | x     | UNALLOCATED                                               | -         |
|   010 | 0xx1xxxx | xxxxxx | x     | SVE Multiply - Indexed                                    | -         |
|   010 | 1xx0xxxx | 0xxxxx | x     | SVE2 Widening Integer Arithmetic                          | -         |
|   010 | 1xx0xxxx | 10xxxx | x     | SVE Misc                                                  | -         |
|   010 | 1xx0xxxx | 11xxxx | x     | SVE2 Accumulate                                           | -         |
|   010 | 1xx1xxxx | 0xxxxx | x     | SVE2 Narrowing                                            | -         |
|   010 | 1xx1xxxx | 101xxx | x     | SVE2 Histogram Computation (Segment) and Lookup Table     | -         |
|   010 | 1xx1xxxx | 111xxx | x     | SVE2 Crypto Extensions                                    | -         |
|   011 | 01x1xxxx | 111000 | x     | UNALLOCATED                                               | -         |
|   011 | 0x01xxxx | 0111xx | x     | UNALLOCATED                                               | -         |
|   011 | 0x01xxxx | 10xx10 | x     | SVE2 FP8 widening multiply-add                            | -         |
|   011 | 0x01xxxx | 10xx11 | x     | UNALLOCATED                                               | -         |
|   011 | 0x01xxxx | 11x1xx | x     | UNALLOCATED                                               | -         |
|   011 | 0x11xxxx | 10xx1x | x     | UNALLOCATED                                               | -         |
|   011 | 0x11xxxx | x1x1xx | x     | UNALLOCATED                                               | -         |
|   011 | 0xx00001 | 100xxx | x     | UNALLOCATED                                               | -         |
|   011 | 0xx0010x | 100xxx | x     | UNALLOCATED                                               | -         |
|   011 | 0xx00x0x | 11xxxx | x     | UNALLOCATED                                               | -         |
|   011 | 0xx00x1x | 1xxxxx | x     | UNALLOCATED                                               | -         |
|   011 | 0xx010xx | 11xxxx | x     | UNALLOCATED                                               | -         |
|   011 | 0xx011xx | 1xxxxx | x     | SVE2 floating-point unary operations - zeroing predicated | -         |
|   011 | 0xx1xxxx | 001011 | x     | UNALLOCATED                                               | -         |
|   011 | 0xx1xxxx | 0011xx | x     | UNALLOCATED                                               | -         |
|   011 | 0xx1xxxx | 01x0xx | x     | SVE floating-point widening multiply-add - indexed        | -         |
|   011 | 0xx1xxxx | 10x00x | x     | SVEfloating-point widening multiply-add                   | -         |
|   011 | 0xx1xxxx | 10x10x | x     | UNALLOCATED                                               | -         |
|   011 | 0xx1xxxx | 11101x | x     | UNALLOCATED                                               | -         |
|   011 | 1xx001xx | 0010xx | x     | UNALLOCATED                                               | -         |
|   011 | 1xx001xx | 0011xx | x     | SVE floating-point unary operations - unpredicated        | -         |
|   011 | 1xx010xx | 001xxx | x     | SVE floating-point compare - with zero                    | -         |
|   011 | 1xx011xx | 001xxx | x     | SVEfloating-point accumulating reduction                  | -         |
|   011 | 1xx0xxxx | 100xxx | x     | SVE floating-point arithmetic - predicated                | -         |
|   011 | 1xx0xxxx | 101xxx | x     | SVE floating-point unary operations - merging predicated  | -         |
|   011 | 1xx1xxxx | xxxxxx | x     | SVE floating-point multiply-add                           | -         |
|   100 | xxxxxxxx | xxxxxx | x     | SVE Memory - 32-bit Gather and Unsized Contiguous         | -         |

|   op0 | op1      | op2    | op3   | Instruction details                                            | Feature                              |
|-------|----------|--------|-------|----------------------------------------------------------------|--------------------------------------|
|   101 | xxxxxxxx | xxxxxx | x     | SVE Memory - Contiguous Load                                   | -                                    |
|   110 | xxxxxxxx | xxxxxx | x     | SVE Memory - 64-bit Gather                                     | -                                    |
|   111 | xxxxxxxx | 001xxx | x     | SVE Memory - Non-temporal and Quadword Scatter Store           | -                                    |
|   111 | xxxxxxxx | 011xxx | x     | SVE Memory - Non-temporal and Multi- register Contiguous Store | -                                    |
|   111 | xxxxxxxx | 0x0xxx | x     | SVE Memory - Contiguous Store and Unsized Contiguous           | -                                    |
|   111 | xxxxxxxx | 101xxx | x     | SVE Memory - Scatter                                           | -                                    |
|   111 | xxxxxxxx | 111xxx | x     | SVE Memory - Contiguous Store with Immediate Offset            | -                                    |
|   111 | xxxxxxxx | 1x0xxx | x     | SVE Memory - Scatter with Optional Sign Extend                 | -                                    |
|   000 | 0xx1xxxx | 000xxx | x     | SVE integer add/subtract vectors (unpredicated)                | -                                    |
|   000 | 0xx1xxxx | 1010xx | x     | SVE address generation                                         | -                                    |
|   000 | 1xx1xxxx | 001000 | x     | DUP(indexed)                                                   | FEAT_SVE &#124;&#124; FEAT_SME       |
|   000 | 1xx1xxxx | 00101x | x     | SVE table lookup (three sources)                               | -                                    |
|   000 | 1xx1xxxx | 001100 | x     | TBL -Single register table                                     | FEAT_SVE &#124;&#124; FEAT_SME       |
|   000 | 1xx1xxxx | 001101 | x     | TBXQ                                                           | FEAT_SVE2p1 &#124;&#124; FEAT_SME2p1 |
|   000 | 1xx1xxxx | 011xxx | x     | SVE permute vector elements                                    | -                                    |
|   000 | 1xx1xxxx | 11xxxx | x     | SEL (vectors)                                                  | FEAT_SVE &#124;&#124; FEAT_SME       |
|   001 | 0xx1xxxx | xxxxxx | x     | SVE integer compare with unsigned immediate                    | -                                    |
|   001 | 1xx00xxx | 01xxxx | x     | SVE predicate logical operations                               | -                                    |
|   001 | 1xx0xxxx | x0xxxx | x     | SVE integer compare with signed immediate                      | -                                    |
|   001 | 1xx1xxxx | 01xxxx | 0     | SVE broadcast predicate element                                | -                                    |
|   010 | 0000xxxx | 11001x | x     | SVE two-way dot product                                        | -                                    |
|   010 | 0100xxxx | 11001x | x     | SVE two-way dot product (indexed)                              | -                                    |
|   010 | 0xx0xxxx | 11000x | x     | SVE integer clamp                                              | -                                    |
|   010 | 0xx0xxxx | 1101x0 | x     | SVE2 multiply-add (checked pointer)                            | -                                    |
|   010 | 0xx0xxxx | 111xxx | x     | SVEpermute vector elements (quadwords)                         | -                                    |
|   010 | 1xx1xxxx | 100xxx | x     | SVE2 character match                                           | -                                    |
|   010 | 1xx1xxxx | 110xxx | x     | HISTCNT                                                        | FEAT_SVE2                            |
|   011 | 00x1xxxx | 111000 | x     | SVE2 FP8 matrix multiply-accumulate                            | -                                    |
|   011 | 0x01xxxx | 0101xx | x     | SVE2 FP8 multiply-add long (indexed)                           | -                                    |
|   011 | 0xx00000 | 100xxx | x     | FCADD                                                          | FEAT_SVE &#124;&#124; FEAT_SME       |
|   011 | 0xx0000x | 101xxx | x     | SVE floating-point convert (top, predicated)                   | -                                    |
|   011 | 0xx0010x | 101xxx | x     | SVE floating-point convert precision odd elements              | -                                    |
|   011 | 0xx010xx | 100xxx | x     | SVE2 floating-point pairwise operations                        | -                                    |

|   op0 | op1      | op2    | op3   | Instruction details                                | Feature                        |
|-------|----------|--------|-------|----------------------------------------------------|--------------------------------|
|   011 | 0xx010xx | 101xxx | x     | SVE floating-point recursive reduction (quadwords) | -                              |
|   011 | 0xx0xxxx | 0xxxxx | x     | FCMLA(vectors)                                     | FEAT_SVE &#124;&#124; FEAT_SME |
|   011 | 0xx1xxxx | 0000xx | x     | SVE floating-point multiply-add (indexed)          | -                              |
|   011 | 0xx1xxxx | 0001xx | x     | SVE floating-point complex multiply-add (indexed)  | -                              |
|   011 | 0xx1xxxx | 001001 | x     | SVE FP clamp                                       | -                              |
|   011 | 0xx1xxxx | 0010x0 | x     | SVE floating-point multiply (indexed)              | -                              |
|   011 | 0xx1xxxx | 1100xx | x     | SVE2 FP8 multiply-add long long (indexed)          | -                              |
|   011 | 0xx1xxxx | 111001 | x     | SVE floating-point matrix multiply accumulate      | -                              |
|   011 | 1xx000xx | 001xxx | x     | SVE floating-point recursive reduction             | -                              |
|   011 | 1xx0xxxx | 000xxx | x     | SVE floating-point arithmetic (unpredicated)       | -                              |
|   011 | 1xx0xxxx | x1xxxx | x     | SVE floating-point compare vectors                 | -                              |

## SVE Integer Binary Arithmetic - Predicated

SVE Integer Binary Arithmetic - Predicated

The encodings in this section are decoded from SVE encodings.

<!-- image -->

| 31          | 24 23 22 21 20 18 17 16 15 13   |
|-------------|---------------------------------|
| 0 0 0 0 0 1 | 0 0 op0 0 0 0                   |

| op0   | Instruction details                           |
|-------|-----------------------------------------------|
| 00x   | SVE integer add/subtract vectors (predicated) |
| 01x   | SVE integer min/max/difference (predicated)   |
| 100   | SVE integer multiply vectors (predicated)     |
| 101   | SVE integer divide vectors (predicated)       |
| 11x   | SVE bitwise logical operations (predicated)   |

## SVE integer add/subtract vectors (predicated)

The encodings in this section are decoded from SVE Integer Binary Arithmetic - Predicated.

<!-- image -->

| size   | opc   | Instruction Details       | Feature                        |
|--------|-------|---------------------------|--------------------------------|
| xx     | 000   | ADD(vectors, predicated)  | FEAT_SVE &#124;&#124; FEAT_SME |
| xx     | 001   | SUB (vectors, predicated) | FEAT_SVE &#124;&#124; FEAT_SME |
| xx     | 010   | UNALLOCATED               | -                              |
| xx     | 011   | SUBR (vectors)            | FEAT_SVE &#124;&#124; FEAT_SME |
| 11     | 100   | ADDPT(predicated)         | FEAT_SVE &&FEAT_CPA            |
| 11     | 101   | SUBPT (predicated)        | FEAT_SVE &&FEAT_CPA            |
| 11     | 11x   | UNALLOCATED               | -                              |
| != 11  | 1xx   | UNALLOCATED               | -                              |

## SVE integer min/max/difference (predicated)

The encodings in this section are decoded from SVE Integer Binary Arithmetic - Predicated.

<!-- image -->

|   opc | U   | Instruction Details   | Feature                        |
|-------|-----|-----------------------|--------------------------------|
|    00 | 0   | SMAX(vectors)         | FEAT_SVE &#124;&#124; FEAT_SME |
|    00 | 1   | UMAX(vectors)         | FEAT_SVE &#124;&#124; FEAT_SME |
|    01 | 0   | SMIN (vectors)        | FEAT_SVE &#124;&#124; FEAT_SME |
|    01 | 1   | UMIN(vectors)         | FEAT_SVE &#124;&#124; FEAT_SME |
|    10 | 0   | SABD                  | FEAT_SVE &#124;&#124; FEAT_SME |
|    10 | 1   | UABD                  | FEAT_SVE &#124;&#124; FEAT_SME |
|    11 | x   | UNALLOCATED           | -                              |

## SVE integer multiply vectors (predicated)

The encodings in this section are decoded from SVE Integer Binary Arithmetic - Predicated.

<!-- image -->

|   H | U                          | Instruction Details   | Feature                        |
|-----|----------------------------|-----------------------|--------------------------------|
|   0 | 0 MUL(vectors, predicated) | FEAT_SVE              | &#124;&#124; FEAT_SME          |
|   0 | 1                          | UNALLOCATED           | -                              |
|   1 | 0                          | SMULH(predicated)     | FEAT_SVE &#124;&#124; FEAT_SME |
|   1 | 1                          | UMULH(predicated)     | FEAT_SVE &#124;&#124; FEAT_SME |

## SVE integer divide vectors (predicated)

The encodings in this section are decoded from SVE Integer Binary Arithmetic - Predicated.

<!-- image -->

|   R | U       | Instruction Details   | Feature               |
|-----|---------|-----------------------|-----------------------|
|   0 | 0 SDIV  | FEAT_SVE              | &#124;&#124; FEAT_SME |
|   0 | 1 UDIV  | FEAT_SVE              | &#124;&#124; FEAT_SME |
|   1 | 0 SDIVR | FEAT_SVE              | &#124;&#124; FEAT_SME |
|   1 | 1 UDIVR | FEAT_SVE              | &#124;&#124; FEAT_SME |

## SVE bitwise logical operations (predicated)

The encodings in this section are decoded from SVE Integer Binary Arithmetic - Predicated.

<!-- image -->

| opc   | Instruction Details       | Feature                        |
|-------|---------------------------|--------------------------------|
| 000   | ORR(vectors, predicated)  | FEAT_SVE &#124;&#124; FEAT_SME |
| 001   | EOR(vectors, predicated)  | FEAT_SVE &#124;&#124; FEAT_SME |
| 010   | AND(vectors, predicated)  | FEAT_SVE &#124;&#124; FEAT_SME |
| 011   | BIC (vectors, predicated) | FEAT_SVE &#124;&#124; FEAT_SME |
| 1xx   | UNALLOCATED               | -                              |

## SVE Integer Reduction

SVE Integer Reduction

The encodings in this section are decoded from SVE encodings.

<!-- image -->

| 31          | 24 23 22 21 20 18 17 16 15 13   |
|-------------|---------------------------------|
| 0 0 0 0 0 1 | 0 0 op0 0 0 1                   |

| op0   | Instruction details                        |
|-------|--------------------------------------------|
| 000   | SVE integer add reduction (predicated)     |
| 001   | SVE integer add reduction (quadwords)      |
| 010   | SVE integer min/max reduction (predicated) |
| 011   | SVE integer min/max reduction (quadwords)  |
| 10x   | SVE constructive prefix (predicated)       |
| 110   | SVE bitwise logical reduction (predicated) |
| 111   | SVEbitwise logical reduction (quadwords)   |

## SVE integer add reduction (predicated)

The encodings in this section are decoded from SVE Integer Reduction.

<!-- image -->

|   op | U       | Instruction Details   | Feature                        |
|------|---------|-----------------------|--------------------------------|
|    0 | 0 SADDV |                       | FEAT_SVE &#124;&#124; FEAT_SME |
|    0 | 1 UADDV |                       | FEAT_SVE &#124;&#124; FEAT_SME |
|    1 | x       | UNALLOCATED           | -                              |

## SVE integer add reduction (quadwords)

The encodings in this section are decoded from SVE Integer Reduction.

<!-- image -->

|   op | U   | Instruction Details   | Feature                              |
|------|-----|-----------------------|--------------------------------------|
|    0 | 0   | UNALLOCATED           | -                                    |
|    0 | 1   | ADDQV                 | FEAT_SVE2p1 &#124;&#124; FEAT_SME2p1 |
|    1 | x   | UNALLOCATED           | -                                    |

## SVE integer min/max reduction (predicated)

The encodings in this section are decoded from SVE Integer Reduction.

<!-- image -->

|   op | U Instruction   | Feature                        |
|------|-----------------|--------------------------------|
|    0 | 0 SMAXV         | FEAT_SVE &#124;&#124; FEAT_SME |
|    0 | 1 UMAXV         | FEAT_SVE &#124;&#124; FEAT_SME |
|    1 | 0 SMINV         | FEAT_SVE &#124;&#124; FEAT_SME |
|    1 | 1 UMINV         | FEAT_SVE &#124;&#124; FEAT_SME |

## SVE integer min/max reduction (quadwords)

The encodings in this section are decoded from SVE Integer Reduction.

<!-- image -->

|   op |   U | Instruction Details   | Feature                              |
|------|-----|-----------------------|--------------------------------------|
|    0 |   0 | SMAXQV                | FEAT_SVE2p1 &#124;&#124; FEAT_SME2p1 |
|    0 |   1 | UMAXQV                | FEAT_SVE2p1 &#124;&#124; FEAT_SME2p1 |
|    1 |   0 | SMINQV                | FEAT_SVE2p1 &#124;&#124; FEAT_SME2p1 |

|   op | U Instruction   | Feature                              |
|------|-----------------|--------------------------------------|
|    1 | 1 UMINQV        | FEAT_SVE2p1 &#124;&#124; FEAT_SME2p1 |

## SVE constructive prefix (predicated)

The encodings in this section are decoded from SVE Integer Reduction.

<!-- image -->

| opc   | Instruction Details   | Feature                        |
|-------|-----------------------|--------------------------------|
| 00    | MOVPRFX(predicated)   | FEAT_SVE &#124;&#124; FEAT_SME |
| != 00 | UNALLOCATED           | -                              |

## SVE bitwise logical reduction (predicated)

The encodings in this section are decoded from SVE Integer Reduction.

<!-- image -->

| 31      | 24 23 22 21 20 18 17 16 15 13 12 10 9   |
|---------|-----------------------------------------|
| 0 0 0 0 | 0 0 1 1 0 opc 0 0 1 Pg Zn               |

|   opc | Instruction Details   | Feature   |                       |
|-------|-----------------------|-----------|-----------------------|
|    00 | ORV                   | FEAT_SVE  | &#124;&#124; FEAT_SME |
|    01 | EORV                  | FEAT_SVE  | &#124;&#124; FEAT_SME |
|    10 | ANDV                  | FEAT_SVE  | &#124;&#124; FEAT_SME |
|    11 | UNALLOCATED           | -         |                       |

## SVE bitwise logical reduction (quadwords)

The encodings in this section are decoded from SVE Integer Reduction.

<!-- image -->

|   opc | Instruction Details   | Feature                              |
|-------|-----------------------|--------------------------------------|
|    00 | ORQV                  | FEAT_SVE2p1 &#124;&#124; FEAT_SME2p1 |
|    01 | EORQV                 | FEAT_SVE2p1 &#124;&#124; FEAT_SME2p1 |
|    10 | ANDQV                 | FEAT_SVE2p1 &#124;&#124; FEAT_SME2p1 |
|    11 | UNALLOCATED           | -                                    |

## SVE Bitwise Shift - Predicated

SVE Bitwise Shift - Predicated

The encodings in this section are decoded from SVE encodings.

<!-- image -->

| 31      | 24 23 22 21 20 19 18 16 15 13   |
|---------|---------------------------------|
| 0 0 0 0 | 0 0 op0 1 0 0                   |

| op0   | Instruction details                             |
|-------|-------------------------------------------------|
| 0x    | SVE bitwise shift by immediate (predicated)     |
| 10    | SVE bitwise shift by vector (predicated)        |
| 11    | SVE bitwise shift by wide elements (predicated) |

## SVE bitwise shift by immediate (predicated)

The encodings in this section are decoded from SVE Bitwise Shift - Predicated.

<!-- image -->

|   opc |   L |   U | Instruction Details         | Feature                         |
|-------|-----|-----|-----------------------------|---------------------------------|
|    00 |   0 |   0 | ASR (immediate, predicated) | FEAT_SVE &#124;&#124; FEAT_SME  |
|    00 |   0 |   1 | LSR (immediate, predicated) | FEAT_SVE &#124;&#124; FEAT_SME  |
|    00 |   1 |   0 | UNALLOCATED                 | -                               |
|    00 |   1 |   1 | LSL (immediate, predicated) | FEAT_SVE &#124;&#124; FEAT_SME  |
|    01 |   0 |   0 | ASRD                        | FEAT_SVE &#124;&#124; FEAT_SME  |
|    01 |   0 |   1 | UNALLOCATED                 | -                               |
|    01 |   1 |   0 | SQSHL (immediate)           | FEAT_SVE2 &#124;&#124; FEAT_SME |
|    01 |   1 |   1 | UQSHL(immediate)            | FEAT_SVE2 &#124;&#124; FEAT_SME |

|   opc | L   | U   | Instruction Details   | Feature                         |
|-------|-----|-----|-----------------------|---------------------------------|
|    10 | x   | x   | UNALLOCATED           | -                               |
|    11 | 0   | 0   | SRSHR                 | FEAT_SVE2 &#124;&#124; FEAT_SME |
|    11 | 0   | 1   | URSHR                 | FEAT_SVE2 &#124;&#124; FEAT_SME |
|    11 | 1   | 0   | UNALLOCATED           | -                               |
|    11 | 1   | 1   | SQSHLU                | FEAT_SVE2 &#124;&#124; FEAT_SME |

## SVE bitwise shift by vector (predicated)

The encodings in this section are decoded from SVE Bitwise Shift - Predicated.

<!-- image -->

| 31          | 24 23 22 21 20 19 18 17 16 15 13 12   |
|-------------|---------------------------------------|
| 0 0 0 0 0 1 | 0 0 1 0 R L U 1 0 0 Pg                |

| R   |   L |   U | Instruction Details   | Feature                        |
|-----|-----|-----|-----------------------|--------------------------------|
| x   |   1 |   0 | UNALLOCATED           | -                              |
| 0   |   0 |   0 | ASR (vectors)         | FEAT_SVE &#124;&#124; FEAT_SME |
| 0   |   0 |   1 | LSR (vectors)         | FEAT_SVE &#124;&#124; FEAT_SME |
| 0   |   1 |   1 | LSL (vectors)         | FEAT_SVE &#124;&#124; FEAT_SME |
| 1   |   0 |   0 | ASRR                  | FEAT_SVE &#124;&#124; FEAT_SME |
| 1   |   0 |   1 | LSRR                  | FEAT_SVE &#124;&#124; FEAT_SME |
| 1   |   1 |   1 | LSLR                  | FEAT_SVE &#124;&#124; FEAT_SME |

## SVE bitwise shift by wide elements (predicated)

The encodings in this section are decoded from SVE Bitwise Shift - Predicated.

<!-- image -->

|   R |   L |   U | Instruction Details             | Feature                        |
|-----|-----|-----|---------------------------------|--------------------------------|
|   0 |   0 |   0 | ASR (wide elements, predicated) | FEAT_SVE &#124;&#124; FEAT_SME |
|   0 |   0 |   1 | LSR (wide elements, predicated) | FEAT_SVE &#124;&#124; FEAT_SME |
|   0 |   1 |   0 | UNALLOCATED                     | -                              |
|   0 |   1 |   1 | LSL (wide elements, predicated) | FEAT_SVE &#124;&#124; FEAT_SME |

|   R | L   | U Instruction Details   | Feature   |
|-----|-----|-------------------------|-----------|
|   1 | x   | x UNALLOCATED           | -         |

## SVE Integer Unary Arithmetic - Predicated

SVE Integer Unary Arithmetic - Predicated

The encodings in this section are decoded from SVE encodings.

<!-- image -->

| 31              | 24 23 22 21 20 19 18 16 15 13   |
|-----------------|---------------------------------|
| 0 0 0 0 0 1 0 0 | 0 op0 1 0 1                     |

| op0   | Instruction details                       |
|-------|-------------------------------------------|
| x0    | SVE integer unary operations (predicated) |
| x1    | SVEbitwise unary operations (predicated)  |

## SVE integer unary operations (predicated)

The encodings in this section are decoded from SVE Integer Unary Arithmetic - Predicated.

<!-- image -->

| 31   | 24 23 19 18 16     | 22 21 20 15 13 12 10 9 5 4   |
|------|--------------------|------------------------------|
| 0 0  | 0 size 0 M 0 opc 1 | 0 1 Pg Zn Zd                 |

|   M |   opc | Instruction Details                  | Feature                              |
|-----|-------|--------------------------------------|--------------------------------------|
|   0 |   000 | SXTB, SXTH, SXTW-Byte, zeroing       | FEAT_SVE2p2 &#124;&#124; FEAT_SME2p2 |
|   0 |   001 | UXTB, UXTH, UXTW-Byte, zeroing       | FEAT_SVE2p2 &#124;&#124; FEAT_SME2p2 |
|   0 |   010 | SXTB, SXTH, SXTW - Halfword, zeroing | FEAT_SVE2p2 &#124;&#124; FEAT_SME2p2 |
|   0 |   011 | UXTB, UXTH, UXTW - Halfword, zeroing | FEAT_SVE2p2 &#124;&#124; FEAT_SME2p2 |
|   0 |   100 | SXTB, SXTH, SXTW-Word,zeroing        | FEAT_SVE2p2 &#124;&#124; FEAT_SME2p2 |
|   0 |   101 | UXTB, UXTH, UXTW-Word,zeroing        | FEAT_SVE2p2 &#124;&#124; FEAT_SME2p2 |
|   0 |   110 | ABS -Zeroing                         | FEAT_SVE2p2 &#124;&#124; FEAT_SME2p2 |
|   0 |   111 | NEG-Zeroing                          | FEAT_SVE2p2 &#124;&#124; FEAT_SME2p2 |
|   1 |   000 | SXTB, SXTH, SXTW-Byte, merging       | FEAT_SVE &#124;&#124; FEAT_SME       |
|   1 |   001 | UXTB, UXTH, UXTW-Byte, merging       | FEAT_SVE &#124;&#124; FEAT_SME       |
|   1 |   010 | SXTB, SXTH, SXTW - Halfword, merging | FEAT_SVE &#124;&#124; FEAT_SME       |

|   M |   opc | Instruction Details                  | Feature                        |
|-----|-------|--------------------------------------|--------------------------------|
|   1 |   011 | UXTB, UXTH, UXTW - Halfword, merging | FEAT_SVE &#124;&#124; FEAT_SME |
|   1 |   100 | SXTB, SXTH, SXTW-Word,merging        | FEAT_SVE &#124;&#124; FEAT_SME |
|   1 |   101 | UXTB, UXTH, UXTW-Word,merging        | FEAT_SVE &#124;&#124; FEAT_SME |
|   1 |   110 | ABS -Merging                         | FEAT_SVE &#124;&#124; FEAT_SME |
|   1 |   111 | NEG-Merging                          | FEAT_SVE &#124;&#124; FEAT_SME |

## SVE bitwise unary operations (predicated)

The encodings in this section are decoded from SVE Integer Unary Arithmetic - Predicated.

<!-- image -->

| M   |   opc | Instruction Details   | Feature                              |
|-----|-------|-----------------------|--------------------------------------|
| x   |   111 | UNALLOCATED           | -                                    |
| 0   |   000 | CLS -Zeroing          | FEAT_SVE2p2 &#124;&#124; FEAT_SME2p2 |
| 0   |   001 | CLZ -Zeroing          | FEAT_SVE2p2 &#124;&#124; FEAT_SME2p2 |
| 0   |   010 | CNT-Zeroing           | FEAT_SVE2p2 &#124;&#124; FEAT_SME2p2 |
| 0   |   011 | CNOT-Zeroing          | FEAT_SVE2p2 &#124;&#124; FEAT_SME2p2 |
| 0   |   100 | FABS -Zeroing         | FEAT_SVE2p2 &#124;&#124; FEAT_SME2p2 |
| 0   |   101 | FNEG -Zeroing         | FEAT_SVE2p2 &#124;&#124; FEAT_SME2p2 |
| 0   |   110 | NOT(vector) -Zeroing  | FEAT_SVE2p2 &#124;&#124; FEAT_SME2p2 |
| 1   |   000 | CLS -Merging          | FEAT_SVE &#124;&#124; FEAT_SME       |
| 1   |   001 | CLZ -Merging          | FEAT_SVE &#124;&#124; FEAT_SME       |
| 1   |   010 | CNT-Merging           | FEAT_SVE &#124;&#124; FEAT_SME       |
| 1   |   011 | CNOT-Merging          | FEAT_SVE &#124;&#124; FEAT_SME       |
| 1   |   100 | FABS -Merging         | FEAT_SVE &#124;&#124; FEAT_SME       |
| 1   |   101 | FNEG -Merging         | FEAT_SVE &#124;&#124; FEAT_SME       |
| 1   |   110 | NOT(vector) -Merging  | FEAT_SVE &#124;&#124; FEAT_SME       |

## SVE Integer Multiply-Add - Predicated

SVE Integer Multiply-Add - Predicated

The encodings in this section are decoded from SVE encodings.

<!-- image -->

| 31   | 25 20 16 15 14   |   24 23 22 21 | 13   |    |       |
|------|------------------|---------------|------|----|-------|
| 0 0  | 0 0 0 1 0        |             0 |      |  0 | op0 1 |

## SVE integer multiply-accumulate writing addend (predicated)

The encodings in this section are decoded from SVE Integer Multiply-Add - Predicated.

<!-- image -->

|   op | Instruction Details   | Feature                        |
|------|-----------------------|--------------------------------|
|    0 | MLA(vectors)          | FEAT_SVE &#124;&#124; FEAT_SME |
|    1 | MLS(vectors)          | FEAT_SVE &#124;&#124; FEAT_SME |

## SVE integer multiply-add writing multiplicand (predicated)

The encodings in this section are decoded from SVE Integer Multiply-Add - Predicated.

<!-- image -->

|   op | Instruction Details   | Feature                        |
|------|-----------------------|--------------------------------|
|    0 | MAD                   | FEAT_SVE &#124;&#124; FEAT_SME |
|    1 | MSB                   | FEAT_SVE &#124;&#124; FEAT_SME |

## SVE Bitwise Logical - Unpredicated

SVE Bitwise Logical - Unpredicated

The encodings in this section are decoded from SVE encodings.

<!-- image -->

|   op0 | Instruction details                                         |
|-------|-------------------------------------------------------------|
|     0 | SVE integer multiply-accumulate writing addend (predicated) |
|     1 | SVE integer multiply-add writing multiplicand (predicated)  |

## SVE2 bitwise ternary operations

The encodings in this section are decoded from SVE Bitwise Logical - Unpredicated.

<!-- image -->

<!-- image -->

| opc   |   o2 | Instruction Details   | Feature                         |
|-------|------|-----------------------|---------------------------------|
| 00    |    0 | EOR3                  | FEAT_SVE2 &#124;&#124; FEAT_SME |
| 00    |    1 | BSL                   | FEAT_SVE2 &#124;&#124; FEAT_SME |
| 01    |    0 | BCAX                  | FEAT_SVE2 &#124;&#124; FEAT_SME |
| 01    |    1 | BSL1N                 | FEAT_SVE2 &#124;&#124; FEAT_SME |
| 1x    |    0 | UNALLOCATED           | -                               |
| 10    |    1 | BSL2N                 | FEAT_SVE2 FEAT_SME              |

| op0   | Instruction details                           | Feature                         |
|-------|-----------------------------------------------|---------------------------------|
| 0xx   | UNALLOCATED                                   | -                               |
| 100   | SVE bitwise logical operations (unpredicated) | -                               |
| 101   | XAR                                           | FEAT_SVE2 &#124;&#124; FEAT_SME |
| 11x   | SVE2 bitwise ternary operations               | -                               |

## SVE bitwise logical operations (unpredicated)

The encodings in this section are decoded from SVE Bitwise Logical - Unpredicated.

<!-- image -->

| 31    | 24 23 22 21 20   | 16 15 13   | 12 10 9   | 5 4   |
|-------|------------------|------------|-----------|-------|
| 0 0 0 | 0 opc 1          | Zm 0 0 1   | 1 0 0 Zn  | Zd    |

|   opc | Instruction Details         | Feature   |                       |
|-------|-----------------------------|-----------|-----------------------|
|    00 | AND(vectors, unpredicated)  | FEAT_SVE  | &#124;&#124; FEAT_SME |
|    01 | ORR(vectors, unpredicated)  | FEAT_SVE  | &#124;&#124; FEAT_SME |
|    10 | EOR(vectors, unpredicated)  | FEAT_SVE  | &#124;&#124; FEAT_SME |
|    11 | BIC (vectors, unpredicated) | FEAT_SVE  | &#124;&#124; FEAT_SME |

||

## SVE Index Generation

SVE Index Generation

The encodings in this section are decoded from SVE encodings.

<!-- image -->

|   op0 | Instruction details       | Feature   |                       |
|-------|---------------------------|-----------|-----------------------|
|    00 | INDEX (immediates)        | FEAT_SVE  | &#124;&#124; FEAT_SME |
|    01 | INDEX (scalar, immediate) | FEAT_SVE  | &#124;&#124; FEAT_SME |
|    10 | INDEX (immediate, scalar) | FEAT_SVE  | &#124;&#124; FEAT_SME |
|    11 | INDEX (scalars)           | FEAT_SVE  | &#124;&#124; FEAT_SME |

## SVE Stack Allocation

SVE Stack Allocation

The encodings in this section are decoded from SVE encodings.

<!-- image -->

| 31    | 24 23 22 21 20 16 15 12 11   |
|-------|------------------------------|
| 0 0 0 | 0 op0 1 0 1 0 1 op1          |

|   op0 |   op1 | Instruction details                  |
|-------|-------|--------------------------------------|
|     0 |     0 | SVE stack frame adjustment           |
|     0 |     1 | Streaming SVE stack frame adjustment |
|     1 |     0 | SVE stack frame size                 |
|     1 |     1 | Streaming SVE stack frame size       |

## SVE stack frame adjustment

The encodings in this section are decoded from SVE Stack Allocation.

<!-- image -->

|   opc |   o2 | Instruction Details   | Feature                         |
|-------|------|-----------------------|---------------------------------|
|    11 |    1 | NBSL                  | FEAT_SVE2 &#124;&#124; FEAT_SME |

## SVE stack frame size

The encodings in this section are decoded from SVE Stack Allocation.

<!-- image -->

| 31    | 24 23 22 21 20 16 15 12   |
|-------|---------------------------|
| 0 0 0 | 0 1 op 1 opc2 0 1 0 1     |

|   op | opc2     | Instruction Details   | Feature                        |
|------|----------|-----------------------|--------------------------------|
|    0 | 11111    | RDVL                  | FEAT_SVE &#124;&#124; FEAT_SME |
|    0 | != 11111 | UNALLOCATED           | -                              |
|    1 | xxxxx    | UNALLOCATED           | -                              |

## Streaming SVE stack frame size

The encodings in this section are decoded from SVE Stack Allocation.

<!-- image -->

|   op | Instruction Details   | Feature                        |
|------|-----------------------|--------------------------------|
|    0 | ADDVL                 | FEAT_SVE &#124;&#124; FEAT_SME |
|    1 | ADDPL                 | FEAT_SVE &#124;&#124; FEAT_SME |

## Streaming SVE stack frame adjustment

The encodings in this section are decoded from SVE Stack Allocation.

<!-- image -->

| 31    | 24 23 22 21 20 16 15   |
|-------|------------------------|
| 0 0 0 | 0 0 op 1 Rn 0 1 0      |

|   op | Instruction Details   | Feature   |
|------|-----------------------|-----------|
|    0 | ADDSVL                | FEAT_SME  |
|    1 | ADDSPL                | FEAT_SME  |

|   op | opc2     | Instruction Details   | Feature   |
|------|----------|-----------------------|-----------|
|    0 | 11111    | RDSVL                 | FEAT_SME  |
|    0 | != 11111 | UNALLOCATED           | -         |
|    1 | xxxxx    | UNALLOCATED           | -         |

## SVE2 Integer Arithmetic - Unpredicated

SVE2 Integer Arithmetic - Unpredicated

The encodings in this section are decoded from SVE encodings.

<!-- image -->

| 31   | 25 24 23 22 21 20 16 15 13 12   |
|------|---------------------------------|
| 0 0  | 0 0 1 0 1 1 op0                 |

| op0   | Instruction details                                          |
|-------|--------------------------------------------------------------|
| 0xx   | SVE2 integer multiply vectors (unpredicated)                 |
| 10x   | SVE2 signed saturating doubling multiply high (unpredicated) |
| 11x   | UNALLOCATED                                                  |

## SVE2 integer multiply vectors (unpredicated)

The encodings in this section are decoded from SVE2 Integer Arithmetic - Unpredicated.

<!-- image -->

| size   | opc                           | Instruction Details   | Feature                         |
|--------|-------------------------------|-----------------------|---------------------------------|
| xx     | 00 MUL(vectors, unpredicated) | FEAT_SVE2             | &#124;&#124; FEAT_SME           |
| xx     | 10                            | SMULH(unpredicated)   | FEAT_SVE2 &#124;&#124; FEAT_SME |
| xx     | 11                            | UMULH(unpredicated)   | FEAT_SVE2 &#124;&#124; FEAT_SME |
| 00     | 01                            | PMUL                  | FEAT_SVE2 &#124;&#124; FEAT_SME |
| != 00  | 01                            | UNALLOCATED           | -                               |

## SVE2 signed saturating doubling multiply high (unpredicated)

The encodings in this section are decoded from SVE2 Integer Arithmetic - Unpredicated.

<!-- image -->

|   R | Instruction Details   | Feature                         |
|-----|-----------------------|---------------------------------|
|   0 | SQDMULH(vectors)      | FEAT_SVE2 &#124;&#124; FEAT_SME |
|   1 | SQRDMULH(vectors)     | FEAT_SVE2 &#124;&#124; FEAT_SME |

## SVE Bitwise Shift - Unpredicated

SVE Bitwise Shift - Unpredicated

The encodings in this section are decoded from SVE encodings.

<!-- image -->

|   op0 | Instruction details                               |
|-------|---------------------------------------------------|
|     0 | SVE bitwise shift by wide elements (unpredicated) |
|     1 | SVE bitwise shift by immediate (unpredicated)     |

## SVE bitwise shift by wide elements (unpredicated)

The encodings in this section are decoded from SVE Bitwise Shift - Unpredicated.

<!-- image -->

|   opc | Instruction Details               | Feature                        |
|-------|-----------------------------------|--------------------------------|
|    00 | ASR (wide elements, unpredicated) | FEAT_SVE &#124;&#124; FEAT_SME |
|    01 | LSR (wide elements, unpredicated) | FEAT_SVE &#124;&#124; FEAT_SME |

## SVE Integer Misc - Unpredicated

SVE Integer Misc - Unpredicated

The encodings in this section are decoded from SVE encodings.

<!-- image -->

| op0   | Instruction details                        |
|-------|--------------------------------------------|
| 0x    | SVE floating-point trig select coefficient |
| 10    | SVE floating-point exponential accelerator |
| 11    | SVE constructive prefix (unpredicated)     |

|   opc | Instruction Details               | Feature                        |
|-------|-----------------------------------|--------------------------------|
|    10 | UNALLOCATED                       | -                              |
|    11 | LSL (wide elements, unpredicated) | FEAT_SVE &#124;&#124; FEAT_SME |

## SVE bitwise shift by immediate (unpredicated)

The encodings in this section are decoded from SVE Bitwise Shift - Unpredicated.

<!-- image -->

|   opc | Instruction Details           | Feature                        |
|-------|-------------------------------|--------------------------------|
|    00 | ASR (immediate, unpredicated) | FEAT_SVE &#124;&#124; FEAT_SME |
|    01 | LSR (immediate, unpredicated) | FEAT_SVE &#124;&#124; FEAT_SME |
|    10 | UNALLOCATED                   | -                              |
|    11 | LSL (immediate, unpredicated) | FEAT_SVE &#124;&#124; FEAT_SME |

## SVE floating-point trig select coefficient

The encodings in this section are decoded from SVE Integer Misc - Unpredicated.

<!-- image -->

## SVE floating-point exponential accelerator

The encodings in this section are decoded from SVE Integer Misc - Unpredicated.

<!-- image -->

| opc      | Instruction Details   | Feature                               |
|----------|-----------------------|---------------------------------------|
| 00000    | FEXPA                 | FEAT_SVE &#124;&#124; FEAT_SSVE_FEXPA |
| != 00000 | UNALLOCATED           | -                                     |

## SVE constructive prefix (unpredicated)

The encodings in this section are decoded from SVE Integer Misc - Unpredicated.

<!-- image -->

| opc   | opc2     | Instruction Details   | Feature                        |
|-------|----------|-----------------------|--------------------------------|
| 00    | 00000    | MOVPRFX(unpredicated) | FEAT_SVE &#124;&#124; FEAT_SME |
| 00    | != 00000 | UNALLOCATED           | -                              |
| != 00 | xxxxx    | UNALLOCATED           | -                              |

## SVE Element Count

SVE Element Count

The encodings in this section are decoded from SVE encodings.

<!-- image -->

| 31          | 24 23 22 21 20 19 16 15 14 13   |
|-------------|---------------------------------|
| 0 0 0 0 0 1 | 0 1 op0 1 1 op1                 |

|   op | Instruction Details   | Feature   |
|------|-----------------------|-----------|
|    0 | FTSSEL                | FEAT_SVE  |
|    1 | UNALLOCATED           | -         |

## SVE element count

The encodings in this section are decoded from SVE Element Count.

| op0   | op1   | Instruction details                              |
|-------|-------|--------------------------------------------------|
| 0     | 00x   | SVE saturating inc/dec vector by element count   |
| 0     | 100   | SVE element count                                |
| 0     | 101   | UNALLOCATED                                      |
| 1     | 000   | SVE inc/dec vector by element count              |
| 1     | 100   | SVE inc/dec register by element count            |
| 1     | x01   | UNALLOCATED                                      |
| x     | 01x   | UNALLOCATED                                      |
| x     | 11x   | SVE saturating inc/dec register by element count |

## SVE saturating inc/dec vector by element count

The encodings in this section are decoded from SVE Element Count.

<!-- image -->

|   size | D   | U   | Instruction Details   | Feature                        |
|--------|-----|-----|-----------------------|--------------------------------|
|     00 | x   | x   | UNALLOCATED           | -                              |
|     01 | 0   | 0   | SQINCH (vector)       | FEAT_SVE &#124;&#124; FEAT_SME |
|     01 | 0   | 1   | UQINCH (vector)       | FEAT_SVE &#124;&#124; FEAT_SME |
|     01 | 1   | 0   | SQDECH(vector)        | FEAT_SVE &#124;&#124; FEAT_SME |
|     01 | 1   | 1   | UQDECH(vector)        | FEAT_SVE &#124;&#124; FEAT_SME |
|     10 | 0   | 0   | SQINCW (vector)       | FEAT_SVE &#124;&#124; FEAT_SME |
|     10 | 0   | 1   | UQINCW(vector)        | FEAT_SVE &#124;&#124; FEAT_SME |
|     10 | 1   | 0   | SQDECW(vector)        | FEAT_SVE &#124;&#124; FEAT_SME |
|     10 | 1   | 1   | UQDECW(vector)        | FEAT_SVE &#124;&#124; FEAT_SME |
|     11 | 0   | 0   | SQINCD (vector)       | FEAT_SVE &#124;&#124; FEAT_SME |
|     11 | 0   | 1   | UQINCD (vector)       | FEAT_SVE &#124;&#124; FEAT_SME |
|     11 | 1   | 0   | SQDECD(vector)        | FEAT_SVE &#124;&#124; FEAT_SME |
|     11 | 1   | 1   | UQDECD(vector)        | FEAT_SVE &#124;&#124; FEAT_SME |

<!-- image -->

| size   |   op | Instruction Details                 | Feature                        |
|--------|------|-------------------------------------|--------------------------------|
| xx     |    1 | UNALLOCATED                         | -                              |
| 00     |    0 | CNTB,CNTD,CNTH,CNTW-Byte            | FEAT_SVE &#124;&#124; FEAT_SME |
| 01     |    0 | CNTB, CNTD, CNTH, CNTW - Halfword   | FEAT_SVE &#124;&#124; FEAT_SME |
| 10     |    0 | CNTB,CNTD,CNTH,CNTW-Word            | FEAT_SVE &#124;&#124; FEAT_SME |
| 11     |    0 | CNTB, CNTD, CNTH, CNTW - Doubleword | FEAT_SVE &#124;&#124; FEAT_SME |

## SVE inc/dec vector by element count

The encodings in this section are decoded from SVE Element Count.

<!-- image -->

| 31    | 24 23 22 21 20 19 16 15 14 13 11 10 9   |
|-------|-----------------------------------------|
| 0 0 0 | 0 size 1 1 imm4 1 1 0 0 0 D pattern     |

|   size | D   | Instruction Details                    | Feature                        |
|--------|-----|----------------------------------------|--------------------------------|
|     00 | x   | UNALLOCATED                            | -                              |
|     01 | 0   | INCD, INCH, INCW(vector) -Halfword     | FEAT_SVE &#124;&#124; FEAT_SME |
|     01 | 1   | DECD, DECH, DECW (vector) - Halfword   | FEAT_SVE &#124;&#124; FEAT_SME |
|     10 | 0   | INCD, INCH, INCW(vector)-Word          | FEAT_SVE &#124;&#124; FEAT_SME |
|     10 | 1   | DECD, DECH, DECW(vector)-Word          | FEAT_SVE &#124;&#124; FEAT_SME |
|     11 | 0   | INCD, INCH, INCW (vector) - Doubleword | FEAT_SVE &#124;&#124; FEAT_SME |
|     11 | 1   | DECD, DECH, DECW (vector) - Doubleword | FEAT_SVE &#124;&#124; FEAT_SME |

## SVE inc/dec register by element count

The encodings in this section are decoded from SVE Element Count.

<!-- image -->

|   size |   D | Instruction Details                          | Feature                        |
|--------|-----|----------------------------------------------|--------------------------------|
|     00 |   0 | INCB, INCD, INCH, INCW (scalar) - Byte       | FEAT_SVE &#124;&#124; FEAT_SME |
|     00 |   1 | DECB, DECD, DECH, DECW(scalar)- Byte         | FEAT_SVE &#124;&#124; FEAT_SME |
|     01 |   0 | INCB, INCD, INCH, INCW (scalar) - Halfword   | FEAT_SVE &#124;&#124; FEAT_SME |
|     01 |   1 | DECB, DECD, DECH, DECW(scalar)- Halfword     | FEAT_SVE &#124;&#124; FEAT_SME |
|     10 |   0 | INCB, INCD, INCH, INCW (scalar) - Word       | FEAT_SVE &#124;&#124; FEAT_SME |
|     10 |   1 | DECB, DECD, DECH, DECW(scalar)- Word         | FEAT_SVE &#124;&#124; FEAT_SME |
|     11 |   0 | INCB, INCD, INCH, INCW (scalar) - Doubleword | FEAT_SVE &#124;&#124; FEAT_SME |
|     11 |   1 | DECB, DECD, DECH, DECW(scalar)- Doubleword   | FEAT_SVE &#124;&#124; FEAT_SME |

## SVE saturating inc/dec register by element count

The encodings in this section are decoded from SVE Element Count.

<!-- image -->

| 31    | 24 23 22 21 20   | 16 12 11   | 15 10 9 5 4   |
|-------|------------------|------------|---------------|
| 0 0 0 | 0 size 1 sf      | 1 1 1 1 D  | U pattern Rdn |

|   size |   sf |   D |   U | Instruction Details     | Feature                        |
|--------|------|-----|-----|-------------------------|--------------------------------|
|     00 |    0 |   0 |   0 | SQINCB -32-bit          | FEAT_SVE &#124;&#124; FEAT_SME |
|     00 |    0 |   0 |   1 | UQINCB -32-bit          | FEAT_SVE &#124;&#124; FEAT_SME |
|     00 |    0 |   1 |   0 | SQDECB -32-bit          | FEAT_SVE &#124;&#124; FEAT_SME |
|     00 |    0 |   1 |   1 | UQDECB-32-bit           | FEAT_SVE &#124;&#124; FEAT_SME |
|     00 |    1 |   0 |   0 | SQINCB -64-bit          | FEAT_SVE &#124;&#124; FEAT_SME |
|     00 |    1 |   0 |   1 | UQINCB -64-bit          | FEAT_SVE &#124;&#124; FEAT_SME |
|     00 |    1 |   1 |   0 | SQDECB -64-bit          | FEAT_SVE &#124;&#124; FEAT_SME |
|     00 |    1 |   1 |   1 | UQDECB-64-bit           | FEAT_SVE &#124;&#124; FEAT_SME |
|     01 |    0 |   0 |   0 | SQINCH (scalar) -32-bit | FEAT_SVE &#124;&#124; FEAT_SME |
|     01 |    0 |   0 |   1 | UQINCH (scalar) -32-bit | FEAT_SVE &#124;&#124; FEAT_SME |
|     01 |    0 |   1 |   0 | SQDECH(scalar) -32-bit  | FEAT_SVE &#124;&#124; FEAT_SME |
|     01 |    0 |   1 |   1 | UQDECH(scalar) -32-bit  | FEAT_SVE &#124;&#124; FEAT_SME |
|     01 |    1 |   0 |   0 | SQINCH (scalar) -64-bit | FEAT_SVE &#124;&#124; FEAT_SME |
|     01 |    1 |   0 |   1 | UQINCH (scalar) -64-bit | FEAT_SVE &#124;&#124; FEAT_SME |

|   size |   sf |   D |   U | Instruction Details     | Feature                        |
|--------|------|-----|-----|-------------------------|--------------------------------|
|     01 |    1 |   1 |   0 | SQDECH(scalar) -64-bit  | FEAT_SVE &#124;&#124; FEAT_SME |
|     01 |    1 |   1 |   1 | UQDECH(scalar) -64-bit  | FEAT_SVE &#124;&#124; FEAT_SME |
|     10 |    0 |   0 |   0 | SQINCW (scalar) -32-bit | FEAT_SVE &#124;&#124; FEAT_SME |
|     10 |    0 |   0 |   1 | UQINCW(scalar) -32-bit  | FEAT_SVE &#124;&#124; FEAT_SME |
|     10 |    0 |   1 |   0 | SQDECW(scalar) -32-bit  | FEAT_SVE &#124;&#124; FEAT_SME |
|     10 |    0 |   1 |   1 | UQDECW(scalar) -32-bit  | FEAT_SVE &#124;&#124; FEAT_SME |
|     10 |    1 |   0 |   0 | SQINCW (scalar) -64-bit | FEAT_SVE &#124;&#124; FEAT_SME |
|     10 |    1 |   0 |   1 | UQINCW(scalar) -64-bit  | FEAT_SVE &#124;&#124; FEAT_SME |
|     10 |    1 |   1 |   0 | SQDECW(scalar) -64-bit  | FEAT_SVE &#124;&#124; FEAT_SME |
|     10 |    1 |   1 |   1 | UQDECW(scalar) -64-bit  | FEAT_SVE &#124;&#124; FEAT_SME |
|     11 |    0 |   0 |   0 | SQINCD (scalar) -32-bit | FEAT_SVE &#124;&#124; FEAT_SME |
|     11 |    0 |   0 |   1 | UQINCD (scalar) -32-bit | FEAT_SVE &#124;&#124; FEAT_SME |
|     11 |    0 |   1 |   0 | SQDECD(scalar) -32-bit  | FEAT_SVE &#124;&#124; FEAT_SME |
|     11 |    0 |   1 |   1 | UQDECD(scalar) -32-bit  | FEAT_SVE &#124;&#124; FEAT_SME |
|     11 |    1 |   0 |   0 | SQINCD (scalar) -64-bit | FEAT_SVE &#124;&#124; FEAT_SME |
|     11 |    1 |   0 |   1 | UQINCD (scalar) -64-bit | FEAT_SVE &#124;&#124; FEAT_SME |
|     11 |    1 |   1 |   0 | SQDECD(scalar) -64-bit  | FEAT_SVE &#124;&#124; FEAT_SME |
|     11 |    1 |   1 |   1 | UQDECD(scalar) -64-bit  | FEAT_SVE &#124;&#124; FEAT_SME |

## SVE Permute Vector - Extract

SVE Permute Vector - Extract

The encodings in this section are decoded from SVE encodings.

<!-- image -->

| 31    | 16 15 13   |
|-------|------------|
| 0 0 0 | 0 0 0      |

|   op0 | Instruction details   | Feature                         |
|-------|-----------------------|---------------------------------|
|     0 | EXT -Destructive      | FEAT_SVE &#124;&#124; FEAT_SME  |
|     1 | EXT -Constructive     | FEAT_SVE2 &#124;&#124; FEAT_SME |

## SVE Permute Vector - Segments

SVE Permute Vector - Segments

The encodings in this section are decoded from SVE encodings.

<!-- image -->

## SVE permute vector segments

The encodings in this section are decoded from SVE Permute Vector - Segments.

<!-- image -->

| 31   | 23 22 21 20 16 15 13 12 11   |
|------|------------------------------|
| 0 0  | 1 0 1 Zm 0 0 0 opc           |

|   opc | H   | Instruction Details                | Instruction Details   | Instruction Details   | Feature    |
|-------|-----|------------------------------------|-----------------------|-----------------------|------------|
|    00 | 0   | ZIP1, ZIP2 (vectors) - (quadwords) | Low                   | halves                | FEAT_F64MM |
|    00 | 1   | ZIP1, ZIP2 (vectors) - (quadwords) | High                  | halves                | FEAT_F64MM |
|    01 | 0   | UZP1, UZP2 (vectors) (quadwords)   | -                     | Even                  | FEAT_F64MM |
|    01 | 1   | UZP1, UZP2 (vectors) (quadwords)   | -                     | Odd                   | FEAT_F64MM |
|    10 | x   | UNALLOCATED                        | UNALLOCATED           | UNALLOCATED           | -          |
|    11 | 0   | TRN1, TRN2 (vectors) (quadwords)   | -                     | Even                  | FEAT_F64MM |
|    11 | 1   | TRN1, TRN2 (vectors) (quadwords)   | -                     | Odd                   | FEAT_F64MM |

## SVE Bitwise Immediate

SVE Bitwise Immediate

The encodings in this section are decoded from SVE encodings.

<!-- image -->

| 31   | 24 23 22 21 20 19 18 17   |
|------|---------------------------|
| 0 0  | 1 op0 0 0 op1             |

| op0   | op1   | Instruction details   | Feature                        |
|-------|-------|-----------------------|--------------------------------|
| 11    | 00    | DUPM                  | FEAT_SVE &#124;&#124; FEAT_SME |
| xx    | != 00 | UNALLOCATED           | -                              |

|   op0 | Instruction details         |
|-------|-----------------------------|
|     0 | SVE permute vector segments |
|     1 | UNALLOCATED                 |

| op0   |   op1 | Instruction details Feature                         |
|-------|-------|-----------------------------------------------------|
| != 11 |    00 | SVE bitwise logical with immediate (unpredicated) - |

## SVE bitwise logical with immediate (unpredicated)

The encodings in this section are decoded from SVE Bitwise Immediate.

<!-- image -->

The following constraints also apply to this encoding: opc != '11'

|   opc | Instruction Details   | Feature                        |
|-------|-----------------------|--------------------------------|
|    00 | ORR(immediate)        | FEAT_SVE &#124;&#124; FEAT_SME |
|    01 | EOR(immediate)        | FEAT_SVE &#124;&#124; FEAT_SME |
|    10 | AND(immediate)        | FEAT_SVE &#124;&#124; FEAT_SME |

## SVE Integer Wide Immediate - Predicated

SVE Integer Wide Immediate - Predicated

The encodings in this section are decoded from SVE encodings.

<!-- image -->

| op0   | Instruction details                     | Feature                        |
|-------|-----------------------------------------|--------------------------------|
| 0xx   | SVE copy integer immediate (predicated) | -                              |
| 10x   | UNALLOCATED                             | -                              |
| 110   | FCPY                                    | FEAT_SVE &#124;&#124; FEAT_SME |
| 111   | UNALLOCATED                             | -                              |

## SVE copy integer immediate (predicated)

The encodings in this section are decoded from SVE Integer Wide Immediate - Predicated.

<!-- image -->

|   M | Instruction Details      | Feature                        |
|-----|--------------------------|--------------------------------|
|   0 | CPY (immediate, zeroing) | FEAT_SVE &#124;&#124; FEAT_SME |
|   1 | CPY (immediate, merging) | FEAT_SVE &#124;&#124; FEAT_SME |

## SVE Permute Vector - One Source Quadwords

SVE Permute Vector - One Source Quadwords

The encodings in this section are decoded from SVE encodings.

<!-- image -->

| 31    | 24 23 22 21 20 19 16 15 10   |
|-------|------------------------------|
| 0 0 0 | 1 op0 1 op1 0 0 1 0 0 1      |

| op0   | op1   | Instruction details   | Feature                              |
|-------|-------|-----------------------|--------------------------------------|
| 00    | x     | DUPQ                  | FEAT_SVE2p1 &#124;&#124; FEAT_SME2p1 |
| 01    | 0     | EXTQ                  | FEAT_SVE2p1 &#124;&#124; FEAT_SME2p1 |
| 01    | 1     | UNALLOCATED           | -                                    |
| 1x    | x     | UNALLOCATED           | -                                    |

## SVE Permute Vector - Unpredicated

SVE Permute Vector - Unpredicated

The encodings in this section are decoded from SVE encodings.

<!-- image -->

|   op0 | op1   | op2   | op3   | Instruction details            | Feature                        |
|-------|-------|-------|-------|--------------------------------|--------------------------------|
|    00 | 000   | x     | x     | DUP(scalar)                    | FEAT_SVE &#124;&#124; FEAT_SME |
|    00 | 100   | x     | x     | INSR (scalar)                  | FEAT_SVE &#124;&#124; FEAT_SME |
|    00 | x01   | x     | x     | UNALLOCATED                    | -                              |
|    00 | x1x   | x     | x     | UNALLOCATED                    | -                              |
|    01 | xx0   | x     | 0     | SVE move predicate from vector | -                              |
|    01 | xx0   | x     | 1     | UNALLOCATED                    | -                              |
|    01 | xx1   | 0     | x     | SVE move predicate into vector | -                              |
|    01 | xx1   | 1     | x     | UNALLOCATED                    | -                              |
|    10 | 0xx   | x     | x     | SVE unpack vector elements     | -                              |

|   op0 | op1    | op2   | op3   | Instruction details   | Feature                        |
|-------|--------|-------|-------|-----------------------|--------------------------------|
|    10 | 100    | x     | x     | INSR (SIMD&FP scalar) | FEAT_SVE &#124;&#124; FEAT_SME |
|    10 | 101    | x     | x     | UNALLOCATED           | -                              |
|    10 | 11x    | x     | x     | UNALLOCATED           | -                              |
|    11 | 000    | x     | x     | REV(vector)           | FEAT_SVE &#124;&#124; FEAT_SME |
|    11 | != 000 | x     | x     | UNALLOCATED           | -                              |

## SVE move predicate from vector

The encodings in this section are decoded from SVE Permute Vector - Unpredicated.

<!-- image -->

| opc   | opc2   | Instruction Details            | Feature                              |
|-------|--------|--------------------------------|--------------------------------------|
| 00    | 00     | UNALLOCATED                    | -                                    |
| 00    | 01     | PMOV(to predicate) -Byte       | FEAT_SVE2p1 &#124;&#124; FEAT_SME2p1 |
| 00    | 1x     | PMOV(to predicate) -Halfword   | FEAT_SVE2p1 &#124;&#124; FEAT_SME2p1 |
| 01    | xx     | PMOV(to predicate)-Word        | FEAT_SVE2p1 &#124;&#124; FEAT_SME2p1 |
| 1x    | xx     | PMOV(to predicate) -Doubleword | FEAT_SVE2p1 &#124;&#124; FEAT_SME2p1 |

## SVE move predicate into vector

The encodings in this section are decoded from SVE Permute Vector - Unpredicated.

<!-- image -->

| opc   | opc2   | Instruction Details         | Feature                              |
|-------|--------|-----------------------------|--------------------------------------|
| 00    | 00     | UNALLOCATED                 | -                                    |
| 00    | 01     | PMOV(to vector) -Byte       | FEAT_SVE2p1 &#124;&#124; FEAT_SME2p1 |
| 00    | 1x     | PMOV(to vector) -Halfword   | FEAT_SVE2p1 &#124;&#124; FEAT_SME2p1 |
| 01    | xx     | PMOV(to vector)-Word        | FEAT_SVE2p1 &#124;&#124; FEAT_SME2p1 |
| 1x    | xx     | PMOV(to vector) -Doubleword | FEAT_SVE2p1 &#124;&#124; FEAT_SME2p1 |

## SVE unpack vector elements

The encodings in this section are decoded from SVE Permute Vector - Unpredicated.

<!-- image -->

| 31    | 24 23 22 21 20 19 18 17 16 15   | 10 9 5 4   |
|-------|---------------------------------|------------|
| 0 0 0 | 1 size 1 1 0 0 U H 0 0 1 1 1 Zn | 0 Zd       |

|   U |   H | Instruction Details         | Feature                        |
|-----|-----|-----------------------------|--------------------------------|
|   0 |   0 | SUNPKHI, SUNPKLO -Lowhalf   | FEAT_SVE &#124;&#124; FEAT_SME |
|   0 |   1 | SUNPKHI, SUNPKLO -High half | FEAT_SVE &#124;&#124; FEAT_SME |
|   1 |   0 | UUNPKHI, UUNPKLO-Lowhalf    | FEAT_SVE &#124;&#124; FEAT_SME |
|   1 |   1 | UUNPKHI, UUNPKLO-Highhalf   | FEAT_SVE &#124;&#124; FEAT_SME |

## SVE Permute Predicate

SVE Permute Predicate

The encodings in this section are decoded from SVE encodings.

<!-- image -->

| 31    | 24 23 22 21   |   20 | 16 15 13 12   | 9 8   | 5 4   | 3 0   |
|-------|---------------|------|---------------|-------|-------|-------|
| 0 0 0 | 0 1 op0       |    1 | op1 0 1 0     | op2   | op3   |       |

| op0   | op1   | op2   | op3   | Instruction details            | Feature                        |
|-------|-------|-------|-------|--------------------------------|--------------------------------|
| 00    | 1000x | 0000  | 0     | SVE unpack predicate elements  | -                              |
| xx    | 0xxxx | xxx0  | 0     | SVE permute predicate elements | -                              |
| xx    | 10100 | 0000  | 0     | REV(predicate)                 | FEAT_SVE &#124;&#124; FEAT_SME |
| xx    | 10101 | 0000  | 0     | UNALLOCATED                    | -                              |
| xx    | 10x0x | 0010  | 0     | UNALLOCATED                    | -                              |
| xx    | 10x0x | 01x0  | 0     | UNALLOCATED                    | -                              |
| xx    | 10x0x | 1xx0  | 0     | UNALLOCATED                    | -                              |
| xx    | 10x1x | xxx0  | 0     | UNALLOCATED                    | -                              |
| xx    | 11xxx | xxx0  | 0     | UNALLOCATED                    | -                              |
| xx    | xxxxx | xxx0  | 1     | UNALLOCATED                    | -                              |
| xx    | xxxxx | xxx1  | x     | UNALLOCATED                    | -                              |
| != 00 | 1000x | 0000  | 0     | UNALLOCATED                    | -                              |

## SVE unpack predicate elements

The encodings in this section are decoded from SVE Permute Predicate.

<!-- image -->

|   H | Instruction Details         | Feature                        |
|-----|-----------------------------|--------------------------------|
|   0 | PUNPKHI, PUNPKLO -Lowhalf   | FEAT_SVE &#124;&#124; FEAT_SME |
|   1 | PUNPKHI, PUNPKLO -High half | FEAT_SVE &#124;&#124; FEAT_SME |

## SVE permute predicate elements

The encodings in this section are decoded from SVE Permute Predicate.

<!-- image -->

|   opc | H   | Instruction Details                  | Feature                        |
|-------|-----|--------------------------------------|--------------------------------|
|    00 | 0   | ZIP1, ZIP2 (predicates) -Lowhalves   | FEAT_SVE &#124;&#124; FEAT_SME |
|    00 | 1   | ZIP1, ZIP2 (predicates) -High halves | FEAT_SVE &#124;&#124; FEAT_SME |
|    01 | 0   | UZP1, UZP2 (predicates) -Even        | FEAT_SVE &#124;&#124; FEAT_SME |
|    01 | 1   | UZP1, UZP2 (predicates)-Odd          | FEAT_SVE &#124;&#124; FEAT_SME |
|    10 | 0   | TRN1, TRN2 (predicates) -Even        | FEAT_SVE &#124;&#124; FEAT_SME |
|    10 | 1   | TRN1, TRN2 (predicates)-Odd          | FEAT_SVE &#124;&#124; FEAT_SME |
|    11 | x   | UNALLOCATED                          | -                              |

## SVE Permute Vector - Predicated

SVE Permute Vector - Predicated

The encodings in this section are decoded from SVE encodings.

<!-- image -->

| 31          | 24 23 22 21 20 19 17 16 15 14   |
|-------------|---------------------------------|
| 0 0 0 0 0 1 | 1 1 op0 op1 op2 1 0             |

|   op0 | op1    | op2   | op3   | Instruction details                                   | Feature                              |
|-------|--------|-------|-------|-------------------------------------------------------|--------------------------------------|
|     0 | 000    | 0     | 0     | CPY (SIMD&FP scalar)                                  | FEAT_SVE &#124;&#124; FEAT_SME       |
|     0 | 000    | 1     | 0     | SVE compress Active elements                          | -                                    |
|     0 | 000    | x     | 1     | SVE extract element to general register               | -                                    |
|     0 | 001    | 1     | 1     | UNALLOCATED                                           | -                                    |
|     0 | 001    | x     | 0     | SVE extract element to SIMD&FP scalar register        | -                                    |
|     0 | 01x    | x     | x     | SVE reverse within elements                           | -                                    |
|     0 | 100    | 0     | 1     | CPY (scalar)                                          | FEAT_SVE &#124;&#124; FEAT_SME       |
|     0 | 100    | x     | 0     | SVE conditionally broadcast element to vector         | -                                    |
|     0 | 101    | x     | 0     | SVE conditionally extract element to SIMD&FP scalar   | -                                    |
|     0 | 110    | 0     | 0     | SPLICE -Destructive                                   | FEAT_SVE &#124;&#124; FEAT_SME       |
|     0 | 110    | 0     | 1     | UNALLOCATED                                           | -                                    |
|     0 | 110    | 1     | 0     | SPLICE -Constructive                                  | FEAT_SVE2 &#124;&#124; FEAT_SME      |
|     0 | 111    | 0     | x     | SVE reverse doublewords                               | -                                    |
|     0 | 111    | 1     | 0     | UNALLOCATED                                           | -                                    |
|     0 | 1xx    | 1     | 1     | UNALLOCATED                                           | -                                    |
|     0 | x01    | 0     | 1     | UNALLOCATED                                           | -                                    |
|     1 | 000    | 0     | 0     | UNALLOCATED                                           | -                                    |
|     1 | 000    | 1     | 0     | EXPAND                                                | FEAT_SVE2p2 &#124;&#124; FEAT_SME2p2 |
|     1 | 000    | x     | 1     | SVE conditionally extract element to general register | -                                    |
|     1 | != 000 | x     | x     | UNALLOCATED                                           | -                                    |

## SVE compress Active elements

The encodings in this section are decoded from SVE Permute Vector - Predicated.

<!-- image -->

| 31    | 24 23 19 17 16 15       | 22 21 20 14 13 12 10 9 5 4   |
|-------|-------------------------|------------------------------|
| 0 0 0 | 1 size 1 0 0 0 0 1 1 Pg | 0 0 Zn Zd                    |

| size   | Instruction Details       | Feature                              |
|--------|---------------------------|--------------------------------------|
| 0x     | COMPACT-Byteand halfword  | FEAT_SVE2p2 &#124;&#124; FEAT_SME2p2 |
| 1x     | COMPACT-Wordanddoubleword | FEAT_SVE &#124;&#124; FEAT_SME2p2    |

## SVE extract element to general register

The encodings in this section are decoded from SVE Permute Vector - Predicated.

<!-- image -->

|   B | Instruction Details   | Feature                        |
|-----|-----------------------|--------------------------------|
|   0 | LASTA (scalar)        | FEAT_SVE &#124;&#124; FEAT_SME |
|   1 | LASTB (scalar)        | FEAT_SVE &#124;&#124; FEAT_SME |

## SVE extract element to SIMD\&amp;FP scalar register

The encodings in this section are decoded from SVE Permute Vector - Predicated.

<!-- image -->

|   B | Instruction Details    | Feature                        |
|-----|------------------------|--------------------------------|
|   0 | LASTA (SIMD&FP scalar) | FEAT_SVE &#124;&#124; FEAT_SME |
|   1 | LASTB (SIMD&FP scalar) | FEAT_SVE &#124;&#124; FEAT_SME |

## SVE reverse within elements

The encodings in this section are decoded from SVE Permute Vector - Predicated.

<!-- image -->

|   opc |   Z | Instruction Details                  | Feature                              |
|-------|-----|--------------------------------------|--------------------------------------|
|    00 |   0 | REVB, REVH, REVW-Byte, merging       | FEAT_SVE &#124;&#124; FEAT_SME       |
|    00 |   1 | REVB, REVH, REVW-Byte, zeroing       | FEAT_SVE2p2 &#124;&#124; FEAT_SME2p2 |
|    01 |   0 | REVB, REVH, REVW - Halfword, merging | FEAT_SVE &#124;&#124; FEAT_SME       |

|   opc |   Z | Instruction Details                  | Feature                              |
|-------|-----|--------------------------------------|--------------------------------------|
|    01 |   1 | REVB, REVH, REVW - Halfword, zeroing | FEAT_SVE2p2 &#124;&#124; FEAT_SME2p2 |
|    10 |   0 | REVB, REVH, REVW-Word,merging        | FEAT_SVE &#124;&#124; FEAT_SME       |
|    10 |   1 | REVB, REVH, REVW-Word,zeroing        | FEAT_SVE2p2 &#124;&#124; FEAT_SME2p2 |
|    11 |   0 | RBIT -Merging                        | FEAT_SVE &#124;&#124; FEAT_SME       |
|    11 |   1 | RBIT -Zeroing                        | FEAT_SVE2p2 &#124;&#124; FEAT_SME2p2 |

## SVE conditionally broadcast element to vector

The encodings in this section are decoded from SVE Permute Vector - Predicated.

<!-- image -->

|   B | Instruction Details   | Feature                        |
|-----|-----------------------|--------------------------------|
|   0 | CLASTA (vectors)      | FEAT_SVE &#124;&#124; FEAT_SME |
|   1 | CLASTB (vectors)      | FEAT_SVE &#124;&#124; FEAT_SME |

## SVE conditionally extract element to SIMD\&amp;FP scalar

The encodings in this section are decoded from SVE Permute Vector - Predicated.

<!-- image -->

|   B | Instruction Details     | Feature                        |
|-----|-------------------------|--------------------------------|
|   0 | CLASTA (SIMD&FP scalar) | FEAT_SVE &#124;&#124; FEAT_SME |
|   1 | CLASTB (SIMD&FP scalar) | FEAT_SVE &#124;&#124; FEAT_SME |

## SVE reverse doublewords

The encodings in this section are decoded from SVE Permute Vector - Predicated.

<!-- image -->

| size   | Z   | Instruction Details   | Feature                              |
|--------|-----|-----------------------|--------------------------------------|
| 00     | 0   | REVD-Merging          | FEAT_SME &#124;&#124; FEAT_SVE2p1    |
| 00     | 1   | REVD-Zeroing          | FEAT_SVE2p2 &#124;&#124; FEAT_SME2p2 |
| != 00  | x   | UNALLOCATED           | -                                    |

## SVE conditionally extract element to general register

The encodings in this section are decoded from SVE Permute Vector - Predicated.

<!-- image -->

|   B | Instruction Details   | Feature                        |
|-----|-----------------------|--------------------------------|
|   0 | CLASTA (scalar)       | FEAT_SVE &#124;&#124; FEAT_SME |
|   1 | CLASTB (scalar)       | FEAT_SVE &#124;&#124; FEAT_SME |

## SVE Integer Compare - Vectors

SVE Integer Compare - Vectors

The encodings in this section are decoded from SVE encodings.

<!-- image -->

|   31 | 25 24       |   23 |   22 21 | 15 14 13   |
|------|-------------|------|---------|------------|
|    0 | 0 1 0 0 1 0 |    0 |       0 | op0        |

|   op0 | Instruction details                    |
|-------|----------------------------------------|
|     0 | SVE integer compare vectors            |
|     1 | SVE integer compare with wide elements |

## SVE integer compare vectors

The encodings in this section are decoded from SVE Integer Compare - Vectors.

<!-- image -->

## SVE Propagate Break

SVE Propagate Break

The encodings in this section are decoded from SVE encodings.

<!-- image -->

|   op |   o2 |   ne | Instruction Details                          | Feature                        |
|------|------|------|----------------------------------------------|--------------------------------|
|    0 |    0 |    0 | CMP < cc > (vectors) -Higher or same         | FEAT_SVE &#124;&#124; FEAT_SME |
|    0 |    0 |    1 | CMP < cc > (vectors) -Higher                 | FEAT_SVE &#124;&#124; FEAT_SME |
|    0 |    1 |    0 | CMP < cc > (wide elements) -Equal            | FEAT_SVE &#124;&#124; FEAT_SME |
|    0 |    1 |    1 | CMP < cc > (wide elements) -Notequal         | FEAT_SVE &#124;&#124; FEAT_SME |
|    1 |    0 |    0 | CMP < cc > (vectors) - Greater than or equal | FEAT_SVE &#124;&#124; FEAT_SME |
|    1 |    0 |    1 | CMP < cc > (vectors) -Greater than           | FEAT_SVE &#124;&#124; FEAT_SME |
|    1 |    1 |    0 | CMP < cc > (vectors) -Equal                  | FEAT_SVE &#124;&#124; FEAT_SME |
|    1 |    1 |    1 | CMP < cc > (vectors) -Notequal               | FEAT_SVE &#124;&#124; FEAT_SME |

## SVE integer compare with wide elements

The encodings in this section are decoded from SVE Integer Compare - Vectors.

<!-- image -->

| 31    | 24 23 22 21 20   | 16 15 14 13   | 12 10 9 5 4 3   |
|-------|------------------|---------------|-----------------|
| 0 0 1 | 0 size 0         | U 1 lt Pg     | Zn ne Pd        |

|   U |   lt |   ne | Instruction Details                                | Feature                        |
|-----|------|------|----------------------------------------------------|--------------------------------|
|   0 |    0 |    0 | CMP < cc > (wide elements) - Greater than or equal | FEAT_SVE &#124;&#124; FEAT_SME |
|   0 |    0 |    1 | CMP < cc > (wide elements) - Greater than          | FEAT_SVE &#124;&#124; FEAT_SME |
|   0 |    1 |    0 | CMP < cc > (wide elements) -Less than              | FEAT_SVE &#124;&#124; FEAT_SME |
|   0 |    1 |    1 | CMP < cc > (wide elements) - Less than or equal    | FEAT_SVE &#124;&#124; FEAT_SME |
|   1 |    0 |    0 | CMP < cc > (wide elements) -Higher or same         | FEAT_SVE &#124;&#124; FEAT_SME |
|   1 |    0 |    1 | CMP < cc > (wide elements) -Higher                 | FEAT_SVE &#124;&#124; FEAT_SME |
|   1 |    1 |    0 | CMP < cc > (wide elements) -Lower                  | FEAT_SVE &#124;&#124; FEAT_SME |
|   1 |    1 |    1 | CMP < cc > (wide elements) - Lower or same         | FEAT_SVE &#124;&#124; FEAT_SME |

## SVE propagate break from previous partition

The encodings in this section are decoded from SVE Propagate Break.

<!-- image -->

|   op | S   | B   | Instruction Details   | Feature                        |
|------|-----|-----|-----------------------|--------------------------------|
|    0 | 0   | 0   | BRKPA                 | FEAT_SVE &#124;&#124; FEAT_SME |
|    0 | 0   | 1   | BRKPB                 | FEAT_SVE &#124;&#124; FEAT_SME |
|    0 | 1   | 0   | BRKPAS                | FEAT_SVE &#124;&#124; FEAT_SME |
|    0 | 1   | 1   | BRKPBS                | FEAT_SVE &#124;&#124; FEAT_SME |
|    1 | x   | x   | UNALLOCATED           | -                              |

## SVE Partition Break

SVE Partition Break

The encodings in this section are decoded from SVE encodings.

<!-- image -->

| op0   | op1   | op2   | op3   | Instruction details                   |
|-------|-------|-------|-------|---------------------------------------|
| 0     | 1000  | 0     | 0     | SVE propagate break to next partition |
| 0     | 1000  | 0     | 1     | UNALLOCATED                           |
| 1     | 1000  | 0     | x     | UNALLOCATED                           |
| x     | 0000  | 0     | x     | SVE partition break condition         |
| x     | x000  | 1     | x     | UNALLOCATED                           |
| x     | x001  | x     | x     | UNALLOCATED                           |
| x     | x01x  | x     | x     | UNALLOCATED                           |

|   op0 | Instruction details                         |
|-------|---------------------------------------------|
|     0 | SVE propagate break from previous partition |
|     1 | UNALLOCATED                                 |

## SVE propagate break to next partition

The encodings in this section are decoded from SVE Partition Break.

<!-- image -->

|   S | Instruction Details   | Feature                        |
|-----|-----------------------|--------------------------------|
|   0 | BRKN                  | FEAT_SVE &#124;&#124; FEAT_SME |
|   1 | BRKNS                 | FEAT_SVE &#124;&#124; FEAT_SME |

## SVE partition break condition

The encodings in this section are decoded from SVE Partition Break.

<!-- image -->

| B   |   S | M   | Instruction Details   | Feature                        |
|-----|-----|-----|-----------------------|--------------------------------|
| x   |   1 | 1   | UNALLOCATED           | -                              |
| 0   |   0 | x   | BRKA                  | FEAT_SVE &#124;&#124; FEAT_SME |
| 0   |   1 | 0   | BRKAS                 | FEAT_SVE &#124;&#124; FEAT_SME |
| 1   |   0 | x   | BRKB                  | FEAT_SVE &#124;&#124; FEAT_SME |
| 1   |   1 | 0   | BRKBS                 | FEAT_SVE &#124;&#124; FEAT_SME |

## SVE Predicate Misc

SVE Predicate Misc

The encodings in this section are decoded from SVE encodings.

<!-- image -->

| op0   | op1   | op2   | op3   | Instruction details   |
|-------|-------|-------|-------|-----------------------|
| x     | x1xx  | x     | x     | UNALLOCATED           |

| op0   | op1   | op2   | op3     | op4   | Instruction details                     |      |     | Feature                        |
|-------|-------|-------|---------|-------|-----------------------------------------|------|-----|--------------------------------|
| 0000  | xxx   | x0    | xxxx    | 0     | SVE predicate test                      |      |     | -                              |
| 0000  | xxx   | x1    | xxxx    | 0     | UNALLOCATED                             |      |     | -                              |
| 0001  | xxx   | xx    | xxxx    | 0     | UNALLOCATED                             |      |     | -                              |
| 1000  | 000   | 00    | xxxx    | 0     | SVE predicate first active              |      |     | -                              |
| 1000  | 000   | 10    | xxxx    | 0     | UNALLOCATED                             |      |     | -                              |
| 1000  | 100   | 10    | 0000    | 0     | SVE predicate zero                      |      |     | -                              |
| 1000  | 100   | 10    | != 0000 | 0     | UNALLOCATED                             |      |     | -                              |
| 1000  | 110   | 00    | xxxx    | 0     | SVEpredicate read from FFR (predicated) |      |     | -                              |
| 1001  | 000   | 00    | xxxx    | 0     | UNALLOCATED                             |      |     | -                              |
| 1001  | 000   | 10    | xxxx    | 0     | PNEXT                                   |      |     | FEAT_SVE &#124;&#124; FEAT_SME |
| 1001  | 100   | 10    | xxxx    | 0     | UNALLOCATED                             |      |     | -                              |
| 1001  | 110   | 00    | 0000    | 0     | SVE predicate read (unpredicated)       | from | FFR | -                              |
| 1001  | 110   | 00    | != 0000 | 0     | UNALLOCATED                             |      |     | -                              |
| 100x  | 010   | x0    | xxxx    | 0     | UNALLOCATED                             |      |     | -                              |
| 100x  | 0x0   | x1    | xxxx    | 0     | UNALLOCATED                             |      |     | -                              |
| 100x  | 100   | 0x    | xxxx    | 0     | SVE predicate initialize                |      |     | -                              |
| 100x  | 100   | 11    | xxxx    | 0     | UNALLOCATED                             |      |     | -                              |
| 100x  | 110   | != 00 | xxxx    | 0     | UNALLOCATED                             |      |     | -                              |
| 100x  | xx1   | xx    | xxxx    | 0     | UNALLOCATED                             |      |     | -                              |
| x00x  | xxx   | xx    | xxxx    | 1     | UNALLOCATED                             |      |     | -                              |
| x01x  | xxx   | xx    | xxxx    | x     | UNALLOCATED                             |      |     | -                              |
| x1xx  | xxx   | xx    | xxxx    | x     | UNALLOCATED                             |      |     | -                              |

## SVE predicate test

The encodings in this section are decoded from SVE Predicate Misc.

<!-- image -->

|   op | S opc2    | Instruction Details   | Feature                        |
|------|-----------|-----------------------|--------------------------------|
|    0 | 0 xxxx    | UNALLOCATED           | -                              |
|    0 | 1 0000    | PTEST                 | FEAT_SVE &#124;&#124; FEAT_SME |
|    0 | 1 != 0000 | UNALLOCATED           | -                              |
|    1 | x xxxx    | UNALLOCATED           | -                              |

## SVE predicate first active

The encodings in this section are decoded from SVE Predicate Misc.

<!-- image -->

| 31 24 23 22 21 20 19   | 16 15 14 13 11             | 10 9 8 5 4   |    |   3 | 0   |
|------------------------|----------------------------|--------------|----|-----|-----|
| 0 0 1 0 0 1 0          | 1 op S 0 1 1 0 0 0 1 1 0 0 | 0 0 0        | Pg |   0 | Pdn |

|   op | S   | Instruction Details   | Feature                        |
|------|-----|-----------------------|--------------------------------|
|    0 | 0   | UNALLOCATED           | -                              |
|    0 | 1   | PFIRST                | FEAT_SVE &#124;&#124; FEAT_SME |
|    1 | x   | UNALLOCATED           | -                              |

## SVE predicate zero

The encodings in this section are decoded from SVE Predicate Misc.

<!-- image -->

| 31    | 24 23 22 21 20 19 16 15 14 13 11 10 9 8 5 4 3   |
|-------|-------------------------------------------------|
| 0 0 1 | 1 op S 0 1 1 0 0 0 1 1 1 0 0 1 0 0 0 0 0 0 Pd   |

|   op | S   | Instruction Details   | Feature                        |
|------|-----|-----------------------|--------------------------------|
|    0 | 0   | PFALSE                | FEAT_SVE &#124;&#124; FEAT_SME |
|    0 | 1   | UNALLOCATED           | -                              |
|    1 | x   | UNALLOCATED           | -                              |

## SVE predicate read from FFR (predicated)

The encodings in this section are decoded from SVE Predicate Misc.

<!-- image -->

| 31   | 24 23 22 21 20 19 16         | 15 14 13 11 10 9 8 5 4 3   |
|------|------------------------------|----------------------------|
| 0 0  | 1 op S 0 1 1 0 0 0 1 1 1 1 0 | 0 0 0 Pg Pd                |

## SVE predicate initialize

The encodings in this section are decoded from SVE Predicate Misc.

<!-- image -->

|   S | Instruction Details   | Feature                        |
|-----|-----------------------|--------------------------------|
|   0 | PTRUE (predicate)     | FEAT_SVE &#124;&#124; FEAT_SME |
|   1 | PTRUES                | FEAT_SVE &#124;&#124; FEAT_SME |

## SVE Predicate Count

SVE Predicate Count

The encodings in this section are decoded from SVE encodings.

<!-- image -->

|   op | S   | Instruction Details   | Feature   |
|------|-----|-----------------------|-----------|
|    0 | 0   | RDFFR (predicated)    | FEAT_SVE  |
|    0 | 1   | RDFFRS                | FEAT_SVE  |
|    1 | x   | UNALLOCATED           | -         |

## SVE predicate read from FFR (unpredicated)

The encodings in this section are decoded from SVE Predicate Misc.

<!-- image -->

|   op | S   | Instruction Details   | Feature   |
|------|-----|-----------------------|-----------|
|    0 | 0   | RDFFR (unpredicated)  | FEAT_SVE  |
|    0 | 1   | UNALLOCATED           | -         |
|    1 | x   | UNALLOCATED           | -         |

## SVE predicate count (predicate-as-counter)

The encodings in this section are decoded from SVE Predicate Count.

<!-- image -->

| opc    | Instruction Details         | Feature                            |
|--------|-----------------------------|------------------------------------|
| 000    | CNTP (predicate as counter) | FEAT_SME2 &#124;&#124; FEAT_SVE2p1 |
| != 000 | UNALLOCATED                 | -                                  |

## SVE predicate count

The encodings in this section are decoded from SVE Predicate Count.

<!-- image -->

| 31   | 24 23 22 21 19   | 18   | 16 15 14   | 13 10   |   9 8 | 5 4   | 0   |
|------|------------------|------|------------|---------|-------|-------|-----|
| 0 0  | 1 size           | 1 0  | 0 opc      | 1 0 Pg  |     0 | Pn    | Rd  |

| opc   | Instruction Details   | Feature                              |
|-------|-----------------------|--------------------------------------|
| 000   | CNTP (predicate)      | FEAT_SVE &#124;&#124; FEAT_SME       |
| 001   | FIRSTP                | FEAT_SVE2p2 &#124;&#124; FEAT_SME2p2 |
| 010   | LASTP                 | FEAT_SVE2p2 &#124;&#124; FEAT_SME2p2 |
| 011   | UNALLOCATED           | -                                    |
| 1xx   | UNALLOCATED           | -                                    |

| op0    |   op1 | Instruction details                         |
|--------|-------|---------------------------------------------|
| 000    |     1 | SVE predicate count (predicate-as- counter) |
| xxx    |     0 | SVE predicate count                         |
| != 000 |     1 | UNALLOCATED                                 |

## SVE Inc/Dec by Predicate Count

SVE Inc/Dec by Predicate Count

The encodings in this section are decoded from SVE encodings.

<!-- image -->

|   op0 |   op1 | Instruction details                                |
|-------|-------|----------------------------------------------------|
|     0 |     0 | SVE saturating inc/dec vector by predicate count   |
|     0 |     1 | SVE saturating inc/dec register by predicate count |
|     1 |     0 | SVE inc/dec vector by predicate count              |
|     1 |     1 | SVE inc/dec register by predicate count            |

## SVE saturating inc/dec vector by predicate count

The encodings in this section are decoded from SVE Inc/Dec by Predicate Count.

<!-- image -->

| D   | U   | opc   | Instruction Details   | Feature                        |
|-----|-----|-------|-----------------------|--------------------------------|
| x   | x   | != 00 | UNALLOCATED           | -                              |
| 0   | 0   | 00    | SQINCP (vector)       | FEAT_SVE &#124;&#124; FEAT_SME |
| 0   | 1   | 00    | UQINCP (vector)       | FEAT_SVE &#124;&#124; FEAT_SME |
| 1   | 0   | 00    | SQDECP (vector)       | FEAT_SVE &#124;&#124; FEAT_SME |
| 1   | 1   | 00    | UQDECP(vector)        | FEAT_SVE &#124;&#124; FEAT_SME |

## SVE saturating inc/dec register by predicate count

The encodings in this section are decoded from SVE Inc/Dec by Predicate Count.

<!-- image -->

| D   | U   | sf   |   op | Instruction Details     | Feature                        |
|-----|-----|------|------|-------------------------|--------------------------------|
| x   | x   | x    |    1 | UNALLOCATED             | -                              |
| 0   | 0   | 0    |    0 | SQINCP (scalar) -32-bit | FEAT_SVE &#124;&#124; FEAT_SME |
| 0   | 0   | 1    |    0 | SQINCP (scalar) -64-bit | FEAT_SVE &#124;&#124; FEAT_SME |
| 0   | 1   | 0    |    0 | UQINCP (scalar) -32-bit | FEAT_SVE &#124;&#124; FEAT_SME |
| 0   | 1   | 1    |    0 | UQINCP (scalar) -64-bit | FEAT_SVE &#124;&#124; FEAT_SME |
| 1   | 0   | 0    |    0 | SQDECP (scalar) -32-bit | FEAT_SVE &#124;&#124; FEAT_SME |
| 1   | 0   | 1    |    0 | SQDECP (scalar) -64-bit | FEAT_SVE &#124;&#124; FEAT_SME |
| 1   | 1   | 0    |    0 | UQDECP(scalar) -32-bit  | FEAT_SVE &#124;&#124; FEAT_SME |
| 1   | 1   | 1    |    0 | UQDECP(scalar) -64-bit  | FEAT_SVE &#124;&#124; FEAT_SME |

## SVE inc/dec vector by predicate count

The encodings in this section are decoded from SVE Inc/Dec by Predicate Count.

<!-- image -->

|   op | D   | opc2   | Instruction Details   | Feature                        |
|------|-----|--------|-----------------------|--------------------------------|
|    0 | x   | != 00  | UNALLOCATED           | -                              |
|    0 | 0   | 00     | INCP (vector)         | FEAT_SVE &#124;&#124; FEAT_SME |
|    0 | 1   | 00     | DECP (vector)         | FEAT_SVE &#124;&#124; FEAT_SME |
|    1 | x   | xx     | UNALLOCATED           | -                              |

## SVE inc/dec register by predicate count

The encodings in this section are decoded from SVE Inc/Dec by Predicate Count.

<!-- image -->

|   op | D   | opc2   | Instruction Details   | Feature   |
|------|-----|--------|-----------------------|-----------|
|    0 | x   | != 00  | UNALLOCATED           | -         |

## SVE Write FFR

SVE Write FFR

The encodings in this section are decoded from SVE encodings.

<!-- image -->

| op0   | op1   | op2    | op3     | op4      | Instruction details          |
|-------|-------|--------|---------|----------|------------------------------|
| 0     | 00    | 000    | xxxx    | 00000    | SVE FFR write from predicate |
| 1     | 00    | 000    | 0000    | 00000    | SVE FFR initialise           |
| 1     | 00    | 000    | != 0000 | 00000    | UNALLOCATED                  |
| x     | 00    | 000    | xxxx    | != 00000 | UNALLOCATED                  |
| x     | 00    | != 000 | xxxx    | xxxxx    | UNALLOCATED                  |
| x     | != 00 | xxx    | xxxx    | xxxxx    | UNALLOCATED                  |

## SVE FFR write from predicate

The encodings in this section are decoded from SVE Write FFR.

<!-- image -->

| opc   | Instruction Details   | Feature   |
|-------|-----------------------|-----------|
| 00    | WRFFR                 | FEAT_SVE  |
| != 00 | UNALLOCATED           | -         |

## SVE FFR initialise

The encodings in this section are decoded from SVE Write FFR.

|   op | D   | opc2   | Instruction Details   | Feature                        |
|------|-----|--------|-----------------------|--------------------------------|
|    0 | 0   | 00     | INCP (scalar)         | FEAT_SVE &#124;&#124; FEAT_SME |
|    0 | 1   | 00     | DECP (scalar)         | FEAT_SVE &#124;&#124; FEAT_SME |
|    1 | x   | xx     | UNALLOCATED           | -                              |

<!-- image -->

| opc   | Instruction Details   | Feature   |
|-------|-----------------------|-----------|
| 00    | SETFFR                | FEAT_SVE  |
| != 00 | UNALLOCATED           | -         |

## SVE Integer Compare - Scalars

SVE Integer Compare - Scalars

The encodings in this section are decoded from SVE encodings.

<!-- image -->

| op0   | op1   | op2     | Instruction details                       |
|-------|-------|---------|-------------------------------------------|
| 0x    | xx    | xxxx    | SVEinteger compare scalar count and limit |
| 10    | 00    | 0000    | SVE conditionally terminate scalars       |
| 10    | 00    | != 0000 | UNALLOCATED                               |
| 11    | 00    | xxxx    | SVE pointer conflict compare              |
| 1x    | != 00 | xxxx    | UNALLOCATED                               |

## SVE integer compare scalar count and limit

The encodings in this section are decoded from SVE Integer Compare - Scalars.

<!-- image -->

|   U |   lt | Instruction Details   | Feature                         |
|-----|------|-----------------------|---------------------------------|
|   0 |    0 | WHILEGE (predicate)   | FEAT_SVE2 &#124;&#124; FEAT_SME |
|   0 |    0 | WHILEGT (predicate)   | FEAT_SVE2 &#124;&#124; FEAT_SME |
|   0 |    1 | WHILELT (predicate)   | FEAT_SVE FEAT_SME               |

||

|   U |   lt | eq        | Instruction Details   | Feature                         |
|-----|------|-----------|-----------------------|---------------------------------|
|   0 |    1 | 1 WHILELE | (predicate)           | FEAT_SVE &#124;&#124; FEAT_SME  |
|   1 |    0 | 0         | WHILEHS (predicate)   | FEAT_SVE2 &#124;&#124; FEAT_SME |
|   1 |    0 | 1 WHILEHI | (predicate)           | FEAT_SVE2 &#124;&#124; FEAT_SME |
|   1 |    1 | 0         | WHILELO (predicate)   | FEAT_SVE &#124;&#124; FEAT_SME  |
|   1 |    1 | 1         | WHILELS (predicate)   | FEAT_SVE &#124;&#124; FEAT_SME  |

## SVE conditionally terminate scalars

The encodings in this section are decoded from SVE Integer Compare - Scalars.

<!-- image -->

| 31    | 24 23 22 21 20 16 15 14 13 12 11 10 9 5 4 3 0   |
|-------|-------------------------------------------------|
| 0 0 1 | 1 op sz 1 Rm 0 0 1 0 0 0 Rn ne 0 0 0 0          |

|   op | ne   | Instruction Details       | Feature                        |
|------|------|---------------------------|--------------------------------|
|    0 | x    | UNALLOCATED               | -                              |
|    1 | 0    | CTERMEQ, CTERMNE-Equal    | FEAT_SVE &#124;&#124; FEAT_SME |
|    1 | 1    | CTERMEQ, CTERMNE-Notequal | FEAT_SVE &#124;&#124; FEAT_SME |

## SVE pointer conflict compare

The encodings in this section are decoded from SVE Integer Compare - Scalars.

<!-- image -->

|   rw | Instruction Details   | Feature                         |
|------|-----------------------|---------------------------------|
|    0 | WHILEWR               | FEAT_SVE2 &#124;&#124; FEAT_SME |
|    1 | WHILERW               | FEAT_SVE2 &#124;&#124; FEAT_SME |

## SVE Scalar Integer Compare - Predicate-as-counter

SVE Scalar Integer Compare - Predicate-as-counter

The encodings in this section are decoded from SVE encodings.

<!-- image -->

| 31    | 24 23 22 21   |   20 | 16 15 14 13   | 11   |     | 5 4 3 2   |
|-------|---------------|------|---------------|------|-----|-----------|
| 0 0 1 | 1 0 1         |    1 | 0 1           | op1  | op2 | 1 op3     |

| op0      | op1   | op2       | op3   | Instruction details                                              | Feature                            |
|----------|-------|-----------|-------|------------------------------------------------------------------|------------------------------------|
| 00000    | 110   | xxxxxx    | x     | SVE extract mask predicate from predicate-as-counter             | -                                  |
| 00000    | 111   | 000000    | 0     | PTRUE (predicate as counter)                                     | FEAT_SME2 &#124;&#124; FEAT_SVE2p1 |
| 00000    | 111   | 000000    | 1     | UNALLOCATED                                                      | -                                  |
| 00000    | 111   | != 000000 | x     | UNALLOCATED                                                      | -                                  |
| xxxxx    | 01x   | xxxxxx    | x     | SVEinteger compare scalar count and limit (predicate pair)       | -                                  |
| xxxxx    | x0x   | xxxxxx    | x     | SVEinteger compare scalar count and limit (predicate-as-counter) | -                                  |
| != 00000 | 11x   | xxxxxx    | x     | UNALLOCATED                                                      | -                                  |

## SVE extract mask predicate from predicate-as-counter

The encodings in this section are decoded from SVE Scalar Integer Compare - Predicate-as-counter.

<!-- image -->

| opc   | Instruction Details   | Feature                            |
|-------|-----------------------|------------------------------------|
| 0xx   | PEXT (predicate)      | FEAT_SME2 &#124;&#124; FEAT_SVE2p1 |
| 10x   | PEXT (predicate pair) | FEAT_SME2 &#124;&#124; FEAT_SVE2p1 |
| 11x   | UNALLOCATED           | -                                  |

## SVE integer compare scalar count and limit (predicate pair)

The encodings in this section are decoded from SVE Scalar Integer Compare - Predicate-as-counter.

<!-- image -->

| 31    | 24 23 22 21 20 16 15 12 11 10 9   |
|-------|-----------------------------------|
| 0 0 1 | 1 size 1 Rm 0 1 0 1 U lt Rn       |

|   U |   lt |   eq | Instruction Details      | Feature                            |
|-----|------|------|--------------------------|------------------------------------|
|   0 |    0 |    0 | WHILEGE (predicate pair) | FEAT_SME2 &#124;&#124; FEAT_SVE2p1 |
|   0 |    0 |    1 | WHILEGT (predicate pair) | FEAT_SME2 &#124;&#124; FEAT_SVE2p1 |

|   U |   lt |   eq | Instruction Details      | Feature                            |
|-----|------|------|--------------------------|------------------------------------|
|   0 |    1 |    0 | WHILELT (predicate pair) | FEAT_SME2 &#124;&#124; FEAT_SVE2p1 |
|   0 |    1 |    1 | WHILELE (predicate pair) | FEAT_SME2 &#124;&#124; FEAT_SVE2p1 |
|   1 |    0 |    0 | WHILEHS (predicate pair) | FEAT_SME2 &#124;&#124; FEAT_SVE2p1 |
|   1 |    0 |    1 | WHILEHI (predicate pair) | FEAT_SME2 &#124;&#124; FEAT_SVE2p1 |
|   1 |    1 |    0 | WHILELO (predicate pair) | FEAT_SME2 &#124;&#124; FEAT_SVE2p1 |
|   1 |    1 |    1 | WHILELS (predicate pair) | FEAT_SME2 &#124;&#124; FEAT_SVE2p1 |

## SVE integer compare scalar count and limit (predicate-as-counter)

The encodings in this section are decoded from SVE Scalar Integer Compare - Predicate-as-counter.

<!-- image -->

| 31    | 24 23 22 21 20 16 15 14 13 12 11 10 9 5 4 3   |
|-------|-----------------------------------------------|
| 0 0 1 | 1 size 1 Rm 0 1 vl 0 U lt Rn 1 eq             |

|   U |   lt |   eq | Instruction Details            | Feature                            |
|-----|------|------|--------------------------------|------------------------------------|
|   0 |    0 |    0 | WHILEGE (predicate as counter) | FEAT_SME2 &#124;&#124; FEAT_SVE2p1 |
|   0 |    0 |    1 | WHILEGT (predicate as counter) | FEAT_SME2 &#124;&#124; FEAT_SVE2p1 |
|   0 |    1 |    0 | WHILELT (predicate as counter) | FEAT_SME2 &#124;&#124; FEAT_SVE2p1 |
|   0 |    1 |    1 | WHILELE (predicate as counter) | FEAT_SME2 &#124;&#124; FEAT_SVE2p1 |
|   1 |    0 |    0 | WHILEHS (predicate as counter) | FEAT_SME2 &#124;&#124; FEAT_SVE2p1 |
|   1 |    0 |    1 | WHILEHI (predicate as counter) | FEAT_SME2 &#124;&#124; FEAT_SVE2p1 |
|   1 |    1 |    0 | WHILELO (predicate as counter) | FEAT_SME2 &#124;&#124; FEAT_SVE2p1 |
|   1 |    1 |    1 | WHILELS (predicate as counter) | FEAT_SME2 &#124;&#124; FEAT_SVE2p1 |

## SVE Integer Wide Immediate - Unpredicated

SVE Integer Wide Immediate - Unpredicated

The encodings in this section are decoded from SVE encodings.

<!-- image -->

| 31    | 23 22 21 20 19 18 17 16 15 14   |
|-------|---------------------------------|
| 0 0 1 | 1 op0 op1 1 1                   |

|   op0 | op1   | Instruction details                               |
|-------|-------|---------------------------------------------------|
|    00 | x     | SVE integer add/subtract immediate (unpredicated) |

## SVE integer add/subtract immediate (unpredicated)

The encodings in this section are decoded from SVE Integer Wide Immediate - Unpredicated.

<!-- image -->

|   opc | Instruction Details   | Feature                        |
|-------|-----------------------|--------------------------------|
|   000 | ADD(immediate)        | FEAT_SVE &#124;&#124; FEAT_SME |
|   001 | SUB (immediate)       | FEAT_SVE &#124;&#124; FEAT_SME |
|   010 | UNALLOCATED           | -                              |
|   011 | SUBR (immediate)      | FEAT_SVE &#124;&#124; FEAT_SME |
|   100 | SQADD(immediate)      | FEAT_SVE &#124;&#124; FEAT_SME |
|   101 | UQADD(immediate)      | FEAT_SVE &#124;&#124; FEAT_SME |
|   110 | SQSUB (immediate)     | FEAT_SVE &#124;&#124; FEAT_SME |
|   111 | UQSUB(immediate)      | FEAT_SVE &#124;&#124; FEAT_SME |

## SVE integer min/max immediate (unpredicated)

The encodings in this section are decoded from SVE Integer Wide Immediate - Unpredicated.

<!-- image -->

| opc   |   o2 | Instruction Details   | Feature                        |
|-------|------|-----------------------|--------------------------------|
| 0xx   |    1 | UNALLOCATED           | -                              |
| 000   |    0 | SMAX(immediate)       | FEAT_SVE &#124;&#124; FEAT_SME |

|   op0 | op1   | Instruction details                                   |
|-------|-------|-------------------------------------------------------|
|    01 | x     | SVE integer min/max immediate (unpredicated)          |
|    10 | x     | SVE integer multiply immediate (unpredicated)         |
|    11 | 0     | SVE broadcast integer immediate (unpredicated)        |
|    11 | 1     | SVE broadcast floating-point immediate (unpredicated) |

| opc   | o2   | Instruction Details   | Feature                        |
|-------|------|-----------------------|--------------------------------|
| 001   | 0    | UMAX(immediate)       | FEAT_SVE &#124;&#124; FEAT_SME |
| 010   | 0    | SMIN (immediate)      | FEAT_SVE &#124;&#124; FEAT_SME |
| 011   | 0    | UMIN(immediate)       | FEAT_SVE &#124;&#124; FEAT_SME |
| 1xx   | x    | UNALLOCATED           | -                              |

## SVE integer multiply immediate (unpredicated)

The encodings in this section are decoded from SVE Integer Wide Immediate - Unpredicated.

<!-- image -->

| opc    | o2   | Instruction Details   | Feature                        |
|--------|------|-----------------------|--------------------------------|
| 000    | 0    | MUL(immediate)        | FEAT_SVE &#124;&#124; FEAT_SME |
| 000    | 1    | UNALLOCATED           | -                              |
| != 000 | x    | UNALLOCATED           | -                              |

## SVE broadcast integer immediate (unpredicated)

The encodings in this section are decoded from SVE Integer Wide Immediate - Unpredicated.

<!-- image -->

| opc   | Instruction Details   | Feature                        |
|-------|-----------------------|--------------------------------|
| 00    | DUP(immediate)        | FEAT_SVE &#124;&#124; FEAT_SME |
| != 00 | UNALLOCATED           | -                              |

## SVE broadcast floating-point immediate (unpredicated)

The encodings in this section are decoded from SVE Integer Wide Immediate - Unpredicated.

<!-- image -->

| opc   | o2   | Instruction Details   | Feature                        |
|-------|------|-----------------------|--------------------------------|
| 00    | 0    | FDUP                  | FEAT_SVE &#124;&#124; FEAT_SME |
| 00    | 1    | UNALLOCATED           | -                              |
| != 00 | x    | UNALLOCATED           | -                              |

## SVE Integer Multiply-Add - Unpredicated

SVE Integer Multiply-Add - Unpredicated

The encodings in this section are decoded from SVE encodings.

<!-- image -->

| 31   | 24 23 22 21 20 16 15 14   |
|------|---------------------------|
| 0 1  | 0 0 0 op0                 |

| op0   | Instruction details                           | Feature                         |
|-------|-----------------------------------------------|---------------------------------|
| 0000x | SVE integer dot product (unpredicated)        | -                               |
| 0001x | SVE2 saturating multiply-add interleaved long | -                               |
| 001xx | CDOT(vectors)                                 | FEAT_SVE2 &#124;&#124; FEAT_SME |
| 01xxx | SVE2 complex integer multiply-add             | -                               |
| 10xxx | SVE2 integer multiply-add long                | -                               |
| 110xx | SVE2 saturating multiply-add long             | -                               |
| 1110x | SVE2 saturating multiply-add high             | -                               |
| 11110 | SVE mixed sign dot product                    | -                               |
| 11111 | UNALLOCATED                                   | -                               |

## SVE integer dot product (unpredicated)

The encodings in this section are decoded from SVE Integer Multiply-Add - Unpredicated.

<!-- image -->

| size   | U   | Instruction Details   | Feature                        |
|--------|-----|-----------------------|--------------------------------|
| 0x     | x   | UNALLOCATED           | -                              |
| 1x     | 0   | SDOT (4-way, vectors) | FEAT_SVE &#124;&#124; FEAT_SME |

| size   | U Instruction Details   | Feature                        |
|--------|-------------------------|--------------------------------|
| 1x     | 1 UDOT(4-way, vectors)  | FEAT_SVE &#124;&#124; FEAT_SME |

## SVE2 saturating multiply-add interleaved long

The encodings in this section are decoded from SVE Integer Multiply-Add - Unpredicated.

<!-- image -->

|   S | Instruction Details   | Feature                         |
|-----|-----------------------|---------------------------------|
|   0 | SQDMLALBT             | FEAT_SVE2 &#124;&#124; FEAT_SME |
|   1 | SQDMLSLBT             | FEAT_SVE2 &#124;&#124; FEAT_SME |

## SVE2 complex integer multiply-add

The encodings in this section are decoded from SVE Integer Multiply-Add - Unpredicated.

<!-- image -->

|   op | Instruction Details   | Feature                         |
|------|-----------------------|---------------------------------|
|    0 | CMLA(vectors)         | FEAT_SVE2 &#124;&#124; FEAT_SME |
|    1 | SQRDCMLAH(vectors)    | FEAT_SVE2 &#124;&#124; FEAT_SME |

## SVE2 integer multiply-add long

The encodings in this section are decoded from SVE Integer Multiply-Add - Unpredicated.

<!-- image -->

|   S |   U | T                 | Instruction Details   | Feature                         |
|-----|-----|-------------------|-----------------------|---------------------------------|
|   0 |   0 | 0 SMLALB(vectors) |                       | FEAT_SVE2 &#124;&#124; FEAT_SME |
|   0 |   0 | 1                 | SMLALT (vectors)      | FEAT_SVE2 &#124;&#124; FEAT_SME |
|   0 |   1 | 0                 | UMLALB(vectors)       | FEAT_SVE2 &#124;&#124; FEAT_SME |
|   0 |   1 | 1                 | UMLALT(vectors)       | FEAT_SVE2 &#124;&#124; FEAT_SME |
|   1 |   0 | 0                 | SMLSLB (vectors)      | FEAT_SVE2 &#124;&#124; FEAT_SME |
|   1 |   0 | 1 SMLSLT          | (vectors)             | FEAT_SVE2 &#124;&#124; FEAT_SME |
|   1 |   1 | 0                 | UMLSLB(vectors)       | FEAT_SVE2 &#124;&#124; FEAT_SME |
|   1 |   1 | 1                 | UMLSLT (vectors)      | FEAT_SVE2 &#124;&#124; FEAT_SME |

## SVE2 saturating multiply-add long

The encodings in this section are decoded from SVE Integer Multiply-Add - Unpredicated.

<!-- image -->

|   S | T                    | Instruction Details   | Feature               |
|-----|----------------------|-----------------------|-----------------------|
|   0 | 0 SQDMLALB(vectors)  | FEAT_SVE2             | &#124;&#124; FEAT_SME |
|   0 | 1 SQDMLALT(vectors)  | FEAT_SVE2             | &#124;&#124; FEAT_SME |
|   1 | 0 SQDMLSLB(vectors)  | FEAT_SVE2             | &#124;&#124; FEAT_SME |
|   1 | 1 SQDMLSLT (vectors) | FEAT_SVE2             | &#124;&#124; FEAT_SME |

## SVE2 saturating multiply-add high

The encodings in this section are decoded from SVE Integer Multiply-Add - Unpredicated.

<!-- image -->

|   S | Instruction Details   | Feature                         |
|-----|-----------------------|---------------------------------|
|   0 | SQRDMLAH(vectors)     | FEAT_SVE2 &#124;&#124; FEAT_SME |
|   1 | SQRDMLSH(vectors)     | FEAT_SVE2 &#124;&#124; FEAT_SME |

## SVE mixed sign dot product

The encodings in this section are decoded from SVE Integer Multiply-Add - Unpredicated.

<!-- image -->

| size   | Instruction Details   | Feature                                                    |
|--------|-----------------------|------------------------------------------------------------|
| 10     | USDOT(vectors)        | (FEAT_SVE &&FEAT_I8MM) &#124;&#124; (FEAT_SME &&FEAT_I8MM) |
| != 10  | UNALLOCATED           | -                                                          |

## SVE2 Integer - Predicated

SVE2 Integer - Predicated

The encodings in this section are decoded from SVE encodings.

<!-- image -->

| 31          | 24 23 22 21 20 17 16 15 14 13   |
|-------------|---------------------------------|
| 0 1 0 0 0 1 | 0 0 op0 1 0 op1                 |

| op0   |   op1 | Instruction details                                      |
|-------|-------|----------------------------------------------------------|
| 0010  |     1 | SVE2 integer pairwise add and accumulate long            |
| 0011  |     1 | UNALLOCATED                                              |
| 011x  |     1 | UNALLOCATED                                              |
| 0x0x  |     1 | SVE2 integer unary operations (predicated)               |
| 0xxx  |     0 | SVE2 saturating/rounding bitwise shift left (predicated) |
| 10xx  |     0 | SVE2 integer halving add/subtract (predicated)           |
| 10xx  |     1 | SVE2 integer pairwise arithmetic                         |
| 11xx  |     0 | SVE2 saturating add/subtract                             |
| 11xx  |     1 | UNALLOCATED                                              |

## SVE2 integer pairwise add and accumulate long

The encodings in this section are decoded from SVE2 Integer - Predicated.

<!-- image -->

|   U | Instruction Details   | Feature                         |
|-----|-----------------------|---------------------------------|
|   0 | SADALP                | FEAT_SVE2 &#124;&#124; FEAT_SME |
|   1 | UADALP                | FEAT_SVE2 &#124;&#124; FEAT_SME |

## SVE2 integer unary operations (predicated)

The encodings in this section are decoded from SVE2 Integer - Predicated.

<!-- image -->

| 31    | 24 23 22 21 20 19 18 17 16 15 14 13 12 10 9 5 4   |
|-------|---------------------------------------------------|
| 0 1 0 | 0 size 0 0 Q 0 Z op 1 0 1 Pg Zn Zd                |

|   Q |   Z |   op | Instruction Details   | Feature                              |
|-----|-----|------|-----------------------|--------------------------------------|
|   0 |   0 |    0 | URECPE -Merging       | FEAT_SVE2 &#124;&#124; FEAT_SME      |
|   0 |   0 |    1 | URSQRTE -Merging      | FEAT_SVE2 &#124;&#124; FEAT_SME      |
|   0 |   1 |    0 | URECPE -Zeroing       | FEAT_SVE2p2 &#124;&#124; FEAT_SME2p2 |
|   0 |   1 |    1 | URSQRTE -Zeroing      | FEAT_SVE2p2 &#124;&#124; FEAT_SME2p2 |
|   1 |   0 |    0 | SQABS -Merging        | FEAT_SVE2 &#124;&#124; FEAT_SME      |
|   1 |   0 |    1 | SQNEG-Merging         | FEAT_SVE2 &#124;&#124; FEAT_SME      |
|   1 |   1 |    0 | SQABS -Zeroing        | FEAT_SVE2p2 &#124;&#124; FEAT_SME2p2 |
|   1 |   1 |    1 | SQNEG-Zeroing         | FEAT_SVE2p2 &#124;&#124; FEAT_SME2p2 |

## SVE2 saturating/rounding bitwise shift left (predicated)

The encodings in this section are decoded from SVE2 Integer - Predicated.

<!-- image -->

|   Q | R   |   N | U   | Instruction Details   | Feature                         |
|-----|-----|-----|-----|-----------------------|---------------------------------|
|   0 | x   |   0 | x   | UNALLOCATED           | -                               |
|   0 | 0   |   1 | 0   | SRSHL                 | FEAT_SVE2 &#124;&#124; FEAT_SME |
|   0 | 0   |   1 | 1   | URSHL                 | FEAT_SVE2 &#124;&#124; FEAT_SME |
|   0 | 1   |   1 | 0   | SRSHLR                | FEAT_SVE2 &#124;&#124; FEAT_SME |

|   Q |   R |   N |   U | Instruction Details   | Feature                         |
|-----|-----|-----|-----|-----------------------|---------------------------------|
|   0 |   1 |   1 |   1 | URSHLR                | FEAT_SVE2 &#124;&#124; FEAT_SME |
|   1 |   0 |   0 |   0 | SQSHL (vectors)       | FEAT_SVE2 &#124;&#124; FEAT_SME |
|   1 |   0 |   0 |   1 | UQSHL(vectors)        | FEAT_SVE2 &#124;&#124; FEAT_SME |
|   1 |   0 |   1 |   0 | SQRSHL                | FEAT_SVE2 &#124;&#124; FEAT_SME |
|   1 |   0 |   1 |   1 | UQRSHL                | FEAT_SVE2 &#124;&#124; FEAT_SME |
|   1 |   1 |   0 |   0 | SQSHLR                | FEAT_SVE2 &#124;&#124; FEAT_SME |
|   1 |   1 |   0 |   1 | UQSHLR                | FEAT_SVE2 &#124;&#124; FEAT_SME |
|   1 |   1 |   1 |   0 | SQRSHLR               | FEAT_SVE2 &#124;&#124; FEAT_SME |
|   1 |   1 |   1 |   1 | UQRSHLR               | FEAT_SVE2 &#124;&#124; FEAT_SME |

## SVE2 integer halving add/subtract (predicated)

The encodings in this section are decoded from SVE2 Integer - Predicated.

<!-- image -->

|   R |   S | U       | Instruction Details   | Feature                         |
|-----|-----|---------|-----------------------|---------------------------------|
|   0 |   0 | 0 SHADD | FEAT_SVE2             | &#124;&#124; FEAT_SME           |
|   0 |   0 | 1       | UHADD                 | FEAT_SVE2 &#124;&#124; FEAT_SME |
|   0 |   1 | 0       | SHSUB                 | FEAT_SVE2 &#124;&#124; FEAT_SME |
|   0 |   1 | 1       | UHSUB                 | FEAT_SVE2 &#124;&#124; FEAT_SME |
|   1 |   0 | 0       | SRHADD                | FEAT_SVE2 &#124;&#124; FEAT_SME |
|   1 |   0 | 1       | URHADD                | FEAT_SVE2 &#124;&#124; FEAT_SME |
|   1 |   1 | 0       | SHSUBR                | FEAT_SVE2 &#124;&#124; FEAT_SME |
|   1 |   1 | 1       | UHSUBR                | FEAT_SVE2 &#124;&#124; FEAT_SME |

## SVE2 integer pairwise arithmetic

The encodings in this section are decoded from SVE2 Integer - Predicated.

<!-- image -->

## SVE2 saturating add/subtract

The encodings in this section are decoded from SVE2 Integer - Predicated.

<!-- image -->

|   op |   S | U                | Instruction Details         | Feature                         |
|------|-----|------------------|-----------------------------|---------------------------------|
|    0 |   0 | 0 SQADD(vectors, | predicated)                 | FEAT_SVE2 &#124;&#124; FEAT_SME |
|    0 |   0 | 1                | UQADD(vectors, predicated)  | FEAT_SVE2 &#124;&#124; FEAT_SME |
|    0 |   1 | 0                | SQSUB (vectors, predicated) | FEAT_SVE2 &#124;&#124; FEAT_SME |
|    0 |   1 | 1                | UQSUB(vectors, predicated)  | FEAT_SVE2 &#124;&#124; FEAT_SME |
|    1 |   0 | 0                | SUQADD                      | FEAT_SVE2 &#124;&#124; FEAT_SME |
|    1 |   0 | 1                | USQADD                      | FEAT_SVE2 &#124;&#124; FEAT_SME |
|    1 |   1 | 0                | SQSUBR                      | FEAT_SVE2 &#124;&#124; FEAT_SME |
|    1 |   1 | 1                | UQSUBR                      | FEAT_SVE2 &#124;&#124; FEAT_SME |

## SVE Multiply - Indexed

SVE Multiply - Indexed

The encodings in this section are decoded from SVE encodings.

<!-- image -->

| op0    | Instruction details               |
|--------|-----------------------------------|
| 00000x | SVE integer dot product (indexed) |

|   opc | U   | Instruction Details   | Feature                         |
|-------|-----|-----------------------|---------------------------------|
|    00 | 0   | UNALLOCATED           | -                               |
|    00 | 1   | ADDP                  | FEAT_SVE2 &#124;&#124; FEAT_SME |
|    01 | x   | UNALLOCATED           | -                               |
|    10 | 0   | SMAXP                 | FEAT_SVE2 &#124;&#124; FEAT_SME |
|    10 | 1   | UMAXP                 | FEAT_SVE2 &#124;&#124; FEAT_SME |
|    11 | 0   | SMINP                 | FEAT_SVE2 &#124;&#124; FEAT_SME |
|    11 | 1   | UMINP                 | FEAT_SVE2 &#124;&#124; FEAT_SME |

## SVE integer dot product (indexed)

The encodings in this section are decoded from SVE Multiply - Indexed.

<!-- image -->

| size   | U   | Instruction Details                     | Feature                        |
|--------|-----|-----------------------------------------|--------------------------------|
| 0x     | x   | UNALLOCATED                             | -                              |
| 10     | 0   | SDOT (4-way, indexed) -8-bit to 32-bit  | FEAT_SVE &#124;&#124; FEAT_SME |
| 10     | 1   | UDOT(4-way, indexed) -8-bit to 32-bit   | FEAT_SVE &#124;&#124; FEAT_SME |
| 11     | 0   | SDOT (4-way, indexed) -16-bit to 64-bit | FEAT_SVE &#124;&#124; FEAT_SME |
| 11     | 1   | UDOT(4-way, indexed) -16-bit to 64-bit  | FEAT_SVE &#124;&#124; FEAT_SME |

## SVE2 integer multiply-add (indexed)

The encodings in this section are decoded from SVE Multiply - Indexed.

| op0    | Instruction details                            |
|--------|------------------------------------------------|
| 00001x | SVE2 integer multiply-add (indexed)            |
| 00010x | SVE2 saturating multiply-add high (indexed)    |
| 00011x | SVE mixed sign dot product (indexed)           |
| 001xxx | SVE2 saturating multiply-add (indexed)         |
| 0100xx | SVE2 complex integer dot product (indexed)     |
| 0101xx | UNALLOCATED                                    |
| 0110xx | SVE2 complex integer multiply-add (indexed)    |
| 0111xx | SVE2 complex saturating multiply-add (indexed) |
| 10xxxx | SVE2 integer multiply-add long (indexed)       |
| 110xxx | SVE2 integer multiply long (indexed)           |
| 1110xx | SVE2 saturating multiply (indexed)             |
| 11110x | SVE2 saturating multiply high (indexed)        |
| 111110 | SVE2 integer multiply (indexed)                |
| 111111 | UNALLOCATED                                    |

<!-- image -->

| size   | S                      | Instruction Details    | Feature                         |
|--------|------------------------|------------------------|---------------------------------|
| 0x     | 0 MLA(indexed) -16-bit | FEAT_SVE2 &#124;&#124; | FEAT_SME                        |
| 0x     | 1                      | MLS(indexed) -16-bit   | FEAT_SVE2 &#124;&#124; FEAT_SME |
| 10     | 0 MLA(indexed)         | -32-bit FEAT_SVE2      | &#124;&#124; FEAT_SME           |
| 10     | 1                      | MLS(indexed) -32-bit   | FEAT_SVE2 &#124;&#124; FEAT_SME |
| 11     | 0                      | MLA(indexed) -64-bit   | FEAT_SVE2 &#124;&#124; FEAT_SME |
| 11     | 1                      | MLS(indexed) -64-bit   | FEAT_SVE2 &#124;&#124; FEAT_SME |

## SVE2 saturating multiply-add high (indexed)

The encodings in this section are decoded from SVE Multiply - Indexed.

<!-- image -->

| size   | S                           | Instruction Details       | Feature                         |
|--------|-----------------------------|---------------------------|---------------------------------|
| 0x     | 0 SQRDMLAH(indexed) -16-bit | FEAT_SVE2                 | &#124;&#124; FEAT_SME           |
| 0x     | 1                           | SQRDMLSH(indexed) -16-bit | FEAT_SVE2 &#124;&#124; FEAT_SME |
| 10     | 0                           | SQRDMLAH(indexed) -32-bit | FEAT_SVE2 &#124;&#124; FEAT_SME |
| 10     | 1                           | SQRDMLSH(indexed) -32-bit | FEAT_SVE2 &#124;&#124; FEAT_SME |
| 11     | 0                           | SQRDMLAH(indexed) -64-bit | FEAT_SVE2 &#124;&#124; FEAT_SME |
| 11     | 1                           | SQRDMLSH(indexed) -64-bit | FEAT_SVE2 &#124;&#124; FEAT_SME |

## SVE mixed sign dot product (indexed)

The encodings in this section are decoded from SVE Multiply - Indexed.

<!-- image -->

| size   | U   | Instruction Details   | Feature                                                    |
|--------|-----|-----------------------|------------------------------------------------------------|
| 10     | 0   | USDOT(indexed)        | (FEAT_SVE &&FEAT_I8MM) &#124;&#124; (FEAT_SME &&FEAT_I8MM) |
| 10     | 1   | SUDOT                 | (FEAT_SVE &&FEAT_I8MM) &#124;&#124; (FEAT_SME &&FEAT_I8MM) |
| != 10  | x   | UNALLOCATED           | -                                                          |

## SVE2 saturating multiply-add (indexed)

The encodings in this section are decoded from SVE Multiply - Indexed.

<!-- image -->

| 31   | 24 23 22 21 20   | 16 15 13 12 11 10 9   |
|------|------------------|-----------------------|
| 0 1  | 0 size 1 opc     | 0 0 1 S il T Zn       |

| size   | S   | T   | Instruction Details        | Feature                         |
|--------|-----|-----|----------------------------|---------------------------------|
| 0x     | x   | x   | UNALLOCATED                | -                               |
| 10     | 0   | 0   | SQDMLALB(indexed) -32-bit  | FEAT_SVE2 &#124;&#124; FEAT_SME |
| 10     | 0   | 1   | SQDMLALT(indexed) -32-bit  | FEAT_SVE2 &#124;&#124; FEAT_SME |
| 10     | 1   | 0   | SQDMLSLB(indexed) -32-bit  | FEAT_SVE2 &#124;&#124; FEAT_SME |
| 10     | 1   | 1   | SQDMLSLT (indexed) -32-bit | FEAT_SVE2 &#124;&#124; FEAT_SME |
| 11     | 0   | 0   | SQDMLALB(indexed) -64-bit  | FEAT_SVE2 &#124;&#124; FEAT_SME |
| 11     | 0   | 1   | SQDMLALT(indexed) -64-bit  | FEAT_SVE2 &#124;&#124; FEAT_SME |
| 11     | 1   | 0   | SQDMLSLB(indexed) -64-bit  | FEAT_SVE2 &#124;&#124; FEAT_SME |
| 11     | 1   | 1   | SQDMLSLT (indexed) -64-bit | FEAT_SVE2 &#124;&#124; FEAT_SME |

## SVE2 complex integer dot product (indexed)

The encodings in this section are decoded from SVE Multiply - Indexed.

<!-- image -->

| size   | Instruction Details             | Feature                         |
|--------|---------------------------------|---------------------------------|
| 0x     | UNALLOCATED                     | -                               |
| 10     | CDOT(indexed) -8-bit to 32-bit  | FEAT_SVE2 &#124;&#124; FEAT_SME |
| 11     | CDOT(indexed) -16-bit to 64-bit | FEAT_SVE2 &#124;&#124; FEAT_SME |

## SVE2 complex integer multiply-add (indexed)

The encodings in this section are decoded from SVE Multiply - Indexed.

<!-- image -->

| size   | Instruction Details   | Feature                         |
|--------|-----------------------|---------------------------------|
| 0x     | UNALLOCATED           | -                               |
| 10     | CMLA(indexed) -16-bit | FEAT_SVE2 &#124;&#124; FEAT_SME |
| 11     | CMLA(indexed) -32-bit | FEAT_SVE2 &#124;&#124; FEAT_SME |

## SVE2 complex saturating multiply-add (indexed)

The encodings in this section are decoded from SVE Multiply - Indexed.

<!-- image -->

| size   | Instruction Details        | Feature                         |
|--------|----------------------------|---------------------------------|
| 0x     | UNALLOCATED                | -                               |
| 10     | SQRDCMLAH(indexed) -16-bit | FEAT_SVE2 &#124;&#124; FEAT_SME |
| 11     | SQRDCMLAH(indexed) -32-bit | FEAT_SVE2 &#124;&#124; FEAT_SME |

## SVE2 integer multiply-add long (indexed)

The encodings in this section are decoded from SVE Multiply - Indexed.

<!-- image -->

| size   | S   | U   | T   | Instruction Details     | Feature                         |
|--------|-----|-----|-----|-------------------------|---------------------------------|
| 0x     | x   | x   | x   | UNALLOCATED             | -                               |
| 10     | 0   | 0   | 0   | SMLALB(indexed) -32-bit | FEAT_SVE2 &#124;&#124; FEAT_SME |

|   size |   S |   U |   T | Instruction Details      | Feature                         |
|--------|-----|-----|-----|--------------------------|---------------------------------|
|     10 |   0 |   0 |   1 | SMLALT (indexed) -32-bit | FEAT_SVE2 &#124;&#124; FEAT_SME |
|     10 |   0 |   1 |   0 | UMLALB(indexed) -32-bit  | FEAT_SVE2 &#124;&#124; FEAT_SME |
|     10 |   0 |   1 |   1 | UMLALT(indexed) -32-bit  | FEAT_SVE2 &#124;&#124; FEAT_SME |
|     10 |   1 |   0 |   0 | SMLSLB (indexed) -32-bit | FEAT_SVE2 &#124;&#124; FEAT_SME |
|     10 |   1 |   0 |   1 | SMLSLT (indexed) -32-bit | FEAT_SVE2 &#124;&#124; FEAT_SME |
|     10 |   1 |   1 |   0 | UMLSLB(indexed) -32-bit  | FEAT_SVE2 &#124;&#124; FEAT_SME |
|     10 |   1 |   1 |   1 | UMLSLT (indexed) -32-bit | FEAT_SVE2 &#124;&#124; FEAT_SME |
|     11 |   0 |   0 |   0 | SMLALB(indexed) -64-bit  | FEAT_SVE2 &#124;&#124; FEAT_SME |
|     11 |   0 |   0 |   1 | SMLALT (indexed) -64-bit | FEAT_SVE2 &#124;&#124; FEAT_SME |
|     11 |   0 |   1 |   0 | UMLALB(indexed) -64-bit  | FEAT_SVE2 &#124;&#124; FEAT_SME |
|     11 |   0 |   1 |   1 | UMLALT(indexed) -64-bit  | FEAT_SVE2 &#124;&#124; FEAT_SME |
|     11 |   1 |   0 |   0 | SMLSLB (indexed) -64-bit | FEAT_SVE2 &#124;&#124; FEAT_SME |
|     11 |   1 |   0 |   1 | SMLSLT (indexed) -64-bit | FEAT_SVE2 &#124;&#124; FEAT_SME |
|     11 |   1 |   1 |   0 | UMLSLB(indexed) -64-bit  | FEAT_SVE2 &#124;&#124; FEAT_SME |
|     11 |   1 |   1 |   1 | UMLSLT (indexed) -64-bit | FEAT_SVE2 &#124;&#124; FEAT_SME |

## SVE2 integer multiply long (indexed)

The encodings in this section are decoded from SVE Multiply - Indexed.

<!-- image -->

| size   | U   | T   | Instruction Details      | Feature                         |
|--------|-----|-----|--------------------------|---------------------------------|
| 0x     | x   | x   | UNALLOCATED              | -                               |
| 10     | 0   | 0   | SMULLB(indexed) -32-bit  | FEAT_SVE2 &#124;&#124; FEAT_SME |
| 10     | 0   | 1   | SMULLT (indexed) -32-bit | FEAT_SVE2 &#124;&#124; FEAT_SME |
| 10     | 1   | 0   | UMULLB(indexed) -32-bit  | FEAT_SVE2 &#124;&#124; FEAT_SME |
| 10     | 1   | 1   | UMULLT(indexed) -32-bit  | FEAT_SVE2 &#124;&#124; FEAT_SME |
| 11     | 0   | 0   | SMULLB(indexed) -64-bit  | FEAT_SVE2 &#124;&#124; FEAT_SME |
| 11     | 0   | 1   | SMULLT (indexed) -64-bit | FEAT_SVE2 &#124;&#124; FEAT_SME |
| 11     | 1   | 0   | UMULLB(indexed) -64-bit  | FEAT_SVE2 &#124;&#124; FEAT_SME |
| 11     | 1   | 1   | UMULLT(indexed) -64-bit  | FEAT_SVE2 &#124;&#124; FEAT_SME |

## SVE2 saturating multiply (indexed)

The encodings in this section are decoded from SVE Multiply - Indexed.

<!-- image -->

| size   | T   | Instruction Details       | Feature                         |
|--------|-----|---------------------------|---------------------------------|
| 0x     | x   | UNALLOCATED               | -                               |
| 10     | 0   | SQDMULLB(indexed) -32-bit | FEAT_SVE2 &#124;&#124; FEAT_SME |
| 10     | 1   | SQDMULLT(indexed) -32-bit | FEAT_SVE2 &#124;&#124; FEAT_SME |
| 11     | 0   | SQDMULLB(indexed) -64-bit | FEAT_SVE2 &#124;&#124; FEAT_SME |
| 11     | 1   | SQDMULLT(indexed) -64-bit | FEAT_SVE2 &#124;&#124; FEAT_SME |

## SVE2 saturating multiply high (indexed)

The encodings in this section are decoded from SVE Multiply - Indexed.

<!-- image -->

| 31    | 24 23 22 21 20   | 16 15       | 11 10 9 5 4   |
|-------|------------------|-------------|---------------|
| 0 1 0 | 0 size 1         | 1 1 1 1 0 R | Zn Zd         |

| size   |   R | Instruction Details       | Feature                         |
|--------|-----|---------------------------|---------------------------------|
| 0x     |   0 | SQDMULH(indexed) -16-bit  | FEAT_SVE2 &#124;&#124; FEAT_SME |
| 0x     |   1 | SQRDMULH(indexed) -16-bit | FEAT_SVE2 &#124;&#124; FEAT_SME |
| 10     |   0 | SQDMULH(indexed) -32-bit  | FEAT_SVE2 &#124;&#124; FEAT_SME |
| 10     |   1 | SQRDMULH(indexed) -32-bit | FEAT_SVE2 &#124;&#124; FEAT_SME |
| 11     |   0 | SQDMULH(indexed) -64-bit  | FEAT_SVE2 &#124;&#124; FEAT_SME |
| 11     |   1 | SQRDMULH(indexed) -64-bit | FEAT_SVE2 &#124;&#124; FEAT_SME |

## SVE2 integer multiply (indexed)

The encodings in this section are decoded from SVE Multiply - Indexed.

<!-- image -->

## SVE2 integer add/subtract long

The encodings in this section are decoded from SVE2 Widening Integer Arithmetic.

<!-- image -->

|   op |   S | U   | T   | Instruction Details   | Feature                         |
|------|-----|-----|-----|-----------------------|---------------------------------|
|    0 |   0 | 0   | 0   | SADDLB                | FEAT_SVE2 &#124;&#124; FEAT_SME |
|    0 |   0 | 0   | 1   | SADDLT                | FEAT_SVE2 &#124;&#124; FEAT_SME |
|    0 |   0 | 1   | 0   | UADDLB                | FEAT_SVE2 &#124;&#124; FEAT_SME |
|    0 |   0 | 1   | 1   | UADDLT                | FEAT_SVE2 &#124;&#124; FEAT_SME |
|    0 |   1 | 0   | 0   | SSUBLB                | FEAT_SVE2 &#124;&#124; FEAT_SME |
|    0 |   1 | 0   | 1   | SSUBLT                | FEAT_SVE2 &#124;&#124; FEAT_SME |
|    0 |   1 | 1   | 0   | USUBLB                | FEAT_SVE2 &#124;&#124; FEAT_SME |
|    0 |   1 | 1   | 1   | USUBLT                | FEAT_SVE2 &#124;&#124; FEAT_SME |
|    1 |   0 | x   | x   | UNALLOCATED           | -                               |
|    1 |   1 | 0   | 0   | SABDLB                | FEAT_SVE2 &#124;&#124; FEAT_SME |

| size   | Instruction Details   | Feature                         |
|--------|-----------------------|---------------------------------|
| 0x     | MUL(indexed) -16-bit  | FEAT_SVE2 &#124;&#124; FEAT_SME |
| 10     | MUL(indexed) -32-bit  | FEAT_SVE2 &#124;&#124; FEAT_SME |
| 11     | MUL(indexed) -64-bit  | FEAT_SVE2 &#124;&#124; FEAT_SME |

## SVE2 Widening Integer Arithmetic

SVE2 Widening Integer Arithmetic

The encodings in this section are decoded from SVE encodings.

<!-- image -->

| 31   | 24 23 22 21 20   | 0   |
|------|------------------|-----|
| 0 1  | 1 0              |     |

| op0   | Instruction details            |
|-------|--------------------------------|
| 0x    | SVE2 integer add/subtract long |
| 10    | SVE2 integer add/subtract wide |
| 11    | SVE2 integer multiply long     |

|   op |   S |   U |   T | Instruction Details   | Feature                         |
|------|-----|-----|-----|-----------------------|---------------------------------|
|    1 |   1 |   0 |   1 | SABDLT                | FEAT_SVE2 &#124;&#124; FEAT_SME |
|    1 |   1 |   1 |   0 | UABDLB                | FEAT_SVE2 &#124;&#124; FEAT_SME |
|    1 |   1 |   1 |   1 | UABDLT                | FEAT_SVE2 &#124;&#124; FEAT_SME |

## SVE2 integer add/subtract wide

The encodings in this section are decoded from SVE2 Widening Integer Arithmetic.

<!-- image -->

| 31    | 24 23 22 21   | 20             | 16 15 14 13 12 11 10 9 5 4   |
|-------|---------------|----------------|------------------------------|
| 0 1 0 | 1 size 0      | Zm 0 1 0 S U T | Zn Zd                        |

|   S |   U | T        | Instruction Details   | Feature                         |
|-----|-----|----------|-----------------------|---------------------------------|
|   0 |   0 | 0 SADDWB | FEAT_SVE2             | &#124;&#124; FEAT_SME           |
|   0 |   0 | 1        | SADDWT                | FEAT_SVE2 &#124;&#124; FEAT_SME |
|   0 |   1 | 0        | UADDWB                | FEAT_SVE2 &#124;&#124; FEAT_SME |
|   0 |   1 | 1 UADDWT | FEAT_SVE2             | &#124;&#124; FEAT_SME           |
|   1 |   0 | 0        | SSUBWB                | FEAT_SVE2 &#124;&#124; FEAT_SME |
|   1 |   0 | 1        | SSUBWT                | FEAT_SVE2 &#124;&#124; FEAT_SME |
|   1 |   1 | 0        | USUBWB                | FEAT_SVE2 &#124;&#124; FEAT_SME |
|   1 |   1 | 1        | USUBWT                | FEAT_SVE2 &#124;&#124; FEAT_SME |

## SVE2 integer multiply long

The encodings in this section are decoded from SVE2 Widening Integer Arithmetic.

<!-- image -->

| 31    | 24 23 22 21 20    | 16 15 14 13 12 11 10 9 5 4   |
|-------|-------------------|------------------------------|
| 0 1 0 | 1 size 0 Zm 0 1 1 | op U T Zn Zd                 |

| size   |   op |   U |   T | Instruction Details   | Feature                         |
|--------|------|-----|-----|-----------------------|---------------------------------|
| xx     |    0 |   0 |   0 | SQDMULLB(vectors)     | FEAT_SVE2 &#124;&#124; FEAT_SME |
| xx     |    0 |   0 |   1 | SQDMULLT(vectors)     | FEAT_SVE2 &#124;&#124; FEAT_SME |
| xx     |    1 |   0 |   0 | SMULLB(vectors)       | FEAT_SVE2 &#124;&#124; FEAT_SME |
| xx     |    1 |   0 |   1 | SMULLT (vectors)      | FEAT_SVE2 &#124;&#124; FEAT_SME |
| xx     |    1 |   1 |   0 | UMULLB(vectors)       | FEAT_SVE2 FEAT_SME              |

||

## SVE Misc

SVE Misc

The encodings in this section are decoded from SVE encodings.

<!-- image -->

| 31   | 24 23 22 21 20 16 15 14   |
|------|---------------------------|
| 0 1  | 1 op0 0 1 0               |

| op0   | op1   | Instruction details                        |
|-------|-------|--------------------------------------------|
| 0     | 10xx  | SVE2 bitwise shift left long               |
| 1     | 10xx  | UNALLOCATED                                |
| x     | 00xx  | SVE2 integer add/subtract interleaved long |
| x     | 010x  | SVE2 bitwise exclusive-OR interleaved      |
| x     | 0110  | SVE integer matrix multiply accumulate     |
| x     | 0111  | UNALLOCATED                                |
| x     | 11xx  | SVE2 bitwise permute                       |

| size   |   op |   U |   T | Instruction Details               | Feature                         |
|--------|------|-----|-----|-----------------------------------|---------------------------------|
| xx     |    1 |   1 |   1 | UMULLT(vectors)                   | FEAT_SVE2 &#124;&#124; FEAT_SME |
| 00     |    0 |   1 |   0 | PMULLB-128-bit element            | FEAT_SVE_PMULL128               |
| 00     |    0 |   1 |   1 | PMULLT -128-bit element           | FEAT_SVE_PMULL128               |
| != 00  |    0 |   1 |   0 | PMULLB-16-bit or 64-bit elements  | FEAT_SVE2 &#124;&#124; FEAT_SME |
| != 00  |    0 |   1 |   1 | PMULLT -16-bit or 64-bit elements | FEAT_SVE2 &#124;&#124; FEAT_SME |

## SVE2 bitwise shift left long

The encodings in this section are decoded from SVE Misc.

<!-- image -->

|   U | T Instruction   | Feature                         |
|-----|-----------------|---------------------------------|
|   0 | 0 SSHLLB        | FEAT_SVE2 &#124;&#124; FEAT_SME |
|   0 | 1 SSHLLT        | FEAT_SVE2 &#124;&#124; FEAT_SME |
|   1 | 0 USHLLB        | FEAT_SVE2 &#124;&#124; FEAT_SME |

|   U | T Instruction Details   | Feature                         |
|-----|-------------------------|---------------------------------|
|   1 | 1 USHLLT                | FEAT_SVE2 &#124;&#124; FEAT_SME |

## SVE2 integer add/subtract interleaved long

The encodings in this section are decoded from SVE Misc.

<!-- image -->

|   S |   tb | Instruction Details   | Feature                         |
|-----|------|-----------------------|---------------------------------|
|   0 |    0 | SADDLBT               | FEAT_SVE2 &#124;&#124; FEAT_SME |
|   0 |    1 | UNALLOCATED           | -                               |
|   1 |    0 | SSUBLBT               | FEAT_SVE2 &#124;&#124; FEAT_SME |
|   1 |    1 | SSUBLTB               | FEAT_SVE2 &#124;&#124; FEAT_SME |

## SVE2 bitwise exclusive-OR interleaved

The encodings in this section are decoded from SVE Misc.

<!-- image -->

|   tb | Instruction Details   | Feature                         |
|------|-----------------------|---------------------------------|
|    0 | EORBT                 | FEAT_SVE2 &#124;&#124; FEAT_SME |
|    1 | EORTB                 | FEAT_SVE2 &#124;&#124; FEAT_SME |

## SVE integer matrix multiply accumulate

The encodings in this section are decoded from SVE Misc.

<!-- image -->

## SVE2 bitwise permute

The encodings in this section are decoded from SVE Misc.

<!-- image -->

|   opc | Instruction Details   | Feature          |
|-------|-----------------------|------------------|
|    00 | BEXT                  | FEAT_SVE_BitPerm |
|    01 | BDEP                  | FEAT_SVE_BitPerm |
|    10 | BGRP                  | FEAT_SVE_BitPerm |
|    11 | UNALLOCATED           | -                |

## SVE2 Accumulate

SVE2 Accumulate

The encodings in this section are decoded from SVE encodings.

<!-- image -->

| op0     | op1   | Instruction details                                  |
|---------|-------|------------------------------------------------------|
| 0000    | 011   | SVE2 complex integer add                             |
| xxxx    | 00x   | SVE2 integer absolute difference and accumulate long |
| xxxx    | 010   | SVE2 integer add/subtract long with carry            |
| xxxx    | 10x   | SVE2 bitwise shift right and accumulate              |
| xxxx    | 110   | SVE2 bitwise shift and insert                        |
| xxxx    | 111   | SVE2 integer absolute difference and accumulate      |
| != 0000 | 011   | UNALLOCATED                                          |

|   uns | Instruction Details   | Feature              |
|-------|-----------------------|----------------------|
|    00 | SMMLA                 | FEAT_SVE &&FEAT_I8MM |
|    01 | UNALLOCATED           | -                    |
|    10 | USMMLA                | FEAT_SVE &&FEAT_I8MM |
|    11 | UMMLA                 | FEAT_SVE &&FEAT_I8MM |

## SVE2 complex integer add

The encodings in this section are decoded from SVE2 Accumulate.

<!-- image -->

|   op | Instruction Details   | Feature                         |
|------|-----------------------|---------------------------------|
|    0 | CADD                  | FEAT_SVE2 &#124;&#124; FEAT_SME |
|    1 | SQCADD                | FEAT_SVE2 &#124;&#124; FEAT_SME |

## SVE2 integer absolute difference and accumulate long

The encodings in this section are decoded from SVE2 Accumulate.

<!-- image -->

|   U |   T | Instruction Details   | Feature   |                       |          |
|-----|-----|-----------------------|-----------|-----------------------|----------|
|   0 |   0 | SABALB                | FEAT_SVE2 | &#124;&#124; FEAT_SME |          |
|   0 |   1 | SABALT                | FEAT_SVE2 | &#124;&#124;          | FEAT_SME |
|   1 |   0 | UABALB                | FEAT_SVE2 | &#124;&#124;          | FEAT_SME |
|   1 |   1 | UABALT                | FEAT_SVE2 | &#124;&#124;          | FEAT_SME |

## SVE2 integer add/subtract long with carry

The encodings in this section are decoded from SVE2 Accumulate.

<!-- image -->

| size   |   T | Instruction Details   | Feature                         |
|--------|-----|-----------------------|---------------------------------|
| 0x     |   0 | ADCLB                 | FEAT_SVE2 &#124;&#124; FEAT_SME |
| 0x     |   1 | ADCLT                 | FEAT_SVE2 &#124;&#124; FEAT_SME |

## SVE2 bitwise shift and insert

The encodings in this section are decoded from SVE2 Accumulate.

<!-- image -->

|   op | Instruction Details   | Feature                         |
|------|-----------------------|---------------------------------|
|    0 | SRI                   | FEAT_SVE2 &#124;&#124; FEAT_SME |
|    1 | SLI                   | FEAT_SVE2 &#124;&#124; FEAT_SME |

## SVE2 integer absolute difference and accumulate

The encodings in this section are decoded from SVE2 Accumulate.

<!-- image -->

| 31   | 24 23 22 21 20   | 16 15 14 13 11 10 9 5 4   |
|------|------------------|---------------------------|
| 0 1  | 1 size 0 Zm      | 1 1 1 1 1 U Zn Zda        |

| size   |   T | Instruction Details   | Feature                         |
|--------|-----|-----------------------|---------------------------------|
| 1x     |   0 | SBCLB                 | FEAT_SVE2 &#124;&#124; FEAT_SME |
| 1x     |   1 | SBCLT                 | FEAT_SVE2 &#124;&#124; FEAT_SME |

## SVE2 bitwise shift right and accumulate

The encodings in this section are decoded from SVE2 Accumulate.

<!-- image -->

| 31   | 24 23 22 21 20 19 18 16 15 12 11 10 9 5 4   |
|------|---------------------------------------------|
| 0 1  | 1 tszh 0 tszl imm3 1 1 1 0 R U Zn Zda       |

|   R |   U | Instruction Details   | Feature   |                       |          |
|-----|-----|-----------------------|-----------|-----------------------|----------|
|   0 |   0 | SSRA                  | FEAT_SVE2 | &#124;&#124; FEAT_SME |          |
|   0 |   1 | USRA                  | FEAT_SVE2 | &#124;&#124;          | FEAT_SME |
|   1 |   0 | SRSRA                 | FEAT_SVE2 | &#124;&#124; FEAT_SME |          |
|   1 |   1 | URSRA                 | FEAT_SVE2 | &#124;&#124; FEAT_SME |          |

## SVE2 Narrowing

SVE2 Narrowing

The encodings in this section are decoded from SVE encodings.

<!-- image -->

| 31   | 24 23 22 21 20 19 18 17 16 15 14 13 12 11 10 9 6 5   |
|------|------------------------------------------------------|
| 0 1  | 1 op0 1 op1 op2 0 op3 op4 op5                        |

| op0   | op1   | op2   | op3   | op4   | op5   | Instruction details                       |
|-------|-------|-------|-------|-------|-------|-------------------------------------------|
| 0     | 00    | 0     | 10    | x     | x     | SVE2 saturating extract narrow            |
| 0     | 00    | 1     | 10    | 0     | 0     | SME2 multi-vec extract narrow             |
| 0     | 00    | 1     | 10    | 0     | 1     | UNALLOCATED                               |
| 0     | 00    | 1     | 10    | 1     | x     | UNALLOCATED                               |
| 0     | xx    | x     | 0x    | x     | x     | SVE2 bitwise shift right narrow           |
| 0     | != 00 | x     | 10    | x     | x     | UNALLOCATED                               |
| 1     | xx    | x     | 0x    | 0     | 0     | SME2 multi-vec shift narrow               |
| 1     | xx    | x     | 0x    | 0     | 1     | UNALLOCATED                               |
| 1     | xx    | x     | 0x    | 1     | x     | UNALLOCATED                               |
| 1     | xx    | x     | 10    | x     | x     | UNALLOCATED                               |
| x     | xx    | x     | 11    | x     | x     | SVE2integer add/subtract narrow high part |

## SVE2 saturating extract narrow

The encodings in this section are decoded from SVE2 Narrowing.

<!-- image -->

tszh

|   U | Instruction Details   | Feature                         |
|-----|-----------------------|---------------------------------|
|   0 | SABA                  | FEAT_SVE2 &#124;&#124; FEAT_SME |
|   1 | UABA                  | FEAT_SVE2 &#124;&#124; FEAT_SME |

|   opc | T   | Instruction Details   | Feature                         |
|-------|-----|-----------------------|---------------------------------|
|    00 | 0   | SQXTNB                | FEAT_SVE2 &#124;&#124; FEAT_SME |
|    00 | 1   | SQXTNT                | FEAT_SVE2 &#124;&#124; FEAT_SME |
|    01 | 0   | UQXTNB                | FEAT_SVE2 &#124;&#124; FEAT_SME |
|    01 | 1   | UQXTNT                | FEAT_SVE2 &#124;&#124; FEAT_SME |
|    10 | 0   | SQXTUNB               | FEAT_SVE2 &#124;&#124; FEAT_SME |
|    10 | 1   | SQXTUNT               | FEAT_SVE2 &#124;&#124; FEAT_SME |
|    11 | x   | UNALLOCATED           | -                               |

## SME2 multi-vec extract narrow

The encodings in this section are decoded from SVE2 Narrowing.

<!-- image -->

tszh

|   tszh | tszl   | opc   | Instruction Details   | Feature                            |
|--------|--------|-------|-----------------------|------------------------------------|
|      0 | 10     | 00    | SQCVTN                | FEAT_SME2 &#124;&#124; FEAT_SVE2p1 |
|      0 | 10     | 01    | UQCVTN                | FEAT_SME2 &#124;&#124; FEAT_SVE2p1 |
|      0 | 10     | 10    | SQCVTUN               | FEAT_SME2 &#124;&#124; FEAT_SVE2p1 |
|      0 | 10     | 11    | UNALLOCATED           | -                                  |
|      0 | != 10  | xx    | UNALLOCATED           | -                                  |
|      1 | xx     | xx    | UNALLOCATED           | -                                  |

## SVE2 bitwise shift right narrow

The encodings in this section are decoded from SVE2 Narrowing.

<!-- image -->

|   op |   U |   R | T   | Instruction Details   | Feature                         |
|------|-----|-----|-----|-----------------------|---------------------------------|
|    0 |   0 |   0 | 0   | SQSHRUNB              | FEAT_SVE2 &#124;&#124; FEAT_SME |
|    0 |   0 |   0 |     | 1 SQSHRUNT            | FEAT_SVE2 &#124;&#124; FEAT_SME |

|   op |   U |   R |   T | Instruction Details   | Feature                         |
|------|-----|-----|-----|-----------------------|---------------------------------|
|    0 |   0 |   1 |   0 | SQRSHRUNB             | FEAT_SVE2 &#124;&#124; FEAT_SME |
|    0 |   0 |   1 |   1 | SQRSHRUNT             | FEAT_SVE2 &#124;&#124; FEAT_SME |
|    0 |   1 |   0 |   0 | SHRNB                 | FEAT_SVE2 &#124;&#124; FEAT_SME |
|    0 |   1 |   0 |   1 | SHRNT                 | FEAT_SVE2 &#124;&#124; FEAT_SME |
|    0 |   1 |   1 |   0 | RSHRNB                | FEAT_SVE2 &#124;&#124; FEAT_SME |
|    0 |   1 |   1 |   1 | RSHRNT                | FEAT_SVE2 &#124;&#124; FEAT_SME |
|    1 |   0 |   0 |   0 | SQSHRNB               | FEAT_SVE2 &#124;&#124; FEAT_SME |
|    1 |   0 |   0 |   1 | SQSHRNT               | FEAT_SVE2 &#124;&#124; FEAT_SME |
|    1 |   0 |   1 |   0 | SQRSHRNB              | FEAT_SVE2 &#124;&#124; FEAT_SME |
|    1 |   0 |   1 |   1 | SQRSHRNT              | FEAT_SVE2 &#124;&#124; FEAT_SME |
|    1 |   1 |   0 |   0 | UQSHRNB               | FEAT_SVE2 &#124;&#124; FEAT_SME |
|    1 |   1 |   0 |   1 | UQSHRNT               | FEAT_SVE2 &#124;&#124; FEAT_SME |
|    1 |   1 |   1 |   0 | UQRSHRNB              | FEAT_SVE2 &#124;&#124; FEAT_SME |
|    1 |   1 |   1 |   1 | UQRSHRNT              | FEAT_SVE2 &#124;&#124; FEAT_SME |

## SME2 multi-vec shift narrow

The encodings in this section are decoded from SVE2 Narrowing.

<!-- image -->

|   op0 | opc   | op1   | U   | R   | Instruction Details   | Feature                            |
|-------|-------|-------|-----|-----|-----------------------|------------------------------------|
|     0 | 0xxxx | x     | x   | x   | UNALLOCATED           | -                                  |
|     0 | 1xxxx | x     | x   | 0   | UNALLOCATED           | -                                  |
|     0 | 1xxxx | 0     | 0   | 1   | SQRSHRUN              | FEAT_SME2 &#124;&#124; FEAT_SVE2p1 |
|     0 | 1xxxx | 0     | 1   | 1   | UNALLOCATED           | -                                  |
|     0 | 1xxxx | 1     | 0   | 1   | SQRSHRN               | FEAT_SME2 &#124;&#124; FEAT_SVE2p1 |
|     0 | 1xxxx | 1     | 1   | 1   | UQRSHRN               | FEAT_SME2 &#124;&#124; FEAT_SVE2p1 |
|     1 | xxxxx | x     | x   | x   | UNALLOCATED           | -                                  |

## SVE2 integer add/subtract narrow high part

The encodings in this section are decoded from SVE2 Narrowing.

<!-- image -->

|   S |   R | T        | Instruction Details   | Feature                         |
|-----|-----|----------|-----------------------|---------------------------------|
|   0 |   0 | 0 ADDHNB | FEAT_SVE2             | &#124;&#124; FEAT_SME           |
|   0 |   0 | 1        | ADDHNT                | FEAT_SVE2 &#124;&#124; FEAT_SME |
|   0 |   1 | 0        | RADDHNB               | FEAT_SVE2 &#124;&#124; FEAT_SME |
|   0 |   1 | 1        | RADDHNT               | FEAT_SVE2 &#124;&#124; FEAT_SME |
|   1 |   0 | 0        | SUBHNB                | FEAT_SVE2 &#124;&#124; FEAT_SME |
|   1 |   0 | 1        | SUBHNT                | FEAT_SVE2 &#124;&#124; FEAT_SME |
|   1 |   1 | 0        | RSUBHNB               | FEAT_SVE2 &#124;&#124; FEAT_SME |
|   1 |   1 | 1        | RSUBHNT               | FEAT_SVE2 &#124;&#124; FEAT_SME |

## SVE2 Histogram Computation (Segment) and Lookup Table

SVE2 Histogram Computation (Segment) and Lookup Table

The encodings in this section are decoded from SVE encodings.

<!-- image -->

| op0   | op1   | Instruction details                                          | Feature                                                    |
|-------|-------|--------------------------------------------------------------|------------------------------------------------------------|
| 0     | 0x1   | UNALLOCATED                                                  | -                                                          |
| 1     | 001   | LUTI4 (8-bit and 16-bit) - Byte, single register table       | (FEAT_SVE2 &&FEAT_LUT) &#124;&#124; (FEAT_SME2 &&FEAT_LUT) |
| 1     | 011   | UNALLOCATED                                                  | -                                                          |
| x     | 000   | HISTSEG                                                      | FEAT_SVE2                                                  |
| x     | 100   | LUTI2 (8-bit and 16-bit) -Byte                               | (FEAT_SVE2 &&FEAT_LUT) &#124;&#124; (FEAT_SME2 &&FEAT_LUT) |
| x     | 1x1   | SVE2 lookup table with 4-bit indices and 16-bit element size | -                                                          |
| x     | x10   | LUTI2 (8-bit and 16-bit) -Halfword                           | (FEAT_SVE2 &&FEAT_LUT) &#124;&#124; (FEAT_SME2 &&FEAT_LUT) |

## SVE2 lookup table with 4-bit indices and 16-bit element size

The encodings in this section are decoded from SVE2 Histogram Computation (Segment) and Lookup Table.

<!-- image -->

| 31    | 24 23 22 21 20 16 15 12 11 10   |
|-------|---------------------------------|
| 0 1 0 | 1 i2 1 Zm 1 0 1 1 op 1          |

|   op | Instruction Details                                        | Feature                                                    |
|------|------------------------------------------------------------|------------------------------------------------------------|
|    0 | LUTI4 (8-bit and 16-bit) -Halfword, two register table     | (FEAT_SVE2 &&FEAT_LUT) &#124;&#124; (FEAT_SME2 &&FEAT_LUT) |
|    1 | LUTI4 (8-bit and 16-bit) - Halfword, single register table | (FEAT_SVE2 &&FEAT_LUT) &#124;&#124; (FEAT_SME2 &&FEAT_LUT) |

## SVE2 Crypto Extensions

SVE2 Crypto Extensions

The encodings in this section are decoded from SVE encodings.

<!-- image -->

| 31   | 24 23 22 21   |   20 | 18 17   | 16   | 15   |   13 12 | 10   | 5   | 4   | 1 0   |
|------|---------------|------|---------|------|------|---------|------|-----|-----|-------|
| 0 1  | 0 1 0 1       |    1 | op0     | op1  | 1 1  |       1 | op2  | op3 |     | op4   |

| op0    | op1   | op2   | op3      | op4   | Instruction details                                               |
|--------|-------|-------|----------|-------|-------------------------------------------------------------------|
| 000    | 00    | 00x   | 00000    | x     | SVE2 crypto unary operations                                      |
| 000    | 00    | 00x   | != 00000 | x     | UNALLOCATED                                                       |
| 000    | 01    | 00x   | xxxxx    | x     | UNALLOCATED                                                       |
| 000    | 1x    | 00x   | xxxxx    | x     | SVE2 crypto destructive binary operations                         |
| xx0    | 1x    | 01x   | xxxxx    | x     | SVE2 multi-vector AES single round (two registers)                |
| xx1    | 1x    | 01x   | xxxxx    | x     | SVE2 multi-vector AES single round (four registers)               |
| xxx    | 00    | 01x   | xxxxx    | x     | UNALLOCATED                                                       |
| xxx    | 01    | 01x   | xxxxx    | x     | UNALLOCATED                                                       |
| xxx    | xx    | 10x   | xxxxx    | x     | SVE2 crypto constructive binary operations                        |
| xxx    | xx    | 110   | xxxxx    | 0     | SVE2 Multi-vector polynomial multiply long                        |
| xxx    | xx    | 111   | xxxxx    | 0     | SVE2 Multi-vector polynomial multiply long and accumulate vectors |
| xxx    | xx    | 11x   | xxxxx    | 1     | UNALLOCATED                                                       |
| != 000 | xx    | 00x   | xxxxx    | x     | UNALLOCATED                                                       |

## SVE2 crypto unary operations

The encodings in this section are decoded from SVE2 Crypto Extensions.

<!-- image -->

| size   | op   | Instruction Details   | Feature      |
|--------|------|-----------------------|--------------|
| 00     | 0    | AESMC                 | FEAT_SVE_AES |
| 00     | 1    | AESIMC                | FEAT_SVE_AES |
| != 00  | x    | UNALLOCATED           | -            |

## SVE2 crypto destructive binary operations

The encodings in this section are decoded from SVE2 Crypto Extensions.

<!-- image -->

| size   | op   | o2   | Instruction Details   | Feature      |
|--------|------|------|-----------------------|--------------|
| 00     | 0    | 0    | AESE (vectors)        | FEAT_SVE_AES |
| 00     | 0    | 1    | AESD (vectors)        | FEAT_SVE_AES |
| 00     | 1    | 0    | SM4E                  | FEAT_SVE_SM4 |
| 00     | 1    | 1    | UNALLOCATED           | -            |
| != 00  | x    | x    | UNALLOCATED           | -            |

## SVE2 multi-vector AES single round (two registers)

The encodings in this section are decoded from SVE2 Crypto Extensions.

<!-- image -->

| 31   | 23 22 21 20 19 18 17             | 16 15 11 10 9 5 4 1 0   |
|------|----------------------------------|-------------------------|
| 0 1  | size 1 i2 0 1 op 1 1 1 0 1 o2 Zm | Zdn o3                  |

| size   | op   | o2   | o3   | Instruction Details   | Feature       |
|--------|------|------|------|-----------------------|---------------|
| 00     | x    | x    | 1    | UNALLOCATED           | -             |
| 00     | 0    | 0    | 0    | AESE (indexed)        | FEAT_SVE_AES2 |
| 00     | 0    | 1    | 0    | AESD (indexed)        | FEAT_SVE_AES2 |
| 00     | 1    | 0    | 0    | AESEMC                | FEAT_SVE_AES2 |
| 00     | 1    | 1    | 0    | AESDIMC               | FEAT_SVE_AES2 |
| != 00  | x    | x    | x    | UNALLOCATED           | -             |

## SVE2 multi-vector AES single round (four registers)

The encodings in this section are decoded from SVE2 Crypto Extensions.

<!-- image -->

| 31    | 24 23 22 21 20 17 16 15         | 19 18 11 10 9 5   | 4 2 1 0   |
|-------|---------------------------------|-------------------|-----------|
| 0 1 0 | 1 size 1 i2 1 1 op 1 1 1 0 1 o2 | Zm Zdn            | opc3      |

| size   | op   | o2   | opc3   | Instruction Details   | Feature       |
|--------|------|------|--------|-----------------------|---------------|
| 00     | x    | x    | != 00  | UNALLOCATED           | -             |
| 00     | 0    | 0    | 00     | AESE (indexed)        | FEAT_SVE_AES2 |
| 00     | 0    | 1    | 00     | AESD (indexed)        | FEAT_SVE_AES2 |
| 00     | 1    | 0    | 00     | AESEMC                | FEAT_SVE_AES2 |
| 00     | 1    | 1    | 00     | AESDIMC               | FEAT_SVE_AES2 |
| != 00  | x    | x    | xx     | UNALLOCATED           | -             |

## SVE2 crypto constructive binary operations

The encodings in this section are decoded from SVE2 Crypto Extensions.

<!-- image -->

| size   | op   | Instruction Details   | Feature       |
|--------|------|-----------------------|---------------|
| 00     | 0    | SM4EKEY               | FEAT_SVE_SM4  |
| 00     | 1    | RAX1                  | FEAT_SVE_SHA3 |
| != 00  | x    | UNALLOCATED           | -             |

## SVE2 Multi-vector polynomial multiply long

The encodings in this section are decoded from SVE2 Crypto Extensions.

<!-- image -->

## SVE2 FP8 widening multiply-add

SVE2 FP8 widening multiply-add

The encodings in this section are decoded from SVE encodings.

<!-- image -->

| 31 24 23                | 22 21 20 16 15 14 13 12   |
|-------------------------|---------------------------|
| 0 1 1 0 0 1 0 0 op0 0 1 | 1 0 op1                   |

|   op0 | op1   | Instruction details             |
|-------|-------|---------------------------------|
|     0 | x     | SVE2 FP8 multiply-add long long |
|     1 | 0     | SVE2 FP8 multiply-add long      |
|     1 | 1     | UNALLOCATED                     |

## SVE2 FP8 multiply-add long long

The encodings in this section are decoded from SVE2 FP8 widening multiply-add.

<!-- image -->

| size   | Instruction Details   | Feature       |
|--------|-----------------------|---------------|
| 00     | PMULL                 | FEAT_SVE_AES2 |
| != 00  | UNALLOCATED           | -             |

## SVE2 Multi-vector polynomial multiply long and accumulate vectors

The encodings in this section are decoded from SVE2 Crypto Extensions.

<!-- image -->

| size   | Instruction Details   | Feature       |
|--------|-----------------------|---------------|
| 00     | PMLAL                 | FEAT_SVE_AES2 |
| != 00  | UNALLOCATED           | -             |

|   TT | Instruction Details   | Feature                                                 |
|------|-----------------------|---------------------------------------------------------|
|   00 | FMLALLBB(vectors)     | FEAT_SSVE_FP8FMA &#124;&#124; (FEAT_SVE2 &&FEAT_FP8FMA) |
|   01 | FMLALLBT(vectors)     | FEAT_SSVE_FP8FMA &#124;&#124; (FEAT_SVE2 &&FEAT_FP8FMA) |
|   10 | FMLALLTB (vectors)    | FEAT_SSVE_FP8FMA &#124;&#124; (FEAT_SVE2 &&FEAT_FP8FMA) |
|   11 | FMLALLTT (vectors)    | FEAT_SSVE_FP8FMA &#124;&#124; (FEAT_SVE2 &&FEAT_FP8FMA) |

## SVE2 FP8 multiply-add long

The encodings in this section are decoded from SVE2 FP8 widening multiply-add.

<!-- image -->

| 31    | 24 23 22 21 20     | 16 15 14 13 12 11 10 9 5 4   |
|-------|--------------------|------------------------------|
| 0 1 1 | 0 1 0 1 Zm 1 0 0 T | 1 0 Zn Zda                   |

|   T | Instruction Details           | Feature                                                 |
|-----|-------------------------------|---------------------------------------------------------|
|   0 | FMLALB(vectors, FP8 to FP16)  | FEAT_SSVE_FP8FMA &#124;&#124; (FEAT_SVE2 &&FEAT_FP8FMA) |
|   1 | FMLALT (vectors, FP8 to FP16) | FEAT_SSVE_FP8FMA &#124;&#124; (FEAT_SVE2 &&FEAT_FP8FMA) |

## SVE2 floating-point unary operations - zeroing predicated

SVE2 floating-point unary operations - zeroing predicated

The encodings in this section are decoded from SVE encodings.

<!-- image -->

| 31      | 24 23 22 21 19 18   |
|---------|---------------------|
| 0 1 1 0 | 0 0 1 1 op0         |

| op0   | Instruction details                                        |
|-------|------------------------------------------------------------|
| 00x   | Floating-point round to integral value (predicated)        |
| 010   | Floating-point convert (predicated)                        |
| 011   | Floating-point square root (predicated)                    |
| 10x   | Floating-point round and convert from integer (predicated) |
| 11x   | Floating-point log and convert to integer                  |

## Floating-point round to integral value (predicated)

The encodings in this section are decoded from SVE2 floating-point unary operations - zeroing predicated.

<!-- image -->

| 31   | 24 23 22 21                   | 17 16 15 14 13 12 10 9 5 4   |
|------|-------------------------------|------------------------------|
| 0 1  | 0 size 0 1 1 0 0 op 1 opc2 Pg | Zn Zd                        |

|   op |   opc2 | Instruction Details                                    | Feature                              |
|------|--------|--------------------------------------------------------|--------------------------------------|
|    0 |     00 | FRINT < r > - Nearest with ties to even, zeroing       | FEAT_SVE2p2 &#124;&#124; FEAT_SME2p2 |
|    0 |     01 | FRINT < r > - Toward plus infinity, zeroing            | FEAT_SVE2p2 &#124;&#124; FEAT_SME2p2 |
|    0 |     10 | FRINT < r > - Toward minus infinity, zeroing           | FEAT_SVE2p2 &#124;&#124; FEAT_SME2p2 |
|    0 |     11 | FRINT < r > -Toward zero, zeroing                      | FEAT_SVE2p2 &#124;&#124; FEAT_SME2p2 |
|    1 |     00 | FRINT < r > -Nearest with ties to away, zeroing        | FEAT_SVE2p2 &#124;&#124; FEAT_SME2p2 |
|    1 |     01 | UNALLOCATED                                            | -                                    |
|    1 |     10 | FRINT < r > - Current mode signalling inexact, zeroing | FEAT_SVE2p2 &#124;&#124; FEAT_SME2p2 |
|    1 |     11 | FRINT < r > -Current mode, zeroing                     | FEAT_SVE2p2 &#124;&#124; FEAT_SME2p2 |

## Floating-point convert (predicated)

The encodings in this section are decoded from SVE2 floating-point unary operations - zeroing predicated.

<!-- image -->

| 31    | 24 23 22 21     | 19 18       | 16 15 14 13 12 10 9 5 4   |
|-------|-----------------|-------------|---------------------------|
| 0 1 1 | 0 opc 0 1 1 0 1 | 0 1 opc2 Pg | Zn Zd                     |

| opc   | opc2   | Instruction Details                                 | Feature                              |
|-------|--------|-----------------------------------------------------|--------------------------------------|
| x0    | 11     | UNALLOCATED                                         | -                                    |
| 00    | 0x     | UNALLOCATED                                         | -                                    |
| 00    | 10     | FCVTX                                               | FEAT_SVE2p2 &#124;&#124; FEAT_SME2p2 |
| 01    | xx     | UNALLOCATED                                         | -                                    |
| 10    | 00     | FCVT - Single-precision to half- precision, zeroing | FEAT_SVE2p2 &#124;&#124; FEAT_SME2p2 |
| 10    | 01     | FCVT - Half-precision to single- precision, zeroing | FEAT_SVE2p2 &#124;&#124; FEAT_SME2p2 |
| 10    | 10     | BFCVT                                               | FEAT_SVE2p2 &#124;&#124; FEAT_SME2p2 |

|   opc |   opc2 | Instruction Details                                   | Feature                              |
|-------|--------|-------------------------------------------------------|--------------------------------------|
|    11 |     00 | FCVT - Double-precision to half- precision, zeroing   | FEAT_SVE2p2 &#124;&#124; FEAT_SME2p2 |
|    11 |     01 | FCVT - Half-precision to double- precision, zeroing   | FEAT_SVE2p2 &#124;&#124; FEAT_SME2p2 |
|    11 |     10 | FCVT - Double-precision to single- precision, zeroing | FEAT_SVE2p2 &#124;&#124; FEAT_SME2p2 |
|    11 |     11 | FCVT - Single-precision to double- precision, zeroing | FEAT_SVE2p2 &#124;&#124; FEAT_SME2p2 |

## Floating-point square root (predicated)

The encodings in this section are decoded from SVE2 floating-point unary operations - zeroing predicated.

<!-- image -->

| opc   | Instruction Details   | Feature                              |
|-------|-----------------------|--------------------------------------|
| 00    | FRECPX                | FEAT_SVE2p2 &#124;&#124; FEAT_SME2p2 |
| 01    | FSQRT                 | FEAT_SVE2p2 &#124;&#124; FEAT_SME2p2 |
| 1x    | UNALLOCATED           | -                                    |

## Floating-point round and convert from integer (predicated)

The encodings in this section are decoded from SVE2 floating-point unary operations - zeroing predicated.

<!-- image -->

| 31      | 24 23 22 21 17 16 15 14 13 12   |
|---------|---------------------------------|
| 0 1 1 0 | 0 opc 0 1 1 1 0 o2 1 o3 U Pg    |

|   opc |   o2 | o3   | U   | Instruction Details                                     | Feature                              |
|-------|------|------|-----|---------------------------------------------------------|--------------------------------------|
|    00 |    0 | x    | 0   | FRINT32Z                                                | FEAT_SVE2p2 &#124;&#124; FEAT_SME2p2 |
|    00 |    0 | x    | 1   | FRINT32X                                                | FEAT_SVE2p2 &#124;&#124; FEAT_SME2p2 |
|    00 |    1 | x    | 0   | FRINT64Z                                                | FEAT_SVE2p2 &#124;&#124; FEAT_SME2p2 |
|    00 |    1 | x    | 1   | FRINT64X                                                | FEAT_SVE2p2 &#124;&#124; FEAT_SME2p2 |
|    01 |    0 | 0    | x   | UNALLOCATED                                             | -                                    |
|    01 |    0 | 1    | 0   | SCVTF (predicated) - 16-bit to half- precision, zeroing | FEAT_SVE2p2 &#124;&#124; FEAT_SME2p2 |

|   opc |   o2 | o3   | U   | Instruction Details                                       | Feature                              |
|-------|------|------|-----|-----------------------------------------------------------|--------------------------------------|
|    01 |    0 | 1    | 1   | UCVTF (predicated) - 16-bit to half- precision, zeroing   | FEAT_SVE2p2 &#124;&#124; FEAT_SME2p2 |
|    01 |    1 | 0    | 0   | SCVTF (predicated) - 32-bit to half- precision, zeroing   | FEAT_SVE2p2 &#124;&#124; FEAT_SME2p2 |
|    01 |    1 | 0    | 1   | UCVTF (predicated) - 32-bit to half- precision, zeroing   | FEAT_SVE2p2 &#124;&#124; FEAT_SME2p2 |
|    01 |    1 | 1    | 0   | SCVTF (predicated) - 64-bit to half- precision, zeroing   | FEAT_SVE2p2 &#124;&#124; FEAT_SME2p2 |
|    01 |    1 | 1    | 1   | UCVTF (predicated) - 64-bit to half- precision, zeroing   | FEAT_SVE2p2 &#124;&#124; FEAT_SME2p2 |
|    10 |    0 | x    | x   | UNALLOCATED                                               | -                                    |
|    10 |    1 | 0    | 0   | SCVTF (predicated) - 32-bit to single- precision, zeroing | FEAT_SVE2p2 &#124;&#124; FEAT_SME2p2 |
|    10 |    1 | 0    | 1   | UCVTF (predicated) - 32-bit to single- precision, zeroing | FEAT_SVE2p2 &#124;&#124; FEAT_SME2p2 |
|    10 |    1 | 1    | x   | UNALLOCATED                                               | -                                    |
|    11 |    0 | 0    | 0   | SCVTF (predicated) - 32-bit to double- precision, zeroing | FEAT_SVE2p2 &#124;&#124; FEAT_SME2p2 |
|    11 |    0 | 0    | 1   | UCVTF (predicated) - 32-bit to double- precision, zeroing | FEAT_SVE2p2 &#124;&#124; FEAT_SME2p2 |
|    11 |    0 | 1    | x   | UNALLOCATED                                               | -                                    |
|    11 |    1 | 0    | 0   | SCVTF (predicated) - 64-bit to single- precision, zeroing | FEAT_SVE2p2 &#124;&#124; FEAT_SME2p2 |
|    11 |    1 | 0    | 1   | UCVTF (predicated) - 64-bit to single- precision, zeroing | FEAT_SVE2p2 &#124;&#124; FEAT_SME2p2 |
|    11 |    1 | 1    | 0   | SCVTF (predicated) - 64-bit to double- precision, zeroing | FEAT_SVE2p2 &#124;&#124; FEAT_SME2p2 |
|    11 |    1 | 1    | 1   | UCVTF (predicated) - 64-bit to double- precision, zeroing | FEAT_SVE2p2 &#124;&#124; FEAT_SME2p2 |

## Floating-point log and convert to integer

The encodings in this section are decoded from SVE2 floating-point unary operations - zeroing predicated.

<!-- image -->

| 31      | 24 23 22 21   | 17 16 15 14 13 12   | 10 9 5 4   |
|---------|---------------|---------------------|------------|
| 0 1 1 0 | 0 opc 0       | 1 o2 1 o3 U Pg Zn   | Zd         |

|   opc |   o2 | o3   | U   | Instruction Details   | Feature                              |
|-------|------|------|-----|-----------------------|--------------------------------------|
|    00 |    0 | x    | x   | FLOGB                 | FEAT_SVE2p2 &#124;&#124; FEAT_SME2p2 |
|    00 |    1 | x    | x   | UNALLOCATED           | -                                    |
|    01 |    0 | 0    | x   | UNALLOCATED           | -                                    |

|   opc |   o2 | o3   | U   | Instruction Details               |    |         | Feature                              |
|-------|------|------|-----|-----------------------------------|----|---------|--------------------------------------|
|    01 |    0 | 1    | 0   | FCVTZS - Half-precision zeroing   | to | 16-bit, | FEAT_SVE2p2 &#124;&#124; FEAT_SME2p2 |
|    01 |    0 | 1    | 1   | FCVTZU - Half-precision zeroing   | to | 16-bit, | FEAT_SVE2p2 &#124;&#124; FEAT_SME2p2 |
|    01 |    1 | 0    | 0   | FCVTZS - Half-precision zeroing   | to | 32-bit, | FEAT_SVE2p2 &#124;&#124; FEAT_SME2p2 |
|    01 |    1 | 0    | 1   | FCVTZU - Half-precision zeroing   | to | 32-bit, | FEAT_SVE2p2 &#124;&#124; FEAT_SME2p2 |
|    01 |    1 | 1    | 0   | FCVTZS - Half-precision zeroing   | to | 64-bit, | FEAT_SVE2p2 &#124;&#124; FEAT_SME2p2 |
|    01 |    1 | 1    | 1   | FCVTZU - Half-precision zeroing   | to | 64-bit, | FEAT_SVE2p2 &#124;&#124; FEAT_SME2p2 |
|    10 |    0 | x    | x   | UNALLOCATED                       |    |         | -                                    |
|    10 |    1 | 0    | 0   | FCVTZS - Single-precision zeroing | to | 32-bit, | FEAT_SVE2p2 &#124;&#124; FEAT_SME2p2 |
|    10 |    1 | 0    | 1   | FCVTZU - Single-precision zeroing | to | 32-bit, | FEAT_SVE2p2 &#124;&#124; FEAT_SME2p2 |
|    10 |    1 | 1    | x   | UNALLOCATED                       |    |         | -                                    |
|    11 |    0 | 0    | 0   | FCVTZS - Double-precision zeroing | to | 32-bit, | FEAT_SVE2p2 &#124;&#124; FEAT_SME2p2 |
|    11 |    0 | 0    | 1   | FCVTZU - Double-precision zeroing | to | 32-bit, | FEAT_SVE2p2 &#124;&#124; FEAT_SME2p2 |
|    11 |    0 | 1    | x   | UNALLOCATED                       |    |         | -                                    |
|    11 |    1 | 0    | 0   | FCVTZS - Single-precision zeroing | to | 64-bit, | FEAT_SVE2p2 &#124;&#124; FEAT_SME2p2 |
|    11 |    1 | 0    | 1   | FCVTZU - Single-precision zeroing | to | 64-bit, | FEAT_SVE2p2 &#124;&#124; FEAT_SME2p2 |
|    11 |    1 | 1    | 0   | FCVTZS - Double-precision zeroing | to | 64-bit, | FEAT_SVE2p2 &#124;&#124; FEAT_SME2p2 |
|    11 |    1 | 1    | 1   | FCVTZU - Double-precision zeroing | to | 64-bit, | FEAT_SVE2p2 &#124;&#124; FEAT_SME2p2 |

## SVE floating-point widening multiply-add - indexed

SVE floating-point widening multiply-add - indexed

The encodings in this section are decoded from SVE encodings.

<!-- image -->

| 31      | 24 23 22 21 20 16 15 14 13 12   |
|---------|---------------------------------|
| 0 1 1 0 | 0 op0 1 0 1 op1 0               |

|   op0 |   op1 | Instruction details                               |
|-------|-------|---------------------------------------------------|
|     0 |     0 | SVE BFloat16 floating-point dot product (indexed) |
|     0 |     1 | UNALLOCATED                                       |

## SVE BFloat16 floating-point dot product (indexed)

The encodings in this section are decoded from SVE floating-point widening multiply-add - indexed.

<!-- image -->

| 31    | 24 23 22 21 20 19 18 16 15 14 13 12 11 10 9   |
|-------|-----------------------------------------------|
| 0 1 1 | 0 0 op 1 i2 Zm 0 1 0 0 opc2 Zn                |

|   op | opc2   | Instruction Details                 | Feature                                                    |
|------|--------|-------------------------------------|------------------------------------------------------------|
|    0 | x1     | FDOT (2-way, indexed, FP8 to FP16)  | FEAT_SSVE_FP8DOT2 &#124;&#124; (FEAT_SVE2 &&FEAT_FP8DOT2)  |
|    0 | 00     | FDOT (2-way, indexed, FP16 to FP32) | FEAT_SME2 &#124;&#124; FEAT_SVE2p1                         |
|    0 | 10     | UNALLOCATED                         | -                                                          |
|    1 | 00     | BFDOT (indexed)                     | (FEAT_SVE &&FEAT_BF16) &#124;&#124; (FEAT_SME &&FEAT_BF16) |
|    1 | 01     | FDOT (4-way, indexed)               | FEAT_SSVE_FP8DOT4 &#124;&#124; (FEAT_SVE2 &&FEAT_FP8DOT4)  |
|    1 | 1x     | UNALLOCATED                         | -                                                          |

## SVE floating-point multiply-add long (indexed)

The encodings in this section are decoded from SVE floating-point widening multiply-add - indexed.

<!-- image -->

| 31    | 24 23 22 21   |
|-------|---------------|
| 0 1 1 | 0 1 o2 1      |

|   o2 |   op |   T | Instruction Details            | Feature                                                    |
|------|------|-----|--------------------------------|------------------------------------------------------------|
|    0 |    0 |   0 | FMLALB(indexed, FP16 to FP32)  | FEAT_SVE2 &#124;&#124; FEAT_SME                            |
|    0 |    0 |   1 | FMLALT (indexed, FP16 to FP32) | FEAT_SVE2 &#124;&#124; FEAT_SME                            |
|    0 |    1 |   0 | FMLSLB (indexed)               | FEAT_SVE2 &#124;&#124; FEAT_SME                            |
|    0 |    1 |   1 | FMLSLT (indexed)               | FEAT_SVE2 &#124;&#124; FEAT_SME                            |
|    1 |    0 |   0 | BFMLALB(indexed)               | (FEAT_SVE &&FEAT_BF16) &#124;&#124; (FEAT_SME &&FEAT_BF16) |
|    1 |    0 |   1 | BFMLALT (indexed)              | (FEAT_SVE &&FEAT_BF16) &#124;&#124; (FEAT_SME &&FEAT_BF16) |
|    1 |    1 |   0 | BFMLSLB (indexed)              | FEAT_SME2 &#124;&#124; FEAT_SVE2p1                         |
|    1 |    1 |   1 | BFMLSLT (indexed)              | FEAT_SME2 &#124;&#124; FEAT_SVE2p1                         |

|   op0 | op1   | Instruction details                            |
|-------|-------|------------------------------------------------|
|     1 | x     | SVE floating-point multiply-add long (indexed) |

## SVE floating-point widening multiply-add

SVE floating-point widening multiply-add

The encodings in this section are decoded from SVE encodings.

<!-- image -->

| 31   | 24 23 22 21   | 16 15 14 13 12 11 10   |
|------|---------------|------------------------|
| 0 1  | 0 op0 1       | 1 0 op1 0 0            |

|   op0 | op1   | Instruction details                     |
|-------|-------|-----------------------------------------|
|     0 | 0     | SVE BFloat16 floating-point dot product |
|     0 | 1     | UNALLOCATED                             |
|     1 | x     | SVE floating-point multiply-add long    |

## SVE BFloat16 floating-point dot product

The encodings in this section are decoded from SVE floating-point widening multiply-add.

<!-- image -->

|   op |   o2 | Instruction Details                 | Feature                                                    |
|------|------|-------------------------------------|------------------------------------------------------------|
|    0 |    0 | FDOT (2-way, vectors, FP16 to FP32) | FEAT_SME2 &#124;&#124; FEAT_SVE2p1                         |
|    0 |    1 | FDOT (2-way, vectors, FP8 to FP16)  | FEAT_SSVE_FP8DOT2 &#124;&#124; (FEAT_SVE2 &&FEAT_FP8DOT2)  |
|    1 |    0 | BFDOT (vectors)                     | (FEAT_SVE &&FEAT_BF16) &#124;&#124; (FEAT_SME &&FEAT_BF16) |
|    1 |    1 | FDOT (4-way, vectors)               | FEAT_SSVE_FP8DOT4 &#124;&#124; (FEAT_SVE2 &&FEAT_FP8DOT4)  |

## SVE floating-point multiply-add long

The encodings in this section are decoded from SVE floating-point widening multiply-add.

<!-- image -->

|   o2 |   op |   T | Instruction Details            | Feature                                                    |
|------|------|-----|--------------------------------|------------------------------------------------------------|
|    0 |    0 |   0 | FMLALB(vectors, FP16 to FP32)  | FEAT_SVE2 &#124;&#124; FEAT_SME                            |
|    0 |    0 |   1 | FMLALT (vectors, FP16 to FP32) | FEAT_SVE2 &#124;&#124; FEAT_SME                            |
|    0 |    1 |   0 | FMLSLB (vectors)               | FEAT_SVE2 &#124;&#124; FEAT_SME                            |
|    0 |    1 |   1 | FMLSLT (vectors)               | FEAT_SVE2 &#124;&#124; FEAT_SME                            |
|    1 |    0 |   0 | BFMLALB(vectors)               | (FEAT_SVE &&FEAT_BF16) &#124;&#124; (FEAT_SME &&FEAT_BF16) |
|    1 |    0 |   1 | BFMLALT (vectors)              | (FEAT_SVE &&FEAT_BF16) &#124;&#124; (FEAT_SME &&FEAT_BF16) |
|    1 |    1 |   0 | BFMLSLB (vectors)              | FEAT_SME2 &#124;&#124; FEAT_SVE2p1                         |
|    1 |    1 |   1 | BFMLSLT (vectors)              | FEAT_SME2 &#124;&#124; FEAT_SVE2p1                         |

## SVE floating-point unary operations - unpredicated

SVE floating-point unary operations - unpredicated

The encodings in this section are decoded from SVE encodings.

<!-- image -->

| 31   | 24 23 22 21 19 18   |     | 16 15     | 12 11 10   | 9   | 6 5   |
|------|---------------------|-----|-----------|------------|-----|-------|
| 0 1  | 1 0 0 1 0 1         | op0 | 0 0 1 op1 | 0 0 1 1    | op2 | op3   |

| op0   | op1   | op2   | op3   | Instruction details                                   |
|-------|-------|-------|-------|-------------------------------------------------------|
| 00    | 00x   | xx    | x     | SVE2 FP8 upconverts                                   |
| 00    | 010   | xx    | 0     | SVE2 FP8 downconverts                                 |
| 00    | 010   | xx    | 1     | UNALLOCATED                                           |
| 00    | 011   | xx    | x     | UNALLOCATED                                           |
| xx    | 10x   | xx    | x     | UNALLOCATED                                           |
| xx    | 11x   | 00    | x     | SVE floating-point reciprocal estimate (unpredicated) |
| xx    | 11x   | != 00 | x     | UNALLOCATED                                           |
| != 00 | 0xx   | xx    | x     | UNALLOCATED                                           |

## SVE2 FP8 upconverts

The encodings in this section are decoded from SVE floating-point unary operations - unpredicated.

<!-- image -->

|   L |   opc | Instruction Details         | Feature                                                    |
|-----|-------|-----------------------------|------------------------------------------------------------|
|   0 |    00 | F1CVT,F2CVT-F1CVT           | (FEAT_SVE2 &&FEAT_FP8) &#124;&#124; (FEAT_SME2 &&FEAT_FP8) |
|   0 |    01 | F1CVT,F2CVT-F2CVT           | (FEAT_SVE2 &&FEAT_FP8) &#124;&#124; (FEAT_SME2 &&FEAT_FP8) |
|   0 |    10 | BF1CVT,BF2CVT-BF1CVT        | (FEAT_SVE2 &&FEAT_FP8) &#124;&#124; (FEAT_SME2 &&FEAT_FP8) |
|   0 |    11 | BF1CVT,BF2CVT-BF2CVT        | (FEAT_SVE2 &&FEAT_FP8) &#124;&#124; (FEAT_SME2 &&FEAT_FP8) |
|   1 |    00 | F1CVTLT, F2CVTLT-F1CVTLT    | (FEAT_SVE2 &&FEAT_FP8) &#124;&#124; (FEAT_SME2 &&FEAT_FP8) |
|   1 |    01 | F1CVTLT, F2CVTLT-F2CVTLT    | (FEAT_SVE2 &&FEAT_FP8) &#124;&#124; (FEAT_SME2 &&FEAT_FP8) |
|   1 |    10 | BF1CVTLT, BF2CVTLT-BF1CVTLT | (FEAT_SVE2 &&FEAT_FP8) &#124;&#124; (FEAT_SME2 &&FEAT_FP8) |
|   1 |    11 | BF1CVTLT, BF2CVTLT-BF2CVTLT | (FEAT_SVE2 &&FEAT_FP8) &#124;&#124; (FEAT_SME2 &&FEAT_FP8) |

## SVE2 FP8 downconverts

The encodings in this section are decoded from SVE floating-point unary operations - unpredicated.

<!-- image -->

|   opc | Instruction Details   | Feature                                                    |
|-------|-----------------------|------------------------------------------------------------|
|    00 | FCVTN                 | (FEAT_SVE2 &&FEAT_FP8) &#124;&#124; (FEAT_SME2 &&FEAT_FP8) |
|    01 | FCVTNB                | (FEAT_SVE2 &&FEAT_FP8) &#124;&#124; (FEAT_SME2 &&FEAT_FP8) |
|    10 | BFCVTN                | (FEAT_SVE2 &&FEAT_FP8) &#124;&#124; (FEAT_SME2 &&FEAT_FP8) |
|    11 | FCVTNT (unpredicated) | (FEAT_SVE2 &&FEAT_FP8) &#124;&#124; (FEAT_SME2 &&FEAT_FP8) |

## SVE floating-point reciprocal estimate (unpredicated)

The encodings in this section are decoded from SVE floating-point unary operations - unpredicated.

<!-- image -->

|   op | Instruction Details   | Feature                        |
|------|-----------------------|--------------------------------|
|    0 | FRECPE                | FEAT_SVE &#124;&#124; FEAT_SME |
|    1 | FRSQRTE               | FEAT_SVE &#124;&#124; FEAT_SME |

## SVE floating-point compare - with zero

SVE floating-point compare - with zero

The encodings in this section are decoded from SVE encodings.

<!-- image -->

| 31    | 23 22 21 19 18 17 16 15   |
|-------|---------------------------|
| 0 1 1 | 0 1 0 op0 0 0             |

|   op0 | Instruction details                  |
|-------|--------------------------------------|
|     0 | SVE floating-point compare with zero |
|     1 | UNALLOCATED                          |

## SVE floating-point compare with zero

The encodings in this section are decoded from SVE floating-point compare - with zero.

<!-- image -->

|   eq | lt   |   ne | Instruction Details                      | Feature                        |
|------|------|------|------------------------------------------|--------------------------------|
|    0 | 0    |    0 | FCM < cc > (zero) -Greater than or equal | FEAT_SVE &#124;&#124; FEAT_SME |
|    0 | 0    |    1 | FCM < cc > (zero) -Greater than          | FEAT_SVE &#124;&#124; FEAT_SME |
|    0 | 1    |    0 | FCM < cc > (zero) -Less than             | FEAT_SVE &#124;&#124; FEAT_SME |
|    0 | 1    |    1 | FCM < cc > (zero) -Less than or equal    | FEAT_SVE &#124;&#124; FEAT_SME |
|    1 | x    |    1 | UNALLOCATED                              | -                              |
|    1 | 0    |    0 | FCM < cc > (zero) -Equal                 | FEAT_SVE &#124;&#124; FEAT_SME |
|    1 | 1    |    0 | FCM < cc > (zero) -Notequal              | FEAT_SVE &#124;&#124; FEAT_SME |

## SVE floating-point accumulating reduction

SVE floating-point accumulating reduction

The encodings in this section are decoded from SVE encodings.

<!-- image -->

## SVE floating-point serial reduction (predicated)

The encodings in this section are decoded from SVE floating-point accumulating reduction.

<!-- image -->

| opc   | Instruction Details   | Feature   |
|-------|-----------------------|-----------|
| 00    | FADDA                 | FEAT_SVE  |
| != 00 | UNALLOCATED           | -         |

## SVE floating-point arithmetic - predicated

SVE floating-point arithmetic - predicated

The encodings in this section are decoded from SVE encodings.

<!-- image -->

| 31      | 24 23 22 21 20 19 18 16 15 13   |
|---------|---------------------------------|
| 0 1 1 0 | 1 0 op0 1 0 0                   |

| op0   | op1    | op2     | Instruction details                                       | Feature   |
|-------|--------|---------|-----------------------------------------------------------|-----------|
| 0x    | xxx    | xxxx    | SVE floating-point arithmetic (predicated)                | -         |
| 10    | 000    | xxxx    | FTMAD                                                     | FEAT_SVE  |
| 10    | != 000 | xxxx    | UNALLOCATED                                               | -         |
| 11    | xxx    | 0000    | SVE floating-point arithmetic with immediate (predicated) | -         |
| 11    | xxx    | != 0000 | UNALLOCATED                                               | -         |

## SVE floating-point arithmetic (predicated)

The encodings in this section are decoded from SVE floating-point arithmetic - predicated.

|   op0 | Instruction details                              |
|-------|--------------------------------------------------|
|     0 | SVE floating-point serial reduction (predicated) |
|     1 | UNALLOCATED                                      |

<!-- image -->

| size   |   opc | Instruction Details        | Feature                                                              |
|--------|-------|----------------------------|----------------------------------------------------------------------|
| xx     |  0011 | FSUBR (vectors)            | FEAT_SVE &#124;&#124; FEAT_SME                                       |
| xx     |  1000 | FABD                       | FEAT_SVE &#124;&#124; FEAT_SME                                       |
| xx     |  1010 | FMULX                      | FEAT_SVE &#124;&#124; FEAT_SME                                       |
| xx     |  1011 | UNALLOCATED                | -                                                                    |
| xx     |  1100 | FDIVR                      | FEAT_SVE &#124;&#124; FEAT_SME                                       |
| xx     |  1101 | FDIV                       | FEAT_SVE &#124;&#124; FEAT_SME                                       |
| xx     |  1110 | FAMAX                      | (FEAT_SVE2 &&FEAT_FAMINMAX) &#124;&#124; (FEAT_SME2 &&FEAT_FAMINMAX) |
| xx     |  1111 | FAMIN                      | (FEAT_SVE2 &&FEAT_FAMINMAX) &#124;&#124; (FEAT_SME2 &&FEAT_FAMINMAX) |
| 00     |  0000 | BFADD(predicated)          | FEAT_SVE_B16B16                                                      |
| 00     |  0001 | BFSUB (predicated)         | FEAT_SVE_B16B16                                                      |
| 00     |  0010 | BFMUL(vectors, predicated) | FEAT_SVE_B16B16                                                      |
| 00     |  0100 | BFMAXNM                    | FEAT_SVE_B16B16                                                      |
| 00     |  0101 | BFMINNM                    | FEAT_SVE_B16B16                                                      |
| 00     |  0110 | BFMAX                      | FEAT_SVE_B16B16                                                      |
| 00     |  0111 | BFMIN                      | FEAT_SVE_B16B16                                                      |
| 00     |  1001 | BFSCALE                    | FEAT_SVE_BFSCALE                                                     |
| != 00  |  0000 | FADD(vectors, predicated)  | FEAT_SVE &#124;&#124; FEAT_SME                                       |
| != 00  |  0001 | FSUB (vectors, predicated) | FEAT_SVE &#124;&#124; FEAT_SME                                       |
| != 00  |  0010 | FMUL(vectors, predicated)  | FEAT_SVE &#124;&#124; FEAT_SME                                       |
| != 00  |  0100 | FMAXNM(vectors)            | FEAT_SVE &#124;&#124; FEAT_SME                                       |
| != 00  |  0101 | FMINNM(vectors)            | FEAT_SVE &#124;&#124; FEAT_SME                                       |
| != 00  |  0110 | FMAX(vectors)              | FEAT_SVE &#124;&#124; FEAT_SME                                       |
| != 00  |  0111 | FMIN (vectors)             | FEAT_SVE &#124;&#124; FEAT_SME                                       |
| != 00  |  1001 | FSCALE                     | FEAT_SVE &#124;&#124; FEAT_SME                                       |

## SVE floating-point arithmetic with immediate (predicated)

The encodings in this section are decoded from SVE floating-point arithmetic - predicated.

<!-- image -->

|   opc | Instruction Details   | Feature                        |
|-------|-----------------------|--------------------------------|
|   000 | FADD(immediate)       | FEAT_SVE &#124;&#124; FEAT_SME |
|   001 | FSUB (immediate)      | FEAT_SVE &#124;&#124; FEAT_SME |
|   010 | FMUL(immediate)       | FEAT_SVE &#124;&#124; FEAT_SME |
|   011 | FSUBR (immediate)     | FEAT_SVE &#124;&#124; FEAT_SME |
|   100 | FMAXNM(immediate)     | FEAT_SVE &#124;&#124; FEAT_SME |
|   101 | FMINNM(immediate)     | FEAT_SVE &#124;&#124; FEAT_SME |
|   110 | FMAX(immediate)       | FEAT_SVE &#124;&#124; FEAT_SME |
|   111 | FMIN (immediate)      | FEAT_SVE &#124;&#124; FEAT_SME |

## SVE floating-point unary operations - merging predicated

SVE floating-point unary operations - merging predicated

The encodings in this section are decoded from SVE encodings.

<!-- image -->

| 31          | 24 23 22 21 20 18 17 16 15   |
|-------------|------------------------------|
| 0 1 1 0 0 1 | 1 0 op0 1 0                  |

| op0   | Instruction details                        |
|-------|--------------------------------------------|
| 00x   | SVE floating-point round to integral value |
| 010   | SVE floating-point convert precision       |
| 011   | SVE floating-point unary operations        |
| 10x   | SVE integer convert to floating-point      |
| 11x   | SVE floating-point convert to integer      |

## SVE floating-point round to integral value

The encodings in this section are decoded from SVE floating-point unary operations - merging predicated.

<!-- image -->

|   opc | Instruction Details                              | Feature                        |
|-------|--------------------------------------------------|--------------------------------|
|   000 | FRINT < r > - Nearest with ties to even, merging | FEAT_SVE &#124;&#124; FEAT_SME |
|   001 | FRINT < r > - Toward plus infinity, merging      | FEAT_SVE &#124;&#124; FEAT_SME |

|   opc | Instruction Details                                    | Feature                        |
|-------|--------------------------------------------------------|--------------------------------|
|   010 | FRINT < r > - Toward minus infinity, merging           | FEAT_SVE &#124;&#124; FEAT_SME |
|   011 | FRINT < r > -Toward zero, merging                      | FEAT_SVE &#124;&#124; FEAT_SME |
|   100 | FRINT < r > -Nearest with ties to away, merging        | FEAT_SVE &#124;&#124; FEAT_SME |
|   101 | UNALLOCATED                                            | -                              |
|   110 | FRINT < r > - Current mode signalling inexact, merging | FEAT_SVE &#124;&#124; FEAT_SME |
|   111 | FRINT < r > -Current mode, merging                     | FEAT_SVE &#124;&#124; FEAT_SME |

## SVE floating-point convert precision

The encodings in this section are decoded from SVE floating-point unary operations - merging predicated.

<!-- image -->

| 31    | 24 23 22 21 20 18 17 16 15 13 12 10 9   |
|-------|-----------------------------------------|
| 0 1 1 | 1 opc 0 0 1 0 opc2 1 0 1 Pg Zn          |

| opc   | opc2   | Instruction Details                                   | Feature                                                    |
|-------|--------|-------------------------------------------------------|------------------------------------------------------------|
| x0    | 11     | UNALLOCATED                                           | -                                                          |
| 00    | 0x     | UNALLOCATED                                           | -                                                          |
| 00    | 10     | FCVTX                                                 | FEAT_SVE2 &#124;&#124; FEAT_SME                            |
| 01    | xx     | UNALLOCATED                                           | -                                                          |
| 10    | 00     | FCVT - Single-precision to half- precision, merging   | FEAT_SVE &#124;&#124; FEAT_SME                             |
| 10    | 01     | FCVT - Half-precision to single- precision, merging   | FEAT_SVE &#124;&#124; FEAT_SME                             |
| 10    | 10     | BFCVT                                                 | (FEAT_SVE &&FEAT_BF16) &#124;&#124; (FEAT_SME &&FEAT_BF16) |
| 11    | 00     | FCVT - Double-precision to half- precision, merging   | FEAT_SVE &#124;&#124; FEAT_SME                             |
| 11    | 01     | FCVT - Half-precision to double- precision, merging   | FEAT_SVE &#124;&#124; FEAT_SME                             |
| 11    | 10     | FCVT - Double-precision to single- precision, merging | FEAT_SVE &#124;&#124; FEAT_SME                             |
| 11    | 11     | FCVT - Single-precision to double- precision, merging | FEAT_SVE &#124;&#124; FEAT_SME                             |

## SVE floating-point unary operations

The encodings in this section are decoded from SVE floating-point unary operations - merging predicated.

<!-- image -->

| opc   | Instruction Details   | Feature                        |
|-------|-----------------------|--------------------------------|
| 00    | FRECPX                | FEAT_SVE &#124;&#124; FEAT_SME |
| 01    | FSQRT                 | FEAT_SVE &#124;&#124; FEAT_SME |
| 1x    | UNALLOCATED           | -                              |

## SVE integer convert to floating-point

The encodings in this section are decoded from SVE floating-point unary operations - merging predicated.

<!-- image -->

|   opc | opc2   | U   | Instruction Details                                       | Feature                              |
|-------|--------|-----|-----------------------------------------------------------|--------------------------------------|
|    00 | 0x     | 0   | FRINT32Z                                                  | FEAT_SVE2p2 &#124;&#124; FEAT_SME2p2 |
|    00 | 0x     | 1   | FRINT32X                                                  | FEAT_SVE2p2 &#124;&#124; FEAT_SME2p2 |
|    00 | 1x     | 0   | FRINT64Z                                                  | FEAT_SVE2p2 &#124;&#124; FEAT_SME2p2 |
|    00 | 1x     | 1   | FRINT64X                                                  | FEAT_SVE2p2 &#124;&#124; FEAT_SME2p2 |
|    01 | 00     | x   | UNALLOCATED                                               | -                                    |
|    01 | 01     | 0   | SCVTF (predicated) - 16-bit to half- precision, merging   | FEAT_SVE &#124;&#124; FEAT_SME       |
|    01 | 01     | 1   | UCVTF (predicated) - 16-bit to half- precision, merging   | FEAT_SVE &#124;&#124; FEAT_SME       |
|    01 | 10     | 0   | SCVTF (predicated) - 32-bit to half- precision, merging   | FEAT_SVE &#124;&#124; FEAT_SME       |
|    01 | 10     | 1   | UCVTF (predicated) - 32-bit to half- precision, merging   | FEAT_SVE &#124;&#124; FEAT_SME       |
|    01 | 11     | 0   | SCVTF (predicated) - 64-bit to half- precision, merging   | FEAT_SVE &#124;&#124; FEAT_SME       |
|    01 | 11     | 1   | UCVTF (predicated) - 64-bit to half- precision, merging   | FEAT_SVE &#124;&#124; FEAT_SME       |
|    10 | 10     | 0   | SCVTF (predicated) - 32-bit to single- precision, merging | FEAT_SVE &#124;&#124; FEAT_SME       |
|    10 | 10     | 1   | UCVTF (predicated) - 32-bit to single- precision, merging | FEAT_SVE &#124;&#124; FEAT_SME       |
|    10 | != 10  | x   | UNALLOCATED                                               | -                                    |

|   opc |   opc2 | U   | Instruction Details                                       | Feature                        |
|-------|--------|-----|-----------------------------------------------------------|--------------------------------|
|    11 |     00 | 0   | SCVTF (predicated) - 32-bit to double- precision, merging | FEAT_SVE &#124;&#124; FEAT_SME |
|    11 |     00 | 1   | UCVTF (predicated) - 32-bit to double- precision, merging | FEAT_SVE &#124;&#124; FEAT_SME |
|    11 |     01 | x   | UNALLOCATED                                               | -                              |
|    11 |     10 | 0   | SCVTF (predicated) - 64-bit to single- precision, merging | FEAT_SVE &#124;&#124; FEAT_SME |
|    11 |     10 | 1   | UCVTF (predicated) - 64-bit to single- precision, merging | FEAT_SVE &#124;&#124; FEAT_SME |
|    11 |     11 | 0   | SCVTF (predicated) - 64-bit to double- precision, merging | FEAT_SVE &#124;&#124; FEAT_SME |
|    11 |     11 | 1   | UCVTF (predicated) - 64-bit to double- precision, merging | FEAT_SVE &#124;&#124; FEAT_SME |

## SVE floating-point convert to integer

The encodings in this section are decoded from SVE floating-point unary operations - merging predicated.

<!-- image -->

|   opc | opc2   | U   | Instruction Details                          | Feature                         |
|-------|--------|-----|----------------------------------------------|---------------------------------|
|    00 | xx     | 0   | FLOGB                                        | FEAT_SVE2 &#124;&#124; FEAT_SME |
|    00 | xx     | 1   | UNALLOCATED                                  | -                               |
|    01 | 00     | x   | UNALLOCATED                                  | -                               |
|    01 | 01     | 0   | FCVTZS - Half-precision to 16-bit, merging   | FEAT_SVE &#124;&#124; FEAT_SME  |
|    01 | 01     | 1   | FCVTZU - Half-precision to 16-bit, merging   | FEAT_SVE &#124;&#124; FEAT_SME  |
|    01 | 10     | 0   | FCVTZS - Half-precision to 32-bit, merging   | FEAT_SVE &#124;&#124; FEAT_SME  |
|    01 | 10     | 1   | FCVTZU - Half-precision to 32-bit, merging   | FEAT_SVE &#124;&#124; FEAT_SME  |
|    01 | 11     | 0   | FCVTZS - Half-precision to 64-bit, merging   | FEAT_SVE &#124;&#124; FEAT_SME  |
|    01 | 11     | 1   | FCVTZU - Half-precision to 64-bit, merging   | FEAT_SVE &#124;&#124; FEAT_SME  |
|    10 | 10     | 0   | FCVTZS - Single-precision to 32-bit, merging | FEAT_SVE &#124;&#124; FEAT_SME  |
|    10 | 10     | 1   | FCVTZU - Single-precision to 32-bit, merging | FEAT_SVE &#124;&#124; FEAT_SME  |
|    10 | != 10  | x   | UNALLOCATED                                  | -                               |

|   opc |   opc2 | U   | Instruction Details                          | Feature                        |
|-------|--------|-----|----------------------------------------------|--------------------------------|
|    11 |     00 | 0   | FCVTZS - Double-precision to 32-bit, merging | FEAT_SVE &#124;&#124; FEAT_SME |
|    11 |     00 | 1   | FCVTZU - Double-precision to 32-bit, merging | FEAT_SVE &#124;&#124; FEAT_SME |
|    11 |     01 | x   | UNALLOCATED                                  | -                              |
|    11 |     10 | 0   | FCVTZS - Single-precision to 64-bit, merging | FEAT_SVE &#124;&#124; FEAT_SME |
|    11 |     10 | 1   | FCVTZU - Single-precision to 64-bit, merging | FEAT_SVE &#124;&#124; FEAT_SME |
|    11 |     11 | 0   | FCVTZS - Double-precision to 64-bit, merging | FEAT_SVE &#124;&#124; FEAT_SME |
|    11 |     11 | 1   | FCVTZU - Double-precision to 64-bit, merging | FEAT_SVE &#124;&#124; FEAT_SME |

## SVE floating-point multiply-add

SVE floating-point multiply-add

The encodings in this section are decoded from SVE encodings.

<!-- image -->

| 31   | 16 15   |
|------|---------|
| 0 1  | op0     |

|   op0 | Instruction details                                         |
|-------|-------------------------------------------------------------|
|     0 | SVE floating-point multiply-accumulate writing addend       |
|     1 | SVE floating-point multiply-accumulate writing multiplicand |

## SVE floating-point multiply-accumulate writing addend

The encodings in this section are decoded from SVE floating-point multiply-add.

<!-- image -->

|   size |   opc | Instruction Details   | Feature         |
|--------|-------|-----------------------|-----------------|
|     00 |    00 | BFMLA(vectors)        | FEAT_SVE_B16B16 |
|     00 |    01 | BFMLS (vectors)       | FEAT_SVE_B16B16 |

| size   | opc   | Instruction Details   | Feature                        |
|--------|-------|-----------------------|--------------------------------|
| 00     | 1x    | UNALLOCATED           | -                              |
| != 00  | 00    | FMLA(vectors)         | FEAT_SVE &#124;&#124; FEAT_SME |
| != 00  | 01    | FMLS (vectors)        | FEAT_SVE &#124;&#124; FEAT_SME |
| != 00  | 10    | FNMLA                 | FEAT_SVE &#124;&#124; FEAT_SME |
| != 00  | 11    | FNMLS                 | FEAT_SVE &#124;&#124; FEAT_SME |

## SVE floating-point multiply-accumulate writing multiplicand

The encodings in this section are decoded from SVE floating-point multiply-add.

<!-- image -->

| 31    | 24 23 22 21 20 16 15 14 13 12 10 9   |
|-------|--------------------------------------|
| 0 1 1 | 1 size 1 Za 1 opc Pg Zm              |

|   opc | Instruction Details   | Feature   |                       |
|-------|-----------------------|-----------|-----------------------|
|    00 | FMAD                  | FEAT_SVE  | &#124;&#124; FEAT_SME |
|    01 | FMSB                  | FEAT_SVE  | &#124;&#124; FEAT_SME |
|    10 | FNMAD                 | FEAT_SVE  | &#124;&#124; FEAT_SME |
|    11 | FNMSB                 | FEAT_SVE  | &#124;&#124; FEAT_SME |

## SVE Memory - 32-bit Gather and Unsized Contiguous

SVE Memory - 32-bit Gather and Unsized Contiguous

The encodings in this section are decoded from SVE encodings.

<!-- image -->

| 31    | 25 24 23 22 21 20 16 15   | 5 4 3   |
|-------|---------------------------|---------|
| 1 0 0 | 0 op0 op1 op2             | op3     |

|   op0 | op1   | op2   | op3   | Instruction details                                                  | Feature                        |
|-------|-------|-------|-------|----------------------------------------------------------------------|--------------------------------|
|    00 | x1    | 0xx   | 0     | SVE 32-bit gather prefetch (scalar plus 32- bit scaled offsets)      | -                              |
|    00 | x1    | 0xx   | 1     | UNALLOCATED                                                          | -                              |
|    01 | x1    | 0xx   | x     | SVE 32-bit gather load halfwords (scalar plus 32-bit scaled offsets) | -                              |
|    10 | x1    | 0xx   | x     | SVE 32-bit gather load words (scalar plus 32-bit scaled offsets)     | -                              |
|    11 | 0x    | 000   | 0     | LDR(predicate)                                                       | FEAT_SVE &#124;&#124; FEAT_SME |

| op0   | op1   | op2   | op3   | Instruction details                                          | Feature                        |
|-------|-------|-------|-------|--------------------------------------------------------------|--------------------------------|
| 11    | 0x    | 000   | 1     | UNALLOCATED                                                  | -                              |
| 11    | 0x    | 010   | x     | LDR(vector)                                                  | FEAT_SVE &#124;&#124; FEAT_SME |
| 11    | 0x    | 0x1   | x     | UNALLOCATED                                                  | -                              |
| 11    | 1x    | 0xx   | 0     | SVE contiguous prefetch (scalar plus immediate)              | -                              |
| 11    | 1x    | 0xx   | 1     | UNALLOCATED                                                  | -                              |
| xx    | 00    | 10x   | x     | SVE2 32-bit gather non-temporal load (vector plus scalar)    | -                              |
| xx    | 00    | 110   | 0     | SVE contiguous prefetch (scalar plus scalar)                 | -                              |
| xx    | 00    | 111   | 0     | SVE 32-bit gather prefetch (vector plus immediate)           | -                              |
| xx    | 00    | 11x   | 1     | UNALLOCATED                                                  | -                              |
| xx    | 01    | 1xx   | x     | SVE 32-bit gather load (vector plus immediate)               | -                              |
| xx    | 1x    | 1xx   | x     | SVE load and broadcast element                               | -                              |
| != 11 | x0    | 0xx   | x     | SVE 32-bit gather load (scalar plus 32-bit unscaled offsets) | -                              |

## SVE 32-bit gather prefetch (scalar plus 32-bit scaled offsets)

The encodings in this section are decoded from SVE Memory - 32-bit Gather and Unsized Contiguous.

<!-- image -->

|   31 | 25 24 23 22 21   | 20 16 15 14 13 12   | 10 9   |   5 4 3 |       |
|------|------------------|---------------------|--------|---------|-------|
|    1 | 0 0 0 1 0 0 0 1  | xs Zm 0 msz         | Pg     |       0 | prfop |

|   msz | Instruction Details       | Feature   |
|-------|---------------------------|-----------|
|    00 | PRFB (scalar plus vector) | FEAT_SVE  |
|    01 | PRFH (scalar plus vector) | FEAT_SVE  |
|    10 | PRFW(scalar plus vector)  | FEAT_SVE  |
|    11 | PRFD (scalar plus vector) | FEAT_SVE  |

## SVE 32-bit gather load halfwords (scalar plus 32-bit scaled offsets)

The encodings in this section are decoded from SVE Memory - 32-bit Gather and Unsized Contiguous.

<!-- image -->

| 31   | 25 24 23 22 21 20   | 16 15 14 13 12   | 10 9   | 5   | 4   |
|------|---------------------|------------------|--------|-----|-----|
| 1 0  | 0 0 1 0 0 1 xs 1    | 0 U ff           | Pg     | Rn  | Zt  |

|   U |   ff | Instruction Details          | Feature   |
|-----|------|------------------------------|-----------|
|   0 |    0 | LD1SH (scalar plus vector)   | FEAT_SVE  |
|   0 |    1 | LDFF1SH (scalar plus vector) | FEAT_SVE  |
|   1 |    0 | LD1H (scalar plus vector)    | FEAT_SVE  |
|   1 |    1 | LDFF1H (scalar plus vector)  | FEAT_SVE  |

## SVE 32-bit gather load words (scalar plus 32-bit scaled offsets)

The encodings in this section are decoded from SVE Memory - 32-bit Gather and Unsized Contiguous.

<!-- image -->

|   31 | 25 24 23 22 21 20   | 16 15   |    |    |    |    | 14   | 13   | 12   | 10   | 5   | 0   |
|------|---------------------|---------|----|----|----|----|------|------|------|------|-----|-----|
|    1 | 0 0 0 0 1           | 0 1 0   | xs |  1 | Zm |  0 | U    |      | ff   |      | Rn  | Zt  |

|   U | ff   | Instruction Details         | Feature   |
|-----|------|-----------------------------|-----------|
|   0 | x    | UNALLOCATED                 | -         |
|   1 | 0    | LD1W(scalar plus vector)    | FEAT_SVE  |
|   1 | 1    | LDFF1W (scalar plus vector) | FEAT_SVE  |

## SVE contiguous prefetch (scalar plus immediate)

The encodings in this section are decoded from SVE Memory - 32-bit Gather and Unsized Contiguous.

<!-- image -->

| 31    | 25 24 23 22 21        | 16 15 14 13 12 10 9 5 4 3   |
|-------|-----------------------|-----------------------------|
| 1 0 0 | 0 1 1 1 imm6 0 msz Pg | Rn 0 prfop                  |

|   msz | Instruction Details          | Feature   |                       |          |
|-------|------------------------------|-----------|-----------------------|----------|
|    00 | PRFB (scalar plus immediate) | FEAT_SVE  | &#124;&#124; FEAT_SME |          |
|    01 | PRFH (scalar plus immediate) | FEAT_SVE  | &#124;&#124;          | FEAT_SME |
|    10 | PRFW(scalar plus immediate)  | FEAT_SVE  | &#124;&#124; FEAT_SME |          |
|    11 | PRFD (scalar plus immediate) | FEAT_SVE  | &#124;&#124; FEAT_SME |          |

## SVE2 32-bit gather non-temporal load (vector plus scalar)

The encodings in this section are decoded from SVE Memory - 32-bit Gather and Unsized Contiguous.

<!-- image -->

| 31          | 25 24 23 22 21 20   | 16 15 14    | 13 12 10 9 5 4   |
|-------------|---------------------|-------------|------------------|
| 1 0 0 0 0 1 | 0 msz 0 0           | Rm 1 0 U Pg | Zn Zt            |

|   msz | U   | Instruction Details         | Feature   |
|-------|-----|-----------------------------|-----------|
|    00 | 0   | LDNT1SB                     | FEAT_SVE2 |
|    00 | 1   | LDNT1B (vector plus scalar) | FEAT_SVE2 |
|    01 | 0   | LDNT1SH                     | FEAT_SVE2 |
|    01 | 1   | LDNT1H (vector plus scalar) | FEAT_SVE2 |
|    10 | 0   | UNALLOCATED                 | -         |
|    10 | 1   | LDNT1W(vector plus scalar)  | FEAT_SVE2 |
|    11 | x   | UNALLOCATED                 | -         |

## SVE contiguous prefetch (scalar plus scalar)

The encodings in this section are decoded from SVE Memory - 32-bit Gather and Unsized Contiguous.

<!-- image -->

| msz   | Rm       | Instruction Details       | Feature                        |
|-------|----------|---------------------------|--------------------------------|
| xx    | 11111    | UNALLOCATED               | -                              |
| 00    | != 11111 | PRFB (scalar plus scalar) | FEAT_SVE &#124;&#124; FEAT_SME |
| 01    | != 11111 | PRFH (scalar plus scalar) | FEAT_SVE &#124;&#124; FEAT_SME |
| 10    | != 11111 | PRFW(scalar plus scalar)  | FEAT_SVE &#124;&#124; FEAT_SME |
| 11    | != 11111 | PRFD (scalar plus scalar) | FEAT_SVE &#124;&#124; FEAT_SME |

## SVE 32-bit gather prefetch (vector plus immediate)

The encodings in this section are decoded from SVE Memory - 32-bit Gather and Unsized Contiguous.

<!-- image -->

| 31    | 25 24 23 22 21 20   | 16 15   | 13 12   | 10   |    |   5 4 | 0     |
|-------|---------------------|---------|---------|------|----|-------|-------|
| 1 0 0 | 0 msz 0 0           | imm5    | 1 1 1   | Pg   | Zn |     0 | prfop |

## SVE 32-bit gather load (vector plus immediate)

The encodings in this section are decoded from SVE Memory - 32-bit Gather and Unsized Contiguous.

<!-- image -->

| 31    | 24 23 22 21   | 20   | 16        | 15 14 13 12 10 9   | 5 4   |
|-------|---------------|------|-----------|--------------------|-------|
| 1 0 0 | msz           | 0 1  | 1 U ff Pg | Zn                 | Zt    |

|   msz | U   | ff   | Instruction Details             | Feature   |
|-------|-----|------|---------------------------------|-----------|
|    00 | 0   | 0    | LD1SB (vector plus immediate)   | FEAT_SVE  |
|    00 | 0   | 1    | LDFF1SB (vector plus immediate) | FEAT_SVE  |
|    00 | 1   | 0    | LD1B (vector plus immediate)    | FEAT_SVE  |
|    00 | 1   | 1    | LDFF1B (vector plus immediate)  | FEAT_SVE  |
|    01 | 0   | 0    | LD1SH (vector plus immediate)   | FEAT_SVE  |
|    01 | 0   | 1    | LDFF1SH (vector plus immediate) | FEAT_SVE  |
|    01 | 1   | 0    | LD1H (vector plus immediate)    | FEAT_SVE  |
|    01 | 1   | 1    | LDFF1H (vector plus immediate)  | FEAT_SVE  |
|    10 | 0   | x    | UNALLOCATED                     | -         |
|    10 | 1   | 0    | LD1W(vector plus immediate)     | FEAT_SVE  |
|    10 | 1   | 1    | LDFF1W (vector plus immediate)  | FEAT_SVE  |
|    11 | x   | x    | UNALLOCATED                     | -         |

## SVE load and broadcast element

The encodings in this section are decoded from SVE Memory - 32-bit Gather and Unsized Contiguous.

<!-- image -->

| 31   | 25 24 23 22              | 21   | 16 15 14 13 12 10 9 5 4   |
|------|--------------------------|------|---------------------------|
| 1 0  | 0 dtypeh 1 imm6 1 dtypel | Pg   | Rn Zt                     |

|   msz | Instruction Details          | Feature   |
|-------|------------------------------|-----------|
|    00 | PRFB (vector plus immediate) | FEAT_SVE  |
|    01 | PRFH (vector plus immediate) | FEAT_SVE  |
|    10 | PRFW(vector plus immediate)  | FEAT_SVE  |
|    11 | PRFD (vector plus immediate) | FEAT_SVE  |

|   dtypeh |   dtypel | Instruction Details    | Feature                        |
|----------|----------|------------------------|--------------------------------|
|       00 |       00 | LD1RB -8-bit element   | FEAT_SVE &#124;&#124; FEAT_SME |
|       00 |       01 | LD1RB -16-bit element  | FEAT_SVE &#124;&#124; FEAT_SME |
|       00 |       10 | LD1RB -32-bit element  | FEAT_SVE &#124;&#124; FEAT_SME |
|       00 |       11 | LD1RB -64-bit element  | FEAT_SVE &#124;&#124; FEAT_SME |
|       01 |       00 | LD1RSW                 | FEAT_SVE &#124;&#124; FEAT_SME |
|       01 |       01 | LD1RH -16-bit element  | FEAT_SVE &#124;&#124; FEAT_SME |
|       01 |       10 | LD1RH -32-bit element  | FEAT_SVE &#124;&#124; FEAT_SME |
|       01 |       11 | LD1RH -64-bit element  | FEAT_SVE &#124;&#124; FEAT_SME |
|       10 |       00 | LD1RSH -64-bit element | FEAT_SVE &#124;&#124; FEAT_SME |
|       10 |       01 | LD1RSH -32-bit element | FEAT_SVE &#124;&#124; FEAT_SME |
|       10 |       10 | LD1RW-32-bit element   | FEAT_SVE &#124;&#124; FEAT_SME |
|       10 |       11 | LD1RW-64-bit element   | FEAT_SVE &#124;&#124; FEAT_SME |
|       11 |       00 | LD1RSB -64-bit element | FEAT_SVE &#124;&#124; FEAT_SME |
|       11 |       01 | LD1RSB -32-bit element | FEAT_SVE &#124;&#124; FEAT_SME |
|       11 |       10 | LD1RSB -16-bit element | FEAT_SVE &#124;&#124; FEAT_SME |
|       11 |       11 | LD1RD                  | FEAT_SVE &#124;&#124; FEAT_SME |

## SVE 32-bit gather load (scalar plus 32-bit unscaled offsets)

The encodings in this section are decoded from SVE Memory - 32-bit Gather and Unsized Contiguous.

<!-- image -->

The following constraints also apply to this encoding: opc != '11'

|   opc |   U | ff   | Instruction Details          | Feature   |
|-------|-----|------|------------------------------|-----------|
|    00 |   0 | 0    | LD1SB (scalar plus vector)   | FEAT_SVE  |
|    00 |   0 | 1    | LDFF1SB (scalar plus vector) | FEAT_SVE  |
|    00 |   1 | 0    | LD1B (scalar plus vector)    | FEAT_SVE  |
|    00 |   1 | 1    | LDFF1B (scalar plus vector)  | FEAT_SVE  |
|    01 |   0 | 0    | LD1SH (scalar plus vector)   | FEAT_SVE  |
|    01 |   0 | 1    | LDFF1SH (scalar plus vector) | FEAT_SVE  |
|    01 |   1 | 0    | LD1H (scalar plus vector)    | FEAT_SVE  |
|    01 |   1 | 1    | LDFF1H (scalar plus vector)  | FEAT_SVE  |
|    10 |   0 | x    | UNALLOCATED                  | -         |
|    10 |   1 | 0    | LD1W(scalar plus vector)     | FEAT_SVE  |
|    10 |   1 | 1    | LDFF1W (scalar plus vector)  | FEAT_SVE  |

## SVE Memory - Contiguous Load

SVE Memory - Contiguous Load

The encodings in this section are decoded from SVE encodings.

<!-- image -->

| 31   | 25 24 23 22 21 20   | 16 15   |
|------|---------------------|---------|
| 1 0  | 0 op0 op1           | op2     |

| op0   | op1   |   op2 | Instruction details                                             |
|-------|-------|-------|-----------------------------------------------------------------|
| 00    | 0     |   111 | SVE contiguous non-temporal load (scalar plus immediate)        |
| 00    | 1     |   001 | SVE contiguous load (quadwords, scalar plus immediate)          |
| 00    | 1     |   111 | SVE load multiple structures (quadwords, scalar plus immediate) |
| 00    | x     |   100 | SVE contiguous load (quadwords, scalar plus scalar)             |
| 00    | x     |   110 | SVE contiguous non-temporal load (scalar plus scalar)           |
| 01    | x     |   100 | SVE load multiple structures (quadwords, scalar plus scalar)    |
| 1x    | x     |   100 | UNALLOCATED                                                     |
| xx    | 0     |   001 | SVE load and broadcast quadword (scalar plus immediate)         |
| xx    | 0     |   101 | SVE contiguous load (scalar plus immediate)                     |
| xx    | 1     |   101 | SVE contiguous non-fault load (scalar plus immediate)           |
| xx    | x     |   000 | SVE load and broadcast quadword (scalar plus scalar)            |
| xx    | x     |   010 | SVE contiguous load (scalar plus scalar)                        |
| xx    | x     |   011 | SVEcontiguous first-fault load (scalar plus scalar)             |
| != 00 | 0     |   111 | SVE load multiple structures (scalar plus immediate)            |
| != 00 | 1     |   001 | UNALLOCATED                                                     |
| != 00 | 1     |   111 | UNALLOCATED                                                     |
| != 00 | x     |   110 | SVE load multiple structures (scalar plus scalar)               |

SVE contiguous non-temporal load (scalar plus immediate)

The encodings in this section are decoded from SVE Memory - Contiguous Load.

<!-- image -->

|   msz | Instruction Details                             | Feature                        |
|-------|-------------------------------------------------|--------------------------------|
|    00 | LDNT1B (scalar plus immediate, single register) | FEAT_SVE &#124;&#124; FEAT_SME |
|    01 | LDNT1H (scalar plus immediate, single register) | FEAT_SVE &#124;&#124; FEAT_SME |
|    10 | LDNT1W (scalar plus immediate, single register) | FEAT_SVE &#124;&#124; FEAT_SME |
|    11 | LDNT1D (scalar plus immediate, single register) | FEAT_SVE &#124;&#124; FEAT_SME |

## SVE contiguous load (quadwords, scalar plus immediate)

The encodings in this section are decoded from SVE Memory - Contiguous Load.

<!-- image -->

| dtype   | Instruction Details                           | Feature     |
|---------|-----------------------------------------------|-------------|
| 0x      | UNALLOCATED                                   | -           |
| 10      | LD1W (scalar plus immediate, single register) | FEAT_SVE2p1 |
| 11      | LD1D (scalar plus immediate, single register) | FEAT_SVE2p1 |

## SVE load multiple structures (quadwords, scalar plus immediate)

The encodings in this section are decoded from SVE Memory - Contiguous Load.

<!-- image -->

|   num | Instruction Details          | Feature                              |
|-------|------------------------------|--------------------------------------|
|    00 | UNALLOCATED                  | -                                    |
|    01 | LD2Q (scalar plus immediate) | FEAT_SVE2p1 &#124;&#124; FEAT_SME2p1 |
|    10 | LD3Q (scalar plus immediate) | FEAT_SVE2p1 &#124;&#124; FEAT_SME2p1 |
|    11 | LD4Q (scalar plus immediate) | FEAT_SVE2p1 &#124;&#124; FEAT_SME2p1 |

## SVE contiguous load (quadwords, scalar plus scalar)

The encodings in this section are decoded from SVE Memory - Contiguous Load.

<!-- image -->

| 31    | 25 24 23 22 21 20   | 16 15   | 13 12   | 10       | 5 4   | 0   |
|-------|---------------------|---------|---------|----------|-------|-----|
| 1 0 1 | 0 dtype             | 0 0     | Rm      | 1 0 0 Pg | Rn    | Zt  |

| dtype   | Rm       | Instruction Details                        | Feature     |
|---------|----------|--------------------------------------------|-------------|
| 0x      | xxxxx    | UNALLOCATED                                | -           |
| 1x      | 11111    | UNALLOCATED                                | -           |
| 10      | != 11111 | LD1W(scalar plus scalar, single register)  | FEAT_SVE2p1 |
| 11      | != 11111 | LD1D (scalar plus scalar, single register) | FEAT_SVE2p1 |

## SVE contiguous non-temporal load (scalar plus scalar)

The encodings in this section are decoded from SVE Memory - Contiguous Load.

<!-- image -->

| 31      | 25 24 23 22 21 20   | 16 15 13 12 10 9 5 4   |
|---------|---------------------|------------------------|
| 1 0 1 0 | 0 msz 0 0 Rm 1 1    | 0 Pg Rn Zt             |

| msz   | Rm       | Instruction Details   | Instruction Details   | Instruction Details   | Instruction Details   | Instruction Details   | Feature                        |
|-------|----------|-----------------------|-----------------------|-----------------------|-----------------------|-----------------------|--------------------------------|
| xx    | 11111    | UNALLOCATED           | UNALLOCATED           | UNALLOCATED           | UNALLOCATED           | UNALLOCATED           | -                              |
| 00    | != 11111 | LDNT1B register)      | (scalar               | plus                  | scalar,               | single                | FEAT_SVE &#124;&#124; FEAT_SME |
| 01    | != 11111 | LDNT1H register)      | (scalar               | plus                  | scalar,               | single                | FEAT_SVE &#124;&#124; FEAT_SME |
| 10    | != 11111 | LDNT1W register)      | (scalar               | plus                  | scalar,               | single                | FEAT_SVE &#124;&#124; FEAT_SME |
| 11    | != 11111 | LDNT1D register)      | (scalar               | plus                  | scalar,               | single                | FEAT_SVE &#124;&#124; FEAT_SME |

## SVE load multiple structures (quadwords, scalar plus scalar)

The encodings in this section are decoded from SVE Memory - Contiguous Load.

<!-- image -->

| 31    | 25 24 23 22 21   | 16 15   | 13 12   | 10 9   | 5   | 4   |
|-------|------------------|---------|---------|--------|-----|-----|
| 1 0 1 | 1 0 num 0 1      | Rm      | 1 0 0   | Pg     | Rn  | Zt  |

| num   | Rm       | Instruction Details       | Feature                              |
|-------|----------|---------------------------|--------------------------------------|
| 00    | xxxxx    | UNALLOCATED               | -                                    |
| 01    | != 11111 | LD2Q (scalar plus scalar) | FEAT_SVE2p1 &#124;&#124; FEAT_SME2p1 |
| 10    | != 11111 | LD3Q (scalar plus scalar) | FEAT_SVE2p1 &#124;&#124; FEAT_SME2p1 |
| 11    | != 11111 | LD4Q (scalar plus scalar) | FEAT_SVE2p1 &#124;&#124; FEAT_SME2p1 |
| != 00 | 11111    | UNALLOCATED               | -                                    |

## SVE load and broadcast quadword (scalar plus immediate)

The encodings in this section are decoded from SVE Memory - Contiguous Load.

<!-- image -->

| 31    | 25 24 23   | 22 21   |   20 | 19   |   16 15 | 13 12   | 10 9   | 5 4   | 0   |
|-------|------------|---------|------|------|---------|---------|--------|-------|-----|
| 1 0 1 | 1 0 msz    | ssz     |    0 | imm4 |       0 | 0 1     | Pg     | Rn    | Zt  |

| msz   | ssz   | Instruction Details            | Feature                        |
|-------|-------|--------------------------------|--------------------------------|
| xx    | 1x    | UNALLOCATED                    | -                              |
| 00    | 00    | LD1RQB (scalar plus immediate) | FEAT_SVE &#124;&#124; FEAT_SME |
| 00    | 01    | LD1ROB (scalar plus immediate) | FEAT_F64MM                     |
| 01    | 00    | LD1RQH (scalar plus immediate) | FEAT_SVE &#124;&#124; FEAT_SME |
| 01    | 01    | LD1ROH (scalar plus immediate) | FEAT_F64MM                     |
| 10    | 00    | LD1RQW(scalar plus immediate)  | FEAT_SVE &#124;&#124; FEAT_SME |
| 10    | 01    | LD1ROW(scalar plus immediate)  | FEAT_F64MM                     |
| 11    | 00    | LD1RQD (scalar plus immediate) | FEAT_SVE &#124;&#124; FEAT_SME |
| 11    | 01    | LD1ROD (scalar plus immediate) | FEAT_F64MM                     |

## SVE contiguous load (scalar plus immediate)

The encodings in this section are decoded from SVE Memory - Contiguous Load.

<!-- image -->

|   dtype | Instruction Details                                    |         | Feature                        |
|---------|--------------------------------------------------------|---------|--------------------------------|
|    0000 | LD1B (scalar plus immediate, register) -8-bit element  | single  | FEAT_SVE &#124;&#124; FEAT_SME |
|    0001 | LD1B (scalar plus immediate, register) -16-bit element | single  | FEAT_SVE &#124;&#124; FEAT_SME |
|    0010 | LD1B (scalar plus immediate, register) -32-bit element | single  | FEAT_SVE &#124;&#124; FEAT_SME |
|    0011 | LD1B (scalar plus immediate, register) -64-bit element | single  | FEAT_SVE &#124;&#124; FEAT_SME |
|    0100 | LD1SW(scalar plus immediate)                           |         | FEAT_SVE &#124;&#124; FEAT_SME |
|    0101 | LD1H (scalar plus immediate, register) -16-bit element | single  | FEAT_SVE &#124;&#124; FEAT_SME |
|    0110 | LD1H (scalar plus immediate, register) -32-bit element | single  | FEAT_SVE &#124;&#124; FEAT_SME |
|    0111 | LD1H (scalar plus immediate, register) -64-bit element | single  | FEAT_SVE &#124;&#124; FEAT_SME |
|    1000 | LD1SH (scalar plus immediate) element                  | -64-bit | FEAT_SVE &#124;&#124; FEAT_SME |
|    1001 | LD1SH (scalar plus immediate) element                  | -32-bit | FEAT_SVE &#124;&#124; FEAT_SME |
|    1010 | LD1W (scalar plus immediate, register) -32-bit element | single  | FEAT_SVE &#124;&#124; FEAT_SME |
|    1011 | LD1W (scalar plus immediate, register) -64-bit element | single  | FEAT_SVE &#124;&#124; FEAT_SME |
|    1100 | LD1SB (scalar plus immediate) - element                | 64-bit  | FEAT_SVE &#124;&#124; FEAT_SME |
|    1101 | LD1SB (scalar plus immediate) - element                | 32-bit  | FEAT_SVE &#124;&#124; FEAT_SME |
|    1110 | LD1SB (scalar plus immediate) - element                | 16-bit  | FEAT_SVE &#124;&#124; FEAT_SME |
|    1111 | LD1D (scalar plus immediate, register)                 | single  | FEAT_SVE &#124;&#124; FEAT_SME |

## SVE contiguous non-fault load (scalar plus immediate)

The encodings in this section are decoded from SVE Memory - Contiguous Load.

<!-- image -->

|   dtype | Instruction Details     | Feature   |
|---------|-------------------------|-----------|
|    0000 | LDNF1B -8-bit element   | FEAT_SVE  |
|    0001 | LDNF1B -16-bit element  | FEAT_SVE  |
|    0010 | LDNF1B -32-bit element  | FEAT_SVE  |
|    0011 | LDNF1B -64-bit element  | FEAT_SVE  |
|    0100 | LDNF1SW                 | FEAT_SVE  |
|    0101 | LDNF1H -16-bit element  | FEAT_SVE  |
|    0110 | LDNF1H -32-bit element  | FEAT_SVE  |
|    0111 | LDNF1H -64-bit element  | FEAT_SVE  |
|    1000 | LDNF1SH -64-bit element | FEAT_SVE  |
|    1001 | LDNF1SH -32-bit element | FEAT_SVE  |
|    1010 | LDNF1W-32-bit element   | FEAT_SVE  |
|    1011 | LDNF1W-64-bit element   | FEAT_SVE  |
|    1100 | LDNF1SB -64-bit element | FEAT_SVE  |
|    1101 | LDNF1SB -32-bit element | FEAT_SVE  |
|    1110 | LDNF1SB -16-bit element | FEAT_SVE  |
|    1111 | LDNF1D                  | FEAT_SVE  |

## SVE load and broadcast quadword (scalar plus scalar)

The encodings in this section are decoded from SVE Memory - Contiguous Load.

<!-- image -->

| msz   | ssz   | Rm       | Instruction Details         | Feature                        |
|-------|-------|----------|-----------------------------|--------------------------------|
| xx    | 0x    | 11111    | UNALLOCATED                 | -                              |
| xx    | 1x    | xxxxx    | UNALLOCATED                 | -                              |
| 00    | 00    | != 11111 | LD1RQB (scalar plus scalar) | FEAT_SVE &#124;&#124; FEAT_SME |
| 00    | 01    | != 11111 | LD1ROB (scalar plus scalar) | FEAT_F64MM                     |
| 01    | 00    | != 11111 | LD1RQH (scalar plus scalar) | FEAT_SVE &#124;&#124; FEAT_SME |
| 01    | 01    | != 11111 | LD1ROH (scalar plus scalar) | FEAT_F64MM                     |
| 10    | 00    | != 11111 | LD1RQW(scalar plus scalar)  | FEAT_SVE &#124;&#124; FEAT_SME |
| 10    | 01    | != 11111 | LD1ROW(scalar plus scalar)  | FEAT_F64MM                     |
| 11    | 00    | != 11111 | LD1RQD (scalar plus scalar) | FEAT_SVE &#124;&#124; FEAT_SME |
| 11    | 01    | != 11111 | LD1ROD (scalar plus scalar) | FEAT_F64MM                     |

## SVE contiguous load (scalar plus scalar)

The encodings in this section are decoded from SVE Memory - Contiguous Load.

<!-- image -->

| 31          | 25 24   | 20   | 16 15 13 12   |
|-------------|---------|------|---------------|
| 1 0 1 0 0 1 | 0 dtype | Rm   | 0 1 0 Pg      |

| dtype   | Rm       | Instruction Details                                        | Feature                        |
|---------|----------|------------------------------------------------------------|--------------------------------|
| xxxx    | 11111    | UNALLOCATED                                                | -                              |
| 0000    | != 11111 | LD1B (scalar plus scalar, single register) -8-bit element  | FEAT_SVE &#124;&#124; FEAT_SME |
| 0001    | != 11111 | LD1B (scalar plus scalar, single register) -16-bit element | FEAT_SVE &#124;&#124; FEAT_SME |
| 0010    | != 11111 | LD1B (scalar plus scalar, single register) -32-bit element | FEAT_SVE &#124;&#124; FEAT_SME |
| 0011    | != 11111 | LD1B (scalar plus scalar, single register) -64-bit element | FEAT_SVE &#124;&#124; FEAT_SME |
| 0100    | != 11111 | LD1SW(scalar plus scalar)                                  | FEAT_SVE &#124;&#124; FEAT_SME |
| 0101    | != 11111 | LD1H (scalar plus scalar, single register) -16-bit element | FEAT_SVE &#124;&#124; FEAT_SME |
| 0110    | != 11111 | LD1H (scalar plus scalar, single register) -32-bit element | FEAT_SVE &#124;&#124; FEAT_SME |
| 0111    | != 11111 | LD1H (scalar plus scalar, single register) -64-bit element | FEAT_SVE &#124;&#124; FEAT_SME |
| 1000    | != 11111 | LD1SH (scalar plus scalar) - 64-bit element                | FEAT_SVE &#124;&#124; FEAT_SME |
| 1001    | != 11111 | LD1SH (scalar plus scalar) - 32-bit element                | FEAT_SVE &#124;&#124; FEAT_SME |
| 1010    | != 11111 | LD1W (scalar plus scalar, single register) -32-bit element | FEAT_SVE &#124;&#124; FEAT_SME |
| 1011    | != 11111 | LD1W (scalar plus scalar, single register) -64-bit element | FEAT_SVE &#124;&#124; FEAT_SME |
| 1100    | != 11111 | LD1SB (scalar plus scalar) - 64-bit element                | FEAT_SVE &#124;&#124; FEAT_SME |
| 1101    | != 11111 | LD1SB (scalar plus scalar) - 32-bit element                | FEAT_SVE &#124;&#124; FEAT_SME |
| 1110    | != 11111 | LD1SB (scalar plus scalar) - 16-bit element                | FEAT_SVE &#124;&#124; FEAT_SME |
| 1111    | != 11111 | LD1D (scalar plus scalar, single register)                 | FEAT_SVE &#124;&#124; FEAT_SME |

## SVE contiguous first-fault load (scalar plus scalar)

The encodings in this section are decoded from SVE Memory - Contiguous Load.

<!-- image -->

|   dtype | Instruction Details          | Instruction Details          | Instruction Details          | Instruction Details          | Feature   |
|---------|------------------------------|------------------------------|------------------------------|------------------------------|-----------|
|    0000 | LDFF1B element               | (scalar                      | plus scalar) -               | 8-bit                        | FEAT_SVE  |
|    0001 | LDFF1B element               | (scalar plus                 | scalar) -                    | 16-bit                       | FEAT_SVE  |
|    0010 | LDFF1B element               | (scalar plus                 | scalar) -                    | 32-bit                       | FEAT_SVE  |
|    0011 | LDFF1B element               | (scalar plus                 | scalar) -                    | 64-bit                       | FEAT_SVE  |
|    0100 | LDFF1SW (scalar plus scalar) | LDFF1SW (scalar plus scalar) | LDFF1SW (scalar plus scalar) | LDFF1SW (scalar plus scalar) | FEAT_SVE  |
|    0101 | LDFF1H element               | (scalar plus                 | scalar) -                    | 16-bit                       | FEAT_SVE  |
|    0110 | LDFF1H element               | (scalar plus                 | scalar) -                    | 32-bit                       | FEAT_SVE  |
|    0111 | LDFF1H element               | (scalar plus                 | scalar) -                    | 64-bit                       | FEAT_SVE  |
|    1000 | LDFF1SH element              | (scalar                      | plus scalar) -               | 64-bit                       | FEAT_SVE  |
|    1001 | LDFF1SH element              | (scalar                      | plus scalar) -               | 32-bit                       | FEAT_SVE  |
|    1010 | LDFF1W element               | (scalar plus                 | scalar) -                    | 32-bit                       | FEAT_SVE  |
|    1011 | LDFF1W element               | (scalar plus                 | scalar) -                    | 64-bit                       | FEAT_SVE  |
|    1100 | LDFF1SB element              | (scalar                      | plus scalar) -               | 64-bit                       | FEAT_SVE  |
|    1101 | LDFF1SB element              | (scalar                      | plus scalar) -               | 32-bit                       | FEAT_SVE  |
|    1110 | LDFF1SB element              | (scalar                      | plus scalar) -               | 16-bit                       | FEAT_SVE  |
|    1111 | LDFF1D (scalar               | plus                         | scalar)                      |                              | FEAT_SVE  |

## SVE load multiple structures (scalar plus immediate)

The encodings in this section are decoded from SVE Memory - Contiguous Load.

<!-- image -->

The following constraints also apply to this encoding: opc != '00'

|   msz |   opc | Instruction Details          | Feature           |
|-------|-------|------------------------------|-------------------|
|    00 |    01 | LD2B (scalar plus immediate) | FEAT_SVE FEAT_SME |

||

|   msz |   opc | Instruction Details          | Feature                        |
|-------|-------|------------------------------|--------------------------------|
|    00 |    10 | LD3B (scalar plus immediate) | FEAT_SVE &#124;&#124; FEAT_SME |
|    00 |    11 | LD4B (scalar plus immediate) | FEAT_SVE &#124;&#124; FEAT_SME |
|    01 |    01 | LD2H (scalar plus immediate) | FEAT_SVE &#124;&#124; FEAT_SME |
|    01 |    10 | LD3H (scalar plus immediate) | FEAT_SVE &#124;&#124; FEAT_SME |
|    01 |    11 | LD4H (scalar plus immediate) | FEAT_SVE &#124;&#124; FEAT_SME |
|    10 |    01 | LD2W(scalar plus immediate)  | FEAT_SVE &#124;&#124; FEAT_SME |
|    10 |    10 | LD3W(scalar plus immediate)  | FEAT_SVE &#124;&#124; FEAT_SME |
|    10 |    11 | LD4W(scalar plus immediate)  | FEAT_SVE &#124;&#124; FEAT_SME |
|    11 |    01 | LD2D (scalar plus immediate) | FEAT_SVE &#124;&#124; FEAT_SME |
|    11 |    10 | LD3D (scalar plus immediate) | FEAT_SVE &#124;&#124; FEAT_SME |
|    11 |    11 | LD4D (scalar plus immediate) | FEAT_SVE &#124;&#124; FEAT_SME |

## SVE load multiple structures (scalar plus scalar)

The encodings in this section are decoded from SVE Memory - Contiguous Load.

<!-- image -->

The following constraints also apply to this encoding: opc != '00'

| msz   | opc   | Rm       | Instruction Details       | Feature                        |
|-------|-------|----------|---------------------------|--------------------------------|
| xx    | != 00 | 11111    | UNALLOCATED               | -                              |
| 00    | 01    | != 11111 | LD2B (scalar plus scalar) | FEAT_SVE &#124;&#124; FEAT_SME |
| 00    | 10    | != 11111 | LD3B (scalar plus scalar) | FEAT_SVE &#124;&#124; FEAT_SME |
| 00    | 11    | != 11111 | LD4B (scalar plus scalar) | FEAT_SVE &#124;&#124; FEAT_SME |
| 01    | 01    | != 11111 | LD2H (scalar plus scalar) | FEAT_SVE &#124;&#124; FEAT_SME |
| 01    | 10    | != 11111 | LD3H (scalar plus scalar) | FEAT_SVE &#124;&#124; FEAT_SME |
| 01    | 11    | != 11111 | LD4H (scalar plus scalar) | FEAT_SVE &#124;&#124; FEAT_SME |
| 10    | 01    | != 11111 | LD2W(scalar plus scalar)  | FEAT_SVE &#124;&#124; FEAT_SME |
| 10    | 10    | != 11111 | LD3W(scalar plus scalar)  | FEAT_SVE &#124;&#124; FEAT_SME |
| 10    | 11    | != 11111 | LD4W(scalar plus scalar)  | FEAT_SVE &#124;&#124; FEAT_SME |
| 11    | 01    | != 11111 | LD2D (scalar plus scalar) | FEAT_SVE &#124;&#124; FEAT_SME |
| 11    | 10    | != 11111 | LD3D (scalar plus scalar) | FEAT_SVE &#124;&#124; FEAT_SME |
| 11    | 11    | != 11111 | LD4D (scalar plus scalar) | FEAT_SVE &#124;&#124; FEAT_SME |

## SVE Memory - 64-bit Gather

SVE Memory - 64-bit Gather

The encodings in this section are decoded from SVE encodings.

<!-- image -->

| 31    | 25 24 23   | 22 21   | 16 15 13 12 5 4   |
|-------|------------|---------|-------------------|
| 1 1 0 | 0 op0      | op1     | op2 op3           |

| op0   | op1   | op2   | op3   | Instruction details                                                     | Feature     |
|-------|-------|-------|-------|-------------------------------------------------------------------------|-------------|
| 00    | 00    | 101   | x     | LD1Q                                                                    | FEAT_SVE2p1 |
| 00    | 01    | 0xx   | 1     | UNALLOCATED                                                             | -           |
| 00    | 11    | 1xx   | 0     | SVE 64-bit gather prefetch (scalar plus 64- bit scaled offsets)         | -           |
| 00    | 11    | xxx   | 1     | UNALLOCATED                                                             | -           |
| 00    | x1    | 0xx   | 0     | SVE 64-bit gather prefetch (scalar plus unpacked 32-bit scaled offsets) | -           |
| xx    | 00    | 111   | 0     | SVE 64-bit gather prefetch (vector plus immediate)                      | -           |
| xx    | 00    | 111   | 1     | UNALLOCATED                                                             | -           |
| xx    | 00    | 1x0   | x     | SVE2 64-bit gather non-temporal load (vector plus scalar)               | -           |
| xx    | 01    | 1xx   | x     | SVE 64-bit gather load (vector plus immediate)                          | -           |
| xx    | 10    | 1xx   | x     | SVE 64-bit gather load (scalar plus 64-bit unscaled offsets)            | -           |
| xx    | x0    | 0xx   | x     | SVE 64-bit gather load (scalar plus unpacked 32-bit unscaled offsets)   | -           |
| != 00 | 00    | 101   | x     | UNALLOCATED                                                             | -           |
| != 00 | 11    | 1xx   | x     | SVE 64-bit gather load (scalar plus 64-bit scaled offsets)              | -           |
| != 00 | x1    | 0xx   | x     | SVE 64-bit gather load (scalar plus 32-bit unpacked scaled offsets)     | -           |

## SVE 64-bit gather prefetch (scalar plus 64-bit scaled offsets)

The encodings in this section are decoded from SVE Memory - 64-bit Gather.

<!-- image -->

| 31      | 25 24 23 22 21 20     | 16 15 14 13 12 10 9 5 4 3   |
|---------|-----------------------|-----------------------------|
| 1 1 0 0 | 0 0 0 1 1 Zm 1 msz Pg | Rn 0 prfop                  |

## SVE 64-bit gather prefetch (vector plus immediate)

The encodings in this section are decoded from SVE Memory - 64-bit Gather.

<!-- image -->

| 31        | 25 24 23 22 21 20   | 16 15   | 13 12   | 10   |   5 4 | 0     |
|-----------|---------------------|---------|---------|------|-------|-------|
| 1 1 0 0 0 | 0 msz 0 0           | imm5    | 1 1 1   | Pg   |     0 | prfop |

|   msz | Instruction Details          | Feature   |
|-------|------------------------------|-----------|
|    00 | PRFB (vector plus immediate) | FEAT_SVE  |
|    01 | PRFH (vector plus immediate) | FEAT_SVE  |
|    10 | PRFW(vector plus immediate)  | FEAT_SVE  |
|    11 | PRFD (vector plus immediate) | FEAT_SVE  |

|   msz | Instruction Details       | Feature   |
|-------|---------------------------|-----------|
|    00 | PRFB (scalar plus vector) | FEAT_SVE  |
|    01 | PRFH (scalar plus vector) | FEAT_SVE  |
|    10 | PRFW(scalar plus vector)  | FEAT_SVE  |
|    11 | PRFD (scalar plus vector) | FEAT_SVE  |

## SVE 64-bit gather prefetch (scalar plus unpacked 32-bit scaled offsets)

The encodings in this section are decoded from SVE Memory - 64-bit Gather.

<!-- image -->

|   31 | 25 24 23 22   | 21 20 16 15 14 13   | 12 10 9   |   4 3 | 0     |
|------|---------------|---------------------|-----------|-------|-------|
|    1 | 0 0 0 1 0 0 0 | xs 1 Zm 0 msz       | Pg Rn     |     0 | prfop |

|   msz | Instruction Details       | Feature   |
|-------|---------------------------|-----------|
|    00 | PRFB (scalar plus vector) | FEAT_SVE  |
|    01 | PRFH (scalar plus vector) | FEAT_SVE  |
|    10 | PRFW(scalar plus vector)  | FEAT_SVE  |
|    11 | PRFD (scalar plus vector) | FEAT_SVE  |

## SVE2 64-bit gather non-temporal load (vector plus scalar)

The encodings in this section are decoded from SVE Memory - 64-bit Gather.

<!-- image -->

| 31        | 25 24 23 22 21 20   | 16 15 14    | 13 12 10 9 5 4   |
|-----------|---------------------|-------------|------------------|
| 1 1 0 0 0 | 0 msz 0 0           | Rm 1 U 0 Pg | Zn Zt            |

|   msz |   U | Instruction Details         | Feature   |
|-------|-----|-----------------------------|-----------|
|    00 |   0 | LDNT1SB                     | FEAT_SVE2 |
|    00 |   1 | LDNT1B (vector plus scalar) | FEAT_SVE2 |
|    01 |   0 | LDNT1SH                     | FEAT_SVE2 |
|    01 |   1 | LDNT1H (vector plus scalar) | FEAT_SVE2 |
|    10 |   0 | LDNT1SW                     | FEAT_SVE2 |
|    10 |   1 | LDNT1W(vector plus scalar)  | FEAT_SVE2 |
|    11 |   0 | UNALLOCATED                 | -         |
|    11 |   1 | LDNT1D (vector plus scalar) | FEAT_SVE2 |

## SVE 64-bit gather load (vector plus immediate)

The encodings in this section are decoded from SVE Memory - 64-bit Gather.

<!-- image -->

| 31      | 25 24 23 22 21 20   | 16 15 14 13   | 12 10   | 9      | 5   | 4   |    |
|---------|---------------------|---------------|---------|--------|-----|-----|----|
| 1 1 0 0 | 0 msz               | 0 1           | imm5    | 1 U ff | Pg  | Zn  | Zt |

|   msz |   U |   ff | Instruction Details             | Feature   |
|-------|-----|------|---------------------------------|-----------|
|    00 |   0 |    0 | LD1SB (vector plus immediate)   | FEAT_SVE  |
|    00 |   0 |    1 | LDFF1SB (vector plus immediate) | FEAT_SVE  |
|    00 |   1 |    0 | LD1B (vector plus immediate)    | FEAT_SVE  |
|    00 |   1 |    1 | LDFF1B (vector plus immediate)  | FEAT_SVE  |
|    01 |   0 |    0 | LD1SH (vector plus immediate)   | FEAT_SVE  |
|    01 |   0 |    1 | LDFF1SH (vector plus immediate) | FEAT_SVE  |
|    01 |   1 |    0 | LD1H (vector plus immediate)    | FEAT_SVE  |
|    01 |   1 |    1 | LDFF1H (vector plus immediate)  | FEAT_SVE  |
|    10 |   0 |    0 | LD1SW(vector plus immediate)    | FEAT_SVE  |
|    10 |   0 |    1 | LDFF1SW (vector plus immediate) | FEAT_SVE  |
|    10 |   1 |    0 | LD1W(vector plus immediate)     | FEAT_SVE  |
|    10 |   1 |    1 | LDFF1W (vector plus immediate)  | FEAT_SVE  |

|   msz |   U | ff   | Instruction Details            | Feature   |
|-------|-----|------|--------------------------------|-----------|
|    11 |   0 | x    | UNALLOCATED                    | -         |
|    11 |   1 | 0    | LD1D (vector plus immediate)   | FEAT_SVE  |
|    11 |   1 | 1    | LDFF1D (vector plus immediate) | FEAT_SVE  |

## SVE 64-bit gather load (scalar plus 64-bit unscaled offsets)

The encodings in this section are decoded from SVE Memory - 64-bit Gather.

<!-- image -->

| 31    | 25 24 23 22 21 20   | 16 15 14   | 13 12   | 10 9   | 5 4   | 0   |
|-------|---------------------|------------|---------|--------|-------|-----|
| 1 1 0 | 0 msz               | 1 0        | Zm 1    | U ff   | Pg Rn | Zt  |

|   msz |   U | ff   | Instruction Details          | Feature   |
|-------|-----|------|------------------------------|-----------|
|    00 |   0 | 0    | LD1SB (scalar plus vector)   | FEAT_SVE  |
|    00 |   0 | 1    | LDFF1SB (scalar plus vector) | FEAT_SVE  |
|    00 |   1 | 0    | LD1B (scalar plus vector)    | FEAT_SVE  |
|    00 |   1 | 1    | LDFF1B (scalar plus vector)  | FEAT_SVE  |
|    01 |   0 | 0    | LD1SH (scalar plus vector)   | FEAT_SVE  |
|    01 |   0 | 1    | LDFF1SH (scalar plus vector) | FEAT_SVE  |
|    01 |   1 | 0    | LD1H (scalar plus vector)    | FEAT_SVE  |
|    01 |   1 | 1    | LDFF1H (scalar plus vector)  | FEAT_SVE  |
|    10 |   0 | 0    | LD1SW(scalar plus vector)    | FEAT_SVE  |
|    10 |   0 | 1    | LDFF1SW (scalar plus vector) | FEAT_SVE  |
|    10 |   1 | 0    | LD1W(scalar plus vector)     | FEAT_SVE  |
|    10 |   1 | 1    | LDFF1W (scalar plus vector)  | FEAT_SVE  |
|    11 |   0 | x    | UNALLOCATED                  | -         |
|    11 |   1 | 0    | LD1D (scalar plus vector)    | FEAT_SVE  |
|    11 |   1 | 1    | LDFF1D (scalar plus vector)  | FEAT_SVE  |

## SVE 64-bit gather load (scalar plus unpacked 32-bit unscaled offsets)

The encodings in this section are decoded from SVE Memory - 64-bit Gather.

<!-- image -->

| 31      | 25 24 23 22   | 21 20 16 15 14 13   | 12 10 9   | 5 4   |
|---------|---------------|---------------------|-----------|-------|
| 1 1 0 0 | 0 msz xs      | 0 Zm 0 U ff         | Pg Rn     | Zt    |

|   msz |   U | ff   | Instruction Details          | Feature   |
|-------|-----|------|------------------------------|-----------|
|    00 |   0 | 0    | LD1SB (scalar plus vector)   | FEAT_SVE  |
|    00 |   0 | 1    | LDFF1SB (scalar plus vector) | FEAT_SVE  |
|    00 |   1 | 0    | LD1B (scalar plus vector)    | FEAT_SVE  |
|    00 |   1 | 1    | LDFF1B (scalar plus vector)  | FEAT_SVE  |
|    01 |   0 | 0    | LD1SH (scalar plus vector)   | FEAT_SVE  |
|    01 |   0 | 1    | LDFF1SH (scalar plus vector) | FEAT_SVE  |
|    01 |   1 | 0    | LD1H (scalar plus vector)    | FEAT_SVE  |
|    01 |   1 | 1    | LDFF1H (scalar plus vector)  | FEAT_SVE  |
|    10 |   0 | 0    | LD1SW(scalar plus vector)    | FEAT_SVE  |
|    10 |   0 | 1    | LDFF1SW (scalar plus vector) | FEAT_SVE  |
|    10 |   1 | 0    | LD1W(scalar plus vector)     | FEAT_SVE  |
|    10 |   1 | 1    | LDFF1W (scalar plus vector)  | FEAT_SVE  |
|    11 |   0 | x    | UNALLOCATED                  | -         |
|    11 |   1 | 0    | LD1D (scalar plus vector)    | FEAT_SVE  |
|    11 |   1 | 1    | LDFF1D (scalar plus vector)  | FEAT_SVE  |

## SVE 64-bit gather load (scalar plus 64-bit scaled offsets)

The encodings in this section are decoded from SVE Memory - 64-bit Gather.

<!-- image -->

The following constraints also apply to this encoding: opc != '00'

|   opc |   U | ff   | Instruction Details          | Feature   |
|-------|-----|------|------------------------------|-----------|
|    01 |   0 | 0    | LD1SH (scalar plus vector)   | FEAT_SVE  |
|    01 |   0 | 1    | LDFF1SH (scalar plus vector) | FEAT_SVE  |
|    01 |   1 | 0    | LD1H (scalar plus vector)    | FEAT_SVE  |
|    01 |   1 | 1    | LDFF1H (scalar plus vector)  | FEAT_SVE  |
|    10 |   0 | 0    | LD1SW(scalar plus vector)    | FEAT_SVE  |
|    10 |   0 | 1    | LDFF1SW (scalar plus vector) | FEAT_SVE  |
|    10 |   1 | 0    | LD1W(scalar plus vector)     | FEAT_SVE  |
|    10 |   1 | 1    | LDFF1W (scalar plus vector)  | FEAT_SVE  |
|    11 |   0 | x    | UNALLOCATED                  | -         |
|    11 |   1 | 0    | LD1D (scalar plus vector)    | FEAT_SVE  |
|    11 |   1 | 1    | LDFF1D (scalar plus vector)  | FEAT_SVE  |

## SVE 64-bit gather load (scalar plus 32-bit unpacked scaled offsets)

The encodings in this section are decoded from SVE Memory - 64-bit Gather.

<!-- image -->

The following constraints also apply to this encoding: opc != '00'

|   opc |   U | ff   | Instruction Details          | Feature   |
|-------|-----|------|------------------------------|-----------|
|    01 |   0 | 0    | LD1SH (scalar plus vector)   | FEAT_SVE  |
|    01 |   0 | 1    | LDFF1SH (scalar plus vector) | FEAT_SVE  |
|    01 |   1 | 0    | LD1H (scalar plus vector)    | FEAT_SVE  |
|    01 |   1 | 1    | LDFF1H (scalar plus vector)  | FEAT_SVE  |
|    10 |   0 | 0    | LD1SW(scalar plus vector)    | FEAT_SVE  |
|    10 |   0 | 1    | LDFF1SW (scalar plus vector) | FEAT_SVE  |
|    10 |   1 | 0    | LD1W(scalar plus vector)     | FEAT_SVE  |
|    10 |   1 | 1    | LDFF1W (scalar plus vector)  | FEAT_SVE  |
|    11 |   0 | x    | UNALLOCATED                  | -         |
|    11 |   1 | 0    | LD1D (scalar plus vector)    | FEAT_SVE  |
|    11 |   1 | 1    | LDFF1D (scalar plus vector)  | FEAT_SVE  |

## SVE Memory - Non-temporal and Quadword Scatter Store

SVE Memory - Non-temporal and Quadword Scatter Store

The encodings in this section are decoded from SVE encodings.

<!-- image -->

| op0    |   op1 | Instruction details                                         | Feature     |
|--------|-------|-------------------------------------------------------------|-------------|
| 000    |     1 | ST1Q                                                        | FEAT_SVE2p1 |
| xx0    |     0 | SVE2 64-bit scatter non-temporal store (vector plus scalar) | -           |
| xx1    |     0 | SVE2 32-bit scatter non-temporal store (vector plus scalar) | -           |
| != 000 |     1 | UNALLOCATED                                                 | -           |

## SVE2 64-bit scatter non-temporal store (vector plus scalar)

The encodings in this section are decoded from SVE Memory - Non-temporal and Quadword Scatter Store.

<!-- image -->

|   msz | Instruction Details         | Feature   |
|-------|-----------------------------|-----------|
|    00 | STNT1B (vector plus scalar) | FEAT_SVE2 |
|    01 | STNT1H (vector plus scalar) | FEAT_SVE2 |
|    10 | STNT1W (vector plus scalar) | FEAT_SVE2 |
|    11 | STNT1D (vector plus scalar) | FEAT_SVE2 |

## SVE2 32-bit scatter non-temporal store (vector plus scalar)

The encodings in this section are decoded from SVE Memory - Non-temporal and Quadword Scatter Store.

<!-- image -->

|   msz | Instruction Details         | Feature   |
|-------|-----------------------------|-----------|
|    00 | STNT1B (vector plus scalar) | FEAT_SVE2 |
|    01 | STNT1H (vector plus scalar) | FEAT_SVE2 |
|    10 | STNT1W (vector plus scalar) | FEAT_SVE2 |
|    11 | UNALLOCATED                 | -         |

## SVE Memory - Non-temporal and Multi-register Contiguous Store

SVE Memory - Non-temporal and Multi-register Contiguous Store

The encodings in this section are decoded from SVE encodings.

<!-- image -->

## SVE contiguous non-temporal store (scalar plus scalar)

The encodings in this section are decoded from SVE Memory - Non-temporal and Multi-register Contiguous Store.

<!-- image -->

| msz   | Rm       | Instruction Details   | Instruction Details   | Instruction Details   | Instruction Details   | Instruction Details   | Feature                        |
|-------|----------|-----------------------|-----------------------|-----------------------|-----------------------|-----------------------|--------------------------------|
| xx    | 11111    | UNALLOCATED           | UNALLOCATED           | UNALLOCATED           | UNALLOCATED           | UNALLOCATED           | -                              |
| 00    | != 11111 | STNT1B register)      | (scalar               | plus                  | scalar,               | single                | FEAT_SVE &#124;&#124; FEAT_SME |
| 01    | != 11111 | STNT1H register)      | (scalar               | plus                  | scalar,               | single                | FEAT_SVE &#124;&#124; FEAT_SME |
| 10    | != 11111 | STNT1W register)      | (scalar               | plus                  | scalar,               | single                | FEAT_SVE &#124;&#124; FEAT_SME |
| 11    | != 11111 | STNT1D register)      | (scalar               | plus                  | scalar,               | single                | FEAT_SVE &#124;&#124; FEAT_SME |

## SVE store multiple structures (scalar plus scalar)

The encodings in this section are decoded from SVE Memory - Non-temporal and Multi-register Contiguous Store.

<!-- image -->

The following constraints also apply to this encoding: opc != '00'

| msz   | opc   | Rm       | Instruction Details       | Feature                        |
|-------|-------|----------|---------------------------|--------------------------------|
| xx    | != 00 | 11111    | UNALLOCATED               | -                              |
| 00    | 01    | != 11111 | ST2B (scalar plus scalar) | FEAT_SVE &#124;&#124; FEAT_SME |
| 00    | 10    | != 11111 | ST3B (scalar plus scalar) | FEAT_SVE &#124;&#124; FEAT_SME |
| 00    | 11    | != 11111 | ST4B (scalar plus scalar) | FEAT_SVE &#124;&#124; FEAT_SME |

| op0   | Instruction details                                   |
|-------|-------------------------------------------------------|
| 00    | SVEcontiguous non-temporal store (scalar plus scalar) |
| != 00 | SVE store multiple structures (scalar plus scalar)    |

|   msz |   opc | Rm       | Instruction Details       | Feature                        |
|-------|-------|----------|---------------------------|--------------------------------|
|    01 |    01 | != 11111 | ST2H (scalar plus scalar) | FEAT_SVE &#124;&#124; FEAT_SME |
|    01 |    10 | != 11111 | ST3H (scalar plus scalar) | FEAT_SVE &#124;&#124; FEAT_SME |
|    01 |    11 | != 11111 | ST4H (scalar plus scalar) | FEAT_SVE &#124;&#124; FEAT_SME |
|    10 |    01 | != 11111 | ST2W (scalar plus scalar) | FEAT_SVE &#124;&#124; FEAT_SME |
|    10 |    10 | != 11111 | ST3W (scalar plus scalar) | FEAT_SVE &#124;&#124; FEAT_SME |
|    10 |    11 | != 11111 | ST4W (scalar plus scalar) | FEAT_SVE &#124;&#124; FEAT_SME |
|    11 |    01 | != 11111 | ST2D (scalar plus scalar) | FEAT_SVE &#124;&#124; FEAT_SME |
|    11 |    10 | != 11111 | ST3D (scalar plus scalar) | FEAT_SVE &#124;&#124; FEAT_SME |
|    11 |    11 | != 11111 | ST4D (scalar plus scalar) | FEAT_SVE &#124;&#124; FEAT_SME |

## SVE Memory - Contiguous Store and Unsized Contiguous

SVE Memory - Contiguous Store and Unsized Contiguous

The encodings in this section are decoded from SVE encodings.

<!-- image -->

| 31    | 25 24   | 22 21 20 19   | 16 15 14 13 12   | 5 4 3   |
|-------|---------|---------------|------------------|---------|
| 1 1 1 | 0 op0   | op1           | 0 op2 0          | op3     |

| op0    | op1   |   op2 | op3   | Instruction details                                              | Feature                        |
|--------|-------|-------|-------|------------------------------------------------------------------|--------------------------------|
| 0xx    | 00    |     0 | x     | SVE store multiple structures (quadwords, scalar plus immediate) | -                              |
| 0xx    | 01    |     0 | x     | UNALLOCATED                                                      | -                              |
| 0xx    | 1x    |     0 | x     | SVE store multiple structures (quadwords, scalar plus scalar)    | -                              |
| 10x    | xx    |     0 | x     | UNALLOCATED                                                      | -                              |
| 110    | xx    |     0 | 0     | STR (predicate)                                                  | FEAT_SVE &#124;&#124; FEAT_SME |
| 110    | xx    |     0 | 1     | UNALLOCATED                                                      | -                              |
| 110    | xx    |     1 | x     | STR (vector)                                                     | FEAT_SVE &#124;&#124; FEAT_SME |
| 111    | xx    |     0 | x     | UNALLOCATED                                                      | -                              |
| != 110 | xx    |     1 | x     | SVE contiguous store (scalar plus scalar)                        | -                              |

## SVE store multiple structures (quadwords, scalar plus immediate)

The encodings in this section are decoded from SVE Memory - Contiguous Store and Unsized Contiguous.

<!-- image -->

|   num | Instruction Details          | Feature                              |
|-------|------------------------------|--------------------------------------|
|    00 | UNALLOCATED                  | -                                    |
|    01 | ST2Q (scalar plus immediate) | FEAT_SVE2p1 &#124;&#124; FEAT_SME2p1 |
|    10 | ST3Q (scalar plus immediate) | FEAT_SVE2p1 &#124;&#124; FEAT_SME2p1 |
|    11 | ST4Q (scalar plus immediate) | FEAT_SVE2p1 &#124;&#124; FEAT_SME2p1 |

## SVE store multiple structures (quadwords, scalar plus scalar)

The encodings in this section are decoded from SVE Memory - Contiguous Store and Unsized Contiguous.

<!-- image -->

| num   | Rm       | Instruction Details       | Feature                              |
|-------|----------|---------------------------|--------------------------------------|
| 00    | xxxxx    | UNALLOCATED               | -                                    |
| 01    | != 11111 | ST2Q (scalar plus scalar) | FEAT_SVE2p1 &#124;&#124; FEAT_SME2p1 |
| 10    | != 11111 | ST3Q (scalar plus scalar) | FEAT_SVE2p1 &#124;&#124; FEAT_SME2p1 |
| 11    | != 11111 | ST4Q (scalar plus scalar) | FEAT_SVE2p1 &#124;&#124; FEAT_SME2p1 |
| != 00 | 11111    | UNALLOCATED               | -                                    |

## SVE contiguous store (scalar plus scalar)

The encodings in this section are decoded from SVE Memory - Contiguous Store and Unsized Contiguous.

<!-- image -->

The following constraints also apply to this encoding: opc != '110'

| opc   | o2   | Rm       | Instruction Details                        | Feature                        |
|-------|------|----------|--------------------------------------------|--------------------------------|
| xx1   | x    | 11111    | UNALLOCATED                                | -                              |
| 0x0   | x    | 11111    | UNALLOCATED                                | -                              |
| 00x   | x    | != 11111 | ST1B (scalar plus scalar, single register) | FEAT_SVE &#124;&#124; FEAT_SME |
| 01x   | x    | != 11111 | ST1H (scalar plus scalar, single register) | FEAT_SVE &#124;&#124; FEAT_SME |
| 100   | 0    | 11111    | UNALLOCATED                                | -                              |

|   opc | o2   | Rm       | Instruction Details                              | Feature                        |
|-------|------|----------|--------------------------------------------------|--------------------------------|
|   100 | 0    | != 11111 | ST1W (scalar plus scalar, single register) -SVE2 | FEAT_SVE2p1                    |
|   100 | 1    | xxxxx    | UNALLOCATED                                      | -                              |
|   101 | x    | != 11111 | ST1W (scalar plus scalar, single register) -SVE  | FEAT_SVE &#124;&#124; FEAT_SME |
|   111 | 0    | != 11111 | ST1D(scalar plus scalar, single register)- SVE2  | FEAT_SVE2p1                    |
|   111 | 1    | != 11111 | ST1D(scalar plus scalar, single register)- SVE   | FEAT_SVE &#124;&#124; FEAT_SME |

## SVE Memory - Scatter

SVE Memory - Scatter

The encodings in this section are decoded from SVE encodings.

<!-- image -->

|   op0 | Instruction details                                            |
|-------|----------------------------------------------------------------|
|    00 | SVE 64-bit scatter store (scalar plus 64-bit unscaled offsets) |
|    01 | SVE 64-bit scatter store (scalar plus 64-bit scaled offsets)   |
|    10 | SVE 64-bit scatter store (vector plus immediate)               |
|    11 | SVE 32-bit scatter store (vector plus immediate)               |

## SVE 64-bit scatter store (scalar plus 64-bit unscaled offsets)

The encodings in this section are decoded from SVE Memory - Scatter.

<!-- image -->

|   msz | Instruction Details       | Feature   |
|-------|---------------------------|-----------|
|    00 | ST1B (scalar plus vector) | FEAT_SVE  |
|    01 | ST1H (scalar plus vector) | FEAT_SVE  |
|    10 | ST1W (scalar plus vector) | FEAT_SVE  |

|   msz | Instruction Details       | Feature   |
|-------|---------------------------|-----------|
|    11 | ST1D (scalar plus vector) | FEAT_SVE  |

## SVE 64-bit scatter store (scalar plus 64-bit scaled offsets)

The encodings in this section are decoded from SVE Memory - Scatter.

<!-- image -->

|   msz | Instruction Details       | Feature   |
|-------|---------------------------|-----------|
|    00 | UNALLOCATED               | -         |
|    01 | ST1H (scalar plus vector) | FEAT_SVE  |
|    10 | ST1W (scalar plus vector) | FEAT_SVE  |
|    11 | ST1D (scalar plus vector) | FEAT_SVE  |

## SVE 64-bit scatter store (vector plus immediate)

The encodings in this section are decoded from SVE Memory - Scatter.

<!-- image -->

| 31    | 25 24 23 22 21 20   | 16 15   | 13 12   | 10 9   | 5 4   | 0   |
|-------|---------------------|---------|---------|--------|-------|-----|
| 1 1 1 | 0 msz 1 0           | imm5    | 1 0 1   | Pg     | Zn    | Zt  |

|   msz | Instruction Details          | Feature   |
|-------|------------------------------|-----------|
|    00 | ST1B (vector plus immediate) | FEAT_SVE  |
|    01 | ST1H (vector plus immediate) | FEAT_SVE  |
|    10 | ST1W (vector plus immediate) | FEAT_SVE  |
|    11 | ST1D (vector plus immediate) | FEAT_SVE  |

## SVE 32-bit scatter store (vector plus immediate)

The encodings in this section are decoded from SVE Memory - Scatter.

<!-- image -->

|   msz | Instruction Details          | Feature   |
|-------|------------------------------|-----------|
|    00 | ST1B (vector plus immediate) | FEAT_SVE  |
|    01 | ST1H (vector plus immediate) | FEAT_SVE  |
|    10 | ST1W (vector plus immediate) | FEAT_SVE  |
|    11 | UNALLOCATED                  | -         |

## SVE Memory - Contiguous Store with Immediate Offset

SVE Memory - Contiguous Store with Immediate Offset

The encodings in this section are decoded from SVE encodings.

<!-- image -->

| op0   |   op1 | Instruction details                                      |
|-------|-------|----------------------------------------------------------|
| 00    |     1 | SVEcontiguous non-temporal store (scalar plus immediate) |
| xx    |     0 | SVE contiguous store (scalar plus immediate)             |
| != 00 |     1 | SVE store multiple structures (scalar plus immediate)    |

## SVE contiguous non-temporal store (scalar plus immediate)

The encodings in this section are decoded from SVE Memory - Contiguous Store with Immediate Offset.

<!-- image -->

| 31    | 25 24 23   | 22 21 20 19   | 16 15   | 13 12   | 10 9   | 5 4   | 0   |
|-------|------------|---------------|---------|---------|--------|-------|-----|
| 1 1 1 | 0 msz      | 0 0 1         | imm4    | 1 1 1   | Pg     | Rn    | Zt  |

|   msz | Instruction Details                             | Feature                        |
|-------|-------------------------------------------------|--------------------------------|
|    00 | STNT1B (scalar plus immediate, single register) | FEAT_SVE &#124;&#124; FEAT_SME |
|    01 | STNT1H (scalar plus immediate, single register) | FEAT_SVE &#124;&#124; FEAT_SME |
|    10 | STNT1W (scalar plus immediate, single register) | FEAT_SVE &#124;&#124; FEAT_SME |

|   msz | Instruction Details                             | Feature                        |
|-------|-------------------------------------------------|--------------------------------|
|    11 | STNT1D (scalar plus immediate, single register) | FEAT_SVE &#124;&#124; FEAT_SME |

## SVE contiguous store (scalar plus immediate)

The encodings in this section are decoded from SVE Memory - Contiguous Store with Immediate Offset.

<!-- image -->

| 31    | 25 24   | 23 22 21   | 20   |   19 | 16 15   | 13 12   | 10   | 5   | 0   |
|-------|---------|------------|------|------|---------|---------|------|-----|-----|
| 1 1 1 | 1 0     | msz        | opc  |    0 | imm4    | 1 1 1   | Pg   | Rn  | Zt  |

|   msz | opc   | Instruction Details              |            |        | Feature                        |
|-------|-------|----------------------------------|------------|--------|--------------------------------|
|    00 | xx    | ST1B (scalar plus register)      | immediate, | single | FEAT_SVE &#124;&#124; FEAT_SME |
|    01 | xx    | ST1H (scalar plus register)      | immediate, | single | FEAT_SVE &#124;&#124; FEAT_SME |
|    10 | 00    | ST1W (scalar plus register)-SVE2 | immediate, | single | FEAT_SVE2p1                    |
|    10 | 01    | UNALLOCATED                      |            |        | -                              |
|    10 | 1x    | ST1W (scalar plus register)-SVE  | immediate, | single | FEAT_SVE &#124;&#124; FEAT_SME |
|    11 | 0x    | UNALLOCATED                      |            |        | -                              |
|    11 | 10    | ST1D (scalar plus register)-SVE2 | immediate, | single | FEAT_SVE2p1                    |
|    11 | 11    | ST1D (scalar plus register)-SVE  | immediate, | single | FEAT_SVE &#124;&#124; FEAT_SME |

## SVE store multiple structures (scalar plus immediate)

The encodings in this section are decoded from SVE Memory - Contiguous Store with Immediate Offset.

<!-- image -->

The following constraints also apply to this encoding: opc != '00'

|   msz |   opc | Instruction Details          | Feature                        |
|-------|-------|------------------------------|--------------------------------|
|    00 |    01 | ST2B (scalar plus immediate) | FEAT_SVE &#124;&#124; FEAT_SME |

|   msz |   opc | Instruction Details          | Feature                        |
|-------|-------|------------------------------|--------------------------------|
|    00 |    10 | ST3B (scalar plus immediate) | FEAT_SVE &#124;&#124; FEAT_SME |
|    00 |    11 | ST4B (scalar plus immediate) | FEAT_SVE &#124;&#124; FEAT_SME |
|    01 |    01 | ST2H (scalar plus immediate) | FEAT_SVE &#124;&#124; FEAT_SME |
|    01 |    10 | ST3H (scalar plus immediate) | FEAT_SVE &#124;&#124; FEAT_SME |
|    01 |    11 | ST4H (scalar plus immediate) | FEAT_SVE &#124;&#124; FEAT_SME |
|    10 |    01 | ST2W (scalar plus immediate) | FEAT_SVE &#124;&#124; FEAT_SME |
|    10 |    10 | ST3W (scalar plus immediate) | FEAT_SVE &#124;&#124; FEAT_SME |
|    10 |    11 | ST4W (scalar plus immediate) | FEAT_SVE &#124;&#124; FEAT_SME |
|    11 |    01 | ST2D (scalar plus immediate) | FEAT_SVE &#124;&#124; FEAT_SME |
|    11 |    10 | ST3D (scalar plus immediate) | FEAT_SVE &#124;&#124; FEAT_SME |
|    11 |    11 | ST4D (scalar plus immediate) | FEAT_SVE &#124;&#124; FEAT_SME |

## SVE Memory - Scatter with Optional Sign Extend

SVE Memory - Scatter with Optional Sign Extend

The encodings in this section are decoded from SVE encodings.

<!-- image -->

| 31          | 22 21 20 16 15 14 13   |
|-------------|------------------------|
| 1 1 1 0 0 1 | op0 1 0                |

|   op0 | Instruction details                                                     |
|-------|-------------------------------------------------------------------------|
|    00 | SVE 64-bit scatter store (scalar plus unpacked 32-bit unscaled offsets) |
|    01 | SVE 64-bit scatter store (scalar plus unpacked 32-bit scaled offsets)   |
|    10 | SVE 32-bit scatter store (scalar plus 32-bit unscaled offsets)          |
|    11 | SVE 32-bit scatter store (scalar plus 32-bit scaled offsets)            |

## SVE 64-bit scatter store (scalar plus unpacked 32-bit unscaled offsets)

The encodings in this section are decoded from SVE Memory - Scatter with Optional Sign Extend.

<!-- image -->

| 31    | 25 24 23 22 21 20   | 16 15   | 14 13 12   | 5   |    |
|-------|---------------------|---------|------------|-----|----|
| 1 1 1 | 0 msz 0 0           | Zm 1    | xs 0 Pg    | Rn  | Zt |

|   msz | Instruction Details       | Feature   |
|-------|---------------------------|-----------|
|    00 | ST1B (scalar plus vector) | FEAT_SVE  |
|    01 | ST1H (scalar plus vector) | FEAT_SVE  |
|    10 | ST1W (scalar plus vector) | FEAT_SVE  |
|    11 | ST1D (scalar plus vector) | FEAT_SVE  |

## SVE 64-bit scatter store (scalar plus unpacked 32-bit scaled offsets)

The encodings in this section are decoded from SVE Memory - Scatter with Optional Sign Extend.

<!-- image -->

| 31      | 25 24 23 22 21 20   | 16 15 14 13 12 10 9 5 4   |
|---------|---------------------|---------------------------|
| 1 1 1 0 | 0 msz 0 1 Zm 1 xs 0 | Pg Rn Zt                  |

|   msz | Instruction Details       | Feature   |
|-------|---------------------------|-----------|
|    00 | UNALLOCATED               | -         |
|    01 | ST1H (scalar plus vector) | FEAT_SVE  |
|    10 | ST1W (scalar plus vector) | FEAT_SVE  |
|    11 | ST1D (scalar plus vector) | FEAT_SVE  |

## SVE 32-bit scatter store (scalar plus 32-bit unscaled offsets)

The encodings in this section are decoded from SVE Memory - Scatter with Optional Sign Extend.

<!-- image -->

| 31      | 25 24 23 22 21 20   | 16 15 14   | 13 12   | 10 9   | 5 4   |    |
|---------|---------------------|------------|---------|--------|-------|----|
| 1 1 1 0 | 0 msz 1 0           | Zm         | 1 xs 0  | Pg     | Rn    | Zt |

|   msz | Instruction Details       | Feature   |
|-------|---------------------------|-----------|
|    00 | ST1B (scalar plus vector) | FEAT_SVE  |
|    01 | ST1H (scalar plus vector) | FEAT_SVE  |
|    10 | ST1W (scalar plus vector) | FEAT_SVE  |
|    11 | UNALLOCATED               | -         |

## SVE 32-bit scatter store (scalar plus 32-bit scaled offsets)

The encodings in this section are decoded from SVE Memory - Scatter with Optional Sign Extend.

<!-- image -->

| 31      | 25 24 23 22 21 20   | 16 15        | 14 13 12 10 9 5 4   |
|---------|---------------------|--------------|---------------------|
| 1 1 1 0 | 0 msz 1 1           | Zm 1 xs 0 Pg | Rn Zt               |

|   msz | Instruction Details       | Feature   |
|-------|---------------------------|-----------|
|    00 | UNALLOCATED               | -         |
|    01 | ST1H (scalar plus vector) | FEAT_SVE  |
|    10 | ST1W (scalar plus vector) | FEAT_SVE  |
|    11 | UNALLOCATED               | -         |

## SVE integer add/subtract vectors (unpredicated)

The encodings in this section are decoded from SVE encodings.

<!-- image -->

| size   | opc   | Instruction Details           | Feature                        |
|--------|-------|-------------------------------|--------------------------------|
| xx     | 000   | ADD(vectors, unpredicated)    | FEAT_SVE &#124;&#124; FEAT_SME |
| xx     | 001   | SUB (vectors, unpredicated)   | FEAT_SVE &#124;&#124; FEAT_SME |
| xx     | 100   | SQADD(vectors, unpredicated)  | FEAT_SVE &#124;&#124; FEAT_SME |
| xx     | 101   | UQADD(vectors, unpredicated)  | FEAT_SVE &#124;&#124; FEAT_SME |
| xx     | 110   | SQSUB (vectors, unpredicated) | FEAT_SVE &#124;&#124; FEAT_SME |
| xx     | 111   | UQSUB(vectors, unpredicated)  | FEAT_SVE &#124;&#124; FEAT_SME |
| 11     | 010   | ADDPT(unpredicated)           | FEAT_SVE &&FEAT_CPA            |
| 11     | 011   | SUBPT (unpredicated)          | FEAT_SVE &&FEAT_CPA            |
| != 11  | 01x   | UNALLOCATED                   | -                              |

## SVE address generation

The encodings in this section are decoded from SVE encodings.

<!-- image -->

| opc   | Instruction Details                 | Feature   |
|-------|-------------------------------------|-----------|
| 00    | ADR-Unpacked 32-bit signed offsets  | FEAT_SVE  |
| 01    | ADR-Unpacked32-bit unsigned offsets | FEAT_SVE  |
| 1x    | ADR-Packed offsets                  | FEAT_SVE  |

## SVE table lookup (three sources)

The encodings in this section are decoded from SVE encodings.

<!-- image -->

| 31   | 29 28   | 24 23 22   | 21   |   20 | 16   | 15 11 10     | 5 4   | 0   |
|------|---------|------------|------|------|------|--------------|-------|-----|
| 0 0  | 0 0     | 0 1 0 1    | size |    1 | Zm   | 0 0 1 0 1 op | Zn    | Zd  |

|   op | Instruction Details   | Feature                         |
|------|-----------------------|---------------------------------|
|    0 | TBL                   | FEAT_SVE2 &#124;&#124; FEAT_SME |
|    1 | TBX                   | FEAT_SVE2 &#124;&#124; FEAT_SME |

## SVE permute vector elements

The encodings in this section are decoded from SVE encodings.

<!-- image -->

|   opc | Instruction Details               | Feature                        |
|-------|-----------------------------------|--------------------------------|
|   000 | ZIP1, ZIP2 (vectors) -Lowhalves   | FEAT_SVE &#124;&#124; FEAT_SME |
|   001 | ZIP1, ZIP2 (vectors) -High halves | FEAT_SVE &#124;&#124; FEAT_SME |
|   010 | UZP1, UZP2 (vectors) -Even        | FEAT_SVE &#124;&#124; FEAT_SME |
|   011 | UZP1, UZP2 (vectors)-Odd          | FEAT_SVE &#124;&#124; FEAT_SME |

| opc   | Instruction Details        | Feature                        |
|-------|----------------------------|--------------------------------|
| 100   | TRN1, TRN2 (vectors) -Even | FEAT_SVE &#124;&#124; FEAT_SME |
| 101   | TRN1, TRN2 (vectors)-Odd   | FEAT_SVE &#124;&#124; FEAT_SME |
| 11x   | UNALLOCATED                | -                              |

## SVE integer compare with unsigned immediate

The encodings in this section are decoded from SVE encodings.

<!-- image -->

| 31   | 29 28   | 24 23 22 21   | 20   | 14 13 12   | 10   | 9   | 5 4   | 0   |
|------|---------|---------------|------|------------|------|-----|-------|-----|
| 0 0  | 1 0     | 0 1           | imm7 | lt         | Pg   | Zn  | ne    | Pd  |

|   lt | ne                                    | Instruction Details Feature                  |
|------|---------------------------------------|----------------------------------------------|
|    0 | 0 CMP < cc > (immediate)-Higherorsame | FEAT_SVE &#124;&#124; FEAT_SME               |
|    0 | 1 CMP < cc > (immediate)              | -Higher FEAT_SVE &#124;&#124; FEAT_SME       |
|    1 | 0 CMP < cc > (immediate) -Lower       | FEAT_SVE &#124;&#124; FEAT_SME               |
|    1 | 1 CMP < cc > (immediate)              | -Loweror same FEAT_SVE &#124;&#124; FEAT_SME |

## SVE predicate logical operations

The encodings in this section are decoded from SVE encodings.

<!-- image -->

| 31   |   29 28 | 24 23 22 21 20 19   | 16 15 14   | 13 10   | 9 8   | 5 4      | 0   |
|------|---------|---------------------|------------|---------|-------|----------|-----|
| 0 0  |       1 | 0 0 1 0 1 op S      | 0 0        | Pm 0 1  | Pg    | o2 Pn o3 | Pd  |

|   op |   S |   o2 |   o3 | Instruction Details   | Feature                        |
|------|-----|------|------|-----------------------|--------------------------------|
|    0 |   0 |    0 |    0 | AND(predicates)       | FEAT_SVE &#124;&#124; FEAT_SME |
|    0 |   0 |    0 |    1 | BIC (predicates)      | FEAT_SVE &#124;&#124; FEAT_SME |
|    0 |   0 |    1 |    0 | EOR(predicates)       | FEAT_SVE &#124;&#124; FEAT_SME |
|    0 |   0 |    1 |    1 | SEL (predicates)      | FEAT_SVE &#124;&#124; FEAT_SME |
|    0 |   1 |    0 |    0 | ANDS                  | FEAT_SVE &#124;&#124; FEAT_SME |
|    0 |   1 |    0 |    1 | BICS                  | FEAT_SVE &#124;&#124; FEAT_SME |
|    0 |   1 |    1 |    0 | EORS                  | FEAT_SVE &#124;&#124; FEAT_SME |
|    0 |   1 |    1 |    1 | UNALLOCATED           | -                              |

|   op |   S |   o2 |   o3 | Instruction Details   | Feature                        |
|------|-----|------|------|-----------------------|--------------------------------|
|    1 |   0 |    0 |    0 | ORR(predicates)       | FEAT_SVE &#124;&#124; FEAT_SME |
|    1 |   0 |    0 |    1 | ORN(predicates)       | FEAT_SVE &#124;&#124; FEAT_SME |
|    1 |   0 |    1 |    0 | NOR                   | FEAT_SVE &#124;&#124; FEAT_SME |
|    1 |   0 |    1 |    1 | NAND                  | FEAT_SVE &#124;&#124; FEAT_SME |
|    1 |   1 |    0 |    0 | ORRS                  | FEAT_SVE &#124;&#124; FEAT_SME |
|    1 |   1 |    0 |    1 | ORNS                  | FEAT_SVE &#124;&#124; FEAT_SME |
|    1 |   1 |    1 |    0 | NORS                  | FEAT_SVE &#124;&#124; FEAT_SME |
|    1 |   1 |    1 |    1 | NANDS                 | FEAT_SVE &#124;&#124; FEAT_SME |

## SVE integer compare with signed immediate

The encodings in this section are decoded from SVE encodings.

<!-- image -->

| 31    |   29 28 | 24 23 22 21 20   |    | 16 15 14 13   | 12   | 10 9   | 5 4   | 0   |
|-------|---------|------------------|----|---------------|------|--------|-------|-----|
| 0 0 1 |       0 | 1 size           |  0 | op 0          | o2   | Zn     | ne    | Pd  |

|   op |   o2 | ne   | Instruction Details                           | Feature                        |
|------|------|------|-----------------------------------------------|--------------------------------|
|    0 |    0 | 0    | CMP < cc > (immediate) -Greater than or equal | FEAT_SVE &#124;&#124; FEAT_SME |
|    0 |    0 | 1    | CMP < cc > (immediate) -Greater than          | FEAT_SVE &#124;&#124; FEAT_SME |
|    0 |    1 | 0    | CMP < cc > (immediate) -Less than             | FEAT_SVE &#124;&#124; FEAT_SME |
|    0 |    1 | 1    | CMP < cc > (immediate) - Less than or equal   | FEAT_SVE &#124;&#124; FEAT_SME |
|    1 |    0 | 0    | CMP < cc > (immediate) -Equal                 | FEAT_SVE &#124;&#124; FEAT_SME |
|    1 |    0 | 1    | CMP < cc > (immediate) -Notequal              | FEAT_SVE &#124;&#124; FEAT_SME |
|    1 |    1 | x    | UNALLOCATED                                   | -                              |

## SVE broadcast predicate element

The encodings in this section are decoded from SVE encodings.

<!-- image -->

## SVE two-way dot product

The encodings in this section are decoded from SVE encodings.

<!-- image -->

|   U | Instruction Details   | Feature                            |
|-----|-----------------------|------------------------------------|
|   0 | SDOT (2-way, vectors) | FEAT_SME2 &#124;&#124; FEAT_SVE2p1 |
|   1 | UDOT(2-way, vectors)  | FEAT_SME2 &#124;&#124; FEAT_SVE2p1 |

## SVE two-way dot product (indexed)

The encodings in this section are decoded from SVE encodings.

<!-- image -->

|   U | Instruction Details   | Feature                            |
|-----|-----------------------|------------------------------------|
|   0 | SDOT (2-way, indexed) | FEAT_SME2 &#124;&#124; FEAT_SVE2p1 |
|   1 | UDOT(2-way, indexed)  | FEAT_SME2 &#124;&#124; FEAT_SVE2p1 |

## SVE integer clamp

The encodings in this section are decoded from SVE encodings.

<!-- image -->

|   S | Instruction Details   | Feature                           |
|-----|-----------------------|-----------------------------------|
|   0 | PSEL                  | FEAT_SME &#124;&#124; FEAT_SVE2p1 |
|   1 | UNALLOCATED           | -                                 |

|   U | Instruction Details   | Feature                           |
|-----|-----------------------|-----------------------------------|
|   0 | SCLAMP                | FEAT_SME &#124;&#124; FEAT_SVE2p1 |
|   1 | UCLAMP                | FEAT_SME &#124;&#124; FEAT_SVE2p1 |

## SVE2 multiply-add (checked pointer)

The encodings in this section are decoded from SVE encodings.

<!-- image -->

| 31    | 24 23 22 21   | 20 16 12        | 15 11 10 9 5 4   |
|-------|---------------|-----------------|------------------|
| 0 1 0 | 0 opc 0       | Zm 1 1 0 1 o2 0 | Zn Zda           |

| opc   | o2   | Instruction Details   | Feature             |
|-------|------|-----------------------|---------------------|
| 11    | 0    | MLAPT                 | FEAT_SVE &&FEAT_CPA |
| 11    | 1    | MADPT                 | FEAT_SVE &&FEAT_CPA |
| != 11 | x    | UNALLOCATED           | -                   |

## SVE permute vector elements (quadwords)

The encodings in this section are decoded from SVE encodings.

<!-- image -->

| 31   |   29 28 | 24 23 22 21 20   |   16 15 | 13 12    | 10   | 5   | 0   |
|------|---------|------------------|---------|----------|------|-----|-----|
| 0 1  |       0 | 0 0 1 0 0 size   |       0 | Zm 1 1 1 | opc  | Zn  | Zd  |

| opc   | Instruction Details   | Feature                              |
|-------|-----------------------|--------------------------------------|
| 000   | ZIPQ1                 | FEAT_SVE2p1 &#124;&#124; FEAT_SME2p1 |
| 001   | ZIPQ2                 | FEAT_SVE2p1 &#124;&#124; FEAT_SME2p1 |
| 010   | UZPQ1                 | FEAT_SVE2p1 &#124;&#124; FEAT_SME2p1 |
| 011   | UZPQ2                 | FEAT_SVE2p1 &#124;&#124; FEAT_SME2p1 |
| 10x   | UNALLOCATED           | -                                    |
| 110   | TBLQ                  | FEAT_SVE2p1 &#124;&#124; FEAT_SME2p1 |
| 111   | UNALLOCATED           | -                                    |

## SVE2 character match

The encodings in this section are decoded from SVE encodings.

<!-- image -->

| 31   | 29 28   | 24 23 22 21 20   |      | 16 15 13   | 12    | 10 9   | 5 4   | 0   |
|------|---------|------------------|------|------------|-------|--------|-------|-----|
| 0 1  | 0 0     | 0 1 0 1          | size | 1 Zm       | 1 0 0 | Pg     | op    | Pd  |

|   op | Instruction Details   | Feature   |
|------|-----------------------|-----------|
|    0 | MATCH                 | FEAT_SVE2 |
|    1 | NMATCH                | FEAT_SVE2 |

## SVE2 FP8 matrix multiply-accumulate

The encodings in this section are decoded from SVE encodings.

<!-- image -->

|   op | Instruction Details          | Feature                  |
|------|------------------------------|--------------------------|
|    0 | FMMLA(widening, FP8 to FP32) | FEAT_SVE2 &&FEAT_F8F32MM |
|    1 | FMMLA(widening, FP8 to FP16) | FEAT_SVE2 &&FEAT_F8F16MM |

## SVE2 FP8 multiply-add long (indexed)

The encodings in this section are decoded from SVE encodings.

<!-- image -->

| 31   |   29 28 | 24 23 22 21 20 19   |     |   18 | 16   | 15 12 11 10   | 9 5   | 4   | 0   |
|------|---------|---------------------|-----|------|------|---------------|-------|-----|-----|
| 0 1  |       1 | 0 0 1 0 0           | T 0 |    1 | i4h  | Zm 0 1 0 1    | i4l   | Zn  | Zda |

|   T | Instruction Details           | Feature                                                 |
|-----|-------------------------------|---------------------------------------------------------|
|   0 | FMLALB(indexed, FP8 to FP16)  | FEAT_SSVE_FP8FMA &#124;&#124; (FEAT_SVE2 &&FEAT_FP8FMA) |
|   1 | FMLALT (indexed, FP8 to FP16) | FEAT_SSVE_FP8FMA &#124;&#124; (FEAT_SVE2 &&FEAT_FP8FMA) |

## SVE floating-point convert (top, predicated)

The encodings in this section are decoded from SVE encodings.

<!-- image -->

|   31 | 29 28   | 24 23 22 21   | 18 17 16 15   | 13 12   | 10 9   | 5 4   |    |
|------|---------|---------------|---------------|---------|--------|-------|----|
|    0 | 1 1 0   | 0 opc         | 0 0 0 0 opc2  | 1 0 1   | Pg     | Zn    | Zd |

| opc   | opc2   | Instruction Details                                                  | Feature                              |
|-------|--------|----------------------------------------------------------------------|--------------------------------------|
| x0    | 11     | UNALLOCATED                                                          | -                                    |
| 00    | 0x     | UNALLOCATED                                                          | -                                    |
| 00    | 10     | FCVTXNT                                                              | FEAT_SVE2p2 &#124;&#124; FEAT_SME2p2 |
| 01    | xx     | UNALLOCATED                                                          | -                                    |
| 10    | 00     | FCVTNT (predicated) -Single-precision to half-precision, zeroing     | FEAT_SVE2p2 &#124;&#124; FEAT_SME2p2 |
| 10    | 01     | FCVTLT - Half-precision to single- precision, zeroing                | FEAT_SVE2p2 &#124;&#124; FEAT_SME2p2 |
| 10    | 10     | BFCVTNT                                                              | FEAT_SVE2p2 &#124;&#124; FEAT_SME2p2 |
| 11    | 0x     | UNALLOCATED                                                          | -                                    |
| 11    | 10     | FCVTNT (predicated) - Double- precision to single-precision, zeroing | FEAT_SVE2p2 &#124;&#124; FEAT_SME2p2 |
| 11    | 11     | FCVTLT - Single-precision to double- precision, zeroing              | FEAT_SVE2p2 &#124;&#124; FEAT_SME2p2 |

## SVE floating-point convert precision odd elements

The encodings in this section are decoded from SVE encodings.

<!-- image -->

| 31   | 29 28   | 24 23 22 21   | 18 17 16 15   | 13 12      | 10   | 5 4   |
|------|---------|---------------|---------------|------------|------|-------|
| 0 1  | 1 0     | 0 opc         | 0 0 1 0       | opc2 1 0 1 | Pg   | Zd    |

| opc   | opc2   | Instruction Details                                              | Feature                         |
|-------|--------|------------------------------------------------------------------|---------------------------------|
| x0    | 11     | UNALLOCATED                                                      | -                               |
| 00    | 0x     | UNALLOCATED                                                      | -                               |
| 00    | 10     | FCVTXNT                                                          | FEAT_SVE2 &#124;&#124; FEAT_SME |
| 01    | xx     | UNALLOCATED                                                      | -                               |
| 10    | 00     | FCVTNT (predicated) -Single-precision to half-precision, merging | FEAT_SVE2 &#124;&#124; FEAT_SME |

|   opc | opc2   | Instruction Details                                                  | Feature                                                    |
|-------|--------|----------------------------------------------------------------------|------------------------------------------------------------|
|    10 | 01     | FCVTLT - Half-precision to single- precision, merging                | FEAT_SVE2 &#124;&#124; FEAT_SME                            |
|    10 | 10     | BFCVTNT                                                              | (FEAT_SVE &&FEAT_BF16) &#124;&#124; (FEAT_SME &&FEAT_BF16) |
|    11 | 0x     | UNALLOCATED                                                          | -                                                          |
|    11 | 10     | FCVTNT (predicated) - Double- precision to single-precision, merging | FEAT_SVE2 &#124;&#124; FEAT_SME                            |
|    11 | 11     | FCVTLT - Single-precision to double- precision, merging              | FEAT_SVE2 &#124;&#124; FEAT_SME                            |

## SVE2 floating-point pairwise operations

The encodings in this section are decoded from SVE encodings.

<!-- image -->

|   31 | 29 28   | 24 23 22   |   21 |   19 18 | 16   | 15 13 12   | 10   | 5   | 0   |
|------|---------|------------|------|---------|------|------------|------|-----|-----|
|    0 | 1 1     | 0 0 1 0 0  |    0 |       0 | opc  | 1 0 0      | Pg   | Zm  | Zdn |

| opc   | Instruction Details   | Feature                         |
|-------|-----------------------|---------------------------------|
| 000   | FADDP                 | FEAT_SVE2 &#124;&#124; FEAT_SME |
| 001   | UNALLOCATED           | -                               |
| 01x   | UNALLOCATED           | -                               |
| 100   | FMAXNMP               | FEAT_SVE2 &#124;&#124; FEAT_SME |
| 101   | FMINNMP               | FEAT_SVE2 &#124;&#124; FEAT_SME |
| 110   | FMAXP                 | FEAT_SVE2 &#124;&#124; FEAT_SME |
| 111   | FMINP                 | FEAT_SVE2 &#124;&#124; FEAT_SME |

## SVE floating-point recursive reduction (quadwords)

The encodings in this section are decoded from SVE encodings.

<!-- image -->

|   31 | 29 28   | 24 23 22 21   | 19 18   | 16 15   | 13 12   |   10 |    | 5 4   | 0   |
|------|---------|---------------|---------|---------|---------|------|----|-------|-----|
|    0 | 1 1     | 0 0 1 0 0     | size 0  | 1 0 opc | 1 0     |    1 | Pg | Zn    | Vd  |

|   opc | Instruction Details   | Feature                              |
|-------|-----------------------|--------------------------------------|
|   000 | FADDQV                | FEAT_SVE2p1 &#124;&#124; FEAT_SME2p1 |
|   001 | UNALLOCATED           | -                                    |

| opc   | Instruction Details   | Feature                              |
|-------|-----------------------|--------------------------------------|
| 01x   | UNALLOCATED           | -                                    |
| 100   | FMAXNMQV              | FEAT_SVE2p1 &#124;&#124; FEAT_SME2p1 |
| 101   | FMINNMQV              | FEAT_SVE2p1 &#124;&#124; FEAT_SME2p1 |
| 110   | FMAXQV                | FEAT_SVE2p1 &#124;&#124; FEAT_SME2p1 |
| 111   | FMINQV                | FEAT_SVE2p1 &#124;&#124; FEAT_SME2p1 |

## SVE floating-point multiply-add (indexed)

The encodings in this section are decoded from SVE encodings.

<!-- image -->

| size   |   o2 | op   | Instruction Details              | Feature                        |
|--------|------|------|----------------------------------|--------------------------------|
| 0x     |    0 | 0    | FMLA(indexed) -Half-precision    | FEAT_SVE &#124;&#124; FEAT_SME |
| 0x     |    0 | 1    | FMLS (indexed) -Half-precision   | FEAT_SVE &#124;&#124; FEAT_SME |
| 0x     |    1 | 0    | BFMLA(indexed)                   | FEAT_SVE_B16B16                |
| 0x     |    1 | 1    | BFMLS (indexed)                  | FEAT_SVE_B16B16                |
| 1x     |    1 | x    | UNALLOCATED                      | -                              |
| 10     |    0 | 0    | FMLA(indexed) -Single-precision  | FEAT_SVE &#124;&#124; FEAT_SME |
| 10     |    0 | 1    | FMLS (indexed) -Single-precision | FEAT_SVE &#124;&#124; FEAT_SME |
| 11     |    0 | 0    | FMLA(indexed) -Double-precision  | FEAT_SVE &#124;&#124; FEAT_SME |
| 11     |    0 | 1    | FMLS (indexed) -Double-precision | FEAT_SVE &#124;&#124; FEAT_SME |

## SVE floating-point complex multiply-add (indexed)

The encodings in this section are decoded from SVE encodings.

<!-- image -->

| size   | Instruction Details            | Feature           |
|--------|--------------------------------|-------------------|
| 0x     | UNALLOCATED                    | -                 |
| 10     | FCMLA(indexed) -Half-precision | FEAT_SVE FEAT_SME |

||

## SVE FP clamp

The encodings in this section are decoded from SVE encodings.

<!-- image -->

| size   | Instruction Details   | Feature                            |
|--------|-----------------------|------------------------------------|
| 00     | BFCLAMP               | FEAT_SVE_B16B16                    |
| != 00  | FCLAMP                | FEAT_SME2 &#124;&#124; FEAT_SVE2p1 |

## SVE floating-point multiply (indexed)

The encodings in this section are decoded from SVE encodings.

<!-- image -->

| size   |   o2 | Instruction Details             | Feature                        |
|--------|------|---------------------------------|--------------------------------|
| 0x     |    0 | FMUL(indexed) -Half-precision   | FEAT_SVE &#124;&#124; FEAT_SME |
| 0x     |    1 | BFMUL(indexed)                  | FEAT_SVE_B16B16                |
| 1x     |    1 | UNALLOCATED                     | -                              |
| 10     |    0 | FMUL(indexed) -Single-precision | FEAT_SVE &#124;&#124; FEAT_SME |
| 11     |    0 | FMUL(indexed) -Double-precision | FEAT_SVE &#124;&#124; FEAT_SME |

## SVE2 FP8 multiply-add long long (indexed)

The encodings in this section are decoded from SVE encodings.

<!-- image -->

|   size | Instruction Details              | Feature                        |
|--------|----------------------------------|--------------------------------|
|     11 | FCMLA(indexed) -Single-precision | FEAT_SVE &#124;&#124; FEAT_SME |

|   TT | Instruction Details   | Feature                                                 |
|------|-----------------------|---------------------------------------------------------|
|   00 | FMLALLBB(indexed)     | FEAT_SSVE_FP8FMA &#124;&#124; (FEAT_SVE2 &&FEAT_FP8FMA) |
|   01 | FMLALLBT(indexed)     | FEAT_SSVE_FP8FMA &#124;&#124; (FEAT_SVE2 &&FEAT_FP8FMA) |
|   10 | FMLALLTB (indexed)    | FEAT_SSVE_FP8FMA &#124;&#124; (FEAT_SVE2 &&FEAT_FP8FMA) |
|   11 | FMLALLTT (indexed)    | FEAT_SSVE_FP8FMA &#124;&#124; (FEAT_SVE2 &&FEAT_FP8FMA) |

## SVE floating-point matrix multiply accumulate

The encodings in this section are decoded from SVE encodings.

<!-- image -->

|   opc | Instruction Details                   | Feature              |
|-------|---------------------------------------|----------------------|
|    00 | FMMLA(widening, FP16 to FP32)         | FEAT_SVE_F16F32MM    |
|    01 | BFMMLA(widening)                      | FEAT_SVE &&FEAT_BF16 |
|    10 | FMMLA (non-widening) - 32-bit element | FEAT_F32MM           |
|    11 | FMMLA (non-widening) - 64-bit element | FEAT_F64MM           |

## SVE floating-point recursive reduction

The encodings in this section are decoded from SVE encodings.

<!-- image -->

|   31 | 29 28   | 24 23 22   |        | 21 19 18   | 16 15   | 13 12 10   | 9   | 5 4   | 0   |
|------|---------|------------|--------|------------|---------|------------|-----|-------|-----|
|    0 | 1 1     | 0 0 1 0    | 1 size | 0 0 0      | opc     | 0 0 1      | Pg  | Zn    | Vd  |

| opc   | Instruction Details   | Feature                        |
|-------|-----------------------|--------------------------------|
| 000   | FADDV                 | FEAT_SVE &#124;&#124; FEAT_SME |
| 001   | UNALLOCATED           | -                              |
| 01x   | UNALLOCATED           | -                              |
| 100   | FMAXNMV               | FEAT_SVE &#124;&#124; FEAT_SME |
| 101   | FMINNMV               | FEAT_SVE &#124;&#124; FEAT_SME |

|   opc | Instruction Details   | Feature                        |
|-------|-----------------------|--------------------------------|
|   110 | FMAXV                 | FEAT_SVE &#124;&#124; FEAT_SME |
|   111 | FMINV                 | FEAT_SVE &#124;&#124; FEAT_SME |

## SVE floating-point arithmetic (unpredicated)

The encodings in this section are decoded from SVE encodings.

<!-- image -->

|   31 | 29 28   | 24 23 22 21 20   |      | 16 15 13 12   | 10    | 9   | 5 4   | 0   |
|------|---------|------------------|------|---------------|-------|-----|-------|-----|
|    0 | 1 1     | 0 0 1 0 1        | size | 0 Zm          | 0 0 0 | opc | Zn    | Zd  |

| size   | opc   | Instruction Details          | Feature                        |
|--------|-------|------------------------------|--------------------------------|
| xx     | 011   | FTSMUL                       | FEAT_SVE                       |
| xx     | 10x   | UNALLOCATED                  | -                              |
| xx     | 110   | FRECPS                       | FEAT_SVE &#124;&#124; FEAT_SME |
| xx     | 111   | FRSQRTS                      | FEAT_SVE &#124;&#124; FEAT_SME |
| 00     | 000   | BFADD(unpredicated)          | FEAT_SVE_B16B16                |
| 00     | 001   | BFSUB (unpredicated)         | FEAT_SVE_B16B16                |
| 00     | 010   | BFMUL(vectors, unpredicated) | FEAT_SVE_B16B16                |
| != 00  | 000   | FADD(vectors, unpredicated)  | FEAT_SVE &#124;&#124; FEAT_SME |
| != 00  | 001   | FSUB (vectors, unpredicated) | FEAT_SVE &#124;&#124; FEAT_SME |
| != 00  | 010   | FMUL(vectors, unpredicated)  | FEAT_SVE &#124;&#124; FEAT_SME |

## SVE floating-point compare vectors

The encodings in this section are decoded from SVE encodings.

<!-- image -->

|   op |   o2 |   o3 | Instruction Details                          | Feature                        |
|------|------|------|----------------------------------------------|--------------------------------|
|    0 |    0 |    0 | FCM < cc > (vectors) - Greater than or equal | FEAT_SVE &#124;&#124; FEAT_SME |
|    0 |    0 |    1 | FCM < cc > (vectors) -Greater than           | FEAT_SVE &#124;&#124; FEAT_SME |
|    0 |    1 |    0 | FCM < cc > (vectors) -Equal                  | FEAT_SVE &#124;&#124; FEAT_SME |

|   op |   o2 |   o3 | Instruction Details               | Feature                        |
|------|------|------|-----------------------------------|--------------------------------|
|    0 |    1 |    1 | FCM < cc > (vectors) -Notequal    | FEAT_SVE &#124;&#124; FEAT_SME |
|    1 |    0 |    0 | FCM < cc > (vectors) -Unordered   | FEAT_SVE &#124;&#124; FEAT_SME |
|    1 |    0 |    1 | FAC < cc > -Greater than or equal | FEAT_SVE &#124;&#124; FEAT_SME |
|    1 |    1 |    0 | UNALLOCATED                       | -                              |
|    1 |    1 |    1 | FAC < cc > -Greater than          | FEAT_SVE &#124;&#124; FEAT_SME |

## Data Processing -- Immediate

Data Processing - Immediate

The encodings in this section are decoded from A64 instruction set encoding.

<!-- image -->

| 31 30   | 29 28   | 26 25   | 22   |
|---------|---------|---------|------|
| op0     | 1 0 0   | op1     |      |

| op0   | op1   | Instruction details                  |
|-------|-------|--------------------------------------|
| 11    | 111x  | Data-processing (1 source immediate) |
| xx    | 00xx  | PC-rel. addressing                   |
| xx    | 010x  | Add/subtract (immediate)             |
| xx    | 0110  | Add/subtract (immediate, with tags)  |
| xx    | 0111  | Min/max (immediate)                  |
| xx    | 100x  | Logical (immediate)                  |
| xx    | 101x  | Move wide (immediate)                |
| xx    | 110x  | Bitfield                             |
| != 11 | 111x  | Extract                              |

## Data-processing (1 source immediate)

The encodings in this section are decoded from Data Processing - Immediate.

<!-- image -->

| 31   | 30 29 28 21 20            | 23 22 5 4   |
|------|---------------------------|-------------|
| sf   | 1 1 1 0 0 1 1 1 opc imm16 | Rd          |

|   sf | opc   | Rd    | Instruction Details   | Feature   |
|------|-------|-------|-----------------------|-----------|
|    0 | xx    | xxxxx | UNALLOCATED           | -         |

## PC-rel. addressing

The encodings in this section are decoded from Data Processing - Immediate.

<!-- image -->

| 31   | 30 29 28    | 0   |
|------|-------------|-----|
| op   | immlo 1 0 0 | Rd  |

|   op | Instruction Details   |
|------|-----------------------|
|    0 | ADR                   |
|    1 | ADRP                  |

|   sf | opc   | Rd       | Instruction Details   | Feature       |
|------|-------|----------|-----------------------|---------------|
|    1 | 0x    | != 11111 | UNALLOCATED           | -             |
|    1 | 00    | 11111    | AUTIASPPC             | FEAT_PAuth_LR |
|    1 | 01    | 11111    | AUTIBSPPC             | FEAT_PAuth_LR |
|    1 | 1x    | xxxxx    | UNALLOCATED           | -             |

## Add/subtract (immediate)

The encodings in this section are decoded from Data Processing - Immediate.

<!-- image -->

| 31   | 30   | 29   | 28          | 23 22   | 21   | 5 4   |    |
|------|------|------|-------------|---------|------|-------|----|
| sf   | op   | S    | 1 0 0 0 1 0 | sh      |      | Rn    | Rd |

|   sf |   op |   S | Instruction Details      |
|------|------|-----|--------------------------|
|    0 |    0 |   0 | ADD(immediate) -32-bit   |
|    0 |    0 |   1 | ADDS(immediate) -32-bit  |
|    0 |    1 |   0 | SUB (immediate) -32-bit  |
|    0 |    1 |   1 | SUBS (immediate) -32-bit |
|    1 |    0 |   0 | ADD(immediate) -64-bit   |
|    1 |    0 |   1 | ADDS(immediate) -64-bit  |
|    1 |    1 |   0 | SUB (immediate) -64-bit  |
|    1 |    1 |   1 | SUBS (immediate) -64-bit |

## Add/subtract (immediate, with tags)

The encodings in this section are decoded from Data Processing - Immediate.

<!-- image -->

| 31   | 30   | 29 28   | 26 25   |   22 |      | 16 15 14 13   | 10   | 5   | 0   |
|------|------|---------|---------|------|------|---------------|------|-----|-----|
| sf   | op   | S 1 0 0 | 0 1 1   |    0 | imm6 | op3           | imm4 | Rn  | Rd  |

|   sf | op   | S   | Instruction Details   | Feature   |
|------|------|-----|-----------------------|-----------|
|    0 | x    | x   | UNALLOCATED           | -         |
|    1 | x    | 1   | UNALLOCATED           | -         |
|    1 | 0    | 0   | ADDG                  | FEAT_MTE  |
|    1 | 1    | 0   | SUBG                  | FEAT_MTE  |

## Min/max (immediate)

The encodings in this section are decoded from Data Processing - Immediate.

<!-- image -->

| 31   | 30 29 28   | 26 25   | 22 21     | 18 17   | 10 9   |    |
|------|------------|---------|-----------|---------|--------|----|
| sf   | op S       | 1 0     | 0 0 1 1 1 | imm8    | Rn     | Rd |

| sf   |   op | S   | opc   | Instruction Details      | Feature   |
|------|------|-----|-------|--------------------------|-----------|
| x    |    0 | 0   | 01xx  | UNALLOCATED              | -         |
| x    |    0 | 0   | 1xxx  | UNALLOCATED              | -         |
| x    |    0 | 1   | xxxx  | UNALLOCATED              | -         |
| x    |    1 | x   | xxxx  | UNALLOCATED              | -         |
| 0    |    0 | 0   | 0000  | SMAX(immediate) -32-bit  | FEAT_CSSC |
| 0    |    0 | 0   | 0001  | UMAX(immediate) -32-bit  | FEAT_CSSC |
| 0    |    0 | 0   | 0010  | SMIN (immediate) -32-bit | FEAT_CSSC |
| 0    |    0 | 0   | 0011  | UMIN(immediate) -32-bit  | FEAT_CSSC |
| 1    |    0 | 0   | 0000  | SMAX(immediate) -64-bit  | FEAT_CSSC |
| 1    |    0 | 0   | 0001  | UMAX(immediate) -64-bit  | FEAT_CSSC |
| 1    |    0 | 0   | 0010  | SMIN (immediate) -64-bit | FEAT_CSSC |
| 1    |    0 | 0   | 0011  | UMIN(immediate) -64-bit  | FEAT_CSSC |

## Logical (immediate)

The encodings in this section are decoded from Data Processing - Immediate.

<!-- image -->

| 31   | 30 29   | 23 22 21   | 16   | 10   | 5   | 0   |
|------|---------|------------|------|------|-----|-----|
| sf   | opc     | 1 0 0 N    | immr | imms | Rn  | Rd  |

|   sf | opc   | N   | Instruction Details     |
|------|-------|-----|-------------------------|
|    0 | xx    | 1   | UNALLOCATED             |
|    0 | 00    | 0   | AND(immediate) -32-bit  |
|    0 | 01    | 0   | ORR(immediate) -32-bit  |
|    0 | 10    | 0   | EOR(immediate) -32-bit  |
|    0 | 11    | 0   | ANDS(immediate) -32-bit |
|    1 | 00    | x   | AND(immediate) -64-bit  |
|    1 | 01    | x   | ORR(immediate) -64-bit  |
|    1 | 10    | x   | EOR(immediate) -64-bit  |
|    1 | 11    | x   | ANDS(immediate) -64-bit |

## Move wide (immediate)

The encodings in this section are decoded from Data Processing - Immediate.

<!-- image -->

| 31   | 30   | 29 28       | 23 22   | 21 20 5 4   |
|------|------|-------------|---------|-------------|
| sf   | opc  | 1 0 0 1 0 1 | hw      | imm16 Rd    |

| sf   | opc   | hw   | Instruction Details   |
|------|-------|------|-----------------------|
| x    | 01    | 0x   | UNALLOCATED           |
| 0    | xx    | 1x   | UNALLOCATED           |
| 0    | 00    | 0x   | MOVN-32-bit           |
| 0    | 10    | 0x   | MOVZ-32-bit           |
| 0    | 11    | 0x   | MOVK-32-bit           |
| 1    | 00    | xx   | MOVN-64-bit           |
| 1    | 01    | 1x   | UNALLOCATED           |
| 1    | 10    | xx   | MOVZ-64-bit           |
| 1    | 11    | xx   | MOVK-64-bit           |

## Bitfield

The encodings in this section are decoded from Data Processing - Immediate.

<!-- image -->

| 31   | 30   | 29 28   | 23 22   |      | 16 15   | 10 9   | 4   |
|------|------|---------|---------|------|---------|--------|-----|
| sf   | opc  | 1 0     | 1 1 0 N | immr | imms    | Rn     | Rd  |

|   sf | opc   |   N | Instruction Details   |
|------|-------|-----|-----------------------|
|    0 | xx    |   1 | UNALLOCATED           |
|    0 | 00    |   0 | SBFM-32-bit           |
|    0 | 01    |   0 | BFM-32-bit            |
|    0 | 10    |   0 | UBFM-32-bit           |
|    0 | 11    |   0 | UNALLOCATED           |
|    1 | xx    |   0 | UNALLOCATED           |
|    1 | 00    |   1 | SBFM-64-bit           |
|    1 | 01    |   1 | BFM-64-bit            |
|    1 | 10    |   1 | UBFM-64-bit           |
|    1 | 11    |   1 | UNALLOCATED           |

## Extract

The encodings in this section are decoded from Data Processing - Immediate.

<!-- image -->

The following constraints also apply to this encoding: op21 != '11'

| sf   |   op21 | N   | o0   | imms   | Instruction Details   |
|------|--------|-----|------|--------|-----------------------|
| x    |     00 | x   | 1    | xxxxxx | UNALLOCATED           |
| x    |     01 | x   | x    | xxxxxx | UNALLOCATED           |
| x    |     10 | x   | x    | xxxxxx | UNALLOCATED           |
| 0    |     00 | 0   | 0    | 0xxxxx | EXTR -32-bit          |
| 0    |     00 | 0   | 0    | 1xxxxx | UNALLOCATED           |
| 0    |     00 | 1   | 0    | xxxxxx | UNALLOCATED           |
| 1    |     00 | 0   | 0    | xxxxxx | UNALLOCATED           |
| 1    |     00 | 1   | 0    | xxxxxx | EXTR -64-bit          |

## Branches, Exception Generating and System instructions

Branches, Exception Generating and System instructions

The encodings in this section are decoded from A64 instruction set encoding.

<!-- image -->

| 31   | 29 28 26   |     | 5 4   |
|------|------------|-----|-------|
| op0  | 1 0 1      | op1 | op2   |

| op0   | op1            | op2      | Instruction details                             |
|-------|----------------|----------|-------------------------------------------------|
| 010   | 00xxxxxxxxxxxx | xxxxx    | Conditional branch (immediate)                  |
| 010   | 01xxxxxxxxxxxx | xxxxx    | Miscellaneous branch (immediate)                |
| 011   | 00xxxxxxxx1xxx | xxxxx    | Compare bytes/halfwords in registers and branch |
| 01x   | 1xxxxxxxxxxxxx | xxxxx    | UNALLOCATED                                     |
| 110   | 00xxxxxxxxxxxx | xxxxx    | Exception generation                            |
| 110   | 010000000x00xx | xxxxx    | UNALLOCATED                                     |
| 110   | 010000001000xx | xxxxx    | UNALLOCATED                                     |
| 110   | 01000000110000 | xxxxx    | UNALLOCATED                                     |
| 110   | 01000000110001 | xxxxx    | System instructions with register argument      |
| 110   | 01000000110010 | 11111    | Hints                                           |
| 110   | 01000000110010 | != 11111 | UNALLOCATED                                     |
| 110   | 01000000110011 | xxxxx    | Barriers                                        |
| 110   | 01000001xx00xx | xxxxx    | UNALLOCATED                                     |
| 110   | 0100000xxx0100 | xxxxx    | PSTATE                                          |
| 110   | 0100000xxx0101 | xxxxx    | UNALLOCATED                                     |
| 110   | 0100000xxx011x | xxxxx    | UNALLOCATED                                     |
| 110   | 0100000xxx1xxx | xxxxx    | UNALLOCATED                                     |
| 110   | 0100100xxxxxxx | xxxxx    | UNALLOCATED                                     |
| 110   | 0100x01xxxxxxx | xxxxx    | System instructions                             |
| 110   | 0100x1xxxxxxxx | xxxxx    | System register move                            |
| 110   | 0101x00xxxxxxx | xxxxx    | UNALLOCATED                                     |
| 110   | 0101x01xxxxxxx | xxxxx    | System pair instructions                        |
| 110   | 0101x1xxxxxxxx | xxxxx    | System register pair move                       |
| 110   | 011xxxxxxxxxxx | xxxxx    | UNALLOCATED                                     |
| 110   | 1xxxxxxxxxxxxx | xxxxx    | Unconditional branch (register)                 |
| 111   | 00xxxxxxxx1xxx | xxxxx    | UNALLOCATED                                     |
| 111   | 1xxxxxxxxxxxxx | xxxxx    | UNALLOCATED                                     |
| x00   | xxxxxxxxxxxxxx | xxxxx    | Unconditional branch (immediate)                |
| x01   | 0xxxxxxxxxxxxx | xxxxx    | Compare and branch (immediate)                  |

| op0   | op1            | op2   | Instruction details                        |
|-------|----------------|-------|--------------------------------------------|
| x01   | 1xxxxxxxxxxxxx | xxxxx | Test and branch (immediate)                |
| x11   | 00xxxxxxxx00xx | xxxxx | Compare registers and branch               |
| x11   | 00xxxxxxxx01xx | xxxxx | UNALLOCATED                                |
| x11   | 01xxxxxxxxx0xx | xxxxx | Compare register with immediate and branch |
| x11   | 01xxxxxxxxx1xx | xxxxx | UNALLOCATED                                |

## Conditional branch (immediate)

The encodings in this section are decoded from Branches, Exception Generating and System instructions.

<!-- image -->

|   31 | 29 28   | 24 23     | 5 4   |      |
|------|---------|-----------|-------|------|
|    0 | 1 0     | 1 0 1 0 0 | o0    | cond |

|   o0 | Instruction Details   | Feature   |
|------|-----------------------|-----------|
|    0 | B.cond                | -         |
|    1 | BC.cond               | FEAT_HBC  |

## Miscellaneous branch (immediate)

The encodings in this section are decoded from Branches, Exception Generating and System instructions.

<!-- image -->

| 31   |   29 28 | 24 23     | 21 20   | 4   |
|------|---------|-----------|---------|-----|
| 0 1  |       0 | 1 0 1 0 1 | imm16   | op2 |

| opc   | op2      | Instruction Details   |           | Feature       |
|-------|----------|-----------------------|-----------|---------------|
| 00x   | != 11111 | UNALLOCATED           |           | -             |
| 000   | 11111    | RETAASPPC, RETAASPPC  | RETABSPPC | FEAT_PAuth_LR |
| 001   | 11111    | RETAASPPC, RETABSPPC  | RETABSPPC | FEAT_PAuth_LR |
| 01x   | xxxxx    | UNALLOCATED           |           | -             |
| 1xx   | xxxxx    | UNALLOCATED           |           | -             |

## Compare bytes/halfwords in registers and branch

The encodings in this section are decoded from Branches, Exception Generating and System instructions.

<!-- image -->

|   31 | 29 28   | 24 23   | 21 20   | 16 15 14 13   |      |    |
|------|---------|---------|---------|---------------|------|----|
|    0 | 1 1 1   | 0 1 0 0 | cc      | Rm 1 H        | imm9 | Rt |

| cc   | H   | Instruction Details               | Feature    |
|------|-----|-----------------------------------|------------|
| 000  | 0   | CBB < cc > -Greater than          | FEAT_CMPBR |
| 000  | 1   | CBH < cc > -Greater than          | FEAT_CMPBR |
| 001  | 0   | CBB < cc > -Greater than or equal | FEAT_CMPBR |
| 001  | 1   | CBH < cc > -Greater than or equal | FEAT_CMPBR |
| 010  | 0   | CBB < cc > -Higher                | FEAT_CMPBR |
| 010  | 1   | CBH < cc > -Higher                | FEAT_CMPBR |
| 011  | 0   | CBB < cc > -Higher or same        | FEAT_CMPBR |
| 011  | 1   | CBH < cc > -Higher or same        | FEAT_CMPBR |
| 10x  | x   | UNALLOCATED                       | -          |
| 110  | 0   | CBB < cc > -Equal                 | FEAT_CMPBR |
| 110  | 1   | CBH < cc > -Equal                 | FEAT_CMPBR |
| 111  | 0   | CBB < cc > -Notequal              | FEAT_CMPBR |
| 111  | 1   | CBH < cc > -Notequal              | FEAT_CMPBR |

## Exception generation

The encodings in this section are decoded from Branches, Exception Generating and System instructions.

<!-- image -->

|   31 | 29 28   | 24 23     | 21 20   |       | 2   | 1   |
|------|---------|-----------|---------|-------|-----|-----|
|    1 | 1 0     | 1 0 1 0 0 | opc     | imm16 | op2 | LL  |

| opc   | op2    | LL   | Instruction Details   |
|-------|--------|------|-----------------------|
| xxx   | != 000 | xx   | UNALLOCATED           |
| x11   | 000    | xx   | UNALLOCATED           |
| 000   | 000    | 00   | UNALLOCATED           |
| 000   | 000    | 01   | SVC                   |
| 000   | 000    | 10   | HVC                   |
| 000   | 000    | 11   | SMC                   |

## Hints

The encodings in this section are decoded from Branches, Exception Generating and System instructions.

<!-- image -->

|   31 | 29 28   | 26 25 12 11                       | 8 7   | 5 4   | 0         |
|------|---------|-----------------------------------|-------|-------|-----------|
|    1 | 1 0     | 1 0 1 0 1 0 0 0 0 0 0 1 1 0 0 1 0 | CRm   | op2   | 1 1 1 1 1 |

| CRm   | op2   | Instruction Details   | Feature   |
|-------|-------|-----------------------|-----------|
| xxxx  | xxx   | HINT                  | -         |
| 0000  | 000   | NOP                   | -         |

| opc   |   op2 | LL    | Instruction Details   |
|-------|-------|-------|-----------------------|
| 001   |   000 | 00    | BRK                   |
| 001   |   000 | != 00 | UNALLOCATED           |
| 010   |   000 | 00    | HLT                   |
| 010   |   000 | != 00 | UNALLOCATED           |
| 1x0   |   000 | xx    | UNALLOCATED           |
| 101   |   000 | 00    | UNALLOCATED           |
| 101   |   000 | 01    | DCPS1                 |
| 101   |   000 | 10    | DCPS2                 |
| 101   |   000 | 11    | DCPS3                 |

## System instructions with register argument

The encodings in this section are decoded from Branches, Exception Generating and System instructions.

<!-- image -->

| 31   | 29 28   | 26 25 12 11                   | 8 7   | 5   | 0   |
|------|---------|-------------------------------|-------|-----|-----|
| 1 1  | 0 1     | 1 0 1 0 0 0 0 0 0 1 1 0 0 0 1 | CRm   | op2 | Rt  |

| CRm     | op2   | Instruction Details   | Feature   |
|---------|-------|-----------------------|-----------|
| 0000    | 000   | WFET                  | FEAT_WFxT |
| 0000    | 001   | WFIT                  | FEAT_WFxT |
| 0000    | 01x   | UNALLOCATED           | -         |
| 0000    | 1xx   | UNALLOCATED           | -         |
| != 0000 | xxx   | UNALLOCATED           | -         |

|   CRm | op2   | Instruction Details                                   | Feature       |
|-------|-------|-------------------------------------------------------|---------------|
|  0000 | 001   | YIELD                                                 | -             |
|  0000 | 010   | WFE                                                   | -             |
|  0000 | 011   | WFI                                                   | -             |
|  0000 | 100   | SEV                                                   | -             |
|  0000 | 101   | SEVL                                                  | -             |
|  0000 | 110   | DGH                                                   | FEAT_DGH      |
|  0000 | 111   | XPACD, XPACI, XPACLRI                                 | FEAT_PAuth    |
|  0001 | 000   | PACIA, PACIA1716, PACIASP, PACIAZ, PACIZA -PACIA1716  | FEAT_PAuth    |
|  0001 | 010   | PACIB, PACIB1716, PACIBSP, PACIBZ, PACIZB -PACIB1716  | FEAT_PAuth    |
|  0001 | 100   | AUTIA, AUTIA1716, AUTIASP, AUTIAZ, AUTIZA - AUTIA1716 | FEAT_PAuth    |
|  0001 | 110   | AUTIB, AUTIB1716, AUTIBSP, AUTIBZ, AUTIZB - AUTIB1716 | FEAT_PAuth    |
|  0010 | 000   | ESB                                                   | FEAT_RAS      |
|  0010 | 001   | PSB                                                   | FEAT_SPE      |
|  0010 | 010   | TSB                                                   | FEAT_TRF      |
|  0010 | 011   | GCSB                                                  | FEAT_GCS      |
|  0010 | 100   | CSDB                                                  | -             |
|  0010 | 110   | CLRBHB                                                | FEAT_CLRBHB   |
|  0011 | 000   | PACIA, PACIA1716, PACIASP, PACIAZ, PACIZA-PACIAZ      | FEAT_PAuth    |
|  0011 | 001   | PACIA, PACIA1716, PACIASP, PACIAZ, PACIZA -PACIASP    | FEAT_PAuth    |
|  0011 | 010   | PACIB, PACIB1716, PACIBSP, PACIBZ, PACIZB-PACIBZ      | FEAT_PAuth    |
|  0011 | 011   | PACIB, PACIB1716, PACIBSP, PACIBZ, PACIZB -PACIBSP    | FEAT_PAuth    |
|  0011 | 100   | AUTIA, AUTIA1716, AUTIASP, AUTIAZ,AUTIZA-AUTIAZ       | FEAT_PAuth    |
|  0011 | 101   | AUTIA, AUTIA1716, AUTIASP, AUTIAZ,AUTIZA-AUTIASP      | FEAT_PAuth    |
|  0011 | 110   | AUTIB, AUTIB1716, AUTIBSP, AUTIBZ,AUTIZB-AUTIBZ       | FEAT_PAuth    |
|  0011 | 111   | AUTIB, AUTIB1716, AUTIBSP, AUTIBZ,AUTIZB-AUTIBSP      | FEAT_PAuth    |
|  0100 | xx0   | BTI                                                   | FEAT_BTI      |
|  0100 | 111   | PACM                                                  | FEAT_PAuth_LR |
|  0101 | 000   | CHKFEAT                                               | FEAT_CHK      |
|  0110 | 00x   | STSHH                                                 | FEAT_PCDPHINT |

## Barriers

The encodings in this section are decoded from Branches, Exception Generating and System instructions.

<!-- image -->

|   31 | 29 28   | 26 25 12 11                     | 8 7   | 5 4   | 0   |
|------|---------|---------------------------------|-------|-------|-----|
|    1 | 1 0 1   | 0 1 0 1 0 0 0 0 0 0 1 1 0 0 1 1 | CRm   | op2   | Rt  |

| CRm   | op2   | Rt       | Instruction Details   | Feature   |
|-------|-------|----------|-----------------------|-----------|
| xxxx  | xxx   | != 11111 | UNALLOCATED           | -         |
| xxxx  | 000   | 11111    | UNALLOCATED           | -         |
| xxxx  | 010   | 11111    | CLREX                 | -         |
| xxxx  | 100   | 11111    | DSB -Memorybarrier    | -         |
| xxxx  | 101   | 11111    | DMB                   | -         |
| xxxx  | 110   | 11111    | ISB                   | -         |
| xxxx  | 111   | 11111    | SB                    | FEAT_SB   |
| xx0x  | 0x1   | 11111    | UNALLOCATED           | -         |
| xx10  | 001   | 11111    | DSB -MemorynXSbarrier | FEAT_XS   |
| xx10  | 011   | 11111    | UNALLOCATED           | -         |
| xx11  | 0x1   | 11111    | UNALLOCATED           | -         |

## PSTATE

The encodings in this section are decoded from Branches, Exception Generating and System instructions.

<!-- image -->

| 31   |   29 28 | 19 18               | 16 15   | 12 11   | 8 7   | 5   | 0   |
|------|---------|---------------------|---------|---------|-------|-----|-----|
| 1 1  |       0 | 1 0 1 0 1 0 0 0 0 0 | op1     | 0 1 0 0 | CRm   | op2 | Rt  |

| op1:op2   | Rt    | Instruction Details   | Feature     |
|-----------|-------|-----------------------|-------------|
| xxxxxx    | 0xxxx | UNALLOCATED           | -           |
| xxxxxx    | 10xxx | UNALLOCATED           | -           |
| xxxxxx    | 110xx | UNALLOCATED           | -           |
| xxxxxx    | 1110x | UNALLOCATED           | -           |
| xxxxxx    | 11110 | UNALLOCATED           | -           |
| 000000    | 11111 | CFINV                 | FEAT_FlagM  |
| 000001    | 11111 | XAFLAG                | FEAT_FlagM2 |
| 000010    | 11111 | AXFLAG                | FEAT_FlagM2 |

## System instructions

The encodings in this section are decoded from Branches, Exception Generating and System instructions.

<!-- image -->

|   31 | 29 28   | 22 21 20 19 18   | 16 15   | 12 11   | 8 7   | 5 4   | 0   |
|------|---------|------------------|---------|---------|-------|-------|-----|
|    1 | 1 0     | 1 0 1 0 1 0 0    | L 0 1   | op1 CRn | CRm   | op2   | Rt  |

- L Instruction Details

|   0 | SYS   |
|-----|-------|
|   1 | SYSL  |

## System register move

The encodings in this section are decoded from Branches, Exception Generating and System instructions.

<!-- image -->

| 31   | 29 28                          | 22 21 20 19 18 16 15 12 11 8 7 5 4   |
|------|--------------------------------|--------------------------------------|
| 1 1  | 0 1 0 1 0 1 0 0 L 1 o0 op1 CRn | CRm op2 Rt                           |

## L Instruction Details

|   0 | MSR(register)   |
|-----|-----------------|
|   1 | MRS             |

## System pair instructions

The encodings in this section are decoded from Branches, Exception Generating and System instructions.

<!-- image -->

| 31   | 29 28   | 22 21 20 19   | 18 16   | 12 11   | 8 7   | 5   |    |
|------|---------|---------------|---------|---------|-------|-----|----|
| 1 1  | 0 1     | 0 1 0 1 L     | 0 1 op1 | CRn     | CRm   | op2 | Rt |

| op1:op2   |    Rt | Instruction Details   | Feature   |
|-----------|-------|-----------------------|-----------|
| != 00000x | 11111 | MSR(immediate)        | -         |

## System register pair move

The encodings in this section are decoded from Branches, Exception Generating and System instructions.

<!-- image -->

|   31 | 29 28   | 22 21 20 19 18   | 16 15   | 12 11   | 8 7   | 5 4   | 0   |
|------|---------|------------------|---------|---------|-------|-------|-----|
|    1 | 1 0 1   | 0 1 0 1          | L 1 o0  | op1 CRn | CRm   | op2   | Rt  |

|   L | Instruction Details   | Feature        |
|-----|-----------------------|----------------|
|   0 | MSRR                  | FEAT_SYSREG128 |
|   1 | MRRS                  | FEAT_SYSREG128 |

## Unconditional branch (register)

The encodings in this section are decoded from Branches, Exception Generating and System instructions.

<!-- image -->

|   31 | 29 28   |   25 24 | 21 20   | 16 15   | 10 9   | 5 4   |
|------|---------|---------|---------|---------|--------|-------|
|    1 | 1 0 1   |       1 | op2     | op3     | Rn     | op4   |

| opc   | op2      | op3    | Rn    | op4      | Instruction Details                            | Feature    |
|-------|----------|--------|-------|----------|------------------------------------------------|------------|
| xxxx  | 11111    | 0001xx | xxxxx | xxxxx    | UNALLOCATED                                    | -          |
| xxxx  | 11111    | 001xxx | xxxxx | xxxxx    | UNALLOCATED                                    | -          |
| xxxx  | 11111    | 01xxxx | xxxxx | xxxxx    | UNALLOCATED                                    | -          |
| xxxx  | 11111    | 1xxxxx | xxxxx | xxxxx    | UNALLOCATED                                    | -          |
| xxxx  | != 11111 | xxxxxx | xxxxx | xxxxx    | UNALLOCATED                                    | -          |
| 00x0  | 11111    | 000000 | xxxxx | != 00000 | UNALLOCATED                                    | -          |
| 00x0  | 11111    | 000001 | xxxxx | xxxxx    | UNALLOCATED                                    | -          |
| 000x  | 11111    | 00001x | xxxxx | != 11111 | UNALLOCATED                                    | -          |
| 0000  | 11111    | 000000 | xxxxx | 00000    | BR                                             | -          |
| 0000  | 11111    | 000010 | xxxxx | 11111    | BRAA, BRAAZ, BRAB, BRABZ -Key A, zero modifier | FEAT_PAuth |

|   L | Instruction Details   | Feature          |
|-----|-----------------------|------------------|
|   0 | SYSP                  | FEAT_SYSINSTR128 |
|   1 | UNALLOCATED           | -                |

| opc   |   op2 | op3    | Rn       | op4      | Instruction Details                                  | Feature       |
|-------|-------|--------|----------|----------|------------------------------------------------------|---------------|
| 0000  | 11111 | 000011 | xxxxx    | 11111    | BRAA, BRAAZ, BRAB, BRABZ -Key B, zero modifier       | FEAT_PAuth    |
| 0001  | 11111 | 000000 | xxxxx    | 00000    | BLR                                                  | -             |
| 0001  | 11111 | 000000 | xxxxx    | != 00000 | UNALLOCATED                                          | -             |
| 0001  | 11111 | 000001 | xxxxx    | xxxxx    | UNALLOCATED                                          | -             |
| 0001  | 11111 | 000010 | xxxxx    | 11111    | BLRAA, BLRAAZ, BLRAB, BLRABZ -KeyA,zero modifier     | FEAT_PAuth    |
| 0001  | 11111 | 000011 | xxxxx    | 11111    | BLRAA, BLRAAZ, BLRAB, BLRABZ -KeyB,zero modifier     | FEAT_PAuth    |
| 0010  | 11111 | 000000 | xxxxx    | 00000    | RET                                                  | -             |
| 0010  | 11111 | 00001x | != 11111 | xxxxx    | UNALLOCATED                                          | -             |
| 0010  | 11111 | 000010 | 11111    | 11111    | RETAA,RETAB-RETAA                                    | FEAT_PAuth    |
| 0010  | 11111 | 000010 | 11111    | != 11111 | RETAASPPCR, RETABSPPCR - RETAASPPCR                  | FEAT_PAuth_LR |
| 0010  | 11111 | 000011 | 11111    | 11111    | RETAA,RETAB-RETAB                                    | FEAT_PAuth    |
| 0010  | 11111 | 000011 | 11111    | != 11111 | RETAASPPCR, RETABSPPCR - RETABSPPCR                  | FEAT_PAuth_LR |
| 0011  | 11111 | 0000xx | xxxxx    | xxxxx    | UNALLOCATED                                          | -             |
| 010x  | 11111 | 0000xx | != 11111 | xxxxx    | UNALLOCATED                                          | -             |
| 010x  | 11111 | 000000 | 11111    | != 00000 | UNALLOCATED                                          | -             |
| 010x  | 11111 | 000001 | 11111    | xxxxx    | UNALLOCATED                                          | -             |
| 010x  | 11111 | 00001x | 11111    | xxxx0    | UNALLOCATED                                          | -             |
| 0100  | 11111 | 000000 | 11111    | 00000    | ERET                                                 | -             |
| 0100  | 11111 | 00001x | 11111    | 0xxx1    | UNALLOCATED                                          | -             |
| 0100  | 11111 | 00001x | 11111    | 10xx1    | UNALLOCATED                                          | -             |
| 0100  | 11111 | 00001x | 11111    | 110x1    | UNALLOCATED                                          | -             |
| 0100  | 11111 | 00001x | 11111    | 11101    | UNALLOCATED                                          | -             |
| 0100  | 11111 | 000010 | 11111    | 11111    | ERETAA,ERETAB-ERETAA                                 | FEAT_PAuth    |
| 0100  | 11111 | 000011 | 11111    | 11111    | ERETAA,ERETAB-ERETAB                                 | FEAT_PAuth    |
| 0101  | 11111 | 000000 | 11111    | 00000    | DRPS                                                 | -             |
| 0101  | 11111 | 00001x | 11111    | xxxx1    | UNALLOCATED                                          | -             |
| 011x  | 11111 | 0000xx | xxxxx    | xxxxx    | UNALLOCATED                                          | -             |
| 100x  | 11111 | 00000x | xxxxx    | xxxxx    | UNALLOCATED                                          | -             |
| 1000  | 11111 | 000010 | xxxxx    | xxxxx    | BRAA, BRAAZ, BRAB, BRABZ -Key A, register modifier   | FEAT_PAuth    |
| 1000  | 11111 | 000011 | xxxxx    | xxxxx    | BRAA, BRAAZ, BRAB, BRABZ -Key B, register modifier   | FEAT_PAuth    |
| 1001  | 11111 | 000010 | xxxxx    | xxxxx    | BLRAA, BLRAAZ, BLRAB, BLRABZ -KeyA,register modifier | FEAT_PAuth    |
| 1001  | 11111 | 000011 | xxxxx    | xxxxx    | BLRAA, BLRAAZ, BLRAB, BLRABZ -KeyB,register modifier | FEAT_PAuth    |
| 101x  | 11111 | 0000xx | xxxxx    | xxxxx    | UNALLOCATED                                          | -             |
| 11xx  | 11111 | 0000xx | xxxxx    | xxxxx    | UNALLOCATED                                          | -             |

## Unconditional branch (immediate)

The encodings in this section are decoded from Branches, Exception Generating and System instructions.

<!-- image -->

| 31 30    | 26 25   |
|----------|---------|
| op 0 0 1 | 1 imm26 |

|   op | Instruction Details   |
|------|-----------------------|
|    0 | B                     |
|    1 | BL                    |

## Compare and branch (immediate)

The encodings in this section are decoded from Branches, Exception Generating and System instructions.

<!-- image -->

|   sf |   op | Instruction Details   |
|------|------|-----------------------|
|    0 |    0 | CBZ -32-bit           |
|    0 |    1 | CBNZ-32-bit           |
|    1 |    0 | CBZ -64-bit           |
|    1 |    1 | CBNZ-64-bit           |

## Test and branch (immediate)

The encodings in this section are decoded from Branches, Exception Generating and System instructions.

<!-- image -->

## Compare registers and branch

The encodings in this section are decoded from Branches, Exception Generating and System instructions.

<!-- image -->

| 31 30   | 24 23   | 21 20   | 16 15 14 13   |      |    |
|---------|---------|---------|---------------|------|----|
| sf 1    | 0 1 0 0 | cc      | Rm 0 0        | imm9 | Rt |

| sf   | cc   | Instruction Details                                 | Feature    |
|------|------|-----------------------------------------------------|------------|
| x    | 10x  | UNALLOCATED                                         | -          |
| 0    | 000  | CB < cc > (register) -32-bit greater than           | FEAT_CMPBR |
| 0    | 001  | CB < cc > (register) - 32-bit greater than or equal | FEAT_CMPBR |
| 0    | 010  | CB < cc > (register) -32-bit higher                 | FEAT_CMPBR |
| 0    | 011  | CB < cc > (register) - 32-bit higher or same        | FEAT_CMPBR |
| 0    | 110  | CB < cc > (register) -32-bit equal                  | FEAT_CMPBR |
| 0    | 111  | CB < cc > (register) -32-bit not equal              | FEAT_CMPBR |
| 1    | 000  | CB < cc > (register) -64-bit greater than           | FEAT_CMPBR |
| 1    | 001  | CB < cc > (register) - 64-bit greater than or equal | FEAT_CMPBR |
| 1    | 010  | CB < cc > (register) -64-bit higher                 | FEAT_CMPBR |
| 1    | 011  | CB < cc > (register) - 64-bit higher or same        | FEAT_CMPBR |
| 1    | 110  | CB < cc > (register) -64-bit equal                  | FEAT_CMPBR |
| 1    | 111  | CB < cc > (register) -64-bit not equal              | FEAT_CMPBR |

## Compare register with immediate and branch

The encodings in this section are decoded from Branches, Exception Generating and System instructions.

<!-- image -->

| 31 30   | 24 23     | 21 20   |      | 15 14 13   | 4   |
|---------|-----------|---------|------|------------|-----|
| sf 1    | 1 0 1 0 1 | cc      | imm6 | 0 imm9     | Rt  |

|   op | Instruction Details   |
|------|-----------------------|
|    0 | TBZ                   |
|    1 | TBNZ                  |

## Data Processing -- Register

Data Processing - Register

The encodings in this section are decoded from A64 instruction set encoding.

<!-- image -->

| 31   | 30   | 29 28   | 27 25 24   | 21 20   | 10   | 0   |
|------|------|---------|------------|---------|------|-----|
|      | op0  | op1     | 1 0 1      | op2     | op3  |     |

| op0   |   op1 | op2   | op3    | Instruction details              |
|-------|-------|-------|--------|----------------------------------|
| 0     |     1 | 0110  | xxxxxx | Data-processing (2 source)       |
| 1     |     1 | 0110  | xxxxxx | Data-processing (1 source)       |
| x     |     0 | 0xxx  | xxxxxx | Logical (shifted register)       |
| x     |     0 | 1xx0  | xxxxxx | Add/subtract (shifted register)  |
| x     |     0 | 1xx1  | xxxxxx | Add/subtract (extended register) |
| x     |     1 | 0000  | 000000 | Add/subtract (with carry)        |
| x     |     1 | 0000  | 001xxx | Add/subtract (checked pointer)   |
| x     |     1 | 0000  | 011xxx | UNALLOCATED                      |
| x     |     1 | 0000  | 100000 | UNALLOCATED                      |
| x     |     1 | 0000  | 1x1xxx | UNALLOCATED                      |
| x     |     1 | 0000  | x00001 | Rotate right into flags          |
| x     |     1 | 0000  | x0010x | UNALLOCATED                      |
| x     |     1 | 0000  | x10x0x | UNALLOCATED                      |

| sf   | cc   | Instruction Details                         | Feature    |
|------|------|---------------------------------------------|------------|
| x    | 10x  | UNALLOCATED                                 | -          |
| 0    | 000  | CB < cc > (immediate) - 32-bit greater than | FEAT_CMPBR |
| 0    | 001  | CB < cc > (immediate) -32-bit less than     | FEAT_CMPBR |
| 0    | 010  | CB < cc > (immediate) -32-bit higher        | FEAT_CMPBR |
| 0    | 011  | CB < cc > (immediate) -32-bit lower         | FEAT_CMPBR |
| 0    | 110  | CB < cc > (immediate) -32-bit equal         | FEAT_CMPBR |
| 0    | 111  | CB < cc > (immediate) -32-bit not equal     | FEAT_CMPBR |
| 1    | 000  | CB < cc > (immediate) - 64-bit greater than | FEAT_CMPBR |
| 1    | 001  | CB < cc > (immediate) -64-bit less than     | FEAT_CMPBR |
| 1    | 010  | CB < cc > (immediate) -64-bit higher        | FEAT_CMPBR |
| 1    | 011  | CB < cc > (immediate) -64-bit lower         | FEAT_CMPBR |
| 1    | 110  | CB < cc > (immediate) -64-bit equal         | FEAT_CMPBR |
| 1    | 111  | CB < cc > (immediate) -64-bit not equal     | FEAT_CMPBR |

## Data-processing (2 source)

The encodings in this section are decoded from Data Processing - Register.

<!-- image -->

| 31   |   30 | 29 28   | 27 25 24   | 21    | 20   | 15     | 10 9   |    |
|------|------|---------|------------|-------|------|--------|--------|----|
| sf   |    0 | S 1     | 1 0 1 0    | 1 1 0 | Rm   | opcode | Rn     | Rd |

| sf   | S   | opcode   | Instruction Details                    | Feature    |
|------|-----|----------|----------------------------------------|------------|
| x    | x   | 1xxxxx   | UNALLOCATED                            | -          |
| x    | 0   | 00011x   | UNALLOCATED                            | -          |
| x    | 1   | 00001x   | UNALLOCATED                            | -          |
| x    | 1   | 0001xx   | UNALLOCATED                            | -          |
| x    | 1   | 001xxx   | UNALLOCATED                            | -          |
| x    | 1   | 01xxxx   | UNALLOCATED                            | -          |
| 0    | x   | 00000x   | UNALLOCATED                            | -          |
| 0    | 0   | 0x11xx   | UNALLOCATED                            | -          |
| 0    | 0   | 000010   | UDIV -32-bit                           | -          |
| 0    | 0   | 000011   | SDIV -32-bit                           | -          |
| 0    | 0   | 00010x   | UNALLOCATED                            | -          |
| 0    | 0   | 001000   | LSLV -32-bit                           | -          |
| 0    | 0   | 001001   | LSRV -32-bit                           | -          |
| 0    | 0   | 001010   | ASRV -32-bit                           | -          |
| 0    | 0   | 001011   | RORV-32-bit                            | -          |
| 0    | 0   | 010x11   | UNALLOCATED                            | -          |
| 0    | 0   | 010000   | CRC32B, CRC32H, CRC32W, CRC32X -CRC32B | FEAT_CRC32 |
| 0    | 0   | 010001   | CRC32B, CRC32H, CRC32W, CRC32X -CRC32H | FEAT_CRC32 |

| op0   |   op1 | op2   | op3    | Instruction details             |
|-------|-------|-------|--------|---------------------------------|
| x     |     1 | 0000  | xx0010 | Evaluate into flags             |
| x     |     1 | 0000  | xx0011 | UNALLOCATED                     |
| x     |     1 | 0000  | xx011x | UNALLOCATED                     |
| x     |     1 | 0010  | xxxx0x | Conditional compare (register)  |
| x     |     1 | 0010  | xxxx1x | Conditional compare (immediate) |
| x     |     1 | 0100  | xxxxxx | Conditional select              |
| x     |     1 | 0xx1  | xxxxxx | UNALLOCATED                     |
| x     |     1 | 1xxx  | xxxxxx | Data-processing (3 source)      |

## Data-processing (1 source)

The encodings in this section are decoded from Data Processing - Register.

|   sf | S   | opcode   | Instruction Details                        | Feature    |
|------|-----|----------|--------------------------------------------|------------|
|    0 | 0   | 010010   | CRC32B, CRC32H, CRC32W, CRC32X -CRC32W     | FEAT_CRC32 |
|    0 | 0   | 010100   | CRC32CB, CRC32CH, CRC32CW, CRC32CX-CRC32CB | FEAT_CRC32 |
|    0 | 0   | 010101   | CRC32CB, CRC32CH, CRC32CW, CRC32CX-CRC32CH | FEAT_CRC32 |
|    0 | 0   | 010110   | CRC32CB, CRC32CH, CRC32CW, CRC32CX-CRC32CW | FEAT_CRC32 |
|    0 | 0   | 011000   | SMAX(register) -32-bit                     | FEAT_CSSC  |
|    0 | 0   | 011001   | UMAX(register) -32-bit                     | FEAT_CSSC  |
|    0 | 0   | 011010   | SMIN (register) -32-bit                    | FEAT_CSSC  |
|    0 | 0   | 011011   | UMIN(register) -32-bit                     | FEAT_CSSC  |
|    1 | x   | 000001   | UNALLOCATED                                | -          |
|    1 | 0   | 000000   | SUBP                                       | FEAT_MTE   |
|    1 | 0   | 000010   | UDIV -64-bit                               | -          |
|    1 | 0   | 000011   | SDIV -64-bit                               | -          |
|    1 | 0   | 000100   | IRG                                        | FEAT_MTE   |
|    1 | 0   | 000101   | GMI                                        | FEAT_MTE   |
|    1 | 0   | 001000   | LSLV -64-bit                               | -          |
|    1 | 0   | 001001   | LSRV -64-bit                               | -          |
|    1 | 0   | 001010   | ASRV -64-bit                               | -          |
|    1 | 0   | 001011   | RORV-64-bit                                | -          |
|    1 | 0   | 001100   | PACGA                                      | FEAT_PAuth |
|    1 | 0   | 001101   | UNALLOCATED                                | -          |
|    1 | 0   | 00111x   | UNALLOCATED                                | -          |
|    1 | 0   | 010xx0   | UNALLOCATED                                | -          |
|    1 | 0   | 010001   | UNALLOCATED                                | -          |
|    1 | 0   | 010011   | CRC32B, CRC32H, CRC32W, CRC32X -CRC32X     | FEAT_CRC32 |
|    1 | 0   | 010101   | UNALLOCATED                                | -          |
|    1 | 0   | 010111   | CRC32CB, CRC32CH, CRC32CW, CRC32CX-CRC32CX | FEAT_CRC32 |
|    1 | 0   | 011000   | SMAX(register) -64-bit                     | FEAT_CSSC  |
|    1 | 0   | 011001   | UMAX(register) -64-bit                     | FEAT_CSSC  |
|    1 | 0   | 011010   | SMIN (register) -64-bit                    | FEAT_CSSC  |
|    1 | 0   | 011011   | UMIN(register) -64-bit                     | FEAT_CSSC  |
|    1 | 0   | 0111xx   | UNALLOCATED                                | -          |
|    1 | 1   | 000000   | SUBPS                                      | FEAT_MTE   |

<!-- image -->

| 31   |   30 | 29   |   28 | 27 25 24   |   21 | 20   |        | 9   |    |
|------|------|------|------|------------|------|------|--------|-----|----|
| sf   |    1 | S    |    1 | 1 0 1 0    |    1 | 1 0  | opcode | Rn  | Rd |

| sf   |   S | opcode2   | opcode   | Rn    | Rd    | Instruction Details                             | Feature    |
|------|-----|-----------|----------|-------|-------|-------------------------------------------------|------------|
| x    |   0 | 00000     | 001001   | xxxxx | xxxxx | UNALLOCATED                                     | -          |
| x    |   0 | 00000     | 00101x   | xxxxx | xxxxx | UNALLOCATED                                     | -          |
| x    |   0 | 00000     | 0011xx   | xxxxx | xxxxx | UNALLOCATED                                     | -          |
| x    |   0 | 00000     | 01xxxx   | xxxxx | xxxxx | UNALLOCATED                                     | -          |
| x    |   0 | 00000     | 1xxxxx   | xxxxx | xxxxx | UNALLOCATED                                     | -          |
| x    |   0 | 0001x     | xxxxxx   | xxxxx | xxxxx | UNALLOCATED                                     | -          |
| x    |   0 | 001xx     | xxxxxx   | xxxxx | xxxxx | UNALLOCATED                                     | -          |
| x    |   0 | 01xxx     | xxxxxx   | xxxxx | xxxxx | UNALLOCATED                                     | -          |
| x    |   0 | 1xxxx     | xxxxxx   | xxxxx | xxxxx | UNALLOCATED                                     | -          |
| x    |   1 | xxxxx     | xxxxxx   | xxxxx | xxxxx | UNALLOCATED                                     | -          |
| 0    |   0 | 00000     | 000000   | xxxxx | xxxxx | RBIT -32-bit                                    | -          |
| 0    |   0 | 00000     | 000001   | xxxxx | xxxxx | REV16 -32-bit                                   | -          |
| 0    |   0 | 00000     | 000010   | xxxxx | xxxxx | REV-32-bit                                      | -          |
| 0    |   0 | 00000     | 000011   | xxxxx | xxxxx | UNALLOCATED                                     | -          |
| 0    |   0 | 00000     | 000100   | xxxxx | xxxxx | CLZ -32-bit                                     | -          |
| 0    |   0 | 00000     | 000101   | xxxxx | xxxxx | CLS -32-bit                                     | -          |
| 0    |   0 | 00000     | 000110   | xxxxx | xxxxx | CTZ -32-bit                                     | FEAT_CSSC  |
| 0    |   0 | 00000     | 000111   | xxxxx | xxxxx | CNT-32-bit                                      | FEAT_CSSC  |
| 0    |   0 | 00000     | 001000   | xxxxx | xxxxx | ABS -32-bit                                     | FEAT_CSSC  |
| 0    |   0 | 00001     | xxxxxx   | xxxxx | xxxxx | UNALLOCATED                                     | -          |
| 1    |   0 | 00000     | 000000   | xxxxx | xxxxx | RBIT -64-bit                                    | -          |
| 1    |   0 | 00000     | 000001   | xxxxx | xxxxx | REV16 -64-bit                                   | -          |
| 1    |   0 | 00000     | 000010   | xxxxx | xxxxx | REV32                                           | -          |
| 1    |   0 | 00000     | 000011   | xxxxx | xxxxx | REV-64-bit                                      | -          |
| 1    |   0 | 00000     | 000100   | xxxxx | xxxxx | CLZ -64-bit                                     | -          |
| 1    |   0 | 00000     | 000101   | xxxxx | xxxxx | CLS -64-bit                                     | -          |
| 1    |   0 | 00000     | 000110   | xxxxx | xxxxx | CTZ -64-bit                                     | FEAT_CSSC  |
| 1    |   0 | 00000     | 000111   | xxxxx | xxxxx | CNT-64-bit                                      | FEAT_CSSC  |
| 1    |   0 | 00000     | 001000   | xxxxx | xxxxx | ABS -64-bit                                     | FEAT_CSSC  |
| 1    |   0 | 00001     | 000000   | xxxxx | xxxxx | PACIA, PACIA1716, PACIASP, PACIAZ, PACIZA-PACIA | FEAT_PAuth |
| 1    |   0 | 00001     | 000001   | xxxxx | xxxxx | PACIB, PACIB1716, PACIBSP, PACIBZ, PACIZB-PACIB | FEAT_PAuth |
| 1    |   0 | 00001     | 000010   | xxxxx | xxxxx | PACDA,PACDZA-PACDA                              | FEAT_PAuth |
| 1    |   0 | 00001     | 000011   | xxxxx | xxxxx | PACDB,PACDZB-PACDB                              | FEAT_PAuth |

|   sf |   S |   opcode2 | opcode   | Rn       | Rd       | Instruction Details                              | Feature       | Feature    |
|------|-----|-----------|----------|----------|----------|--------------------------------------------------|---------------|------------|
|    1 |   0 |     00001 | 000100   | xxxxx    | xxxxx    | AUTIA, AUTIA1716, AUTIASP, AUTIAZ,AUTIZA-AUTIA   | FEAT_PAuth    | FEAT_PAuth |
|    1 |   0 |     00001 | 000101   | xxxxx    | xxxxx    | AUTIB, AUTIB1716, AUTIBSP, AUTIBZ,AUTIZB-AUTIB   | FEAT_PAuth    | FEAT_PAuth |
|    1 |   0 |     00001 | 000110   | xxxxx    | xxxxx    | AUTDA,AUTDZA-AUTDA                               | FEAT_PAuth    |            |
|    1 |   0 |     00001 | 000111   | xxxxx    | xxxxx    | AUTDB,AUTDZB-AUTDB                               |               | FEAT_PAuth |
|    1 |   0 |     00001 | 001xxx   | != 11111 | xxxxx    | UNALLOCATED                                      | -             |            |
|    1 |   0 |     00001 | 001000   | 11111    | xxxxx    | PACIA, PACIA1716, PACIASP, PACIAZ, PACIZA-PACIZA | FEAT_PAuth    |            |
|    1 |   0 |     00001 | 001001   | 11111    | xxxxx    | PACIB, PACIB1716, PACIBSP, PACIBZ, PACIZB-PACIZB | FEAT_PAuth    |            |
|    1 |   0 |     00001 | 001010   | 11111    | xxxxx    | PACDA,PACDZA-PACDZA                              | FEAT_PAuth    |            |
|    1 |   0 |     00001 | 001011   | 11111    | xxxxx    | PACDB,PACDZB-PACDZB                              | FEAT_PAuth    |            |
|    1 |   0 |     00001 | 001100   | 11111    | xxxxx    | AUTIA, AUTIA1716, AUTIASP, AUTIAZ,AUTIZA-AUTIZA  | FEAT_PAuth    |            |
|    1 |   0 |     00001 | 001101   | 11111    | xxxxx    | AUTIB, AUTIB1716, AUTIBSP, AUTIBZ,AUTIZB-AUTIZB  | FEAT_PAuth    |            |
|    1 |   0 |     00001 | 001110   | 11111    | xxxxx    | AUTDA,AUTDZA-AUTDZA                              | FEAT_PAuth    |            |
|    1 |   0 |     00001 | 001111   | 11111    | xxxxx    | AUTDB,AUTDZB-AUTDZB                              | FEAT_PAuth    |            |
|    1 |   0 |     00001 | 01000x   | != 11111 | xxxxx    | UNALLOCATED                                      | -             |            |
|    1 |   0 |     00001 | 010000   | 11111    | xxxxx    | XPACD, XPACI, XPACLRI-XPACI                      | FEAT_PAuth    |            |
|    1 |   0 |     00001 | 010001   | 11111    | xxxxx    | XPACD, XPACI,XPACLRI-XPACD                       | FEAT_PAuth    |            |
|    1 |   0 |     00001 | 01001x   | xxxxx    | xxxxx    | UNALLOCATED                                      | -             |            |
|    1 |   0 |     00001 | 0101xx   | xxxxx    | xxxxx    | UNALLOCATED                                      | -             |            |
|    1 |   0 |     00001 | 011xxx   | xxxxx    | xxxxx    | UNALLOCATED                                      | -             |            |
|    1 |   0 |     00001 | 10xxxx   | xxxxx    | != 11110 | UNALLOCATED                                      | -             |            |
|    1 |   0 |     00001 | 1000xx   | != 11111 | 11110    | UNALLOCATED                                      | -             |            |
|    1 |   0 |     00001 | 100000   | 11111    | 11110    | PACNBIASPPC                                      | FEAT_PAuth_LR |            |
|    1 |   0 |     00001 | 100001   | 11111    | 11110    | PACNBIBSPPC                                      | FEAT_PAuth_LR |            |
|    1 |   0 |     00001 | 100010   | 11111    | 11110    | PACIA171615                                      | FEAT_PAuth_LR |            |
|    1 |   0 |     00001 | 100011   | 11111    | 11110    | PACIB171615                                      | FEAT_PAuth_LR |            |
|    1 |   0 |     00001 | 100100   | xxxxx    | 11110    | AUTIASPPCR                                       | FEAT_PAuth_LR |            |
|    1 |   0 |     00001 | 100101   | xxxxx    | 11110    | AUTIBSPPCR                                       | FEAT_PAuth_LR |            |
|    1 |   0 |     00001 | 10011x   | xxxxx    | 11110    | UNALLOCATED                                      | -             |            |
|    1 |   0 |     00001 | 101xxx   | != 11111 | 11110    | UNALLOCATED                                      | -             |            |
|    1 |   0 |     00001 | 101000   | 11111    | 11110    | PACIASPPC                                        | FEAT_PAuth_LR |            |
|    1 |   0 |     00001 | 101001   | 11111    | 11110    | PACIBSPPC                                        | FEAT_PAuth_LR |            |
|    1 |   0 |     00001 | 10101x   | 11111    | 11110    | UNALLOCATED                                      | -             |            |
|    1 |   0 |     00001 | 10110x   | 11111    | 11110    | UNALLOCATED                                      | -             |            |
|    1 |   0 |     00001 | 101110   | 11111    | 11110    | AUTIA171615                                      | FEAT_PAuth_LR |            |
|    1 |   0 |     00001 | 101111   | 11111    | 11110    | AUTIB171615                                      | FEAT_PAuth_LR |            |
|    1 |   0 |     00001 | 11xxxx   | xxxxx    | xxxxx    | UNALLOCATED                                      | -             |            |

## Logical (shifted register)

The encodings in this section are decoded from Data Processing - Register.

<!-- image -->

| 31   | 30   | 29 28 27   | 24 23 22   | 21    |    | 20   | 16 15   | 5   |    |
|------|------|------------|------------|-------|----|------|---------|-----|----|
| sf   | opc  | 0 1 0 1 0  |            | shift | N  | Rm   | imm6    | Rn  | Rd |

|   sf |   opc |   N | Instruction Details             |
|------|-------|-----|---------------------------------|
|    0 |    00 |   0 | AND(shifted register) -32-bit   |
|    0 |    00 |   1 | BIC (shifted register) -32-bit  |
|    0 |    01 |   0 | ORR(shifted register) -32-bit   |
|    0 |    01 |   1 | ORN(shifted register) -32-bit   |
|    0 |    10 |   0 | EOR(shifted register) -32-bit   |
|    0 |    10 |   1 | EON(shifted register) -32-bit   |
|    0 |    11 |   0 | ANDS(shifted register) -32-bit  |
|    0 |    11 |   1 | BICS (shifted register) -32-bit |
|    1 |    00 |   0 | AND(shifted register) -64-bit   |
|    1 |    00 |   1 | BIC (shifted register) -64-bit  |
|    1 |    01 |   0 | ORR(shifted register) -64-bit   |
|    1 |    01 |   1 | ORN(shifted register) -64-bit   |
|    1 |    10 |   0 | EOR(shifted register) -64-bit   |
|    1 |    10 |   1 | EON(shifted register) -64-bit   |
|    1 |    11 |   0 | ANDS(shifted register) -64-bit  |
|    1 |    11 |   1 | BICS (shifted register) -64-bit |

## Add/subtract (shifted register)

The encodings in this section are decoded from Data Processing - Register.

<!-- image -->

| 31   | 30   | 29 28   | 27    |   24 | 23    |   22 21 |    |      |    | 5   | 0   |
|------|------|---------|-------|------|-------|---------|----|------|----|-----|-----|
| sf   | op   | S 0     | 1 0 1 |    1 | shift |       0 | Rm | imm6 | Rn |     | Rd  |

|   sf |   op | S Instruction Details            |
|------|------|----------------------------------|
|    0 |    0 | 0 ADD(shifted register) -32-bit  |
|    0 |    0 | 1 ADDS(shifted register) -32-bit |

## Add/subtract (extended register)

The encodings in this section are decoded from Data Processing - Register.

<!-- image -->

| 31   | 30   | 29 28   | 27      | 24   | 23   |   22 21 | 20   | 16 15   | 13 12   | 10   | 5   |    |
|------|------|---------|---------|------|------|---------|------|---------|---------|------|-----|----|
| sf   | op   | S 0     | 1 0 1 1 |      | opt  |       1 | Rm   |         | option  | imm3 | Rn  | Rd |

| sf   | op   | S   | opt   | Instruction Details              |
|------|------|-----|-------|----------------------------------|
| x    | x    | x   | != 00 | UNALLOCATED                      |
| 0    | 0    | 0   | 00    | ADD(extended register) -32-bit   |
| 0    | 0    | 1   | 00    | ADDS(extended register) -32-bit  |
| 0    | 1    | 0   | 00    | SUB (extended register) -32-bit  |
| 0    | 1    | 1   | 00    | SUBS (extended register) -32-bit |
| 1    | 0    | 0   | 00    | ADD(extended register) -64-bit   |
| 1    | 0    | 1   | 00    | ADDS(extended register) -64-bit  |
| 1    | 1    | 0   | 00    | SUB (extended register) -64-bit  |
| 1    | 1    | 1   | 00    | SUBS (extended register) -64-bit |

## Add/subtract (with carry)

The encodings in this section are decoded from Data Processing - Register.

<!-- image -->

| 31   | 30   | 29 28   | 27 25 24   | 21 20   |    | 15 10       | 5   | 0   |
|------|------|---------|------------|---------|----|-------------|-----|-----|
| sf   | op   | S 1     | 1 0 1 0    | 0 0 0   | Rm | 0 0 0 0 0 0 | Rn  | Rd  |

|   sf |   op |   S | Instruction Details             |
|------|------|-----|---------------------------------|
|    0 |    1 |   0 | SUB (shifted register) -32-bit  |
|    0 |    1 |   1 | SUBS (shifted register) -32-bit |
|    1 |    0 |   0 | ADD(shifted register) -64-bit   |
|    1 |    0 |   1 | ADDS(shifted register) -64-bit  |
|    1 |    1 |   0 | SUB (shifted register) -64-bit  |
|    1 |    1 |   1 | SUBS (shifted register) -64-bit |

## Add/subtract (checked pointer)

The encodings in this section are decoded from Data Processing - Register.

<!-- image -->

| 31 30   | 29   | 28 27   | 25 24   |   21 20 | 16 15   | 10   | 9   | 5 4   |
|---------|------|---------|---------|---------|---------|------|-----|-------|
| sf op   | S    | 1 1 0 1 | 0 0 0   |       0 | 0 0     | imm3 | Rn  | Rd    |

|   sf | op   | S   | Instruction Details   | Feature   |
|------|------|-----|-----------------------|-----------|
|    0 | x    | x   | UNALLOCATED           | -         |
|    1 | x    | 1   | UNALLOCATED           | -         |
|    1 | 0    | 0   | ADDPT                 | FEAT_CPA  |
|    1 | 1    | 0   | SUBPT                 | FEAT_CPA  |

## Rotate right into flags

The encodings in this section are decoded from Data Processing - Register.

<!-- image -->

|   sf | op   | S   | o2   | Instruction Details   | Feature    |
|------|------|-----|------|-----------------------|------------|
|    0 | x    | x   | x    | UNALLOCATED           | -          |
|    1 | 0    | 0   | x    | UNALLOCATED           | -          |
|    1 | 0    | 1   | 0    | RMIF                  | FEAT_FlagM |
|    1 | 0    | 1   | 1    | UNALLOCATED           | -          |

|   sf |   op |   S | Instruction Details   |
|------|------|-----|-----------------------|
|    0 |    0 |   0 | ADC-32-bit            |
|    0 |    0 |   1 | ADCS-32-bit           |
|    0 |    1 |   0 | SBC -32-bit           |
|    0 |    1 |   1 | SBCS -32-bit          |
|    1 |    0 |   0 | ADC-64-bit            |
|    1 |    0 |   1 | ADCS-64-bit           |
|    1 |    1 |   0 | SBC -64-bit           |
|    1 |    1 |   1 | SBCS -64-bit          |

## Evaluate into flags

The encodings in this section are decoded from Data Processing - Register.

<!-- image -->

|   sf | op   | S   | opcode2   | sz   | o3   | mask    | Instruction Details   | Feature    |
|------|------|-----|-----------|------|------|---------|-----------------------|------------|
|    0 | 0    | 0   | xxxxxx    | x    | x    | xxxx    | UNALLOCATED           | -          |
|    0 | 0    | 1   | 000000    | x    | 0    | != 1101 | UNALLOCATED           | -          |
|    0 | 0    | 1   | 000000    | x    | 1    | xxxx    | UNALLOCATED           | -          |
|    0 | 0    | 1   | 000000    | 0    | 0    | 1101    | SETF8, SETF16-SETF8   | FEAT_FlagM |
|    0 | 0    | 1   | 000000    | 1    | 0    | 1101    | SETF8, SETF16 -SETF16 | FEAT_FlagM |
|    0 | 0    | 1   | != 000000 | x    | x    | xxxx    | UNALLOCATED           | -          |
|    0 | 1    | x   | xxxxxx    | x    | x    | xxxx    | UNALLOCATED           | -          |
|    1 | x    | x   | xxxxxx    | x    | x    | xxxx    | UNALLOCATED           | -          |

## Conditional compare (register)

The encodings in this section are decoded from Data Processing - Register.

<!-- image -->

| 31   | 30   | 29 28   | 27    | 25 24   | 21 20   |    | 15   |   12 11 | 10   |    | 5 4   | 0    |
|------|------|---------|-------|---------|---------|----|------|---------|------|----|-------|------|
| sf   | op   | S 1     | 1 0 1 | 0 0     | 1 0     | Rm | cond |       0 | o2   | Rn | o3    | nzcv |

| sf   | op   |   S | o2   | o3   | Instruction Details    |
|------|------|-----|------|------|------------------------|
| x    | x    |   0 | x    | x    | UNALLOCATED            |
| x    | x    |   1 | 0    | 1    | UNALLOCATED            |
| x    | x    |   1 | 1    | x    | UNALLOCATED            |
| 0    | 0    |   1 | 0    | 0    | CCMN(register) -32-bit |
| 0    | 1    |   1 | 0    | 0    | CCMP(register) -32-bit |
| 1    | 0    |   1 | 0    | 0    | CCMN(register) -64-bit |
| 1    | 1    |   1 | 0    | 0    | CCMP(register) -64-bit |

|   sf |   op | S o2   | Instruction Details   | Feature   |
|------|------|--------|-----------------------|-----------|
|    1 |    1 | x x    | UNALLOCATED           | -         |

## Conditional compare (immediate)

The encodings in this section are decoded from Data Processing - Register.

<!-- image -->

| 31   | 30   | 29 28   | 27    | 25 24   | 21 20   | 16 15   | 12 11   |   10 | 9   | 5 4   |    | 0    |
|------|------|---------|-------|---------|---------|---------|---------|------|-----|-------|----|------|
| sf   | op   | S 1     | 1 0 1 | 0 0     | 1 0     | imm5    | cond    |    1 | o2  | Rn    | o3 | nzcv |

| sf   | op   | S o2   | o3   | Instruction Details     |
|------|------|--------|------|-------------------------|
| x    | x    | 0 x    | x    | UNALLOCATED             |
| x    | x    | 1 0    | 1    | UNALLOCATED             |
| x    | x    | 1 1    | x    | UNALLOCATED             |
| 0    | 0    | 1 0    | 0    | CCMN(immediate) -32-bit |
| 0    | 1    | 1 0    | 0    | CCMP(immediate) -32-bit |
| 1    | 0    | 1 0    | 0    | CCMN(immediate) -64-bit |
| 1    | 1    | 1 0    | 0    | CCMP(immediate) -64-bit |

## Conditional select

The encodings in this section are decoded from Data Processing - Register.

<!-- image -->

| 31   | 30 29 28 27   | 21 20 16         | 12 11 10   | 5   | 0   |
|------|---------------|------------------|------------|-----|-----|
| sf   | op S 1        | 1 0 1 0 1 0 0 Rm | cond op2   | Rn  | Rd  |

| sf   | op   |   S | op2   | Instruction Details   |
|------|------|-----|-------|-----------------------|
| x    | x    |   0 | 1x    | UNALLOCATED           |
| x    | x    |   1 | xx    | UNALLOCATED           |
| 0    | 0    |   0 | 00    | CSEL -32-bit          |
| 0    | 0    |   0 | 01    | CSINC -32-bit         |
| 0    | 1    |   0 | 00    | CSINV -32-bit         |
| 0    | 1    |   0 | 01    | CSNEG -32-bit         |
| 1    | 0    |   0 | 00    | CSEL -64-bit          |
| 1    | 0    |   0 | 01    | CSINC -64-bit         |
| 1    | 1    |   0 | 00    | CSINV -64-bit         |
| 1    | 1    |   0 | 01    | CSNEG -64-bit         |

## Data-processing (3 source)

The encodings in this section are decoded from Data Processing - Register.

<!-- image -->

| 31   | 30   | 29 28 27 24   | 21   | 20   | 16 15   | 10   | 5   |    |
|------|------|---------------|------|------|---------|------|-----|----|
| sf   | op54 | 1 1 0 1 1     |      |      | o0      | Ra   | Rn  | Rd |

| sf   | op54   | op31   | o0   | Instruction Details   | Feature   |
|------|--------|--------|------|-----------------------|-----------|
| x    | 00     | 100    | x    | UNALLOCATED           | -         |
| x    | != 00  | xxx    | x    | UNALLOCATED           | -         |
| 0    | 00     | x01    | x    | UNALLOCATED           | -         |
| 0    | 00     | x1x    | x    | UNALLOCATED           | -         |
| 0    | 00     | 000    | 0    | MADD-32-bit           | -         |
| 0    | 00     | 000    | 1    | MSUB-32-bit           | -         |
| 1    | 00     | x10    | 1    | UNALLOCATED           | -         |
| 1    | 00     | 000    | 0    | MADD-64-bit           | -         |
| 1    | 00     | 000    | 1    | MSUB-64-bit           | -         |
| 1    | 00     | 001    | 0    | SMADDL                | -         |
| 1    | 00     | 001    | 1    | SMSUBL                | -         |
| 1    | 00     | 010    | 0    | SMULH                 | -         |
| 1    | 00     | 011    | 0    | MADDPT                | FEAT_CPA  |
| 1    | 00     | 011    | 1    | MSUBPT                | FEAT_CPA  |
| 1    | 00     | 101    | 0    | UMADDL                | -         |
| 1    | 00     | 101    | 1    | UMSUBL                | -         |
| 1    | 00     | 110    | 0    | UMULH                 | -         |
| 1    | 00     | 111    | x    | UNALLOCATED           | -         |

## Data Processing -- Scalar Floating-Point and Advanced SIMD

Data Processing - Scalar Floating-Point and Advanced SIMD

The encodings in this section are decoded from A64 instruction set encoding.

<!-- image -->

| op0   | op1   | op2   | op3       | Instruction details                                  | Feature   |
|-------|-------|-------|-----------|------------------------------------------------------|-----------|
| 00x0  | 0x    | x101  | 00xxxxx10 | UNALLOCATED                                          | -         |
| 00x0  | 11    | xxxx  | xxxxxxxx1 | UNALLOCATED                                          | -         |
| 0100  | 0x    | x101  | 00xxxxx10 | Cryptographic AES                                    | -         |
| 0101  | 0x    | x0xx  | xxx0xxx00 | Cryptographic three-registerSHA                      | -         |
| 0101  | 0x    | x0xx  | xxx0xxx10 | UNALLOCATED                                          | -         |
| 0101  | 0x    | x0xx  | xxx1xxxx0 | UNALLOCATED                                          | -         |
| 0101  | 0x    | x101  | 00xxxxx10 | Cryptographic two-registerSHA                        | -         |
| 0111  | 0x    | x0xx  | xxxxxxxx0 | UNALLOCATED                                          | -         |
| 011x  | 0x    | x101  | 00xxxxx10 | UNALLOCATED                                          | -         |
| 01x1  | 00    | 00xx  | xxx0xxxx1 | Advanced SIMD scalar copy                            | -         |
| 01x1  | 01    | 00xx  | xxx0xxxx1 | UNALLOCATED                                          | -         |
| 01x1  | 0x    | 0111  | 00xxxxx10 | UNALLOCATED                                          | -         |
| 01x1  | 0x    | 10xx  | xxx00xxx1 | Advanced SIMD scalar three same FP16                 | -         |
| 01x1  | 0x    | 10xx  | xxx01xxx1 | UNALLOCATED                                          | -         |
| 01x1  | 0x    | 1111  | 00xxxxx10 | Advanced SIMD scalar two-register miscellaneous FP16 | -         |
| 01x1  | 0x    | x0xx  | xxx1xxxx1 | Advanced SIMD scalar three same extra                | -         |
| 01x1  | 0x    | x100  | 00xxxxx10 | Advanced SIMD scalar two-register miscellaneous      | -         |
| 01x1  | 0x    | x110  | 00xxxxx10 | Advanced SIMD scalar pairwise                        | -         |
| 01x1  | 0x    | x1xx  | 01xxxxx10 | UNALLOCATED                                          | -         |
| 01x1  | 0x    | x1xx  | 1xxxxxx10 | UNALLOCATED                                          | -         |
| 01x1  | 0x    | x1xx  | xxxxxxx00 | Advanced SIMD scalar three different                 | -         |
| 01x1  | 0x    | x1xx  | xxxxxxxx1 | Advanced SIMD scalar three same                      | -         |
| 01x1  | 10    | xxxx  | xxxxxxxx1 | Advanced SIMD scalar shift by immediate              | -         |
| 01x1  | 1x    | xxxx  | xxxxxxxx0 | Advanced SIMD scalar x indexed element               | -         |
| 01xx  | 11    | xxxx  | xxxxxxxx1 | UNALLOCATED                                          | -         |
| 0x00  | 0x    | x0xx  | xxx0xxx00 | Advanced SIMD table lookup                           | -         |
| 0x10  | 0x    | x0xx  | xxx0xxxx0 | Advanced SIMD extract                                | -         |
| 0xx0  | 00    | 00xx  | xxx0xxxx1 | Advanced SIMD copy                                   | -         |
| 0xx0  | 01    | 00xx  | xxx0xxxx1 | UNALLOCATED                                          | -         |
| 0xx0  | 0x    | 0111  | 00xxxxx10 | UNALLOCATED                                          | -         |
| 0xx0  | 0x    | 10xx  | xxx00xxx1 | Advanced SIMD three same (FP16)                      | -         |
| 0xx0  | 0x    | 10xx  | xxx01xxx1 | UNALLOCATED                                          | -         |
| 0xx0  | 0x    | 1111  | 00xxxxx10 | Advanced SIMD two-register miscellaneous (FP16)      | -         |
| 0xx0  | 0x    | x0xx  | xxx1xxxx0 | UNALLOCATED                                          | -         |
| 0xx0  | 0x    | x0xx  | xxx1xxxx1 | Advanced SIMD three-register extension               | -         |
| 0xx0  | 0x    | x100  | 00xxxxx10 | Advanced SIMD two-register miscellaneous             | -         |

| op0   | op1   | op2     | op3       | Instruction details                               | Feature   |
|-------|-------|---------|-----------|---------------------------------------------------|-----------|
| 0xx0  | 0x    | x110    | 00xxxxx10 | Advanced SIMD across lanes                        | -         |
| 0xx0  | 0x    | x1xx    | 01xxxxx10 | UNALLOCATED                                       | -         |
| 0xx0  | 0x    | x1xx    | 1xxxxxx10 | UNALLOCATED                                       | -         |
| 0xx0  | 0x    | x1xx    | xxxxxxx00 | Advanced SIMD three different                     | -         |
| 0xx0  | 0x    | x1xx    | xxxxxxxx1 | Advanced SIMD three same                          | -         |
| 0xx0  | 10    | 0000    | xxxxxxxx1 | Advanced SIMD modified immediate                  | -         |
| 0xx0  | 10    | != 0000 | xxxxxxxx1 | Advanced SIMD shift by immediate                  | -         |
| 0xx0  | 1x    | xxxx    | xxxxxxxx0 | Advanced SIMD vector x indexed element            | -         |
| 10x0  | xx    | xxxx    | xxxxxxxxx | UNALLOCATED                                       | -         |
| 1100  | 00    | 0xxx    | xxx1xxxxx | UNALLOCATED                                       | -         |
| 1100  | 00    | 10xx    | xxx10xxxx | Cryptographic three-register, imm2                | -         |
| 1100  | 00    | 10xx    | xxx11xxxx | UNALLOCATED                                       | -         |
| 1100  | 00    | 11xx    | xxx1x00xx | Cryptographic three-register SHA512               | -         |
| 1100  | 00    | 11xx    | xxx1x01xx | UNALLOCATED                                       | -         |
| 1100  | 00    | 11xx    | xxx1x1xxx | UNALLOCATED                                       | -         |
| 1100  | 00    | xxxx    | xxx0xxxxx | Cryptographic four-register                       | -         |
| 1100  | 01    | 00xx    | xxxxxxxxx | XAR                                               | FEAT_SHA3 |
| 1100  | 01    | 1000    | 0000xxxxx | UNALLOCATED                                       | -         |
| 1100  | 01    | 1000    | 0001000xx | Cryptographic two-register SHA512                 | -         |
| 1100  | 01    | 1000    | 0001100xx | UNALLOCATED                                       | -         |
| 1100  | 01    | 1000    | 0001x01xx | UNALLOCATED                                       | -         |
| 1100  | 01    | 1000    | 0001x1xxx | UNALLOCATED                                       | -         |
| 1100  | 01    | 1000    | 001xxxxxx | UNALLOCATED                                       | -         |
| 1100  | 01    | 1000    | 01xxxxxxx | UNALLOCATED                                       | -         |
| 1100  | 01    | 1000    | 1xxxxxxxx | UNALLOCATED                                       | -         |
| 1100  | 01    | 1001    | xxxxxxxxx | UNALLOCATED                                       | -         |
| 1100  | 01    | 101x    | xxxxxxxxx | UNALLOCATED                                       | -         |
| 1100  | 01    | x1xx    | xxxxxxxxx | UNALLOCATED                                       | -         |
| 1100  | 1x    | xxxx    | xxxxxxxxx | UNALLOCATED                                       | -         |
| 1110  | xx    | xxxx    | xxxxxxxxx | UNALLOCATED                                       | -         |
| 11x1  | xx    | xxxx    | xxxxxxxxx | UNALLOCATED                                       | -         |
| x0x1  | 0x    | x0xx    | xxxxxxxxx | Conversion between floating-point and fixed-point | -         |
| x0x1  | 0x    | x1xx    | xxx000000 | Conversion between floating-point and integer     | -         |
| x0x1  | 0x    | x1xx    | xxx100000 | UNALLOCATED                                       | -         |
| x0x1  | 0x    | x1xx    | xxxx10000 | Floating-point data-processing (1 source)         | -         |
| x0x1  | 0x    | x1xx    | xxxxx1000 | Floating-point compare                            | -         |
| x0x1  | 0x    | x1xx    | xxxxxx100 | Floating-point immediate                          | -         |
| x0x1  | 0x    | x1xx    | xxxxxxx01 | Floating-point conditional compare                | -         |

| op0   | op1   | op2   | op3       | Instruction details                       | Feature   |
|-------|-------|-------|-----------|-------------------------------------------|-----------|
| x0x1  | 0x    | x1xx  | xxxxxxx10 | Floating-point data-processing (2 source) | -         |
| x0x1  | 0x    | x1xx  | xxxxxxx11 | Floating-point conditional select         | -         |
| x0x1  | 1x    | xxxx  | xxxxxxxxx | Floating-point data-processing (3 source) | -         |

## Cryptographic AES

The encodings in this section are decoded from Data Processing - Scalar Floating-Point and Advanced SIMD.

<!-- image -->

| 31   | 28 27   | 24 23 22 21   | 17 16     | 12 11 10 9   | 5 4   | 0   |
|------|---------|---------------|-----------|--------------|-------|-----|
| 0 1  | 0 0 1   | 1 0 size      | 1 0 1 0 0 | 1 0          | Rn    | Rd  |

| size   | opcode   | Instruction Details   | Feature   |
|--------|----------|-----------------------|-----------|
| 00     | 000xx    | UNALLOCATED           | -         |
| 00     | 00100    | AESE                  | FEAT_AES  |
| 00     | 00101    | AESD                  | FEAT_AES  |
| 00     | 00110    | AESMC                 | FEAT_AES  |
| 00     | 00111    | AESIMC                | FEAT_AES  |
| 00     | 01xxx    | UNALLOCATED           | -         |
| 00     | 1xxxx    | UNALLOCATED           | -         |
| != 00  | xxxxx    | UNALLOCATED           | -         |

## Cryptographic three-register SHA

The encodings in this section are decoded from Data Processing - Scalar Floating-Point and Advanced SIMD.

<!-- image -->

| 31   | 28 27   | 24 23 22   | 21   |   20 | 16 15 14   | 12     | 11 10   | 5 4   | 0   |
|------|---------|------------|------|------|------------|--------|---------|-------|-----|
| 0 1  | 0 1     | 1 1 1 0    | size |    0 | Rm 0       | opcode | 0 0     | Rn    | Rd  |

|   size |   opcode | Instruction Details   | Feature     |
|--------|----------|-----------------------|-------------|
|     00 |      000 | SHA1C                 | FEAT_SHA1   |
|     00 |      001 | SHA1P                 | FEAT_SHA1   |
|     00 |      010 | SHA1M                 | FEAT_SHA1   |
|     00 |      011 | SHA1SU0               | FEAT_SHA1   |
|     00 |      100 | SHA256H               | FEAT_SHA256 |

## Advanced SIMD scalar copy

The encodings in this section are decoded from Data Processing - Scalar Floating-Point and Advanced SIMD.

<!-- image -->

|   31 30 | 29 28   | 25 24 23 22 21 20   | 16 15 14   |    | 11 10   | 9 5    | 4   | 0   |
|---------|---------|---------------------|------------|----|---------|--------|-----|-----|
|       0 | 1 op    | 1 1 1               | 1 0 0 0    |  0 | imm5 0  | imm4 1 | Rn  | Rd  |

|   op | imm4    | Instruction Details   | Feature      |
|------|---------|-----------------------|--------------|
|    0 | 0000    | DUP(element)          | FEAT_AdvSIMD |
|    0 | != 0000 | UNALLOCATED           | -            |
|    1 | xxxx    | UNALLOCATED           | -            |

| size   | opcode   | Instruction Details   | Feature     |
|--------|----------|-----------------------|-------------|
| 00     | 101      | SHA256H2              | FEAT_SHA256 |
| 00     | 110      | SHA256SU1             | FEAT_SHA256 |
| 00     | 111      | UNALLOCATED           | -           |
| != 00  | xxx      | UNALLOCATED           | -           |

## Cryptographic two-register SHA

The encodings in this section are decoded from Data Processing - Scalar Floating-Point and Advanced SIMD.

<!-- image -->

| 31   | 28 27   | 24 23 22 21   | 17 16 12         | 11 10   | 5   | 0   |
|------|---------|---------------|------------------|---------|-----|-----|
| 0 1  | 0 1 1   | 1 0 size      | 1 0 1 0 0 opcode | 1 0     | Rn  | Rd  |

| size   | opcode   | Instruction Details   | Feature     |
|--------|----------|-----------------------|-------------|
| 00     | 00000    | SHA1H                 | FEAT_SHA1   |
| 00     | 00001    | SHA1SU1               | FEAT_SHA1   |
| 00     | 00010    | SHA256SU0             | FEAT_SHA256 |
| 00     | 00011    | UNALLOCATED           | -           |
| 00     | 001xx    | UNALLOCATED           | -           |
| 00     | 01xxx    | UNALLOCATED           | -           |
| 00     | 1xxxx    | UNALLOCATED           | -           |
| != 00  | xxxxx    | UNALLOCATED           | -           |

## Advanced SIMD scalar three same FP16

The encodings in this section are decoded from Data Processing - Scalar Floating-Point and Advanced SIMD.

<!-- image -->

|   31 30 | 29 28   | 24 23 22 21 20 16 15 14   | 13       | 11 10      |   9 5 | 4   | 0   |
|---------|---------|---------------------------|----------|------------|-------|-----|-----|
|       0 | 1 U     | 1 1 1 1 0                 | a 1 0 Rm | 0 0 opcode |     1 | Rn  | Rd  |

| U   | a   | opcode   | Instruction Details   | Feature                  |
|-----|-----|----------|-----------------------|--------------------------|
| x   | x   | 00x      | UNALLOCATED           | -                        |
| x   | 0   | 010      | UNALLOCATED           | -                        |
| 0   | x   | 101      | UNALLOCATED           | -                        |
| 0   | 0   | 011      | FMULX                 | FEAT_AdvSIMD &&FEAT_FP16 |
| 0   | 0   | 100      | FCMEQ(register)       | FEAT_AdvSIMD &&FEAT_FP16 |
| 0   | 0   | 110      | UNALLOCATED           | -                        |
| 0   | 0   | 111      | FRECPS                | FEAT_AdvSIMD &&FEAT_FP16 |
| 0   | 1   | x10      | UNALLOCATED           | -                        |
| 0   | 1   | 011      | UNALLOCATED           | -                        |
| 0   | 1   | 100      | UNALLOCATED           | -                        |
| 0   | 1   | 111      | FRSQRTS               | FEAT_AdvSIMD &&FEAT_FP16 |
| 1   | x   | 011      | UNALLOCATED           | -                        |
| 1   | x   | 11x      | UNALLOCATED           | -                        |
| 1   | 0   | 100      | FCMGE(register)       | FEAT_AdvSIMD &&FEAT_FP16 |
| 1   | 0   | 101      | FACGE                 | FEAT_AdvSIMD &&FEAT_FP16 |
| 1   | 1   | 010      | FABD                  | FEAT_AdvSIMD &&FEAT_FP16 |
| 1   | 1   | 100      | FCMGT(register)       | FEAT_AdvSIMD &&FEAT_FP16 |
| 1   | 1   | 101      | FACGT                 | FEAT_AdvSIMD &&FEAT_FP16 |

## Advanced SIMD scalar two-register miscellaneous FP16

The encodings in this section are decoded from Data Processing - Scalar Floating-Point and Advanced SIMD.

<!-- image -->

|   31 | 30 29 28   | 24 23 22 19 18 17 16   | 12 11 10         | 9   | 5   | 0   |
|------|------------|------------------------|------------------|-----|-----|-----|
|    0 | 1 U        | 1 1 1 1 0 a 1          | 1 1 1 0 0 opcode | 1 0 | Rn  | Rd  |

| U   | a   | opcode   | Instruction Details   | Feature   |
|-----|-----|----------|-----------------------|-----------|
| x   | x   | x0xxx    | UNALLOCATED           | -         |

| U   | a   | opcode   | Instruction Details      | Feature                  |
|-----|-----|----------|--------------------------|--------------------------|
| x   | x   | 1100x    | UNALLOCATED              | -                        |
| x   | 0   | 01xxx    | UNALLOCATED              | -                        |
| x   | 1   | 010xx    | UNALLOCATED              | -                        |
| x   | 1   | 11100    | UNALLOCATED              | -                        |
| 0   | 0   | 11010    | FCVTNS (vector)          | FEAT_AdvSIMD &&FEAT_FP16 |
| 0   | 0   | 11011    | FCVTMS(vector)           | FEAT_AdvSIMD &&FEAT_FP16 |
| 0   | 0   | 11100    | FCVTAS (vector)          | FEAT_AdvSIMD &&FEAT_FP16 |
| 0   | 0   | 11101    | SCVTF (vector, integer)  | FEAT_AdvSIMD &&FEAT_FP16 |
| 0   | 0   | 1111x    | UNALLOCATED              | -                        |
| 0   | 1   | 01100    | FCMGT(zero)              | FEAT_AdvSIMD &&FEAT_FP16 |
| 0   | 1   | 01101    | FCMEQ(zero)              | FEAT_AdvSIMD &&FEAT_FP16 |
| 0   | 1   | 01110    | FCMLT (zero)             | FEAT_AdvSIMD &&FEAT_FP16 |
| 0   | 1   | 01111    | UNALLOCATED              | -                        |
| 0   | 1   | 11010    | FCVTPS (vector)          | FEAT_AdvSIMD &&FEAT_FP16 |
| 0   | 1   | 11011    | FCVTZS (vector, integer) | FEAT_AdvSIMD &&FEAT_FP16 |
| 0   | 1   | 11101    | FRECPE                   | FEAT_AdvSIMD &&FEAT_FP16 |
| 0   | 1   | 11110    | UNALLOCATED              | -                        |
| 0   | 1   | 11111    | FRECPX                   | FEAT_AdvSIMD &&FEAT_FP16 |
| 1   | x   | 1111x    | UNALLOCATED              | -                        |
| 1   | 0   | 11010    | FCVTNU(vector)           | FEAT_AdvSIMD &&FEAT_FP16 |
| 1   | 0   | 11011    | FCVTMU(vector)           | FEAT_AdvSIMD &&FEAT_FP16 |
| 1   | 0   | 11100    | FCVTAU (vector)          | FEAT_AdvSIMD &&FEAT_FP16 |
| 1   | 0   | 11101    | UCVTF (vector, integer)  | FEAT_AdvSIMD &&FEAT_FP16 |
| 1   | 1   | 01100    | FCMGE(zero)              | FEAT_AdvSIMD &&FEAT_FP16 |
| 1   | 1   | 01101    | FCMLE(zero)              | FEAT_AdvSIMD &&FEAT_FP16 |
| 1   | 1   | 0111x    | UNALLOCATED              | -                        |
| 1   | 1   | 11010    | FCVTPU (vector)          | FEAT_AdvSIMD &&FEAT_FP16 |
| 1   | 1   | 11011    | FCVTZU (vector, integer) | FEAT_AdvSIMD &&FEAT_FP16 |
| 1   | 1   | 11101    | FRSQRTE                  | FEAT_AdvSIMD &&FEAT_FP16 |

## Advanced SIMD scalar three same extra

The encodings in this section are decoded from Data Processing - Scalar Floating-Point and Advanced SIMD.

<!-- image -->

|   31 | 30 29 28   |   24 23 | 22 21   |      |   20 |   16 15 14 |   11 10 | 5   | 0   |
|------|------------|---------|---------|------|------|------------|---------|-----|-----|
|    0 | 1 U        |       1 | 1 1 1 0 | size |    0 |          1 |       1 | Rn  | Rd  |

|   U | opcode   | Instruction Details   | Feature   |
|-----|----------|-----------------------|-----------|
|   0 | xxxx     | UNALLOCATED           | -         |
|   1 | 0000     | SQRDMLAH(vector)      | FEAT_RDM  |
|   1 | 0001     | SQRDMLSH(vector)      | FEAT_RDM  |
|   1 | 001x     | UNALLOCATED           | -         |
|   1 | 01xx     | UNALLOCATED           | -         |
|   1 | 1xxx     | UNALLOCATED           | -         |

## Advanced SIMD scalar two-register miscellaneous

The encodings in this section are decoded from Data Processing - Scalar Floating-Point and Advanced SIMD.

<!-- image -->

|   31 30 29 | 28 24 23 22 21   | 17 16        | 12 11 10 9   | 5 4    |    |
|------------|------------------|--------------|--------------|--------|----|
|          0 | 1 U 1 1 1 1 0    | size 1 0 0 0 | 0 opcode     | 1 0 Rn | Rd |

| U   | size   | opcode   | Instruction Details     | Feature      |
|-----|--------|----------|-------------------------|--------------|
| x   | xx     | 00xx0    | UNALLOCATED             | -            |
| x   | xx     | 00x01    | UNALLOCATED             | -            |
| x   | xx     | 1x000    | UNALLOCATED             | -            |
| x   | xx     | 10xx1    | UNALLOCATED             | -            |
| x   | xx     | 11001    | UNALLOCATED             | -            |
| x   | 0x     | 01xxx    | UNALLOCATED             | -            |
| x   | 0x     | 1111x    | UNALLOCATED             | -            |
| x   | 1x     | 01111    | UNALLOCATED             | -            |
| x   | 1x     | 11100    | UNALLOCATED             | -            |
| x   | 10     | 010x1    | UNALLOCATED             | -            |
| x   | 10     | 01000    | UNALLOCATED             | -            |
| 0   | xx     | 00011    | SUQADD                  | FEAT_AdvSIMD |
| 0   | xx     | 00111    | SQABS                   | FEAT_AdvSIMD |
| 0   | xx     | 10010    | UNALLOCATED             | -            |
| 0   | xx     | 10100    | SQXTN, SQXTN2           | FEAT_AdvSIMD |
| 0   | xx     | 10110    | UNALLOCATED             | -            |
| 0   | 0x     | 11010    | FCVTNS (vector)         | FEAT_AdvSIMD |
| 0   | 0x     | 11011    | FCVTMS(vector)          | FEAT_AdvSIMD |
| 0   | 0x     | 11100    | FCVTAS (vector)         | FEAT_AdvSIMD |
| 0   | 0x     | 11101    | SCVTF (vector, integer) | FEAT_AdvSIMD |
| 0   | 1x     | 01100    | FCMGT(zero)             | FEAT_AdvSIMD |
| 0   | 1x     | 01101    | FCMEQ(zero)             | FEAT_AdvSIMD |

|   U | size   | opcode   | Instruction Details      | Feature      |
|-----|--------|----------|--------------------------|--------------|
|   0 | 1x     | 01110    | FCMLT (zero)             | FEAT_AdvSIMD |
|   0 | 1x     | 11010    | FCVTPS (vector)          | FEAT_AdvSIMD |
|   0 | 1x     | 11011    | FCVTZS (vector, integer) | FEAT_AdvSIMD |
|   0 | 1x     | 11101    | FRECPE                   | FEAT_AdvSIMD |
|   0 | 1x     | 11110    | UNALLOCATED              | -            |
|   0 | 1x     | 11111    | FRECPX                   | FEAT_AdvSIMD |
|   0 | 10     | 01010    | UNALLOCATED              | -            |
|   0 | 11     | 01000    | CMGT(zero)               | FEAT_AdvSIMD |
|   0 | 11     | 01001    | CMEQ(zero)               | FEAT_AdvSIMD |
|   0 | 11     | 01010    | CMLT(zero)               | FEAT_AdvSIMD |
|   0 | 11     | 01011    | ABS                      | FEAT_AdvSIMD |
|   1 | xx     | 00011    | USQADD                   | FEAT_AdvSIMD |
|   1 | xx     | 00111    | SQNEG                    | FEAT_AdvSIMD |
|   1 | xx     | 10010    | SQXTUN, SQXTUN2          | FEAT_AdvSIMD |
|   1 | xx     | 10100    | UQXTN,UQXTN2             | FEAT_AdvSIMD |
|   1 | 0x     | 11010    | FCVTNU(vector)           | FEAT_AdvSIMD |
|   1 | 0x     | 11011    | FCVTMU(vector)           | FEAT_AdvSIMD |
|   1 | 0x     | 11100    | FCVTAU (vector)          | FEAT_AdvSIMD |
|   1 | 0x     | 11101    | UCVTF (vector, integer)  | FEAT_AdvSIMD |
|   1 | 00     | 10110    | UNALLOCATED              | -            |
|   1 | 01     | 10110    | FCVTXN, FCVTXN2          | FEAT_AdvSIMD |
|   1 | 1x     | 01x10    | UNALLOCATED              | -            |
|   1 | 1x     | 01100    | FCMGE(zero)              | FEAT_AdvSIMD |
|   1 | 1x     | 01101    | FCMLE(zero)              | FEAT_AdvSIMD |
|   1 | 1x     | 1x110    | UNALLOCATED              | -            |
|   1 | 1x     | 11010    | FCVTPU (vector)          | FEAT_AdvSIMD |
|   1 | 1x     | 11011    | FCVTZU (vector, integer) | FEAT_AdvSIMD |
|   1 | 1x     | 11101    | FRSQRTE                  | FEAT_AdvSIMD |
|   1 | 1x     | 11111    | UNALLOCATED              | -            |
|   1 | 11     | 01000    | CMGE(zero)               | FEAT_AdvSIMD |
|   1 | 11     | 01001    | CMLE(zero)               | FEAT_AdvSIMD |
|   1 | 11     | 01011    | NEG(vector)              | FEAT_AdvSIMD |

## Advanced SIMD scalar pairwise

The encodings in this section are decoded from Data Processing - Scalar Floating-Point and Advanced SIMD.

<!-- image -->

|   31 | 30 29 28   | 24 23 22       | 17 16 12 11 10     | 5   | 0   |
|------|------------|----------------|--------------------|-----|-----|
|    0 | 1 U        | 1 1 1 1 0 size | 1 0 0 0 opcode 1 0 | Rn  | Rd  |

| U   | size   | opcode   | Instruction Details                                      | Feature                  |
|-----|--------|----------|----------------------------------------------------------|--------------------------|
| x   | xx     | x0xxx    | UNALLOCATED                                              | -                        |
| x   | xx     | 01110    | UNALLOCATED                                              | -                        |
| x   | xx     | 111xx    | UNALLOCATED                                              | -                        |
| x   | 10     | 01101    | UNALLOCATED                                              | -                        |
| 0   | x1     | 011x1    | UNALLOCATED                                              | -                        |
| 0   | x1     | 01100    | UNALLOCATED                                              | -                        |
| 0   | 00     | 01100    | FMAXNMP(scalar) -Half-precision                          | FEAT_AdvSIMD &&FEAT_FP16 |
| 0   | 00     | 01101    | FADDP (scalar) -Half-precision                           | FEAT_AdvSIMD &&FEAT_FP16 |
| 0   | 00     | 01111    | FMAXP(scalar) -Half-precision                            | FEAT_AdvSIMD &&FEAT_FP16 |
| 0   | 10     | 01100    | FMINNMP(scalar) -Half-precision                          | FEAT_AdvSIMD &&FEAT_FP16 |
| 0   | 10     | 01111    | FMINP (scalar) -Half-precision                           | FEAT_AdvSIMD &&FEAT_FP16 |
| 0   | 11     | x100x    | UNALLOCATED                                              | -                        |
| 0   | 11     | x1010    | UNALLOCATED                                              | -                        |
| 0   | 11     | 01011    | UNALLOCATED                                              | -                        |
| 0   | 11     | 11011    | ADDP(scalar)                                             | FEAT_AdvSIMD             |
| 0   | != 11  | x10xx    | UNALLOCATED                                              | -                        |
| 1   | xx     | x10xx    | UNALLOCATED                                              | -                        |
| 1   | 0x     | 01100    | FMAXNMP (scalar) - Single-precision and double-precision | FEAT_AdvSIMD             |
| 1   | 0x     | 01101    | FADDP (scalar) - Single-precision and double-precision   | FEAT_AdvSIMD             |
| 1   | 0x     | 01111    | FMAXP (scalar) - Single-precision and double-precision   | FEAT_AdvSIMD             |
| 1   | 1x     | 01100    | FMINNMP (scalar) - Single-precision and double-precision | FEAT_AdvSIMD             |
| 1   | 1x     | 01111    | FMINP (scalar) - Single-precision and double-precision   | FEAT_AdvSIMD             |
| 1   | 11     | 01101    | UNALLOCATED                                              | -                        |

## Advanced SIMD scalar three different

The encodings in this section are decoded from Data Processing - Scalar Floating-Point and Advanced SIMD.

<!-- image -->

|   31 | 30 29   | 28 24 23 22 21   | 12 11 10          |   20 16 15 |    | 5 4   | 0   |
|------|---------|------------------|-------------------|------------|----|-------|-----|
|    0 | 1 U     | 1 1 1 1          | 0 size opcode 0 0 |          1 | Rm | Rn    | Rd  |

|   U | opcode   | Instruction Details        | Feature      |
|-----|----------|----------------------------|--------------|
|   0 | 0xxx     | UNALLOCATED                | -            |
|   0 | 1xx0     | UNALLOCATED                | -            |
|   0 | 1001     | SQDMLAL, SQDMLAL2(vector)  | FEAT_AdvSIMD |
|   0 | 1011     | SQDMLSL, SQDMLSL2 (vector) | FEAT_AdvSIMD |
|   0 | 1101     | SQDMULL, SQDMULL2(vector)  | FEAT_AdvSIMD |
|   0 | 1111     | UNALLOCATED                | -            |
|   1 | xxxx     | UNALLOCATED                | -            |

## Advanced SIMD scalar three same

The encodings in this section are decoded from Data Processing - Scalar Floating-Point and Advanced SIMD.

<!-- image -->

| 31 30   | 29 28 24 23 22 21 20   | 16 15   | 11 10 9 5 4   |
|---------|------------------------|---------|---------------|
| 0 1     | U 1 1 1 1 0 size 1 Rm  | opcode  | 1 Rn Rd       |

| U   | size   | opcode   | Instruction Details   | Feature      |
|-----|--------|----------|-----------------------|--------------|
| x   | xx     | x0011    | UNALLOCATED           | -            |
| x   | xx     | 011x1    | UNALLOCATED           | -            |
| x   | xx     | 11001    | UNALLOCATED           | -            |
| x   | xx     | 11110    | UNALLOCATED           | -            |
| x   | x0     | 0x1x0    | UNALLOCATED           | -            |
| x   | x1     | 00100    | UNALLOCATED           | -            |
| x   | x1     | 011x0    | UNALLOCATED           | -            |
| x   | 0x     | xx0x0    | UNALLOCATED           | -            |
| x   | 0x     | 10x01    | UNALLOCATED           | -            |
| x   | 01     | 00110    | UNALLOCATED           | -            |
| x   | 1x     | 10010    | UNALLOCATED           | -            |
| x   | 1x     | 11000    | UNALLOCATED           | -            |
| x   | 10     | 0x0x0    | UNALLOCATED           | -            |
| x   | 10     | 10x0x    | UNALLOCATED           | -            |
| x   | 11     | 00000    | UNALLOCATED           | -            |
| x   | 11     | 00010    | UNALLOCATED           | -            |
| x   | 11     | 10101    | UNALLOCATED           | -            |
| x   | != 10  | 10100    | UNALLOCATED           | -            |
| x   | != 11  | 00111    | UNALLOCATED           | -            |
| 0   | xx     | 00001    | SQADD                 | FEAT_AdvSIMD |
| 0   | xx     | 00101    | SQSUB                 | FEAT_AdvSIMD |

|   U | size   | opcode   | Instruction Details   | Feature      |
|-----|--------|----------|-----------------------|--------------|
|   0 | xx     | 01001    | SQSHL (register)      | FEAT_AdvSIMD |
|   0 | xx     | 01011    | SQRSHL                | FEAT_AdvSIMD |
|   0 | xx     | 10110    | SQDMULH(vector)       | FEAT_AdvSIMD |
|   0 | xx     | 10111    | UNALLOCATED           | -            |
|   0 | xx     | 11101    | UNALLOCATED           | -            |
|   0 | 0x     | 11011    | FMULX                 | FEAT_AdvSIMD |
|   0 | 0x     | 11100    | FCMEQ(register)       | FEAT_AdvSIMD |
|   0 | 0x     | 11111    | FRECPS                | FEAT_AdvSIMD |
|   0 | 1x     | 11010    | UNALLOCATED           | -            |
|   0 | 1x     | 11011    | UNALLOCATED           | -            |
|   0 | 1x     | 11100    | UNALLOCATED           | -            |
|   0 | 1x     | 11111    | FRSQRTS               | FEAT_AdvSIMD |
|   0 | 11     | 00110    | CMGT(register)        | FEAT_AdvSIMD |
|   0 | 11     | 00111    | CMGE(register)        | FEAT_AdvSIMD |
|   0 | 11     | 01000    | SSHL                  | FEAT_AdvSIMD |
|   0 | 11     | 01010    | SRSHL                 | FEAT_AdvSIMD |
|   0 | 11     | 10000    | ADD(vector)           | FEAT_AdvSIMD |
|   0 | 11     | 10001    | CMTST                 | FEAT_AdvSIMD |
|   1 | xx     | 00001    | UQADD                 | FEAT_AdvSIMD |
|   1 | xx     | 00101    | UQSUB                 | FEAT_AdvSIMD |
|   1 | xx     | 01001    | UQSHL(register)       | FEAT_AdvSIMD |
|   1 | xx     | 01011    | UQRSHL                | FEAT_AdvSIMD |
|   1 | xx     | 1x111    | UNALLOCATED           | -            |
|   1 | xx     | 10110    | SQRDMULH(vector)      | FEAT_AdvSIMD |
|   1 | xx     | 11011    | UNALLOCATED           | -            |
|   1 | 0x     | 11100    | FCMGE(register)       | FEAT_AdvSIMD |
|   1 | 0x     | 11101    | FACGE                 | FEAT_AdvSIMD |
|   1 | 1x     | 11010    | FABD                  | FEAT_AdvSIMD |
|   1 | 1x     | 11100    | FCMGT(register)       | FEAT_AdvSIMD |
|   1 | 1x     | 11101    | FACGT                 | FEAT_AdvSIMD |
|   1 | 11     | 00110    | CMHI (register)       | FEAT_AdvSIMD |
|   1 | 11     | 00111    | CMHS(register)        | FEAT_AdvSIMD |
|   1 | 11     | 01000    | USHL                  | FEAT_AdvSIMD |
|   1 | 11     | 01010    | URSHL                 | FEAT_AdvSIMD |
|   1 | 11     | 10000    | SUB (vector)          | FEAT_AdvSIMD |
|   1 | 11     | 10001    | CMEQ(register)        | FEAT_AdvSIMD |

## Advanced SIMD scalar shift by immediate

The encodings in this section are decoded from Data Processing - Scalar Floating-Point and Advanced SIMD.

<!-- image -->

|   31 | 30 29 28   | 25 24 23 22 19 18   | 16 15     | 11     |   10 | 5   | 0   |
|------|------------|---------------------|-----------|--------|------|-----|-----|
|    0 | 1 U        | 1 1 1 1 1 0         | immh immb | opcode |    1 | Rn  | Rd  |

| U   | immh    | opcode   | Instruction Details          | Feature      |
|-----|---------|----------|------------------------------|--------------|
| x   | xxxx    | 0xxx1    | UNALLOCATED                  | -            |
| x   | xxxx    | 101xx    | UNALLOCATED                  | -            |
| x   | xxxx    | 11101    | UNALLOCATED                  | -            |
| x   | 0xxx    | x10x0    | UNALLOCATED                  | -            |
| x   | 0xxx    | 00xx0    | UNALLOCATED                  | -            |
| x   | 0xxx    | 110x1    | UNALLOCATED                  | -            |
| x   | 0000    | x1110    | UNALLOCATED                  | -            |
| x   | 0000    | 1001x    | UNALLOCATED                  | -            |
| x   | 0000    | 11100    | UNALLOCATED                  | -            |
| x   | 0000    | 11111    | UNALLOCATED                  | -            |
| x   | 1xxx    | 110xx    | UNALLOCATED                  | -            |
| x   | != 0000 | 11110    | UNALLOCATED                  | -            |
| 0   | xxxx    | 01100    | UNALLOCATED                  | -            |
| 0   | xxxx    | 1000x    | UNALLOCATED                  | -            |
| 0   | 1xxx    | 00000    | SSHR                         | FEAT_AdvSIMD |
| 0   | 1xxx    | 00010    | SSRA                         | FEAT_AdvSIMD |
| 0   | 1xxx    | 00100    | SRSHR                        | FEAT_AdvSIMD |
| 0   | 1xxx    | 00110    | SRSRA                        | FEAT_AdvSIMD |
| 0   | 1xxx    | 01000    | UNALLOCATED                  | -            |
| 0   | 1xxx    | 01010    | SHL                          | FEAT_AdvSIMD |
| 0   | != 0000 | 01110    | SQSHL (immediate)            | FEAT_AdvSIMD |
| 0   | != 0000 | 10010    | SQSHRN, SQSHRN2              | FEAT_AdvSIMD |
| 0   | != 0000 | 10011    | SQRSHRN, SQRSHRN2            | FEAT_AdvSIMD |
| 0   | != 0000 | 11100    | SCVTF (vector, fixed-point)  | FEAT_AdvSIMD |
| 0   | != 0000 | 11111    | FCVTZS (vector, fixed-point) | FEAT_AdvSIMD |
| 1   | 0000    | 01100    | UNALLOCATED                  | -            |
| 1   | 0000    | 1000x    | UNALLOCATED                  | -            |
| 1   | 1xxx    | 00000    | USHR                         | FEAT_AdvSIMD |
| 1   | 1xxx    | 00010    | USRA                         | FEAT_AdvSIMD |
| 1   | 1xxx    | 00100    | URSHR                        | FEAT_AdvSIMD |
| 1   | 1xxx    | 00110    | URSRA                        | FEAT_AdvSIMD |
| 1   | 1xxx    | 01000    | SRI                          | FEAT_AdvSIMD |
| 1   | 1xxx    | 01010    | SLI                          | FEAT_AdvSIMD |
| 1   | != 0000 | 01100    | SQSHLU                       | FEAT_AdvSIMD |

|   U | immh    |   opcode | Instruction Details          | Feature      |
|-----|---------|----------|------------------------------|--------------|
|   1 | != 0000 |    01110 | UQSHL(immediate)             | FEAT_AdvSIMD |
|   1 | != 0000 |    10000 | SQSHRUN, SQSHRUN2            | FEAT_AdvSIMD |
|   1 | != 0000 |    10001 | SQRSHRUN, SQRSHRUN2          | FEAT_AdvSIMD |
|   1 | != 0000 |    10010 | UQSHRN, UQSHRN2              | FEAT_AdvSIMD |
|   1 | != 0000 |    10011 | UQRSHRN,UQRSHRN2             | FEAT_AdvSIMD |
|   1 | != 0000 |    11100 | UCVTF (vector, fixed-point)  | FEAT_AdvSIMD |
|   1 | != 0000 |    11111 | FCVTZU (vector, fixed-point) | FEAT_AdvSIMD |

## Advanced SIMD scalar x indexed element

The encodings in this section are decoded from Data Processing - Scalar Floating-Point and Advanced SIMD.

<!-- image -->

| 31 30   | 29 28 21 20 19          | 24 23 22 16 15 12 11 10 9 5 4   |
|---------|-------------------------|---------------------------------|
| 0 1     | U 1 1 1 1 1 size L M Rm | opcode H 0 Rn Rd                |

| U   | size   | opcode   | Instruction Details                                                | Feature                  |
|-----|--------|----------|--------------------------------------------------------------------|--------------------------|
| x   | 01     | 1001     | UNALLOCATED                                                        | -                        |
| 0   | xx     | 0xx0     | UNALLOCATED                                                        | -                        |
| 0   | xx     | 0011     | SQDMLAL, SQDMLAL2(by element)                                      | FEAT_AdvSIMD             |
| 0   | xx     | 0111     | SQDMLSL, SQDMLSL2 (by element)                                     | FEAT_AdvSIMD             |
| 0   | xx     | 10x0     | UNALLOCATED                                                        | -                        |
| 0   | xx     | 1011     | SQDMULL, SQDMULL2(by element)                                      | FEAT_AdvSIMD             |
| 0   | xx     | 1100     | SQDMULH(by element)                                                | FEAT_AdvSIMD             |
| 0   | xx     | 1101     | SQRDMULH(by element)                                               | FEAT_AdvSIMD             |
| 0   | xx     | 111x     | UNALLOCATED                                                        | -                        |
| 0   | 00     | 0001     | FMLA (by element) - Scalar, half- precision                        | FEAT_AdvSIMD &&FEAT_FP16 |
| 0   | 00     | 0101     | FMLS (by element) - Scalar, half- precision                        | FEAT_AdvSIMD &&FEAT_FP16 |
| 0   | 00     | 1001     | FMUL (by element) - Scalar, half- precision                        | FEAT_AdvSIMD &&FEAT_FP16 |
| 0   | 01     | 0x01     | UNALLOCATED                                                        | -                        |
| 0   | 1x     | 0001     | FMLA (by element) - Scalar, single- precision and double-precision | FEAT_AdvSIMD             |
| 0   | 1x     | 0101     | FMLS (by element) - Scalar, single- precision and double-precision | FEAT_AdvSIMD             |
| 0   | 1x     | 1001     | FMUL (by element) - Scalar, single- precision and double-precision | FEAT_AdvSIMD             |
| 1   | xx     | 0xxx     | UNALLOCATED                                                        | -                        |

|   U | size   | opcode   | Instruction Details                                                 | Feature                  |
|-----|--------|----------|---------------------------------------------------------------------|--------------------------|
|   1 | xx     | 1xx0     | UNALLOCATED                                                         | -                        |
|   1 | xx     | 1011     | UNALLOCATED                                                         | -                        |
|   1 | xx     | 1101     | SQRDMLAH(by element)                                                | FEAT_RDM                 |
|   1 | xx     | 1111     | SQRDMLSH(by element)                                                | FEAT_RDM                 |
|   1 | 00     | 1001     | FMULX (by element) - Scalar, half- precision                        | FEAT_AdvSIMD &&FEAT_FP16 |
|   1 | 1x     | 1001     | FMULX (by element) - Scalar, single- precision and double-precision | FEAT_AdvSIMD             |

## Advanced SIMD table lookup

The encodings in this section are decoded from Data Processing - Scalar Floating-Point and Advanced SIMD.

<!-- image -->

|   31 | 30 29   | 24        | 23 22 21   |    | 20            | 5   | 16 15 14 13 12 11 10 9 4   |
|------|---------|-----------|------------|----|---------------|-----|----------------------------|
|    0 | Q 0     | 0 1 1 1 0 | op2        |  0 | Rm 0 len op 0 | Rn  | 0 Rd                       |

| Q   | op2   | len   | op   | Instruction Details        | Feature                 |
|-----|-------|-------|------|----------------------------|-------------------------|
| x   | 00    | 00    | 0    | TBL -Single register table | FEAT_AdvSIMD            |
| x   | 00    | 00    | 1    | TBX-Single register table  | FEAT_AdvSIMD            |
| x   | 00    | 01    | 0    | TBL -Tworegister table     | FEAT_AdvSIMD            |
| x   | 00    | 01    | 1    | TBX-Tworegister table      | FEAT_AdvSIMD            |
| x   | 00    | 10    | 0    | TBL -Three register table  | FEAT_AdvSIMD            |
| x   | 00    | 10    | 1    | TBX-Three register table   | FEAT_AdvSIMD            |
| x   | 00    | 11    | 0    | TBL -Four register table   | FEAT_AdvSIMD            |
| x   | 00    | 11    | 1    | TBX-Fourregister table     | FEAT_AdvSIMD            |
| 0   | != 00 | xx    | x    | UNALLOCATED                | -                       |
| 1   | 01    | xx    | 1    | LUTI4 -Halfword            | FEAT_AdvSIMD &&FEAT_LUT |
| 1   | 01    | x0    | 0    | UNALLOCATED                | -                       |
| 1   | 01    | x1    | 0    | LUTI4 -Byte                | FEAT_AdvSIMD &&FEAT_LUT |
| 1   | 10    | xx    | 0    | UNALLOCATED                | -                       |
| 1   | 10    | xx    | 1    | LUTI2 -Byte                | FEAT_AdvSIMD &&FEAT_LUT |
| 1   | 11    | xx    | x    | LUTI2 -Halfword            | FEAT_AdvSIMD &&FEAT_LUT |

## Advanced SIMD permute

The encodings in this section are decoded from Data Processing - Scalar Floating-Point and Advanced SIMD.

<!-- image -->

| 31 30 29   | 24 23 22 21 20   | 16 15 14 12 11 10 9 5 4   |
|------------|------------------|---------------------------|
| 0 Q 0      | 0 size 0 Rm      | 0 opcode 1 0 Rn Rd        |

| opcode   | Instruction Details   | Feature      |
|----------|-----------------------|--------------|
| x00      | UNALLOCATED           | -            |
| 001      | UZP1                  | FEAT_AdvSIMD |
| 010      | TRN1                  | FEAT_AdvSIMD |
| 011      | ZIP1                  | FEAT_AdvSIMD |
| 101      | UZP2                  | FEAT_AdvSIMD |
| 110      | TRN2                  | FEAT_AdvSIMD |
| 111      | ZIP2                  | FEAT_AdvSIMD |

## Advanced SIMD extract

The encodings in this section are decoded from Data Processing - Scalar Floating-Point and Advanced SIMD.

<!-- image -->

|   31 | 30 29   | 24 23 22 21 20   | 16 15 14   |    | 11 10 9 5 4   |
|------|---------|------------------|------------|----|---------------|
|    0 | Q 1     | 0 1 1 1 0 op2 0  | 0 imm4     | Rn | 0 Rd          |

| op2   | Instruction Details   | Feature      |
|-------|-----------------------|--------------|
| 00    | EXT                   | FEAT_AdvSIMD |
| != 00 | UNALLOCATED           | -            |

## Advanced SIMD copy

The encodings in this section are decoded from Data Processing - Scalar Floating-Point and Advanced SIMD.

<!-- image -->

|   31 | 30 29 28   | 25 24 23 22 21 20   | 16 15 14     |    |   11 10 | 9 5   | 4   | 0   |
|------|------------|---------------------|--------------|----|---------|-------|-----|-----|
|    0 | Q op       | 0 1 1 1             | 0 0 0 imm5 0 |  0 |       1 | imm4  | Rn  | Rd  |

| Q   |   op | imm5   | imm4   | Instruction Details   | Feature      |
|-----|------|--------|--------|-----------------------|--------------|
| x   |    0 | xxxxx  | 0000   | DUP(element)          | FEAT_AdvSIMD |
| x   |    0 | xxxxx  | 0001   | DUP(general)          | FEAT_AdvSIMD |
| x   |    0 | xxxxx  | 01x0   | UNALLOCATED           | -            |
| x   |    0 | xxxxx  | 1xxx   | UNALLOCATED           | -            |
| 0   |    0 | xxxxx  | 001x   | UNALLOCATED           | -            |
| 0   |    0 | xxxxx  | 0101   | SMOV-32-bit           | FEAT_AdvSIMD |
| 0   |    0 | xxxxx  | 0111   | UMOV-32-bit           | FEAT_AdvSIMD |
| 0   |    1 | xxxxx  | xxxx   | UNALLOCATED           | -            |
| 1   |    0 | xxxxx  | 0010   | UNALLOCATED           | -            |
| 1   |    0 | xxxxx  | 0011   | INS (general)         | FEAT_AdvSIMD |
| 1   |    0 | xxxxx  | 0101   | SMOV-64-bit           | FEAT_AdvSIMD |
| 1   |    0 | x0xxx  | 0111   | UNALLOCATED           | -            |
| 1   |    0 | x1000  | 0111   | UMOV-64-bit           | FEAT_AdvSIMD |
| 1   |    0 | x1001  | 0111   | UNALLOCATED           | -            |
| 1   |    0 | x101x  | 0111   | UNALLOCATED           | -            |
| 1   |    0 | x11xx  | 0111   | UNALLOCATED           | -            |
| 1   |    1 | xxxxx  | xxxx   | INS (element)         | FEAT_AdvSIMD |

## Advanced SIMD three same (FP16)

The encodings in this section are decoded from Data Processing - Scalar Floating-Point and Advanced SIMD.

<!-- image -->

|   31 | 30 29 28   |   24 23 22 21 20 | 16 15 14 13   | 11     | 10         |   9 5 | 4   | 0   |
|------|------------|------------------|---------------|--------|------------|-------|-----|-----|
|    0 | Q U        |                0 | 1 1 1 0 a     | 1 0 Rm | 0 0 opcode |     1 | Rn  | Rd  |

|   U |   a |   opcode | Instruction Details   | Feature                  |
|-----|-----|----------|-----------------------|--------------------------|
|   0 |   0 |      000 | FMAXNM(vector)        | FEAT_AdvSIMD &&FEAT_FP16 |
|   0 |   0 |      001 | FMLA(vector)          | FEAT_AdvSIMD &&FEAT_FP16 |
|   0 |   0 |      010 | FADD(vector)          | FEAT_AdvSIMD &&FEAT_FP16 |
|   0 |   0 |      011 | FMULX                 | FEAT_AdvSIMD &&FEAT_FP16 |
|   0 |   0 |      100 | FCMEQ(register)       | FEAT_AdvSIMD &&FEAT_FP16 |
|   0 |   0 |      101 | UNALLOCATED           | -                        |
|   0 |   0 |      110 | FMAX(vector)          | FEAT_AdvSIMD &&FEAT_FP16 |
|   0 |   0 |      111 | FRECPS                | FEAT_AdvSIMD &&FEAT_FP16 |
|   0 |   1 |      000 | FMINNM(vector)        | FEAT_AdvSIMD &&FEAT_FP16 |
|   0 |   1 |      001 | FMLS (vector)         | FEAT_AdvSIMD &&FEAT_FP16 |
|   0 |   1 |      010 | FSUB (vector)         | FEAT_AdvSIMD &&FEAT_FP16 |

|   U | a   | opcode   | Instruction Details   | Feature                     |
|-----|-----|----------|-----------------------|-----------------------------|
|   0 | 1   | 011      | FAMAX                 | FEAT_AdvSIMD&&FEAT_FAMINMAX |
|   0 | 1   | 10x      | UNALLOCATED           | -                           |
|   0 | 1   | 110      | FMIN (vector)         | FEAT_AdvSIMD &&FEAT_FP16    |
|   0 | 1   | 111      | FRSQRTS               | FEAT_AdvSIMD &&FEAT_FP16    |
|   1 | x   | 001      | UNALLOCATED           | -                           |
|   1 | 0   | 000      | FMAXNMP(vector)       | FEAT_AdvSIMD &&FEAT_FP16    |
|   1 | 0   | 010      | FADDP (vector)        | FEAT_AdvSIMD &&FEAT_FP16    |
|   1 | 0   | 011      | FMUL(vector)          | FEAT_AdvSIMD &&FEAT_FP16    |
|   1 | 0   | 100      | FCMGE(register)       | FEAT_AdvSIMD &&FEAT_FP16    |
|   1 | 0   | 101      | FACGE                 | FEAT_AdvSIMD &&FEAT_FP16    |
|   1 | 0   | 110      | FMAXP(vector)         | FEAT_AdvSIMD &&FEAT_FP16    |
|   1 | 0   | 111      | FDIV (vector)         | FEAT_AdvSIMD &&FEAT_FP16    |
|   1 | 1   | 000      | FMINNMP(vector)       | FEAT_AdvSIMD &&FEAT_FP16    |
|   1 | 1   | 010      | FABD                  | FEAT_AdvSIMD &&FEAT_FP16    |
|   1 | 1   | 011      | FAMIN                 | FEAT_AdvSIMD&&FEAT_FAMINMAX |
|   1 | 1   | 100      | FCMGT(register)       | FEAT_AdvSIMD &&FEAT_FP16    |
|   1 | 1   | 101      | FACGT                 | FEAT_AdvSIMD &&FEAT_FP16    |
|   1 | 1   | 110      | FMINP (vector)        | FEAT_AdvSIMD &&FEAT_FP16    |
|   1 | 1   | 111      | FSCALE                | FEAT_FP8                    |

## Advanced SIMD two-register miscellaneous (FP16)

The encodings in this section are decoded from Data Processing - Scalar Floating-Point and Advanced SIMD.

<!-- image -->

|   31 | 30 29   | 28   | 24 23 22   | 19 18 17   | 16 12 11         | 10 9 5   | 4   |    |
|------|---------|------|------------|------------|------------------|----------|-----|----|
|    0 | Q       | U    | 0 1 1 1 0  | a 1        | 1 1 1 0 0 opcode | 1 0      | Rn  | Rd |

| U   | a   | opcode   | Instruction Details   | Feature                  |
|-----|-----|----------|-----------------------|--------------------------|
| x   | x   | x0xxx    | UNALLOCATED           | -                        |
| x   | 0   | 01xxx    | UNALLOCATED           | -                        |
| x   | 0   | 1111x    | UNALLOCATED           | -                        |
| x   | 1   | 010xx    | UNALLOCATED           | -                        |
| x   | 1   | 11100    | UNALLOCATED           | -                        |
| 0   | 0   | 11000    | FRINTN (vector)       | FEAT_AdvSIMD &&FEAT_FP16 |
| 0   | 0   | 11001    | FRINTM (vector)       | FEAT_AdvSIMD &&FEAT_FP16 |
| 0   | 0   | 11010    | FCVTNS (vector)       | FEAT_AdvSIMD &&FEAT_FP16 |
| 0   | 0   | 11011    | FCVTMS(vector)        | FEAT_AdvSIMD &&FEAT_FP16 |

|   U |   a | opcode   | Instruction Details      | Feature                  |
|-----|-----|----------|--------------------------|--------------------------|
|   0 |   0 | 11100    | FCVTAS (vector)          | FEAT_AdvSIMD &&FEAT_FP16 |
|   0 |   0 | 11101    | SCVTF (vector, integer)  | FEAT_AdvSIMD &&FEAT_FP16 |
|   0 |   1 | 01100    | FCMGT(zero)              | FEAT_AdvSIMD &&FEAT_FP16 |
|   0 |   1 | 01101    | FCMEQ(zero)              | FEAT_AdvSIMD &&FEAT_FP16 |
|   0 |   1 | 01110    | FCMLT (zero)             | FEAT_AdvSIMD &&FEAT_FP16 |
|   0 |   1 | 01111    | FABS (vector)            | FEAT_AdvSIMD &&FEAT_FP16 |
|   0 |   1 | 11000    | FRINTP (vector)          | FEAT_AdvSIMD &&FEAT_FP16 |
|   0 |   1 | 11001    | FRINTZ (vector)          | FEAT_AdvSIMD &&FEAT_FP16 |
|   0 |   1 | 11010    | FCVTPS (vector)          | FEAT_AdvSIMD &&FEAT_FP16 |
|   0 |   1 | 11011    | FCVTZS (vector, integer) | FEAT_AdvSIMD &&FEAT_FP16 |
|   0 |   1 | 11101    | FRECPE                   | FEAT_AdvSIMD &&FEAT_FP16 |
|   0 |   1 | 1111x    | UNALLOCATED              | -                        |
|   1 |   0 | 11000    | FRINTA (vector)          | FEAT_AdvSIMD &&FEAT_FP16 |
|   1 |   0 | 11001    | FRINTX (vector)          | FEAT_AdvSIMD &&FEAT_FP16 |
|   1 |   0 | 11010    | FCVTNU(vector)           | FEAT_AdvSIMD &&FEAT_FP16 |
|   1 |   0 | 11011    | FCVTMU(vector)           | FEAT_AdvSIMD &&FEAT_FP16 |
|   1 |   0 | 11100    | FCVTAU (vector)          | FEAT_AdvSIMD &&FEAT_FP16 |
|   1 |   0 | 11101    | UCVTF (vector, integer)  | FEAT_AdvSIMD &&FEAT_FP16 |
|   1 |   1 | x1110    | UNALLOCATED              | -                        |
|   1 |   1 | 01100    | FCMGE(zero)              | FEAT_AdvSIMD &&FEAT_FP16 |
|   1 |   1 | 01101    | FCMLE(zero)              | FEAT_AdvSIMD &&FEAT_FP16 |
|   1 |   1 | 01111    | FNEG (vector)            | FEAT_AdvSIMD &&FEAT_FP16 |
|   1 |   1 | 11000    | UNALLOCATED              | -                        |
|   1 |   1 | 11001    | FRINTI (vector)          | FEAT_AdvSIMD &&FEAT_FP16 |
|   1 |   1 | 11010    | FCVTPU (vector)          | FEAT_AdvSIMD &&FEAT_FP16 |
|   1 |   1 | 11011    | FCVTZU (vector, integer) | FEAT_AdvSIMD &&FEAT_FP16 |
|   1 |   1 | 11101    | FRSQRTE                  | FEAT_AdvSIMD &&FEAT_FP16 |
|   1 |   1 | 11111    | FSQRT (vector)           | FEAT_AdvSIMD &&FEAT_FP16 |

## Advanced SIMD three-register extension

The encodings in this section are decoded from Data Processing - Scalar Floating-Point and Advanced SIMD.

<!-- image -->

|   31 | 30   | 29 28   | 24    |    | 23   |   22 21 | 20   | 16   |   15 | 14     |   11 10 | 5   |    |
|------|------|---------|-------|----|------|---------|------|------|------|--------|---------|-----|----|
|    0 | Q    | U 0     | 1 1 1 |  0 | size |       0 |      | Rm   |    1 | opcode |       1 | Rn  | Rd |

| Q   | U   | size   | opcode   | Instruction Details                                       | Feature      |
|-----|-----|--------|----------|-----------------------------------------------------------|--------------|
| x   | 0   | xx     | 0000     | UNALLOCATED                                               | -            |
| x   | 0   | xx     | 0010     | SDOT (vector)                                             | FEAT_DotProd |
| x   | 0   | 0x     | 1010     | UNALLOCATED                                               | -            |
| x   | 0   | 0x     | 1100     | UNALLOCATED                                               | -            |
| x   | 0   | 00     | 1110     | FCVTN, FCVTN2 (single-precision to 8- bit floating-point) | FEAT_FP8     |
| x   | 0   | 00     | 1111     | FDOT (8-bit floating-point to single- precision, vector)  | FEAT_FP8DOT4 |
| x   | 0   | 01     | 1110     | FCVTN (half-precision to 8-bit floating- point)           | FEAT_FP8     |
| x   | 0   | 01     | 1111     | FDOT (8-bit floating-point to half- precision, vector)    | FEAT_FP8DOT2 |
| x   | 0   | 10     | 0001     | UNALLOCATED                                               | -            |
| x   | 0   | 10     | 0011     | USDOT(vector)                                             | FEAT_I8MM    |
| x   | 0   | 10     | 1xx0     | UNALLOCATED                                               | -            |
| x   | 0   | 10     | 1x11     | UNALLOCATED                                               | -            |
| x   | 0   | 10     | 1001     | UNALLOCATED                                               | -            |
| x   | 0   | 11     | 1xx0     | UNALLOCATED                                               | -            |
| x   | 0   | != 10  | x0x1     | UNALLOCATED                                               | -            |
| x   | 1   | xx     | 0000     | SQRDMLAH(vector)                                          | FEAT_RDM     |
| x   | 1   | xx     | 0001     | SQRDMLSH(vector)                                          | FEAT_RDM     |
| x   | 1   | xx     | 0010     | UDOT(vector)                                              | FEAT_DotProd |
| x   | 1   | xx     | 0011     | UNALLOCATED                                               | -            |
| x   | 1   | xx     | 10xx     | FCMLA                                                     | FEAT_FCMA    |
| x   | 1   | xx     | 11x0     | FCADD                                                     | FEAT_FCMA    |
| x   | 1   | x0     | 1111     | UNALLOCATED                                               | -            |
| x   | 1   | 01     | 1111     | BFDOT (vector)                                            | FEAT_BF16    |
| x   | 1   | 11     | 1111     | BFMLALB, BFMLALT (vector)                                 | FEAT_BF16    |
| 0   | x   | xx     | 01xx     | UNALLOCATED                                               | -            |
| 0   | x   | xx     | 1101     | UNALLOCATED                                               | -            |
| 0   | 0   | 00     | 1000     | FMLALLBB, FMLALLBT, FMLALLTB, FMLALLTT (vector)-FMLALLBB  | FEAT_FP8FMA  |
| 0   | 0   | 01     | 1000     | FMLALLBB, FMLALLBT, FMLALLTB, FMLALLTT (vector)-FMLALLBT  | FEAT_FP8FMA  |
| 0   | 0   | 11     | 1111     | FMLALB, FMLALT (vector) - FMLALB                          | FEAT_FP8FMA  |
| 1   | x   | 10     | 011x     | UNALLOCATED                                               | -            |
| 1   | x   | != 10  | 01xx     | UNALLOCATED                                               | -            |
| 1   | 0   | 00     | 1000     | FMLALLBB, FMLALLBT, FMLALLTB, FMLALLTT (vector)-FMLALLTB  | FEAT_FP8FMA  |
| 1   | 0   | 01     | 1000     | FMLALLBB, FMLALLBT, FMLALLTB, FMLALLTT (vector)-FMLALLTT  | FEAT_FP8FMA  |
| 1   | 0   | 10     | 0100     | SMMLA(vector)                                             | FEAT_I8MM    |

|   Q |   U | size   |   opcode | Instruction Details                                       | Feature      |
|-----|-----|--------|----------|-----------------------------------------------------------|--------------|
|   1 |   0 | 10     |     0101 | USMMLA(vector)                                            | FEAT_I8MM    |
|   1 |   0 | 11     |     1101 | UNALLOCATED                                               | -            |
|   1 |   0 | 11     |     1111 | FMLALB,FMLALT(vector)-FMLALT                              | FEAT_FP8FMA  |
|   1 |   0 | != 11  |     1101 | UNALLOCATED                                               | -            |
|   1 |   1 | 00     |     1101 | FMMLA(widening, 8-bit floating-point to half-precision)   | FEAT_F8F16MM |
|   1 |   1 | 01     |     1101 | BFMMLA(widening)                                          | FEAT_BF16    |
|   1 |   1 | 10     |     0100 | UMMLA(vector)                                             | FEAT_I8MM    |
|   1 |   1 | 10     |     0101 | UNALLOCATED                                               | -            |
|   1 |   1 | 10     |     1101 | FMMLA(widening, 8-bit floating-point to single-precision) | FEAT_F8F32MM |
|   1 |   1 | 11     |     1101 | UNALLOCATED                                               | -            |

## Advanced SIMD two-register miscellaneous

The encodings in this section are decoded from Data Processing - Scalar Floating-Point and Advanced SIMD.

<!-- image -->

| 31 30 29   | 28 24 23 22    | 12 11 10   | 5 4   |    |
|------------|----------------|------------|-------|----|
| 0 Q U      | 0 1 1 1 0 size | opcode 1 0 | Rn    | Rd |

| U   | size   | opcode   | Instruction Details   | Feature      |
|-----|--------|----------|-----------------------|--------------|
| x   | xx     | 1000x    | UNALLOCATED           | -            |
| x   | xx     | 10101    | UNALLOCATED           | -            |
| x   | 0x     | 011xx    | UNALLOCATED           | -            |
| x   | 10     | 11110    | UNALLOCATED           | -            |
| x   | 11     | 1x110    | UNALLOCATED           | -            |
| 0   | xx     | 00000    | REV64                 | FEAT_AdvSIMD |
| 0   | xx     | 00001    | REV16 (vector)        | FEAT_AdvSIMD |
| 0   | xx     | 00010    | SADDLP                | FEAT_AdvSIMD |
| 0   | xx     | 00011    | SUQADD                | FEAT_AdvSIMD |
| 0   | xx     | 00100    | CLS (vector)          | FEAT_AdvSIMD |
| 0   | xx     | 00101    | CNT                   | FEAT_AdvSIMD |
| 0   | xx     | 00110    | SADALP                | FEAT_AdvSIMD |
| 0   | xx     | 00111    | SQABS                 | FEAT_AdvSIMD |
| 0   | xx     | 01000    | CMGT(zero)            | FEAT_AdvSIMD |
| 0   | xx     | 01001    | CMEQ(zero)            | FEAT_AdvSIMD |
| 0   | xx     | 01010    | CMLT(zero)            | FEAT_AdvSIMD |

|   U | size   | opcode   | Instruction Details                                                   | Feature      |
|-----|--------|----------|-----------------------------------------------------------------------|--------------|
|   0 | xx     | 01011    | ABS                                                                   | FEAT_AdvSIMD |
|   0 | xx     | 10010    | XTN, XTN2                                                             | FEAT_AdvSIMD |
|   0 | xx     | 10011    | UNALLOCATED                                                           | -            |
|   0 | xx     | 10100    | SQXTN, SQXTN2                                                         | FEAT_AdvSIMD |
|   0 | 0x     | 10110    | FCVTN, FCVTN2 (double to single- precision, single to half-precision) | FEAT_AdvSIMD |
|   0 | 0x     | 10111    | FCVTL, FCVTL2                                                         | FEAT_AdvSIMD |
|   0 | 0x     | 11000    | FRINTN (vector)                                                       | FEAT_AdvSIMD |
|   0 | 0x     | 11001    | FRINTM (vector)                                                       | FEAT_AdvSIMD |
|   0 | 0x     | 11010    | FCVTNS (vector)                                                       | FEAT_AdvSIMD |
|   0 | 0x     | 11011    | FCVTMS(vector)                                                        | FEAT_AdvSIMD |
|   0 | 0x     | 11100    | FCVTAS (vector)                                                       | FEAT_AdvSIMD |
|   0 | 0x     | 11101    | SCVTF (vector, integer)                                               | FEAT_AdvSIMD |
|   0 | 0x     | 11110    | FRINT32Z (vector)                                                     | FEAT_FRINTTS |
|   0 | 0x     | 11111    | FRINT64Z (vector)                                                     | FEAT_FRINTTS |
|   0 | 1x     | 01100    | FCMGT(zero)                                                           | FEAT_AdvSIMD |
|   0 | 1x     | 01101    | FCMEQ(zero)                                                           | FEAT_AdvSIMD |
|   0 | 1x     | 01110    | FCMLT (zero)                                                          | FEAT_AdvSIMD |
|   0 | 1x     | 01111    | FABS (vector)                                                         | FEAT_AdvSIMD |
|   0 | 1x     | 1x111    | UNALLOCATED                                                           | -            |
|   0 | 1x     | 11000    | FRINTP (vector)                                                       | FEAT_AdvSIMD |
|   0 | 1x     | 11001    | FRINTZ (vector)                                                       | FEAT_AdvSIMD |
|   0 | 1x     | 11010    | FCVTPS (vector)                                                       | FEAT_AdvSIMD |
|   0 | 1x     | 11011    | FCVTZS (vector, integer)                                              | FEAT_AdvSIMD |
|   0 | 1x     | 11100    | URECPE                                                                | FEAT_AdvSIMD |
|   0 | 1x     | 11101    | FRECPE                                                                | FEAT_AdvSIMD |
|   0 | 10     | 10110    | BFCVTN, BFCVTN2                                                       | FEAT_BF16    |
|   1 | xx     | 00000    | REV32 (vector)                                                        | FEAT_AdvSIMD |
|   1 | xx     | 00010    | UADDLP                                                                | FEAT_AdvSIMD |
|   1 | xx     | 00011    | USQADD                                                                | FEAT_AdvSIMD |
|   1 | xx     | 00100    | CLZ (vector)                                                          | FEAT_AdvSIMD |
|   1 | xx     | 00110    | UADALP                                                                | FEAT_AdvSIMD |
|   1 | xx     | 00111    | SQNEG                                                                 | FEAT_AdvSIMD |
|   1 | xx     | 01000    | CMGE(zero)                                                            | FEAT_AdvSIMD |
|   1 | xx     | 01001    | CMLE(zero)                                                            | FEAT_AdvSIMD |
|   1 | xx     | 01010    | UNALLOCATED                                                           | -            |
|   1 | xx     | 01011    | NEG(vector)                                                           | FEAT_AdvSIMD |
|   1 | xx     | 10010    | SQXTUN, SQXTUN2                                                       | FEAT_AdvSIMD |
|   1 | xx     | 10011    | SHLL, SHLL2                                                           | FEAT_AdvSIMD |
|   1 | x0     | 10110    | UNALLOCATED                                                           | -            |

|   U | size   | opcode   | Instruction Details                              | Feature      |
|-----|--------|----------|--------------------------------------------------|--------------|
|   1 | 0x     | 00001    | UNALLOCATED                                      | -            |
|   1 | 0x     | 11000    | FRINTA (vector)                                  | FEAT_AdvSIMD |
|   1 | 0x     | 11001    | FRINTX (vector)                                  | FEAT_AdvSIMD |
|   1 | 0x     | 11010    | FCVTNU(vector)                                   | FEAT_AdvSIMD |
|   1 | 0x     | 11011    | FCVTMU(vector)                                   | FEAT_AdvSIMD |
|   1 | 0x     | 11100    | FCVTAU (vector)                                  | FEAT_AdvSIMD |
|   1 | 0x     | 11101    | UCVTF (vector, integer)                          | FEAT_AdvSIMD |
|   1 | 0x     | 11110    | FRINT32X (vector)                                | FEAT_FRINTTS |
|   1 | 0x     | 11111    | FRINT64X (vector)                                | FEAT_FRINTTS |
|   1 | 00     | 00101    | NOT                                              | FEAT_AdvSIMD |
|   1 | 00     | 10111    | F1CVTL, F1CVTL2, F2CVTL, F2CVTL2 -F1CVTL{2}      | FEAT_FP8     |
|   1 | 01     | 00101    | RBIT (vector)                                    | FEAT_AdvSIMD |
|   1 | 01     | 10110    | FCVTXN, FCVTXN2                                  | FEAT_AdvSIMD |
|   1 | 01     | 10111    | F1CVTL, F1CVTL2, F2CVTL, F2CVTL2 -F2CVTL{2}      | FEAT_FP8     |
|   1 | 1x     | 00x01    | UNALLOCATED                                      | -            |
|   1 | 1x     | 01100    | FCMGE(zero)                                      | FEAT_AdvSIMD |
|   1 | 1x     | 01101    | FCMLE(zero)                                      | FEAT_AdvSIMD |
|   1 | 1x     | 01110    | UNALLOCATED                                      | -            |
|   1 | 1x     | 01111    | FNEG (vector)                                    | FEAT_AdvSIMD |
|   1 | 1x     | 11000    | UNALLOCATED                                      | -            |
|   1 | 1x     | 11001    | FRINTI (vector)                                  | FEAT_AdvSIMD |
|   1 | 1x     | 11010    | FCVTPU (vector)                                  | FEAT_AdvSIMD |
|   1 | 1x     | 11011    | FCVTZU (vector, integer)                         | FEAT_AdvSIMD |
|   1 | 1x     | 11100    | URSQRTE                                          | FEAT_AdvSIMD |
|   1 | 1x     | 11101    | FRSQRTE                                          | FEAT_AdvSIMD |
|   1 | 1x     | 11111    | FSQRT (vector)                                   | FEAT_AdvSIMD |
|   1 | 10     | 10111    | BF1CVTL, BF1CVTL2, BF2CVTL, BF2CVTL2 -BF1CVTL{2} | FEAT_FP8     |
|   1 | 11     | 10111    | BF1CVTL, BF1CVTL2, BF2CVTL, BF2CVTL2 -BF2CVTL{2} | FEAT_FP8     |

## Advanced SIMD across lanes

The encodings in this section are decoded from Data Processing - Scalar Floating-Point and Advanced SIMD.

<!-- image -->

|   31 | 30 29   | 28 24 23   | 22 21 16    | 17 12 11 10 9   | 5   | 4   | 0   |
|------|---------|------------|-------------|-----------------|-----|-----|-----|
|    0 | Q U     | 0 1        | 1 1 0 1 1 0 | size 0 0 opcode | 1 0 | Rn  | Rd  |

| Q   | U   | size   | opcode   | Instruction Details      | Feature                  |
|-----|-----|--------|----------|--------------------------|--------------------------|
| x   | x   | xx     | x100x    | UNALLOCATED              | -                        |
| x   | x   | xx     | 000x0    | UNALLOCATED              | -                        |
| x   | x   | xx     | 00001    | UNALLOCATED              | -                        |
| x   | x   | xx     | 01011    | UNALLOCATED              | -                        |
| x   | x   | xx     | 100xx    | UNALLOCATED              | -                        |
| x   | x   | x0     | 001xx    | UNALLOCATED              | -                        |
| x   | x   | x0     | 01101    | UNALLOCATED              | -                        |
| x   | x   | x0     | 101xx    | UNALLOCATED              | -                        |
| x   | x   | x0     | 111xx    | UNALLOCATED              | -                        |
| x   | x   | x1     | xx1xx    | UNALLOCATED              | -                        |
| x   | 0   | xx     | 00011    | SADDLV                   | FEAT_AdvSIMD             |
| x   | 0   | xx     | 01010    | SMAXV                    | FEAT_AdvSIMD             |
| x   | 0   | xx     | 11010    | SMINV                    | FEAT_AdvSIMD             |
| x   | 0   | xx     | 11011    | ADDV                     | FEAT_AdvSIMD             |
| x   | 0   | x0     | 01110    | UNALLOCATED              | -                        |
| x   | 0   | 00     | 01100    | FMAXNMV-Half-precision   | FEAT_AdvSIMD &&FEAT_FP16 |
| x   | 0   | 00     | 01111    | FMAXV-Half-precision     | FEAT_AdvSIMD &&FEAT_FP16 |
| x   | 0   | 10     | 01100    | FMINNMV-Half-precision   | FEAT_AdvSIMD &&FEAT_FP16 |
| x   | 0   | 10     | 01111    | FMINV -Half-precision    | FEAT_AdvSIMD &&FEAT_FP16 |
| x   | 1   | xx     | 00011    | UADDLV                   | FEAT_AdvSIMD             |
| x   | 1   | xx     | 01010    | UMAXV                    | FEAT_AdvSIMD             |
| x   | 1   | xx     | 11010    | UMINV                    | FEAT_AdvSIMD             |
| x   | 1   | xx     | 11011    | UNALLOCATED              | -                        |
| 0   | 1   | x0     | 011x0    | UNALLOCATED              | -                        |
| 0   | 1   | x0     | 01111    | UNALLOCATED              | -                        |
| 1   | 1   | x0     | 01110    | UNALLOCATED              | -                        |
| 1   | 1   | 00     | 01100    | FMAXNMV-Single-precision | FEAT_AdvSIMD             |
| 1   | 1   | 00     | 01111    | FMAXV-Single-precision   | FEAT_AdvSIMD             |
| 1   | 1   | 10     | 01100    | FMINNMV-Single-precision | FEAT_AdvSIMD             |
| 1   | 1   | 10     | 01111    | FMINV -Single-precision  | FEAT_AdvSIMD             |

## Advanced SIMD three different

The encodings in this section are decoded from Data Processing - Scalar Floating-Point and Advanced SIMD.

<!-- image -->

|   31 | 30 29   | 24   | 28 20 16 15   | 23 22 21   |    | 12 11 10   | 5 4   |    |
|------|---------|------|---------------|------------|----|------------|-------|----|
|    0 | Q U     |      | 0 1 1 1 0 Rm  | size       |  1 | 0 0        | Rn    | Rd |

## Advanced SIMD three same

The encodings in this section are decoded from Data Processing - Scalar Floating-Point and Advanced SIMD.

<!-- image -->

|   31 | 30 29   |   28 | 24   | 23 22   |   21 | 20   | 16   |        |   11 10 | 5   | 4   |
|------|---------|------|------|---------|------|------|------|--------|---------|-----|-----|
|    0 | Q U     |    0 | 1 0  | size    |    1 | Rm   |      | opcode |       1 | Rn  | Rd  |

|   U | opcode   | Instruction Details        | Feature      |
|-----|----------|----------------------------|--------------|
|   0 | 0000     | SADDL, SADDL2              | FEAT_AdvSIMD |
|   0 | 0001     | SADDW,SADDW2               | FEAT_AdvSIMD |
|   0 | 0010     | SSUBL, SSUBL2              | FEAT_AdvSIMD |
|   0 | 0011     | SSUBW, SSUBW2              | FEAT_AdvSIMD |
|   0 | 0100     | ADDHN,ADDHN2               | FEAT_AdvSIMD |
|   0 | 0101     | SABAL, SABAL2              | FEAT_AdvSIMD |
|   0 | 0110     | SUBHN, SUBHN2              | FEAT_AdvSIMD |
|   0 | 0111     | SABDL, SABDL2              | FEAT_AdvSIMD |
|   0 | 1000     | SMLAL, SMLAL2 (vector)     | FEAT_AdvSIMD |
|   0 | 1001     | SQDMLAL, SQDMLAL2(vector)  | FEAT_AdvSIMD |
|   0 | 1010     | SMLSL, SMLSL2 (vector)     | FEAT_AdvSIMD |
|   0 | 1011     | SQDMLSL, SQDMLSL2 (vector) | FEAT_AdvSIMD |
|   0 | 1100     | SMULL, SMULL2 (vector)     | FEAT_AdvSIMD |
|   0 | 1101     | SQDMULL, SQDMULL2(vector)  | FEAT_AdvSIMD |
|   0 | 1110     | PMULL, PMULL2              | FEAT_AdvSIMD |
|   0 | 1111     | UNALLOCATED                | -            |
|   1 | 0000     | UADDL,UADDL2               | FEAT_AdvSIMD |
|   1 | 0001     | UADDW,UADDW2               | FEAT_AdvSIMD |
|   1 | 0010     | USUBL, USUBL2              | FEAT_AdvSIMD |
|   1 | 0011     | USUBW,USUBW2               | FEAT_AdvSIMD |
|   1 | 0100     | RADDHN,RADDHN2             | FEAT_AdvSIMD |
|   1 | 0101     | UABAL, UABAL2              | FEAT_AdvSIMD |
|   1 | 0110     | RSUBHN, RSUBHN2            | FEAT_AdvSIMD |
|   1 | 0111     | UABDL, UABDL2              | FEAT_AdvSIMD |
|   1 | 1xx1     | UNALLOCATED                | -            |
|   1 | 1000     | UMLAL, UMLAL2(vector)      | FEAT_AdvSIMD |
|   1 | 1010     | UMLSL, UMLSL2 (vector)     | FEAT_AdvSIMD |
|   1 | 1100     | UMULL, UMULL2(vector)      | FEAT_AdvSIMD |
|   1 | 1110     | UNALLOCATED                | -            |

|   U | size   |   opcode | Instruction Details          | Feature      |
|-----|--------|----------|------------------------------|--------------|
|   0 | xx     |    00000 | SHADD                        | FEAT_AdvSIMD |
|   0 | xx     |    00001 | SQADD                        | FEAT_AdvSIMD |
|   0 | xx     |    00010 | SRHADD                       | FEAT_AdvSIMD |
|   0 | xx     |    00100 | SHSUB                        | FEAT_AdvSIMD |
|   0 | xx     |    00101 | SQSUB                        | FEAT_AdvSIMD |
|   0 | xx     |    00110 | CMGT(register)               | FEAT_AdvSIMD |
|   0 | xx     |    00111 | CMGE(register)               | FEAT_AdvSIMD |
|   0 | xx     |    01000 | SSHL                         | FEAT_AdvSIMD |
|   0 | xx     |    01001 | SQSHL (register)             | FEAT_AdvSIMD |
|   0 | xx     |    01010 | SRSHL                        | FEAT_AdvSIMD |
|   0 | xx     |    01011 | SQRSHL                       | FEAT_AdvSIMD |
|   0 | xx     |    01100 | SMAX                         | FEAT_AdvSIMD |
|   0 | xx     |    01101 | SMIN                         | FEAT_AdvSIMD |
|   0 | xx     |    01110 | SABD                         | FEAT_AdvSIMD |
|   0 | xx     |    01111 | SABA                         | FEAT_AdvSIMD |
|   0 | xx     |    10000 | ADD(vector)                  | FEAT_AdvSIMD |
|   0 | xx     |    10001 | CMTST                        | FEAT_AdvSIMD |
|   0 | xx     |    10010 | MLA(vector)                  | FEAT_AdvSIMD |
|   0 | xx     |    10011 | MUL(vector)                  | FEAT_AdvSIMD |
|   0 | xx     |    10100 | SMAXP                        | FEAT_AdvSIMD |
|   0 | xx     |    10101 | SMINP                        | FEAT_AdvSIMD |
|   0 | xx     |    10110 | SQDMULH(vector)              | FEAT_AdvSIMD |
|   0 | xx     |    10111 | ADDP(vector)                 | FEAT_AdvSIMD |
|   0 | x1     |    11101 | UNALLOCATED                  | -            |
|   0 | 0x     |    11000 | FMAXNM(vector)               | FEAT_AdvSIMD |
|   0 | 0x     |    11001 | FMLA(vector)                 | FEAT_AdvSIMD |
|   0 | 0x     |    11010 | FADD(vector)                 | FEAT_AdvSIMD |
|   0 | 0x     |    11011 | FMULX                        | FEAT_AdvSIMD |
|   0 | 0x     |    11100 | FCMEQ(register)              | FEAT_AdvSIMD |
|   0 | 0x     |    11110 | FMAX(vector)                 | FEAT_AdvSIMD |
|   0 | 0x     |    11111 | FRECPS                       | FEAT_AdvSIMD |
|   0 | 00     |    00011 | AND(vector)                  | FEAT_AdvSIMD |
|   0 | 00     |    11101 | FMLAL, FMLAL2 (vector)-FMLAL | FEAT_FHM     |
|   0 | 01     |    00011 | BIC (vector, register)       | FEAT_AdvSIMD |
|   0 | 1x     |    11000 | FMINNM(vector)               | FEAT_AdvSIMD |
|   0 | 1x     |    11001 | FMLS (vector)                | FEAT_AdvSIMD |
|   0 | 1x     |    11010 | FSUB (vector)                | FEAT_AdvSIMD |

|   U | size   |   opcode | Instruction Details           | Feature      |
|-----|--------|----------|-------------------------------|--------------|
|   0 | 1x     |    11100 | UNALLOCATED                   | -            |
|   0 | 1x     |    11110 | FMIN (vector)                 | FEAT_AdvSIMD |
|   0 | 1x     |    11111 | FRSQRTS                       | FEAT_AdvSIMD |
|   0 | 10     |    00011 | ORR(vector, register)         | FEAT_AdvSIMD |
|   0 | 10     |    11101 | FMLSL, FMLSL2 (vector)-FMLSL  | FEAT_FHM     |
|   0 | 11     |    00011 | ORN(vector)                   | FEAT_AdvSIMD |
|   1 | xx     |    00000 | UHADD                         | FEAT_AdvSIMD |
|   1 | xx     |    00001 | UQADD                         | FEAT_AdvSIMD |
|   1 | xx     |    00010 | URHADD                        | FEAT_AdvSIMD |
|   1 | xx     |    00100 | UHSUB                         | FEAT_AdvSIMD |
|   1 | xx     |    00101 | UQSUB                         | FEAT_AdvSIMD |
|   1 | xx     |    00110 | CMHI (register)               | FEAT_AdvSIMD |
|   1 | xx     |    00111 | CMHS(register)                | FEAT_AdvSIMD |
|   1 | xx     |    01000 | USHL                          | FEAT_AdvSIMD |
|   1 | xx     |    01001 | UQSHL(register)               | FEAT_AdvSIMD |
|   1 | xx     |    01010 | URSHL                         | FEAT_AdvSIMD |
|   1 | xx     |    01011 | UQRSHL                        | FEAT_AdvSIMD |
|   1 | xx     |    01100 | UMAX                          | FEAT_AdvSIMD |
|   1 | xx     |    01101 | UMIN                          | FEAT_AdvSIMD |
|   1 | xx     |    01110 | UABD                          | FEAT_AdvSIMD |
|   1 | xx     |    01111 | UABA                          | FEAT_AdvSIMD |
|   1 | xx     |    10000 | SUB (vector)                  | FEAT_AdvSIMD |
|   1 | xx     |    10001 | CMEQ(register)                | FEAT_AdvSIMD |
|   1 | xx     |    10010 | MLS(vector)                   | FEAT_AdvSIMD |
|   1 | xx     |    10011 | PMUL                          | FEAT_AdvSIMD |
|   1 | xx     |    10100 | UMAXP                         | FEAT_AdvSIMD |
|   1 | xx     |    10101 | UMINP                         | FEAT_AdvSIMD |
|   1 | xx     |    10110 | SQRDMULH(vector)              | FEAT_AdvSIMD |
|   1 | xx     |    10111 | UNALLOCATED                   | -            |
|   1 | x1     |    11001 | UNALLOCATED                   | -            |
|   1 | 0x     |    11000 | FMAXNMP(vector)               | FEAT_AdvSIMD |
|   1 | 0x     |    11010 | FADDP (vector)                | FEAT_AdvSIMD |
|   1 | 0x     |    11011 | FMUL(vector)                  | FEAT_AdvSIMD |
|   1 | 0x     |    11100 | FCMGE(register)               | FEAT_AdvSIMD |
|   1 | 0x     |    11101 | FACGE                         | FEAT_AdvSIMD |
|   1 | 0x     |    11110 | FMAXP(vector)                 | FEAT_AdvSIMD |
|   1 | 0x     |    11111 | FDIV (vector)                 | FEAT_AdvSIMD |
|   1 | 00     |    00011 | EOR(vector)                   | FEAT_AdvSIMD |
|   1 | 00     |    11001 | FMLAL, FMLAL2 (vector)-FMLAL2 | FEAT_FHM     |
|   1 | 01     |    00011 | BSL                           | FEAT_AdvSIMD |

|   U | size   |   opcode | Instruction Details           | Feature                     |
|-----|--------|----------|-------------------------------|-----------------------------|
|   1 | 1x     |    11000 | FMINNMP(vector)               | FEAT_AdvSIMD                |
|   1 | 1x     |    11010 | FABD                          | FEAT_AdvSIMD                |
|   1 | 1x     |    11011 | FAMIN                         | FEAT_AdvSIMD&&FEAT_FAMINMAX |
|   1 | 1x     |    11100 | FCMGT(register)               | FEAT_AdvSIMD                |
|   1 | 1x     |    11101 | FACGT                         | FEAT_AdvSIMD                |
|   1 | 1x     |    11110 | FMINP (vector)                | FEAT_AdvSIMD                |
|   1 | 1x     |    11111 | FSCALE                        | FEAT_FP8                    |
|   1 | 10     |    00011 | BIT                           | FEAT_AdvSIMD                |
|   1 | 10     |    11001 | FMLSL, FMLSL2 (vector)-FMLSL2 | FEAT_FHM                    |
|   1 | 11     |    00011 | BIF                           | FEAT_AdvSIMD                |

## Advanced SIMD modified immediate

The encodings in this section are decoded from Data Processing - Scalar Floating-Point and Advanced SIMD.

<!-- image -->

|   31 | 30 29 28   | 25 24 23 22 15            | 19 18 17 16 12 11 10 9 8 7 6 5 4   |
|------|------------|---------------------------|------------------------------------|
|    0 | Q op 0 1   | 1 1 0 0 0 0 0 a b c cmode | o2 1 d e f g h Rd                  |

| Q   |   op | cmode   |   o2 | Instruction Details                          | Feature                  |
|-----|------|---------|------|----------------------------------------------|--------------------------|
| x   |    0 | 0xx0    |    0 | MOVI-32-bit shifted immediate                | FEAT_AdvSIMD             |
| x   |    0 | 0xx1    |    0 | ORR(vector, immediate) -32-bit               | FEAT_AdvSIMD             |
| x   |    0 | 10x0    |    0 | MOVI-16-bit shifted immediate                | FEAT_AdvSIMD             |
| x   |    0 | 10x1    |    0 | ORR(vector, immediate) -16-bit               | FEAT_AdvSIMD             |
| x   |    0 | 110x    |    0 | MOVI-32-bit shifting ones                    | FEAT_AdvSIMD             |
| x   |    0 | 1110    |    0 | MOVI-8-bit                                   | FEAT_AdvSIMD             |
| x   |    0 | 1111    |    0 | FMOV (vector, immediate) - Single- precision | FEAT_AdvSIMD             |
| x   |    0 | 1111    |    1 | FMOV (vector, immediate) - Half- precision   | FEAT_AdvSIMD &&FEAT_FP16 |
| x   |    0 | != 1111 |    1 | UNALLOCATED                                  | -                        |
| x   |    1 | xxxx    |    1 | UNALLOCATED                                  | -                        |
| x   |    1 | 0xx0    |    0 | MVNI-32-bit shifted immediate                | FEAT_AdvSIMD             |
| x   |    1 | 0xx1    |    0 | BIC (vector, immediate) -32-bit              | FEAT_AdvSIMD             |
| x   |    1 | 10x0    |    0 | MVNI-16-bit shifted immediate                | FEAT_AdvSIMD             |
| x   |    1 | 10x1    |    0 | BIC (vector, immediate) -16-bit              | FEAT_AdvSIMD             |
| x   |    1 | 110x    |    0 | MVNI-32-bit shifting ones                    | FEAT_AdvSIMD             |
| 0   |    1 | 1110    |    0 | MOVI-64-bit scalar                           | FEAT_AdvSIMD             |
| 0   |    1 | 1111    |    0 | UNALLOCATED                                  | -                        |

|   Q |   op |   cmode |   o2 | Instruction Details                          | Feature      |
|-----|------|---------|------|----------------------------------------------|--------------|
|   1 |    1 |    1110 |    0 | MOVI-64-bit vector                           | FEAT_AdvSIMD |
|   1 |    1 |    1111 |    0 | FMOV (vector, immediate) - Double- precision | FEAT_AdvSIMD |

## Advanced SIMD shift by immediate

The encodings in this section are decoded from Data Processing - Scalar Floating-Point and Advanced SIMD.

<!-- image -->

immh

The following constraints also apply to this encoding: immh != '0000'

| U   | immh    | opcode   | Instruction Details          | Feature      |
|-----|---------|----------|------------------------------|--------------|
| x   | != 0000 | 0xxx1    | UNALLOCATED                  | -            |
| x   | != 0000 | 1x110    | UNALLOCATED                  | -            |
| x   | != 0000 | 101x1    | UNALLOCATED                  | -            |
| x   | != 0000 | 110xx    | UNALLOCATED                  | -            |
| x   | != 0000 | 11101    | UNALLOCATED                  | -            |
| 0   | != 0000 | 00000    | SSHR                         | FEAT_AdvSIMD |
| 0   | != 0000 | 00010    | SSRA                         | FEAT_AdvSIMD |
| 0   | != 0000 | 00100    | SRSHR                        | FEAT_AdvSIMD |
| 0   | != 0000 | 00110    | SRSRA                        | FEAT_AdvSIMD |
| 0   | != 0000 | 01x00    | UNALLOCATED                  | -            |
| 0   | != 0000 | 01010    | SHL                          | FEAT_AdvSIMD |
| 0   | != 0000 | 01110    | SQSHL (immediate)            | FEAT_AdvSIMD |
| 0   | != 0000 | 10000    | SHRN, SHRN2                  | FEAT_AdvSIMD |
| 0   | != 0000 | 10001    | RSHRN, RSHRN2                | FEAT_AdvSIMD |
| 0   | != 0000 | 10010    | SQSHRN, SQSHRN2              | FEAT_AdvSIMD |
| 0   | != 0000 | 10011    | SQRSHRN, SQRSHRN2            | FEAT_AdvSIMD |
| 0   | != 0000 | 10100    | SSHLL, SSHLL2                | FEAT_AdvSIMD |
| 0   | != 0000 | 11100    | SCVTF (vector, fixed-point)  | FEAT_AdvSIMD |
| 0   | != 0000 | 11111    | FCVTZS (vector, fixed-point) | FEAT_AdvSIMD |
| 1   | != 0000 | 00000    | USHR                         | FEAT_AdvSIMD |
| 1   | != 0000 | 00010    | USRA                         | FEAT_AdvSIMD |
| 1   | != 0000 | 00100    | URSHR                        | FEAT_AdvSIMD |
| 1   | != 0000 | 00110    | URSRA                        | FEAT_AdvSIMD |
| 1   | != 0000 | 01000    | SRI                          | FEAT_AdvSIMD |

|   U | immh    |   opcode | Instruction Details          | Feature      |
|-----|---------|----------|------------------------------|--------------|
|   1 | != 0000 |    01010 | SLI                          | FEAT_AdvSIMD |
|   1 | != 0000 |    01100 | SQSHLU                       | FEAT_AdvSIMD |
|   1 | != 0000 |    01110 | UQSHL(immediate)             | FEAT_AdvSIMD |
|   1 | != 0000 |    10000 | SQSHRUN, SQSHRUN2            | FEAT_AdvSIMD |
|   1 | != 0000 |    10001 | SQRSHRUN, SQRSHRUN2          | FEAT_AdvSIMD |
|   1 | != 0000 |    10010 | UQSHRN, UQSHRN2              | FEAT_AdvSIMD |
|   1 | != 0000 |    10011 | UQRSHRN,UQRSHRN2             | FEAT_AdvSIMD |
|   1 | != 0000 |    10100 | USHLL, USHLL2                | FEAT_AdvSIMD |
|   1 | != 0000 |    11100 | UCVTF (vector, fixed-point)  | FEAT_AdvSIMD |
|   1 | != 0000 |    11111 | FCVTZU (vector, fixed-point) | FEAT_AdvSIMD |

## Advanced SIMD vector x indexed element

The encodings in this section are decoded from Data Processing - Scalar Floating-Point and Advanced SIMD.

|   31 | 30 29   | 24 23 22 21   |      | 20   | 19   | 16   | 15     | 11 10   | 5   |    |
|------|---------|---------------|------|------|------|------|--------|---------|-----|----|
|    0 | Q U     | 1 1 1 L       | size |      | M    | Rm   | opcode | H 0     | Rn  | Rd |

| Q   | U   | size   |   opcode | Instruction Details                                          | Feature                  |
|-----|-----|--------|----------|--------------------------------------------------------------|--------------------------|
| x   | x   | 01     |     1001 | UNALLOCATED                                                  | -                        |
| x   | 0   | xx     |     0010 | SMLAL, SMLAL2 (by element)                                   | FEAT_AdvSIMD             |
| x   | 0   | xx     |     0011 | SQDMLAL, SQDMLAL2(by element)                                | FEAT_AdvSIMD             |
| x   | 0   | xx     |     0110 | SMLSL, SMLSL2 (by element)                                   | FEAT_AdvSIMD             |
| x   | 0   | xx     |     0111 | SQDMLSL, SQDMLSL2 (by element)                               | FEAT_AdvSIMD             |
| x   | 0   | xx     |     1000 | MUL(by element)                                              | FEAT_AdvSIMD             |
| x   | 0   | xx     |     1010 | SMULL, SMULL2 (by element)                                   | FEAT_AdvSIMD             |
| x   | 0   | xx     |     1011 | SQDMULL, SQDMULL2(by element)                                | FEAT_AdvSIMD             |
| x   | 0   | xx     |     1100 | SQDMULH(by element)                                          | FEAT_AdvSIMD             |
| x   | 0   | xx     |     1101 | SQRDMULH(by element)                                         | FEAT_AdvSIMD             |
| x   | 0   | xx     |     1110 | SDOT (by element)                                            | FEAT_DotProd             |
| x   | 0   | 00     |     0000 | FDOT (8-bit floating-point to single- precision, by element) | FEAT_FP8DOT4             |
| x   | 0   | 00     |     0001 | FMLA (by element) - Vector, half- precision                  | FEAT_AdvSIMD &&FEAT_FP16 |
| x   | 0   | 00     |     0101 | FMLS (by element) - Vector, half- precision                  | FEAT_AdvSIMD &&FEAT_FP16 |
| x   | 0   | 00     |     1001 | FMUL (by element) - Vector, half- precision                  | FEAT_AdvSIMD &&FEAT_FP16 |

| Q   |   U | size   | opcode   | Instruction Details                                                 | Feature                  |
|-----|-----|--------|----------|---------------------------------------------------------------------|--------------------------|
| x   |   0 | 00     | 1111     | SUDOT(by element)                                                   | FEAT_I8MM                |
| x   |   0 | 01     | 0x01     | UNALLOCATED                                                         | -                        |
| x   |   0 | 01     | 0000     | FDOT (8-bit floating-point to half- precision, by element)          | FEAT_FP8DOT2             |
| x   |   0 | 01     | 1111     | BFDOT (by element)                                                  | FEAT_BF16                |
| x   |   0 | 1x     | 0001     | FMLA (by element) - Vector, single- precision and double-precision  | FEAT_AdvSIMD             |
| x   |   0 | 1x     | 0101     | FMLS (by element) - Vector, single- precision and double-precision  | FEAT_AdvSIMD             |
| x   |   0 | 1x     | 1001     | FMUL (by element) - Vector, single- precision and double-precision  | FEAT_AdvSIMD             |
| x   |   0 | 10     | 0000     | FMLAL, FMLAL2 (by element) - FMLAL                                  | FEAT_FHM                 |
| x   |   0 | 10     | 0100     | FMLSL, FMLSL2 (by element) - FMLSL                                  | FEAT_FHM                 |
| x   |   0 | 10     | 1111     | USDOT(by element)                                                   | FEAT_I8MM                |
| x   |   0 | 11     | 1111     | BFMLALB, BFMLALT (by element)                                       | FEAT_BF16                |
| x   |   0 | != 10  | 0100     | UNALLOCATED                                                         | -                        |
| x   |   1 | xx     | 0xx1     | FCMLA(by element)                                                   | FEAT_FCMA                |
| x   |   1 | xx     | 0000     | MLA(by element)                                                     | FEAT_AdvSIMD             |
| x   |   1 | xx     | 0010     | UMLAL, UMLAL2(by element)                                           | FEAT_AdvSIMD             |
| x   |   1 | xx     | 0100     | MLS(by element)                                                     | FEAT_AdvSIMD             |
| x   |   1 | xx     | 0110     | UMLSL, UMLSL2 (by element)                                          | FEAT_AdvSIMD             |
| x   |   1 | xx     | 1010     | UMULL, UMULL2(by element)                                           | FEAT_AdvSIMD             |
| x   |   1 | xx     | 1011     | UNALLOCATED                                                         | -                        |
| x   |   1 | xx     | 1101     | SQRDMLAH(by element)                                                | FEAT_RDM                 |
| x   |   1 | xx     | 1110     | UDOT(by element)                                                    | FEAT_DotProd             |
| x   |   1 | xx     | 1111     | SQRDMLSH(by element)                                                | FEAT_RDM                 |
| x   |   1 | 0x     | 1100     | UNALLOCATED                                                         | -                        |
| x   |   1 | 00     | 1001     | FMULX (by element) - Vector, half- precision                        | FEAT_AdvSIMD &&FEAT_FP16 |
| x   |   1 | 1x     | 1001     | FMULX (by element) - Vector, single- precision and double-precision | FEAT_AdvSIMD             |
| x   |   1 | 10     | 1000     | FMLAL, FMLAL2 (by element) - FMLAL2                                 | FEAT_FHM                 |
| x   |   1 | 10     | 1100     | FMLSL, FMLSL2 (by element) - FMLSL2                                 | FEAT_FHM                 |
| x   |   1 | 11     | 1x00     | UNALLOCATED                                                         | -                        |
| 0   |   0 | 11     | 0000     | FMLALB, FMLALT (by element) - FMLALB                                | FEAT_FP8FMA              |
| 0   |   1 | 00     | 1000     | FMLALLBB, FMLALLBT, FMLALLTB, FMLALLTT(byelement)-FMLALLBB          | FEAT_FP8FMA              |
| 0   |   1 | 01     | 1000     | FMLALLBB, FMLALLBT, FMLALLTB, FMLALLTT(byelement)-FMLALLBT          | FEAT_FP8FMA              |

|   Q |   U |   size |   opcode | Instruction Details                                          | Feature     |
|-----|-----|--------|----------|--------------------------------------------------------------|-------------|
|   1 |   0 |     11 |     0000 | FMLALB, FMLALT (by element) - FMLALT                         | FEAT_FP8FMA |
|   1 |   1 |     00 |     1000 | FMLALLBB, FMLALLBT, FMLALLTB, FMLALLTT (by element)-FMLALLTB | FEAT_FP8FMA |
|   1 |   1 |     01 |     1000 | FMLALLBB, FMLALLBT, FMLALLTB, FMLALLTT (by element)-FMLALLTT | FEAT_FP8FMA |

## Cryptographic three-register, imm2

The encodings in this section are decoded from Data Processing - Scalar Floating-Point and Advanced SIMD.

<!-- image -->

| 31   | 28 27 25 24 23 22 21 20     | 16 15 14 13 12 11 10 9 5 4   |
|------|-----------------------------|------------------------------|
| 1 1  | 0 1 1 1 0 0 1 0 Rm 1 0 imm2 | opcode Rn Rd                 |

|   opcode | Instruction Details   | Feature   |
|----------|-----------------------|-----------|
|       00 | SM3TT1A               | FEAT_SM3  |
|       01 | SM3TT1B               | FEAT_SM3  |
|       10 | SM3TT2A               | FEAT_SM3  |
|       11 | SM3TT2B               | FEAT_SM3  |

## Cryptographic three-register SHA 512

The encodings in this section are decoded from Data Processing - Scalar Floating-Point and Advanced SIMD.

<!-- image -->

| 31 28 27 25           | 24 23 22 21 20 16 15 14 13 12 11 10 9   |
|-----------------------|-----------------------------------------|
| 1 1 0 0 1 1 1 0 0 1 1 | Rm 1 O 0 0 opcode Rn                    |

|   O |   opcode | Instruction Details   | Feature     |
|-----|----------|-----------------------|-------------|
|   0 |       00 | SHA512H               | FEAT_SHA512 |
|   0 |       01 | SHA512H2              | FEAT_SHA512 |
|   0 |       10 | SHA512SU1             | FEAT_SHA512 |
|   0 |       11 | RAX1                  | FEAT_SHA3   |
|   1 |       00 | SM3PARTW1             | FEAT_SM3    |
|   1 |       01 | SM3PARTW2             | FEAT_SM3    |

## Cryptographic four-register

The encodings in this section are decoded from Data Processing - Scalar Floating-Point and Advanced SIMD.

<!-- image -->

|   Op0 | Instruction Details   | Feature   |
|-------|-----------------------|-----------|
|    00 | EOR3                  | FEAT_SHA3 |
|    01 | BCAX                  | FEAT_SHA3 |
|    10 | SM3SS1                | FEAT_SM3  |
|    11 | UNALLOCATED           | -         |

|   O |   opcode | Instruction Details   | Feature   |
|-----|----------|-----------------------|-----------|
|   1 |       10 | SM4EKEY               | FEAT_SM4  |
|   1 |       11 | UNALLOCATED           | -         |

## Cryptographic two-register SHA 512

The encodings in this section are decoded from Data Processing - Scalar Floating-Point and Advanced SIMD.

<!-- image -->

| opcode   | Instruction Details   | Feature     |
|----------|-----------------------|-------------|
| 00       | SHA512SU0             | FEAT_SHA512 |
| 01       | SM4E                  | FEAT_SM4    |
| 1x       | UNALLOCATED           | -           |

## Conversion between floating-point and fixed-point

The encodings in this section are decoded from Data Processing - Scalar Floating-Point and Advanced SIMD.

<!-- image -->

| sf   |   S | ftype   | rmode   | opcode   | Instruction Details                                        | Feature   |
|------|-----|---------|---------|----------|------------------------------------------------------------|-----------|
| x    |   0 | xx      | xx      | 1xx      | UNALLOCATED                                                | -         |
| x    |   0 | 10      | xx      | 0xx      | UNALLOCATED                                                | -         |
| x    |   0 | != 10   | x1      | 01x      | UNALLOCATED                                                | -         |
| x    |   0 | != 10   | 0x      | 00x      | UNALLOCATED                                                | -         |
| x    |   0 | != 10   | 10      | 0xx      | UNALLOCATED                                                | -         |
| x    |   1 | xx      | xx      | xxx      | UNALLOCATED                                                | -         |
| 0    |   0 | 00      | 00      | 010      | SCVTF (scalar, fixed-point) - 32-bit to single-precision   | FEAT_FP   |
| 0    |   0 | 00      | 00      | 011      | UCVTF (scalar, fixed-point) - 32-bit to single-precision   | FEAT_FP   |
| 0    |   0 | 00      | 11      | 000      | FCVTZS (scalar, fixed-point) - Single- precision to 32-bit | FEAT_FP   |
| 0    |   0 | 00      | 11      | 001      | FCVTZU (scalar, fixed-point) - Single- precision to 32-bit | FEAT_FP   |
| 0    |   0 | 01      | 00      | 010      | SCVTF (scalar, fixed-point) - 32-bit to double-precision   | FEAT_FP   |
| 0    |   0 | 01      | 00      | 011      | UCVTF (scalar, fixed-point) - 32-bit to double-precision   | FEAT_FP   |
| 0    |   0 | 01      | 11      | 000      | FCVTZS (scalar, fixed-point) - Double- precision to 32-bit | FEAT_FP   |
| 0    |   0 | 01      | 11      | 001      | FCVTZU (scalar, fixed-point) -Double- precision to 32-bit  | FEAT_FP   |
| 0    |   0 | 11      | 00      | 010      | SCVTF (scalar, fixed-point) - 32-bit to half-precision     | FEAT_FP16 |
| 0    |   0 | 11      | 00      | 011      | UCVTF (scalar, fixed-point) - 32-bit to half-precision     | FEAT_FP16 |
| 0    |   0 | 11      | 11      | 000      | FCVTZS (scalar, fixed-point) - Half- precision to 32-bit   | FEAT_FP16 |
| 0    |   0 | 11      | 11      | 001      | FCVTZU (scalar, fixed-point) - Half- precision to 32-bit   | FEAT_FP16 |
| 1    |   0 | 00      | 00      | 010      | SCVTF (scalar, fixed-point) - 64-bit to single-precision   | FEAT_FP   |
| 1    |   0 | 00      | 00      | 011      | UCVTF (scalar, fixed-point) - 64-bit to single-precision   | FEAT_FP   |
| 1    |   0 | 00      | 11      | 000      | FCVTZS (scalar, fixed-point) - Single- precision to 64-bit | FEAT_FP   |
| 1    |   0 | 00      | 11      | 001      | FCVTZU (scalar, fixed-point) - Single- precision to 64-bit | FEAT_FP   |
| 1    |   0 | 01      | 00      | 010      | SCVTF (scalar, fixed-point) - 64-bit to double-precision   | FEAT_FP   |
| 1    |   0 | 01      | 00      | 011      | UCVTF (scalar, fixed-point) - 64-bit to double-precision   | FEAT_FP   |
| 1    |   0 | 01      | 11      | 000      | FCVTZS (scalar, fixed-point) - Double- precision to 64-bit | FEAT_FP   |

|   sf |   S |   ftype |   rmode |   opcode | Instruction Details                                       | Feature   |
|------|-----|---------|---------|----------|-----------------------------------------------------------|-----------|
|    1 |   0 |      01 |      11 |      001 | FCVTZU (scalar, fixed-point) -Double- precision to 64-bit | FEAT_FP   |
|    1 |   0 |      11 |      00 |      010 | SCVTF (scalar, fixed-point) - 64-bit to half-precision    | FEAT_FP16 |
|    1 |   0 |      11 |      00 |      011 | UCVTF (scalar, fixed-point) - 64-bit to half-precision    | FEAT_FP16 |
|    1 |   0 |      11 |      11 |      000 | FCVTZS (scalar, fixed-point) - Half- precision to 64-bit  | FEAT_FP16 |
|    1 |   0 |      11 |      11 |      001 | FCVTZU (scalar, fixed-point) - Half- precision to 64-bit  | FEAT_FP16 |

## Conversion between floating-point and integer

The encodings in this section are decoded from Data Processing - Scalar Floating-Point and Advanced SIMD.

<!-- image -->

| 31 30   | 29 28   | 24    | 23    |   22 21 | 20 19   | 18    | 16 15   | 10      | 9 5   | 4   |    |
|---------|---------|-------|-------|---------|---------|-------|---------|---------|-------|-----|----|
| sf 0    | S 1     | 1 1 0 | ftype |       1 |         | rmode | opcode  | 0 0 0 0 | 0 0   | Rn  | Rd |

| sf   |   S | ftype   | rmode   | opcode   | Instruction Details                                  | Feature   |
|------|-----|---------|---------|----------|------------------------------------------------------|-----------|
| x    |   0 | 10      | x0      | xxx      | UNALLOCATED                                          | -         |
| x    |   0 | 10      | x1      | 0xx      | UNALLOCATED                                          | -         |
| x    |   0 | 10      | x1      | 10x      | UNALLOCATED                                          | -         |
| x    |   0 | 11      | x1      | 11x      | UNALLOCATED                                          | -         |
| x    |   0 | != 10   | 01      | 10x      | UNALLOCATED                                          | -         |
| x    |   1 | xx      | xx      | xxx      | UNALLOCATED                                          | -         |
| 0    |   0 | x0      | 01      | 11x      | UNALLOCATED                                          | -         |
| 0    |   0 | 00      | 00      | 000      | FCVTNS (scalar) - Single-precision to 32-bit         | FEAT_FP   |
| 0    |   0 | 00      | 00      | 001      | FCVTNU (scalar) - Single-precision to 32-bit         | FEAT_FP   |
| 0    |   0 | 00      | 00      | 010      | SCVTF(scalar, integer) -32-bit to single- precision  | FEAT_FP   |
| 0    |   0 | 00      | 00      | 011      | UCVTF (scalar, integer) - 32-bit to single-precision | FEAT_FP   |
| 0    |   0 | 00      | 00      | 100      | FCVTAS (scalar) - Single-precision to 32-bit         | FEAT_FP   |
| 0    |   0 | 00      | 00      | 101      | FCVTAU (scalar) - Single-precision to 32-bit         | FEAT_FP   |
| 0    |   0 | 00      | 00      | 110      | FMOV(general) -Single-precision to 32- bit           | FEAT_FP   |
| 0    |   0 | 00      | 00      | 111      | FMOV (general) - 32-bit to single- precision         | FEAT_FP   |

|   sf |   S |   ftype | rmode   | opcode   | Instruction Details                                    | Feature     |
|------|-----|---------|---------|----------|--------------------------------------------------------|-------------|
|    0 |   0 |      00 | 01      | 000      | FCVTPS (scalar) - Single-precision to 32-bit           | FEAT_FP     |
|    0 |   0 |      00 | 01      | 001      | FCVTPU (scalar) - Single-precision to 32-bit           | FEAT_FP     |
|    0 |   0 |      00 | 1x      | 1xx      | UNALLOCATED                                            | -           |
|    0 |   0 |      00 | 10      | 000      | FCVTMS (scalar) - Single-precision to 32-bit           | FEAT_FP     |
|    0 |   0 |      00 | 10      | 001      | FCVTMU (scalar) - Single-precision to 32-bit           | FEAT_FP     |
|    0 |   0 |      00 | 11      | 000      | FCVTZS (scalar, integer) - Single- precision to 32-bit | FEAT_FP     |
|    0 |   0 |      00 | 11      | 001      | FCVTZU (scalar, integer) - Single- precision to 32-bit | FEAT_FP     |
|    0 |   0 |      00 | != 00   | 01x      | UNALLOCATED                                            | -           |
|    0 |   0 |      01 | 0x      | 11x      | UNALLOCATED                                            | -           |
|    0 |   0 |      01 | 00      | 000      | FCVTNS (scalar) - Double-precision to 32-bit           | FEAT_FP     |
|    0 |   0 |      01 | 00      | 001      | FCVTNU (scalar) -Double-precision to 32-bit            | FEAT_FP     |
|    0 |   0 |      01 | 00      | 010      | SCVTF (scalar, integer) - 32-bit to double-precision   | FEAT_FP     |
|    0 |   0 |      01 | 00      | 011      | UCVTF (scalar, integer) - 32-bit to double-precision   | FEAT_FP     |
|    0 |   0 |      01 | 00      | 100      | FCVTAS (scalar) - Double-precision to 32-bit           | FEAT_FP     |
|    0 |   0 |      01 | 00      | 101      | FCVTAU (scalar) - Double-precision to 32-bit           | FEAT_FP     |
|    0 |   0 |      01 | 01      | 000      | FCVTPS (scalar) - Double-precision to 32-bit           | FEAT_FP     |
|    0 |   0 |      01 | 01      | 001      | FCVTPU (scalar) - Double-precision to 32-bit           | FEAT_FP     |
|    0 |   0 |      01 | 01      | 010      | FCVTNS (scalar SIMD&FP) - Double- precision to 32-bit  | FEAT_FPRCVT |
|    0 |   0 |      01 | 01      | 011      | FCVTNU (scalar SIMD&FP) - Double- precision to 32-bit  | FEAT_FPRCVT |
|    0 |   0 |      01 | 10      | 000      | FCVTMS (scalar) -Double-precision to 32-bit            | FEAT_FP     |
|    0 |   0 |      01 | 10      | 001      | FCVTMU (scalar) -Double-precision to 32-bit            | FEAT_FP     |
|    0 |   0 |      01 | 10      | 010      | FCVTPS (scalar SIMD&FP) - Double- precision to 32-bit  | FEAT_FPRCVT |
|    0 |   0 |      01 | 10      | 011      | FCVTPU (scalar SIMD&FP) - Double- precision to 32-bit  | FEAT_FPRCVT |
|    0 |   0 |      01 | 10      | 100      | FCVTMS (scalar SIMD&FP) - Double- precision to 32-bit  | FEAT_FPRCVT |
|    0 |   0 |      01 | 10      | 101      | FCVTMU (scalar SIMD&FP) -Double- precision to 32-bit   | FEAT_FPRCVT |
|    0 |   0 |      01 | 10      | 110      | FCVTZS (scalar SIMD&FP) - Double- precision to 32-bit  | FEAT_FPRCVT |

|   sf |   S |   ftype |   rmode | opcode   | Instruction Details                                    | Feature     |
|------|-----|---------|---------|----------|--------------------------------------------------------|-------------|
|    0 |   0 |      01 |      10 | 111      | FCVTZU (scalar SIMD&FP) - Double- precision to 32-bit  | FEAT_FPRCVT |
|    0 |   0 |      01 |      11 | 000      | FCVTZS (scalar, integer) - Double- precision to 32-bit | FEAT_FP     |
|    0 |   0 |      01 |      11 | 001      | FCVTZU (scalar, integer) - Double- precision to 32-bit | FEAT_FP     |
|    0 |   0 |      01 |      11 | 010      | FCVTAS (scalar SIMD&FP) - Double- precision to 32-bit  | FEAT_FPRCVT |
|    0 |   0 |      01 |      11 | 011      | FCVTAU (scalar SIMD&FP) - Double- precision to 32-bit  | FEAT_FPRCVT |
|    0 |   0 |      01 |      11 | 100      | SCVTF (scalar SIMD&FP) - 32-bit to double-precision    | FEAT_FPRCVT |
|    0 |   0 |      01 |      11 | 101      | UCVTF (scalar SIMD&FP) - 32-bit to double-precision    | FEAT_FPRCVT |
|    0 |   0 |      01 |      11 | 110      | FJCVTZS                                                | FEAT_JSCVT  |
|    0 |   0 |      01 |      11 | 111      | UNALLOCATED                                            | -           |
|    0 |   0 |      10 |      11 | 11x      | UNALLOCATED                                            | -           |
|    0 |   0 |      11 |      00 | 000      | FCVTNS (scalar) -Half-precision to 32- bit             | FEAT_FP16   |
|    0 |   0 |      11 |      00 | 001      | FCVTNU (scalar) -Half-precision to 32- bit             | FEAT_FP16   |
|    0 |   0 |      11 |      00 | 010      | SCVTF (scalar, integer) -32-bit to half- precision     | FEAT_FP16   |
|    0 |   0 |      11 |      00 | 011      | UCVTF (scalar, integer) -32-bit to half- precision     | FEAT_FP16   |
|    0 |   0 |      11 |      00 | 100      | FCVTAS (scalar) -Half-precision to 32- bit             | FEAT_FP16   |
|    0 |   0 |      11 |      00 | 101      | FCVTAU (scalar) -Half-precision to 32- bit             | FEAT_FP16   |
|    0 |   0 |      11 |      00 | 110      | FMOV (general) -Half-precision to 32- bit              | FEAT_FP16   |
|    0 |   0 |      11 |      00 | 111      | FMOV (general) - 32-bit to half- precision             | FEAT_FP16   |
|    0 |   0 |      11 |      01 | 000      | FCVTPS (scalar) -Half-precision to 32- bit             | FEAT_FP16   |
|    0 |   0 |      11 |      01 | 001      | FCVTPU (scalar) -Half-precision to 32- bit             | FEAT_FP16   |
|    0 |   0 |      11 |      01 | 010      | FCVTNS (scalar SIMD&FP) - Half- precision to 32-bit    | FEAT_FPRCVT |
|    0 |   0 |      11 |      01 | 011      | FCVTNU (scalar SIMD&FP) - Half- precision to 32-bit    | FEAT_FPRCVT |
|    0 |   0 |      11 |      10 | 000      | FCVTMS (scalar) -Half-precision to 32- bit             | FEAT_FP16   |
|    0 |   0 |      11 |      10 | 001      | FCVTMU(scalar) -Half-precision to 32- bit              | FEAT_FP16   |
|    0 |   0 |      11 |      10 | 010      | FCVTPS (scalar SIMD&FP) - Half- precision to 32-bit    | FEAT_FPRCVT |
|    0 |   0 |      11 |      10 | 011      | FCVTPU (scalar SIMD&FP) - Half- precision to 32-bit    | FEAT_FPRCVT |

|   sf |   S | ftype   | rmode   | opcode   | Instruction Details                                   | Feature     |
|------|-----|---------|---------|----------|-------------------------------------------------------|-------------|
|    0 |   0 | 11      | 10      | 100      | FCVTMS (scalar SIMD&FP) - Half- precision to 32-bit   | FEAT_FPRCVT |
|    0 |   0 | 11      | 10      | 101      | FCVTMU (scalar SIMD&FP) - Half- precision to 32-bit   | FEAT_FPRCVT |
|    0 |   0 | 11      | 10      | 110      | FCVTZS (scalar SIMD&FP) - Half- precision to 32-bit   | FEAT_FPRCVT |
|    0 |   0 | 11      | 10      | 111      | FCVTZU (scalar SIMD&FP) - Half- precision to 32-bit   | FEAT_FPRCVT |
|    0 |   0 | 11      | 11      | 000      | FCVTZS (scalar, integer) - Half- precision to 32-bit  | FEAT_FP16   |
|    0 |   0 | 11      | 11      | 001      | FCVTZU (scalar, integer) - Half- precision to 32-bit  | FEAT_FP16   |
|    0 |   0 | 11      | 11      | 010      | FCVTAS (scalar SIMD&FP) - Half- precision to 32-bit   | FEAT_FPRCVT |
|    0 |   0 | 11      | 11      | 011      | FCVTAU (scalar SIMD&FP) - Half- precision to 32-bit   | FEAT_FPRCVT |
|    0 |   0 | 11      | 11      | 100      | SCVTF (scalar SIMD&FP) - 32-bit to half-precision     | FEAT_FPRCVT |
|    0 |   0 | 11      | 11      | 101      | UCVTF (scalar SIMD&FP) - 32-bit to half-precision     | FEAT_FPRCVT |
|    1 |   0 | x0      | 11      | 11x      | UNALLOCATED                                           | -           |
|    1 |   0 | 00      | 0x      | 11x      | UNALLOCATED                                           | -           |
|    1 |   0 | 00      | 00      | 000      | FCVTNS (scalar) - Single-precision to 64-bit          | FEAT_FP     |
|    1 |   0 | 00      | 00      | 001      | FCVTNU (scalar) - Single-precision to 64-bit          | FEAT_FP     |
|    1 |   0 | 00      | 00      | 010      | SCVTF(scalar, integer) -64-bit to single- precision   | FEAT_FP     |
|    1 |   0 | 00      | 00      | 011      | UCVTF (scalar, integer) - 64-bit to single-precision  | FEAT_FP     |
|    1 |   0 | 00      | 00      | 100      | FCVTAS (scalar) - Single-precision to 64-bit          | FEAT_FP     |
|    1 |   0 | 00      | 00      | 101      | FCVTAU (scalar) - Single-precision to 64-bit          | FEAT_FP     |
|    1 |   0 | 00      | 01      | 000      | FCVTPS (scalar) - Single-precision to 64-bit          | FEAT_FP     |
|    1 |   0 | 00      | 01      | 001      | FCVTPU (scalar) - Single-precision to 64-bit          | FEAT_FP     |
|    1 |   0 | 00      | 01      | 010      | FCVTNS (scalar SIMD&FP) - Single- precision to 64-bit | FEAT_FPRCVT |
|    1 |   0 | 00      | 01      | 011      | FCVTNU (scalar SIMD&FP) - Single- precision to 64-bit | FEAT_FPRCVT |
|    1 |   0 | 00      | 10      | 000      | FCVTMS (scalar) - Single-precision to 64-bit          | FEAT_FP     |
|    1 |   0 | 00      | 10      | 001      | FCVTMU (scalar) - Single-precision to 64-bit          | FEAT_FP     |
|    1 |   0 | 00      | 10      | 010      | FCVTPS (scalar SIMD&FP) - Single- precision to 64-bit | FEAT_FPRCVT |

|   sf |   S |   ftype | rmode   | opcode   | Instruction Details                                    | Feature     |
|------|-----|---------|---------|----------|--------------------------------------------------------|-------------|
|    1 |   0 |      00 | 10      | 011      | FCVTPU (scalar SIMD&FP) - Single- precision to 64-bit  | FEAT_FPRCVT |
|    1 |   0 |      00 | 10      | 100      | FCVTMS (scalar SIMD&FP) - Single- precision to 64-bit  | FEAT_FPRCVT |
|    1 |   0 |      00 | 10      | 101      | FCVTMU (scalar SIMD&FP) - Single- precision to 64-bit  | FEAT_FPRCVT |
|    1 |   0 |      00 | 10      | 110      | FCVTZS (scalar SIMD&FP) - Single- precision to 64-bit  | FEAT_FPRCVT |
|    1 |   0 |      00 | 10      | 111      | FCVTZU (scalar SIMD&FP) - Single- precision to 64-bit  | FEAT_FPRCVT |
|    1 |   0 |      00 | 11      | 000      | FCVTZS (scalar, integer) - Single- precision to 64-bit | FEAT_FP     |
|    1 |   0 |      00 | 11      | 001      | FCVTZU (scalar, integer) - Single- precision to 64-bit | FEAT_FP     |
|    1 |   0 |      00 | 11      | 010      | FCVTAS (scalar SIMD&FP) - Single- precision to 64-bit  | FEAT_FPRCVT |
|    1 |   0 |      00 | 11      | 011      | FCVTAU (scalar SIMD&FP) - Single- precision to 64-bit  | FEAT_FPRCVT |
|    1 |   0 |      00 | 11      | 100      | SCVTF (scalar SIMD&FP) - 64-bit to single-precision    | FEAT_FPRCVT |
|    1 |   0 |      00 | 11      | 101      | UCVTF (scalar SIMD&FP) - 64-bit to single-precision    | FEAT_FPRCVT |
|    1 |   0 |      01 | 00      | 000      | FCVTNS (scalar) - Double-precision to 64-bit           | FEAT_FP     |
|    1 |   0 |      01 | 00      | 001      | FCVTNU (scalar) -Double-precision to 64-bit            | FEAT_FP     |
|    1 |   0 |      01 | 00      | 010      | SCVTF (scalar, integer) - 64-bit to double-precision   | FEAT_FP     |
|    1 |   0 |      01 | 00      | 011      | UCVTF (scalar, integer) - 64-bit to double-precision   | FEAT_FP     |
|    1 |   0 |      01 | 00      | 100      | FCVTAS (scalar) - Double-precision to 64-bit           | FEAT_FP     |
|    1 |   0 |      01 | 00      | 101      | FCVTAU (scalar) - Double-precision to 64-bit           | FEAT_FP     |
|    1 |   0 |      01 | 00      | 110      | FMOV (general) - Double-precision to 64-bit            | FEAT_FP     |
|    1 |   0 |      01 | 00      | 111      | FMOV (general) - 64-bit to double- precision           | FEAT_FP     |
|    1 |   0 |      01 | 01      | x1x      | UNALLOCATED                                            | -           |
|    1 |   0 |      01 | 01      | 000      | FCVTPS (scalar) - Double-precision to 64-bit           | FEAT_FP     |
|    1 |   0 |      01 | 01      | 001      | FCVTPU (scalar) - Double-precision to 64-bit           | FEAT_FP     |
|    1 |   0 |      01 | 1x      | 01x      | UNALLOCATED                                            | -           |
|    1 |   0 |      01 | 1x      | 1xx      | UNALLOCATED                                            | -           |
|    1 |   0 |      01 | 10      | 000      | FCVTMS (scalar) -Double-precision to 64-bit            | FEAT_FP     |
|    1 |   0 |      01 | 10      | 001      | FCVTMU (scalar) -Double-precision to 64-bit            | FEAT_FP     |

|   sf |   S |   ftype |   rmode |   opcode | Instruction Details                                    | Feature     |
|------|-----|---------|---------|----------|--------------------------------------------------------|-------------|
|    1 |   0 |      01 |      11 |      000 | FCVTZS (scalar, integer) - Double- precision to 64-bit | FEAT_FP     |
|    1 |   0 |      01 |      11 |      001 | FCVTZU (scalar, integer) - Double- precision to 64-bit | FEAT_FP     |
|    1 |   0 |      10 |      01 |      110 | FMOV (general) -Top half of 128-bit to 64-bit          | FEAT_FP     |
|    1 |   0 |      10 |      01 |      111 | FMOV (general) - 64-bit to top half of 128-bit         | FEAT_FP     |
|    1 |   0 |      11 |      00 |      000 | FCVTNS (scalar) -Half-precision to 64- bit             | FEAT_FP16   |
|    1 |   0 |      11 |      00 |      001 | FCVTNU (scalar) -Half-precision to 64- bit             | FEAT_FP16   |
|    1 |   0 |      11 |      00 |      010 | SCVTF (scalar, integer) -64-bit to half- precision     | FEAT_FP16   |
|    1 |   0 |      11 |      00 |      011 | UCVTF (scalar, integer) -64-bit to half- precision     | FEAT_FP16   |
|    1 |   0 |      11 |      00 |      100 | FCVTAS (scalar) -Half-precision to 64- bit             | FEAT_FP16   |
|    1 |   0 |      11 |      00 |      101 | FCVTAU (scalar) -Half-precision to 64- bit             | FEAT_FP16   |
|    1 |   0 |      11 |      00 |      110 | FMOV (general) -Half-precision to 64- bit              | FEAT_FP16   |
|    1 |   0 |      11 |      00 |      111 | FMOV (general) - 64-bit to half- precision             | FEAT_FP16   |
|    1 |   0 |      11 |      01 |      000 | FCVTPS (scalar) -Half-precision to 64- bit             | FEAT_FP16   |
|    1 |   0 |      11 |      01 |      001 | FCVTPU (scalar) -Half-precision to 64- bit             | FEAT_FP16   |
|    1 |   0 |      11 |      01 |      010 | FCVTNS (scalar SIMD&FP) - Half- precision to 64-bit    | FEAT_FPRCVT |
|    1 |   0 |      11 |      01 |      011 | FCVTNU (scalar SIMD&FP) - Half- precision to 64-bit    | FEAT_FPRCVT |
|    1 |   0 |      11 |      10 |      000 | FCVTMS (scalar) -Half-precision to 64- bit             | FEAT_FP16   |
|    1 |   0 |      11 |      10 |      001 | FCVTMU(scalar) -Half-precision to 64- bit              | FEAT_FP16   |
|    1 |   0 |      11 |      10 |      010 | FCVTPS (scalar SIMD&FP) - Half- precision to 64-bit    | FEAT_FPRCVT |
|    1 |   0 |      11 |      10 |      011 | FCVTPU (scalar SIMD&FP) - Half- precision to 64-bit    | FEAT_FPRCVT |
|    1 |   0 |      11 |      10 |      100 | FCVTMS (scalar SIMD&FP) - Half- precision to 64-bit    | FEAT_FPRCVT |
|    1 |   0 |      11 |      10 |      101 | FCVTMU (scalar SIMD&FP) - Half- precision to 64-bit    | FEAT_FPRCVT |
|    1 |   0 |      11 |      10 |      110 | FCVTZS (scalar SIMD&FP) - Half- precision to 64-bit    | FEAT_FPRCVT |
|    1 |   0 |      11 |      10 |      111 | FCVTZU (scalar SIMD&FP) - Half- precision to 64-bit    | FEAT_FPRCVT |
|    1 |   0 |      11 |      11 |      000 | FCVTZS (scalar, integer) - Half- precision to 64-bit   | FEAT_FP16   |

|   sf |   S |   ftype |   rmode |   opcode | Instruction Details                   |            |           | Feature     |
|------|-----|---------|---------|----------|---------------------------------------|------------|-----------|-------------|
|    1 |   0 |      11 |      11 |      001 | FCVTZU (scalar, precision to 64-bit   | integer)   | - Half-   | FEAT_FP16   |
|    1 |   0 |      11 |      11 |      010 | FCVTAS (scalar precision to 64-bit    | SIMD&FP)   | - Half-   | FEAT_FPRCVT |
|    1 |   0 |      11 |      11 |      011 | FCVTAU (scalar precision to 64-bit    | SIMD&FP)   | - Half-   | FEAT_FPRCVT |
|    1 |   0 |      11 |      11 |      100 | SCVTF (scalar half-precision          | SIMD&FP) - | 64-bit to | FEAT_FPRCVT |
|    1 |   0 |      11 |      11 |      101 | UCVTF (scalar SIMD&FP) half-precision | - 64-bit   | to        | FEAT_FPRCVT |

## Floating-point data-processing (1 source)

The encodings in this section are decoded from Data Processing - Scalar Floating-Point and Advanced SIMD.

<!-- image -->

| 31 30   | 29 28   | 24 23   | 22 21   |    | 20   | 15 14    | 10   | 5   |    |
|---------|---------|---------|---------|----|------|----------|------|-----|----|
| M 0     | S 1     | 1 0     | ftype   |  1 |      | opcode 1 | 0 0  | Rn  | Rd |

|   M |   S | ftype   | opcode   | Instruction Details                          | Feature      |
|-----|-----|---------|----------|----------------------------------------------|--------------|
|   0 |   0 | xx      | 1xxxxx   | UNALLOCATED                                  | -            |
|   0 |   0 | 0x      | 0101xx   | UNALLOCATED                                  | -            |
|   0 |   0 | 0x      | 011xxx   | UNALLOCATED                                  | -            |
|   0 |   0 | 00      | 000000   | FMOV(register) -Single-precision             | FEAT_FP      |
|   0 |   0 | 00      | 000001   | FABS (scalar) -Single-precision              | FEAT_FP      |
|   0 |   0 | 00      | 000010   | FNEG (scalar) -Single-precision              | FEAT_FP      |
|   0 |   0 | 00      | 000011   | FSQRT (scalar) -Single-precision             | FEAT_FP      |
|   0 |   0 | 00      | 0001x0   | UNALLOCATED                                  | -            |
|   0 |   0 | 00      | 000101   | FCVT - Single-precision to double- precision | FEAT_FP      |
|   0 |   0 | 00      | 000111   | FCVT - Single-precision to half- precision   | FEAT_FP      |
|   0 |   0 | 00      | 001000   | FRINTN (scalar) -Single-precision            | FEAT_FP      |
|   0 |   0 | 00      | 001001   | FRINTP (scalar) -Single-precision            | FEAT_FP      |
|   0 |   0 | 00      | 001010   | FRINTM (scalar) -Single-precision            | FEAT_FP      |
|   0 |   0 | 00      | 001011   | FRINTZ (scalar) -Single-precision            | FEAT_FP      |
|   0 |   0 | 00      | 001100   | FRINTA (scalar) -Single-precision            | FEAT_FP      |
|   0 |   0 | 00      | 001110   | FRINTX (scalar) -Single-precision            | FEAT_FP      |
|   0 |   0 | 00      | 001111   | FRINTI (scalar) -Single-precision            | FEAT_FP      |
|   0 |   0 | 00      | 010000   | FRINT32Z (scalar) -Single-precision          | FEAT_FRINTTS |

|   M |   S |   ftype | opcode   | Instruction Details                          | Feature      |
|-----|-----|---------|----------|----------------------------------------------|--------------|
|   0 |   0 |      00 | 010001   | FRINT32X (scalar) -Single-precision          | FEAT_FRINTTS |
|   0 |   0 |      00 | 010010   | FRINT64Z (scalar) -Single-precision          | FEAT_FRINTTS |
|   0 |   0 |      00 | 010011   | FRINT64X (scalar) -Single-precision          | FEAT_FRINTTS |
|   0 |   0 |      01 | 000000   | FMOV(register) -Double-precision             | FEAT_FP      |
|   0 |   0 |      01 | 000001   | FABS (scalar) -Double-precision              | FEAT_FP      |
|   0 |   0 |      01 | 000010   | FNEG (scalar) -Double-precision              | FEAT_FP      |
|   0 |   0 |      01 | 000011   | FSQRT (scalar) -Double-precision             | FEAT_FP      |
|   0 |   0 |      01 | 000100   | FCVT - Double-precision to single- precision | FEAT_FP      |
|   0 |   0 |      01 | 000101   | UNALLOCATED                                  | -            |
|   0 |   0 |      01 | 000110   | BFCVT                                        | FEAT_BF16    |
|   0 |   0 |      01 | 000111   | FCVT - Double-precision to half- precision   | FEAT_FP      |
|   0 |   0 |      01 | 001000   | FRINTN (scalar) -Double-precision            | FEAT_FP      |
|   0 |   0 |      01 | 001001   | FRINTP (scalar) -Double-precision            | FEAT_FP      |
|   0 |   0 |      01 | 001010   | FRINTM (scalar) -Double-precision            | FEAT_FP      |
|   0 |   0 |      01 | 001011   | FRINTZ (scalar) -Double-precision            | FEAT_FP      |
|   0 |   0 |      01 | 001100   | FRINTA (scalar) -Double-precision            | FEAT_FP      |
|   0 |   0 |      01 | 001110   | FRINTX (scalar) -Double-precision            | FEAT_FP      |
|   0 |   0 |      01 | 001111   | FRINTI (scalar) -Double-precision            | FEAT_FP      |
|   0 |   0 |      01 | 010000   | FRINT32Z (scalar) -Double-precision          | FEAT_FRINTTS |
|   0 |   0 |      01 | 010001   | FRINT32X (scalar) -Double-precision          | FEAT_FRINTTS |
|   0 |   0 |      01 | 010010   | FRINT64Z (scalar) -Double-precision          | FEAT_FRINTTS |
|   0 |   0 |      01 | 010011   | FRINT64X (scalar) -Double-precision          | FEAT_FRINTTS |
|   0 |   0 |      10 | 0xxxxx   | UNALLOCATED                                  | -            |
|   0 |   0 |      11 | 000000   | FMOV(register) -Half-precision               | FEAT_FP16    |
|   0 |   0 |      11 | 000001   | FABS (scalar) -Half-precision                | FEAT_FP16    |
|   0 |   0 |      11 | 000010   | FNEG (scalar) -Half-precision                | FEAT_FP16    |
|   0 |   0 |      11 | 000011   | FSQRT (scalar) -Half-precision               | FEAT_FP16    |
|   0 |   0 |      11 | 000100   | FCVT - Half-precision to single- precision   | FEAT_FP      |
|   0 |   0 |      11 | 000101   | FCVT - Half-precision to double- precision   | FEAT_FP      |
|   0 |   0 |      11 | 00011x   | UNALLOCATED                                  | -            |
|   0 |   0 |      11 | 001000   | FRINTN (scalar) -Half-precision              | FEAT_FP16    |
|   0 |   0 |      11 | 001001   | FRINTP (scalar) -Half-precision              | FEAT_FP16    |
|   0 |   0 |      11 | 001010   | FRINTM (scalar) -Half-precision              | FEAT_FP16    |
|   0 |   0 |      11 | 001011   | FRINTZ (scalar) -Half-precision              | FEAT_FP16    |
|   0 |   0 |      11 | 001100   | FRINTA (scalar) -Half-precision              | FEAT_FP16    |
|   0 |   0 |      11 | 001110   | FRINTX (scalar) -Half-precision              | FEAT_FP16    |
|   0 |   0 |      11 | 001111   | FRINTI (scalar) -Half-precision              | FEAT_FP16    |
|   0 |   0 |      11 | 01xxxx   | UNALLOCATED                                  | -            |

|   M | S   | ftype   | opcode   | Instruction Details   | Feature   |
|-----|-----|---------|----------|-----------------------|-----------|
|   0 | 0   | != 10   | 001101   | UNALLOCATED           | -         |
|   0 | 1   | xx      | xxxxxx   | UNALLOCATED           | -         |
|   1 | x   | xx      | xxxxxx   | UNALLOCATED           | -         |

## Floating-point compare

The encodings in this section are decoded from Data Processing - Scalar Floating-Point and Advanced SIMD.

<!-- image -->

| 31   |   30 | 29 28   | 24 23   | 22    |   21 |    | 16 15   | 14   | 13 10   | 9   | 5   | 0       |
|------|------|---------|---------|-------|------|----|---------|------|---------|-----|-----|---------|
| M    |    0 | S 1     | 1 1 0   | ftype |    1 | Rm |         | op   | 1 0 0 0 | Rn  |     | opcode2 |

|   M | S   | ftype   | op    | opcode2   | Instruction Details           | Feature   |
|-----|-----|---------|-------|-----------|-------------------------------|-----------|
|   0 | 0   | xx      | 00    | xx001     | UNALLOCATED                   | -         |
|   0 | 0   | xx      | 00    | xx01x     | UNALLOCATED                   | -         |
|   0 | 0   | xx      | 00    | xx1xx     | UNALLOCATED                   | -         |
|   0 | 0   | xx      | != 00 | xxxxx     | UNALLOCATED                   | -         |
|   0 | 0   | 00      | 00    | 00000     | FCMP-Single-precision         | FEAT_FP   |
|   0 | 0   | 00      | 00    | 01000     | FCMP-Single-precision, zero   | FEAT_FP   |
|   0 | 0   | 00      | 00    | 10000     | FCMPE -Single-precision       | FEAT_FP   |
|   0 | 0   | 00      | 00    | 11000     | FCMPE -Single-precision, zero | FEAT_FP   |
|   0 | 0   | 01      | 00    | 00000     | FCMP-Double-precision         | FEAT_FP   |
|   0 | 0   | 01      | 00    | 01000     | FCMP-Double-precision, zero   | FEAT_FP   |
|   0 | 0   | 01      | 00    | 10000     | FCMPE -Double-precision       | FEAT_FP   |
|   0 | 0   | 01      | 00    | 11000     | FCMPE -Double-precision, zero | FEAT_FP   |
|   0 | 0   | 10      | 00    | xx000     | UNALLOCATED                   | -         |
|   0 | 0   | 11      | 00    | 00000     | FCMP-Half-precision           | FEAT_FP16 |
|   0 | 0   | 11      | 00    | 01000     | FCMP-Half-precision, zero     | FEAT_FP16 |
|   0 | 0   | 11      | 00    | 10000     | FCMPE -Half-precision         | FEAT_FP16 |
|   0 | 0   | 11      | 00    | 11000     | FCMPE -Half-precision, zero   | FEAT_FP16 |
|   0 | 1   | xx      | xx    | xxxxx     | UNALLOCATED                   | -         |
|   1 | x   | xx      | xx    | xxxxx     | UNALLOCATED                   | -         |

## Floating-point immediate

The encodings in this section are decoded from Data Processing - Scalar Floating-Point and Advanced SIMD.

<!-- image -->

| 31   |   30 29 |    |   28 | 24 23 22   |       |   21 20 |      | 12 10 9   | 5 4   |    |
|------|---------|----|------|------------|-------|---------|------|-----------|-------|----|
| M    |       0 | S  |    1 | 1 1 0      | ftype |       1 | imm8 | 1 0 0     | imm5  | Rd |

|   M | S   | ftype   | imm5     | Instruction Details                          | Feature   |
|-----|-----|---------|----------|----------------------------------------------|-----------|
|   0 | 0   | xx      | != 00000 | UNALLOCATED                                  | -         |
|   0 | 0   | 00      | 00000    | FMOV (scalar, immediate) - Single- precision | FEAT_FP   |
|   0 | 0   | 01      | 00000    | FMOV (scalar, immediate) - Double- precision | FEAT_FP   |
|   0 | 0   | 10      | 00000    | UNALLOCATED                                  | -         |
|   0 | 0   | 11      | 00000    | FMOV (scalar, immediate) - Half- precision   | FEAT_FP16 |
|   0 | 1   | xx      | xxxxx    | UNALLOCATED                                  | -         |
|   1 | x   | xx      | xxxxx    | UNALLOCATED                                  | -         |

## Floating-point conditional compare

The encodings in this section are decoded from Data Processing - Scalar Floating-Point and Advanced SIMD.

| 31 30   | 29   | 28    | 24 23 22   | 21    |    | 16 15   | 12 11 10   | 5   | 4   | 0    |
|---------|------|-------|------------|-------|----|---------|------------|-----|-----|------|
| M 0     | S    | 1 1 1 | 1 0        | ftype |  1 | Rm      | 0 1        | Rn  | op  | nzcv |

|   M | S   | ftype   | op   | Instruction Details      | Feature   |
|-----|-----|---------|------|--------------------------|-----------|
|   0 | 0   | 00      | 0    | FCCMP-Single-precision   | FEAT_FP   |
|   0 | 0   | 00      | 1    | FCCMPE -Single-precision | FEAT_FP   |
|   0 | 0   | 01      | 0    | FCCMP-Double-precision   | FEAT_FP   |
|   0 | 0   | 01      | 1    | FCCMPE -Double-precision | FEAT_FP   |
|   0 | 0   | 10      | x    | UNALLOCATED              | -         |
|   0 | 0   | 11      | 0    | FCCMP-Half-precision     | FEAT_FP16 |
|   0 | 0   | 11      | 1    | FCCMPE -Half-precision   | FEAT_FP16 |
|   0 | 1   | xx      | x    | UNALLOCATED              | -         |
|   1 | x   | xx      | x    | UNALLOCATED              | -         |

## Floating-point data-processing (2 source)

The encodings in this section are decoded from Data Processing - Scalar Floating-Point and Advanced SIMD.

| 31   | 30 29   | 24 23 22   | 21    |    |    | 16 15   | 11 10 9 5   | 4   | 0   |
|------|---------|------------|-------|----|----|---------|-------------|-----|-----|
| M    | 0 S     | 1 1 1 0    | ftype |  1 | Rm | opcode  | 1 0         | Rn  | Rd  |

|   M |   S | ftype   | opcode   | Instruction Details              | Feature   |
|-----|-----|---------|----------|----------------------------------|-----------|
|   0 |   0 | 00      | 0000     | FMUL(scalar) -Single-precision   | FEAT_FP   |
|   0 |   0 | 00      | 0001     | FDIV (scalar) -Single-precision  | FEAT_FP   |
|   0 |   0 | 00      | 0010     | FADD(scalar) -Single-precision   | FEAT_FP   |
|   0 |   0 | 00      | 0011     | FSUB (scalar) -Single-precision  | FEAT_FP   |
|   0 |   0 | 00      | 0100     | FMAX(scalar) -Single-precision   | FEAT_FP   |
|   0 |   0 | 00      | 0101     | FMIN (scalar) -Single-precision  | FEAT_FP   |
|   0 |   0 | 00      | 0110     | FMAXNM(scalar) -Single-precision | FEAT_FP   |
|   0 |   0 | 00      | 0111     | FMINNM(scalar) -Single-precision | FEAT_FP   |
|   0 |   0 | 00      | 1000     | FNMUL(scalar) -Single-precision  | FEAT_FP   |
|   0 |   0 | 01      | 0000     | FMUL(scalar) -Double-precision   | FEAT_FP   |
|   0 |   0 | 01      | 0001     | FDIV (scalar) -Double-precision  | FEAT_FP   |
|   0 |   0 | 01      | 0010     | FADD(scalar) -Double-precision   | FEAT_FP   |
|   0 |   0 | 01      | 0011     | FSUB (scalar) -Double-precision  | FEAT_FP   |
|   0 |   0 | 01      | 0100     | FMAX(scalar) -Double-precision   | FEAT_FP   |
|   0 |   0 | 01      | 0101     | FMIN (scalar) -Double-precision  | FEAT_FP   |
|   0 |   0 | 01      | 0110     | FMAXNM(scalar) -Double-precision | FEAT_FP   |
|   0 |   0 | 01      | 0111     | FMINNM(scalar) -Double-precision | FEAT_FP   |
|   0 |   0 | 01      | 1000     | FNMUL(scalar) -Double-precision  | FEAT_FP   |
|   0 |   0 | 10      | xxxx     | UNALLOCATED                      | -         |
|   0 |   0 | 11      | 0000     | FMUL(scalar) -Half-precision     | FEAT_FP16 |
|   0 |   0 | 11      | 0001     | FDIV (scalar) -Half-precision    | FEAT_FP16 |
|   0 |   0 | 11      | 0010     | FADD(scalar) -Half-precision     | FEAT_FP16 |
|   0 |   0 | 11      | 0011     | FSUB (scalar) -Half-precision    | FEAT_FP16 |
|   0 |   0 | 11      | 0100     | FMAX(scalar) -Half-precision     | FEAT_FP16 |
|   0 |   0 | 11      | 0101     | FMIN (scalar) -Half-precision    | FEAT_FP16 |
|   0 |   0 | 11      | 0110     | FMAXNM(scalar) -Half-precision   | FEAT_FP16 |
|   0 |   0 | 11      | 0111     | FMINNM(scalar) -Half-precision   | FEAT_FP16 |
|   0 |   0 | 11      | 1000     | FNMUL(scalar) -Half-precision    | FEAT_FP16 |
|   0 |   0 | != 10   | 1001     | UNALLOCATED                      | -         |
|   0 |   0 | != 10   | 101x     | UNALLOCATED                      | -         |
|   0 |   0 | != 10   | 11xx     | UNALLOCATED                      | -         |
|   0 |   1 | xx      | xxxx     | UNALLOCATED                      | -         |

|   M | S ftype   | opcode   | Instruction Details   | Feature   |
|-----|-----------|----------|-----------------------|-----------|
|   1 | x         | xx xxxx  | UNALLOCATED           | -         |

## Floating-point conditional select

The encodings in this section are decoded from Data Processing - Scalar Floating-Point and Advanced SIMD.

<!-- image -->

| 31 30   | 29   | 28   | 24 23   | 22 21   | 16   | 15   | 12 11 10   | 5   | 0   |
|---------|------|------|---------|---------|------|------|------------|-----|-----|
| M 0     | S    | 1 1  | 1 1 0   | ftype 1 | Rm   | cond | 1 1        | Rn  | Rd  |

|   M | S   | ftype   | Instruction Details     | Feature   |
|-----|-----|---------|-------------------------|-----------|
|   0 | 0   | 00      | FCSEL -Single-precision | FEAT_FP   |
|   0 | 0   | 01      | FCSEL -Double-precision | FEAT_FP   |
|   0 | 0   | 10      | UNALLOCATED             | -         |
|   0 | 0   | 11      | FCSEL -Half-precision   | FEAT_FP16 |
|   0 | 1   | xx      | UNALLOCATED             | -         |
|   1 | x   | xx      | UNALLOCATED             | -         |

## Floating-point data-processing (3 source)

The encodings in this section are decoded from Data Processing - Scalar Floating-Point and Advanced SIMD.

<!-- image -->

| 31 30   | 29   |   28 | 24    | 23 22   | 21   | 20   | 16   | 15 14   | 10 9   | 5   | 0   |
|---------|------|------|-------|---------|------|------|------|---------|--------|-----|-----|
| M 0     | S    |    1 | 1 1 1 | ftype   | o1   | Rm   | o0   | Ra      | Rn     |     | Rd  |

|   M |   S |   ftype | o1   | o0   | Instruction Details     | Feature   |
|-----|-----|---------|------|------|-------------------------|-----------|
|   0 |   0 |      00 | 0    | 0    | FMADD-Single-precision  | FEAT_FP   |
|   0 |   0 |      00 | 0    | 1    | FMSUB-Single-precision  | FEAT_FP   |
|   0 |   0 |      00 | 1    | 0    | FNMADD-Single-precision | FEAT_FP   |
|   0 |   0 |      00 | 1    | 1    | FNMSUB-Single-precision | FEAT_FP   |
|   0 |   0 |      01 | 0    | 0    | FMADD-Double-precision  | FEAT_FP   |
|   0 |   0 |      01 | 0    | 1    | FMSUB-Double-precision  | FEAT_FP   |
|   0 |   0 |      01 | 1    | 0    | FNMADD-Double-precision | FEAT_FP   |
|   0 |   0 |      01 | 1    | 1    | FNMSUB-Double-precision | FEAT_FP   |
|   0 |   0 |      10 | x    | x    | UNALLOCATED             | -         |

## Loads and Stores

Loads and Stores

The encodings in this section are decoded from A64 instruction set encoding.

<!-- image -->

| 31   | 28 27 26 25 24   |
|------|------------------|
| op0  | 1 op1 0          |

| op0   |   op1 | op2             | Instruction details                                         |
|-------|-------|-----------------|-------------------------------------------------------------|
| 0000  |     0 | 1xx1xxxxxxxxxxx | UNALLOCATED                                                 |
| 0001  |     1 | 1xx1xxxxxxxxxxx | UNALLOCATED                                                 |
| 0x00  |     0 | 00x1xxxxxxxxxxx | Compare and swap pair                                       |
| 0x00  |     0 | 10x0xxxxxxxxxxx | UNALLOCATED                                                 |
| 0x00  |     0 | 11x0xxxxxxxxxxx | Compare and swap pair (unprivileged)                        |
| 0x00  |     1 | 00x000000xxxxxx | Advanced SIMD load/store multiple structures                |
| 0x00  |     1 | 00x000001xxxxxx | UNALLOCATED                                                 |
| 0x00  |     1 | 01x0xxxxxxxxxxx | Advanced SIMD load/store multiple structures (post-indexed) |
| 0x00  |     1 | 0xx1xxxxxxxxxxx | UNALLOCATED                                                 |
| 0x00  |     1 | 10x10001xxxxxxx | UNALLOCATED                                                 |
| 0x00  |     1 | 10x1001xxxxxxxx | UNALLOCATED                                                 |
| 0x00  |     1 | 10x101xxxxxxxxx | UNALLOCATED                                                 |
| 0x00  |     1 | 10x11xxxxxxxxxx | UNALLOCATED                                                 |
| 0x00  |     1 | 10xx0000xxxxxxx | Advanced SIMDload/store single structure                    |
| 0x00  |     1 | 11xxxxxxxxxxxxx | Advanced SIMDload/store single structure (post-indexed)     |
| 0x00  |     1 | x0x00001xxxxxxx | UNALLOCATED                                                 |
| 0x00  |     1 | x0x0001xxxxxxxx | UNALLOCATED                                                 |
| 0x00  |     1 | x0x001xxxxxxxxx | UNALLOCATED                                                 |
| 0x00  |     1 | x0x01xxxxxxxxxx | UNALLOCATED                                                 |

|   M | S   | ftype   | o1   | o0   | Instruction Details   | Feature   |
|-----|-----|---------|------|------|-----------------------|-----------|
|   0 | 0   | 11      | 0    | 0    | FMADD-Half-precision  | FEAT_FP16 |
|   0 | 0   | 11      | 0    | 1    | FMSUB-Half-precision  | FEAT_FP16 |
|   0 | 0   | 11      | 1    | 0    | FNMADD-Half-precision | FEAT_FP16 |
|   0 | 0   | 11      | 1    | 1    | FNMSUB-Half-precision | FEAT_FP16 |
|   0 | 1   | xx      | x    | x    | UNALLOCATED           | -         |
|   1 | x   | xx      | x    | x    | UNALLOCATED           | -         |

| op0   |   op1 | op2             | Instruction details                          |
|-------|-------|-----------------|----------------------------------------------|
| 0x01  |     0 | 1xx0xxxxxxxxx11 | UNALLOCATED                                  |
| 0x01  |     0 | 1xx1xxxxx000010 | RCWcompare and swap                          |
| 0x01  |     0 | 1xx1xxxxx000011 | RCWcompare and swap pair                     |
| 0x01  |     0 | 1xx1xxxxx00011x | UNALLOCATED                                  |
| 0x01  |     0 | 1xx1xxxxx001x1x | UNALLOCATED                                  |
| 0x01  |     0 | 1xx1xxxxx01xx1x | UNALLOCATED                                  |
| 0x01  |     0 | 1xx1xxxxx1xxx1x | UNALLOCATED                                  |
| 0x01  |     0 | 1xx1xxxxxxxxx00 | 128-bit atomic memory operations             |
| 0x01  |     0 | 1xx1xxxxxxxxx01 | Atomic memory operations (unprivileged)      |
| 1001  |     0 | 1xx0xxxxxxxxx11 | UNALLOCATED                                  |
| 1001  |     1 | 1xx1xxxxxxxxxxx | UNALLOCATED                                  |
| 100x  |     0 | 1xx1xxxxxxxxxxx | UNALLOCATED                                  |
| 1101  |     0 | 1000111110xxx11 | GCS load/store                               |
| 1101  |     0 | 1100111110xxx11 | UNALLOCATED                                  |
| 1101  |     0 | 1x000xxxxxxxx11 | UNALLOCATED                                  |
| 1101  |     0 | 1x0010xxxxxxx11 | UNALLOCATED                                  |
| 1101  |     0 | 1x00110xxxxxx11 | UNALLOCATED                                  |
| 1101  |     0 | 1x001110xxxxx11 | UNALLOCATED                                  |
| 1101  |     0 | 1x0011110xxxx11 | UNALLOCATED                                  |
| 1101  |     0 | 1x00111111xxx11 | UNALLOCATED                                  |
| 1101  |     0 | 1x10xxxxxxxxx11 | UNALLOCATED                                  |
| 1101  |     0 | 1xx1xxxxxxxxxxx | Load/store memory tags                       |
| 1x00  |     0 | 00x1xxxxxxxxxxx | Load/store exclusive pair                    |
| 1x00  |     0 | 10x0xxxxxxxxxxx | Load/store exclusive register (unprivileged) |
| 1x00  |     0 | 11x0xxxxxxxxxxx | Compare and swap (unprivileged)              |
| 1x00  |     1 | xxxxxxxxxxxxxxx | UNALLOCATED                                  |
| x100  |     0 | 1xx1xxxxxxxxxxx | UNALLOCATED                                  |
| x101  |     1 | 1xx1xxxxxxxxxxx | UNALLOCATED                                  |
| xx00  |     0 | 00x0xxxxxxxxxxx | Load/store exclusive register                |
| xx00  |     0 | 01x0xxxxxxxxxxx | Load/store ordered                           |
| xx00  |     0 | 01x1xxxxxxxxxxx | Compare and swap                             |
| xx01  |     0 | 10x0xxxxxxxxx10 | Load/store ordered register pair             |
| xx01  |     0 | 11x000000000010 | Load/store ordered (writeback)               |
| xx01  |     0 | 11x000000000110 | UNALLOCATED                                  |
| xx01  |     0 | 11x000000001x10 | UNALLOCATED                                  |
| xx01  |     0 | 11x00000001xx10 | UNALLOCATED                                  |
| xx01  |     0 | 11x0000001xxx10 | UNALLOCATED                                  |
| xx01  |     0 | 11x000001xxxx10 | UNALLOCATED                                  |
| xx01  |     0 | 11x00001xxxxx10 | UNALLOCATED                                  |
| xx01  |     0 | 11x0001xxxxxx10 | UNALLOCATED                                  |

## Compare and swap pair

The encodings in this section are decoded from Loads and Stores.

<!-- image -->

|   31 | 30 29   | 27 26   | 25   |   23 | 22   | 21   |    |    | 16 15   |     | 10 9   | 5   | 0   |
|------|---------|---------|------|------|------|------|----|----|---------|-----|--------|-----|-----|
|    0 | sz 0    | 0 1 0   | 0 0  |    0 | L    |      |  1 | Rs | o0      | Rt2 | Rn     |     | Rt  |

| sz   | L   | o0   | Rt2      | Instruction Details                       | Feature   |
|------|-----|------|----------|-------------------------------------------|-----------|
| x    | x   | x    | != 11111 | UNALLOCATED                               | -         |
| 0    | 0   | 0    | 11111    | CASP, CASPA, CASPAL, CASPL -32- bit CASP  | FEAT_LSE  |
| 0    | 0   | 1    | 11111    | CASP, CASPA, CASPAL, CASPL -32- bit CASPL | FEAT_LSE  |
| 0    | 1   | 0    | 11111    | CASP, CASPA, CASPAL, CASPL -32- bit CASPA | FEAT_LSE  |

| op0   | op1   | op2             | Instruction details                           |
|-------|-------|-----------------|-----------------------------------------------|
| xx01  | 0     | 11x001xxxxxxx10 | UNALLOCATED                                   |
| xx01  | 0     | 11x01xxxxxxxx10 | UNALLOCATED                                   |
| xx01  | 0     | 1xx0xxxxxxxxx00 | Load/store ordered (unscaled immediate)       |
| xx01  | 1     | 1xx0xxxxxxxxx00 | UNALLOCATED                                   |
| xx01  | 1     | 1xx0xxxxxxxxx10 | Load/store ordered (SIMD&FP)                  |
| xx01  | 1     | 1xx0xxxxxxxxx11 | UNALLOCATED                                   |
| xx01  | x     | 0xxxxxxxxxxxxxx | Load register (literal)                       |
| xx01  | x     | 1xx0xxxxxxxxx01 | Memory Copy and Memory Set                    |
| xx10  | x     | 00xxxxxxxxxxxxx | Load/store no-allocate pair (offset)          |
| xx10  | x     | 01xxxxxxxxxxxxx | Load/store register pair (post-indexed)       |
| xx10  | x     | 10xxxxxxxxxxxxx | Load/store register pair (offset)             |
| xx10  | x     | 11xxxxxxxxxxxxx | Load/store register pair (pre-indexed)        |
| xx11  | x     | 0xx0xxxxxxxxx00 | Load/store register (unscaled immediate)      |
| xx11  | x     | 0xx0xxxxxxxxx01 | Load/store register (immediate post- indexed) |
| xx11  | x     | 0xx0xxxxxxxxx10 | Load/store register (unprivileged)            |
| xx11  | x     | 0xx0xxxxxxxxx11 | Load/store register (immediate pre- indexed)  |
| xx11  | x     | 0xx1xxxxxxxxx00 | Atomic memory operations                      |
| xx11  | x     | 0xx1xxxxxxxxx10 | Load/store register (register offset)         |
| xx11  | x     | 0xx1xxxxxxxxxx1 | Load/store register (pac)                     |
| xx11  | x     | 1xxxxxxxxxxxxxx | Load/store register (unsigned immediate)      |

|   sz |   L |   o0 |   Rt2 | Instruction Details                        | Feature   |
|------|-----|------|-------|--------------------------------------------|-----------|
|    0 |   1 |    1 | 11111 | CASP, CASPA, CASPAL, CASPL -32- bit CASPAL | FEAT_LSE  |
|    1 |   0 |    0 | 11111 | CASP, CASPA, CASPAL, CASPL -64- bit CASP   | FEAT_LSE  |
|    1 |   0 |    1 | 11111 | CASP, CASPA, CASPAL, CASPL -64- bit CASPL  | FEAT_LSE  |
|    1 |   1 |    0 | 11111 | CASP, CASPA, CASPAL, CASPL -64- bit CASPA  | FEAT_LSE  |
|    1 |   1 |    1 | 11111 | CASP, CASPA, CASPAL, CASPL -64- bit CASPAL | FEAT_LSE  |

## Compare and swap pair (unprivileged)

The encodings in this section are decoded from Loads and Stores.

<!-- image -->

|   sz | L   | o0   | Rt2      | Instruction Details                   | Feature   |
|------|-----|------|----------|---------------------------------------|-----------|
|    0 | x   | x    | xxxxx    | UNALLOCATED                           | -         |
|    1 | x   | x    | != 11111 | UNALLOCATED                           | -         |
|    1 | 0   | 0    | 11111    | CASPT, CASPAT,CASPALT,CASPLT- CASPT   | FEAT_LSUI |
|    1 | 0   | 1    | 11111    | CASPT, CASPAT,CASPALT,CASPLT- CASPLT  | FEAT_LSUI |
|    1 | 1   | 0    | 11111    | CASPT, CASPAT,CASPALT,CASPLT- CASPAT  | FEAT_LSUI |
|    1 | 1   | 1    | 11111    | CASPT, CASPAT,CASPALT,CASPLT- CASPALT | FEAT_LSUI |

## Advanced SIMD load/store multiple structures

The encodings in this section are decoded from Loads and Stores.

<!-- image -->

| L   | opcode   | Instruction Details                         | Feature      |
|-----|----------|---------------------------------------------|--------------|
| x   | x0x1     | UNALLOCATED                                 | -            |
| x   | 0101     | UNALLOCATED                                 | -            |
| x   | 11xx     | UNALLOCATED                                 | -            |
| 0   | 0000     | ST4 (multiple structures)                   | FEAT_AdvSIMD |
| 0   | 0010     | ST1 (multiple structures) -Four registers   | FEAT_AdvSIMD |
| 0   | 0100     | ST3 (multiple structures)                   | FEAT_AdvSIMD |
| 0   | 0110     | ST1 (multiple structures) - Three registers | FEAT_AdvSIMD |
| 0   | 0111     | ST1 (multiple structures) -Oneregister      | FEAT_AdvSIMD |
| 0   | 1000     | ST2 (multiple structures)                   | FEAT_AdvSIMD |
| 0   | 1010     | ST1 (multiple structures) -Tworegisters     | FEAT_AdvSIMD |
| 1   | 0000     | LD4 (multiple structures)                   | FEAT_AdvSIMD |
| 1   | 0010     | LD1 (multiple structures) -Four registers   | FEAT_AdvSIMD |
| 1   | 0100     | LD3 (multiple structures)                   | FEAT_AdvSIMD |
| 1   | 0110     | LD1 (multiple structures) - Three registers | FEAT_AdvSIMD |
| 1   | 0111     | LD1 (multiple structures) -Oneregister      | FEAT_AdvSIMD |
| 1   | 1000     | LD2 (multiple structures)                   | FEAT_AdvSIMD |
| 1   | 1010     | LD1 (multiple structures) -Tworegisters     | FEAT_AdvSIMD |

## Advanced SIMD load/store multiple structures (post-indexed)

The encodings in this section are decoded from Loads and Stores.

<!-- image -->

|   31 | 30 29   | 27 26 25   | 23    | 22 21   | 20   |    | 15   | 12 11 10   | 9 5   | 4   | 0   |
|------|---------|------------|-------|---------|------|----|------|------------|-------|-----|-----|
|    0 | Q 0 0   | 1 1        | 0 0 1 | L 0     |      | Rm |      | opcode     | size  | Rn  | Rt  |

| L   | Rm    | opcode   | Instruction Details                                        | Feature      |
|-----|-------|----------|------------------------------------------------------------|--------------|
| x   | xxxxx | x0x1     | UNALLOCATED                                                | -            |
| x   | xxxxx | 0101     | UNALLOCATED                                                | -            |
| x   | xxxxx | 11xx     | UNALLOCATED                                                | -            |
| 0   | 11111 | 0000     | ST4 (multiple structures) - Immediate offset               | FEAT_AdvSIMD |
| 0   | 11111 | 0010     | ST1 (multiple structures) -Fourregisters, immediate offset | FEAT_AdvSIMD |
| 0   | 11111 | 0100     | ST3 (multiple structures) - Immediate offset               | FEAT_AdvSIMD |

|   L | Rm       |   opcode | Instruction Details                                           | Feature      |
|-----|----------|----------|---------------------------------------------------------------|--------------|
|   0 | 11111    |     0110 | ST1 (multiple structures) - Three registers, immediate offset | FEAT_AdvSIMD |
|   0 | 11111    |     0111 | ST1 (multiple structures) -One register, immediate offset     | FEAT_AdvSIMD |
|   0 | 11111    |     1000 | ST2 (multiple structures) - Immediate offset                  | FEAT_AdvSIMD |
|   0 | 11111    |     1010 | ST1 (multiple structures) -Tworegisters, immediate offset     | FEAT_AdvSIMD |
|   0 | != 11111 |     0000 | ST4 (multiple structures) -Register offset                    | FEAT_AdvSIMD |
|   0 | != 11111 |     0010 | ST1 (multiple structures) -Fourregisters, register offset     | FEAT_AdvSIMD |
|   0 | != 11111 |     0100 | ST3 (multiple structures) -Register offset                    | FEAT_AdvSIMD |
|   0 | != 11111 |     0110 | ST1 (multiple structures) - Three registers, register offset  | FEAT_AdvSIMD |
|   0 | != 11111 |     0111 | ST1 (multiple structures) -One register, register offset      | FEAT_AdvSIMD |
|   0 | != 11111 |     1000 | ST2 (multiple structures) -Register offset                    | FEAT_AdvSIMD |
|   0 | != 11111 |     1010 | ST1 (multiple structures) -Tworegisters, register offset      | FEAT_AdvSIMD |
|   1 | 11111    |     0000 | LD4 (multiple structures) - Immediate offset                  | FEAT_AdvSIMD |
|   1 | 11111    |     0010 | LD1(multiple structures) -Fourregisters, immediate offset     | FEAT_AdvSIMD |
|   1 | 11111    |     0100 | LD3 (multiple structures) - Immediate offset                  | FEAT_AdvSIMD |
|   1 | 11111    |     0110 | LD1 (multiple structures) - Three registers, immediate offset | FEAT_AdvSIMD |
|   1 | 11111    |     0111 | LD1 (multiple structures) -One register, immediate offset     | FEAT_AdvSIMD |
|   1 | 11111    |     1000 | LD2 (multiple structures) - Immediate offset                  | FEAT_AdvSIMD |
|   1 | 11111    |     1010 | LD1(multiple structures) -Tworegisters, immediate offset      | FEAT_AdvSIMD |
|   1 | != 11111 |     0000 | LD4 (multiple structures) - Register offset                   | FEAT_AdvSIMD |
|   1 | != 11111 |     0010 | LD1(multiple structures) -Fourregisters, register offset      | FEAT_AdvSIMD |
|   1 | != 11111 |     0100 | LD3 (multiple structures) - Register offset                   | FEAT_AdvSIMD |
|   1 | != 11111 |     0110 | LD1 (multiple structures) - Three registers, register offset  | FEAT_AdvSIMD |
|   1 | != 11111 |     0111 | LD1 (multiple structures) -One register, register offset      | FEAT_AdvSIMD |
|   1 | != 11111 |     1000 | LD2 (multiple structures) - Register offset                   | FEAT_AdvSIMD |
|   1 | != 11111 |     1010 | LD1(multiple structures) -Tworegisters, register offset       | FEAT_AdvSIMD |

## Advanced SIMD load/store single structure

The encodings in this section are decoded from Loads and Stores.

<!-- image -->

|   31 | 30 29   | 27 26   | 25   |   23 | 22   | 21   | 20   |       |   17 | 16   | 15   | 13     | 11 10 9   | 5   | 4   | 0   |
|------|---------|---------|------|------|------|------|------|-------|------|------|------|--------|-----------|-----|-----|-----|
|    0 | Q 0     | 0 1 1   | 0 1  |    0 | L    |      | R    | 0 0 0 |    0 | o2   |      | opcode | size      | Rn  |     | Rt  |

| L   | R   |   o2 | opcode   | S   | size   | Instruction Details            | Feature                    |
|-----|-----|------|----------|-----|--------|--------------------------------|----------------------------|
| x   | x   |    0 | 01x      | x   | x1     | UNALLOCATED                    | -                          |
| x   | x   |    0 | 10x      | x   | 1x     | UNALLOCATED                    | -                          |
| x   | x   |    0 | 10x      | 1   | 01     | UNALLOCATED                    | -                          |
| x   | 0   |    1 | 100      | x   | != 01  | UNALLOCATED                    | -                          |
| x   | 0   |    1 | 100      | 1   | 01     | UNALLOCATED                    | -                          |
| x   | 0   |    1 | != 100   | x   | xx     | UNALLOCATED                    | -                          |
| x   | 1   |    1 | xxx      | x   | xx     | UNALLOCATED                    | -                          |
| 0   | x   |    0 | 11x      | x   | xx     | UNALLOCATED                    | -                          |
| 0   | 0   |    0 | 000      | x   | xx     | ST1 (single structure) -8-bit  | FEAT_AdvSIMD               |
| 0   | 0   |    0 | 001      | x   | xx     | ST3 (single structure) -8-bit  | FEAT_AdvSIMD               |
| 0   | 0   |    0 | 010      | x   | x0     | ST1 (single structure) -16-bit | FEAT_AdvSIMD               |
| 0   | 0   |    0 | 011      | x   | x0     | ST3 (single structure) -16-bit | FEAT_AdvSIMD               |
| 0   | 0   |    0 | 100      | x   | 00     | ST1 (single structure) -32-bit | FEAT_AdvSIMD               |
| 0   | 0   |    0 | 100      | 0   | 01     | ST1 (single structure) -64-bit | FEAT_AdvSIMD               |
| 0   | 0   |    0 | 101      | x   | 00     | ST3 (single structure) -32-bit | FEAT_AdvSIMD               |
| 0   | 0   |    0 | 101      | 0   | 01     | ST3 (single structure) -64-bit | FEAT_AdvSIMD               |
| 0   | 0   |    1 | 100      | 0   | 01     | STL1 (SIMD&FP)                 | FEAT_AdvSIMD &&FEAT_LRCPC3 |
| 0   | 1   |    0 | 000      | x   | xx     | ST2 (single structure) -8-bit  | FEAT_AdvSIMD               |
| 0   | 1   |    0 | 001      | x   | xx     | ST4 (single structure) -8-bit  | FEAT_AdvSIMD               |
| 0   | 1   |    0 | 010      | x   | x0     | ST2 (single structure) -16-bit | FEAT_AdvSIMD               |
| 0   | 1   |    0 | 011      | x   | x0     | ST4 (single structure) -16-bit | FEAT_AdvSIMD               |
| 0   | 1   |    0 | 100      | x   | 00     | ST2 (single structure) -32-bit | FEAT_AdvSIMD               |
| 0   | 1   |    0 | 100      | 0   | 01     | ST2 (single structure) -64-bit | FEAT_AdvSIMD               |
| 0   | 1   |    0 | 101      | x   | 00     | ST4 (single structure) -32-bit | FEAT_AdvSIMD               |
| 0   | 1   |    0 | 101      | 0   | 01     | ST4 (single structure) -64-bit | FEAT_AdvSIMD               |
| 1   | x   |    0 | 11x      | 1   | xx     | UNALLOCATED                    | -                          |
| 1   | 0   |    0 | 000      | x   | xx     | LD1 (single structure) -8-bit  | FEAT_AdvSIMD               |
| 1   | 0   |    0 | 001      | x   | xx     | LD3 (single structure) -8-bit  | FEAT_AdvSIMD               |
| 1   | 0   |    0 | 010      | x   | x0     | LD1 (single structure) -16-bit | FEAT_AdvSIMD               |
| 1   | 0   |    0 | 011      | x   | x0     | LD3 (single structure) -16-bit | FEAT_AdvSIMD               |

|   L |   R |   o2 |   opcode | S   | size   | Instruction Details            | Feature                    |
|-----|-----|------|----------|-----|--------|--------------------------------|----------------------------|
|   1 |   0 |    0 |      100 | x   | 00     | LD1 (single structure) -32-bit | FEAT_AdvSIMD               |
|   1 |   0 |    0 |      100 | 0   | 01     | LD1 (single structure) -64-bit | FEAT_AdvSIMD               |
|   1 |   0 |    0 |      101 | x   | 00     | LD3 (single structure) -32-bit | FEAT_AdvSIMD               |
|   1 |   0 |    0 |      101 | 0   | 01     | LD3 (single structure) -64-bit | FEAT_AdvSIMD               |
|   1 |   0 |    0 |      110 | 0   | xx     | LD1R                           | FEAT_AdvSIMD               |
|   1 |   0 |    0 |      111 | 0   | xx     | LD3R                           | FEAT_AdvSIMD               |
|   1 |   0 |    1 |      100 | 0   | 01     | LDAP1 (SIMD&FP)                | FEAT_AdvSIMD &&FEAT_LRCPC3 |
|   1 |   1 |    0 |      000 | x   | xx     | LD2 (single structure) -8-bit  | FEAT_AdvSIMD               |
|   1 |   1 |    0 |      001 | x   | xx     | LD4 (single structure) -8-bit  | FEAT_AdvSIMD               |
|   1 |   1 |    0 |      010 | x   | x0     | LD2 (single structure) -16-bit | FEAT_AdvSIMD               |
|   1 |   1 |    0 |      011 | x   | x0     | LD4 (single structure) -16-bit | FEAT_AdvSIMD               |
|   1 |   1 |    0 |      100 | x   | 00     | LD2 (single structure) -32-bit | FEAT_AdvSIMD               |
|   1 |   1 |    0 |      100 | 0   | 01     | LD2 (single structure) -64-bit | FEAT_AdvSIMD               |
|   1 |   1 |    0 |      101 | x   | 00     | LD4 (single structure) -32-bit | FEAT_AdvSIMD               |
|   1 |   1 |    0 |      101 | 0   | 01     | LD4 (single structure) -64-bit | FEAT_AdvSIMD               |
|   1 |   1 |    0 |      110 | 0   | xx     | LD2R                           | FEAT_AdvSIMD               |
|   1 |   1 |    0 |      111 | 0   | xx     | LD4R                           | FEAT_AdvSIMD               |

## Advanced SIMD load/store single structure (post-indexed)

The encodings in this section are decoded from Loads and Stores.

<!-- image -->

| L   | R   | Rm    | opcode   | S   | size   | Instruction Details                              | Feature      |
|-----|-----|-------|----------|-----|--------|--------------------------------------------------|--------------|
| x   | x   | xxxxx | 01x      | x   | x1     | UNALLOCATED                                      | -            |
| x   | x   | xxxxx | 10x      | x   | 1x     | UNALLOCATED                                      | -            |
| x   | x   | xxxxx | 10x      | 1   | 01     | UNALLOCATED                                      | -            |
| 0   | x   | xxxxx | 11x      | x   | xx     | UNALLOCATED                                      | -            |
| 0   | 0   | 11111 | 000      | x   | xx     | ST1 (single structure) -8-bit, immediate offset  | FEAT_AdvSIMD |
| 0   | 0   | 11111 | 001      | x   | xx     | ST3 (single structure) -8-bit, immediate offset  | FEAT_AdvSIMD |
| 0   | 0   | 11111 | 010      | x   | x0     | ST1 (single structure) -16-bit, immediate offset | FEAT_AdvSIMD |
| 0   | 0   | 11111 | 011      | x   | x0     | ST3 (single structure) -16-bit, immediate offset | FEAT_AdvSIMD |

|   L |   R | Rm       |   opcode | S   | size   | Instruction Details                              | Feature      |
|-----|-----|----------|----------|-----|--------|--------------------------------------------------|--------------|
|   0 |   0 | 11111    |      100 | x   | 00     | ST1 (single structure) -32-bit, immediate offset | FEAT_AdvSIMD |
|   0 |   0 | 11111    |      100 | 0   | 01     | ST1 (single structure) -64-bit, immediate offset | FEAT_AdvSIMD |
|   0 |   0 | 11111    |      101 | x   | 00     | ST3 (single structure) -32-bit, immediate offset | FEAT_AdvSIMD |
|   0 |   0 | 11111    |      101 | 0   | 01     | ST3 (single structure) -64-bit, immediate offset | FEAT_AdvSIMD |
|   0 |   0 | != 11111 |      000 | x   | xx     | ST1 (single structure) - 8-bit, register offset  | FEAT_AdvSIMD |
|   0 |   0 | != 11111 |      001 | x   | xx     | ST3 (single structure) - 8-bit, register offset  | FEAT_AdvSIMD |
|   0 |   0 | != 11111 |      010 | x   | x0     | ST1 (single structure) - 16-bit, register offset | FEAT_AdvSIMD |
|   0 |   0 | != 11111 |      011 | x   | x0     | ST3 (single structure) - 16-bit, register offset | FEAT_AdvSIMD |
|   0 |   0 | != 11111 |      100 | x   | 00     | ST1 (single structure) - 32-bit, register offset | FEAT_AdvSIMD |
|   0 |   0 | != 11111 |      100 | 0   | 01     | ST1 (single structure) - 64-bit, register offset | FEAT_AdvSIMD |
|   0 |   0 | != 11111 |      101 | x   | 00     | ST3 (single structure) - 32-bit, register offset | FEAT_AdvSIMD |
|   0 |   0 | != 11111 |      101 | 0   | 01     | ST3 (single structure) - 64-bit, register offset | FEAT_AdvSIMD |
|   0 |   1 | 11111    |      000 | x   | xx     | ST2 (single structure) -8-bit, immediate offset  | FEAT_AdvSIMD |
|   0 |   1 | 11111    |      001 | x   | xx     | ST4 (single structure) -8-bit, immediate offset  | FEAT_AdvSIMD |
|   0 |   1 | 11111    |      010 | x   | x0     | ST2 (single structure) -16-bit, immediate offset | FEAT_AdvSIMD |
|   0 |   1 | 11111    |      011 | x   | x0     | ST4 (single structure) -16-bit, immediate offset | FEAT_AdvSIMD |
|   0 |   1 | 11111    |      100 | x   | 00     | ST2 (single structure) -32-bit, immediate offset | FEAT_AdvSIMD |
|   0 |   1 | 11111    |      100 | 0   | 01     | ST2 (single structure) -64-bit, immediate offset | FEAT_AdvSIMD |
|   0 |   1 | 11111    |      101 | x   | 00     | ST4 (single structure) -32-bit, immediate offset | FEAT_AdvSIMD |
|   0 |   1 | 11111    |      101 | 0   | 01     | ST4 (single structure) -64-bit, immediate offset | FEAT_AdvSIMD |
|   0 |   1 | != 11111 |      000 | x   | xx     | ST2 (single structure) - 8-bit, register offset  | FEAT_AdvSIMD |
|   0 |   1 | != 11111 |      001 | x   | xx     | ST4 (single structure) - 8-bit, register offset  | FEAT_AdvSIMD |
|   0 |   1 | != 11111 |      010 | x   | x0     | ST2 (single structure) - 16-bit, register offset | FEAT_AdvSIMD |
|   0 |   1 | != 11111 |      011 | x   | x0     | ST4 (single structure) - 16-bit, register offset | FEAT_AdvSIMD |
|   0 |   1 | != 11111 |      100 | x   | 00     | ST2 (single structure) - 32-bit, register offset | FEAT_AdvSIMD |
|   0 |   1 | != 11111 |      100 | 0   | 01     | ST2 (single structure) - 64-bit, register offset | FEAT_AdvSIMD |

|   L | R   | Rm       | opcode   | S   | size   | Instruction Details                                     |                                                         |                                                         | Feature      |
|-----|-----|----------|----------|-----|--------|---------------------------------------------------------|---------------------------------------------------------|---------------------------------------------------------|--------------|
|   0 | 1   | != 11111 | 101      | x   | 00     | ST4 (single structure) - 32-bit, register offset        | ST4 (single structure) - 32-bit, register offset        | ST4 (single structure) - 32-bit, register offset        | FEAT_AdvSIMD |
|   0 | 1   | != 11111 | 101      | 0   | 01     | ST4 (single structure) - 64-bit, register offset        | ST4 (single structure) - 64-bit, register offset        | ST4 (single structure) - 64-bit, register offset        | FEAT_AdvSIMD |
|   1 | x   | xxxxx    | 11x      | 1   | xx     | UNALLOCATED                                             | UNALLOCATED                                             | UNALLOCATED                                             | -            |
|   1 | 0   | 11111    | 000      | x   | xx     | LD1 (single structure) -8-bit, immediate offset         | LD1 (single structure) -8-bit, immediate offset         | LD1 (single structure) -8-bit, immediate offset         | FEAT_AdvSIMD |
|   1 | 0   | 11111    | 001      | x   | xx     | LD3 (single structure) -8-bit, immediate offset         | LD3 (single structure) -8-bit, immediate offset         | LD3 (single structure) -8-bit, immediate offset         | FEAT_AdvSIMD |
|   1 | 0   | 11111    | 010      | x   | x0     | LD1 (single structure) immediate offset                 | -                                                       | 16-bit,                                                 | FEAT_AdvSIMD |
|   1 | 0   | 11111    | 011      | x   | x0     | LD3 (single structure) immediate offset                 | -                                                       | 16-bit,                                                 | FEAT_AdvSIMD |
|   1 | 0   | 11111    | 100      | x   | 00     | LD1 (single structure) immediate offset                 | -                                                       | 32-bit,                                                 | FEAT_AdvSIMD |
|   1 | 0   | 11111    | 100      | 0   | 01     | LD1 (single structure) immediate offset                 | -                                                       | 64-bit,                                                 | FEAT_AdvSIMD |
|   1 | 0   | 11111    | 101      | x   | 00     | LD3 (single structure) immediate offset                 | -                                                       | 32-bit,                                                 | FEAT_AdvSIMD |
|   1 | 0   | 11111    | 101      | 0   | 01     | LD3 (single structure) immediate offset                 | -                                                       | 64-bit,                                                 | FEAT_AdvSIMD |
|   1 | 0   | 11111    | 110      | 0   | xx     | LD1R -Immediate offset                                  | LD1R -Immediate offset                                  | LD1R -Immediate offset                                  | FEAT_AdvSIMD |
|   1 | 0   | 11111    | 111      | 0   | xx     |                                                         |                                                         |                                                         | FEAT_AdvSIMD |
|   1 | 0   | != 11111 | 000      | x   | xx     | LD3R -Immediate offset LD1 (single structure) -         | 8-bit,                                                  | register                                                | FEAT_AdvSIMD |
|   1 | 0   | != 11111 | 001      | x   | xx     | offset LD3 (single structure) -                         | 8-bit,                                                  | register                                                | FEAT_AdvSIMD |
|   1 | 0   | != 11111 | 010      | x   | x0     | offset LD1 (single structure) - 16-bit, register offset | offset LD1 (single structure) - 16-bit, register offset | offset LD1 (single structure) - 16-bit, register offset | FEAT_AdvSIMD |
|   1 | 0   | != 11111 | 011      | x   | x0     | LD3 (single structure) - 16-bit, register               | LD3 (single structure) - 16-bit, register               | LD3 (single structure) - 16-bit, register               | FEAT_AdvSIMD |
|   1 | 0   | != 11111 | 100      | x   | 00     | LD1 (single structure) - 32-bit, register offset        | LD1 (single structure) - 32-bit, register offset        | LD1 (single structure) - 32-bit, register offset        | FEAT_AdvSIMD |
|   1 | 0   | != 11111 | 100      | 0   | 01     | LD1 (single structure) - 64-bit, register offset        | LD1 (single structure) - 64-bit, register offset        | LD1 (single structure) - 64-bit, register offset        | FEAT_AdvSIMD |
|   1 | 0   | != 11111 | 101      | x   | 00     | LD3 (single structure) - 32-bit, register offset        | LD3 (single structure) - 32-bit, register offset        | LD3 (single structure) - 32-bit, register offset        | FEAT_AdvSIMD |
|   1 | 0   | != 11111 | 101      | 0   | 01     | LD3 (single structure) - 64-bit, register offset        | LD3 (single structure) - 64-bit, register offset        | LD3 (single structure) - 64-bit, register offset        | FEAT_AdvSIMD |
|   1 | 0   | != 11111 | 110      | 0   | xx     | LD1R -Register offset                                   | LD1R -Register offset                                   | LD1R -Register offset                                   | FEAT_AdvSIMD |
|   1 | 0   | != 11111 | 111      | 0   | xx     | LD3R -Register offset                                   | LD3R -Register offset                                   | LD3R -Register offset                                   | FEAT_AdvSIMD |
|   1 | 1   | 11111    | 000      | x   | xx     | LD2 (single structure) -8-bit, immediate                | LD2 (single structure) -8-bit, immediate                | LD2 (single structure) -8-bit, immediate                | FEAT_AdvSIMD |
|   1 | 1   | 11111    | 001      | x   | xx     | LD4 (single structure) -8-bit, immediate offset         | LD4 (single structure) -8-bit, immediate offset         | LD4 (single structure) -8-bit, immediate offset         | FEAT_AdvSIMD |
|   1 | 1   | 11111    | 010      | x   | x0     | LD2 (single structure) immediate offset                 | -                                                       | 16-bit,                                                 | FEAT_AdvSIMD |
|   1 | 1   | 11111    | 011      | x   | x0 00  | LD4 (single structure) immediate offset                 | -                                                       | 16-bit,                                                 | FEAT_AdvSIMD |
|   1 | 1   | 11111    | 100      | x   |        | LD2 (single structure) immediate offset                 | -                                                       | 32-bit,                                                 | FEAT_AdvSIMD |

|   L |   R | Rm       |   opcode | S   | size   | Instruction Details                              |          | Feature      |
|-----|-----|----------|----------|-----|--------|--------------------------------------------------|----------|--------------|
|   1 |   1 | 11111    |      100 | 0   | 01     | LD2 (single structure) - immediate offset        | 64-bit,  | FEAT_AdvSIMD |
|   1 |   1 | 11111    |      101 | x   | 00     | LD4 (single structure) - immediate offset        | 32-bit,  | FEAT_AdvSIMD |
|   1 |   1 | 11111    |      101 | 0   | 01     | LD4 (single structure) - immediate offset        | 64-bit,  | FEAT_AdvSIMD |
|   1 |   1 | 11111    |      110 | 0   | xx     | LD2R -Immediate offset                           |          | FEAT_AdvSIMD |
|   1 |   1 | 11111    |      111 | 0   | xx     | LD4R -Immediate offset                           |          | FEAT_AdvSIMD |
|   1 |   1 | != 11111 |      000 | x   | xx     | LD2 (single structure) - 8-bit, offset           | register | FEAT_AdvSIMD |
|   1 |   1 | != 11111 |      001 | x   | xx     | LD4 (single structure) - 8-bit, offset           | register | FEAT_AdvSIMD |
|   1 |   1 | != 11111 |      010 | x   | x0     | LD2 (single structure) - 16-bit, offset          | register | FEAT_AdvSIMD |
|   1 |   1 | != 11111 |      011 | x   | x0     | LD4 (single structure) - 16-bit, register offset |          | FEAT_AdvSIMD |
|   1 |   1 | != 11111 |      100 | x   | 00     | LD2 (single structure) - 32-bit, offset          | register | FEAT_AdvSIMD |
|   1 |   1 | != 11111 |      100 | 0   | 01     | LD2 (single structure) - 64-bit, register offset |          | FEAT_AdvSIMD |
|   1 |   1 | != 11111 |      101 | x   | 00     | LD4 (single structure) - 32-bit, register offset |          | FEAT_AdvSIMD |
|   1 |   1 | != 11111 |      101 | 0   | 01     | LD4 (single structure) - 64-bit, register offset |          | FEAT_AdvSIMD |
|   1 |   1 | != 11111 |      110 | 0   | xx     | LD2R -Register offset                            |          | FEAT_AdvSIMD |
|   1 |   1 | != 11111 |      111 | 0   | xx     | LD4R -Register offset                            |          | FEAT_AdvSIMD |

## RCW compare and swap

The encodings in this section are decoded from Loads and Stores.

<!-- image -->

| 31 30   |   29 |       |   27 26 |   25 24 | 23   | 22 21   | 20   | 16   | 15 10       | 5   | 0   |
|---------|------|-------|---------|---------|------|---------|------|------|-------------|-----|-----|
| 0 S     |    0 | 1 1 0 |       0 |       1 | A    | R 1     |      | Rs   | 0 0 0 0 1 0 | Rn  | Rt  |

|   S |   A |   R | Instruction Details                         | Feature   |
|-----|-----|-----|---------------------------------------------|-----------|
|   0 |   0 |   0 | RCWCAS, RCWCASA, RCWCASAL, RCWCASL-RCWCAS   | FEAT_THE  |
|   0 |   0 |   1 | RCWCAS, RCWCASA, RCWCASAL, RCWCASL-RCWCASL  | FEAT_THE  |
|   0 |   1 |   0 | RCWCAS, RCWCASA, RCWCASAL, RCWCASL-RCWCASA  | FEAT_THE  |
|   0 |   1 |   1 | RCWCAS, RCWCASA, RCWCASAL, RCWCASL-RCWCASAL | FEAT_THE  |

## RCW compare and swap pair

The encodings in this section are decoded from Loads and Stores.

<!-- image -->

|   31 | 30 29   | 15          | 10 9   | 5 4   |
|------|---------|-------------|--------|-------|
|    0 | S 0     | 0 0 0 0 1 1 | Rn     | Rt    |

|   S |   A | R                                  | Instruction Details    | Feature              |
|-----|-----|------------------------------------|------------------------|----------------------|
|   0 |   0 | 0 RCWCASP, RCWCASPAL,              | RCWCASPA, RCWCASPL -   | FEAT_D128 &&FEAT_THE |
|   0 |   0 | 1 RCWCASP, RCWCASPAL,              | RCWCASPA, RCWCASPL -   | FEAT_D128 &&FEAT_THE |
|   0 |   1 | 0 RCWCASP, RCWCASPAL,              | RCWCASPA, RCWCASPL -   | FEAT_D128 &&FEAT_THE |
|   0 |   1 | 1 RCWCASP, RCWCASPAL, RCWCASPAL    | RCWCASPA, RCWCASPL -   | FEAT_D128 &&FEAT_THE |
|   1 |   0 | 0 RCWSCASP, RCWSCASPAL,            | RCWSCASPA, RCWSCASPL - | FEAT_D128 &&FEAT_THE |
|   1 |   0 | 1 RCWSCASP, RCWSCASPAL, RCWSCASPL  | RCWSCASPA, RCWSCASPL - | FEAT_D128 &&FEAT_THE |
|   1 |   1 | 0 RCWSCASP, RCWSCASPAL, RCWSCASPA  | RCWSCASPA, RCWSCASPL - | FEAT_D128 &&FEAT_THE |
|   1 |   1 | 1 RCWSCASP, RCWSCASPAL, RCWSCASPAL | RCWSCASPA, RCWSCASPL - | FEAT_D128 &&FEAT_THE |

|   S |   A |   R | Instruction Details           |                      | Feature   |
|-----|-----|-----|-------------------------------|----------------------|-----------|
|   1 |   0 |   0 | RCWSCAS, RCWSCASAL, RCWSCAS   | RCWSCASA, RCWSCASL - | FEAT_THE  |
|   1 |   0 |   1 | RCWSCAS, RCWSCASAL, RCWSCASL  | RCWSCASA, RCWSCASL - | FEAT_THE  |
|   1 |   1 |   0 | RCWSCAS, RCWSCASAL, RCWSCASA  | RCWSCASA, RCWSCASL - | FEAT_THE  |
|   1 |   1 |   1 | RCWSCAS, RCWSCASAL, RCWSCASAL | RCWSCASA, RCWSCASL - | FEAT_THE  |

## 128-bit atomic memory operations

The encodings in this section are decoded from Loads and Stores.

|   31 | 30 29   | 27   |   26 |   25 24 | 23 22   |   21 |     | 16 15   | 14   | 12 11 10   |    | 5   | 4   |
|------|---------|------|------|---------|---------|------|-----|---------|------|------------|----|-----|-----|
|    0 | S 0 1   | 1 0  |    0 |       1 | A R     |    1 | Rt2 | o3      | opc  | 0 0        | Rn |     | Rt  |

| S   | A   | R   | o3   | opc   | Instruction Details                               | Feature              |
|-----|-----|-----|------|-------|---------------------------------------------------|----------------------|
| x   | x   | x   | x    | 1xx   | UNALLOCATED                                       | -                    |
| 0   | x   | x   | 0    | 0x0   | UNALLOCATED                                       | -                    |
| 0   | 0   | 0   | 0    | 001   | LDCLRP, LDCLRPA, LDCLRPAL, LDCLRPL-LDCLRP         | FEAT_LSE128          |
| 0   | 0   | 0   | 0    | 011   | LDSETP, LDSETPA, LDSETPAL, LDSETPL-LDSETP         | FEAT_LSE128          |
| 0   | 0   | 0   | 1    | 000   | SWPP, SWPPA, SWPPAL, SWPPL - SWPP                 | FEAT_LSE128          |
| 0   | 0   | 0   | 1    | 001   | RCWCLRP, RCWCLRPA, RCWCLRPAL, RCWCLRPL - RCWCLRP  | FEAT_D128 &&FEAT_THE |
| 0   | 0   | 0   | 1    | 010   | RCWSWPP, RCWSWPPA, RCWSWPPAL, RCWSWPPL - RCWSWPP  | FEAT_D128 &&FEAT_THE |
| 0   | 0   | 0   | 1    | 011   | RCWSETP, RCWSETPA, RCWSETPAL, RCWSETPL-RCWSETP    | FEAT_D128 &&FEAT_THE |
| 0   | 0   | 1   | 0    | 001   | LDCLRP, LDCLRPA, LDCLRPAL, LDCLRPL-LDCLRPL        | FEAT_LSE128          |
| 0   | 0   | 1   | 0    | 011   | LDSETP, LDSETPA, LDSETPAL, LDSETPL-LDSETPL        | FEAT_LSE128          |
| 0   | 0   | 1   | 1    | 000   | SWPP, SWPPA, SWPPAL, SWPPL - SWPPL                | FEAT_LSE128          |
| 0   | 0   | 1   | 1    | 001   | RCWCLRP, RCWCLRPA, RCWCLRPAL, RCWCLRPL - RCWCLRPL | FEAT_D128 &&FEAT_THE |
| 0   | 0   | 1   | 1    | 010   | RCWSWPP, RCWSWPPA, RCWSWPPAL, RCWSWPPL - RCWSWPPL | FEAT_D128 &&FEAT_THE |
| 0   | 0   | 1   | 1    | 011   | RCWSETP, RCWSETPA, RCWSETPAL, RCWSETPL-RCWSETPL   | FEAT_D128 &&FEAT_THE |
| 0   | 1   | 0   | 0    | 001   | LDCLRP, LDCLRPA, LDCLRPAL, LDCLRPL-LDCLRPA        | FEAT_LSE128          |
| 0   | 1   | 0   | 0    | 011   | LDSETP, LDSETPA, LDSETPAL, LDSETPL-LDSETPA        | FEAT_LSE128          |
| 0   | 1   | 0   | 1    | 000   | SWPP, SWPPA, SWPPAL, SWPPL - SWPPA                | FEAT_LSE128          |
| 0   | 1   | 0   | 1    | 001   | RCWCLRP, RCWCLRPA, RCWCLRPAL, RCWCLRPL - RCWCLRPA | FEAT_D128 &&FEAT_THE |

|   S | A   | R   |   o3 | opc   | Instruction Details                                     | Feature              |
|-----|-----|-----|------|-------|---------------------------------------------------------|----------------------|
|   0 | 1   | 0   |    1 | 010   | RCWSWPP, RCWSWPPA, RCWSWPPAL, RCWSWPPL - RCWSWPPA       | FEAT_D128 &&FEAT_THE |
|   0 | 1   | 0   |    1 | 011   | RCWSETP, RCWSETPA, RCWSETPAL, RCWSETPL-RCWSETPA         | FEAT_D128 &&FEAT_THE |
|   0 | 1   | 1   |    0 | 001   | LDCLRP, LDCLRPA, LDCLRPAL, LDCLRPL-LDCLRPAL             | FEAT_LSE128          |
|   0 | 1   | 1   |    0 | 011   | LDSETP, LDSETPA, LDSETPAL, LDSETPL-LDSETPAL             | FEAT_LSE128          |
|   0 | 1   | 1   |    1 | 000   | SWPP, SWPPA, SWPPAL, SWPPL - SWPPAL                     | FEAT_LSE128          |
|   0 | 1   | 1   |    1 | 001   | RCWCLRP, RCWCLRPA, RCWCLRPAL, RCWCLRPL - RCWCLRPAL      | FEAT_D128 &&FEAT_THE |
|   0 | 1   | 1   |    1 | 010   | RCWSWPP, RCWSWPPA, RCWSWPPAL, RCWSWPPL - RCWSWPPAL      | FEAT_D128 &&FEAT_THE |
|   0 | 1   | 1   |    1 | 011   | RCWSETP, RCWSETPA, RCWSETPAL, RCWSETPL-RCWSETPAL        | FEAT_D128 &&FEAT_THE |
|   1 | x   | x   |    0 | 0xx   | UNALLOCATED                                             | -                    |
|   1 | x   | x   |    1 | 000   | UNALLOCATED                                             | -                    |
|   1 | 0   | 0   |    1 | 001   | RCWSCLRP, RCWSCLRPA, RCWSCLRPAL, RCWSCLRPL - RCWSCLRP   | FEAT_D128 &&FEAT_THE |
|   1 | 0   | 0   |    1 | 010   | RCWSSWPP, RCWSSWPPA, RCWSSWPPAL, RCWSSWPPL - RCWSSWPP   | FEAT_D128 &&FEAT_THE |
|   1 | 0   | 0   |    1 | 011   | RCWSSETP, RCWSSETPA, RCWSSETPAL, RCWSSETPL - RCWSSETP   | FEAT_D128 &&FEAT_THE |
|   1 | 0   | 1   |    1 | 001   | RCWSCLRP, RCWSCLRPA, RCWSCLRPAL, RCWSCLRPL - RCWSCLRPL  | FEAT_D128 &&FEAT_THE |
|   1 | 0   | 1   |    1 | 010   | RCWSSWPP, RCWSSWPPA, RCWSSWPPAL, RCWSSWPPL - RCWSSWPPL  | FEAT_D128 &&FEAT_THE |
|   1 | 0   | 1   |    1 | 011   | RCWSSETP, RCWSSETPA, RCWSSETPAL, RCWSSETPL - RCWSSETPL  | FEAT_D128 &&FEAT_THE |
|   1 | 1   | 0   |    1 | 001   | RCWSCLRP, RCWSCLRPA, RCWSCLRPAL, RCWSCLRPL - RCWSCLRPA  | FEAT_D128 &&FEAT_THE |
|   1 | 1   | 0   |    1 | 010   | RCWSSWPP, RCWSSWPPA, RCWSSWPPAL, RCWSSWPPL - RCWSSWPPA  | FEAT_D128 &&FEAT_THE |
|   1 | 1   | 0   |    1 | 011   | RCWSSETP, RCWSSETPA, RCWSSETPAL, RCWSSETPL - RCWSSETPA  | FEAT_D128 &&FEAT_THE |
|   1 | 1   | 1   |    1 | 001   | RCWSCLRP, RCWSCLRPA, RCWSCLRPAL, RCWSCLRPL - RCWSCLRPAL | FEAT_D128 &&FEAT_THE |
|   1 | 1   | 1   |    1 | 010   | RCWSSWPP, RCWSSWPPA, RCWSSWPPAL, RCWSSWPPL - RCWSSWPPAL | FEAT_D128 &&FEAT_THE |

|   S |   A |   R |   o3 |   opc | Instruction Details                                   | Feature              |
|-----|-----|-----|------|-------|-------------------------------------------------------|----------------------|
|   1 |   1 |   1 |    1 |   011 | RCWSSETP, RCWSSETPA, RCWSSETPAL, RCWSSETPL RCWSSETPAL | FEAT_D128 &&FEAT_THE |

## Atomic memory operations (unprivileged)

The encodings in this section are decoded from Loads and Stores.

<!-- image -->

| 31 30   |   29 | 27    |   26 |   25 24 | 23   | 22   |   21 |    | 16 15   | 14   | 12 11 10   | 9   | 5 4   |
|---------|------|-------|------|---------|------|------|------|----|---------|------|------------|-----|-------|
| 0 sz    |    0 | 1 1 0 |    0 |       1 | A    | R    |    1 | Rs | o3      | opc  | 0 1        | Rn  | Rt    |

| sz   | A   | R   | o3   | opc   | Instruction Details                                           | Feature   |
|------|-----|-----|------|-------|---------------------------------------------------------------|-----------|
| x    | x   | x   | x    | 010   | UNALLOCATED                                                   | -         |
| x    | x   | x   | x    | 1xx   | UNALLOCATED                                                   | -         |
| x    | x   | x   | 1    | 0x1   | UNALLOCATED                                                   | -         |
| 0    | 0   | 0   | 0    | 000   | LDTADD, LDTADDA, LDTADDAL, LDTADDL-32-bit no memory ordering  | FEAT_LSUI |
| 0    | 0   | 0   | 0    | 001   | LDTCLR, LDTCLRA, LDTCLRAL, LDTCLRL -32-bit no memory ordering | FEAT_LSUI |
| 0    | 0   | 0   | 0    | 011   | LDTSET, LDTSETA, LDTSETAL, LDTSETL -32-bit no memory ordering | FEAT_LSUI |
| 0    | 0   | 0   | 1    | 000   | SWPT, SWPTA, SWPTAL, SWPTL - 32-bitSWPT                       | FEAT_LSUI |
| 0    | 0   | 1   | 0    | 000   | LDTADD, LDTADDA, LDTADDAL, LDTADDL -32-bit release            | FEAT_LSUI |
| 0    | 0   | 1   | 0    | 001   | LDTCLR, LDTCLRA, LDTCLRAL, LDTCLRL -32-bit release            | FEAT_LSUI |
| 0    | 0   | 1   | 0    | 011   | LDTSET, LDTSETA, LDTSETAL, LDTSETL -32-bit release            | FEAT_LSUI |
| 0    | 0   | 1   | 1    | 000   | SWPT, SWPTA, SWPTAL, SWPTL - 32-bit SWPTL                     | FEAT_LSUI |
| 0    | 1   | 0   | 0    | 000   | LDTADD, LDTADDA, LDTADDAL, LDTADDL -32-bit acquire            | FEAT_LSUI |
| 0    | 1   | 0   | 0    | 001   | LDTCLR, LDTCLRA, LDTCLRAL, LDTCLRL -32-bit acquire            | FEAT_LSUI |
| 0    | 1   | 0   | 0    | 011   | LDTSET, LDTSETA, LDTSETAL, LDTSETL -32-bit acquire            | FEAT_LSUI |
| 0    | 1   | 0   | 1    | 000   | SWPT, SWPTA, SWPTAL, SWPTL - 32-bitSWPTA                      | FEAT_LSUI |
| 0    | 1   | 1   | 0    | 000   | LDTADD, LDTADDA, LDTADDAL, LDTADDL -32-bit acquire-release    | FEAT_LSUI |
| 0    | 1   | 1   | 0    | 001   | LDTCLR, LDTCLRA, LDTCLRAL, LDTCLRL -32-bit acquire-release    | FEAT_LSUI |

## GCS load/store

The encodings in this section are decoded from Loads and Stores.

<!-- image -->

|   sz |   A |   R |   o3 |   opc | Instruction Details                                           | Feature   |
|------|-----|-----|------|-------|---------------------------------------------------------------|-----------|
|    0 |   1 |   1 |    0 |   011 | LDTSET, LDTSETA, LDTSETAL, LDTSETL -32-bit acquire-release    | FEAT_LSUI |
|    0 |   1 |   1 |    1 |   000 | SWPT, SWPTA, SWPTAL, SWPTL - 32-bit SWPTAL                    | FEAT_LSUI |
|    1 |   0 |   0 |    0 |   000 | LDTADD, LDTADDA, LDTADDAL, LDTADDL-64-bit no memory ordering  | FEAT_LSUI |
|    1 |   0 |   0 |    0 |   001 | LDTCLR, LDTCLRA, LDTCLRAL, LDTCLRL -64-bit no memory ordering | FEAT_LSUI |
|    1 |   0 |   0 |    0 |   011 | LDTSET, LDTSETA, LDTSETAL, LDTSETL -64-bit no memory ordering | FEAT_LSUI |
|    1 |   0 |   0 |    1 |   000 | SWPT, SWPTA, SWPTAL, SWPTL - 64-bitSWPT                       | FEAT_LSUI |
|    1 |   0 |   1 |    0 |   000 | LDTADD, LDTADDA, LDTADDAL, LDTADDL -64-bit release            | FEAT_LSUI |
|    1 |   0 |   1 |    0 |   001 | LDTCLR, LDTCLRA, LDTCLRAL, LDTCLRL -64-bit release            | FEAT_LSUI |
|    1 |   0 |   1 |    0 |   011 | LDTSET, LDTSETA, LDTSETAL, LDTSETL -64-bit release            | FEAT_LSUI |
|    1 |   0 |   1 |    1 |   000 | SWPT, SWPTA, SWPTAL, SWPTL - 64-bit SWPTL                     | FEAT_LSUI |
|    1 |   1 |   0 |    0 |   000 | LDTADD, LDTADDA, LDTADDAL, LDTADDL -64-bit acquire            | FEAT_LSUI |
|    1 |   1 |   0 |    0 |   001 | LDTCLR, LDTCLRA, LDTCLRAL, LDTCLRL -64-bit acquire            | FEAT_LSUI |
|    1 |   1 |   0 |    0 |   011 | LDTSET, LDTSETA, LDTSETAL, LDTSETL -64-bit acquire            | FEAT_LSUI |
|    1 |   1 |   0 |    1 |   000 | SWPT, SWPTA, SWPTAL, SWPTL - 64-bitSWPTA                      | FEAT_LSUI |
|    1 |   1 |   1 |    0 |   000 | LDTADD, LDTADDA, LDTADDAL, LDTADDL -64-bit acquire-release    | FEAT_LSUI |
|    1 |   1 |   1 |    0 |   001 | LDTCLR, LDTCLRA, LDTCLRAL, LDTCLRL -64-bit acquire-release    | FEAT_LSUI |
|    1 |   1 |   1 |    0 |   011 | LDTSET, LDTSETA, LDTSETAL, LDTSETL -64-bit acquire-release    | FEAT_LSUI |
|    1 |   1 |   1 |    1 |   000 | SWPT, SWPTA, SWPTAL, SWPTL - 64-bit SWPTAL                    | FEAT_LSUI |

## Load/store memory tags

The encodings in this section are decoded from Loads and Stores.

<!-- image -->

|   31 | 28 27 26 25   | 24 12 11 10   | 5   | 4   |   23 22 21 | 20   | 9   |    |    |
|------|---------------|---------------|-----|-----|------------|------|-----|----|----|
|    1 | 1 0 1         | 1 0           | 0 1 | opc |          1 | imm9 | op2 | Rn | Rt |

| opc   | imm9         |   op2 | Instruction Details   | Feature   |
|-------|--------------|-------|-----------------------|-----------|
| 00    | xxxxxxxxx    |    01 | STG -Post-index       | FEAT_MTE  |
| 00    | xxxxxxxxx    |    10 | STG -Signed offset    | FEAT_MTE  |
| 00    | xxxxxxxxx    |    11 | STG -Pre-index        | FEAT_MTE  |
| 00    | 000000000    |    00 | STZGM                 | FEAT_MTE2 |
| 01    | xxxxxxxxx    |    00 | LDG                   | FEAT_MTE  |
| 01    | xxxxxxxxx    |    01 | STZG -Post-index      | FEAT_MTE  |
| 01    | xxxxxxxxx    |    10 | STZG -Signed offset   | FEAT_MTE  |
| 01    | xxxxxxxxx    |    11 | STZG -Pre-index       | FEAT_MTE  |
| 10    | xxxxxxxxx    |    01 | ST2G -Post-index      | FEAT_MTE  |
| 10    | xxxxxxxxx    |    10 | ST2G -Signed offset   | FEAT_MTE  |
| 10    | xxxxxxxxx    |    11 | ST2G -Pre-index       | FEAT_MTE  |
| 10    | 000000000    |    00 | STGM                  | FEAT_MTE2 |
| 11    | xxxxxxxxx    |    01 | STZ2G -Post-index     | FEAT_MTE  |
| 11    | xxxxxxxxx    |    10 | STZ2G -Signed offset  | FEAT_MTE  |
| 11    | xxxxxxxxx    |    11 | STZ2G -Pre-index      | FEAT_MTE  |
| 11    | 000000000    |    00 | LDGM                  | FEAT_MTE2 |
| != 01 | != 000000000 |    00 | UNALLOCATED           | -         |

## Load/store exclusive pair

The encodings in this section are decoded from Loads and Stores.

<!-- image -->

|   31 | 30 29   | 27 26 25   | 23 22 21   |     | 20   | 16   | 10   | 5 4   | 0   |
|------|---------|------------|------------|-----|------|------|------|-------|-----|
|    1 | sz 0    | 0 1 0      | 0 0 0      | L 1 |      | Rs   | Rt2  | Rn    | Rt  |

| opc   | Instruction Details   | Feature   |
|-------|-----------------------|-----------|
| 000   | GCSSTR                | FEAT_GCS  |
| 001   | GCSSTTR               | FEAT_GCS  |
| 01x   | UNALLOCATED           | -         |
| 1xx   | UNALLOCATED           | -         |

## Compare and swap (unprivileged)

The encodings in this section are decoded from Loads and Stores.

<!-- image -->

|   sz |   L |   o0 | Instruction Details   |
|------|-----|------|-----------------------|
|    0 |   0 |    0 | STXP -32-bit          |
|    0 |   0 |    1 | STLXP -32-bit         |
|    0 |   1 |    0 | LDXP -32-bit          |
|    0 |   1 |    1 | LDAXP-32-bit          |
|    1 |   0 |    0 | STXP -64-bit          |
|    1 |   0 |    1 | STLXP -64-bit         |
|    1 |   1 |    0 | LDXP -64-bit          |
|    1 |   1 |    1 | LDAXP-64-bit          |

## Load/store exclusive register (unprivileged)

The encodings in this section are decoded from Loads and Stores.

<!-- image -->

|   31 | 30 29   | 27 26   | 25   | 23 22   |   21 | 20   | 16 15   | 10   | 5   | 0   |
|------|---------|---------|------|---------|------|------|---------|------|-----|-----|
|    1 | sz 0    | 0 1 0   | 0 1  | 0 L     |    0 | Rs   | o0      | Rt2  | Rn  | Rt  |

|   sz |   L |   o0 | Instruction Details   | Feature   |
|------|-----|------|-----------------------|-----------|
|    0 |   0 |    0 | STTXR -32-bit         | FEAT_LSUI |
|    0 |   0 |    1 | STLTXR -32-bit        | FEAT_LSUI |
|    0 |   1 |    0 | LDTXR-32-bit          | FEAT_LSUI |
|    0 |   1 |    1 | LDATXR -32-bit        | FEAT_LSUI |
|    1 |   0 |    0 | STTXR -64-bit         | FEAT_LSUI |
|    1 |   0 |    1 | STLTXR -64-bit        | FEAT_LSUI |
|    1 |   1 |    0 | LDTXR-64-bit          | FEAT_LSUI |
|    1 |   1 |    1 | LDATXR -64-bit        | FEAT_LSUI |

|   sz | L   | o0   | Rt2      | Instruction Details   | Instruction Details   | Instruction Details   | Instruction Details   | Feature   |
|------|-----|------|----------|-----------------------|-----------------------|-----------------------|-----------------------|-----------|
|    0 | x   | x    | xxxxx    | UNALLOCATED           | UNALLOCATED           | UNALLOCATED           | UNALLOCATED           | -         |
|    1 | x   | x    | != 11111 | UNALLOCATED           | UNALLOCATED           | UNALLOCATED           | UNALLOCATED           | -         |
|    1 | 0   | 0    | 11111    | CAST, CAST            | CASAT, CASALT,        | CASLT                 | -                     | FEAT_LSUI |
|    1 | 0   | 1    | 11111    | CAST, CASLT           | CASAT, CASALT,        | CASLT                 | -                     | FEAT_LSUI |
|    1 | 1   | 0    | 11111    | CAST, CASAT           | CASAT, CASALT,        | CASLT                 | -                     | FEAT_LSUI |
|    1 | 1   | 1    | 11111    | CAST, CASALT          | CASAT, CASALT,        | CASLT                 | -                     | FEAT_LSUI |

## Load/store exclusive register

The encodings in this section are decoded from Loads and Stores.

<!-- image -->

| 31 30   |   29 | 27 26 25   | 23 22 21   |   20 | 16 15   | 10   | 5 4   | 0   |
|---------|------|------------|------------|------|---------|------|-------|-----|
| size    |    0 | 0 1 0 0    | 0 0 L      |    0 | o0      | Rt2  | Rn    | Rt  |

|   size |   L |   o0 | Instruction Details   |
|--------|-----|------|-----------------------|
|     00 |   0 |    0 | STXRB                 |
|     00 |   0 |    1 | STLXRB                |
|     00 |   1 |    0 | LDXRB                 |
|     00 |   1 |    1 | LDAXRB                |
|     01 |   0 |    0 | STXRH                 |
|     01 |   0 |    1 | STLXRH                |
|     01 |   1 |    0 | LDXRH                 |
|     01 |   1 |    1 | LDAXRH                |
|     10 |   0 |    0 | STXR -32-bit          |
|     10 |   0 |    1 | STLXR -32-bit         |
|     10 |   1 |    0 | LDXR-32-bit           |
|     10 |   1 |    1 | LDAXR-32-bit          |
|     11 |   0 |    0 | STXR -64-bit          |
|     11 |   0 |    1 | STLXR -64-bit         |
|     11 |   1 |    0 | LDXR-64-bit           |
|     11 |   1 |    1 | LDAXR-64-bit          |

## Load/store ordered

The encodings in this section are decoded from Loads and Stores.

<!-- image -->

| 31 30 29   | 27 26 25   | 23 22 21   |   20 |     | 5 4   |    |
|------------|------------|------------|------|-----|-------|----|
| size 0     | 1 0 0 0 1  | L          |    0 | Rt2 | Rn    | Rt |

|   size |   L |   o0 | Instruction Details   | Feature   |
|--------|-----|------|-----------------------|-----------|
|     00 |   0 |    0 | STLLRB                | FEAT_LOR  |
|     00 |   0 |    1 | STLRB                 | -         |
|     00 |   1 |    0 | LDLARB                | FEAT_LOR  |
|     00 |   1 |    1 | LDARB                 | -         |
|     01 |   0 |    0 | STLLRH                | FEAT_LOR  |
|     01 |   0 |    1 | STLRH                 | -         |
|     01 |   1 |    0 | LDLARH                | FEAT_LOR  |
|     01 |   1 |    1 | LDARH                 | -         |
|     10 |   0 |    0 | STLLR -32-bit         | FEAT_LOR  |
|     10 |   0 |    1 | STLR -32-bit          | -         |
|     10 |   1 |    0 | LDLAR-32-bit          | FEAT_LOR  |
|     10 |   1 |    1 | LDAR-32-bit           | -         |
|     11 |   0 |    0 | STLLR -64-bit         | FEAT_LOR  |
|     11 |   0 |    1 | STLR -64-bit          | -         |
|     11 |   1 |    0 | LDLAR-64-bit          | FEAT_LOR  |
|     11 |   1 |    1 | LDAR-64-bit           | -         |

## Compare and swap

The encodings in this section are decoded from Loads and Stores.

<!-- image -->

| size   | L   | o0   | Rt2      | Instruction Details             | Feature   |
|--------|-----|------|----------|---------------------------------|-----------|
| xx     | x   | x    | != 11111 | UNALLOCATED                     | -         |
| 00     | 0   | 0    | 11111    | CASB, CASAB, CASALB, CASLB CASB | FEAT_LSE  |

|   size |   L |   o0 |   Rt2 | Instruction Details                   | Feature   |
|--------|-----|------|-------|---------------------------------------|-----------|
|     00 |   0 |    1 | 11111 | CASB, CASAB, CASALB, CASLB - CASLB    | FEAT_LSE  |
|     00 |   1 |    0 | 11111 | CASB, CASAB, CASALB, CASLB - CASAB    | FEAT_LSE  |
|     00 |   1 |    1 | 11111 | CASB, CASAB, CASALB, CASLB - CASALB   | FEAT_LSE  |
|     01 |   0 |    0 | 11111 | CASH, CASAH, CASALH, CASLH - CASH     | FEAT_LSE  |
|     01 |   0 |    1 | 11111 | CASH, CASAH, CASALH, CASLH - CASLH    | FEAT_LSE  |
|     01 |   1 |    0 | 11111 | CASH, CASAH, CASALH, CASLH - CASAH    | FEAT_LSE  |
|     01 |   1 |    1 | 11111 | CASH, CASAH, CASALH, CASLH - CASALH   | FEAT_LSE  |
|     10 |   0 |    0 | 11111 | CAS, CASA, CASAL, CASL - 32-bit CAS   | FEAT_LSE  |
|     10 |   0 |    1 | 11111 | CAS, CASA, CASAL, CASL - 32-bit CASL  | FEAT_LSE  |
|     10 |   1 |    0 | 11111 | CAS, CASA, CASAL, CASL - 32-bit CASA  | FEAT_LSE  |
|     10 |   1 |    1 | 11111 | CAS, CASA, CASAL, CASL - 32-bit CASAL | FEAT_LSE  |
|     11 |   0 |    0 | 11111 | CAS, CASA, CASAL, CASL - 64-bit CAS   | FEAT_LSE  |
|     11 |   0 |    1 | 11111 | CAS, CASA, CASAL, CASL - 64-bit CASL  | FEAT_LSE  |
|     11 |   1 |    0 | 11111 | CAS, CASA, CASAL, CASL - 64-bit CASA  | FEAT_LSE  |
|     11 |   1 |    1 | 11111 | CAS, CASA, CASAL, CASL - 64-bit CASAL | FEAT_LSE  |

## Load/store ordered register pair

The encodings in this section are decoded from Loads and Stores.

<!-- image -->

| 31 30   |   29 | 27 26 25 23   | 22 21 20 16 12 11   | 15 10        | 5   | 4   |
|---------|------|---------------|---------------------|--------------|-----|-----|
| size    |    0 | 1 0 0 1 0     | L 0                 | Rt2 opc2 1 0 | Rn  | Rt  |

| size   | L   | opc2   | Instruction Details     | Feature     |
|--------|-----|--------|-------------------------|-------------|
| 0x     | x   | xxxx   | UNALLOCATED             | -           |
| 1x     | x   | 001x   | UNALLOCATED             | -           |
| 1x     | x   | 01xx   | UNALLOCATED             | -           |
| 1x     | x   | 1xxx   | UNALLOCATED             | -           |
| 10     | 0   | 0000   | STILP -32-bit pre-index | FEAT_LRCPC3 |

|   size |   L |   opc2 | Instruction Details       | Feature     |
|--------|-----|--------|---------------------------|-------------|
|     10 |   0 |   0001 | STILP -32-bit             | FEAT_LRCPC3 |
|     10 |   1 |   0000 | LDIAPP -32-bit post-index | FEAT_LRCPC3 |
|     10 |   1 |   0001 | LDIAPP -32-bit            | FEAT_LRCPC3 |
|     11 |   0 |   0000 | STILP -64-bit pre-index   | FEAT_LRCPC3 |
|     11 |   0 |   0001 | STILP -64-bit             | FEAT_LRCPC3 |
|     11 |   1 |   0000 | LDIAPP -64-bit post-index | FEAT_LRCPC3 |
|     11 |   1 |   0001 | LDIAPP -64-bit            | FEAT_LRCPC3 |

## Load/store ordered (writeback)

The encodings in this section are decoded from Loads and Stores.

<!-- image -->

| size   | L   | Instruction Details   | Feature     |
|--------|-----|-----------------------|-------------|
| 0x     | x   | UNALLOCATED           | -           |
| 10     | 0   | STLR -32-bit          | FEAT_LRCPC3 |
| 10     | 1   | LDAPR -32-bit         | FEAT_LRCPC3 |
| 11     | 0   | STLR -64-bit          | FEAT_LRCPC3 |
| 11     | 1   | LDAPR -64-bit         | FEAT_LRCPC3 |

## Load/store ordered (unscaled immediate)

The encodings in this section are decoded from Loads and Stores.

<!-- image -->

|   size |   opc | Instruction Details   | Feature     |
|--------|-------|-----------------------|-------------|
|     00 |    00 | STLURB                | FEAT_LRCPC2 |
|     00 |    01 | LDAPURB               | FEAT_LRCPC2 |
|     00 |    10 | LDAPURSB -64-bit      | FEAT_LRCPC2 |
|     00 |    11 | LDAPURSB -32-bit      | FEAT_LRCPC2 |

## Load/store ordered (SIMD\&amp;FP)

The encodings in this section are decoded from Loads and Stores.

<!-- image -->

| 31 30 29   | 27 26 25 24 23 22   | 5     | 10 9   | 21 20   |    | 12 11   | 4   |    |    |
|------------|---------------------|-------|--------|---------|----|---------|-----|----|----|
| size       | 0 1 1               | 1 0 1 |        | opc     |  0 | imm9    | 1 0 | Rn | Rt |

| size   | opc   | Instruction Details      | Feature               |
|--------|-------|--------------------------|-----------------------|
| 00     | 00    | STLUR (SIMD&FP) -8-bit   | FEAT_FP &&FEAT_LRCPC3 |
| 00     | 01    | LDAPUR(SIMD&FP) -8-bit   | FEAT_FP &&FEAT_LRCPC3 |
| 00     | 10    | STLUR (SIMD&FP) -128-bit | FEAT_FP &&FEAT_LRCPC3 |
| 00     | 11    | LDAPUR(SIMD&FP) -128-bit | FEAT_FP &&FEAT_LRCPC3 |
| 01     | 00    | STLUR (SIMD&FP) -16-bit  | FEAT_FP &&FEAT_LRCPC3 |
| 01     | 01    | LDAPUR(SIMD&FP) -16-bit  | FEAT_FP &&FEAT_LRCPC3 |
| 10     | 00    | STLUR (SIMD&FP) -32-bit  | FEAT_FP &&FEAT_LRCPC3 |
| 10     | 01    | LDAPUR(SIMD&FP) -32-bit  | FEAT_FP &&FEAT_LRCPC3 |
| 11     | 00    | STLUR (SIMD&FP) -64-bit  | FEAT_FP &&FEAT_LRCPC3 |
| 11     | 01    | LDAPUR(SIMD&FP) -64-bit  | FEAT_FP &&FEAT_LRCPC3 |
| != 00  | 1x    | UNALLOCATED              | -                     |

## Load register (literal)

The encodings in this section are decoded from Loads and Stores.

|   size | opc   | Instruction Details   | Feature     |
|--------|-------|-----------------------|-------------|
|     01 | 00    | STLURH                | FEAT_LRCPC2 |
|     01 | 01    | LDAPURH               | FEAT_LRCPC2 |
|     01 | 10    | LDAPURSH -64-bit      | FEAT_LRCPC2 |
|     01 | 11    | LDAPURSH -32-bit      | FEAT_LRCPC2 |
|     10 | 00    | STLUR -32-bit         | FEAT_LRCPC2 |
|     10 | 01    | LDAPUR-32-bit         | FEAT_LRCPC2 |
|     10 | 10    | LDAPURSW              | FEAT_LRCPC2 |
|     10 | 11    | UNALLOCATED           | -           |
|     11 | 00    | STLUR -64-bit         | FEAT_LRCPC2 |
|     11 | 01    | LDAPUR-64-bit         | FEAT_LRCPC2 |
|     11 | 1x    | UNALLOCATED           | -           |

<!-- image -->

| 31 30   | 29 27 26 25 24 23   | 5 4   |
|---------|---------------------|-------|
| opc     | 0 1 1 VR 0 0        | Rt    |

|   opc |   VR | Instruction Details            | Feature   |
|-------|------|--------------------------------|-----------|
|    00 |    0 | LDR(literal) -32-bit           | -         |
|    00 |    1 | LDR(literal, SIMD&FP) -32-bit  | FEAT_FP   |
|    01 |    0 | LDR(literal) -64-bit           | -         |
|    01 |    1 | LDR(literal, SIMD&FP) -64-bit  | FEAT_FP   |
|    10 |    0 | LDRSW(literal)                 | -         |
|    10 |    1 | LDR(literal, SIMD&FP) -128-bit | FEAT_FP   |
|    11 |    0 | PRFM(literal)                  | -         |
|    11 |    1 | UNALLOCATED                    | -         |

## Memory Copy and Memory Set

The encodings in this section are decoded from Loads and Stores.

<!-- image -->

| 31   | 30 29   | 27 26   |   25 24 | 23 22   |   21 |    | 12 11 10   | 9 5 4   |    | 0   |
|------|---------|---------|---------|---------|------|----|------------|---------|----|-----|
| size | 0 1 1   | o0 0    |       1 | op1     |    0 | Rs | op2        | 0 1     | Rn | Rd  |

| o0   |   op1 | op2   | Instruction Details                      | Feature   |
|------|-------|-------|------------------------------------------|-----------|
| x    |    11 | 11xx  | UNALLOCATED                              | -         |
| 0    |    00 | 0000  | CPYFP, CPYFM, CPYFE -Prologue            | FEAT_MOPS |
| 0    |    00 | 0001  | CPYFPWT, CPYFMWT, CPYFEWT - Prologue     | FEAT_MOPS |
| 0    |    00 | 0010  | CPYFPRT, CPYFMRT, CPYFERT - Prologue     | FEAT_MOPS |
| 0    |    00 | 0011  | CPYFPT, CPYFMT, CPYFET - Prologue        | FEAT_MOPS |
| 0    |    00 | 0100  | CPYFPWN, CPYFMWN, CPYFEWN- Prologue      | FEAT_MOPS |
| 0    |    00 | 0101  | CPYFPWTWN, CPYFMWTWN, CPYFEWTWN-Prologue | FEAT_MOPS |
| 0    |    00 | 0110  | CPYFPRTWN, CPYFMRTWN, CPYFERTWN-Prologue | FEAT_MOPS |
| 0    |    00 | 0111  | CPYFPTWN, CPYFMTWN, CPYFETWN-Prologue    | FEAT_MOPS |

|   o0 |   op1 |   op2 | Instruction Details                       | Feature   |
|------|-------|-------|-------------------------------------------|-----------|
|    0 |    00 |  1000 | CPYFPRN, CPYFMRN, CPYFERN - Prologue      | FEAT_MOPS |
|    0 |    00 |  1001 | CPYFPWTRN, CPYFMWTRN, CPYFEWTRN-Prologue  | FEAT_MOPS |
|    0 |    00 |  1010 | CPYFPRTRN, CPYFMRTRN, CPYFERTRN -Prologue | FEAT_MOPS |
|    0 |    00 |  1011 | CPYFPTRN, CPYFMTRN, CPYFETRN -Prologue    | FEAT_MOPS |
|    0 |    00 |  1100 | CPYFPN, CPYFMN, CPYFEN - Prologue         | FEAT_MOPS |
|    0 |    00 |  1101 | CPYFPWTN, CPYFMWTN, CPYFEWTN-Prologue     | FEAT_MOPS |
|    0 |    00 |  1110 | CPYFPRTN, CPYFMRTN, CPYFERTN -Prologue    | FEAT_MOPS |
|    0 |    00 |  1111 | CPYFPTN, CPYFMTN, CPYFETN - Prologue      | FEAT_MOPS |
|    0 |    01 |  0000 | CPYFP, CPYFM, CPYFE -Main                 | FEAT_MOPS |
|    0 |    01 |  0001 | CPYFPWT, CPYFMWT, CPYFEWT - Main          | FEAT_MOPS |
|    0 |    01 |  0010 | CPYFPRT, CPYFMRT, CPYFERT - Main          | FEAT_MOPS |
|    0 |    01 |  0011 | CPYFPT, CPYFMT, CPYFET-Main               | FEAT_MOPS |
|    0 |    01 |  0100 | CPYFPWN, CPYFMWN, CPYFEWN- Main           | FEAT_MOPS |
|    0 |    01 |  0101 | CPYFPWTWN, CPYFMWTWN, CPYFEWTWN-Main      | FEAT_MOPS |
|    0 |    01 |  0110 | CPYFPRTWN, CPYFMRTWN, CPYFERTWN-Main      | FEAT_MOPS |
|    0 |    01 |  0111 | CPYFPTWN, CPYFMTWN, CPYFETWN-Main         | FEAT_MOPS |
|    0 |    01 |  1000 | CPYFPRN, CPYFMRN, CPYFERN - Main          | FEAT_MOPS |
|    0 |    01 |  1001 | CPYFPWTRN, CPYFMWTRN, CPYFEWTRN-Main      | FEAT_MOPS |
|    0 |    01 |  1010 | CPYFPRTRN, CPYFMRTRN, CPYFERTRN-Main      | FEAT_MOPS |
|    0 |    01 |  1011 | CPYFPTRN, CPYFMTRN, CPYFETRN -Main        | FEAT_MOPS |
|    0 |    01 |  1100 | CPYFPN, CPYFMN, CPYFEN -Main              | FEAT_MOPS |
|    0 |    01 |  1101 | CPYFPWTN, CPYFMWTN, CPYFEWTN-Main         | FEAT_MOPS |
|    0 |    01 |  1110 | CPYFPRTN, CPYFMRTN, CPYFERTN -Main        | FEAT_MOPS |
|    0 |    01 |  1111 | CPYFPTN, CPYFMTN, CPYFETN - Main          | FEAT_MOPS |
|    0 |    10 |  0000 | CPYFP, CPYFM, CPYFE -Epilogue             | FEAT_MOPS |
|    0 |    10 |  0001 | CPYFPWT, CPYFMWT, CPYFEWT - Epilogue      | FEAT_MOPS |
|    0 |    10 |  0010 | CPYFPRT, CPYFMRT, CPYFERT - Epilogue      | FEAT_MOPS |

|   o0 |   op1 |   op2 | Instruction Details                       | Feature   |
|------|-------|-------|-------------------------------------------|-----------|
|    0 |    10 |  0011 | CPYFPT, CPYFMT, CPYFET - Epilogue         | FEAT_MOPS |
|    0 |    10 |  0100 | CPYFPWN, CPYFMWN, CPYFEWN- Epilogue       | FEAT_MOPS |
|    0 |    10 |  0101 | CPYFPWTWN, CPYFMWTWN, CPYFEWTWN-Epilogue  | FEAT_MOPS |
|    0 |    10 |  0110 | CPYFPRTWN, CPYFMRTWN, CPYFERTWN-Epilogue  | FEAT_MOPS |
|    0 |    10 |  0111 | CPYFPTWN, CPYFMTWN, CPYFETWN-Epilogue     | FEAT_MOPS |
|    0 |    10 |  1000 | CPYFPRN, CPYFMRN, CPYFERN - Epilogue      | FEAT_MOPS |
|    0 |    10 |  1001 | CPYFPWTRN, CPYFMWTRN, CPYFEWTRN-Epilogue  | FEAT_MOPS |
|    0 |    10 |  1010 | CPYFPRTRN, CPYFMRTRN, CPYFERTRN -Epilogue | FEAT_MOPS |
|    0 |    10 |  1011 | CPYFPTRN, CPYFMTRN, CPYFETRN -Epilogue    | FEAT_MOPS |
|    0 |    10 |  1100 | CPYFPN, CPYFMN, CPYFEN - Epilogue         | FEAT_MOPS |
|    0 |    10 |  1101 | CPYFPWTN, CPYFMWTN, CPYFEWTN-Epilogue     | FEAT_MOPS |
|    0 |    10 |  1110 | CPYFPRTN, CPYFMRTN, CPYFERTN -Epilogue    | FEAT_MOPS |
|    0 |    10 |  1111 | CPYFPTN, CPYFMTN, CPYFETN - Epilogue      | FEAT_MOPS |
|    0 |    11 |  0000 | SETP, SETM, SETE -Prologue                | FEAT_MOPS |
|    0 |    11 |  0001 | SETPT, SETMT, SETET -Prologue             | FEAT_MOPS |
|    0 |    11 |  0010 | SETPN, SETMN, SETEN -Prologue             | FEAT_MOPS |
|    0 |    11 |  0011 | SETPTN, SETMTN, SETETN - Prologue         | FEAT_MOPS |
|    0 |    11 |  0100 | SETP, SETM,SETE-Main                      | FEAT_MOPS |
|    0 |    11 |  0101 | SETPT, SETMT, SETET-Main                  | FEAT_MOPS |
|    0 |    11 |  0110 | SETPN, SETMN,SETEN-Main                   | FEAT_MOPS |
|    0 |    11 |  0111 | SETPTN, SETMTN, SETETN-Main               | FEAT_MOPS |
|    0 |    11 |  1000 | SETP, SETM, SETE -Epilogue                | FEAT_MOPS |
|    0 |    11 |  1001 | SETPT, SETMT, SETET -Epilogue             | FEAT_MOPS |
|    0 |    11 |  1010 | SETPN, SETMN, SETEN -Epilogue             | FEAT_MOPS |
|    0 |    11 |  1011 | SETPTN, SETMTN, SETETN - Epilogue         | FEAT_MOPS |
|    1 |    00 |  0000 | CPYP, CPYM, CPYE -Prologue                | FEAT_MOPS |
|    1 |    00 |  0001 | CPYPWT, CPYMWT, CPYEWT - Prologue         | FEAT_MOPS |
|    1 |    00 |  0010 | CPYPRT, CPYMRT, CPYERT - Prologue         | FEAT_MOPS |
|    1 |    00 |  0011 | CPYPT, CPYMT, CPYET -Prologue             | FEAT_MOPS |

|   o0 |   op1 |   op2 | Instruction Details                    | Feature   |
|------|-------|-------|----------------------------------------|-----------|
|    1 |    00 |  0100 | CPYPWN, CPYMWN, CPYEWN - Prologue      | FEAT_MOPS |
|    1 |    00 |  0101 | CPYPWTWN, CPYMWTWN, CPYEWTWN-Prologue  | FEAT_MOPS |
|    1 |    00 |  0110 | CPYPRTWN, CPYMRTWN, CPYERTWN-Prologue  | FEAT_MOPS |
|    1 |    00 |  0111 | CPYPTWN, CPYMTWN,CPYETWN- Prologue     | FEAT_MOPS |
|    1 |    00 |  1000 | CPYPRN, CPYMRN, CPYERN - Prologue      | FEAT_MOPS |
|    1 |    00 |  1001 | CPYPWTRN, CPYMWTRN, CPYEWTRN-Prologue  | FEAT_MOPS |
|    1 |    00 |  1010 | CPYPRTRN, CPYMRTRN, CPYERTRN -Prologue | FEAT_MOPS |
|    1 |    00 |  1011 | CPYPTRN, CPYMTRN, CPYETRN - Prologue   | FEAT_MOPS |
|    1 |    00 |  1100 | CPYPN, CPYMN, CPYEN -Prologue          | FEAT_MOPS |
|    1 |    00 |  1101 | CPYPWTN, CPYMWTN,CPYEWTN- Prologue     | FEAT_MOPS |
|    1 |    00 |  1110 | CPYPRTN, CPYMRTN, CPYERTN - Prologue   | FEAT_MOPS |
|    1 |    00 |  1111 | CPYPTN, CPYMTN, CPYETN - Prologue      | FEAT_MOPS |
|    1 |    01 |  0000 | CPYP,CPYM,CPYE-Main                    | FEAT_MOPS |
|    1 |    01 |  0001 | CPYPWT, CPYMWT, CPYEWT -Main           | FEAT_MOPS |
|    1 |    01 |  0010 | CPYPRT, CPYMRT,CPYERT-Main             | FEAT_MOPS |
|    1 |    01 |  0011 | CPYPT, CPYMT,CPYET-Main                | FEAT_MOPS |
|    1 |    01 |  0100 | CPYPWN, CPYMWN, CPYEWN - Main          | FEAT_MOPS |
|    1 |    01 |  0101 | CPYPWTWN, CPYMWTWN, CPYEWTWN-Main      | FEAT_MOPS |
|    1 |    01 |  0110 | CPYPRTWN, CPYMRTWN, CPYERTWN-Main      | FEAT_MOPS |
|    1 |    01 |  0111 | CPYPTWN, CPYMTWN,CPYETWN- Main         | FEAT_MOPS |
|    1 |    01 |  1000 | CPYPRN, CPYMRN, CPYERN -Main           | FEAT_MOPS |
|    1 |    01 |  1001 | CPYPWTRN, CPYMWTRN, CPYEWTRN-Main      | FEAT_MOPS |
|    1 |    01 |  1010 | CPYPRTRN, CPYMRTRN, CPYERTRN -Main     | FEAT_MOPS |
|    1 |    01 |  1011 | CPYPTRN, CPYMTRN, CPYETRN - Main       | FEAT_MOPS |
|    1 |    01 |  1100 | CPYPN, CPYMN, CPYEN -Main              | FEAT_MOPS |
|    1 |    01 |  1101 | CPYPWTN, CPYMWTN,CPYEWTN- Main         | FEAT_MOPS |
|    1 |    01 |  1110 | CPYPRTN, CPYMRTN, CPYERTN - Main       | FEAT_MOPS |
|    1 |    01 |  1111 | CPYPTN, CPYMTN, CPYETN -Main           | FEAT_MOPS |

|   o0 |   op1 |   op2 | Instruction Details                    | Feature             |
|------|-------|-------|----------------------------------------|---------------------|
|    1 |    10 |  0000 | CPYP, CPYM, CPYE -Epilogue             | FEAT_MOPS           |
|    1 |    10 |  0001 | CPYPWT, CPYMWT, CPYEWT - Epilogue      | FEAT_MOPS           |
|    1 |    10 |  0010 | CPYPRT, CPYMRT, CPYERT - Epilogue      | FEAT_MOPS           |
|    1 |    10 |  0011 | CPYPT, CPYMT, CPYET -Epilogue          | FEAT_MOPS           |
|    1 |    10 |  0100 | CPYPWN, CPYMWN, CPYEWN - Epilogue      | FEAT_MOPS           |
|    1 |    10 |  0101 | CPYPWTWN, CPYMWTWN, CPYEWTWN-Epilogue  | FEAT_MOPS           |
|    1 |    10 |  0110 | CPYPRTWN, CPYMRTWN, CPYERTWN-Epilogue  | FEAT_MOPS           |
|    1 |    10 |  0111 | CPYPTWN, CPYMTWN,CPYETWN- Epilogue     | FEAT_MOPS           |
|    1 |    10 |  1000 | CPYPRN, CPYMRN, CPYERN - Epilogue      | FEAT_MOPS           |
|    1 |    10 |  1001 | CPYPWTRN, CPYMWTRN, CPYEWTRN-Epilogue  | FEAT_MOPS           |
|    1 |    10 |  1010 | CPYPRTRN, CPYMRTRN, CPYERTRN -Epilogue | FEAT_MOPS           |
|    1 |    10 |  1011 | CPYPTRN, CPYMTRN, CPYETRN - Epilogue   | FEAT_MOPS           |
|    1 |    10 |  1100 | CPYPN, CPYMN, CPYEN -Epilogue          | FEAT_MOPS           |
|    1 |    10 |  1101 | CPYPWTN, CPYMWTN,CPYEWTN- Epilogue     | FEAT_MOPS           |
|    1 |    10 |  1110 | CPYPRTN, CPYMRTN, CPYERTN - Epilogue   | FEAT_MOPS           |
|    1 |    10 |  1111 | CPYPTN, CPYMTN, CPYETN - Epilogue      | FEAT_MOPS           |
|    1 |    11 |  0000 | SETGP, SETGM, SETGE -Prologue          | FEAT_MOPS&&FEAT_MTE |
|    1 |    11 |  0001 | SETGPT, SETGMT, SETGET - Prologue      | FEAT_MOPS&&FEAT_MTE |
|    1 |    11 |  0010 | SETGPN, SETGMN, SETGEN - Prologue      | FEAT_MOPS&&FEAT_MTE |
|    1 |    11 |  0011 | SETGPTN, SETGMTN, SETGETN - Prologue   | FEAT_MOPS&&FEAT_MTE |
|    1 |    11 |  0100 | SETGP, SETGM,SETGE-Main                | FEAT_MOPS&&FEAT_MTE |
|    1 |    11 |  0101 | SETGPT, SETGMT, SETGET-Main            | FEAT_MOPS&&FEAT_MTE |
|    1 |    11 |  0110 | SETGPN,SETGMN,SETGEN-Main              | FEAT_MOPS&&FEAT_MTE |
|    1 |    11 |  0111 | SETGPTN, SETGMTN, SETGETN - Main       | FEAT_MOPS&&FEAT_MTE |
|    1 |    11 |  1000 | SETGP, SETGM, SETGE -Epilogue          | FEAT_MOPS&&FEAT_MTE |
|    1 |    11 |  1001 | SETGPT, SETGMT, SETGET - Epilogue      | FEAT_MOPS&&FEAT_MTE |
|    1 |    11 |  1010 | SETGPN, SETGMN, SETGEN - Epilogue      | FEAT_MOPS&&FEAT_MTE |

|   o0 |   op1 |   op2 | Instruction Details   | Instruction Details   | Feature             |
|------|-------|-------|-----------------------|-----------------------|---------------------|
|    1 |    11 |  1011 | SETGPTN, Epilogue     | SETGMTN, SETGETN      | FEAT_MOPS&&FEAT_MTE |

## Load/store no-allocate pair (offset)

The encodings in this section are decoded from Loads and Stores.

<!-- image -->

| 31 30 29   | 27 26   | 25 23 22 21   | 15 14   | 10 9   | 5 4   | 0   |
|------------|---------|---------------|---------|--------|-------|-----|
| opc        | 1 0     | 1 VR 0 0 0 L  | imm7    | Rt2    | Rn    | Rt  |

|   opc |   VR | L   | Instruction Details     | Feature             |
|-------|------|-----|-------------------------|---------------------|
|    00 |    0 | 0   | STNP -32-bit            | -                   |
|    00 |    0 | 1   | LDNP -32-bit            | -                   |
|    00 |    1 | 0   | STNP (SIMD&FP) -32-bit  | FEAT_FP             |
|    00 |    1 | 1   | LDNP (SIMD&FP) -32-bit  | FEAT_FP             |
|    01 |    0 | x   | UNALLOCATED             | -                   |
|    01 |    1 | 0   | STNP (SIMD&FP) -64-bit  | FEAT_FP             |
|    01 |    1 | 1   | LDNP (SIMD&FP) -64-bit  | FEAT_FP             |
|    10 |    0 | 0   | STNP -64-bit            | -                   |
|    10 |    0 | 1   | LDNP -64-bit            | -                   |
|    10 |    1 | 0   | STNP (SIMD&FP) -128-bit | FEAT_FP             |
|    10 |    1 | 1   | LDNP (SIMD&FP) -128-bit | FEAT_FP             |
|    11 |    0 | 0   | STTNP                   | FEAT_LSUI           |
|    11 |    0 | 1   | LDTNP                   | FEAT_LSUI           |
|    11 |    1 | 0   | STTNP (SIMD&FP)         | FEAT_FP &&FEAT_LSUI |
|    11 |    1 | 1   | LDTNP (SIMD&FP)         | FEAT_FP &&FEAT_LSUI |

## Load/store register pair (post-indexed)

The encodings in this section are decoded from Loads and Stores.

<!-- image -->

| 31 30   | 29 27 26 25   | 23 22 21   | 15 14   | 10 9   | 5 4   | 0   |
|---------|---------------|------------|---------|--------|-------|-----|
| opc     | 1 0 1 VR      | 0 0 1 L    | imm7    | Rt2    | Rn    | Rt  |

|   opc |   VR |   L | Instruction Details    | Feature             |
|-------|------|-----|------------------------|---------------------|
|    00 |    0 |   0 | STP -32-bit            | -                   |
|    00 |    0 |   1 | LDP -32-bit            | -                   |
|    00 |    1 |   0 | STP (SIMD&FP) -32-bit  | FEAT_FP             |
|    00 |    1 |   1 | LDP (SIMD&FP) -32-bit  | FEAT_FP             |
|    01 |    0 |   0 | STGP                   | FEAT_MTE            |
|    01 |    0 |   1 | LDPSW                  | -                   |
|    01 |    1 |   0 | STP (SIMD&FP) -64-bit  | FEAT_FP             |
|    01 |    1 |   1 | LDP (SIMD&FP) -64-bit  | FEAT_FP             |
|    10 |    0 |   0 | STP -64-bit            | -                   |
|    10 |    0 |   1 | LDP -64-bit            | -                   |
|    10 |    1 |   0 | STP (SIMD&FP) -128-bit | FEAT_FP             |
|    10 |    1 |   1 | LDP (SIMD&FP) -128-bit | FEAT_FP             |
|    11 |    0 |   0 | STTP                   | FEAT_LSUI           |
|    11 |    0 |   1 | LDTP                   | FEAT_LSUI           |
|    11 |    1 |   0 | STTP (SIMD&FP)         | FEAT_FP &&FEAT_LSUI |
|    11 |    1 |   1 | LDTP (SIMD&FP)         | FEAT_FP &&FEAT_LSUI |

## Load/store register pair (offset)

The encodings in this section are decoded from Loads and Stores.

<!-- image -->

| 31 30   |   29 | 27 26 25 23   |      | 10   | 5   | 0   |
|---------|------|---------------|------|------|-----|-----|
| opc     |    1 | 0 1 VR 0 1 0  | imm7 | Rt2  | Rn  | Rt  |

|   opc |   VR |   L | Instruction Details    | Feature   |
|-------|------|-----|------------------------|-----------|
|    00 |    0 |   0 | STP -32-bit            | -         |
|    00 |    0 |   1 | LDP -32-bit            | -         |
|    00 |    1 |   0 | STP (SIMD&FP) -32-bit  | FEAT_FP   |
|    00 |    1 |   1 | LDP (SIMD&FP) -32-bit  | FEAT_FP   |
|    01 |    0 |   0 | STGP                   | FEAT_MTE  |
|    01 |    0 |   1 | LDPSW                  | -         |
|    01 |    1 |   0 | STP (SIMD&FP) -64-bit  | FEAT_FP   |
|    01 |    1 |   1 | LDP (SIMD&FP) -64-bit  | FEAT_FP   |
|    10 |    0 |   0 | STP -64-bit            | -         |
|    10 |    0 |   1 | LDP -64-bit            | -         |
|    10 |    1 |   0 | STP (SIMD&FP) -128-bit | FEAT_FP   |
|    10 |    1 |   1 | LDP (SIMD&FP) -128-bit | FEAT_FP   |

|   opc |   VR |   L | Instruction Details   | Feature             |
|-------|------|-----|-----------------------|---------------------|
|    11 |    0 |   0 | STTP                  | FEAT_LSUI           |
|    11 |    0 |   1 | LDTP                  | FEAT_LSUI           |
|    11 |    1 |   0 | STTP (SIMD&FP)        | FEAT_FP &&FEAT_LSUI |
|    11 |    1 |   1 | LDTP (SIMD&FP)        | FEAT_FP &&FEAT_LSUI |

## Load/store register pair (pre-indexed)

The encodings in this section are decoded from Loads and Stores.

<!-- image -->

| 31 30   |   29 | 27 26 25     | 23 22 21   | 15 14   | 10 9   | 4   |
|---------|------|--------------|------------|---------|--------|-----|
| opc     |    1 | 0 1 VR 0 1 1 | L          | Rt2     | Rn     | Rt  |

|   opc |   VR |   L | Instruction Details    | Feature             |
|-------|------|-----|------------------------|---------------------|
|    00 |    0 |   0 | STP -32-bit            | -                   |
|    00 |    0 |   1 | LDP -32-bit            | -                   |
|    00 |    1 |   0 | STP (SIMD&FP) -32-bit  | FEAT_FP             |
|    00 |    1 |   1 | LDP (SIMD&FP) -32-bit  | FEAT_FP             |
|    01 |    0 |   0 | STGP                   | FEAT_MTE            |
|    01 |    0 |   1 | LDPSW                  | -                   |
|    01 |    1 |   0 | STP (SIMD&FP) -64-bit  | FEAT_FP             |
|    01 |    1 |   1 | LDP (SIMD&FP) -64-bit  | FEAT_FP             |
|    10 |    0 |   0 | STP -64-bit            | -                   |
|    10 |    0 |   1 | LDP -64-bit            | -                   |
|    10 |    1 |   0 | STP (SIMD&FP) -128-bit | FEAT_FP             |
|    10 |    1 |   1 | LDP (SIMD&FP) -128-bit | FEAT_FP             |
|    11 |    0 |   0 | STTP                   | FEAT_LSUI           |
|    11 |    0 |   1 | LDTP                   | FEAT_LSUI           |
|    11 |    1 |   0 | STTP (SIMD&FP)         | FEAT_FP &&FEAT_LSUI |
|    11 |    1 |   1 | LDTP (SIMD&FP)         | FEAT_FP &&FEAT_LSUI |

## Load/store register (unscaled immediate)

The encodings in this section are decoded from Loads and Stores.

<!-- image -->

| 31 30   | 29   | 27 26 25 24 23   | 22 21   |     |    | 12 11 10   | 5 4   |    |
|---------|------|------------------|---------|-----|----|------------|-------|----|
| size    |      | 1 1 1 VR         | 0 0     | opc |  0 | 0 0        | Rn    | Rt |

| size   |   VR | opc   | Instruction Details     | Feature   |
|--------|------|-------|-------------------------|-----------|
| 00     |    0 | 00    | STURB                   | -         |
| 00     |    0 | 01    | LDURB                   | -         |
| 00     |    0 | 10    | LDURSB -64-bit          | -         |
| 00     |    0 | 11    | LDURSB -32-bit          | -         |
| 00     |    1 | 00    | STUR (SIMD&FP) -8-bit   | FEAT_FP   |
| 00     |    1 | 01    | LDUR(SIMD&FP) -8-bit    | FEAT_FP   |
| 00     |    1 | 10    | STUR (SIMD&FP) -128-bit | FEAT_FP   |
| 00     |    1 | 11    | LDUR(SIMD&FP) -128-bit  | FEAT_FP   |
| 01     |    0 | 00    | STURH                   | -         |
| 01     |    0 | 01    | LDURH                   | -         |
| 01     |    0 | 10    | LDURSH-64-bit           | -         |
| 01     |    0 | 11    | LDURSH-32-bit           | -         |
| 01     |    1 | 00    | STUR (SIMD&FP) -16-bit  | FEAT_FP   |
| 01     |    1 | 01    | LDUR(SIMD&FP) -16-bit   | FEAT_FP   |
| 1x     |    0 | 11    | UNALLOCATED             | -         |
| 10     |    0 | 00    | STUR -32-bit            | -         |
| 10     |    0 | 01    | LDUR-32-bit             | -         |
| 10     |    0 | 10    | LDURSW                  | -         |
| 10     |    1 | 00    | STUR (SIMD&FP) -32-bit  | FEAT_FP   |
| 10     |    1 | 01    | LDUR(SIMD&FP) -32-bit   | FEAT_FP   |
| 11     |    0 | 00    | STUR -64-bit            | -         |
| 11     |    0 | 01    | LDUR-64-bit             | -         |
| 11     |    0 | 10    | PRFUM                   | -         |
| 11     |    1 | 00    | STUR (SIMD&FP) -64-bit  | FEAT_FP   |
| 11     |    1 | 01    | LDUR(SIMD&FP) -64-bit   | FEAT_FP   |
| != 00  |    1 | 1x    | UNALLOCATED             | -         |

## Load/store register (immediate post-indexed)

The encodings in this section are decoded from Loads and Stores.

<!-- image -->

| 31   | 30 29   | 27 26   |   25 24 | 23   |   22 21 |      | 12 11 10   | 5 4   | 0   |
|------|---------|---------|---------|------|---------|------|------------|-------|-----|
| size | 1 1     | 1 VR 0  |       0 | opc  |       0 | imm9 | 0 1        | Rn    | Rt  |

## Load/store register (unprivileged)

The encodings in this section are decoded from Loads and Stores.

<!-- image -->

| 31   |   30 29 | 27 26 25 24 23   |     | 22 21   |    | 11 10 9   | 5   | 4   |
|------|---------|------------------|-----|---------|----|-----------|-----|-----|
| size |       1 | 1 1 VR           | 0 0 | opc     |  0 | 1 0       | Rn  | Rt  |

| size   | VR opc Instruction Details   |
|--------|------------------------------|
| xx     | 1 xx UNALLOCATED             |

|   size | VR   | opc   | Instruction Details               | Feature   |
|--------|------|-------|-----------------------------------|-----------|
|     00 | 0    | 00    | STRB (immediate)                  | -         |
|     00 | 0    | 01    | LDRB(immediate)                   | -         |
|     00 | 0    | 10    | LDRSB (immediate) -64-bit         | -         |
|     00 | 0    | 11    | LDRSB (immediate) -32-bit         | -         |
|     00 | 1    | 00    | STR (immediate, SIMD&FP) -8-bit   | FEAT_FP   |
|     00 | 1    | 01    | LDR(immediate, SIMD&FP) -8-bit    | FEAT_FP   |
|     00 | 1    | 10    | STR (immediate, SIMD&FP) -128-bit | FEAT_FP   |
|     00 | 1    | 11    | LDR(immediate, SIMD&FP) -128-bit  | FEAT_FP   |
|     01 | 0    | 00    | STRH (immediate)                  | -         |
|     01 | 0    | 01    | LDRH(immediate)                   | -         |
|     01 | 0    | 10    | LDRSH (immediate) -64-bit         | -         |
|     01 | 0    | 11    | LDRSH (immediate) -32-bit         | -         |
|     01 | 1    | 00    | STR (immediate, SIMD&FP) -16-bit  | FEAT_FP   |
|     01 | 1    | 01    | LDR(immediate, SIMD&FP) -16-bit   | FEAT_FP   |
|     01 | 1    | 1x    | UNALLOCATED                       | -         |
|     10 | 0    | 00    | STR (immediate) -32-bit           | -         |
|     10 | 0    | 01    | LDR(immediate) -32-bit            | -         |
|     10 | 0    | 10    | LDRSW(immediate)                  | -         |
|     10 | 0    | 11    | UNALLOCATED                       | -         |
|     10 | 1    | 00    | STR (immediate, SIMD&FP) -32-bit  | FEAT_FP   |
|     10 | 1    | 01    | LDR(immediate, SIMD&FP) -32-bit   | FEAT_FP   |
|     10 | 1    | 1x    | UNALLOCATED                       | -         |
|     11 | x    | 1x    | UNALLOCATED                       | -         |
|     11 | 0    | 00    | STR (immediate) -64-bit           | -         |
|     11 | 0    | 01    | LDR(immediate) -64-bit            | -         |
|     11 | 1    | 00    | STR (immediate, SIMD&FP) -64-bit  | FEAT_FP   |
|     11 | 1    | 01    | LDR(immediate, SIMD&FP) -64-bit   | FEAT_FP   |

|   size |   VR | opc   | Instruction Details   |
|--------|------|-------|-----------------------|
|     00 |    0 | 00    | STTRB                 |
|     00 |    0 | 01    | LDTRB                 |
|     00 |    0 | 10    | LDTRSB -64-bit        |
|     00 |    0 | 11    | LDTRSB -32-bit        |
|     01 |    0 | 00    | STTRH                 |
|     01 |    0 | 01    | LDTRH                 |
|     01 |    0 | 10    | LDTRSH -64-bit        |
|     01 |    0 | 11    | LDTRSH -32-bit        |
|     10 |    0 | 00    | STTR -32-bit          |
|     10 |    0 | 01    | LDTR -32-bit          |
|     10 |    0 | 10    | LDTRSW                |
|     10 |    0 | 11    | UNALLOCATED           |
|     11 |    0 | 00    | STTR -64-bit          |
|     11 |    0 | 01    | LDTR -64-bit          |
|     11 |    0 | 1x    | UNALLOCATED           |

## Load/store register (immediate pre-indexed)

The encodings in this section are decoded from Loads and Stores.

<!-- image -->

| 31   | 30 29   | 27 26 25   | 24   | 23 22   |   21 |      | 12 11 10 9   | 5 4   |    |
|------|---------|------------|------|---------|------|------|--------------|-------|----|
| size |         | 1 1 1 VR   | 0 0  | opc     |    0 | imm9 | 1 1          | Rn    | Rt |

|   size |   VR |   opc | Instruction Details               | Feature   |
|--------|------|-------|-----------------------------------|-----------|
|     00 |    0 |    00 | STRB (immediate)                  | -         |
|     00 |    0 |    01 | LDRB(immediate)                   | -         |
|     00 |    0 |    10 | LDRSB (immediate) -64-bit         | -         |
|     00 |    0 |    11 | LDRSB (immediate) -32-bit         | -         |
|     00 |    1 |    00 | STR (immediate, SIMD&FP) -8-bit   | FEAT_FP   |
|     00 |    1 |    01 | LDR(immediate, SIMD&FP) -8-bit    | FEAT_FP   |
|     00 |    1 |    10 | STR (immediate, SIMD&FP) -128-bit | FEAT_FP   |
|     00 |    1 |    11 | LDR(immediate, SIMD&FP) -128-bit  | FEAT_FP   |
|     01 |    0 |    00 | STRH (immediate)                  | -         |
|     01 |    0 |    01 | LDRH(immediate)                   | -         |
|     01 |    0 |    10 | LDRSH (immediate) -64-bit         | -         |
|     01 |    0 |    11 | LDRSH (immediate) -32-bit         | -         |
|     01 |    1 |    00 | STR (immediate, SIMD&FP) -16-bit  | FEAT_FP   |

## Atomic memory operations

The encodings in this section are decoded from Loads and Stores.

<!-- image -->

| 31 30   | 29   | 27 26 25 24 23   | 20 16 12 11 10   | 22   |    |   21 |    | 15 14   |     | 5 4   | 0   |
|---------|------|------------------|------------------|------|----|------|----|---------|-----|-------|-----|
| size    |      | 1 1 1 VR         | 0 0 A            |      | R  |    1 | Rs | o3 opc  | 0 0 | Rn    | Rt  |

| size   |   VR | A   | R   | Rs    |   o3 | opc   | Rt       | Instruction Details   | Feature   |
|--------|------|-----|-----|-------|------|-------|----------|-----------------------|-----------|
| xx     |    0 | 0   | x   | xxxxx |    1 | 100   | xxxxx    | UNALLOCATED           | -         |
| xx     |    0 | 0   | x   | xxxxx |    1 | 11x   | xxxxx    | UNALLOCATED           | -         |
| xx     |    0 | 1   | 1   | xxxxx |    1 | 100   | xxxxx    | UNALLOCATED           | -         |
| xx     |    1 | x   | x   | xxxxx |    0 | 001   | xxxxx    | UNALLOCATED           | -         |
| xx     |    1 | x   | x   | xxxxx |    0 | 01x   | xxxxx    | UNALLOCATED           | -         |
| xx     |    1 | 0   | x   | xxxxx |    1 | xxx   | != 11111 | UNALLOCATED           | -         |
| xx     |    1 | 0   | x   | xxxxx |    1 | 001   | 11111    | UNALLOCATED           | -         |
| xx     |    1 | 0   | x   | xxxxx |    1 | 01x   | 11111    | UNALLOCATED           | -         |
| xx     |    1 | 1   | x   | xxxxx |    1 | xxx   | xxxxx    | UNALLOCATED           | -         |
| 0x     |    0 | x   | 0   | xxxxx |    1 | 101   | xxxxx    | UNALLOCATED           | -         |
| 0x     |    0 | 0   | 1   | xxxxx |    1 | 101   | xxxxx    | UNALLOCATED           | -         |
| 0x     |    0 | 1   | x   | xxxxx |    1 | 11x   | xxxxx    | UNALLOCATED           | -         |
| 0x     |    0 | 1   | 1   | xxxxx |    1 | 101   | xxxxx    | UNALLOCATED           | -         |

|   size | VR   | opc   | Instruction Details              | Feature   |
|--------|------|-------|----------------------------------|-----------|
|     01 | 1    | 01    | LDR(immediate, SIMD&FP) -16-bit  | FEAT_FP   |
|     01 | 1    | 1x    | UNALLOCATED                      | -         |
|     10 | 0    | 00    | STR (immediate) -32-bit          | -         |
|     10 | 0    | 01    | LDR(immediate) -32-bit           | -         |
|     10 | 0    | 10    | LDRSW(immediate)                 | -         |
|     10 | 0    | 11    | UNALLOCATED                      | -         |
|     10 | 1    | 00    | STR (immediate, SIMD&FP) -32-bit | FEAT_FP   |
|     10 | 1    | 01    | LDR(immediate, SIMD&FP) -32-bit  | FEAT_FP   |
|     10 | 1    | 1x    | UNALLOCATED                      | -         |
|     11 | x    | 1x    | UNALLOCATED                      | -         |
|     11 | 0    | 00    | STR (immediate) -64-bit          | -         |
|     11 | 0    | 01    | LDR(immediate) -64-bit           | -         |
|     11 | 1    | 00    | STR (immediate, SIMD&FP) -64-bit | FEAT_FP   |
|     11 | 1    | 01    | LDR(immediate, SIMD&FP) -64-bit  | FEAT_FP   |

|   size |   VR |   A |   R | Rs    |   o3 |   opc | Rt    | Instruction Details                                         | Feature   |
|--------|------|-----|-----|-------|------|-------|-------|-------------------------------------------------------------|-----------|
|     00 |    0 |   0 |   0 | xxxxx |    0 |   000 | xxxxx | LDADDB, LDADDAB, LDADDALB, LDADDLB-Nomemoryordering         | FEAT_LSE  |
|     00 |    0 |   0 |   0 | xxxxx |    0 |   001 | xxxxx | LDCLRB, LDCLRAB, LDCLRALB, LDCLRLB -Nomemoryordering        | FEAT_LSE  |
|     00 |    0 |   0 |   0 | xxxxx |    0 |   010 | xxxxx | LDEORB, LDEORAB, LDEORALB, LDEORLB -Nomemoryordering        | FEAT_LSE  |
|     00 |    0 |   0 |   0 | xxxxx |    0 |   011 | xxxxx | LDSETB, LDSETAB, LDSETALB, LDSETLB -Nomemoryordering        | FEAT_LSE  |
|     00 |    0 |   0 |   0 | xxxxx |    0 |   100 | xxxxx | LDSMAXB, LDSMAXAB, LDSMAXALB, LDSMAXLB - No memory ordering | FEAT_LSE  |
|     00 |    0 |   0 |   0 | xxxxx |    0 |   101 | xxxxx | LDSMINB, LDSMINAB, LDSMINALB, LDSMINLB -Nomemoryordering    | FEAT_LSE  |
|     00 |    0 |   0 |   0 | xxxxx |    0 |   110 | xxxxx | LDUMAXB, LDUMAXAB, LDUMAXALB, LDUMAXLB - No memory ordering | FEAT_LSE  |
|     00 |    0 |   0 |   0 | xxxxx |    0 |   111 | xxxxx | LDUMINB, LDUMINAB, LDUMINALB, LDUMINLB - No memory ordering | FEAT_LSE  |
|     00 |    0 |   0 |   0 | xxxxx |    1 |   000 | xxxxx | SWPB, SWPAB, SWPALB, SWPLB - SWPB                           | FEAT_LSE  |
|     00 |    0 |   0 |   0 | xxxxx |    1 |   001 | xxxxx | RCWCLR, RCWCLRA, RCWCLRAL, RCWCLRL-RCWCLR                   | FEAT_THE  |
|     00 |    0 |   0 |   0 | xxxxx |    1 |   010 | xxxxx | RCWSWP, RCWSWPA, RCWSWPAL, RCWSWPL-RCWSWP                   | FEAT_THE  |
|     00 |    0 |   0 |   0 | xxxxx |    1 |   011 | xxxxx | RCWSET, RCWSETA, RCWSETAL, RCWSETL-RCWSET                   | FEAT_THE  |
|     00 |    0 |   0 |   1 | xxxxx |    0 |   000 | xxxxx | LDADDB, LDADDAB, LDADDALB, LDADDLB-Release                  | FEAT_LSE  |
|     00 |    0 |   0 |   1 | xxxxx |    0 |   001 | xxxxx | LDCLRB, LDCLRAB, LDCLRALB, LDCLRLB -Release                 | FEAT_LSE  |
|     00 |    0 |   0 |   1 | xxxxx |    0 |   010 | xxxxx | LDEORB, LDEORAB, LDEORALB, LDEORLB -Release                 | FEAT_LSE  |
|     00 |    0 |   0 |   1 | xxxxx |    0 |   011 | xxxxx | LDSETB, LDSETAB, LDSETALB, LDSETLB -Release                 | FEAT_LSE  |
|     00 |    0 |   0 |   1 | xxxxx |    0 |   100 | xxxxx | LDSMAXB, LDSMAXAB, LDSMAXALB, LDSMAXLB-Release              | FEAT_LSE  |
|     00 |    0 |   0 |   1 | xxxxx |    0 |   101 | xxxxx | LDSMINB, LDSMINAB, LDSMINALB, LDSMINLB -Release             | FEAT_LSE  |
|     00 |    0 |   0 |   1 | xxxxx |    0 |   110 | xxxxx | LDUMAXB, LDUMAXAB, LDUMAXALB, LDUMAXLB - Release            | FEAT_LSE  |
|     00 |    0 |   0 |   1 | xxxxx |    0 |   111 | xxxxx | LDUMINB, LDUMINAB, LDUMINALB,LDUMINLB -Release              | FEAT_LSE  |
|     00 |    0 |   0 |   1 | xxxxx |    1 |   000 | xxxxx | SWPB, SWPAB, SWPALB, SWPLB - SWPLB                          | FEAT_LSE  |
|     00 |    0 |   0 |   1 | xxxxx |    1 |   001 | xxxxx | RCWCLR, RCWCLRA, RCWCLRAL, RCWCLRL-RCWCLRL                  | FEAT_THE  |
|     00 |    0 |   0 |   1 | xxxxx |    1 |   010 | xxxxx | RCWSWP, RCWSWPA, RCWSWPAL, RCWSWPL-RCWSWPL                  | FEAT_THE  |
|     00 |    0 |   0 |   1 | xxxxx |    1 |   011 | xxxxx | RCWSET, RCWSETA, RCWSETAL, RCWSETL-RCWSETL                  | FEAT_THE  |

|   size |   VR |   A |   R | Rs    |   o3 |   opc | Rt    | Instruction Details                                      | Feature    |
|--------|------|-----|-----|-------|------|-------|-------|----------------------------------------------------------|------------|
|     00 |    0 |   1 |   0 | xxxxx |    0 |   000 | xxxxx | LDADDB, LDADDAB, LDADDALB, LDADDLB-Acquire               | FEAT_LSE   |
|     00 |    0 |   1 |   0 | xxxxx |    0 |   001 | xxxxx | LDCLRB, LDCLRAB, LDCLRALB, LDCLRLB -Acquire              | FEAT_LSE   |
|     00 |    0 |   1 |   0 | xxxxx |    0 |   010 | xxxxx | LDEORB, LDEORAB, LDEORALB, LDEORLB -Acquire              | FEAT_LSE   |
|     00 |    0 |   1 |   0 | xxxxx |    0 |   011 | xxxxx | LDSETB, LDSETAB, LDSETALB, LDSETLB -Acquire              | FEAT_LSE   |
|     00 |    0 |   1 |   0 | xxxxx |    0 |   100 | xxxxx | LDSMAXB, LDSMAXAB, LDSMAXALB, LDSMAXLB -Acquire          | FEAT_LSE   |
|     00 |    0 |   1 |   0 | xxxxx |    0 |   101 | xxxxx | LDSMINB, LDSMINAB, LDSMINALB, LDSMINLB -Acquire          | FEAT_LSE   |
|     00 |    0 |   1 |   0 | xxxxx |    0 |   110 | xxxxx | LDUMAXB, LDUMAXAB, LDUMAXALB, LDUMAXLB - Acquire         | FEAT_LSE   |
|     00 |    0 |   1 |   0 | xxxxx |    0 |   111 | xxxxx | LDUMINB, LDUMINAB, LDUMINALB,LDUMINLB -Acquire           | FEAT_LSE   |
|     00 |    0 |   1 |   0 | xxxxx |    1 |   000 | xxxxx | SWPB, SWPAB, SWPALB, SWPLB - SWPAB                       | FEAT_LSE   |
|     00 |    0 |   1 |   0 | xxxxx |    1 |   001 | xxxxx | RCWCLR, RCWCLRA, RCWCLRAL, RCWCLRL-RCWCLRA               | FEAT_THE   |
|     00 |    0 |   1 |   0 | xxxxx |    1 |   010 | xxxxx | RCWSWP, RCWSWPA, RCWSWPAL, RCWSWPL-RCWSWPA               | FEAT_THE   |
|     00 |    0 |   1 |   0 | xxxxx |    1 |   011 | xxxxx | RCWSET, RCWSETA, RCWSETAL, RCWSETL-RCWSETA               | FEAT_THE   |
|     00 |    0 |   1 |   0 | xxxxx |    1 |   100 | xxxxx | LDAPRB                                                   | FEAT_LRCPC |
|     00 |    0 |   1 |   1 | xxxxx |    0 |   000 | xxxxx | LDADDB, LDADDAB, LDADDALB, LDADDLB-Acquire-release       | FEAT_LSE   |
|     00 |    0 |   1 |   1 | xxxxx |    0 |   001 | xxxxx | LDCLRB, LDCLRAB, LDCLRALB, LDCLRLB -Acquire-release      | FEAT_LSE   |
|     00 |    0 |   1 |   1 | xxxxx |    0 |   010 | xxxxx | LDEORB, LDEORAB, LDEORALB, LDEORLB -Acquire-release      | FEAT_LSE   |
|     00 |    0 |   1 |   1 | xxxxx |    0 |   011 | xxxxx | LDSETB, LDSETAB, LDSETALB, LDSETLB -Acquire-release      | FEAT_LSE   |
|     00 |    0 |   1 |   1 | xxxxx |    0 |   100 | xxxxx | LDSMAXB, LDSMAXAB, LDSMAXALB, LDSMAXLB - Acquire-release | FEAT_LSE   |
|     00 |    0 |   1 |   1 | xxxxx |    0 |   101 | xxxxx | LDSMINB, LDSMINAB, LDSMINALB, LDSMINLB -Acquire-release  | FEAT_LSE   |
|     00 |    0 |   1 |   1 | xxxxx |    0 |   110 | xxxxx | LDUMAXB, LDUMAXAB, LDUMAXALB, LDUMAXLB - Acquire-release | FEAT_LSE   |
|     00 |    0 |   1 |   1 | xxxxx |    0 |   111 | xxxxx | LDUMINB, LDUMINAB, LDUMINALB, LDUMINLB - Acquire-release | FEAT_LSE   |
|     00 |    0 |   1 |   1 | xxxxx |    1 |   000 | xxxxx | SWPB, SWPAB, SWPALB, SWPLB - SWPALB                      | FEAT_LSE   |
|     00 |    0 |   1 |   1 | xxxxx |    1 |   001 | xxxxx | RCWCLR, RCWCLRA, RCWCLRAL, RCWCLRL-RCWCLRAL              | FEAT_THE   |

|   size |   VR |   A |   R | Rs    |   o3 |   opc | Rt    | Instruction Details                                                 | Feature   |
|--------|------|-----|-----|-------|------|-------|-------|---------------------------------------------------------------------|-----------|
|     00 |    0 |   1 |   1 | xxxxx |    1 |   010 | xxxxx | RCWSWP, RCWSWPA, RCWSWPAL, RCWSWPL-RCWSWPAL                         | FEAT_THE  |
|     00 |    0 |   1 |   1 | xxxxx |    1 |   011 | xxxxx | RCWSET, RCWSETA, RCWSETAL, RCWSETL-RCWSETAL                         | FEAT_THE  |
|     00 |    1 |   0 |   0 | xxxxx |    0 |   000 | xxxxx | LDBFADD, LDBFADDA, LDBFADDAL, LDBFADDL - No memory ordering         | FEAT_LSFE |
|     00 |    1 |   0 |   0 | xxxxx |    0 |   100 | xxxxx | LDBFMAX, LDBFMAXA, LDBFMAXAL, LDBFMAXL - No memory ordering         | FEAT_LSFE |
|     00 |    1 |   0 |   0 | xxxxx |    0 |   101 | xxxxx | LDBFMIN, LDBFMINA, LDBFMINAL, LDBFMINL -Nomemoryordering            | FEAT_LSFE |
|     00 |    1 |   0 |   0 | xxxxx |    0 |   110 | xxxxx | LDBFMAXNM, LDBFMAXNMA, LDBFMAXNMAL, LDBFMAXNML - No memory ordering | FEAT_LSFE |
|     00 |    1 |   0 |   0 | xxxxx |    0 |   111 | xxxxx | LDBFMINNM, LDBFMINNMA, LDBFMINNMAL, LDBFMINNML -Nomemoryordering    | FEAT_LSFE |
|     00 |    1 |   0 |   0 | xxxxx |    1 |   000 | 11111 | STBFADD, STBFADDL - No memory ordering                              | FEAT_LSFE |
|     00 |    1 |   0 |   0 | xxxxx |    1 |   100 | 11111 | STBFMAX, STBFMAXL -No memory ordering                               | FEAT_LSFE |
|     00 |    1 |   0 |   0 | xxxxx |    1 |   101 | 11111 | STBFMIN, STBFMINL - No memory ordering                              | FEAT_LSFE |
|     00 |    1 |   0 |   0 | xxxxx |    1 |   110 | 11111 | STBFMAXNM, STBFMAXNML - No memory ordering                          | FEAT_LSFE |
|     00 |    1 |   0 |   0 | xxxxx |    1 |   111 | 11111 | STBFMINNM, STBFMINNML - No memory ordering                          | FEAT_LSFE |
|     00 |    1 |   0 |   1 | xxxxx |    0 |   000 | xxxxx | LDBFADD, LDBFADDA, LDBFADDAL, LDBFADDL -Release                     | FEAT_LSFE |
|     00 |    1 |   0 |   1 | xxxxx |    0 |   100 | xxxxx | LDBFMAX, LDBFMAXA, LDBFMAXAL, LDBFMAXL-Release                      | FEAT_LSFE |
|     00 |    1 |   0 |   1 | xxxxx |    0 |   101 | xxxxx | LDBFMIN, LDBFMINA, LDBFMINAL, LDBFMINL -Release                     | FEAT_LSFE |
|     00 |    1 |   0 |   1 | xxxxx |    0 |   110 | xxxxx | LDBFMAXNM, LDBFMAXNMA, LDBFMAXNMAL, LDBFMAXNML - Release            | FEAT_LSFE |
|     00 |    1 |   0 |   1 | xxxxx |    0 |   111 | xxxxx | LDBFMINNM, LDBFMINNMA, LDBFMINNMAL, LDBFMINNML -Release             | FEAT_LSFE |
|     00 |    1 |   0 |   1 | xxxxx |    1 |   000 | 11111 | STBFADD, STBFADDL -Release                                          | FEAT_LSFE |
|     00 |    1 |   0 |   1 | xxxxx |    1 |   100 | 11111 | STBFMAX,STBFMAXL -Release                                           | FEAT_LSFE |
|     00 |    1 |   0 |   1 | xxxxx |    1 |   101 | 11111 | STBFMIN, STBFMINL -Release                                          | FEAT_LSFE |
|     00 |    1 |   0 |   1 | xxxxx |    1 |   110 | 11111 | STBFMAXNM, STBFMAXNML - Release                                     | FEAT_LSFE |
|     00 |    1 |   0 |   1 | xxxxx |    1 |   111 | 11111 | STBFMINNM, STBFMINNML - Release                                     | FEAT_LSFE |
|     00 |    1 |   1 |   0 | xxxxx |    0 |   000 | xxxxx | LDBFADD, LDBFADDA, LDBFADDAL, LDBFADDL -Acquire                     | FEAT_LSFE |

|   size |   VR |   A |   R | Rs    |   o3 |   opc | Rt    | Instruction Details                                              | Feature   |
|--------|------|-----|-----|-------|------|-------|-------|------------------------------------------------------------------|-----------|
|     00 |    1 |   1 |   0 | xxxxx |    0 |   100 | xxxxx | LDBFMAX, LDBFMAXA, LDBFMAXAL, LDBFMAXL -Acquire                  | FEAT_LSFE |
|     00 |    1 |   1 |   0 | xxxxx |    0 |   101 | xxxxx | LDBFMIN, LDBFMINA, LDBFMINAL, LDBFMINL -Acquire                  | FEAT_LSFE |
|     00 |    1 |   1 |   0 | xxxxx |    0 |   110 | xxxxx | LDBFMAXNM, LDBFMAXNMA, LDBFMAXNMAL, LDBFMAXNML - Acquire         | FEAT_LSFE |
|     00 |    1 |   1 |   0 | xxxxx |    0 |   111 | xxxxx | LDBFMINNM, LDBFMINNMA, LDBFMINNMAL, LDBFMINNML -Acquire          | FEAT_LSFE |
|     00 |    1 |   1 |   1 | xxxxx |    0 |   000 | xxxxx | LDBFADD, LDBFADDA, LDBFADDAL, LDBFADDL - Acquire-release         | FEAT_LSFE |
|     00 |    1 |   1 |   1 | xxxxx |    0 |   100 | xxxxx | LDBFMAX, LDBFMAXA, LDBFMAXAL, LDBFMAXL - Acquire-release         | FEAT_LSFE |
|     00 |    1 |   1 |   1 | xxxxx |    0 |   101 | xxxxx | LDBFMIN, LDBFMINA, LDBFMINAL, LDBFMINL -Acquire-release          | FEAT_LSFE |
|     00 |    1 |   1 |   1 | xxxxx |    0 |   110 | xxxxx | LDBFMAXNM, LDBFMAXNMA, LDBFMAXNMAL, LDBFMAXNML - Acquire-release | FEAT_LSFE |
|     00 |    1 |   1 |   1 | xxxxx |    0 |   111 | xxxxx | LDBFMINNM, LDBFMINNMA, LDBFMINNMAL, LDBFMINNML -Acquire-release  | FEAT_LSFE |
|     01 |    0 |   0 |   0 | xxxxx |    0 |   000 | xxxxx | LDADDH, LDADDAH, LDADDALH, LDADDLH-Nomemoryordering              | FEAT_LSE  |
|     01 |    0 |   0 |   0 | xxxxx |    0 |   001 | xxxxx | LDCLRH, LDCLRAH, LDCLRALH, LDCLRLH -Nomemoryordering             | FEAT_LSE  |
|     01 |    0 |   0 |   0 | xxxxx |    0 |   010 | xxxxx | LDEORH, LDEORAH, LDEORALH, LDEORLH-Nomemoryordering              | FEAT_LSE  |
|     01 |    0 |   0 |   0 | xxxxx |    0 |   011 | xxxxx | LDSETH, LDSETAH, LDSETALH, LDSETLH -Nomemoryordering             | FEAT_LSE  |
|     01 |    0 |   0 |   0 | xxxxx |    0 |   100 | xxxxx | LDSMAXH, LDSMAXAH, LDSMAXALH, LDSMAXLH - No memory ordering      | FEAT_LSE  |
|     01 |    0 |   0 |   0 | xxxxx |    0 |   101 | xxxxx | LDSMINH, LDSMINAH, LDSMINALH, LDSMINLH -Nomemoryordering         | FEAT_LSE  |
|     01 |    0 |   0 |   0 | xxxxx |    0 |   110 | xxxxx | LDUMAXH, LDUMAXAH, LDUMAXALH, LDUMAXLH - No memory ordering      | FEAT_LSE  |
|     01 |    0 |   0 |   0 | xxxxx |    0 |   111 | xxxxx | LDUMINH, LDUMINAH, LDUMINALH, LDUMINLH - No memory ordering      | FEAT_LSE  |
|     01 |    0 |   0 |   0 | xxxxx |    1 |   000 | xxxxx | SWPH, SWPAH, SWPALH, SWPLH - SWPH                                | FEAT_LSE  |
|     01 |    0 |   0 |   0 | xxxxx |    1 |   001 | xxxxx | RCWSCLR, RCWSCLRA, RCWSCLRAL, RCWSCLRL - RCWSCLR                 | FEAT_THE  |
|     01 |    0 |   0 |   0 | xxxxx |    1 |   010 | xxxxx | RCWSSWP, RCWSSWPA, RCWSSWPAL, RCWSSWPL - RCWSSWP                 | FEAT_THE  |

|   size |   VR |   A |   R | Rs    |   o3 |   opc | Rt    | Instruction Details                               | Feature   |
|--------|------|-----|-----|-------|------|-------|-------|---------------------------------------------------|-----------|
|     01 |    0 |   0 |   0 | xxxxx |    1 |   011 | xxxxx | RCWSSET, RCWSSETA, RCWSSETAL, RCWSSETL-RCWSSET    | FEAT_THE  |
|     01 |    0 |   0 |   1 | xxxxx |    0 |   000 | xxxxx | LDADDH, LDADDAH, LDADDALH, LDADDLH-Release        | FEAT_LSE  |
|     01 |    0 |   0 |   1 | xxxxx |    0 |   001 | xxxxx | LDCLRH, LDCLRAH, LDCLRALH, LDCLRLH -Release       | FEAT_LSE  |
|     01 |    0 |   0 |   1 | xxxxx |    0 |   010 | xxxxx | LDEORH, LDEORAH, LDEORALH, LDEORLH-Release        | FEAT_LSE  |
|     01 |    0 |   0 |   1 | xxxxx |    0 |   011 | xxxxx | LDSETH, LDSETAH, LDSETALH, LDSETLH -Release       | FEAT_LSE  |
|     01 |    0 |   0 |   1 | xxxxx |    0 |   100 | xxxxx | LDSMAXH, LDSMAXAH, LDSMAXALH, LDSMAXLH -Release   | FEAT_LSE  |
|     01 |    0 |   0 |   1 | xxxxx |    0 |   101 | xxxxx | LDSMINH, LDSMINAH, LDSMINALH, LDSMINLH -Release   | FEAT_LSE  |
|     01 |    0 |   0 |   1 | xxxxx |    0 |   110 | xxxxx | LDUMAXH, LDUMAXAH, LDUMAXALH, LDUMAXLH - Release  | FEAT_LSE  |
|     01 |    0 |   0 |   1 | xxxxx |    0 |   111 | xxxxx | LDUMINH, LDUMINAH, LDUMINALH,LDUMINLH -Release    | FEAT_LSE  |
|     01 |    0 |   0 |   1 | xxxxx |    1 |   000 | xxxxx | SWPH, SWPAH, SWPALH, SWPLH - SWPLH                | FEAT_LSE  |
|     01 |    0 |   0 |   1 | xxxxx |    1 |   001 | xxxxx | RCWSCLR, RCWSCLRA, RCWSCLRAL, RCWSCLRL - RCWSCLRL | FEAT_THE  |
|     01 |    0 |   0 |   1 | xxxxx |    1 |   010 | xxxxx | RCWSSWP, RCWSSWPA, RCWSSWPAL, RCWSSWPL - RCWSSWPL | FEAT_THE  |
|     01 |    0 |   0 |   1 | xxxxx |    1 |   011 | xxxxx | RCWSSET, RCWSSETA, RCWSSETAL, RCWSSETL-RCWSSETL   | FEAT_THE  |
|     01 |    0 |   1 |   0 | xxxxx |    0 |   000 | xxxxx | LDADDH, LDADDAH, LDADDALH, LDADDLH-Acquire        | FEAT_LSE  |
|     01 |    0 |   1 |   0 | xxxxx |    0 |   001 | xxxxx | LDCLRH, LDCLRAH, LDCLRALH, LDCLRLH -Acquire       | FEAT_LSE  |
|     01 |    0 |   1 |   0 | xxxxx |    0 |   010 | xxxxx | LDEORH, LDEORAH, LDEORALH, LDEORLH-Acquire        | FEAT_LSE  |
|     01 |    0 |   1 |   0 | xxxxx |    0 |   011 | xxxxx | LDSETH, LDSETAH, LDSETALH, LDSETLH -Acquire       | FEAT_LSE  |
|     01 |    0 |   1 |   0 | xxxxx |    0 |   100 | xxxxx | LDSMAXH, LDSMAXAH, LDSMAXALH,LDSMAXLH -Acquire    | FEAT_LSE  |
|     01 |    0 |   1 |   0 | xxxxx |    0 |   101 | xxxxx | LDSMINH, LDSMINAH, LDSMINALH, LDSMINLH -Acquire   | FEAT_LSE  |
|     01 |    0 |   1 |   0 | xxxxx |    0 |   110 | xxxxx | LDUMAXH, LDUMAXAH, LDUMAXALH, LDUMAXLH - Acquire  | FEAT_LSE  |
|     01 |    0 |   1 |   0 | xxxxx |    0 |   111 | xxxxx | LDUMINH, LDUMINAH, LDUMINALH,LDUMINLH -Acquire    | FEAT_LSE  |
|     01 |    0 |   1 |   0 | xxxxx |    1 |   000 | xxxxx | SWPH, SWPAH, SWPALH, SWPLH - SWPAH                | FEAT_LSE  |

|   size |   VR |   A |   R | Rs    |   o3 |   opc | Rt    | Instruction Details                                                            | Feature    |
|--------|------|-----|-----|-------|------|-------|-------|--------------------------------------------------------------------------------|------------|
|     01 |    0 |   1 |   0 | xxxxx |    1 |   001 | xxxxx | RCWSCLR, RCWSCLRA, RCWSCLRAL, RCWSCLRL - RCWSCLRA                              | FEAT_THE   |
|     01 |    0 |   1 |   0 | xxxxx |    1 |   010 | xxxxx | RCWSSWP, RCWSSWPA, RCWSSWPAL, RCWSSWPL - RCWSSWPA                              | FEAT_THE   |
|     01 |    0 |   1 |   0 | xxxxx |    1 |   011 | xxxxx | RCWSSET, RCWSSETA, RCWSSETAL, RCWSSETL-RCWSSETA                                | FEAT_THE   |
|     01 |    0 |   1 |   0 | xxxxx |    1 |   100 | xxxxx | LDAPRH                                                                         | FEAT_LRCPC |
|     01 |    0 |   1 |   1 | xxxxx |    0 |   000 | xxxxx | LDADDH, LDADDAH, LDADDALH, LDADDLH-Acquire-release                             | FEAT_LSE   |
|     01 |    0 |   1 |   1 | xxxxx |    0 |   001 | xxxxx | LDCLRH, LDCLRAH, LDCLRALH, LDCLRLH -Acquire-release                            | FEAT_LSE   |
|     01 |    0 |   1 |   1 | xxxxx |    0 |   010 | xxxxx | LDEORH, LDEORAH, LDEORALH, LDEORLH-Acquire-release                             | FEAT_LSE   |
|     01 |    0 |   1 |   1 | xxxxx |    0 |   011 | xxxxx | LDSETH, LDSETAH, LDSETALH, LDSETLH -Acquire-release                            | FEAT_LSE   |
|     01 |    0 |   1 |   1 | xxxxx |    0 |   100 | xxxxx | LDSMAXH, LDSMAXAH, LDSMAXALH, LDSMAXLH - Acquire-release                       | FEAT_LSE   |
|     01 |    0 |   1 |   1 | xxxxx |    0 |   101 | xxxxx | LDSMINH, LDSMINAH, LDSMINALH, LDSMINLH -Acquire-release                        | FEAT_LSE   |
|     01 |    0 |   1 |   1 | xxxxx |    0 |   110 | xxxxx | LDUMAXH, LDUMAXAH, LDUMAXALH, LDUMAXLH - Acquire-release                       | FEAT_LSE   |
|     01 |    0 |   1 |   1 | xxxxx |    0 |   111 | xxxxx | LDUMINH, LDUMINAH, LDUMINALH, LDUMINLH - Acquire-release                       | FEAT_LSE   |
|     01 |    0 |   1 |   1 | xxxxx |    1 |   000 | xxxxx | SWPH, SWPAH, SWPALH, SWPLH - SWPALH                                            | FEAT_LSE   |
|     01 |    0 |   1 |   1 | xxxxx |    1 |   001 | xxxxx | RCWSCLR, RCWSCLRA, RCWSCLRAL, RCWSCLRL - RCWSCLRAL                             | FEAT_THE   |
|     01 |    0 |   1 |   1 | xxxxx |    1 |   010 | xxxxx | RCWSSWP, RCWSSWPA, RCWSSWPAL, RCWSSWPL - RCWSSWPAL                             | FEAT_THE   |
|     01 |    0 |   1 |   1 | xxxxx |    1 |   011 | xxxxx | RCWSSET, RCWSSETA, RCWSSETAL, RCWSSETL-RCWSSETAL                               | FEAT_THE   |
|     01 |    1 |   0 |   0 | xxxxx |    0 |   000 | xxxxx | LDFADD, LDFADDA, LDFADDAL, LDFADDL -Half-precision no memory ordering          | FEAT_LSFE  |
|     01 |    1 |   0 |   0 | xxxxx |    0 |   100 | xxxxx | LDFMAX, LDFMAXA, LDFMAXAL, LDFMAXL -Half-precision no memory ordering          | FEAT_LSFE  |
|     01 |    1 |   0 |   0 | xxxxx |    0 |   101 | xxxxx | LDFMIN, LDFMINA, LDFMINAL, LDFMINL - Half-precision no memory ordering         | FEAT_LSFE  |
|     01 |    1 |   0 |   0 | xxxxx |    0 |   110 | xxxxx | LDFMAXNM, LDFMAXNMA, LDFMAXNMAL, LDFMAXNML - Half-precision no memory ordering | FEAT_LSFE  |

|   size |   VR |   A |   R | Rs    |   o3 |   opc | Rt    | Instruction Details                                                            | Feature   |
|--------|------|-----|-----|-------|------|-------|-------|--------------------------------------------------------------------------------|-----------|
|     01 |    1 |   0 |   0 | xxxxx |    0 |   111 | xxxxx | LDFMINNM, LDFMINNMA, LDFMINNMAL, LDFMINNML - Half-precision no memory ordering | FEAT_LSFE |
|     01 |    1 |   0 |   0 | xxxxx |    1 |   000 | 11111 | STFADD,STFADDL-Half-precision no memory ordering                               | FEAT_LSFE |
|     01 |    1 |   0 |   0 | xxxxx |    1 |   100 | 11111 | STFMAX, STFMAXL - Half-precision no memory ordering                            | FEAT_LSFE |
|     01 |    1 |   0 |   0 | xxxxx |    1 |   101 | 11111 | STFMIN, STFMINL -Half-precision no memory ordering                             | FEAT_LSFE |
|     01 |    1 |   0 |   0 | xxxxx |    1 |   110 | 11111 | STFMAXNM, STFMAXNML - Half- precision no memory ordering                       | FEAT_LSFE |
|     01 |    1 |   0 |   0 | xxxxx |    1 |   111 | 11111 | STFMINNM, STFMINNML - Half- precision no memory ordering                       | FEAT_LSFE |
|     01 |    1 |   0 |   1 | xxxxx |    0 |   000 | xxxxx | LDFADD, LDFADDA, LDFADDAL, LDFADDL -Half-precision release                     | FEAT_LSFE |
|     01 |    1 |   0 |   1 | xxxxx |    0 |   100 | xxxxx | LDFMAX, LDFMAXA, LDFMAXAL, LDFMAXL-Half-precision release                      | FEAT_LSFE |
|     01 |    1 |   0 |   1 | xxxxx |    0 |   101 | xxxxx | LDFMIN, LDFMINA, LDFMINAL, LDFMINL -Half-precision release                     | FEAT_LSFE |
|     01 |    1 |   0 |   1 | xxxxx |    0 |   110 | xxxxx | LDFMAXNM, LDFMAXNMA, LDFMAXNMAL, LDFMAXNML - Half-precision release            | FEAT_LSFE |
|     01 |    1 |   0 |   1 | xxxxx |    0 |   111 | xxxxx | LDFMINNM, LDFMINNMA, LDFMINNMAL, LDFMINNML - Half-precision release            | FEAT_LSFE |
|     01 |    1 |   0 |   1 | xxxxx |    1 |   000 | 11111 | STFADD, STFADDL - Half-precision release                                       | FEAT_LSFE |
|     01 |    1 |   0 |   1 | xxxxx |    1 |   100 | 11111 | STFMAX, STFMAXL - Half-precision release                                       | FEAT_LSFE |
|     01 |    1 |   0 |   1 | xxxxx |    1 |   101 | 11111 | STFMIN, STFMINL - Half-precision release                                       | FEAT_LSFE |
|     01 |    1 |   0 |   1 | xxxxx |    1 |   110 | 11111 | STFMAXNM, STFMAXNML - Half- precision release                                  | FEAT_LSFE |
|     01 |    1 |   0 |   1 | xxxxx |    1 |   111 | 11111 | STFMINNM, STFMINNML - Half- precision release                                  | FEAT_LSFE |
|     01 |    1 |   1 |   0 | xxxxx |    0 |   000 | xxxxx | LDFADD, LDFADDA, LDFADDAL, LDFADDL -Half-precision acquire                     | FEAT_LSFE |
|     01 |    1 |   1 |   0 | xxxxx |    0 |   100 | xxxxx | LDFMAX, LDFMAXA, LDFMAXAL, LDFMAXL-Half-precision acquire                      | FEAT_LSFE |
|     01 |    1 |   1 |   0 | xxxxx |    0 |   101 | xxxxx | LDFMIN, LDFMINA, LDFMINAL, LDFMINL -Half-precision acquire                     | FEAT_LSFE |
|     01 |    1 |   1 |   0 | xxxxx |    0 |   110 | xxxxx | LDFMAXNM, LDFMAXNMA, LDFMAXNMAL, LDFMAXNML - Half-precision acquire            | FEAT_LSFE |
|     01 |    1 |   1 |   0 | xxxxx |    0 |   111 | xxxxx | LDFMINNM, LDFMINNMA, LDFMINNMAL, LDFMINNML - Half-precision acquire            | FEAT_LSFE |
|     01 |    1 |   1 |   1 | xxxxx |    0 |   000 | xxxxx | LDFADD, LDFADDA, LDFADDAL, LDFADDL - Half-precision acquire- release           | FEAT_LSFE |

| size   |   VR |   A | R   | Rs    |   o3 | opc   | Rt    | Instruction Details                                                         | Feature   |
|--------|------|-----|-----|-------|------|-------|-------|-----------------------------------------------------------------------------|-----------|
| 01     |    1 |   1 | 1   | xxxxx |    0 | 100   | xxxxx | LDFMAX, LDFMAXA, LDFMAXAL, LDFMAXL - Half-precision acquire- release        | FEAT_LSFE |
| 01     |    1 |   1 | 1   | xxxxx |    0 | 101   | xxxxx | LDFMIN, LDFMINA, LDFMINAL, LDFMINL - Half-precision acquire- release        | FEAT_LSFE |
| 01     |    1 |   1 | 1   | xxxxx |    0 | 110   | xxxxx | LDFMAXNM, LDFMAXNMA, LDFMAXNMAL, LDFMAXNML - Half-precision acquire-release | FEAT_LSFE |
| 01     |    1 |   1 | 1   | xxxxx |    0 | 111   | xxxxx | LDFMINNM, LDFMINNMA, LDFMINNMAL, LDFMINNML - Half-precision acquire-release | FEAT_LSFE |
| 1x     |    0 |   1 | x   | xxxxx |    1 | x01   | xxxxx | UNALLOCATED                                                                 | -         |
| 1x     |    0 |   1 | x   | xxxxx |    1 | x1x   | xxxxx | UNALLOCATED                                                                 | -         |
| 10     |    0 |   0 | x   | xxxxx |    1 | x01   | xxxxx | UNALLOCATED                                                                 | -         |
| 10     |    0 |   0 | x   | xxxxx |    1 | 010   | xxxxx | UNALLOCATED                                                                 | -         |
| 10     |    0 |   0 | x   | xxxxx |    1 | 011   | xxxxx | UNALLOCATED                                                                 | -         |
| 10     |    0 |   0 | 0   | xxxxx |    0 | 000   | xxxxx | LDADD, LDADDA, LDADDAL, LDADDL-32-bit no memory ordering                    | FEAT_LSE  |
| 10     |    0 |   0 | 0   | xxxxx |    0 | 001   | xxxxx | LDCLR, LDCLRA, LDCLRAL, LDCLRL -32-bit no memory ordering                   | FEAT_LSE  |
| 10     |    0 |   0 | 0   | xxxxx |    0 | 010   | xxxxx | LDEOR, LDEORA, LDEORAL, LDEORL -32-bit no memory ordering                   | FEAT_LSE  |
| 10     |    0 |   0 | 0   | xxxxx |    0 | 011   | xxxxx | LDSET, LDSETA, LDSETAL, LDSETL -32-bit no memory ordering                   | FEAT_LSE  |
| 10     |    0 |   0 | 0   | xxxxx |    0 | 100   | xxxxx | LDSMAX, LDSMAXA, LDSMAXAL, LDSMAXL-32-bit no memory ordering                | FEAT_LSE  |
| 10     |    0 |   0 | 0   | xxxxx |    0 | 101   | xxxxx | LDSMIN, LDSMINA, LDSMINAL, LDSMINL -32-bit no memory ordering               | FEAT_LSE  |
| 10     |    0 |   0 | 0   | xxxxx |    0 | 110   | xxxxx | LDUMAX, LDUMAXA, LDUMAXAL, LDUMAXL-32-bitnomemoryordering                   | FEAT_LSE  |
| 10     |    0 |   0 | 0   | xxxxx |    0 | 111   | xxxxx | LDUMIN, LDUMINA, LDUMINAL, LDUMINL-32-bit no memory ordering                | FEAT_LSE  |
| 10     |    0 |   0 | 0   | xxxxx |    1 | 000   | xxxxx | SWP, SWPA, SWPAL, SWPL - 32-bit SWP                                         | FEAT_LSE  |
| 10     |    0 |   0 | 1   | xxxxx |    0 | 000   | xxxxx | LDADD, LDADDA, LDADDAL, LDADDL-32-bit release                               | FEAT_LSE  |
| 10     |    0 |   0 | 1   | xxxxx |    0 | 001   | xxxxx | LDCLR, LDCLRA, LDCLRAL, LDCLRL -32-bit release                              | FEAT_LSE  |
| 10     |    0 |   0 | 1   | xxxxx |    0 | 010   | xxxxx | LDEOR, LDEORA, LDEORAL, LDEORL -32-bit release                              | FEAT_LSE  |
| 10     |    0 |   0 | 1   | xxxxx |    0 | 011   | xxxxx | LDSET, LDSETA, LDSETAL, LDSETL -32-bit release                              | FEAT_LSE  |
| 10     |    0 |   0 | 1   | xxxxx |    0 | 100   | xxxxx | LDSMAX, LDSMAXA, LDSMAXAL, LDSMAXL-32-bit release                           | FEAT_LSE  |
| 10     |    0 |   0 | 1   | xxxxx |    0 | 101   | xxxxx | LDSMIN, LDSMINA, LDSMINAL, LDSMINL -32-bit release                          | FEAT_LSE  |
| 10     |    0 |   0 | 1   | xxxxx |    0 | 110   | xxxxx | LDUMAX, LDUMAXA, LDUMAXAL, LDUMAXL-32-bit release                           | FEAT_LSE  |

|   size |   VR |   A |   R | Rs    |   o3 |   opc | Rt    | Instruction Details                                                      | Feature    |
|--------|------|-----|-----|-------|------|-------|-------|--------------------------------------------------------------------------|------------|
|     10 |    0 |   0 |   1 | xxxxx |    0 |   111 | xxxxx | LDUMIN, LDUMINA, LDUMINAL, LDUMINL -32-bit release                       | FEAT_LSE   |
|     10 |    0 |   0 |   1 | xxxxx |    1 |   000 | xxxxx | SWP, SWPA, SWPAL, SWPL - 32-bit SWPL                                     | FEAT_LSE   |
|     10 |    0 |   1 |   0 | xxxxx |    0 |   000 | xxxxx | LDADD, LDADDA, LDADDAL, LDADDL-32-bit acquire                            | FEAT_LSE   |
|     10 |    0 |   1 |   0 | xxxxx |    0 |   001 | xxxxx | LDCLR, LDCLRA, LDCLRAL, LDCLRL -32-bit acquire                           | FEAT_LSE   |
|     10 |    0 |   1 |   0 | xxxxx |    0 |   010 | xxxxx | LDEOR, LDEORA, LDEORAL, LDEORL -32-bit acquire                           | FEAT_LSE   |
|     10 |    0 |   1 |   0 | xxxxx |    0 |   011 | xxxxx | LDSET, LDSETA, LDSETAL, LDSETL -32-bit acquire                           | FEAT_LSE   |
|     10 |    0 |   1 |   0 | xxxxx |    0 |   100 | xxxxx | LDSMAX, LDSMAXA, LDSMAXAL, LDSMAXL-32-bit acquire                        | FEAT_LSE   |
|     10 |    0 |   1 |   0 | xxxxx |    0 |   101 | xxxxx | LDSMIN, LDSMINA, LDSMINAL, LDSMINL -32-bit acquire                       | FEAT_LSE   |
|     10 |    0 |   1 |   0 | xxxxx |    0 |   110 | xxxxx | LDUMAX, LDUMAXA, LDUMAXAL, LDUMAXL-32-bit acquire                        | FEAT_LSE   |
|     10 |    0 |   1 |   0 | xxxxx |    0 |   111 | xxxxx | LDUMIN, LDUMINA, LDUMINAL, LDUMINL -32-bit acquire                       | FEAT_LSE   |
|     10 |    0 |   1 |   0 | xxxxx |    1 |   000 | xxxxx | SWP, SWPA, SWPAL, SWPL - 32-bit SWPA                                     | FEAT_LSE   |
|     10 |    0 |   1 |   0 | xxxxx |    1 |   100 | xxxxx | LDAPR -32-bit                                                            | FEAT_LRCPC |
|     10 |    0 |   1 |   1 | xxxxx |    0 |   000 | xxxxx | LDADD, LDADDA, LDADDAL, LDADDL-32-bit acquire-release                    | FEAT_LSE   |
|     10 |    0 |   1 |   1 | xxxxx |    0 |   001 | xxxxx | LDCLR, LDCLRA, LDCLRAL, LDCLRL - 32-bit acquire-release                  | FEAT_LSE   |
|     10 |    0 |   1 |   1 | xxxxx |    0 |   010 | xxxxx | LDEOR, LDEORA, LDEORAL, LDEORL - 32-bit acquire-release                  | FEAT_LSE   |
|     10 |    0 |   1 |   1 | xxxxx |    0 |   011 | xxxxx | LDSET, LDSETA, LDSETAL, LDSETL -32-bit acquire-release                   | FEAT_LSE   |
|     10 |    0 |   1 |   1 | xxxxx |    0 |   100 | xxxxx | LDSMAX, LDSMAXA, LDSMAXAL, LDSMAXL-32-bit acquire-release                | FEAT_LSE   |
|     10 |    0 |   1 |   1 | xxxxx |    0 |   101 | xxxxx | LDSMIN, LDSMINA, LDSMINAL, LDSMINL -32-bit acquire-release               | FEAT_LSE   |
|     10 |    0 |   1 |   1 | xxxxx |    0 |   110 | xxxxx | LDUMAX, LDUMAXA, LDUMAXAL, LDUMAXL-32-bit acquire-release                | FEAT_LSE   |
|     10 |    0 |   1 |   1 | xxxxx |    0 |   111 | xxxxx | LDUMIN, LDUMINA, LDUMINAL, LDUMINL -32-bit acquire-release               | FEAT_LSE   |
|     10 |    0 |   1 |   1 | xxxxx |    1 |   000 | xxxxx | SWP, SWPA, SWPAL, SWPL - 32-bit SWPAL                                    | FEAT_LSE   |
|     10 |    1 |   0 |   0 | xxxxx |    0 |   000 | xxxxx | LDFADD, LDFADDA, LDFADDAL, LDFADDL - Single-precision no memory ordering | FEAT_LSFE  |
|     10 |    1 |   0 |   0 | xxxxx |    0 |   100 | xxxxx | LDFMAX, LDFMAXA, LDFMAXAL, LDFMAXL - Single-precision no memory ordering | FEAT_LSFE  |

|   size |   VR |   A |   R | Rs    |   o3 | opc       | Rt                                                                               | Instruction Details Feature   |
|--------|------|-----|-----|-------|------|-----------|----------------------------------------------------------------------------------|-------------------------------|
|     10 |    1 |   0 |   0 | xxxxx |    0 | 101 xxxxx | LDFMIN, LDFMINA, LDFMINAL, LDFMINL - Single-precision no memory ordering         | FEAT_LSFE                     |
|     10 |    1 |   0 |   0 | xxxxx |    0 | 110 xxxxx | LDFMAXNM, LDFMAXNMA, LDFMAXNMAL, LDFMAXNML - Single-precision no memory ordering | FEAT_LSFE                     |
|     10 |    1 |   0 |   0 | xxxxx |    0 | 111 xxxxx | LDFMINNM, LDFMINNMA, LDFMINNMAL, LDFMINNML - Single-precision no memory ordering | FEAT_LSFE                     |
|     10 |    1 |   0 |   0 | xxxxx |    1 | 000 11111 | STFADD, STFADDL -Single-precision no memory ordering                             | FEAT_LSFE                     |
|     10 |    1 |   0 |   0 | xxxxx |    1 | 100 11111 | STFMAX, STFMAXL - Single- precision no memory ordering                           | FEAT_LSFE                     |
|     10 |    1 |   0 |   0 | xxxxx |    1 | 101 11111 | STFMIN, STFMINL - Single-precision no memory ordering                            | FEAT_LSFE                     |
|     10 |    1 |   0 |   0 | xxxxx |    1 | 110 11111 | STFMAXNM, STFMAXNML -Single- precision no memory ordering                        | FEAT_LSFE                     |
|     10 |    1 |   0 |   0 | xxxxx |    1 | 111 11111 | STFMINNM, STFMINNML - Single- precision no memory ordering                       | FEAT_LSFE                     |
|     10 |    1 |   0 |   1 | xxxxx |    0 | 000 xxxxx | LDFADD, LDFADDA, LDFADDAL, LDFADDL -Single-precision release                     | FEAT_LSFE                     |
|     10 |    1 |   0 |   1 | xxxxx |    0 | 100 xxxxx | LDFMAX, LDFMAXA, LDFMAXAL, LDFMAXL-Single-precision release                      | FEAT_LSFE                     |
|     10 |    1 |   0 |   1 | xxxxx |    0 | 101 xxxxx | LDFMIN, LDFMINA, LDFMINAL, LDFMINL -Single-precision release                     | FEAT_LSFE                     |
|     10 |    1 |   0 |   1 | xxxxx |    0 | 110 xxxxx | LDFMAXNM, LDFMAXNMA, LDFMAXNMAL, LDFMAXNML - Single-precision release            | FEAT_LSFE                     |
|     10 |    1 |   0 |   1 | xxxxx |    0 | 111 xxxxx | LDFMINNM, LDFMINNMA, LDFMINNMAL, LDFMINNML - Single-precision release            | FEAT_LSFE                     |
|     10 |    1 |   0 |   1 | xxxxx |    1 | 000 11111 | STFADD, STFADDL -Single-precision release                                        | FEAT_LSFE                     |
|     10 |    1 |   0 |   1 | xxxxx |    1 | 100 11111 | STFMAX, STFMAXL - Single- precision release                                      | FEAT_LSFE                     |
|     10 |    1 |   0 |   1 | xxxxx |    1 | 101 11111 | STFMIN, STFMINL - Single-precision release                                       | FEAT_LSFE                     |
|     10 |    1 |   0 |   1 | xxxxx |    1 | 110 11111 | STFMAXNM, STFMAXNML -Single- precision release                                   | FEAT_LSFE                     |
|     10 |    1 |   0 |   1 | xxxxx |    1 | 111 11111 | STFMINNM, STFMINNML - Single- precision release                                  | FEAT_LSFE                     |
|     10 |    1 |   1 |   0 | xxxxx |    0 | 000 xxxxx | LDFADD, LDFADDA, LDFADDAL, LDFADDL -Single-precision acquire                     | FEAT_LSFE                     |
|     10 |    1 |   1 |   0 | xxxxx |    0 | 100 xxxxx | LDFMAX, LDFMAXA, LDFMAXAL, LDFMAXL-Single-precision acquire                      | FEAT_LSFE                     |
|     10 |    1 |   1 |   0 | xxxxx |    0 | 101 xxxxx | LDFMIN, LDFMINA, LDFMINAL, LDFMINL -Single-precision acquire                     | FEAT_LSFE                     |
|     10 |    1 |   1 |   0 | xxxxx |    0 | 110 xxxxx | LDFMAXNM, LDFMAXNMA, LDFMAXNMAL, LDFMAXNML - Single-precision acquire            | FEAT_LSFE                     |

|   size |   VR |   A |   R | Rs       |   o3 | opc   | Rt    | Instruction Details                                                           | Feature           |
|--------|------|-----|-----|----------|------|-------|-------|-------------------------------------------------------------------------------|-------------------|
|     10 |    1 |   1 |   0 | xxxxx    |    0 | 111   | xxxxx | LDFMINNM, LDFMINNMA, LDFMINNMAL, LDFMINNML - Single-precision acquire         | FEAT_LSFE         |
|     10 |    1 |   1 |   1 | xxxxx    |    0 | 000   | xxxxx | LDFADD, LDFADDA, LDFADDAL, LDFADDL - Single-precision acquire-release         | FEAT_LSFE         |
|     10 |    1 |   1 |   1 | xxxxx    |    0 | 100   | xxxxx | LDFMAX, LDFMAXA, LDFMAXAL, LDFMAXL - Single-precision acquire- release        | FEAT_LSFE         |
|     10 |    1 |   1 |   1 | xxxxx    |    0 | 101   | xxxxx | LDFMIN, LDFMINA, LDFMINAL, LDFMINL - Single-precision acquire-release         | FEAT_LSFE         |
|     10 |    1 |   1 |   1 | xxxxx    |    0 | 110   | xxxxx | LDFMAXNM, LDFMAXNMA, LDFMAXNMAL, LDFMAXNML - Single-precision acquire-release | FEAT_LSFE         |
|     10 |    1 |   1 |   1 | xxxxx    |    0 | 111   | xxxxx | LDFMINNM, LDFMINNMA, LDFMINNMAL, LDFMINNML - Single-precision acquire-release | FEAT_LSFE         |
|     11 |    0 |   0 |   0 | xxxxx    |    0 | 000   | xxxxx | LDADD, LDADDA, LDADDAL, LDADDL-64-bit no memory ordering                      | FEAT_LSE          |
|     11 |    0 |   0 |   0 | xxxxx    |    0 | 001   | xxxxx | LDCLR, LDCLRA, LDCLRAL, LDCLRL -64-bit no memory ordering                     | FEAT_LSE          |
|     11 |    0 |   0 |   0 | xxxxx    |    0 | 010   | xxxxx | LDEOR, LDEORA, LDEORAL, LDEORL -64-bit no memory ordering                     | FEAT_LSE          |
|     11 |    0 |   0 |   0 | xxxxx    |    0 | 011   | xxxxx | LDSET, LDSETA, LDSETAL, LDSETL -64-bit no memory ordering                     | FEAT_LSE          |
|     11 |    0 |   0 |   0 | xxxxx    |    0 | 100   | xxxxx | LDSMAX, LDSMAXA, LDSMAXAL, LDSMAXL-64-bit no memory ordering                  | FEAT_LSE          |
|     11 |    0 |   0 |   0 | xxxxx    |    0 | 101   | xxxxx | LDSMIN, LDSMINA, LDSMINAL, LDSMINL -64-bit no memory ordering                 | FEAT_LSE          |
|     11 |    0 |   0 |   0 | xxxxx    |    0 | 110   | xxxxx | LDUMAX, LDUMAXA, LDUMAXAL, LDUMAXL-64-bitnomemoryordering                     | FEAT_LSE          |
|     11 |    0 |   0 |   0 | xxxxx    |    0 | 111   | xxxxx | LDUMIN, LDUMINA, LDUMINAL, LDUMINL-64-bit no memory ordering                  | FEAT_LSE          |
|     11 |    0 |   0 |   0 | xxxxx    |    1 | 000   | xxxxx | SWP, SWPA, SWPAL, SWPL - 64-bit SWP                                           | FEAT_LSE          |
|     11 |    0 |   0 |   0 | xxxxx    |    1 | 010   | xxxxx | ST64BV0                                                                       | FEAT_LS64_ACCDATA |
|     11 |    0 |   0 |   0 | xxxxx    |    1 | 011   | xxxxx | ST64BV                                                                        | FEAT_LS64_V       |
|     11 |    0 |   0 |   0 | 11111    |    1 | 001   | xxxxx | ST64B                                                                         | FEAT_LS64         |
|     11 |    0 |   0 |   0 | 11111    |    1 | 101   | xxxxx | LD64B                                                                         | FEAT_LS64         |
|     11 |    0 |   0 |   0 | != 11111 |    1 | x01   | xxxxx | UNALLOCATED                                                                   | -                 |
|     11 |    0 |   0 |   1 | xxxxx    |    0 | 000   | xxxxx | LDADD, LDADDA, LDADDAL, LDADDL-64-bit release                                 | FEAT_LSE          |
|     11 |    0 |   0 |   1 | xxxxx    |    0 | 001   | xxxxx | LDCLR, LDCLRA, LDCLRAL, LDCLRL -64-bit release                                | FEAT_LSE          |
|     11 |    0 |   0 |   1 | xxxxx    |    0 | 010   | xxxxx | LDEOR, LDEORA, LDEORAL, LDEORL -64-bit release                                | FEAT_LSE          |

|   size |   VR |   A |   R | Rs    |   o3 | opc   | Rt    | Instruction Details                                        | Feature    |
|--------|------|-----|-----|-------|------|-------|-------|------------------------------------------------------------|------------|
|     11 |    0 |   0 |   1 | xxxxx |    0 | 011   | xxxxx | LDSET, LDSETA, LDSETAL, LDSETL -64-bit release             | FEAT_LSE   |
|     11 |    0 |   0 |   1 | xxxxx |    0 | 100   | xxxxx | LDSMAX, LDSMAXA, LDSMAXAL, LDSMAXL-64-bit release          | FEAT_LSE   |
|     11 |    0 |   0 |   1 | xxxxx |    0 | 101   | xxxxx | LDSMIN, LDSMINA, LDSMINAL, LDSMINL -64-bit release         | FEAT_LSE   |
|     11 |    0 |   0 |   1 | xxxxx |    0 | 110   | xxxxx | LDUMAX, LDUMAXA, LDUMAXAL, LDUMAXL-64-bit release          | FEAT_LSE   |
|     11 |    0 |   0 |   1 | xxxxx |    0 | 111   | xxxxx | LDUMIN, LDUMINA, LDUMINAL, LDUMINL -64-bit release         | FEAT_LSE   |
|     11 |    0 |   0 |   1 | xxxxx |    1 | x01   | xxxxx | UNALLOCATED                                                | -          |
|     11 |    0 |   0 |   1 | xxxxx |    1 | 000   | xxxxx | SWP, SWPA, SWPAL, SWPL - 64-bit SWPL                       | FEAT_LSE   |
|     11 |    0 |   0 |   1 | xxxxx |    1 | 010   | xxxxx | UNALLOCATED                                                | -          |
|     11 |    0 |   0 |   1 | xxxxx |    1 | 011   | xxxxx | UNALLOCATED                                                | -          |
|     11 |    0 |   1 |   0 | xxxxx |    0 | 000   | xxxxx | LDADD, LDADDA, LDADDAL, LDADDL-64-bit acquire              | FEAT_LSE   |
|     11 |    0 |   1 |   0 | xxxxx |    0 | 001   | xxxxx | LDCLR, LDCLRA, LDCLRAL, LDCLRL -64-bit acquire             | FEAT_LSE   |
|     11 |    0 |   1 |   0 | xxxxx |    0 | 010   | xxxxx | LDEOR, LDEORA, LDEORAL, LDEORL -64-bit acquire             | FEAT_LSE   |
|     11 |    0 |   1 |   0 | xxxxx |    0 | 011   | xxxxx | LDSET, LDSETA, LDSETAL, LDSETL -64-bit acquire             | FEAT_LSE   |
|     11 |    0 |   1 |   0 | xxxxx |    0 | 100   | xxxxx | LDSMAX, LDSMAXA, LDSMAXAL, LDSMAXL-64-bit acquire          | FEAT_LSE   |
|     11 |    0 |   1 |   0 | xxxxx |    0 | 101   | xxxxx | LDSMIN, LDSMINA, LDSMINAL, LDSMINL -64-bit acquire         | FEAT_LSE   |
|     11 |    0 |   1 |   0 | xxxxx |    0 | 110   | xxxxx | LDUMAX, LDUMAXA, LDUMAXAL, LDUMAXL-64-bit acquire          | FEAT_LSE   |
|     11 |    0 |   1 |   0 | xxxxx |    0 | 111   | xxxxx | LDUMIN, LDUMINA, LDUMINAL, LDUMINL -64-bit acquire         | FEAT_LSE   |
|     11 |    0 |   1 |   0 | xxxxx |    1 | 000   | xxxxx | SWP, SWPA, SWPAL, SWPL - 64-bit SWPA                       | FEAT_LSE   |
|     11 |    0 |   1 |   0 | xxxxx |    1 | 100   | xxxxx | LDAPR -64-bit                                              | FEAT_LRCPC |
|     11 |    0 |   1 |   1 | xxxxx |    0 | 000   | xxxxx | LDADD, LDADDA, LDADDAL, LDADDL-64-bit acquire-release      | FEAT_LSE   |
|     11 |    0 |   1 |   1 | xxxxx |    0 | 001   | xxxxx | LDCLR, LDCLRA, LDCLRAL, LDCLRL - 64-bit acquire-release    | FEAT_LSE   |
|     11 |    0 |   1 |   1 | xxxxx |    0 | 010   | xxxxx | LDEOR, LDEORA, LDEORAL, LDEORL - 64-bit acquire-release    | FEAT_LSE   |
|     11 |    0 |   1 |   1 | xxxxx |    0 | 011   | xxxxx | LDSET, LDSETA, LDSETAL, LDSETL -64-bit acquire-release     | FEAT_LSE   |
|     11 |    0 |   1 |   1 | xxxxx |    0 | 100   | xxxxx | LDSMAX, LDSMAXA, LDSMAXAL, LDSMAXL-64-bit acquire-release  | FEAT_LSE   |
|     11 |    0 |   1 |   1 | xxxxx |    0 | 101   | xxxxx | LDSMIN, LDSMINA, LDSMINAL, LDSMINL -64-bit acquire-release | FEAT_LSE   |
|     11 |    0 |   1 |   1 | xxxxx |    0 | 110   | xxxxx | LDUMAX, LDUMAXA, LDUMAXAL, LDUMAXL-64-bit acquire-release  | FEAT_LSE   |

|   size |   VR |   A |   R | Rs    |   o3 |   opc | Rt    | Instruction Details                                                              | Feature   |
|--------|------|-----|-----|-------|------|-------|-------|----------------------------------------------------------------------------------|-----------|
|     11 |    0 |   1 |   1 | xxxxx |    0 |   111 | xxxxx | LDUMIN, LDUMINA, LDUMINAL, LDUMINL -64-bit acquire-release                       | FEAT_LSE  |
|     11 |    0 |   1 |   1 | xxxxx |    1 |   000 | xxxxx | SWP, SWPA, SWPAL, SWPL - 64-bit SWPAL                                            | FEAT_LSE  |
|     11 |    1 |   0 |   0 | xxxxx |    0 |   000 | xxxxx | LDFADD, LDFADDA, LDFADDAL, LDFADDL - Double-precision no memory ordering         | FEAT_LSFE |
|     11 |    1 |   0 |   0 | xxxxx |    0 |   100 | xxxxx | LDFMAX, LDFMAXA, LDFMAXAL, LDFMAXL - Double-precision no memory ordering         | FEAT_LSFE |
|     11 |    1 |   0 |   0 | xxxxx |    0 |   101 | xxxxx | LDFMIN, LDFMINA, LDFMINAL, LDFMINL - Double-precision no memory ordering         | FEAT_LSFE |
|     11 |    1 |   0 |   0 | xxxxx |    0 |   110 | xxxxx | LDFMAXNM, LDFMAXNMA, LDFMAXNMAL, LDFMAXNML - Double-precision no memory ordering | FEAT_LSFE |
|     11 |    1 |   0 |   0 | xxxxx |    0 |   111 | xxxxx | LDFMINNM, LDFMINNMA, LDFMINNMAL, LDFMINNML - Double-precision no memory ordering | FEAT_LSFE |
|     11 |    1 |   0 |   0 | xxxxx |    1 |   000 | 11111 | STFADD, STFADDL-Double-precision no memory ordering                              | FEAT_LSFE |
|     11 |    1 |   0 |   0 | xxxxx |    1 |   100 | 11111 | STFMAX, STFMAXL - Double- precision no memory ordering                           | FEAT_LSFE |
|     11 |    1 |   0 |   0 | xxxxx |    1 |   101 | 11111 | STFMIN, STFMINL -Double-precision no memory ordering                             | FEAT_LSFE |
|     11 |    1 |   0 |   0 | xxxxx |    1 |   110 | 11111 | STFMAXNM,STFMAXNML-Double- precision no memory ordering                          | FEAT_LSFE |
|     11 |    1 |   0 |   0 | xxxxx |    1 |   111 | 11111 | STFMINNM, STFMINNML - Double- precision no memory ordering                       | FEAT_LSFE |
|     11 |    1 |   0 |   1 | xxxxx |    0 |   000 | xxxxx | LDFADD, LDFADDA, LDFADDAL, LDFADDL -Double-precision release                     | FEAT_LSFE |
|     11 |    1 |   0 |   1 | xxxxx |    0 |   100 | xxxxx | LDFMAX, LDFMAXA, LDFMAXAL, LDFMAXL-Double-precision release                      | FEAT_LSFE |
|     11 |    1 |   0 |   1 | xxxxx |    0 |   101 | xxxxx | LDFMIN, LDFMINA, LDFMINAL, LDFMINL -Double-precision release                     | FEAT_LSFE |
|     11 |    1 |   0 |   1 | xxxxx |    0 |   110 | xxxxx | LDFMAXNM, LDFMAXNMA, LDFMAXNMAL, LDFMAXNML - Double-precision release            | FEAT_LSFE |
|     11 |    1 |   0 |   1 | xxxxx |    0 |   111 | xxxxx | LDFMINNM, LDFMINNMA, LDFMINNMAL, LDFMINNML - Double-precision release            | FEAT_LSFE |
|     11 |    1 |   0 |   1 | xxxxx |    1 |   000 | 11111 | STFADD, STFADDL-Double-precision release                                         | FEAT_LSFE |
|     11 |    1 |   0 |   1 | xxxxx |    1 |   100 | 11111 | STFMAX, STFMAXL - Double- precision release                                      | FEAT_LSFE |
|     11 |    1 |   0 |   1 | xxxxx |    1 |   101 | 11111 | STFMIN, STFMINL -Double-precision release                                        | FEAT_LSFE |
|     11 |    1 |   0 |   1 | xxxxx |    1 |   110 | 11111 | STFMAXNM,STFMAXNML-Double- precision release                                     | FEAT_LSFE |
|     11 |    1 |   0 |   1 | xxxxx |    1 |   111 | 11111 | STFMINNM, STFMINNML - Double- precision release                                  | FEAT_LSFE |

|   size |   VR |   A | R   | Rs      |   o3 |   opc | Rt    | Instruction Details                                                           | Feature   |
|--------|------|-----|-----|---------|------|-------|-------|-------------------------------------------------------------------------------|-----------|
|     11 |    1 |   1 | 0   | xxxxx   |    0 |   000 | xxxxx | LDFADD, LDFADDA, LDFADDAL, LDFADDL -Double-precision acquire                  | FEAT_LSFE |
|     11 |    1 |   1 | 0   | xxxxx   |    0 |   100 | xxxxx | LDFMAX, LDFMAXA, LDFMAXAL, LDFMAXL-Double-precision acquire                   | FEAT_LSFE |
|     11 |    1 |   1 | 0   | xxxxx   |    0 |   101 | xxxxx | LDFMIN, LDFMINA, LDFMINAL, LDFMINL -Double-precision acquire                  | FEAT_LSFE |
|     11 |    1 |   1 | 0   | xxxxx   |    0 |   110 | xxxxx | LDFMAXNM, LDFMAXNMA, LDFMAXNMAL, LDFMAXNML - Double-precision acquire         | FEAT_LSFE |
|     11 |    1 |   1 | 0   | xxxxx   |    0 |   111 | xxxxx | LDFMINNM, LDFMINNMA, LDFMINNMAL, LDFMINNML - Double-precision acquire         | FEAT_LSFE |
|     11 |    1 |   1 | 1   | xxxxx   |    0 |   000 | xxxxx | LDFADD, LDFADDA, LDFADDAL, LDFADDL - Double-precision acquire-release         | FEAT_LSFE |
|     11 |    1 |   1 | 1   | xxxxx   |    0 |   100 | xxxxx | LDFMAX, LDFMAXA, LDFMAXAL, LDFMAXL -Double-precision acquire- release         | FEAT_LSFE |
|     11 |    1 |   1 | 1   | xxxxx   |    0 |   101 | xxxxx | LDFMIN, LDFMINA, LDFMINAL, LDFMINL - Double-precision acquire-release         | FEAT_LSFE |
|     11 |    1 |   1 | 1   | xxxxx   |    0 |   110 | xxxxx | LDFMAXNM, LDFMAXNMA, LDFMAXNMAL, LDFMAXNML - Double-precision acquire-release | FEAT_LSFE |
|     11 |    1 |   1 |     | 1 xxxxx |    0 |   111 | xxxxx | LDFMINNM, LDFMINNMA, LDFMINNMAL, LDFMINNML - Double-precision acquire-release | FEAT_LSFE |

## Load/store register (register offset)

The encodings in this section are decoded from Loads and Stores.

<!-- image -->

| 31 30   | 29 27    | 26 25 24   | 23   | 22   |   21 |    | 15     | 12 11 10   | 5 4   | 0   |
|---------|----------|------------|------|------|------|----|--------|------------|-------|-----|
| size    | 1 1 1 VR | 0 0        |      | opc  |    1 | Rm | option | S 1 0      | Rn    | Rt  |

|   size |   VR |   opc | option   | Rt    | Instruction Details                                    | Feature   |
|--------|------|-------|----------|-------|--------------------------------------------------------|-----------|
|     00 |    0 |    00 | 011      | xxxxx | STRB (register) -Shifted register                      | -         |
|     00 |    0 |    00 | != 011   | xxxxx | STRB (register) -Extended register                     | -         |
|     00 |    0 |    01 | 011      | xxxxx | LDRB(register) -Shifted register                       | -         |
|     00 |    0 |    01 | != 011   | xxxxx | LDRB(register) -Extended register                      | -         |
|     00 |    0 |    10 | 011      | xxxxx | LDRSB (register) - 64-bit with shifted register offset | -         |
|     00 |    0 |    10 | != 011   | xxxxx | LDRSB (register) -64-bit with extended register offset | -         |

| size   |   VR | opc   | option   | Rt       | Instruction Details                                           | Feature    |
|--------|------|-------|----------|----------|---------------------------------------------------------------|------------|
| 00     |    0 | 11    | 011      | xxxxx    | LDRSB (register) - 32-bit with shifted register offset        | -          |
| 00     |    0 | 11    | != 011   | xxxxx    | LDRSB (register) -32-bit with extended register offset        | -          |
| 00     |    1 | 00    | 011      | xxxxx    | STR (register, SIMD&FP) - 8-bit with shifted register offset  | FEAT_FP    |
| 00     |    1 | 00    | != 011   | xxxxx    | STR (register, SIMD&FP) - 8-bit with extended register offset | FEAT_FP    |
| 00     |    1 | 01    | 011      | xxxxx    | LDR (register, SIMD&FP) - 8-bit with shifted register offset  | FEAT_FP    |
| 00     |    1 | 01    | != 011   | xxxxx    | LDR (register, SIMD&FP) - 8-bit with extended register offset | FEAT_FP    |
| 00     |    1 | 10    | xxx      | xxxxx    | STR (register, SIMD&FP) -128-bit                              | FEAT_FP    |
| 00     |    1 | 11    | xxx      | xxxxx    | LDR(register, SIMD&FP) -128-bit                               | FEAT_FP    |
| 01     |    0 | 00    | xxx      | xxxxx    | STRH (register)                                               | -          |
| 01     |    0 | 01    | xxx      | xxxxx    | LDRH(register)                                                | -          |
| 01     |    0 | 10    | xxx      | xxxxx    | LDRSH (register) -64-bit                                      | -          |
| 01     |    0 | 11    | xxx      | xxxxx    | LDRSH (register) -32-bit                                      | -          |
| 01     |    1 | 00    | xxx      | xxxxx    | STR (register, SIMD&FP) -16-bit                               | FEAT_FP    |
| 01     |    1 | 01    | xxx      | xxxxx    | LDR(register, SIMD&FP) -16-bit                                | FEAT_FP    |
| 1x     |    0 | 11    | xxx      | xxxxx    | UNALLOCATED                                                   | -          |
| 10     |    0 | 00    | xxx      | xxxxx    | STR (register) -32-bit                                        | -          |
| 10     |    0 | 01    | xxx      | xxxxx    | LDR(register) -32-bit                                         | -          |
| 10     |    0 | 10    | xxx      | xxxxx    | LDRSW(register)                                               | -          |
| 10     |    1 | 00    | xxx      | xxxxx    | STR (register, SIMD&FP) -32-bit                               | FEAT_FP    |
| 10     |    1 | 01    | xxx      | xxxxx    | LDR(register, SIMD&FP) -32-bit                                | FEAT_FP    |
| 11     |    0 | 00    | xxx      | xxxxx    | STR (register) -64-bit                                        | -          |
| 11     |    0 | 01    | xxx      | xxxxx    | LDR(register) -64-bit                                         | -          |
| 11     |    0 | 10    | x0x      | xxxxx    | UNALLOCATED                                                   | -          |
| 11     |    0 | 10    | x1x      | 11xxx    | RPRFM                                                         | FEAT_RPRFM |
| 11     |    0 | 10    | x1x      | != 11xxx | PRFM(register)                                                | -          |
| 11     |    1 | 00    | xxx      | xxxxx    | STR (register, SIMD&FP) -64-bit                               | FEAT_FP    |
| 11     |    1 | 01    | xxx      | xxxxx    | LDR(register, SIMD&FP) -64-bit                                | FEAT_FP    |
| != 00  |    1 | 1x    | xxx      | xxxxx    | UNALLOCATED                                                   | -          |

## Load/store register (pac)

The encodings in this section are decoded from Loads and Stores.

| 31 30   | 29 27 26 25             | 24 23 22 21 20 12 11 10   |
|---------|-------------------------|---------------------------|
| size    | 1 1 1 VR 0 0 M S 1 imm9 | W 1                       |

| size   | VR   | M   | W   | Instruction Details           | Feature    |
|--------|------|-----|-----|-------------------------------|------------|
| 11     | 0    | 0   | 0   | LDRAA, LDRAB-KeyA,offset      | FEAT_PAuth |
| 11     | 0    | 0   | 1   | LDRAA, LDRAB-KeyA,pre-indexed | FEAT_PAuth |
| 11     | 0    | 1   | 0   | LDRAA, LDRAB-KeyB,offset      | FEAT_PAuth |
| 11     | 0    | 1   | 1   | LDRAA, LDRAB-KeyB,pre-indexed | FEAT_PAuth |
| 11     | 1    | x   | x   | UNALLOCATED                   | -          |
| != 11  | x    | x   | x   | UNALLOCATED                   | -          |

## Load/store register (unsigned immediate)

The encodings in this section are decoded from Loads and Stores.

<!-- image -->

| 31   |   30 29 | 27 26 25 24 23 22   | 9   | 5 4   |
|------|---------|---------------------|-----|-------|
| size |       1 | 1 1 VR 0 1 opc      | Rn  | Rt    |

| size   |   VR |   opc | Instruction Details               | Feature   |
|--------|------|-------|-----------------------------------|-----------|
| 00     |    0 |    00 | STRB (immediate)                  | -         |
| 00     |    0 |    01 | LDRB(immediate)                   | -         |
| 00     |    0 |    10 | LDRSB (immediate) -64-bit         | -         |
| 00     |    0 |    11 | LDRSB (immediate) -32-bit         | -         |
| 00     |    1 |    00 | STR (immediate, SIMD&FP) -8-bit   | FEAT_FP   |
| 00     |    1 |    01 | LDR(immediate, SIMD&FP) -8-bit    | FEAT_FP   |
| 00     |    1 |    10 | STR (immediate, SIMD&FP) -128-bit | FEAT_FP   |
| 00     |    1 |    11 | LDR(immediate, SIMD&FP) -128-bit  | FEAT_FP   |
| 01     |    0 |    00 | STRH (immediate)                  | -         |
| 01     |    0 |    01 | LDRH(immediate)                   | -         |
| 01     |    0 |    10 | LDRSH (immediate) -64-bit         | -         |
| 01     |    0 |    11 | LDRSH (immediate) -32-bit         | -         |
| 01     |    1 |    00 | STR (immediate, SIMD&FP) -16-bit  | FEAT_FP   |
| 01     |    1 |    01 | LDR(immediate, SIMD&FP) -16-bit   | FEAT_FP   |
| 1x     |    0 |    11 | UNALLOCATED                       | -         |
| 10     |    0 |    00 | STR (immediate) -32-bit           | -         |
| 10     |    0 |    01 | LDR(immediate) -32-bit            | -         |
| 10     |    0 |    10 | LDRSW(immediate)                  | -         |
| 10     |    1 |    00 | STR (immediate, SIMD&FP) -32-bit  | FEAT_FP   |
| 10     |    1 |    01 | LDR(immediate, SIMD&FP) -32-bit   | FEAT_FP   |

| size   |   VR | opc   | Instruction Details              | Feature   |
|--------|------|-------|----------------------------------|-----------|
| 11     |    0 | 00    | STR (immediate) -64-bit          | -         |
| 11     |    0 | 01    | LDR(immediate) -64-bit           | -         |
| 11     |    0 | 10    | PRFM(immediate)                  | -         |
| 11     |    1 | 00    | STR (immediate, SIMD&FP) -64-bit | FEAT_FP   |
| 11     |    1 | 01    | LDR(immediate, SIMD&FP) -64-bit  | FEAT_FP   |
| != 00  |    1 | 1x    | UNALLOCATED                      | -         |

## Chapter C5 The A64 System Instruction Class

This chapter describes the A64 System instruction class, and the System instruction class encoding space, that is a subset of the System registers encoding space. It contains the following sections:

- The System instruction class encoding space.
- Special purpose registers.
- A64 System instructions for cache maintenance.
- A64 System instructions for address translation.
- A64 System instructions for TLB maintenance.
- A64 System instructions for prediction restriction.
- A64 System instructions for the Branch Record Buffer Extension.
- A64 System instructions for the Trace Extension.
- A64 System instructions for the Guarded Control Stack.
- A64 IMPLEMENTATION DEFINED System instructions.

See General information about the A64 instruction descriptions for information about entries used in the instruction encoding descriptions.